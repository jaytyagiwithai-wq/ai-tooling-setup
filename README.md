# AI-Powered SEO Content Production Research

This repository is now being used for a 100Hires research project on:

**AI-powered SEO content production for B2B SaaS.**

I chose this topic because B2B SaaS teams are trying to answer a practical question right now: how do you use AI to produce, refresh, and distribute SEO content without creating generic content that fails in Google, AI Overviews, ChatGPT, Perplexity, and other answer engines?

## What I Collected

- 10 high-signal experts who actively publish or practice AI SEO, AEO, GEO, content strategy, and B2B SaaS organic growth.
- Public LinkedIn post references organized by author in `research/linkedin-posts/`.
- YouTube video metadata and transcript collection targets in `research/youtube-transcripts/`.
- Additional article, newsletter, podcast, and tool notes in `research/other/`.
- A reusable Python transcript collection script in `scripts/collect_youtube_transcripts.py`.

## Repository Structure

```text
research/
  sources.md
  linkedin-posts/
  youtube-transcripts/
  other/
scripts/
  collect_youtube_transcripts.py
requirements.txt
```

## Why These Experts

The expert list prioritizes people with operational credibility: agency founders, SaaS content leads, SEO software operators, researchers, and advisors who publish detailed thinking from real client, product, or audience work.

The strongest recurring themes across the source set are:

- AI content only works when it is tied to differentiated inputs, subject-matter expertise, and clear user intent.
- AI search visibility is moving beyond rankings and clicks toward citations, mentions, entity strength, and passage-level relevance.
- B2B SaaS teams need bottom-funnel and product-led content, not just high-volume informational posts.
- Distribution and third-party validation matter more as AI makes generic content cheap.
- Measurement needs to include AI visibility, branded demand, qualified pipeline, and content refresh performance.

## Collection Notes

I used public search, public LinkedIn post pages, YouTube metadata, `yt-dlp`, and `youtube-transcript-api` during collection.

The transcript API successfully returned transcript availability for the selected YouTube videos during initial testing, but YouTube later returned IP/rate-limit blocks while writing files. I left the collection script in the repo so the transcript pass can be rerun from a clean network session or swapped to Supadata/TranscriptAPI if an API key is available.

## Next Step

Run the transcript script after the YouTube rate limit clears:

```bash
python scripts/collect_youtube_transcripts.py
```

Then commit the generated transcript files as the next small commit.
