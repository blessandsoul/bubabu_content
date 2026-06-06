#!/usr/bin/env python3
"""Retry 14 IpBlocked ch2 IDs with delay."""
import json
import time
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

SOURCE = Path(__file__).parent
RETRY_IDS = (SOURCE / "ch2_retry.ids.txt").read_text(encoding="utf-8").splitlines()
OUT_DIR = SOURCE / "transcripts" / "ch2_jirafijoze"

# Need title lookup
ids_full = (SOURCE / "ch2.ids.txt").read_text(encoding="utf-8").splitlines()
title_map = {line.split("|", 1)[0]: line.split("|", 1)[1] if "|" in line else "" for line in ids_full}

api = YouTubeTranscriptApi()
results = []
for i, vid in enumerate(RETRY_IDS):
    vid = vid.strip()
    if not vid:
        continue
    try:
        listing = api.list(vid)
        langs = [f"{t.language_code}{'-auto' if t.is_generated else ''}" for t in listing]
        try:
            chosen = listing.find_transcript(['ka'])
        except NoTranscriptFound:
            try:
                chosen = listing.find_transcript(['en'])
            except NoTranscriptFound:
                print(f"[{i+1}/{len(RETRY_IDS)}] NO_LANG {vid} langs={langs}")
                results.append({"id": vid, "status": "no_lang", "langs": langs})
                continue
        data = chosen.fetch()
        snippets = [{"start": s.start, "duration": s.duration, "text": s.text} for s in data.snippets]
        full = " ".join(s.text for s in data.snippets)
        (OUT_DIR / f"{vid}.json").write_text(json.dumps({
            "id": vid, "lang": chosen.language_code, "auto": chosen.is_generated,
            "snippets": snippets,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        (OUT_DIR / f"{vid}.txt").write_text(full, encoding="utf-8")
        print(f"[{i+1}/{len(RETRY_IDS)}] OK {vid} lang={chosen.language_code} n={len(snippets)} chars={len(full)}")
        results.append({"id": vid, "status": "ok", "lang": chosen.language_code, "n_snippets": len(snippets), "n_chars": len(full)})
    except TranscriptsDisabled:
        print(f"[{i+1}/{len(RETRY_IDS)}] DISABLED {vid}")
        results.append({"id": vid, "status": "disabled"})
    except Exception as e:
        msg = str(e)[:80]
        print(f"[{i+1}/{len(RETRY_IDS)}] {type(e).__name__} {vid}: {msg}")
        results.append({"id": vid, "status": "error", "error": f"{type(e).__name__}: {msg}"})
    time.sleep(1.5)  # gentle delay to avoid re-blocking

(SOURCE / "retry_summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
ok = sum(1 for r in results if r["status"] == "ok")
print(f"\n=== {ok}/{len(results)} ok ===")
