---
expert: Ryan Law
title: AI Writing at Scale: Ahrefs’ Step-by-Step Workflow | Ryan Law (Ahrefs)
channel: Ahrefs Podcast
video_id: D7LBx8RFOcQ
url: https://www.youtube.com/watch?v=D7LBx8RFOcQ
published: 20250805
collected_at: 2026-07-02T20:06:49Z
tool: supadata
language: en
---

# Transcript

[00:00:00] Ryan, uh, welcome to Href's podcast. How
[00:00:03] are you doing?
[00:00:04] >> Yeah, very, very good. Yeah, what an
[00:00:06] honor and privilege to be on the podcast
[00:00:08] with you. Normally, I'm just listening
[00:00:09] to it. So the story of this episode is
[00:00:14] uh the fact that you have devised a
[00:00:16] pretty cool uh workflow for creating
[00:00:20] content with AI uh which you actually
[00:00:23] used to publish some articles at HF's
[00:00:25] blog written by AI and no one kind of
[00:00:28] noticed because those articles were this
[00:00:30] good and when I shared on LinkedIn a
[00:00:33] screenshot of the steps that you're
[00:00:35] taking to walk AI because it's not an
[00:00:38] it's not an easy process to to create
[00:00:40] amazing content with AI. When I shared
[00:00:42] the the screenshot of it on LinkedIn and
[00:00:44] ask people uh if they want to see it uh
[00:00:47] what did we get? 400 comments uh on this
[00:00:50] post or something. So now we have to
[00:00:53] record this episode and show people your
[00:00:56] uh AI content production process.
[00:00:59] >> Yeah. So thank you for making me do
[00:01:01] that.
[00:01:03] >> So uh let let's start from the results.
[00:01:06] So before we go into the process, I want
[00:01:09] to talk a little bit about the results
[00:01:11] uh about the the quality of content that
[00:01:13] you get this way. Well, obviously we
[00:01:14] published it on HF's blog, so it's good
[00:01:17] enough. But I know that you're also
[00:01:19] tracking it uh in in a portfolio format
[00:01:22] at Hrefs. We have this feature called
[00:01:23] portfolios where where you can track a
[00:01:25] custom list of URLs and you're adding
[00:01:27] all your AI generated articles there and
[00:01:30] they're starting to rank for some
[00:01:32] keywords already. So Google kind of
[00:01:34] likes them.
[00:01:36] Yeah. Yeah. Exactly that. Um I was just
[00:01:38] looking at one of them. It's at number
[00:01:39] four for its target keyword at the
[00:01:41] moment, which, you know, we'd be happy
[00:01:42] with with any article that we created
[00:01:45] for the most part. Um a lot of them are
[00:01:47] getting good Google discover traffic as
[00:01:49] well, which is something I don't always
[00:01:50] see with content. Um so yeah, I think
[00:01:54] compared to the human written content we
[00:01:57] published at the same sort of time, the
[00:01:58] same time scale, I can't really notice
[00:02:00] any difference in the performance to be
[00:02:02] honest. Um kind of cool. So basically uh
[00:02:06] we're about to share the process that
[00:02:08] allows you to create the kind of content
[00:02:11] that actually brings traffic and some
[00:02:14] business results. Uh other than just uh
[00:02:18] like publish and forget about it and it
[00:02:20] would be covered with dust because no
[00:02:22] one is uh visiting that content because
[00:02:24] it's so bad it doesn't rank anywhere. Uh
[00:02:27] that sounds good to me. Uh so I I didn't
[00:02:29] see like your process. So this would be
[00:02:31] the first time you're showing it to me.
[00:02:33] uh and we'll see if I have any questions
[00:02:36] or my kind of typical skepticism, but
[00:02:38] yeah, given that the content is
[00:02:40] published on HF's blog and I actually
[00:02:41] read a few of these articles myself,
[00:02:44] they were really good. So yeah, I don't
[00:02:46] I don't think that I would have much
[00:02:48] skepticism. I'm very keen to to see a
[00:02:50] process. Let's go. Basic setup. I'm
[00:02:53] using chat GPT for this and I'm creating
[00:02:55] a project. So I have the HF's blog
[00:02:58] project. Um, and hopefully we can maybe
[00:03:01] slightly blur out some of the side chats
[00:03:03] because, uh, people don't need to know
[00:03:04] that I'm looking up how to cook oene in
[00:03:06] my roast dinner. But, uh, there you go.
[00:03:09] Um, and I think the really important
[00:03:11] part of this is the project files. This
[00:03:14] is why I like using a project. Um, if
[00:03:17] you just ask for a blog post from any
[00:03:19] LLM, normally it comes back like pretty
[00:03:22] terrible. It's not interesting. It's not
[00:03:24] well written. Just the worst kind of
[00:03:26] content marketing. Um so what I've
[00:03:28] actually done is basically taken our
[00:03:30] human editorial process uh so taken the
[00:03:35] existing documentation we already had to
[00:03:37] guide writers on how to write well for
[00:03:39] hrefs. So this is stuff from uh how to
[00:03:43] create an outline for the first time,
[00:03:45] how to edit an outline, the kind of
[00:03:47] guidance for me, how to write, how to
[00:03:49] mention HFS products, how to add
[00:03:52] WordPress short codes, like every single
[00:03:54] facet of the actual like human written
[00:03:56] process that's been each stage of that
[00:03:59] is converted into a written process and
[00:04:02] that is then uploaded as an individual
[00:04:04] document to the project file. So
[00:04:07] basically containing
[00:04:08] >> so we see seven files right am I
[00:04:10] counting correctly seven files in this
[00:04:13] uh chat GBT project right
[00:04:15] >> yeah exactly that uh and so we have also
[00:04:17] a very basic like um instruction here as
[00:04:20] well which I think a lot of this is
[00:04:23] probably fluffy and doesn't actually
[00:04:24] help the model but um parts of it are
[00:04:26] useful. It basically tells the model to
[00:04:28] refer back to the project uh context
[00:04:31] those files we uploaded during every uh
[00:04:35] every conversation we create. So I'm
[00:04:37] always trying to nudge the model back to
[00:04:38] the documentation and say follow the
[00:04:40] process that I provided with you.
[00:04:42] >> Interesting. Uh I kind of thought when
[00:04:44] when I was looking at your diagram with
[00:04:46] steps and um when you told me that you
[00:04:50] are using documents for each step of the
[00:04:52] process, I thought you would have like
[00:04:54] uh a custom GPT for each step and only
[00:04:58] upload one document at a time. But you
[00:05:01] uploaded all seven of them and you kind
[00:05:03] of referred to to each of them at
[00:05:05] different stages of the process, right?
[00:05:07] >> Yeah, exactly that. And actually, Chat
[00:05:09] GBT is quite good at uh actually
[00:05:12] following along through the stages.
[00:05:14] Something like Claude, for example, I've
[00:05:15] been testing this out with it just tries
[00:05:16] to do everything at once. It just runs
[00:05:18] the whole process in one go.
[00:05:20] >> Uh whereas this I can explicitly say,
[00:05:22] right, start with the first step of the
[00:05:24] process. We're doing the content brief.
[00:05:26] give me a chance to provide feedback and
[00:05:28] then move on to the next step of the
[00:05:29] process. Um, so yeah, I basically act
[00:05:32] like the editor for this. The model is
[00:05:34] working through a very similar like
[00:05:35] reasoning and writing process to exactly
[00:05:38] what a human would do. And it's giving
[00:05:40] me small windows to put input into that
[00:05:43] and say, you know, nudge it in the right
[00:05:44] direction.
[00:05:45] >> Okay, we'll get into projects file
[00:05:48] project files later to see what's there
[00:05:50] maybe once we go through the actual
[00:05:51] steps. But uh let let's quickly go
[00:05:54] through the instructions. What are the
[00:05:55] key things are there? Yeah, you you said
[00:05:57] I see you're a senior content marketer
[00:05:59] or something. What what are the key
[00:06:00] things you're telling to AI about this
[00:06:03] project or this process?
[00:06:06] >> Yeah, I I think so. Jeremy, I'm trying
[00:06:09] to provide like a highle sense of what
[00:06:10] we value in our content. Um things about
[00:06:14] being persuasive, about being uh
[00:06:16] detailed and comprehensive.
[00:06:19] Um I I I really do think a lot of this
[00:06:21] is probably fluff. I don't think a lot
[00:06:23] of it works. I think a very hard thing
[00:06:24] about prompting is knowing what are the
[00:06:27] tiny parts of the prompt that have a
[00:06:28] really big impact and which are the ones
[00:06:30] that just have no impact whatsoever.
[00:06:32] Something
[00:06:33] >> because I mean you have seven files
[00:06:34] there already that that explain what
[00:06:37] what you expect in terms of editorial.
[00:06:40] This is why I'm thinking what is there
[00:06:42] to add to to to the instructions window.
[00:06:45] >> Something that is um has been very
[00:06:48] important uh is this bit here. Um, I've
[00:06:52] actually experimented with taking this
[00:06:53] out and seeing how it impacted it. Uh,
[00:06:55] role play is someone who is deep in the
[00:06:57] trenches experience with this topic,
[00:06:59] someone who's used HF's tools to solve
[00:07:01] real problems and can translate that
[00:07:02] into strategic advice. Um, one of the
[00:07:06] things I've noticed between a good first
[00:07:08] draft from AI and a terrible first draft
[00:07:11] is how often it tries to talk from a
[00:07:13] place of experience. where it says, you
[00:07:15] know, oh, when I use this advice or when
[00:07:17] I use this tool, obviously that is
[00:07:20] hallucinated because AI can't actually
[00:07:22] go and use these tools, but quite often
[00:07:24] the experiences it shares are similar to
[00:07:26] the experiences I've had or it's a
[00:07:28] chance for me to kind of slightly adjust
[00:07:30] what it's said to reflect an actual
[00:07:31] experience I've had. And it made me
[00:07:34] realize that so much of the content we
[00:07:35] write at Hrefs is focused on this. We're
[00:07:38] not just passively commentating on
[00:07:40] advice. we're actually saying, "Okay, we
[00:07:43] tested this out or when I was using this
[00:07:45] or I know from first person experience."
[00:07:48] So, actually adding that into the uh
[00:07:50] instructions for the project, yeah, goes
[00:07:52] a long way to making it sound and feel
[00:07:54] like an actual HFS article. Let me
[00:07:57] clarify here. So, this is not for AI to
[00:08:00] hallucinate that it has experience, that
[00:08:03] it did something uh to to make it look
[00:08:06] more authoritative. This is for you as
[00:08:10] an editor and kind of co-author of the
[00:08:12] piece to find proper spots where you can
[00:08:16] jump in and say, "Oh, I actually can can
[00:08:18] say this. Yeah, I have experience with
[00:08:20] this." And like you you edit a little
[00:08:21] bit, maybe add some kind of different
[00:08:23] story, but it kind of finds places in
[00:08:26] the copy where it would be appropriate
[00:08:28] to to say something like this. And then
[00:08:30] you just make sure that you as the kind
[00:08:32] of the ultimate author of of the article
[00:08:36] can say it because I've seen um when
[00:08:38] when people publish AI generated content
[00:08:41] uh and they do say things like that like
[00:08:44] write from your experience blah blah
[00:08:45] blah show that you're authority and AI
[00:08:48] would hallucinate that it actually like
[00:08:50] did some stuff like it it worked with
[00:08:52] clients blah blah blah and I'm like but
[00:08:54] that's not true. So like it it looks
[00:08:57] legit, but you know it's not true
[00:09:00] because this person just just said that
[00:09:01] they used AI to autogenerate this
[00:09:03] article. So yeah, I I want to be very
[00:09:05] clear with that. Uh don't just kind of
[00:09:09] mislead people uh with those AI claims.
[00:09:12] Make sure that you can you can say them
[00:09:14] uh yourself.
[00:09:15] >> Yeah. And actually that goes back to
[00:09:17] probably the most important part of this
[00:09:19] entire process, which is actually
[00:09:21] working out when it's an appropriate
[00:09:22] process to use. Uh, I don't use this for
[00:09:26] article topics that I know nothing about
[00:09:28] where I have absolutely no experience
[00:09:30] and I can't evaluate whether the
[00:09:32] article's good or sensible or coherent.
[00:09:35] Um, so I think you talked about this
[00:09:37] previously, but I try to use this for
[00:09:38] topics where there's already a lot of
[00:09:41] information out in the world on these
[00:09:43] topics. So there's plent there's a
[00:09:44] wealth of information, accurate, good
[00:09:46] information for the LLMs to draw on. And
[00:09:49] also I need to have a sense of what I
[00:09:51] want the end goal of the article to look
[00:09:52] like. I need to have uh an opinion on
[00:09:55] it. I need to ideally have some
[00:09:57] experience that I can use to judge
[00:09:59] whether this is a coherent and useful
[00:10:00] article or not. Um so yeah, I don't
[00:10:04] write about things I have no experience
[00:10:05] in because who would I be to judge
[00:10:08] whether it's actually good or not?
[00:10:09] >> So uh we have those documents which will
[00:10:11] uh dig deeper as the as you keep
[00:10:14] reviewing the process. We have this kind
[00:10:16] of uh system prompt with some
[00:10:19] instructions. Uh where do you start with
[00:10:21] this? So this is a good example. This is
[00:10:23] an actual this is the conversation I had
[00:10:25] that led to a finished article that
[00:10:26] we've published and I actually uh which
[00:10:28] is quite like this article as well. Uh
[00:10:30] this was a a guide to Python for SEO. So
[00:10:34] the way the uh process starts is I
[00:10:36] basically paste in a content brief as
[00:10:39] the very first step. And the way I see a
[00:10:41] lot of people use AI is they generally
[00:10:43] they create an article and they spend a
[00:10:45] bunch of time kind of post hawk editing
[00:10:48] the article trying to get it up to a
[00:10:49] good standard. I don't think that's a
[00:10:51] very good process because there's a
[00:10:53] limit to how much you can polish a like
[00:10:56] a finished draft. Like you don't have
[00:10:57] that much creative freedom to actually
[00:10:58] make big changes to it without taking a
[00:11:00] ton of time. And it's also not very fun.
[00:11:03] Like nobody wants to spend their day,
[00:11:05] you know, polishing awful AI drafts and
[00:11:07] trying to make them sound human. Uh so
[00:11:09] the thing this process does is it tries
[00:11:11] to frontload all of the input and
[00:11:13] direction and guidance right at the very
[00:11:14] start of the process and then kind of
[00:11:16] get out of the way and let the AI
[00:11:18] generate the article based on that. So
[00:11:21] first thing in the brief uh target
[00:11:22] keyword these are keyword targeted
[00:11:24] articles. Uh then working title. I
[00:11:27] always think this is a really important
[00:11:28] thing to do because you're basically
[00:11:30] setting the end goal of what you want to
[00:11:32] arrive at. Um so in this case very
[00:11:36] simple how to get started with Python
[00:11:37] for SEO like not hard to come up with
[00:11:40] that title to begin with. Um and then
[00:11:43] key points to include I think this is a
[00:11:45] very important section. This is where I
[00:11:47] basically say from my own you know
[00:11:50] desire and my knowledge what are the
[00:11:52] things I expect to see in this finished
[00:11:54] article. Uh and this is why this is not
[00:11:56] like a cheap process that I think anyone
[00:11:58] could do because it is dependent on
[00:11:59] having a sense of like the conclusion
[00:12:01] you want to arrive at. So I said uh you
[00:12:05] know my motivation for writing this was
[00:12:06] that actually Python can help automate
[00:12:09] things. It's a good starting point for
[00:12:10] more technical skills. Uh and also
[00:12:12] mention that I have experience using
[00:12:14] this Python course. I want that to be
[00:12:16] the context for the article. That's why
[00:12:18] I'm writing it.
[00:12:20] Uh, I wanted to cover the core concepts
[00:12:21] needed to actually use Python, recommend
[00:12:24] some simple Python projects, and I
[00:12:26] thought, hey, you know, Patrick from our
[00:12:28] team, he knows tons about Python. He's
[00:12:29] got loads of cool scripts. Let's have a
[00:12:31] section where we include that in the
[00:12:33] article. So, right from the outset, I've
[00:12:35] said this has to be in the article at
[00:12:37] some point. Like, your job is to include
[00:12:39] these things.
[00:12:41] And then to help it rank uh what I do is
[00:12:44] I run an AI content helper report for
[00:12:46] every target keyword. I basically just
[00:12:48] copy paste the uh recommended topics
[00:12:50] that that identifies in here as like
[00:12:53] optional context for the LLM to include.
[00:12:56] Okay, for those who don't know what AI
[00:12:59] content helper is, it's it's a tool in
[00:13:01] Hrefs. you you feed it a keyword, it
[00:13:03] pulls the top ranking search results and
[00:13:05] then it pulls the topics from those
[00:13:07] pages and gives you kind of in a way
[00:13:09] like a topical map so to say of uh what
[00:13:13] the the top ranking search results uh
[00:13:15] are covering in terms of uh different
[00:13:17] topics different subtopics of a larger
[00:13:20] topic. So you take information from it
[00:13:22] uh and paste it into your content brief.
[00:13:24] Right.
[00:13:25] >> Yeah. Exactly that. Uh so there's this
[00:13:27] is very very long. There's tons of stuff
[00:13:28] here. So there's the core topic of you
[00:13:30] know content marketing automation should
[00:13:32] be mentioned. Maybe these are some
[00:13:34] relevant terms you can include. This is
[00:13:36] all stuff I do as a human writer like I
[00:13:38] use this as context to my own writing
[00:13:39] process. So I thought it was useful to
[00:13:41] provide it to the LLM for additional
[00:13:43] context as well.
[00:13:45] >> It looks like very clumsy copy paste. We
[00:13:48] don't we don't have the export button
[00:13:49] right in the eye content helper.
[00:13:51] >> No no if we did that would be
[00:13:52] >> this is why it looks so so badly
[00:13:54] formatted.
[00:13:55] >> Okay. Uh and then last thing uh relevant
[00:13:59] HFS products features to reference. So
[00:14:02] there's a step in the process where the
[00:14:04] LLM has to go and find relevant products
[00:14:06] to mention anyway. But sometimes if
[00:14:08] there's something I explicitly want to
[00:14:10] include, I will just bullet out a single
[00:14:12] point here. So in this case, mention
[00:14:14] using Python to call the HF's API for
[00:14:16] data collection and research because
[00:14:18] that's a cool use case.
[00:14:20] >> Sorry for interrupting the interview,
[00:14:21] but I have a very quick announcement to
[00:14:23] make. This October, we're bringing HF's
[00:14:26] Evolve, our 2-day marketing conference
[00:14:28] to sunny San Diego. And Ryan Law is
[00:14:31] actually one of our speakers at this
[00:14:32] event. So, if you're enjoying our
[00:14:34] conversation so far, consider getting a
[00:14:36] ticket to HFSolve in San Diego, where
[00:14:38] you'll get a chance to hang out with
[00:14:40] Ryan and ask him your own questions
[00:14:42] about content marketing and AI. Go to
[00:14:44] our website at hfsevolve.com to see more
[00:14:47] details about the event and get your
[00:14:49] ticket. Again, it's a traps evvolve.com
[00:14:52] this October in San Diego. Now, back to
[00:14:55] the episode. So, this brief is
[00:14:58] essentially very manual. So, you create
[00:15:01] yourself. You're not again using AI to
[00:15:03] like create me a brief for Python for
[00:15:06] SEO.
[00:15:07] >> Yeah, I have the template which doesn't
[00:15:09] change and then, you know, I spend maybe
[00:15:11] five minutes just bulleting out the
[00:15:13] things I expect to see in there and want
[00:15:15] to include. So, my input is still very
[00:15:17] important to that process, I think. But
[00:15:19] again uh looking forward and speaking of
[00:15:21] the AI revolution. So you're taking
[00:15:24] quite a bit of information from AI
[00:15:26] content helper which is our tool that
[00:15:28] kind of uh gives you the the topical
[00:15:31] coverage uh of whatever topic you want
[00:15:34] to write about. Uh, and I I think in the
[00:15:36] future, speaking again of MCP servers
[00:15:39] and API, we could probably add this to
[00:15:41] our MCP server and you could just tell
[00:15:43] AI uh like use HF's MCP to pull the kind
[00:15:48] of topical information from AI content
[00:15:50] helper from this topic and use all the
[00:15:52] relevant terms. So, whatever you do
[00:15:54] right now manually probably like in a
[00:15:57] few months from now, we can potentially
[00:15:59] add it and this this little bit would be
[00:16:02] automated. And then off the LLM goes to
[00:16:04] the next step of the process which is
[00:16:06] actually turning those a content brief
[00:16:08] into an outline. Uh this is something I
[00:16:10] get all of our writers to do and it's
[00:16:11] basically a bullet point uh list of the
[00:16:14] structure of the core ideas of the
[00:16:16] article
[00:16:17] >> and you have uh like in in one of the
[00:16:19] project documents you have a document on
[00:16:21] how to create an outline.
[00:16:23] >> Exactly that. Yeah. It's actually a blog
[00:16:24] post I wrote. So uh outline this is the
[00:16:27] one we want to look at. Uh
[00:16:31] oh, it's pretty short.
[00:16:33] >> Yeah, this is one of the shorter ones.
[00:16:34] There's actually I don't think that much
[00:16:36] that you need to do um to have a good
[00:16:38] outline.
[00:16:39] Uh so yeah, draft all the main section
[00:16:41] headers, ensure they logically support
[00:16:43] the thesis. Uh basically, if you add
[00:16:46] together all the headers, does it amount
[00:16:48] to answering the question you have posed
[00:16:50] by the title? That's like a very
[00:16:51] important thing to do. Um, very minor
[00:16:55] stylistic stuff like avoid ing words in
[00:16:57] headers because it makes it more passive
[00:16:58] and less interesting.
[00:17:00] Um, and yeah, bullet points under each
[00:17:04] header to support the main idea. This is
[00:17:06] quite a good one as well. This is
[00:17:08] something I I think good writing does.
[00:17:10] Uh, start with the bottom line up front.
[00:17:12] So, open every section with the core
[00:17:14] idea articulated in the simplest
[00:17:16] possible way for the reader to
[00:17:18] understand.
[00:17:20] uh then elaborate on that with
[00:17:21] additional like you know supporting
[00:17:23] ideas, examples, opinions, that kind of
[00:17:25] thing. Uh and keep it brief as well.
[00:17:29] And because the introduction I think is
[00:17:31] such an important part of every article,
[00:17:32] there's like specific steps here. Uh
[00:17:35] provide a strong hook idea like what is
[00:17:37] an opening sentence that might get
[00:17:39] somebody's interest in the topic.
[00:17:41] Introduce the thesis and hint at what's
[00:17:43] coming. So what are you actually going
[00:17:45] to cover in the article?
[00:17:48] And similar thing with the conclusion,
[00:17:49] you know, summarize the core argument,
[00:17:51] offer an extra insight or next step.
[00:17:53] Straight up got a hook idea. I used to
[00:17:55] think Python was only for data
[00:17:57] scientists and developers, but after
[00:17:58] finishing replets 100 days of Python, I
[00:18:01] realized it's one of the most powerful
[00:18:02] skills an SEO can learn. And it's never
[00:18:04] been easier to get started. And you
[00:18:07] know, I quite like that it's using my
[00:18:09] experience as the motivation for it,
[00:18:11] which is good. You know, this is
[00:18:12] something that's going to be published
[00:18:13] under my name. Um, and it it, you know,
[00:18:16] appeals to this idea that Python's scary
[00:18:18] and complicated, but actually it's a lot
[00:18:20] easier than you might think. And this
[00:18:22] article will tell you how to do that.
[00:18:24] So, I think it's quite appealing. And
[00:18:25] then here we go. The substantive
[00:18:27] headers, these are the sections it wants
[00:18:28] to cover. So, we've got why learn Python
[00:18:30] as an SEO. Uh, and the bottom line up
[00:18:32] front helps you automate repetitive
[00:18:34] tasks, unlock large scale insights, and
[00:18:36] build technical skills. Uh, and then
[00:18:38] it's got the supporting point. Uh, build
[00:18:41] a technical foundation for writing
[00:18:43] scripts. you don't need to become a
[00:18:44] software engineer all that kind of
[00:18:45] thing.
[00:18:47] It's the core concepts I asked for. Got
[00:18:50] the bluff again. What Python is uh
[00:18:52] choosing a development environment,
[00:18:54] basic building blocks, working with
[00:18:55] data.
[00:18:59] I asked it for some beginner friendly
[00:19:01] projects. So, it's come up with two uh
[00:19:03] three rather look like uh if pages are
[00:19:05] using HTTPS, check for missing image alt
[00:19:08] attributes, scrape titles and metad
[00:19:10] description tags. These are, you know,
[00:19:11] basic, simple, useful things you can do
[00:19:13] with Python. So, that seems pretty
[00:19:15] useful so far. And it included Patrick
[00:19:17] Stock's free Python scripts for SEO. Um,
[00:19:21] and he's found actually found a few from
[00:19:23] uh Patrick's GitHub, which is pretty
[00:19:25] cool. I could have provided those
[00:19:26] manually, but it actually did a decent
[00:19:28] job at finding them itself.
[00:19:31] >> And then the segue to the HF's API,
[00:19:34] and then a quick summary.
[00:19:36] >> Okay. And we have uh the outline at this
[00:19:39] point. uh what is the next step? So I
[00:19:41] review that. I look at it and I think
[00:19:43] you know what do I like? What sucks
[00:19:45] about this? Um and I provide it very
[00:19:48] high level feedback. In this case I
[00:19:50] didn't like the intro that much. I
[00:19:52] suggested an alternate format to use. Uh
[00:19:55] so literally just a few words but to say
[00:19:57] rewrite it using the PAS formula which
[00:20:00] is problem agitate solution like really
[00:20:03] standard copyrightiting formula. Uh like
[00:20:05] a chat GPT understands it. Uh most
[00:20:08] people understand and know it as well.
[00:20:12] uh and you can see that so it came up
[00:20:14] with the problem which is that Python
[00:20:16] feels intimidating if you're not a
[00:20:17] developer. Uh the agitation is where you
[00:20:21] kind of up the ante the make it even
[00:20:23] more dramatic and the solution is how
[00:20:25] the article will deliver on that and
[00:20:27] help you do it and that's exactly what
[00:20:28] it's done with that structure there.
[00:20:30] >> Okay. You you don't have any uh system
[00:20:32] document for writing interest right?
[00:20:34] >> Uh no no none specifically. No. Um, and
[00:20:37] you have to nudge it occasionally like
[00:20:39] it, you know, where is the full outline?
[00:20:41] It deleted the rest of it. I had to make
[00:20:42] it put it back in. You know, it's not
[00:20:44] always the most willing counterpart. Uh,
[00:20:46] but it's then added it back in. So, now
[00:20:48] we have a fairly decent article. Uh, and
[00:20:50] I said, "Cool, turn the outline into an
[00:20:52] article draft." Uh, and obviously it
[00:20:54] then said failed to edit. So, I had to
[00:20:56] say try again. And it then did work. And
[00:20:59] that is when we go on to the next step
[00:21:00] of the process. So, we have an actual
[00:21:01] document which is how to write for
[00:21:03] Hrefs. So I think a lot of these as well
[00:21:06] they're combinations of existing
[00:21:08] documents we had that the team already
[00:21:10] use. Uh in some cases I've asked AI to
[00:21:13] turn you know articles or resources into
[00:21:15] a an SOP for us to include. So yeah very
[00:21:18] simple things. Include specific examples
[00:21:20] for every point you make. Include first
[00:21:22] person experiences and anecdotes.
[00:21:24] Include opinions. Be detailed and
[00:21:27] exhaustive in everything you write.
[00:21:28] Every article should be mey, mutually
[00:21:31] exclusive and collectively exhaustive.
[00:21:33] use the bluff principle. Um, they're all
[00:21:36] like I think the important part about
[00:21:37] this is being able to take, you know,
[00:21:40] good writing and distill it down to, you
[00:21:42] know, maybe 10 core principles that are
[00:21:44] simple enough that the LLM can actually
[00:21:45] understand and act on, which is
[00:21:48] obviously what I've tried to do here.
[00:21:50] >> It's kind of odd that you're keep
[00:21:52] pushing AI to uh act and write from its
[00:21:55] experience uh when it doesn't really
[00:21:58] have any. So, it's kind of faking its
[00:22:01] experience. But I like uh what you
[00:22:03] suggested where essentially you you can
[00:22:05] take some of the best articles from from
[00:22:08] uh your blog or some of your best
[00:22:10] writing. You can feed it to AI and ask
[00:22:12] like can you write me the the guidelines
[00:22:15] uh based on this content that you see
[00:22:17] from me and then use those guidelines to
[00:22:20] create more of such content. I like
[00:22:22] that.
[00:22:23] >> Another important part about this is
[00:22:24] I've actually included some examples of
[00:22:26] good content. So these are not whole
[00:22:28] articles but these are sections from a
[00:22:30] few different writers on our blog of
[00:22:31] good articles uh that can be used as
[00:22:35] context and inspiration for it. Um and I
[00:22:38] think this is actually kind of important
[00:22:39] as well because from an AI content
[00:22:41] detecting point of view because this is
[00:22:43] basically where we are changing the
[00:22:47] output in such a way that it's not very
[00:22:49] easily identifiable as uh the base LLM
[00:22:52] model. It's actually being inspired by a
[00:22:54] different writing pattern like a human
[00:22:55] writing pattern. And that changes the
[00:22:58] the content that comes out at the end.
[00:23:00] So as an example from me, example from
[00:23:02] Desperia.
[00:23:02] >> Are these links to the articles?
[00:23:05] >> Uh I think they are. Yes, they are
[00:23:08] valid.
[00:23:08] >> So basically you give Chad GPT a system
[00:23:11] document and this system document is
[00:23:13] linking to more articles.
[00:23:16] >> Yeah.
[00:23:17] >> Can we be sure that it follows the links
[00:23:20] and actually takes the the content?
[00:23:22] Maybe it would better to just drop the
[00:23:24] actual content into the document.
[00:23:26] >> Yeah, I don't think it will follow these
[00:23:28] links, which is why I've pulled out like
[00:23:30] example uh
[00:23:33] Oh, you know what? No, I actually
[00:23:34] haven't. Well, there you go. Here's a
[00:23:36] way we could improve that process. I
[00:23:38] think you're right. I think what I did
[00:23:39] was I asked uh AI to summarize the
[00:23:42] writing style maybe of these articles.
[00:23:45] [Music]
[00:23:46] But something I do want to do is work
[00:23:48] out how we can use the entire HF's blog
[00:23:50] as context for content generation. I
[00:23:53] think that would be a very cool thing to
[00:23:54] do.
[00:23:55] >> So, uh, you gave it pretty much the same
[00:23:57] guidelines that we're using internally
[00:23:59] for our writers. Uh, so that they would
[00:24:02] know like what's our style, how do we
[00:24:05] write, what makes our content uh,
[00:24:07] awesome.
[00:24:09] And it wrote a draft I imagine. Uh, and
[00:24:12] I really like using uh the canvas in
[00:24:15] Chad GBT. This is why I still use this
[00:24:17] instead of claude, which a lot of people
[00:24:18] think is better. It's kind of like a
[00:24:20] Google doc, and I can actually highlight
[00:24:22] parts and leave editing comments, and it
[00:24:24] will edit it like a human would. So, you
[00:24:26] can get quite granular with specific
[00:24:28] things.
[00:24:29] >> Wait, I already see it added short
[00:24:31] codes.
[00:24:32] >> Yes, it did. Yes. So, this is another
[00:24:35] thing. It It's generally fairly good at
[00:24:37] working through the process. Sometimes
[00:24:39] it does go slightly mad and will jump
[00:24:41] like three steps ahead and add things
[00:24:43] that you were not ready for like short
[00:24:45] codes as you can see here. Maybe this is
[00:24:48] what can be used in the kind of system
[00:24:50] prompt that you would say I have like uh
[00:24:53] seven documents and they want you to
[00:24:56] reference and act according to just one
[00:24:58] of them at every step of the way and
[00:25:01] like specifically say don't add short
[00:25:04] codes until I approve the draft or
[00:25:06] something like this because yeah like
[00:25:09] when you're still working on the draft
[00:25:10] and when you're giving feedback to AI
[00:25:12] you probably don't want this visual
[00:25:14] noise in the form of different short
[00:25:16] short codes for WordPress. You want to
[00:25:18] add them at the very last step when uh
[00:25:21] everything else is settled. So maybe
[00:25:22] that would help to make the process uh
[00:25:25] kind of more step by step and so that AI
[00:25:28] wouldn't get ahead of itself.
[00:25:29] >> Yeah. And there are maybe this is not
[00:25:32] even the right place for short codes. I
[00:25:33] did AI made a script for me that in a
[00:25:36] Google doc I can just press a button and
[00:25:37] it will go in and add the short code at
[00:25:40] the end as well. So yeah, there are
[00:25:41] different ways to handle that
[00:25:42] >> and giving uh giving feedback right in
[00:25:44] in that canvas, right?
[00:25:46] >> Yeah, exactly.
[00:25:47] >> Writes it kind of uh right there.
[00:25:50] >> So you can see some examples of the type
[00:25:51] of feedback uh I've done. They're very
[00:25:54] simple basic things like uh if something
[00:25:56] was vague and unclear, I've said edit to
[00:25:58] explain what this means. And it says
[00:26:00] you're done. I've updated the
[00:26:02] description of Replet to explain what a
[00:26:04] browserbased IDE is and why it's useful.
[00:26:08] Uh, and if there's like an idea I think
[00:26:10] we should add, I can just mention that
[00:26:11] very briefly. I can say, "This is good.
[00:26:13] Expand it into a full section." So,
[00:26:16] again, this is very like writery
[00:26:18] handholdy editing, but it's so much
[00:26:21] faster. Like, I don't have to be the one
[00:26:23] writing it. I just send a little nudge,
[00:26:24] a little prompt, and straight away the
[00:26:27] article is shaped in the direction I
[00:26:29] want it to be shaped. And it's
[00:26:31] essentially the same thing you do when
[00:26:33] uh our uh blog writers send you their
[00:26:36] draft article. You leave essentially the
[00:26:38] same comments, but uh then it takes a
[00:26:41] while for them to to fix those. And here
[00:26:44] you see the result pretty much
[00:26:45] instantly.
[00:26:47] And uh yeah, I don't have to be as nice
[00:26:49] to the AI as I am to our writers as
[00:26:52] well, which is yeah.
[00:26:56] Uh so yeah, it doesn't take too long to
[00:26:58] do this. Yeah, there's a lot of
[00:26:59] comments, but I don't know. We're
[00:27:01] talking maybe half an hour for this
[00:27:03] discreet stage of the process.
[00:27:05] >> Well, yeah. Uh I I guess it's it's good
[00:27:08] that people would read the actual AI
[00:27:11] article that they're about to publish on
[00:27:12] their blogs start to finish before
[00:27:14] publishing it. This is something I think
[00:27:17] I was watching a talk by Andre Karpathy,
[00:27:22] the guy who was in charge of AI for
[00:27:24] Tesla and he published a lot of great
[00:27:26] YouTube videos about how AI works and
[00:27:28] chat GPT works. uh and like his ideology
[00:27:32] the the way I understood it at least is
[00:27:35] that uh no AI output should be kind of
[00:27:41] published or kind of should see the
[00:27:44] world without a human person reviewing
[00:27:47] it first. So I think he was making some
[00:27:50] examples along the lines of uh if
[00:27:52] there's a system that generates I don't
[00:27:55] know a thousand different banner ads for
[00:27:58] your advertising campaign but it's not
[00:28:01] sustainable for uh a person for a human
[00:28:04] being to review all thousand. So uh he's
[00:28:08] suggesting that AI should generate uh
[00:28:10] things only in quantities that people
[00:28:12] are able to review because it still
[00:28:14] hallucinates and uh I I believe uh the
[00:28:18] the engineers the scientists are unsure
[00:28:20] if the hallucinating problem is ever
[00:28:22] going to go away which means if you're
[00:28:25] not if a human uh like editor is not
[00:28:28] reviewing the AI output and just like
[00:28:31] publishing whatever uh whatever is there
[00:28:33] it can very well uh generate something
[00:28:36] that is just not true or something that
[00:28:38] you wouldn't want to publish. So, uh
[00:28:41] yeah, I guess it it does make sense that
[00:28:43] whenever you generate an an AI article
[00:28:46] uh as as an editor or as a person who is
[00:28:48] going to publish it, especially under
[00:28:50] your own name, you want to review it
[00:28:52] start to finish. So, that makes all all
[00:28:55] the sense for me.
[00:28:56] >> Yeah, especially when it's being
[00:28:57] published under my name as well, you
[00:28:58] know, like I do feel a sense of
[00:29:00] ownership over this content. people
[00:29:01] expect a certain level of quality and I
[00:29:03] don't want to mislead people and put,
[00:29:05] you know, rubbish out. I did that when I
[00:29:07] was like 15 and trying to learn how to
[00:29:09] blog in the first place. You hopefully
[00:29:10] I've grown through that now. And then
[00:29:13] when I'm happy with the draft, uh you
[00:29:15] just say on to the next stage, uh in
[00:29:17] which case next stages,
[00:29:20] >> well, so sometimes, uh if the article
[00:29:22] draft is not very good or I'm still
[00:29:24] struggling with it, I will run it
[00:29:25] through like an editing stage. So, in
[00:29:27] some ways, it's kind of automating what
[00:29:29] I've tried to do where I have a whole
[00:29:31] document of like editing principles,
[00:29:33] >> but you just you just added a bunch of
[00:29:35] uh comments to the canvas document in
[00:29:37] chat GPT where it kind of fixed it on
[00:29:40] the fly and you just said next stage.
[00:29:42] So, does it know which next stage to go?
[00:29:45] >> Uh, it went straight to short codes at
[00:29:47] this point.
[00:29:48] Adding the short codes in
[00:30:00] it and this is the article you published
[00:30:03] and that is the article I published.
[00:30:05] Yeah,
[00:30:10] >> I think the thing I have learned doing
[00:30:11] this is that you know chat GBT does
[00:30:13] struggle to follow processes end to end
[00:30:15] in a repeatable way. it does need to be
[00:30:17] nudged from time to time and quite a lot
[00:30:19] of the time I think it uses the
[00:30:21] documents I provided as context for you
[00:30:24] know instead of waiting to the end to
[00:30:26] say let's add in some HS products which
[00:30:28] doesn't work very well it works much
[00:30:29] better when you do that as part of the
[00:30:32] like actual initial outlining process so
[00:30:34] quite often I'll comment to say you know
[00:30:36] you've only included keywords explorer
[00:30:38] let's mention site explorer here as well
[00:30:40] and build it into the article right from
[00:30:42] the outset
[00:30:43] >> okay so since we uh went through this
[00:30:46] process from start till the end. I think
[00:30:48] it would make sense to uh go back to
[00:30:50] your diagram and review which steps you
[00:30:54] had there because the the diagram is
[00:30:56] what attracted attention of people on
[00:30:57] LinkedIn. Uh so I guess let's let's
[00:31:00] review all the documents step by step.
[00:31:02] So the starting prompt is this the same
[00:31:04] thing that you use uh for like
[00:31:07] instructions the the instructions in
[00:31:09] >> Yeah, exactly. It's exactly the same. Uh
[00:31:11] so these I basically write all the
[00:31:14] individual documents in my notes cuz
[00:31:16] that I can write them in markdown and I
[00:31:18] just export them as a folder and dump
[00:31:20] them into chat tpt. So this is kind of
[00:31:22] like where most of them live. Um so we
[00:31:24] very
[00:31:25] >> we discussed that probably uh in that uh
[00:31:27] kind of system prompt it makes sense to
[00:31:29] to tell it to kind of go step by step
[00:31:32] and not kind of move between steps until
[00:31:34] you approve uh the next one and
[00:31:36] basically at line outline what the steps
[00:31:38] are. So first like I will give you a
[00:31:40] brief and you will generate an outline.
[00:31:42] Then once we agree on the outline uh you
[00:31:45] will generate a draft. Uh then you would
[00:31:48] what like add internal links. So yeah
[00:31:50] maybe maybe outlining the steps uh could
[00:31:53] be useful. I don't know. Let's see the
[00:31:55] next step. Content brief. Yep. So we've
[00:31:57] already uh seen what this looked like
[00:32:00] pasted in. But this is like the kind of
[00:32:01] template I use. Um, so this is just very
[00:32:05] quick way for me to add in the
[00:32:06] information I think the LLM needs to do
[00:32:08] a good job and just dump it into the
[00:32:10] document very quickly. As you can say,
[00:32:12] it's not formatted very well, the AI
[00:32:13] content helper stuff, but that's fine
[00:32:15] for AI.
[00:32:16] >> We also discussed outline. You also
[00:32:18] shared like what are the key elements of
[00:32:20] the outline, how to make it good, how to
[00:32:22] structure structurally edit an outline.
[00:32:24] This is something we didn't look into.
[00:32:26] >> So this um some of the projects actually
[00:32:28] the AI does do a good job at basically
[00:32:31] works to this checklist. It says right
[00:32:32] we'll move on to the next step. I'll
[00:32:34] review according to your editing
[00:32:35] checklist. And it looks at these
[00:32:36] principles and this is quite a useful
[00:32:38] thing. Um again not too many here but
[00:32:41] these are very important things. These
[00:32:43] are what I look for when I'm looking at
[00:32:44] an outline that somebody has sent to me.
[00:32:46] Uh so mei is probably the most important
[00:32:49] framework. All the ideas and the bullet
[00:32:51] points together should be mutually
[00:32:52] exclusive so they don't overlap one
[00:32:55] another too much. If the title of the
[00:32:57] post is how to do keyword research, you
[00:32:59] don't want a subheader that is how to do
[00:33:01] keyword research. Like it doesn't make
[00:33:03] sense to do that
[00:33:04] >> unless you're doing SEO in 2022.
[00:33:07] >> Oh, maybe 2025 is uh the way things are
[00:33:10] going with LLMs. But yeah, exactly. Um
[00:33:13] and also collectively exhaustive. So
[00:33:15] that just means that together all of the
[00:33:17] points you cover are sufficient to
[00:33:20] answer the the question you want to
[00:33:22] answer, cover the topic you want to in
[00:33:23] useful detail. uh and that is honestly
[00:33:26] about 80% of I think uh structural
[00:33:28] editing making sure you actually
[00:33:30] sufficiently cover the topic at hand.
[00:33:32] Pyramid principle this is another thing
[00:33:33] AI is very good at this stick to one
[00:33:36] idea per section if you can support it
[00:33:38] with evidence and then after that offer
[00:33:40] additional context and elaboration this
[00:33:42] is something that was popularized by
[00:33:43] Barbara Mento. He's a former McKenzie
[00:33:46] consultant and it's a great like
[00:33:47] thinking framework. Is each section
[00:33:49] appropriately weighted relative to total
[00:33:51] word count? Um, quite often, you know,
[00:33:54] bad content, the really interesting
[00:33:56] ideas will have like, you know, 50 words
[00:33:58] dedicated to them and the really boring,
[00:34:00] obvious stuff will have a thousand words
[00:34:03] dedicated to it. Um, I always try and
[00:34:05] make sure that's not the case and
[00:34:07] actually make sure the most important
[00:34:09] ideas have the greatest word count. Make
[00:34:10] sure it's balanced in that way. Do we
[00:34:12] deliver on what was promised in the
[00:34:14] title? And do the headers provide clear
[00:34:15] benefits and explicit advice? basically
[00:34:18] can you read the headers and understand
[00:34:20] what the article is about and get
[00:34:21] something useful just from the headers.
[00:34:23] >> So again very simple things that AI can
[00:34:26] actually follow in structured and can do
[00:34:28] and understand and very useful for
[00:34:30] improving the content.
[00:34:32] >> Okay, next step how to write for hrefs.
[00:34:34] Uh this is the the guidelines that we
[00:34:36] also already reviewed and also where you
[00:34:39] give some examples of the articles,
[00:34:40] right?
[00:34:41] >> Yeah, exactly that. And there's quite a
[00:34:43] lot of overlap in some of these. So I
[00:34:44] think I can probably like tighten up and
[00:34:46] uh simplify this process. Uh then I have
[00:34:49] a specific thing about how to mention HS
[00:34:51] products and features cuz obviously
[00:34:53] that's very important to the type of
[00:34:54] content we create cuz we're you know the
[00:34:57] business value is something we care
[00:34:59] about. We always try and promote it. So
[00:35:00] I think I've basically given it some an
[00:35:02] overview of we aim to educate generally
[00:35:05] but we also showcase HFS as part of the
[00:35:08] solution when it makes sense. You we try
[00:35:10] and do this in a very natural way. It
[00:35:11] should feel helpful and not overly
[00:35:13] promotional.
[00:35:15] And then I think I gave some examples of
[00:35:17] it. And what I have done is I've dumped
[00:35:19] a a summary of some uh core products so
[00:35:23] it can understand what they are and
[00:35:24] mention them. Uh I need to
[00:35:26] >> but also I remember that in your brief
[00:35:28] you're already giving AI kind of a
[00:35:30] direction of which products uh or which
[00:35:34] uh like HF's things uh can be mentioned
[00:35:37] in the article. So yeah it has overview
[00:35:39] of the product. So it can come up with
[00:35:40] its own ideas but you also specifically
[00:35:42] guided in the brief that uh I know uh
[00:35:45] Python for ICO it makes sense to mention
[00:35:48] HF's API because like that's the closest
[00:35:51] product that we can promote uh in in
[00:35:54] regards to this topic.
[00:35:55] >> I basically just mentioned the use cases
[00:35:57] that I think AI might not understand in
[00:35:59] the brief because generally it's quite
[00:36:01] good at saying oh mention keywords
[00:36:03] explorer because you've included the
[00:36:04] word keywords here and that kind of
[00:36:06] thing. How to line edit an article draft
[00:36:08] is the next step.
[00:36:09] >> So this is basically uh like final copy
[00:36:12] editing. Um I found this is not that
[00:36:15] important because generally AI is
[00:36:17] obviously quite good at writing things.
[00:36:19] You know they're not I'm not going to
[00:36:20] pick up massive typos and things but
[00:36:21] there are a few principles that can be
[00:36:24] useful.
[00:36:25] >> Um so just making sure that we open each
[00:36:27] section with a core idea. That's that
[00:36:28] bluff uh principle we talked about
[00:36:30] earlier. Um have we addressed the most
[00:36:33] obvious objections to this idea? So if
[00:36:36] we make a point, is it worth saying, you
[00:36:39] know, what is the common objection to
[00:36:40] this? Should I address that objection
[00:36:42] and mention why that's not actually a
[00:36:44] problem? Have we provided sufficient
[00:36:46] evidence? Um, have we used dense words?
[00:36:50] So use novel instead of something new,
[00:36:53] worldwide instead of on a global scale.
[00:36:56] Um, I think this is quite useful for
[00:36:58] getting rid of some of the kind of very
[00:36:59] AI flavored text that, you know, quite
[00:37:01] often comes out of AI outputs. Make sure
[00:37:03] we define any jargon or uh concepts we
[00:37:07] talk about. Use parallel formats for our
[00:37:09] headers. Uh that basically means the
[00:37:12] headers follow the same uh formulation.
[00:37:14] So it's very easy to read and
[00:37:15] understand. Is the sentence structure
[00:37:17] varied to sound pleasing to the reader?
[00:37:19] That's that classic uh you know writing
[00:37:22] is music Gary Provost quote that
[00:37:24] everyone likes screenshotting and
[00:37:25] sharing on LinkedIn.
[00:37:28] Have we included first person anecdotes
[00:37:30] and replace phrases that sound like AI?
[00:37:32] This isn't X, it's Y. It's more than X,
[00:37:35] it's Y. Their secret. That kind of
[00:37:38] thing. Um, I added this in very recently
[00:37:41] because a few of them still bleed
[00:37:42] through and it seems to be helping so
[00:37:44] far.
[00:37:44] >> Internal links. Oh, that that one is
[00:37:46] interesting. How does it how does it add
[00:37:48] internal links?
[00:37:49] >> Yeah. So, this is a very mixed bag. Uh,
[00:37:51] I basically say read through this
[00:37:52] article, find 10 relevant places to
[00:37:54] integrate uh existing HF's blog content
[00:37:58] as a link. It does a good job. It does
[00:38:00] it contextually. it finds a good place
[00:38:02] to mention it. I'd say about half of the
[00:38:04] links are completely hallucinated and
[00:38:06] made up. So, um I actually had Mail
[00:38:09] message me. He's in charge of our like
[00:38:11] WordPress setup uh to point out, hey,
[00:38:14] there's some weird broken links
[00:38:15] appearing in these recent articles. What
[00:38:17] happened here? And it's because I didn't
[00:38:19] pay close enough attention and I
[00:38:20] published hallucinated URLs.
[00:38:22] >> Speaking of reviewing your content, your
[00:38:25] AI generated content start to finish.
[00:38:28] >> Yeah, exactly that. Um, so I think what
[00:38:30] I could do here is I could probably just
[00:38:32] export a list of uh blog actual real
[00:38:34] blog post URLs maybe with like an AI
[00:38:37] generated summary of the page and ask it
[00:38:39] to pick from that list and that might uh
[00:38:41] that might do a better job there. To be
[00:38:43] honest, this is something that can be
[00:38:45] done after the article is published,
[00:38:47] right? Because uh in HF's inside audit,
[00:38:49] we have this link opportunities report
[00:38:52] uh which automatically finds which kind
[00:38:55] of keywords you can link to which
[00:38:57] articles uh on on your website. So maybe
[00:39:01] you don't even need to uh include it
[00:39:03] right away. Maybe you can ask it uh to
[00:39:07] to scrape the last I don't know 10 to 20
[00:39:10] posts. uh see what their topics are. See
[00:39:13] if there's the if these topics are
[00:39:15] mentioned in the article and maybe
[00:39:16] suggest linking something not just link
[00:39:19] it straight away but kind of get your
[00:39:21] confirmation again speaking about
[00:39:23] reviewing the AI output before like uh
[00:39:26] publishing it somewhere. Maybe this
[00:39:28] could be the process. Okay. Then we have
[00:39:30] metadata. I believe it's meta
[00:39:32] description and URL slug.
[00:39:35] >> Yeah, very easy, very simple. It just
[00:39:37] saves me, you know, like 2 minutes of
[00:39:40] thought and effort to do that.
[00:39:41] >> If there's something I hate about online
[00:39:43] publishing is writing a meta description
[00:39:45] for uh a post that I wrote. This is such
[00:39:48] a uh grueling task for me.
[00:39:51] >> Yeah, exactly that. Uh and then the last
[00:39:54] stage, yeah, just adding WordPress short
[00:39:55] codes. This is still something that
[00:39:57] takes the team a ton of time. So, we've
[00:39:58] tried a bunch of different ways to
[00:40:00] automate this. Uh I think we're quite
[00:40:02] close to this being solved now through
[00:40:03] some mechanism. Um, but yeah, that's it.
[00:40:07] That's effectively how to go from a
[00:40:08] keyword through to a publish ready
[00:40:11] article with the exception obviously of
[00:40:14] images which are still a really big part
[00:40:16] of content. I haven't tried to do any
[00:40:18] kind of uh, you know, AI generated
[00:40:20] imagery for these cuz a lot of what we
[00:40:22] rely on are like screenshots or real
[00:40:24] world examples. So that is still
[00:40:26] something that takes quite a lot of my
[00:40:28] time and thought to do to incorporate
[00:40:30] that into the finished draft. Well, this
[00:40:32] looks uh like a very good process.
[00:40:34] Actually, we we already uh kind of I I
[00:40:37] tried to poke some holes in it and I
[00:40:39] think we we found some opportunities uh
[00:40:41] where something can be simplified, where
[00:40:43] some steps can be merged, where
[00:40:45] something can be removed, something that
[00:40:47] can be done later. Um and yeah, I I
[00:40:50] already see some opportunities for
[00:40:52] automation, specifically the the pulling
[00:40:54] data from AI content helper, which
[00:40:57] studies kind of the articles that uh
[00:40:59] that you compete with. One one thing
[00:41:02] that we constantly discuss in our
[00:41:05] contingent content marketing department
[00:41:06] is if we're adding anything unique to
[00:41:09] the content or if we're just creating uh
[00:41:11] the the content uh that's that that is
[00:41:15] abundant on the internet already if
[00:41:17] we're adding anything else to the
[00:41:18] conversation. So, so I think that could
[00:41:21] be an interesting part of the process
[00:41:22] where
[00:41:24] uh I'm not sure at which step maybe in
[00:41:27] the beginning you would have an
[00:41:28] interesting idea. Well, your article did
[00:41:31] add it kind of inherently because you
[00:41:33] said look up Patrick's scripts and
[00:41:37] feature them in the article. So it
[00:41:39] doesn't just the article doesn't just
[00:41:40] generically say oh like SEO for Python
[00:41:44] for SEO is like a useful uh useful tool
[00:41:47] to be able to use but it actually gave
[00:41:50] examples of how uh our own Patrick our
[00:41:53] own teammate uh the the scripts he wrote
[00:41:56] and uh which tasks he's solving he's
[00:41:59] automating I think it's it adds kind of
[00:42:01] net new information to the topic of
[00:42:03] Python for so I think I'm not sure how
[00:42:06] to solve it with AI Can it can it kind
[00:42:09] of point out to you that like there is
[00:42:13] nothing new in this article? Like
[00:42:15] everything that that you're saying here
[00:42:16] has been said by by someone else. So
[00:42:18] maybe you should work harder to add
[00:42:21] something interesting to it. Uh yeah, I
[00:42:24] have no idea how to solve for that. But
[00:42:25] it seems to me pretty important for
[00:42:28] creating the content that people would
[00:42:30] want to I know follow you for because
[00:42:33] like people follow our blog and people
[00:42:35] follow us on social media because we
[00:42:36] come up with new stuff. not the stuff
[00:42:38] that they can read uh anywhere else.
[00:42:41] >> I think potent you could do something
[00:42:42] obviously we have the AI content helper
[00:42:44] suggestions which are a really good
[00:42:46] summary of how other articles already
[00:42:48] talk about the topic. Potentially you
[00:42:50] could use that as input to like a
[00:42:52] reasoning step with the LLM and say you
[00:42:55] know what is a relevant and interesting
[00:42:57] part of this topic that has not been
[00:42:58] covered or discussed here and consider
[00:43:00] adding that in. Obviously you want to
[00:43:02] make sure that you are still you're not
[00:43:04] just making something up. you're talking
[00:43:06] from an actual place of experience. But,
[00:43:08] um, yeah, we talk a lot about like
[00:43:10] information gain in our content, don't
[00:43:12] we? You know, what can we add in that
[00:43:13] isn't already out there. I I do think
[00:43:15] LLM can actually help with that.
[00:43:16] >> Awesome. Uh, Ryan, uh, thanks a lot for
[00:43:19] finally doing it. I've been pushing you
[00:43:21] to to share this process for a while,
[00:43:23] but I think this podcast interview was a
[00:43:25] perfect format to do it. So I think we
[00:43:28] will try to do it regularly as we come
[00:43:30] up with more uh different AI automations
[00:43:33] because yeah the the the world of
[00:43:35] marketing and and the world of SEO is
[00:43:37] changing and everyone is keen to learn
[00:43:40] how other teams and other people are
[00:43:42] implementing AI in their work. So uh
[00:43:45] yeah uh my my question to people
[00:43:48] listening this uh did you enjoy this
[00:43:50] episode? Do you want us to publish more
[00:43:52] of that? Uh, leave your comments,
[00:43:55] subscribe to uh, HF's podcast on
[00:43:58] different platforms and yeah, I'll see
[00:44:00] you in the next episode. Thanks a lot
[00:44:02] for sticking till the very end of this
[00:44:04] episode. I guess that means you enjoyed
[00:44:06] it, right? Because if you did, I have to
[00:44:09] ask you to subscribe to this YouTube
[00:44:11] channel or maybe click the follow button
[00:44:13] if you're listening to this on Apple or
[00:44:15] Spotify. Not sure if you know this, but
[00:44:18] subscriptions and follows are the
[00:44:20] strongest signal for these platforms to
[00:44:22] show this piece of content to more
[00:44:24] people. So, I would really, really
[00:44:26] appreciate it if you would follow and
[00:44:28] subscribe. Thanks in advance and I'll
[00:44:30] see you in the next episode. Why?
