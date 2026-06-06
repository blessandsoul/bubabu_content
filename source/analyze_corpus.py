#!/usr/bin/env python3
"""Analyze 29-transcript Bubabu corpus → output analysis.md + raw stats."""
import json
import re
from collections import Counter
from pathlib import Path

SOURCE = Path(__file__).parent
TRANS_DIR = SOURCE / "transcripts"

# Georgian common-word stopwords (function words to exclude from content vocab)
GE_STOP = set("და მე შენ ის ჩვენ თქვენ ისინი არის იყო იქნება ერთი ორი სამი ერთხელ რომ რომელიც ვინც რაც ეს ის ეგ ჩემი შენი მისი ჩვენი თქვენი მათი ჩემთან შენთან მისთან ვინ რა სად როდის როცა როგორ რატომ მაგრამ თუ კი არა ხო ჰო ნუ აი არ ან ხოლო ვერ ან მერე ისე ასე როდის როცა აქ იქ აქედან იქით ნუ ხან ხანდახან რომ ვითომ თითქოს უნდა მინდა გინდა გვინდა გინდათ უნდათ შემიძლია შეუძლია მქონდა მქონია ისე ბევრი ცოტა ცოტათი ცოტა მთლად ცოტას ხელით ფეხით ბევრად ცოტათი".split())

def parse_sentences(text: str):
    """Rough sentence split (KA uses ./?/! same as Latin; no abbreviation issue here)."""
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"[.!?]+", text)
    return [p.strip() for p in parts if p.strip() and len(p.strip()) > 2]

def word_tokens(text: str):
    """Words: any run of Georgian letters."""
    return re.findall(r"[Ⴀ-ჿⴀ-⴯]+", text)

