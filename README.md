# AI-Powered SEO Content Production Research

This repo is for a 100Hires research assignment on:

**AI-powered SEO content production for B2B SaaS.**

I chose this topic because it sits right in the middle of what a lot of SaaS marketers are trying to figure out: how to use AI for SEO without flooding the internet with generic posts that nobody trusts.

## What I Collected

- 10+ experts who actually work in SEO/content/growth, not just people writing broad AI takes.
- Public LinkedIn post references organized by author in `research/linkedin-posts/`.
- YouTube video transcripts collected with Supadata in `research/youtube-transcripts/`.
- Additional article, newsletter, podcast, and tool notes in `research/other/`.
- A reusable Python transcript collection script in `scripts/collect_youtube_transcripts.py`.
- A strategy layer so the repo is not just links and transcripts.

## Repository Structure

```text
research/
  sources.md
  linkedin-posts/
  youtube-transcripts/
  other/
    expert-takeaways.md
    playbook-outline.md
    content-decision-rubric.md
    research-synthesis.md
scripts/
  collect_youtube_transcripts.py
requirements.txt
```

## Why These Experts

I tried to avoid the obvious "top AI SEO influencers" list. The people here are a mix of SaaS content operators, agency founders, SEO researchers, tool founders, and B2B marketers with public work that connects to real content systems.

The main patterns I saw:

- AI is useful, but only after the team has real inputs: customer calls, SME notes, product proof, examples, and opinions.
- AI search is pushing SEO beyond rankings/clicks into mentions, citations, entities, and passage-level answers.
- B2B SaaS teams should care more about bottom-funnel and product-led content than pumping out top-funnel posts.
- Distribution matters more now because third-party mentions help both buyers and AI systems understand who is credible.
- Traffic alone is not enough. The better measurement set includes AI visibility, branded demand, pipeline influence, and refresh performance.

## Added Analysis

After collecting the raw material, I added three analysis files:

- `research/other/research-synthesis.md`: what the experts agree on, where they differ, and what most teams get wrong.
- `research/other/playbook-outline.md`: a proposed B2B SaaS AI SEO playbook built from the collected sources.
- `research/other/content-decision-rubric.md`: a practical scoring system for deciding what to create, refresh, merge, or skip.

## Collection Notes

I used public search, public LinkedIn pages, YouTube metadata, `yt-dlp`, `youtube-transcript-api`, and Supadata.

The free YouTube transcript library hit IP/rate-limit blocks, so I added Supadata support to the script. The Supadata key was only used locally and is not stored in the repo.
