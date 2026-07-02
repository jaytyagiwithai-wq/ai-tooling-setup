# AI-Powered SEO Content Production Research

This repository is now being used for a 100Hires research project on:

**AI-powered SEO content production for B2B SaaS.**

I chose this topic because B2B SaaS teams are trying to answer a practical question right now: how do you use AI to produce, refresh, and distribute SEO content without creating generic content that fails in Google, AI Overviews, ChatGPT, Perplexity, and other answer engines?

## What I Collected

- 10 high-signal experts who actively publish or practice AI SEO, AEO, GEO, content strategy, and B2B SaaS organic growth.
- Public LinkedIn post references organized by author in `research/linkedin-posts/`.
- YouTube video transcripts collected with Supadata in `research/youtube-transcripts/`.
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

I used public search, public LinkedIn post pages, YouTube metadata, `yt-dlp`, `youtube-transcript-api`, and Supadata during collection.

YouTube initially returned IP/rate-limit blocks through the free transcript library, so I switched the collection script to use Supadata when `SUPADATA_API_KEY` is available. The API key is not stored in the repository.

## Next Step

Rerun the transcript script if new videos are added:

```bash
python scripts/collect_youtube_transcripts.py
```

When using Supadata, set `SUPADATA_API_KEY` locally before running the script.
