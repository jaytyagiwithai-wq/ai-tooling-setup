"""Collect YouTube transcript markdown files for the research project.

This uses youtube-transcript-api for captions and yt-dlp for public metadata.
If YouTube returns an IP/rate-limit block, wait and rerun or switch to a
managed transcript API such as Supadata.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi


VIDEOS = [
    {
        "expert": "Sam Dunning",
        "video_id": "e9ccLnRmeo0",
        "title": "A Complete Guide to AI SEO in 2026 (AEO, GEO, LLMO)",
    },
    {
        "expert": "Ryan Law",
        "video_id": "D7LBx8RFOcQ",
        "title": "AI Writing at Scale: Ahrefs' Step-by-Step Workflow",
    },
    {
        "expert": "Ryan Law",
        "video_id": "mL1W1SMtTT4",
        "title": "How to Win in AI Search (Real Data, No Hype)",
    },
    {
        "expert": "Ryan Law",
        "video_id": "iVZrVeESnFQ",
        "title": "How to Automate Blog Writing with AI from Keyword to Published",
    },
    {
        "expert": "Kevin Indig",
        "video_id": "eepyi-NYFiM",
        "title": "SEO in the AI Era: What Marketers Need to Know",
    },
    {
        "expert": "Ross Simmonds",
        "video_id": "u41_Sq91SW0",
        "title": "Ross Simmonds on Unlocking the Power of Content",
    },
    {
        "expert": "Bernard Huang",
        "video_id": "4KyYqe1s_XY",
        "title": "How GEO Actually Works",
    },
    {
        "expert": "Eli Schwartz",
        "video_id": "x5CgYCRLgbc",
        "title": "Product-Led SEO in AI Era",
    },
    {
        "expert": "Andy Crestodina",
        "video_id": "jXUPJ_z1i4Q",
        "title": "How AI is Reshaping Your SEO Strategy",
    },
    {
        "expert": "Amanda Natividad",
        "video_id": "t6Yxdw-Sid4",
        "title": "How to Win with Zero Click Content",
    },
    {
        "expert": "Mike King",
        "video_id": "Bs6-ROULCLk",
        "title": "The Brave New World of SEO",
    },
]


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def fmt_time(seconds: float) -> str:
    seconds = int(seconds)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_metadata(video_id: str) -> dict:
    url = f"https://www.youtube.com/watch?v={video_id}"
    options = {"quiet": True, "skip_download": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(options) as ydl:
        return ydl.extract_info(url, download=False)


def main() -> None:
    out_dir = Path("research/youtube-transcripts")
    out_dir.mkdir(parents=True, exist_ok=True)
    transcript_api = YouTubeTranscriptApi()
    collected_at = dt.datetime.now(dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    for video in VIDEOS:
        video_id = video["video_id"]
        url = f"https://www.youtube.com/watch?v={video_id}"
        metadata = get_metadata(video_id)
        transcript = transcript_api.fetch(video_id)

        upload_date = metadata.get("upload_date") or "unknown-date"
        title = metadata.get("title") or video["title"]
        channel = metadata.get("channel") or "unknown channel"
        filename = f"{upload_date}-{slugify(video['expert'])}-{video_id}.md"

        lines = [
            "---",
            f"expert: {video['expert']}",
            f"title: {title}",
            f"channel: {channel}",
            f"video_id: {video_id}",
            f"url: {url}",
            f"published: {upload_date}",
            f"collected_at: {collected_at}",
            "tool: youtube-transcript-api",
            "---",
            "",
            "# Transcript",
            "",
        ]

        for item in transcript:
            lines.append(f"[{fmt_time(item.start)}] {item.text}")

        (out_dir / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote {filename}")


if __name__ == "__main__":
    main()
