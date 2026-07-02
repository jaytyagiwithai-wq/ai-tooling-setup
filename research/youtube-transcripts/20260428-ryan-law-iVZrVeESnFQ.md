---
expert: Ryan Law
title: How to automate blog writing with AI from keyword to published | Ryan Law (Ahrefs)
channel: Ahrefs Podcast
video_id: iVZrVeESnFQ
url: https://www.youtube.com/watch?v=iVZrVeESnFQ
published: 20260428
collected_at: 2026-07-02T20:06:49Z
tool: supadata
language: en
---

# Transcript

[00:00:00] So Ryan, I was thinking today, uh, it
[00:00:02] didn't take us too long to go from this
[00:00:05] AI thing cannot really do great content
[00:00:08] to, oh my god, this is amazing, right?
[00:00:11] And here we are. Uh, you have devised an
[00:00:15] AI content automation workflow that you
[00:00:18] use to actually publish quite a few
[00:00:19] articles on HF's blog already. And these
[00:00:22] are good articles. These are great
[00:00:24] articles. And yeah, full disclosure, I
[00:00:27] haven't seen it yet, so I'll be checking
[00:00:29] it out live together with uh anyone
[00:00:32] watching it, and I'm excited. Yeah. Do
[00:00:34] you want to say a few quick words on
[00:00:36] what people are about to see? Yeah.
[00:00:39] Well, exactly that. So, we've obviously
[00:00:41] been tinkering with using AI in our
[00:00:43] content workflows for years at this
[00:00:46] point, and it's always been very
[00:00:47] effortful. It can be helpful, but you
[00:00:49] have to sink a ton of time and energy
[00:00:51] into it. There's still a lot of manual
[00:00:52] stuff that has to happen. I kind of feel
[00:00:54] like that's not the case anymore. Uh
[00:00:56] it's a bit spooky actually. I think
[00:00:58] since Claude code is probably the big
[00:01:00] thing that has changed this this kind of
[00:01:02] agentic workflow where Claude can make
[00:01:04] some decisions on your behalf and you
[00:01:06] can provide it with some guard rails to
[00:01:08] actually make it do things in a certain
[00:01:10] way. Um so we've basically yeah built I
[00:01:13] call it the blog pipeline. Uh and it is
[00:01:16] a kind of content automation system for
[00:01:18] new articles and for content updates. Uh
[00:01:21] we've done maybe like 30 article updates
[00:01:24] with it so far. Um published maybe uh 10
[00:01:28] 15 articles. Got maybe something similar
[00:01:30] in progress at the moment.
[00:01:32] >> Um yeah, it's been pretty cool.
[00:01:35] >> Let's review it. Show it to me.
[00:01:37] >> Yeah, let's do it. Um so obviously two
[00:01:39] things on the screen right now. We have
[00:01:41] a terminal and we have Claude code
[00:01:44] running in that terminal. So that is
[00:01:45] just a folder that I've called blog
[00:01:47] pipeline and claude code is living in
[00:01:49] that folder and it will do stuff in that
[00:01:51] folder for me when I ask it to. Um and
[00:01:54] we've got VS Code over here. This is
[00:01:56] just a really good way of showing you
[00:01:57] the contents of that folder in a way
[00:01:59] that is a bit easier to understand. Uh
[00:02:02] these are all the folders on the left
[00:02:04] hand side and they've all got files
[00:02:05] inside them. And I of course I asked
[00:02:08] Claude I said I'm going to present this
[00:02:10] process on a podcast with Tim. give me
[00:02:13] some notes and visualizations to help
[00:02:14] explain this. So, it added a handy
[00:02:16] little podcast folder here uh that has
[00:02:18] some notes and visualizations to make
[00:02:21] this a bit more interesting.
[00:02:24] But the basic premise is uh we have
[00:02:27] basically set it up such that there are
[00:02:29] maybe 23 or so uh skill files in here.
[00:02:33] You can see them in this folder. Uh and
[00:02:36] skill
[00:02:36] >> 23 skill files. That's that's a lot.
[00:02:39] >> That is a lot. Um, and each of these
[00:02:42] skill files is basically a process. It
[00:02:44] is a process that at some point during
[00:02:46] creating content or updating content as
[00:02:48] a human, we generally do something like
[00:02:50] this or very similar to this. Um, and
[00:02:53] this is just a markdown document with
[00:02:56] very you lost me already. I I kind of
[00:02:59] know what skills are, but you lost me
[00:03:00] already. Let's start from the beginning.
[00:03:02] Where does the process start? What do we
[00:03:04] start from? Do we start from a keyword?
[00:03:06] Do we start from an idea? What's the
[00:03:07] first step with this?
[00:03:08] >> Yes. Uh so what you can do is so this is
[00:03:12] a keyword ideas CSV. Um it's obviously a
[00:03:15] bit hard to see in this format but
[00:03:18] basically we've even set up a a process
[00:03:21] right now where we can use the HF's MCP
[00:03:24] which is obviously a way for Claude and
[00:03:25] other LLMs to access HF's data and it
[00:03:28] will run a content gap analysis for us
[00:03:31] and I've then set up another process
[00:03:33] where it will review this list of
[00:03:34] keywords and prioritize them. Uh it
[00:03:37] looks
[00:03:37] >> Ryan, again, let me uh use my Eastern
[00:03:40] European politeness uh to bring you
[00:03:43] right to the point. We're not talking
[00:03:44] about keyword research. We're talking
[00:03:45] about creating content. So, let's say we
[00:03:47] have a keyword or a topic. Uh what do we
[00:03:50] do with it? We're not we're not talking
[00:03:51] about keyword research. We want to
[00:03:52] create content. Let me show you that. Uh
[00:03:55] let me clear this.
[00:04:01] Uh so, I can trigger blog pipeline. And
[00:04:04] I can put in a keyword like keyword
[00:04:06] opportunities.
[00:04:08] And if I want, I can add some context to
[00:04:11] it and explain, you know, if there are
[00:04:12] points I want to add, I can add that.
[00:04:15] And off claude goes. And probably
[00:04:17] somewhere from between 8 to 11 minutes
[00:04:19] from now, it will have a draft ready for
[00:04:22] review. Um, it goes through, yeah, about
[00:04:26] 12 steps at this point, as you can see.
[00:04:29] >> Oh, wow.
[00:04:30] >> It's actually It's actually telling me
[00:04:31] we've already It's so clever. it's not
[00:04:33] letting me do the same one that we've
[00:04:35] already done before. Um, so there's a
[00:04:38] research step, there's a reference step
[00:04:40] where it looks at existing articles on
[00:04:42] the HF's blog. There's an outlining step
[00:04:44] where it turns that into a structured
[00:04:46] outline. There's a like product
[00:04:48] annotation stage where we look for
[00:04:50] opportunities to mention specific HS
[00:04:53] products. There is a drafting phase, a
[00:04:56] citation phase for internal linking and
[00:04:58] finding supporting sources. There's a
[00:05:00] screenshot phase, which doesn't work
[00:05:02] very well, but we're working on that.
[00:05:04] Uh, a preview phase where you can
[00:05:06] actually preview how it would look on
[00:05:07] the blog. Uh, and then a formatting for
[00:05:10] publish phase where it will add in all
[00:05:12] the WordPress short codes, all the kind
[00:05:13] of stuff we need. Um so basically when
[00:05:18] you when you ask it to create uh a piece
[00:05:20] of content around a given keyword you
[00:05:24] are essentially uh launching a skill
[00:05:28] which is a combination of steps where
[00:05:31] each step is uh a separate skill and
[00:05:35] basically it has to finish them one by
[00:05:37] one or how does it work
[00:05:40] >> exactly that? Yeah. So what you can
[00:05:42] either trigger the skills individually.
[00:05:44] So if you just want an outline, you can
[00:05:46] just ask for an outline by triggering
[00:05:47] that skill. But I've created these kind
[00:05:49] of master skills and they are very
[00:05:51] simple. They exist just to tell Claude
[00:05:53] to work through the other skills in a
[00:05:55] particular order. Um so this one's
[00:05:57] called blog pipeline and there's also
[00:05:59] update pipeline. Uh and they literally
[00:06:01] yeah just stitch them together and make
[00:06:03] Claude systematically work through these
[00:06:05] processes. Okay. Uh let me go straight
[00:06:09] into the uh phase of being critical of
[00:06:14] this. Uh how is this not a slope? So
[00:06:17] what makes this process produce good
[00:06:20] content and not some generic stuff?
[00:06:25] >> Yeah. So that's a very good question. I
[00:06:27] think this definitely works best for one
[00:06:29] thing on topics that we have already
[00:06:31] covered in some capacity on the HF's
[00:06:34] blog. Um, so one we published recently,
[00:06:38] content gap. We have never written an
[00:06:40] article about content gap spec or is it
[00:06:43] keyword gap? One of these two, content
[00:06:44] decay and keyword gap. We've written
[00:06:46] loads about these concepts generally,
[00:06:48] but in slightly different contexts, but
[00:06:50] we've never specifically targeted that
[00:06:52] keyword. But because this uh is able to
[00:06:55] go and look up existing HF's articles
[00:06:57] and anchor the content generation
[00:06:59] process in what we've already written,
[00:07:02] uh that goes a long way to getting rid
[00:07:04] of a lot of the problems you'd have. Um
[00:07:07] and there are also some topics I think
[00:07:09] I'm mainly using this for very
[00:07:11] straightforwardformational topics,
[00:07:13] things that the LLMs know a lot about.
[00:07:15] Um there are opportunities for you to
[00:07:18] provide some context in it. Uh there's a
[00:07:20] particular step in here that looks for
[00:07:22] um opportunities to add information
[00:07:24] gain. So it actually reads the top
[00:07:26] ranking articles, summarizes the
[00:07:28] contents of them and make suggestions
[00:07:30] for ideas that are not covered but would
[00:07:32] be useful for the reader to understand
[00:07:34] within this.
[00:07:36] And I think AI is better at research
[00:07:38] than a person is as well. Um it can be
[00:07:40] faster and more systematic about it. It
[00:07:42] can go out and look up uh you know the
[00:07:44] latest research articles, the latest
[00:07:46] stats, all these kinds of things. Okay.
[00:07:48] So, we definitely cannot go through uh
[00:07:51] all of your skills uh in the course of
[00:07:54] this podcast episode because there is a
[00:07:56] lot of uh a lot of content in each of
[00:07:58] the skills. But I want you to uh start
[00:08:02] from the very first step of creating
[00:08:04] content and then go to the second and
[00:08:06] third and highlight maybe one or two
[00:08:10] kind of counterintuitive things. So, for
[00:08:12] example, what what might people get
[00:08:14] wrong if they would want to kind of
[00:08:16] recreate your process? Because uh I'm
[00:08:19] not sure that we want to just uh give
[00:08:20] out your process to everyone else if we
[00:08:22] want just like open source it and have
[00:08:25] everyone else have access to the same
[00:08:26] process. And I would imagine that people
[00:08:28] would want to uh make it uh personal to
[00:08:32] to them and their voice and their blog
[00:08:34] and the style of content that they want.
[00:08:36] But yeah, walk me through each step and
[00:08:38] tell me if you uncovered
[00:08:42] anything interesting about
[00:08:45] uh giving instructions to AI on how to
[00:08:49] kind of improve the output of this
[00:08:51] specific step if you know what I mean.
[00:08:53] >> Yeah. Yeah. Yeah. So you made a very
[00:08:55] good point there as well. I think the
[00:08:57] way we are using this is not as though
[00:08:59] this is the universal process that
[00:09:01] everyone the team has to follow. Um,
[00:09:04] we've actually set it up such that the
[00:09:05] team can fork their own versions of this
[00:09:07] repo. So, they can make their own
[00:09:09] version of this folder and they can
[00:09:11] modify it how they like. This version
[00:09:14] has examples of content that I like and
[00:09:16] my writing voice uh and it's used as
[00:09:18] part of the article generation process.
[00:09:20] It would be super weird if SQ or Louise
[00:09:23] uh did the same thing, used my writing
[00:09:24] voice for their articles. So, it's very
[00:09:27] easy to actually update it and
[00:09:28] personalize it. And part of that might
[00:09:30] be changing the steps it goes through
[00:09:31] your own personal preferences. Um, this
[00:09:34] is kind of very unique to me, I think,
[00:09:36] and that's kind of I think how this
[00:09:38] should be used. Um, another good point
[00:09:41] as well, you said you were surprised at
[00:09:43] how many steps there were in this
[00:09:44] process. I think that is actually a very
[00:09:46] very good thing. Um, the more steps you
[00:09:51] create, the more kind of introspection
[00:09:53] you have into the process, the better
[00:09:54] you understand it. uh the more
[00:09:56] opportunities you have to actually
[00:09:57] control and personalize how the content
[00:09:59] turns out. So one very important thing I
[00:10:02] learned very quickly obviously I could
[00:10:05] just set this process in motion and it
[00:10:07] would give me an article in 8 minutes
[00:10:09] and either it's good or it's bad. It's
[00:10:11] quite hard to work out how to fix and
[00:10:13] improve the process if you do that. So
[00:10:15] actually at every single step of the
[00:10:17] process um you can actually see it it
[00:10:21] will give me an output at every stage.
[00:10:23] So if something goes wrong, if I don't
[00:10:24] like the article or how it turned out, I
[00:10:26] can go back and see which part of the
[00:10:28] process it didn't work very well. I'm
[00:10:31] actually surprised that when you
[00:10:33] initially tried to launch this process,
[00:10:36] you said that you would wait like 8 to
[00:10:38] 12 minutes because I was expecting that
[00:10:40] you would actually babysit it from step
[00:10:44] to step. So you would see the output of
[00:10:45] the first step, see if you want to
[00:10:47] refine it, if if it's according to your
[00:10:49] expectations, and then allow it to go to
[00:10:52] the second step. But it's all just
[00:10:53] batched for you. And the thing is that
[00:10:56] that's actually an interesting tip. This
[00:10:58] is exactly what I was looking for, some
[00:10:59] tips for people of uh what they need to
[00:11:02] look for when they're building this
[00:11:04] themselves. And the tip is make sure
[00:11:06] that the process saves the output of the
[00:11:09] step. So if you don't like the final
[00:11:11] thing, you can go step by step and
[00:11:14] review at which step kind of it went
[00:11:17] sideways so that you could uh like give
[00:11:19] it more instructions or refine the the
[00:11:21] skill that that refers to the step uh
[00:11:24] and make it uh do over again and see if
[00:11:27] that would help. But yeah, I'm surprised
[00:11:29] that uh you let it run for like 8 to 12
[00:11:32] minutes. Is this the point that you
[00:11:35] trust it well enough? you like your
[00:11:37] steps or Yeah, probably it's that I I
[00:11:40] don't see any other reason why would you
[00:11:42] would just let it cook for so long and
[00:11:44] follow all the steps. Yeah, great point.
[00:11:46] Very importantly, this is uh actually
[00:11:49] months and months of refinement has gone
[00:11:51] into this thinking and the process in
[00:11:53] here and actually the last podcast
[00:11:54] episode we talked about where we had the
[00:11:56] custom GPTs, it was like the kind of
[00:11:59] baby version of this process. So a lot
[00:12:01] of the skills I have in here are things
[00:12:03] that we improved and refined and did
[00:12:05] handhold and babysit as part of that
[00:12:07] process. So we'd already written these,
[00:12:09] already tested these, already made
[00:12:11] dozens and dozens of article outputs
[00:12:13] with them and kind of learned to refine
[00:12:14] them. So the thing that Claude does very
[00:12:17] well is just stitching those together.
[00:12:19] Um actually automating that process.
[00:12:22] Okay, let's go step by step. The first
[00:12:24] step I think I see it though it is quite
[00:12:26] small is research, right? any like one
[00:12:28] or two tips to that you saw that would
[00:12:31] significantly improve the output of this
[00:12:34] step.
[00:12:34] >> So it does a combination of things.
[00:12:36] Maybe most people would assume you know
[00:12:38] keyword research is the most important
[00:12:40] thing to do and we have that in here. It
[00:12:42] goes and gets a bunch of HF's data from
[00:12:44] the MCP uh related keywords parent topic
[00:12:47] all this kind of thing.
[00:12:50] We don't have this yet but I've asked
[00:12:52] for it. What is more important I think
[00:12:54] is going and looking at the existing SER
[00:12:56] the content that is ranking and
[00:12:58] analyzing that and seeing the topics
[00:13:00] that are kind of consensus and commonly
[00:13:02] used there opportunities to
[00:13:04] differentiate from that um that is what
[00:13:07] AI content helper is perfect for doing
[00:13:09] but we don't have the endpoint for that
[00:13:11] yet so this does a kind of laborious
[00:13:13] manual version of that but what is ex
[00:13:15] what is exactly like what are you asking
[00:13:17] it to do do you ask it like open the top
[00:13:20] ranking articles for this keyword and
[00:13:23] what and and read them and summarize
[00:13:26] them. What do what do I ask it to do?
[00:13:28] Like give me something interesting about
[00:13:30] the research step. Yeah, let me try and
[00:13:32] find it. Here we go. This is the skill
[00:13:34] file.
[00:13:37] Um so it starts with keyword ideas.
[00:13:42] It gets uh primary keyword metrics and
[00:13:44] parent topic. Uh it finds longtail
[00:13:46] keyword variations that share the same
[00:13:48] parent topic.
[00:13:50] Uh there's some prioritization where it
[00:13:52] groups them together and discards ones
[00:13:53] that wouldn't fit the right intent.
[00:13:56] Pulls the questions report through the
[00:13:57] MCP as well. So we get commonly asked
[00:13:59] questions that people might have related
[00:14:01] to this topic. Groups them into question
[00:14:03] themes. So we're not just doing like FAQ
[00:14:05] spam.
[00:14:07] Uh we get the SER overview. We use that
[00:14:09] to go and look at the type of content
[00:14:11] that is ranking, the estimated traffic,
[00:14:13] all these kinds of things. Uh analyze
[00:14:15] the dominant search intent of the SER
[00:14:17] results. So we can see what type of
[00:14:19] content performs best. That's kind of
[00:14:20] going into this process. Uh and then it
[00:14:23] looks at the actual top ranking pages.
[00:14:25] So it uses web fetch. It retrieves the
[00:14:27] content. It extracts the headers. It
[00:14:30] summarizes them. It looks for themes and
[00:14:32] gaps in them. And yeah, creates content
[00:14:35] gaps and opportunities.
[00:14:38] Um and you can see an example of the
[00:14:39] kind of output. So it basically creates
[00:14:41] a report like a research report at this
[00:14:43] step. I don't have to see this, but this
[00:14:45] is what gets fed into Claude at the next
[00:14:47] stage of the process. Uh, so you got
[00:14:49] loads of keyword data, questions to
[00:14:51] answer, organic results. Uh, you know
[00:14:54] what? At this point, as I'm looking at
[00:14:56] how detailed and sophisticated these
[00:14:59] steps are, I want to say the word
[00:15:03] overengineered.
[00:15:05] M
[00:15:05] >> I'm actually wondering if you would like
[00:15:07] remove half of that, would it just do as
[00:15:10] good of a job?
[00:15:13] >> Yeah, quite possibly. And that is
[00:15:14] another really important part of this
[00:15:16] process. Um I'm always surprised at how
[00:15:19] good increasingly the most like uh
[00:15:21] frontier most up-to-date models actually
[00:15:23] are on their own without any input. Um
[00:15:27] so a big part of the testing and
[00:15:28] iteration we've been doing is to we've
[00:15:31] actually been writing um like test
[00:15:33] cases. We've been following this these
[00:15:36] steps with the skill file and without it
[00:15:39] and seeing whether the without version
[00:15:41] is actually good enough. Does the skill
[00:15:42] file actually add any benefit to it? Um
[00:15:46] a good number of cases the models do a
[00:15:48] very good job on its own and it just
[00:15:50] needs a little nudging in a particular
[00:15:52] direction. So, I expect as we continue
[00:15:54] to improve on these, these skill files
[00:15:56] and these outputs will just get simpler
[00:15:58] and simpler over time until they're
[00:16:00] distilled down to the handful of things
[00:16:01] that are very important for getting the
[00:16:03] output that we want cuz yeah, it's
[00:16:05] probably completely overengineered at
[00:16:06] this point, I think. But again, my brain
[00:16:10] wants some kind of structure to what
[00:16:13] we're trying to do. So the the structure
[00:16:16] I would uh so if I were building this
[00:16:18] process myself from scratch and they
[00:16:20] needed to start from research of
[00:16:22] competitors and I know that my
[00:16:24] competitors are the pages that are
[00:16:26] ranking uh at the top. Uh what I would
[00:16:29] tell uh AI or Claude specifically to do
[00:16:32] I would tell it to download all the
[00:16:34] content uh in the folder. uh and then
[00:16:37] yeah I would I would ask it to extract
[00:16:40] from each piece of content kind of the
[00:16:42] main themes and the main ideas and then
[00:16:44] I would ask it to cross reference those
[00:16:47] main themes and the main ideas between
[00:16:49] the articles and create me one master
[00:16:52] document with all of the kind of ideas
[00:16:56] stories interesting points uh from all
[00:16:59] of the content so my my output uh I I
[00:17:03] don't necessarily need like you had the
[00:17:04] people also ask questions and that
[00:17:06] stuff. I would just ask it to uh analyze
[00:17:09] articles and create kind of a blended
[00:17:12] master file with everything unique that
[00:17:15] is pulled from all the articles.
[00:17:16] Actually, I do a similar process right
[00:17:18] now when I when I prepare for podcast
[00:17:20] interviews uh with uh marketing leaders.
[00:17:23] What I do is I do a pretty similar
[00:17:25] thing. Uh I give Claude uh their
[00:17:29] previous interviews, links to their
[00:17:30] previous interviews on YouTube. It
[00:17:32] downloads the transcript and then it
[00:17:35] creates me for each of these transcripts
[00:17:37] because I don't want to read the whole
[00:17:38] thing. I want TLDDR too long didn't
[00:17:40] read. So I ask it extract the questions
[00:17:43] because questions are topics within the
[00:17:45] interview and then differentiate between
[00:17:47] uh main questions and follow-up
[00:17:49] questions where the host is digging uh
[00:17:51] more into this topic. So, uh, yeah, you
[00:17:54] know, like where the main question,
[00:17:55] where the follow-up question, and then
[00:17:57] instead of giving me the whole answer,
[00:17:59] uh, give me TLDDR, just a few sentences
[00:18:02] of what the guest replied, give me if
[00:18:04] there was any hot take, give me if there
[00:18:06] was any story, give give me if there was
[00:18:08] any specific number like, oh, we
[00:18:10] increased our leads by 300% or
[00:18:13] something. Uh, and I think there was
[00:18:15] something else, but I forgot about it.
[00:18:17] So, it creates me TLDDR for each of the
[00:18:20] interviews. And as the next step I ask
[00:18:22] it now create me a master TLDDR and this
[00:18:26] is what I would read uh while preparing
[00:18:29] for for the podcast interview because it
[00:18:31] would give me all the unique information
[00:18:33] from like a dozen interviews. So it
[00:18:36] feels that uh when I want to create a
[00:18:38] piece of content it's kind of the same.
[00:18:39] I want to know what has been said
[00:18:43] already by uh on this topic. So this is
[00:18:45] what I would include in the research
[00:18:47] phase. But uh yeah, you're giving it uh
[00:18:51] people also ask questions, parent
[00:18:52] topics, but it it feels that when you
[00:18:54] say that you're extracting kind of
[00:18:56] topics from a page, it feels the same
[00:18:58] what I'm doing when I'm extracting
[00:19:00] questions that a host asked uh my guest
[00:19:02] and then I do do you also ask it to
[00:19:04] create a master document with
[00:19:06] everything?
[00:19:08] Uh that is yeah basically that research
[00:19:10] document is the kind of um uh this is
[00:19:14] the research document it would hand over
[00:19:16] to the next step of the process.
[00:19:18] Okay. Uh we discussed research. What is
[00:19:20] the next step?
[00:19:22] So the next step uh uh HF's references.
[00:19:28] So how how does it work? So this was I
[00:19:31] actually added this very recently and
[00:19:32] this has been very helpful. Um
[00:19:36] Claude can do a good job writing an
[00:19:37] article on most topics. It can go and
[00:19:39] look up other content. That's all well
[00:19:41] and good. Um, I really wanted a part of
[00:19:43] the process where, you know, as a human
[00:19:44] writer, I would go and see what we
[00:19:46] already have on a topic because I want
[00:19:48] to make sure a new article is consistent
[00:19:50] with old things we've written. I want to
[00:19:52] interlink between them. Uh, I want to
[00:19:54] make sure the kind of framing is useful.
[00:19:55] I want to be efficient and make sure I'm
[00:19:57] not repeating myself. I can just pluck
[00:20:00] elements from existing articles. So this
[00:20:02] specifically looks up the target keyword
[00:20:04] to see what we have already published on
[00:20:06] that topic, what is already ranking for
[00:20:07] similar topics and it incorporates
[00:20:10] elements of that into the uh like
[00:20:14] outlining and generation process.
[00:20:17] Okay, it feels like it feels again I
[00:20:21] will try to uh explain it from my
[00:20:24] perspective. Uh I will try to kind of
[00:20:26] simplify the process. So it feels the
[00:20:28] same as research as the first step where
[00:20:31] you take the pages where you extract
[00:20:33] kind of unique information from them and
[00:20:35] you want to understand kind of the the
[00:20:37] overall topic coverage uh as pulled from
[00:20:40] like a dozen different pages and now
[00:20:43] what you're doing you're referencing our
[00:20:45] own content. So rather than searching
[00:20:47] which are the top 10 ranking pages for
[00:20:49] the topic, you're going and searching
[00:20:51] okay what relevant pages does hrefs does
[00:20:55] our website already have on this topic
[00:20:57] and can we pull something interesting
[00:20:59] from them and again cross reference with
[00:21:02] my master document if we're saying
[00:21:04] something unique uh that this master
[00:21:07] document is not saying and what's what's
[00:21:08] important is because our content is very
[00:21:11] productled and we try to fill our
[00:21:13] content with use cases of our tools and
[00:21:16] data often times the unique bits that uh
[00:21:20] AI can pull from our content on this
[00:21:22] topic are those use cases and you can
[00:21:24] even specifically instruct it so you can
[00:21:26] tell cloud so specifically look for
[00:21:28] whenever we're discussing this topic how
[00:21:31] are we uh teaching people to use our
[00:21:33] tools what kind of actionable use cases
[00:21:35] we're teaching them uh and then it would
[00:21:37] create you another document with like
[00:21:39] okay this is the master document of what
[00:21:41] all competitors are talking about this
[00:21:43] topic and these are unique unique
[00:21:45] insights that I saw published on your
[00:21:48] blog and here are unique I don't know
[00:21:50] use cases uh of your product that I saw
[00:21:52] in your articles uh on this topic. So is
[00:21:55] this more or less what you're looking
[00:21:57] for? Yeah, exactly that. And this step
[00:22:00] is quite simple as well. It's basically
[00:22:03] I wanted to provide a almost like a list
[00:22:05] of modules or sections that could be
[00:22:08] relevant to this topic that we have
[00:22:10] already covered so that when it comes to
[00:22:12] outlining and drafting Claude can go and
[00:22:14] look up these examples, incorporate
[00:22:16] those headers, uh link back to them as
[00:22:18] an internal linking step just make it
[00:22:20] kind of an integrated part of how we
[00:22:22] create content.
[00:22:24] >> Okay. And then we have next step.
[00:22:26] >> Yeah. And then onto the outlining phase.
[00:22:28] Um, so let's have a look see if I can
[00:22:31] find the skill for this one.
[00:22:33] So these are this is very similar to
[00:22:35] what we had in the uh custom GPTs. This
[00:22:38] is kind of the editorial process that
[00:22:40] when a writer puts together an outline,
[00:22:42] this is how I expect them to do it. Um,
[00:22:45] so it's got some very simple core
[00:22:47] concepts. Um, you know, every uh we must
[00:22:50] use the bluff principle. So, every
[00:22:52] section must open with the most
[00:22:53] important idea and then segue to
[00:22:56] examples, extra context, that kind of
[00:22:58] thing.
[00:23:00] Um, we need to make sure we're logically
[00:23:02] supporting the thesis. So, the headers
[00:23:04] must make sense within the context of
[00:23:06] the title you've created. We need to be
[00:23:08] exhaustive in how we cover the topic. We
[00:23:10] need to be mutually exclusive so we
[00:23:11] don't have loads of overlap between each
[00:23:14] of the sections. Um, and again, these
[00:23:17] are things that if you ask Claude to
[00:23:18] edit an article and make it me, it does
[00:23:21] a fairly good job of that. It has a good
[00:23:22] comprehension of what that means.
[00:23:25] Um, and then you can see, uh, an example
[00:23:28] out of an outline here.
[00:23:32] So, we've got hook, key points, uh, any
[00:23:35] ideas for transition it wants to include
[00:23:36] or a specific example it wants to
[00:23:38] include. It wants to include a table.
[00:23:41] Um, these are the bones of the article.
[00:23:45] you mention a very uh important word.
[00:23:47] The word is example.
[00:23:50] Uh I can give you uh a quick reference
[00:23:54] of why I'm talking about it. So I have a
[00:23:57] bunch of uh skills in my cloud code for
[00:24:01] creating LinkedIn posts. Uh
[00:24:04] for example, I have uh product based
[00:24:06] LinkedIn posts when I'm announcing a
[00:24:08] feature. I have uh podcast announcements
[00:24:11] when I'm announcing that I had a new
[00:24:13] guest on the podcast. Uh or just regular
[00:24:17] posts when I have an idea and I want to
[00:24:19] kind of deliver it in the best possible
[00:24:21] and punchy way. The thing is for like
[00:24:25] each of those is a separate skill that I
[00:24:27] have created and I have instructed uh uh
[00:24:30] clo code of what I'm looking for because
[00:24:31] when I'm announcing a podcast that's one
[00:24:34] format when I'm announcing a product
[00:24:36] update from HFS that's another format.
[00:24:38] when I want just to improve a random
[00:24:40] post that can be about anything that's a
[00:24:42] different set of instructions. But the
[00:24:45] thing is for each of those skills I have
[00:24:47] a folder where I I have given claude
[00:24:50] code a bunch of examples here are the
[00:24:54] examples of my previous podcast
[00:24:55] announcements. So that not only you have
[00:24:58] my instructions of how to write them,
[00:25:00] how to structure them, you have examples
[00:25:02] of how I did that in my voice already
[00:25:04] previously and also like those examples
[00:25:06] come uh also with engagement metrics. So
[00:25:09] it's it even sees which posts perform
[00:25:12] better, which post performed worse. Uh
[00:25:14] same for podcast announcements, same for
[00:25:16] product announcements, and same for
[00:25:18] random posts. So it always have uh a
[00:25:21] folder with examples to reference. And I
[00:25:23] almost feel like when it only has
[00:25:27] instructions
[00:25:29] versus when it has instructions and like
[00:25:32] five to 10 examples, I feel it does a
[00:25:36] better job when it has kind of the
[00:25:38] actual examples to fall back to. So when
[00:25:40] you're saying that this is there's a
[00:25:42] step of an outline, I almost want to you
[00:25:46] to have a folder where you have five
[00:25:48] examples of outlines of previous posts.
[00:25:52] We do have that somewhere. Is it
[00:25:54] templates?
[00:25:57] Yeah, somewhere we do have that. Maybe
[00:25:58] it's in part of the the skill files
[00:26:02] because exactly the same thing. I you
[00:26:04] know, we every time we generate
[00:26:06] something, we generally want it to maybe
[00:26:08] sound like us or sound a particular way.
[00:26:11] And I used to see a lot of people feed
[00:26:13] it writing and say, can you distill my
[00:26:15] writing down to a handful of principles
[00:26:17] that you can then follow? I was I was
[00:26:20] always very skeptical of that though
[00:26:21] like how can you reduce somebody's
[00:26:22] unique voice down to a handful of things
[00:26:24] that then Claude without that example to
[00:26:27] back it up can actually go away and do.
[00:26:29] I think what you you're right the much
[00:26:30] better thing to do is let the model
[00:26:32] infer itself from an actual example
[00:26:35] cuz you know your writing style I don't
[00:26:37] think is always going to map neatly
[00:26:39] across to a five bullet point lists of
[00:26:42] your writing style or whatever but
[00:26:44] Claude is a large language model. it can
[00:26:46] infer from large samples of text the
[00:26:48] patterns that do actually exist in your
[00:26:50] content and that is how it will end up
[00:26:52] sounding like you. So I totally agree
[00:26:54] anchoring it with an actual example and
[00:26:56] saying make it sound like and feel like
[00:26:57] this is actually pretty good from what
[00:27:00] I've seen. Yeah. And this is this is
[00:27:02] exactly how people should create those
[00:27:04] skills in the first place because the
[00:27:06] way I created my skills is I gave it a
[00:27:09] bunch of my previous podcast
[00:27:10] announcements. I said analyze these
[00:27:13] posts. tell me what I'm doing here, tell
[00:27:16] me what's my style. It would tell me
[00:27:19] like what it kind of inferred from uh
[00:27:21] reading my posts and I would correct it
[00:27:23] if I disagree somewhere. If if it
[00:27:25] doesn't feel like it understands what
[00:27:27] I'm doing, uh sometimes it would
[00:27:29] understand what I'm doing better than
[00:27:31] myself, which is funny. I'm like, "Oh,
[00:27:33] that's that's really what I'm doing. I
[00:27:35] just I I was doing it subconsciously. I
[00:27:37] didn't understand that." And then for
[00:27:39] example uh speaking of podcast
[00:27:41] announcements I would give it some
[00:27:42] podcast announcements from Lenny
[00:27:45] Richitzky how he announces his podcast
[00:27:47] interviews on LinkedIn and I would say
[00:27:48] okay analyze what Lenny is doing here.
[00:27:51] Uh it would analyze what Lenny is doing
[00:27:53] again I would correct if I disagree with
[00:27:55] something and then I would say now
[00:27:57] create kind of something in between
[00:27:59] something between my approach and
[00:28:01] Lenny's approach and tell me what set of
[00:28:03] instructions you would come up with. So
[00:28:05] basically I'm not creating instructions
[00:28:07] myself. I don't need to write out
[00:28:08] instructions. I'm giving it examples.
[00:28:10] I'm telling I'm telling it analyze and
[00:28:13] tell me what you see like what's the
[00:28:15] kind of principles behind this piece of
[00:28:17] content. And then I would correct it. If
[00:28:20] I disagree with something, I would
[00:28:21] monitor what what instructions it is
[00:28:23] creating for itself and I would correct
[00:28:25] it. And then like I said, it's very
[00:28:27] important to have those examples for it
[00:28:29] to fall back on. Uh because then I just
[00:28:32] I just feel the output is always better.
[00:28:35] Okay. So that's outlining step. Uh like
[00:28:37] you said, you you do have some outline
[00:28:39] examples. Actually, it's as easy as uh
[00:28:42] asking Claude, hey, outlining step. Uh
[00:28:44] tell me, do we have examples for it? How
[00:28:46] are they stored? Are they stored in a
[00:28:48] text document? Are they stored in a
[00:28:49] folder? And it would tell you. And if
[00:28:51] you don't, you can just say, okay, then
[00:28:53] create this folder, add these examples,
[00:28:55] and cross reference it. So, yeah. uh a
[00:28:58] lot of people kind of
[00:29:01] I'm not sure if I can use the word
[00:29:03] overengineer but they overthink they
[00:29:05] overthink what is AI but it's like as
[00:29:07] easy as just talking to it asking it
[00:29:09] questions like how did you do this how
[00:29:11] did you do that and guiding it uh well
[00:29:14] of course if you have a good idea of
[00:29:16] what you want to achieve but it's very
[00:29:17] important to be able to break the
[00:29:19] process into kind of uh smaller steps
[00:29:23] into building blocks so to say
[00:29:26] >> okay Next, after outline, what's the
[00:29:28] step?
[00:29:29] >> So, now what we do is we look at the
[00:29:31] outline we've created and we ask Claude
[00:29:33] to find specific opportunities to
[00:29:36] mention relevant HF's products. Um, I
[00:29:39] tried, you know, having this integrated
[00:29:41] into other steps and it was a bit hit
[00:29:43] and miss. And this is obviously
[00:29:44] something that really matters to us
[00:29:45] because this is why we write content. We
[00:29:48] want to talk about the product in
[00:29:49] context where it makes sense to do that.
[00:29:51] So, this is a discrete stage. This will
[00:29:53] do this every single time. Um
[00:29:57] uh you know it's very simple cuz within
[00:29:59] the skill I actually have a kind of
[00:30:01] master list of HFS products and features
[00:30:04] which I asked Claude to create for me
[00:30:06] and then I updated and tweaked myself to
[00:30:09] include like newer ones add some
[00:30:10] features. So it goes to that and it
[00:30:12] looks at the outline. It says which of
[00:30:14] these can I contextually mention in this
[00:30:17] outline and have it make sense, have it
[00:30:19] be useful for the reader. And it just
[00:30:21] adds a little signpost for the next
[00:30:22] step. Uh so that when it comes to
[00:30:24] drafting, it knows to actually
[00:30:25] incorporate HFS into it.
[00:30:28] You know, keyword explorer, that kind of
[00:30:30] thing.
[00:30:32] And again, probably this is not
[00:30:33] something that people need to write
[00:30:35] start to finish themselves. Just drop
[00:30:38] links to your landing pages to your
[00:30:40] video overviews. Ask it to analyze it
[00:30:43] and tell it tell you what the product
[00:30:45] is, what is it, what is it good for,
[00:30:47] what are the top use cases, what are the
[00:30:49] like uh use cases for I don't know for
[00:30:52] this area, for that area and then you
[00:30:54] just correct it. So yeah, it's actually
[00:30:57] those things are easier to create than
[00:30:59] than uh people might think.
[00:31:02] >> Yeah, exactly. We've got site audit,
[00:31:04] rank tracker, content explorer. Uh
[00:31:06] Claude did most of the heavy lifting
[00:31:08] here. I just reviewed it. Um and I added
[00:31:10] in some I need to add in like fire hose
[00:31:12] and things like that actually. Um but
[00:31:16] again, Claude can do all this for you.
[00:31:17] It's a fantastic diligent worker. Uh and
[00:31:20] then after that is the drafting stage.
[00:31:23] Now I think when most people would do
[00:31:24] like an AI content process, this is
[00:31:26] probably the only stage they would
[00:31:28] create. And certainly when I've talked
[00:31:29] to people, this is all they do. they
[00:31:31] focus on what are the best prompts for
[00:31:33] making an article. But yeah, from all of
[00:31:36] our trial and error, I think having tons
[00:31:37] of steps for research and structure
[00:31:39] before you get to writing is what ends
[00:31:41] up giving you the best outcome. Um,
[00:31:45] and this is again similar to the writing
[00:31:48] rules we had in our previous GPT. It
[00:31:50] just has some this is adapted from our
[00:31:52] own internal writer like style guide for
[00:31:54] writing. You know, use the problem,
[00:31:56] agitate, solution uh formula. Here's an
[00:31:59] example of it in action as part of the
[00:32:01] introduction that works pretty well.
[00:32:03] Some structural stuff that inverted
[00:32:06] pyramid uh always explain what and why
[00:32:10] uh all these very simple things and
[00:32:12] draft very well
[00:32:15] >> draft is not a final step right is not
[00:32:18] the final step.
[00:32:18] >> So what goes after draft?
[00:32:21] So uh as we have a kind of verify claims
[00:32:26] stage um internal linking is very
[00:32:29] important for us and for SEO and also
[00:32:32] making sure we have included useful up
[00:32:35] to-ate sources for everything that we
[00:32:37] do. So there is a particular step in
[00:32:38] here that it actually goes through the
[00:32:40] draft and it looks for the claims
[00:32:43] things you know claims that the article
[00:32:45] is making that we would need to go out
[00:32:47] and validate and it makes sure that it
[00:32:49] has an upto-date source for that or it
[00:32:52] update it reviews it to see if it's
[00:32:54] accurate or not. Um and actually I've
[00:32:57] been working on this updating this skill
[00:33:00] because this is a big part of our
[00:33:01] content updating workflow. We want to go
[00:33:04] back to old articles, find all the
[00:33:05] claims, make sure they have the most
[00:33:06] up-to-date uh validation and accurate
[00:33:08] stats for it. Uh so that's the next step
[00:33:11] of that process there.
[00:33:13] >> And there's there's more steps after
[00:33:15] this.
[00:33:16] >> Yeah, not too many more. Um so we have
[00:33:19] uh a preview stage. So at this point, I
[00:33:21] wanted to be able to look at the draft
[00:33:23] uh and sadly check it and see if I was
[00:33:25] happy with it. And it's not always I
[00:33:27] don't like looking at markdown files
[00:33:29] like this. So, it actually generates a
[00:33:30] HTML file that is styled to look like
[00:33:33] the HF's blog. And I can then open that
[00:33:36] up in my browser just to like see what
[00:33:38] it would look like and feel like on the
[00:33:40] blog so I can quickly review it from
[00:33:42] that point of view.
[00:33:44] And the thing that still takes a ton of
[00:33:46] my time that I'm trying to work on is uh
[00:33:49] screenshots.
[00:33:50] So much of our content is productled. It
[00:33:52] involves using the HF's product.
[00:33:54] Screenshots are so important for that.
[00:33:57] At the moment, what this does is it will
[00:34:00] uh suggest a report uh that we can
[00:34:03] actually go and visit and take a
[00:34:05] screenshot of. And we actually have
[00:34:07] another skill that other people on the
[00:34:09] in the company have built which allows
[00:34:11] the claw to structure correct URLs for
[00:34:14] our reports. So it can actually generate
[00:34:16] a genuine report URL for you to visit in
[00:34:19] HFS and then I can take a screenshot of
[00:34:21] that.
[00:34:22] >> So that's quite useful. I'm trying to
[00:34:24] automate that with some headless browser
[00:34:25] stuff and some screenshotting and that
[00:34:27] kind of thing. Um, but at the moment I
[00:34:30] spend as much time doing the screenshots
[00:34:32] as I do actually editing, reviewing,
[00:34:34] generating. So that's a big part of it.
[00:34:37] Okay. Uh, since my my job on this
[00:34:40] podcast and in our calls is to
[00:34:43] essentially criticize everything you do.
[00:34:47] What a fun job. people would would uh
[00:34:49] think I'm a terrible person, but it is
[00:34:52] what it is. To be honest, one one step I
[00:34:55] I uh expected to see in this process is
[00:35:00] when you would uh kind of dictate to
[00:35:05] this system some of your thoughts of
[00:35:07] where to take this article in free form
[00:35:10] and I would explain uh why ah you have
[00:35:13] it or something. You you're pointing
[00:35:14] something out.
[00:35:15] >> I do indeed. Yeah, I kind of glossed
[00:35:16] over it. Um, I totally agree. Sometimes
[00:35:19] you just want to provide a few sentences
[00:35:21] of thought or direction. You want to
[00:35:22] mention a specific product and you don't
[00:35:24] trust that it will do it itself. So, one
[00:35:27] of the things I added recently was this
[00:35:28] context trigger. Um, so this right at
[00:35:31] the get- go when you trigger the
[00:35:32] workflow, you can provide it with as
[00:35:34] many sentences of context as you would
[00:35:36] like and that is then used to shape and
[00:35:38] inform the rest of the process. Um, so
[00:35:41] often I'll say cover this topic or this
[00:35:43] topic or review this existing article
[00:35:45] and bring elements of that into it or
[00:35:47] mention this new product and that kind
[00:35:49] of thing and it's just a little
[00:35:51] directional nudge and again that seems
[00:35:53] to be very useful for getting a good
[00:35:54] outcome from it. Uh, I think it's like a
[00:35:58] critical step in my opinion. Again uh we
[00:36:01] are still in the very early days of all
[00:36:04] that. We're still experimenting and I
[00:36:06] like I have thought so many thoughts uh
[00:36:09] in regards to all this. So first of all,
[00:36:10] I think it's important to point out that
[00:36:13] what you just showed is a work in
[00:36:15] progress because any any kind of skill,
[00:36:18] any kind of workflow that you build for
[00:36:20] yourself uh in cloud code or any other
[00:36:23] AI, it shouldn't be set in stone. Every
[00:36:26] time you run it and every time you
[00:36:28] analyze the output whether total output
[00:36:31] or whether output of the steps and you
[00:36:33] don't like something you need to go and
[00:36:35] refine and you keep refining and
[00:36:37] refining and you're basically teaching
[00:36:39] your AI workflow AI agent AI skills
[00:36:43] skill to do a better job and with every
[00:36:45] run it would get better and better. Uh
[00:36:47] so this is the first point. The second
[00:36:48] point I feel this uh this this step of
[00:36:51] giving it context is super important
[00:36:55] because it is what will essentially make
[00:36:59] your content unique because again uh the
[00:37:03] reason why I was also surprised that you
[00:37:04] would let it run for 8 minutes and just
[00:37:06] generate something for you is because I
[00:37:09] would expect that uh you would get a
[00:37:11] TLDDR file from the top competitors. you
[00:37:15] would go through it and you would just
[00:37:16] like in free form uh I'm I'm using
[00:37:18] whisper flow this thing to dictate into
[00:37:21] into anywhere basically in text all the
[00:37:23] time and I would just click a button and
[00:37:25] I would say oh like so I disagree with
[00:37:28] this part I think this part is good
[00:37:30] don't even mention this part is not
[00:37:32] important here is where I think you can
[00:37:34] and you can give it a lot of
[00:37:36] instructions it's almost as when we had
[00:37:38] those uh content mastermind calls where
[00:37:40] we would discuss ideas and we would
[00:37:42] brainstorm where to take every idea
[00:37:45] In the same way that we were giving each
[00:37:47] other feedback and uh kind of figuring
[00:37:50] out what angle is best to take uh with
[00:37:53] uh any given content idea in the same
[00:37:56] way you can provide uh feedback to or
[00:38:00] context to AI and I feel it would it it
[00:38:03] typically would do a great job at doing
[00:38:06] this
[00:38:08] >> and that very another very good point
[00:38:10] maybe I'll talk briefly about how I
[00:38:12] think conceptually this process should
[00:38:13] be use for content marketing generally
[00:38:16] like this is not the HF's content
[00:38:18] process going forward. It is not as
[00:38:20] though everything we create has to come
[00:38:21] through this or will come through this.
[00:38:23] Um we spend a lot of time writing stuff
[00:38:26] that is AI is still not very good at
[00:38:28] helping with things that require tons of
[00:38:30] thought and experience and unique
[00:38:32] perspectives and ideas that maybe other
[00:38:34] people haven't even shared before. I
[00:38:36] think this is really useful because, you
[00:38:39] know, we've written literally thousands
[00:38:41] of articles over the years. And what I
[00:38:44] see being really important for us going
[00:38:45] forward is having this well-maintained
[00:38:47] library of evergreen search content. I
[00:38:50] want to make sure we cover all the core
[00:38:51] topics that relate to our product and
[00:38:53] how to use it, keep them updated. And a
[00:38:55] lot of times that is very simple, quite
[00:38:57] repetitive stuff like how many ways are
[00:38:59] there to do keyword research? Quite a
[00:39:01] few as it turns out. So I think this is
[00:39:04] really good for topics you know we have
[00:39:06] tons of information documenting keyword
[00:39:08] research and all these kinds of topics
[00:39:10] that can be used to inform this process.
[00:39:13] This is almost like you know doing our
[00:39:14] housekeeping for us in some sense. Um
[00:39:17] it's not something that requires a ton
[00:39:19] of direct involvement guidance because
[00:39:21] we've already done that. We've written
[00:39:22] dozens of articles on these topics that
[00:39:24] is using used to shape these articles
[00:39:27] now. Um, and you know, I've generated
[00:39:29] tons of articles from this that were I
[00:39:31] could have published and would have been
[00:39:33] fine, but I didn't know enough about
[00:39:35] them. I didn't think they were
[00:39:36] interesting enough, and I've chosen not
[00:39:37] to do that because I still deeply care
[00:39:40] about everything we publish and I'm I
[00:39:41] want to make sure we put out the best
[00:39:43] thing we can.
[00:39:45] So yeah, I feel this process and the
[00:39:48] reason why kind of you let it run on
[00:39:50] itself with little output, it feels that
[00:39:53] it's best used to take some kind of what
[00:39:56] we call a general knowledge topic and
[00:39:59] adapt it to us because one of the steps
[00:40:02] it pulls from our existing content and
[00:40:04] it finds what kind of unique stuff we
[00:40:06] said. Then it finds the the way to uh
[00:40:09] include HFS in our use cases in this
[00:40:11] post. So basically for example there's
[00:40:14] plenty of information about link
[00:40:16] building but it doesn't necessarily
[00:40:19] share what we have shared about link
[00:40:21] building and it doesn't necessarily
[00:40:23] makes good use of HF's tools when it
[00:40:25] comes to link building. So with this
[00:40:27] automated process this is where you
[00:40:28] don't need to write something from
[00:40:30] scratch. You can analyze existing
[00:40:31] content and AI can find a lot of
[00:40:34] information from our existing articles
[00:40:36] and from our tools to include in the
[00:40:38] post and yeah you have uh the post
[00:40:40] ready. Am I right?
[00:40:43] >> Yeah, exactly that. Yeah. I like to
[00:40:45] think, is this a boring topic that I
[00:40:47] don't want to write? Um because we've
[00:40:49] covered it a thousand times. If so,
[00:40:51] maybe it's a good candidate for the AI
[00:40:53] process, which is not everything we
[00:40:56] publish
[00:40:58] >> in that regard. Uh oh, you have you have
[00:41:01] some something else to say.
[00:41:02] >> Yeah. So, very briefly, I because it
[00:41:03] kind of ties on to this. I'm also we
[00:41:05] built a content updating pipeline. This
[00:41:07] is a bit newer. I'm still tinkering with
[00:41:09] this but in a similar you know we have
[00:41:11] yeah thousand published articles for
[00:41:12] example and it's very hard for human
[00:41:15] people to keep on top of that keep them
[00:41:17] updated so we're working on a similar
[00:41:19] process here that is designed to
[00:41:21] basically periodically give you updated
[00:41:24] content to review and edit and approve
[00:41:26] and potentially publish um and very
[00:41:29] similar thing there are basically three
[00:41:31] things this does it looks for claims
[00:41:34] that might be outdated so there's an old
[00:41:37] stat or something that doesn't make
[00:41:38] sense, Claude will review it and try and
[00:41:40] find a new version of that and allow you
[00:41:42] to accept it if you want to. Um, you can
[00:41:45] find opportunities to add new hrefs
[00:41:47] product features. So, obviously some of
[00:41:49] our articles were published like 8 years
[00:41:51] ago. They don't mention our latest
[00:41:53] products like fire hose or you know uh
[00:41:55] AI content helper. This can make
[00:41:57] recommendations for you. And lastly,
[00:42:00] updating topic gaps. So this is where it
[00:42:02] looks at the SER and it says, "Is there
[00:42:03] anything that has other articles talk
[00:42:06] about that we don't? Perhaps we should
[00:42:07] draft a section for you to review and
[00:42:10] edit and include." And it just makes,
[00:42:12] you know, very boring um unstructured
[00:42:14] process a bit more organized and a bit
[00:42:16] more um fun for people to engage with. I
[00:42:19] think I I really really like where all
[00:42:22] of this is going because I think this is
[00:42:24] actually the future of how content is
[00:42:26] going to be created. And uh I wanted to
[00:42:29] wrap wrap this up from a different
[00:42:32] perspective because you essentially
[00:42:33] shared a workflow of how uh to create
[00:42:36] content on what you call like a boring
[00:42:38] topic, something that has been covered
[00:42:40] over and over and we just have like some
[00:42:43] unique spin or we want to cover this
[00:42:45] topic and include our products and
[00:42:47] services. I wanted to to share a quick
[00:42:49] story uh from the other side when you
[00:42:51] want to create something completely
[00:42:53] unique. uh and that is uh so I'm in the
[00:42:56] process of writing a book as I mentioned
[00:42:58] many times on this podcast already and
[00:43:01] uh just 8 months ago I was complaining
[00:43:04] to uh a bunch of our team members that
[00:43:07] it is very hard for me to context switch
[00:43:09] because when I stop working on the book
[00:43:11] and I do some like projects uh inside
[00:43:15] HFS and then I need to return to the
[00:43:17] book like a few weeks later I barely
[00:43:19] remember what I was writing about I
[00:43:21] barely remember my train of thought and
[00:43:23] it's almost like I need to upload all
[00:43:24] the information from scratch and uh I
[00:43:28] think it was further who said uh why
[00:43:30] don't you just upload like all your
[00:43:31] chapters to AI and kind of ask it to
[00:43:34] guide you like AI would ask like a
[00:43:36] journalist or a ghost writer who would
[00:43:37] be interviewing you asking you questions
[00:43:39] and would be kind of writing the book
[00:43:41] for you it was 8 months ago about 8
[00:43:43] months ago and I said I cannot see how I
[00:43:47] would be able to do that so back in the
[00:43:49] day we didn't have cloud code back in
[00:43:51] the day like Chad GPT just released
[00:43:53] their custom GPTs or something. I
[00:43:55] couldn't see how I would upload like my
[00:43:58] entire book and be able to work with it.
[00:44:01] Fast forward eight months and the last
[00:44:03] chapter of my book, I just finished the
[00:44:05] the draft. The last chapter I wrote it
[00:44:07] with AI by dictating my ideas into cloud
[00:44:10] code and my process was I told it, okay,
[00:44:13] the name of the chapter is this. What is
[00:44:16] going to happen is you're going to
[00:44:17] create a folder with my random
[00:44:19] dictations because I have a list of
[00:44:21] notes. what I want to say uh within this
[00:44:23] chapter and those notes exist in the
[00:44:25] form of three words or one sentence
[00:44:29] basically talk about this or expand on
[00:44:31] this idea and I would hit a button and I
[00:44:34] would just ramble. So there's this idea
[00:44:37] and they wanted to say blah blah blah
[00:44:39] and we like did this thing at HS and we
[00:44:42] have this interesting story blah blah
[00:44:43] blah dictation over next idea and I was
[00:44:47] just uh rambling on each of my ideas. I
[00:44:50] had a few dozen of them. Okay, it saved
[00:44:52] that to the folder. And I said, okay,
[00:44:54] I'm also like one talking when talking
[00:44:56] about those ideas, I was referencing a
[00:44:58] few things. Some of the things that I
[00:45:00] discussed with some other marketing
[00:45:01] leaders on the podcast, some of the
[00:45:03] things that we actually covered on HF's
[00:45:04] blog, for example, we have an article
[00:45:06] about taste and I just said, "Oh, like
[00:45:08] I'm talking about taste in in my chapter
[00:45:10] and you have my voice dictation with my
[00:45:12] ramblings about it, but we also wrote a
[00:45:15] nice post. Please include it as sources
[00:45:17] when talking about taste." So I gave AI
[00:45:20] I gave it all my dictations and I gave
[00:45:23] it all the resources that I remembered
[00:45:25] like different uh YouTube videos,
[00:45:27] interviews, different articles that I
[00:45:28] want to reference etc. Even some
[00:45:30] LinkedIn posts that I saw from people
[00:45:32] who are sharing these ideas and then I
[00:45:35] said okay now the general idea of this
[00:45:39] chapter is this. I'm trying to make a
[00:45:42] point that blah blah blah blah blah now
[00:45:45] you know like all my dictations now you
[00:45:47] know all my resources all the stories I
[00:45:49] want to tell me how would you connect
[00:45:52] the dots how would you structure it so
[00:45:55] essentially create me an outline and it
[00:45:58] would write me oh so I suggest that you
[00:46:00] lead with this story then it transitions
[00:46:02] well this and then this argument and
[00:46:04] then these things blah blah blah at
[00:46:06] which point I would say like I would
[00:46:08] give it some feedback where change it or
[00:46:10] not or I would say sounds good to me
[00:46:13] write it and it would write a chapter
[00:46:16] for me and then I also like uh uploaded
[00:46:18] to cloud code. I uh I downloaded from
[00:46:20] Google documents all my previous
[00:46:22] chapters and I said okay for each
[00:46:24] chapter create kind of a synopsis file
[00:46:27] what this chapter is about what are the
[00:46:29] key arguments that I'm making and what
[00:46:31] is the TLDDR outline of a chapter what
[00:46:33] are the main stories and key ideas and
[00:46:35] I'm sharing so for each chapter it
[00:46:37] created this file kind of with a recap
[00:46:39] of the chapter and then I said now refer
[00:46:41] to all the files of all the chapters and
[00:46:44] create me a synopsis of the book I want
[00:46:46] to know like what the book is about how
[00:46:47] it is structured and what is illogical
[00:46:49] ical and it is so good. It's like it's
[00:46:52] literally like you're you're offloading
[00:46:55] some of your brain work to someone else
[00:46:57] like you have an external brain that
[00:46:59] processes information for you. So this
[00:47:02] is why kind of when when we started
[00:47:05] talking and when you shared that you
[00:47:06] created a system for uh creating uh blog
[00:47:10] post fast and you said that your
[00:47:12] productivity increased that you
[00:47:13] published like three articles in a few
[00:47:15] days or something like that. I am
[00:47:17] actually expecting that all of the
[00:47:20] content that we're going to create, it
[00:47:22] would go through AI that we will no
[00:47:25] longer manually write stuff. We would
[00:47:28] just hit a button. We would ramble to AI
[00:47:30] what we want to say. We would point it
[00:47:32] at like whatever resources we want to
[00:47:35] use to make a point and it would help us
[00:47:38] write even a better article because its
[00:47:40] ability to connect the dots and
[00:47:42] understand what you're saying is
[00:47:45] actually quite crazy. I'm very surprised
[00:47:48] how well it was able to distill my
[00:47:50] ramblings into coherent ideas and
[00:47:54] connect the dots between them and
[00:47:56] organize it in a way where I'm like,
[00:47:58] "Wo, this actually looks quite good." So
[00:48:02] yeah, uh the process that that we just
[00:48:04] covered uh in in this podcast is uh
[00:48:07] mostly for kind of semi-automated
[00:48:09] content. you still want to like overlook
[00:48:11] it and like like you said you have a
[00:48:13] step to give it context of where you
[00:48:14] want to take it and what's the unique
[00:48:16] angle and stuff like this but it's still
[00:48:18] like you're you're offloading the
[00:48:20] majority of the work while I think going
[00:48:24] forward creating content yeah AI would
[00:48:28] act like a journalist an editor a ghost
[00:48:30] writer and you would act as a source of
[00:48:33] ideas and opinions and people who don't
[00:48:36] have a good writing skill but have
[00:48:38] strong opinions would be able to publish
[00:48:40] their content fast. So, what are your
[00:48:42] thoughts on this?
[00:48:43] >> Yeah, I totally agree with that. Um, I
[00:48:46] always find some people think that human
[00:48:48] creativity is too unique and magical and
[00:48:51] special that like AI could never help
[00:48:53] with it and never be a useful aid in
[00:48:54] that process. But actually, there's a
[00:48:56] lot of mental drudgery we do when we're
[00:48:58] writing a book or an essay or anything
[00:49:01] like that. I think the ideas, the
[00:49:03] motivations, the experiences, the things
[00:49:05] we care about, that is still uniquely
[00:49:07] you in your book. still your book and
[00:49:09] your ideas. Yeah.
[00:49:10] >> But all you just sitting down for hours
[00:49:12] and shuffling these ideas about and
[00:49:14] working out what are the common themes
[00:49:16] that is something that AI is fantastic
[00:49:18] at doing.
[00:49:19] >> Um yeah, if it can make these writing
[00:49:22] and creative processes more fun for us,
[00:49:24] then like that shouldn't be scary. I
[00:49:26] think that should be fun. We'll be more
[00:49:27] prolific. We'll share more stuff.
[00:49:29] There'll be more of our unique thoughts
[00:49:30] and ideas out in the world. Um, so if
[00:49:34] yeah, for all the kind of like sad
[00:49:35] drudgery and you know, are we automating
[00:49:37] careers and jobs away? Actually, we
[00:49:38] could create more cool stuff than has
[00:49:40] ever existed before in human history.
[00:49:42] It's totally possible. Now, I I like I
[00:49:45] like the word drudgery. I think what
[00:49:47] what AI does, it it literally eliminates
[00:49:50] drudgery because like I said, for me, it
[00:49:52] was a pain to go back and to because I
[00:49:56] would need to read my entire chapter
[00:49:58] again to remember what I was saying
[00:50:00] there. And now I can say remind me what
[00:50:02] was the synopsis of the chapter where we
[00:50:04] left off. Uh which ideas need work. It
[00:50:07] would tell me all that and I'm like
[00:50:08] immediately I can continue working and I
[00:50:11] can pick up where we left off. So yeah,
[00:50:13] let's let's not make it longer than uh
[00:50:16] than we need. Uh thanks a lot for
[00:50:18] sharing your uh process. Thanks a lot
[00:50:21] for as always letting me to jump in with
[00:50:23] my thoughts and ideas. Uh I generally
[00:50:26] think we're on the right track with with
[00:50:28] uh these kinds of things and this is the
[00:50:31] future. Definitely this is the future of
[00:50:33] content marketing and content creation.
[00:50:35] Thank you Ryan.
[00:50:37] >> Thanks Tim.
