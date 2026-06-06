#!/usr/bin/env python3
"""Phase 7-11 deep corpus analysis: trigrams, titles, per-beat, channel diff, refrains."""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

SOURCE = Path(__file__).parent
TRANS_DIR = SOURCE / "transcripts"

GE_STOP = set("და მე შენ ის ჩვენ თქვენ ისინი არის იყო იქნება ერთი ორი სამი ერთხელ რომ რომელიც ვინც რაც ეს ის ეგ ჩემი შენი მისი ჩვენი თქვენი მათი ჩემთან შენთან მისთან ვინ რა სად როდის როცა როგორ რატომ მაგრამ თუ კი არა ხო ჰო ნუ აი არ ან ხოლო ვერ ან მერე ისე ასე როდის როცა აქ იქ აქედან იქით ნუ ხან ხანდახან რომ ვითომ თითქოს უნდა მინდა გინდა გვინდა გინდათ უნდათ შემიძლია შეუძლია მქონდა მქონია ისე ბევრი ცოტა ცოტათი ცოტა მთლად ცოტას ხელით ფეხით ბევრად ცოტათი".split())

def words(text):
    return re.findall(r"[Ⴀ-ჿⴀ-⴯]+", text)

def sentences(text):
    text = re.sub(r"\[.*?\]|\(.*?\)", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"[.!?]+", text)
    return [p.strip() for p in parts if p.strip() and len(p.strip()) > 2]

def load_corpus():
    out = []
    for ch_dir in sorted(TRANS_DIR.iterdir()):
        if not ch_dir.is_dir():
            continue
        for json_path in sorted(ch_dir.glob("*.json")):
            d = json.loads(json_path.read_text(encoding="utf-8"))
            if d["lang"] != "ka":
                continue
            text = " ".join(s["text"] for s in d["snippets"])
            text_clean = re.sub(r"\[.*?\]|\(.*?\)", "", text)
            d["text_clean"] = text_clean
            d["channel"] = ch_dir.name
            d["sentences"] = sentences(text_clean)
            d["words"] = words(text_clean)
            d["duration_sec"] = d["snippets"][-1]["start"] + d["snippets"][-1]["duration"] if d["snippets"] else 0
            out.append(d)
    return out

