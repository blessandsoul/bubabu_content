#!/usr/bin/env python3
"""Batch-download KA transcripts from ch1 + ch2 via youtube-transcript-api."""
import json
import os
import sys
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

SOURCE = Path(__file__).parent
CHANNELS = [
    ("ch1_dziliskhairi", "ch1.ids.txt"),
    ("ch2_jirafijoze",   "ch2.ids.txt"),
]

api = YouTubeTranscriptApi()

def fetch_one(vid: str, out_dir: Path) -> dict:
    try:
        listing = api.list(vid)
        # Prefer ka, fallback en
        chosen = None
        langs_avail = []
        for t in listing:
            langs_avail.append(f"{t.language_code}{'-auto' if t.is_generated else ''}")
        for code in ('ka', 'en'):
            try:
                chosen = listing.find_transcript([code])
                break
            except NoTranscriptFound:
                continue
        if chosen is None:
            return {"id": vid, "status": "no_lang", "langs": langs_avail}
        data = chosen.fetch()
        snippets = [{"start": s.start, "duration": s.duration, "text": s.text}
                    for s in data.snippets]
        full_text = " ".join(s.text for s in data.snippets)
        out_dir.mkdir(parents=True, exist_ok=True)
        json_path = out_dir / f"{vid}.json"
        txt_path  = out_dir / f"{vid}.txt"
        json_path.write_text(json.dumps({
            "id": vid,
            "lang": chosen.language_code,
            "auto": chosen.is_generated,
            "snippets": snippets,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        txt_path.write_text(full_text, encoding="utf-8")
        return {"id": vid, "status": "ok", "lang": chosen.language_code,
                "n_snippets": len(snippets), "n_chars": len(full_text),
                "langs": langs_avail}
    except TranscriptsDisabled:
        return {"id": vid, "status": "disabled"}
    except Exception as e:
        return {"id": vid, "status": "error", "error": f"{type(e).__name__}: {str(e)[:120]}"}

def run_channel(channel: str, ids_file: str):
    ids_path = SOURCE / ids_file
    if not ids_path.exists():
        print(f"MISSING {ids_path}")
        return []
    out_dir = SOURCE / "transcripts" / channel
    results = []
    for line in ids_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        vid = line.split("|", 1)[0]
        title = line.split("|", 1)[1] if "|" in line else ""
        r = fetch_one(vid, out_dir)
        r["title"] = title
        results.append(r)
        marker = "OK" if r["status"] == "ok" else r["status"].upper()
        extra = ""
        if r["status"] == "ok":
            extra = f" lang={r['lang']} n={r['n_snippets']} chars={r['n_chars']}"
        print(f"[{channel}] {marker} {vid} '{title[:50]}'{extra}")
    return results

if __name__ == "__main__":
    all_results = {}
    for channel, ids_file in CHANNELS:
        print(f"\n=== {channel} ===")
        all_results[channel] = run_channel(channel, ids_file)

    summary_path = SOURCE / "transcript_fetch_summary.json"
    summary_path.write_text(json.dumps(all_results, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n=== SUMMARY ===")
    for ch, res in all_results.items():
        ok = sum(1 for r in res if r["status"] == "ok")
        print(f"{ch}: {ok}/{len(res)} ok")