def analyze_transcript(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    text = " ".join(s["text"] for s in data["snippets"])
    text_clean = re.sub(r"\[.*?\]|\(.*?\)", "", text)  # strip [Music] / (laugh)
    sentences = parse_sentences(text_clean)
    words = word_tokens(text_clean)
    duration_sec = data["snippets"][-1]["start"] + data["snippets"][-1]["duration"] if data["snippets"] else 0
    return {
        "id": data["id"],
        "lang": data["lang"],
        "n_snippets": len(data["snippets"]),
        "n_sentences": len(sentences),
        "n_words": len(words),
        "duration_sec": duration_sec,
        "wpm": (len(words) / max(duration_sec, 1)) * 60 if duration_sec else 0,
        "first_3_sentences": sentences[:3],
        "last_3_sentences": sentences[-3:],
        "all_text": text_clean,
        "words": words,
        "sentences": sentences,
    }

def main():
    all_transcripts = []
    for ch_dir in sorted(TRANS_DIR.iterdir()):
        if not ch_dir.is_dir():
            continue
        for json_path in sorted(ch_dir.glob("*.json")):
            try:
                t = analyze_transcript(json_path)
                t["channel"] = ch_dir.name
                all_transcripts.append(t)
            except Exception as e:
                print(f"ERROR {json_path.name}: {e}")

    if not all_transcripts:
        print("NO TRANSCRIPTS FOUND")
        return

    # Filter to ka only (drop en-auto from ch1 ESEQAzGCnpA which was music video)
    ka_only = [t for t in all_transcripts if t["lang"] == "ka"]
    en_only = [t for t in all_transcripts if t["lang"] != "ka"]

    print(f"=== CORPUS ===")
    print(f"Total transcripts: {len(all_transcripts)} ({len(ka_only)} ka, {len(en_only)} other)")
    print()

    # Length distribution
    print("=== LENGTH STATS (ka only) ===")
    if ka_only:
        durs = sorted(t["duration_sec"] for t in ka_only)
        words = sorted(t["n_words"] for t in ka_only)
        sents = sorted(t["n_sentences"] for t in ka_only)
        wpms = sorted(t["wpm"] for t in ka_only if t["wpm"] > 0)
        n = len(ka_only)
        print(f"Duration sec: min={durs[0]:.0f}  median={durs[n//2]:.0f}  max={durs[-1]:.0f}")
        print(f"Words count:  min={words[0]}  median={words[n//2]}  max={words[-1]}")
        print(f"Sentences:    min={sents[0]}  median={sents[n//2]}  max={sents[-1]}")
        if wpms:
            print(f"WPM:          min={wpms[0]:.1f}  median={wpms[len(wpms)//2]:.1f}  max={wpms[-1]:.1f}")
        print()

    # Vocab (top content words, exclude function-word stopwords)
    print("=== TOP CONTENT WORDS (ka only) ===")
    all_words = []
    for t in ka_only:
        all_words.extend(t["words"])
    wc = Counter(w for w in all_words if w not in GE_STOP and len(w) > 2)
    top50 = wc.most_common(50)
    for w, c in top50:
        print(f"  {c:5d}  {w}")
    print()

    # Hook patterns (first sentence)
    print("=== HOOK SENTENCES (first sentence of each ka transcript) ===")
    hook_words = Counter()
    for t in ka_only:
        if t["first_3_sentences"]:
            first = t["first_3_sentences"][0]
            print(f"  [{t['channel'][:5]}] {first[:120]}")
            for w in word_tokens(first)[:3]:
                hook_words[w] += 1
    print()
    print("=== HOOK FIRST-3-WORDS distribution ===")
    for w, c in hook_words.most_common(20):
        print(f"  {c:3d}  {w}")
    print()

    # Ending patterns
    print("=== ENDING SENTENCES (last sentence of each ka transcript) ===")
    for t in ka_only:
        if t["last_3_sentences"]:
            last = t["last_3_sentences"][-1]
            print(f"  [{t['channel'][:5]}] {last[:120]}")
    print()

    # Sentence length
    print("=== SENTENCE LENGTH (words per sentence, ka only) ===")
    sent_lens = []
    for t in ka_only:
        for s in t["sentences"]:
            sent_lens.append(len(word_tokens(s)))
    if sent_lens:
        sent_lens.sort()
        print(f"  mean={sum(sent_lens)/len(sent_lens):.1f}")
        print(f"  median={sent_lens[len(sent_lens)//2]}")
        print(f"  90th-percentile={sent_lens[int(len(sent_lens)*0.9)]}")
        print(f"  max={sent_lens[-1]}")
    print()

    # Bigrams (top ka content phrases — 2-word seqs)
    print("=== TOP BIGRAMS (ka content, stopword-filtered) ===")
    bigrams = Counter()
    for t in ka_only:
        ws = t["words"]
        for i in range(len(ws) - 1):
            w1, w2 = ws[i], ws[i+1]
            if w1 in GE_STOP or w2 in GE_STOP:
                continue
            if len(w1) < 3 or len(w2) < 3:
                continue
            bigrams[(w1, w2)] += 1
    for (a, b), c in bigrams.most_common(30):
        print(f"  {c:4d}  {a} {b}")
    print()

    # Save raw analysis JSON
    out = {
        "n_transcripts": len(all_transcripts),
        "n_ka": len(ka_only),
        "length_stats": {
            "duration_sec": {"min": durs[0], "median": durs[n//2], "max": durs[-1]} if ka_only else {},
            "n_words": {"min": words[0], "median": words[n//2], "max": words[-1]} if ka_only else {},
            "n_sentences": {"min": sents[0], "median": sents[n//2], "max": sents[-1]} if ka_only else {},
        },
        "top_words": dict(top50),
        "top_bigrams": [{"phrase": f"{a} {b}", "count": c} for (a, b), c in bigrams.most_common(50)],
        "hooks": [
            {"channel": t["channel"], "id": t["id"], "first_sentence": t["first_3_sentences"][0] if t["first_3_sentences"] else ""}
            for t in ka_only
        ],
        "endings": [
            {"channel": t["channel"], "id": t["id"], "last_sentence": t["last_3_sentences"][-1] if t["last_3_sentences"] else ""}
            for t in ka_only
        ],
        "per_transcript": [
            {k: v for k, v in t.items() if k not in ("words", "sentences", "all_text")}
            for t in ka_only
        ],
    }
    (SOURCE / "corpus_analysis.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nSaved: {SOURCE / 'corpus_analysis.json'}")

if __name__ == "__main__":
    main()