def main():
    corpus = load_corpus()
    print(f"=== CORPUS LOADED: {len(corpus)} KA transcripts ===\n")

    # PHASE 7 — Trigrams + 4-grams
    print("=" * 60)
    print("PHASE 7 — TRIGRAMS + 4-GRAMS (stopword-filtered, len>=3)")
    print("=" * 60)
    trigrams = Counter()
    fourgrams = Counter()
    for t in corpus:
        ws = t["words"]
        for i in range(len(ws) - 2):
            a, b, c = ws[i], ws[i+1], ws[i+2]
            if any(w in GE_STOP for w in (a, b, c)):
                continue
            if any(len(w) < 3 for w in (a, b, c)):
                continue
            trigrams[(a, b, c)] += 1
        for i in range(len(ws) - 3):
            quad = ws[i:i+4]
            if sum(1 for w in quad if w in GE_STOP) > 1:
                continue
            if any(len(w) < 3 for w in quad):
                continue
            fourgrams[tuple(quad)] += 1

    print("\nTop 30 trigrams:")
    for (a, b, c), n in trigrams.most_common(30):
        print(f"  {n:3d}  {a} {b} {c}")

    print("\nTop 20 4-grams (≥2 occurrences):")
    for quad, n in fourgrams.most_common(20):
        if n < 2:
            break
        print(f"  {n:3d}  {' '.join(quad)}")

    # PHASE 8 — Title patterns from ch1.ids.txt + ch2.ids.txt
    print()
    print("=" * 60)
    print("PHASE 8 — TITLE PATTERNS (131 titles)")
    print("=" * 60)
    all_titles = []
    for fn in ("ch1.ids.txt", "ch2.ids.txt"):
        for line in (SOURCE / fn).read_text(encoding="utf-8").splitlines():
            if "|" in line:
                all_titles.append((fn[:3], line.split("|", 1)[1]))

    # Emoji prefix
    emoji_prefix = Counter()
    for ch, title in all_titles:
        m = re.match(r"^([\U0001F000-\U0001FFFF☀-➿✀-➿]+)", title)
        if m:
            emoji_prefix[m.group(1)] += 1
        else:
            emoji_prefix["(none)"] += 1

    print("\nEmoji prefix frequency (signals video type):")
    for e, n in emoji_prefix.most_common(15):
        print(f"  {n:3d}  '{e}'")

    # Title-first-word
    first_words = Counter()
    for ch, title in all_titles:
        title_clean = re.sub(r"^[\U0001F000-\U0001FFFF☀-➿✀-➿]+\s*", "", title)
        ws = words(title_clean)
        if ws:
            first_words[ws[0]] += 1

    print("\nTitle first content-word (top 20):")
    for w, n in first_words.most_common(20):
        print(f"  {n:3d}  {w}")

    # Title common bigrams
    title_bigrams = Counter()
    for ch, title in all_titles:
        ws = words(title)
        for i in range(len(ws) - 1):
            if ws[i] in GE_STOP or ws[i+1] in GE_STOP:
                continue
            if len(ws[i]) < 3 or len(ws[i+1]) < 3:
                continue
            title_bigrams[(ws[i], ws[i+1])] += 1

    print("\nTitle bigrams (top 15):")
    for (a, b), n in title_bigrams.most_common(15):
        print(f"  {n:3d}  {a} {b}")

    # PHASE 9 — Per-beat vocab split
    print()
    print("=" * 60)
    print("PHASE 9 — PER-BEAT VOCAB (split body into 5 equal parts)")
    print("=" * 60)
    beat_words = [Counter() for _ in range(5)]
    for t in corpus:
        ws = [w for w in t["words"] if w not in GE_STOP and len(w) >= 3]
        if len(ws) < 10:
            continue
        chunk = len(ws) // 5
        for i in range(5):
            start = i * chunk
            end = (i + 1) * chunk if i < 4 else len(ws)
            for w in ws[start:end]:
                beat_words[i][w] += 1

    beat_labels = ["B1 OPEN (0-20%)", "B2 SETUP (20-40%)", "B3 JOURNEY (40-60%)", "B4 RESOLVE (60-80%)", "B5 CLOSE (80-100%)"]
    for i, lbl in enumerate(beat_labels):
        print(f"\n{lbl} — top 12:")
        for w, n in beat_words[i].most_common(12):
            print(f"  {n:3d}  {w}")

    # Closer-only signature
    print("\nB5 CLOSING-only (words present in B5 but rare/absent in B1+B2):")
    early_words = set()
    for c in beat_words[:2]:
        early_words |= set(c.keys())
    closing_signature = []
    for w, n in beat_words[4].most_common(50):
        if w not in early_words and n >= 2:
            closing_signature.append((w, n))
    for w, n in closing_signature[:15]:
        print(f"  {n:3d}  {w}  (B5 only)")

    # PHASE 10 — Channel cross-diff
    print()
    print("=" * 60)
    print("PHASE 10 — CHANNEL CROSS-DIFF (ch1 sleep vs ch2 adventure)")
    print("=" * 60)
    ch1 = [t for t in corpus if t["channel"] == "ch1_dziliskhairi"]
    ch2 = [t for t in corpus if t["channel"] == "ch2_jirafijoze"]
    print(f"ch1 sleep: {len(ch1)} transcripts · ch2 jirafi: {len(ch2)} transcripts")

    def ch_words(ts):
        c = Counter()
        for t in ts:
            for w in t["words"]:
                if w not in GE_STOP and len(w) >= 3:
                    c[w] += 1
        return c

    c1 = ch_words(ch1)
    c2 = ch_words(ch2)
    total1 = sum(c1.values()) or 1
    total2 = sum(c2.values()) or 1

    # Words skewed to ch1
    print("\nch1-skewed (≥5 in ch1, freq ratio ≥3× ch2 OR absent in ch2):")
    ch1_only = []
    for w, n in c1.most_common(100):
        if n < 5:
            continue
        f1 = n / total1
        f2 = c2.get(w, 0) / total2
        if f2 == 0 or f1 / f2 >= 3.0:
            ch1_only.append((w, n, c2.get(w, 0)))
    for w, n1, n2 in ch1_only[:20]:
        print(f"  ch1={n1:3d}  ch2={n2:3d}  {w}")

    print("\nch2-skewed (≥3 in ch2, freq ratio ≥3× ch1 OR absent in ch1):")
    ch2_only = []
    for w, n in c2.most_common(100):
        if n < 3:
            continue
        f1 = c1.get(w, 0) / total1
        f2 = n / total2
        if f1 == 0 or f2 / f1 >= 3.0:
            ch2_only.append((w, n, c1.get(w, 0)))
    for w, n2, n1 in ch2_only[:20]:
        print(f"  ch2={n2:3d}  ch1={n1:3d}  {w}")

    # PHASE 11 — Refrains, repetition, onomatopoeia
    print()
    print("=" * 60)
    print("PHASE 11 — REFRAINS / REPETITION / ONOMATOPOEIA")
    print("=" * 60)

    # Detect immediate repetitions: same word repeated twice consecutively
    consec_repeat = Counter()
    for t in corpus:
        ws = t["words"]
        for i in range(len(ws) - 1):
            if ws[i] == ws[i+1] and len(ws[i]) >= 3:
                consec_repeat[ws[i]] += 1
    print("\nConsecutive word repetition (kid emphasis pattern):")
    for w, n in consec_repeat.most_common(15):
        print(f"  {n:3d}  {w} {w}")

    # Onomatopoeia / sound words (short repeated syllables / kid sounds)
    onomato = Counter()
    onomato_patterns = re.compile(r"[აეიოუ]?[ბგდვზთლმნპჟრსტფქღყშჩცძწჭხჯჰ]?[აეიოუ][ბგდვზთლმნპჟრსტფქღყშჩცძწჭხჯჰ]?[აეიოუ]?\b")
    short_words = Counter()
    for t in corpus:
        for w in t["words"]:
            if 2 <= len(w) <= 4:
                short_words[w] += 1

    # Look for kid-sound suspects
    suspects = ['უი', 'აი', 'ჰო', 'ჰეჰე', 'ცარცარ', 'ცარ', 'მუი', 'ნანი', 'ნანა', 'ბაი', 'შრრ', 'ჰმ', 'ცაც', 'ცუც', 'პუპუ', 'ბუბუ']
    print("\nKid sound-words / onomatopoeia (manual list):")
    for s in suspects:
        n = sum(t["text_clean"].count(s) for t in corpus)
        if n > 0:
            print(f"  {n:3d}  '{s}'")

    # Most common short words 2-4 chars (excluding stopwords)
    print("\nShort words 2-4 chars (top 15, non-stopword) — refrain candidates:")
    for w, n in short_words.most_common(40):
        if w in GE_STOP:
            continue
        if n >= 5:
            print(f"  {n:3d}  {w}")
            if n < 5:
                break

    # Question + exclamation density
    print("\nPunctuation density (per 1000 chars):")
    for t in corpus[:6]:
        c = len(t["text_clean"])
        if c == 0:
            continue
        q = t["text_clean"].count("?")
        e = t["text_clean"].count("!")
        print(f"  [{t['channel'][:5]}] {t['id'][:11]} q={q/c*1000:.2f} e={e/c*1000:.2f}")

    # Save deep analysis JSON
    out = {
        "top_trigrams": [{"phrase": " ".join(k), "count": v} for k, v in trigrams.most_common(50)],
        "top_4grams": [{"phrase": " ".join(k), "count": v} for k, v in fourgrams.most_common(30) if v >= 2],
        "emoji_prefix": dict(emoji_prefix.most_common(20)),
        "title_first_words": dict(first_words.most_common(30)),
        "title_bigrams": [{"phrase": f"{a} {b}", "count": v} for (a, b), v in title_bigrams.most_common(30)],
        "per_beat_top": {beat_labels[i]: dict(beat_words[i].most_common(20)) for i in range(5)},
        "closing_signature": [{"word": w, "count": n} for w, n in closing_signature[:20]],
        "ch1_skewed": [{"word": w, "ch1": n1, "ch2": n2} for w, n1, n2 in ch1_only],
        "ch2_skewed": [{"word": w, "ch2": n2, "ch1": n1} for w, n2, n1 in ch2_only],
        "consec_repeat": dict(consec_repeat.most_common(20)),
    }
    (SOURCE / "deep_analysis.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSaved: {SOURCE / 'deep_analysis.json'}")

if __name__ == "__main__":
    main()
