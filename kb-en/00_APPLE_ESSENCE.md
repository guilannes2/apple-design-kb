# Apple Essence: how Apple thinks, designs and builds interfaces

Synthesis document of the `apple-design-kb/kb` base. It consolidates the 18 files distilled from the Human Interface Guidelines (folder `kb-en/hig/`) and the 18 files distilled from the transcripts of Apple's design sessions from 2014 to 2026 (folder `kb-en/videos/`). Everything here comes from those 36 files; nothing was added from memory or from an external source. Literal quotes are short and appear in quotation marks; the rest is paraphrase.

Source conventions used throughout the text:
- `hig/NN` indicates the file in the `kb-en/hig/` folder (for example `hig/02` is `02_foundations-part-2.md`), followed by the article slug when useful (for example `hig/02 typography`).
- `vid/NN` indicates the file in the `kb-en/videos/` folder, followed by the session id (for example `vid/04 wwdc2018_803`).
- When a number comes from a talk and not from the guidelines, that is stated.
- In chapter 9 the citation changes form, because the visual layer is indexed by image and by frame sheet: pages appear by the article slug plus the image number, and videos by the session id plus the frame sheet and the frames.
## Contents

1. The philosophy: first-order principles
2. How Apple builds an interface, from the problem to the screen
3. The system: typography, color, materials, layout and spacing, icons and symbols, motion, haptics and sound, writing, accessibility
4. Differences between platforms that change design decisions
5. Evolution of Apple's design thinking by period
6. Anti-patterns Apple explicitly condemns
7. Checklist for reviewing an interface against the Apple standard
8. Limits of this base
9. What only the images show
---

## 1. The philosophy: first-order principles

The principles below appear both in the written guidelines and in the session talks. For each one: what it says, why Apple defends it, and where it is supported.

A formal starting point: the "Design principles" page of the guidelines lists eight principles (Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight) and treats them as tools for arbitrating competing priorities, not as fixed rules (`hig/00 design-principles`). The 2026 session "Principles of great design" lists nine, adding Forgiveness between Agency and Responsibility, and opens with the definition of design as making something with intention, focusing on what matters most to people (`vid/17 wwdc2026_250`). The thirteen principles in this section organize that grammar with what the other 34 sources add.

### 1.1 Purpose before everything: do a few things that matter

What it says: start from the intention, from what is genuinely useful to the person using it; deciding what to build is, in practice, deciding what to leave out.

Why: every feature consumes people's time, attention and trust, resources that cannot be wasted (`vid/17 wwdc2026_250`). Great apps do a few things very well, instead of trying to solve everything on one screen (`vid/11 wwdc2022_10001`). Configuration is a cost too: each extra option is one more decision and interrupts the task (`hig/04 settings`).

Support: `hig/00 design-principles` (Purpose); `vid/17 wwdc2026_250`; `vid/04 wwdc2018_802` (radical simplification, extreme focus, the case of the Rollaboard suitcase designed for 0.1% of 1% of travelers); `vid/02 wwdc2016_805` (crossing features with the customer's goals and the app's goals); `vid/00 meet-with-apple_254` (LTK and "brutal prioritization"); `vid/15 wwdc2025_359` (list everything, then cut, rename and group).

### 1.2 Content comes first; the interface and the brand step back

What it says: the interface exists to serve the content. Controls form a functional layer that appears when needed and recedes when not; brand identity lives in the content layer.

Why: screen space used only to display a brand is space taken from what the person came for (`hig/01 branding`). The interface layer had been taking up more and more space as screens grew, and Liquid Glass aims to reduce that footprint (`vid/00 meet-with-apple_208`). A good reading experience is one you do not notice (`vid/03 wwdc2017_815`).

Support: `hig/01 branding` (the brand always gives way to the content; no repeated logo; the launch screen is not a branding moment); `hig/02 materials` (Liquid Glass as a layer of controls above the content, never in the content layer); `hig/03 launching`; `vid/00 meet-with-apple_208`, `_254`, `_255`, `_256`; `vid/05 wwdc2019_211` ("content first" on tvOS); `vid/03 wwdc2017_816` (lead with content); `vid/05 wwdc2019_809` (on the Mac the interface should be more neutral and not compete with the content); `vid/16 wwdc2025_219`; `vid/17 wwdc2026_251` (UI layer for familiar patterns, content layer for the brand).

### 1.3 Familiarity and consistency: the system component is the default, custom is a justified exception

What it says: build on what people already know, from the real world and from the platform. An established behavior should hold everywhere. Use system components and patterns; customize only where there is an important reason.

Why: consistency of symbols, position and behavior avoids relearning, like a car's controls that work the same way in different cars (`vid/03 wwdc2017_802`). System components bring accessibility, layout adaptation, Dynamic Type, localization and animation for free (`hig/00`, insight 10; `vid/00 meet-with-apple_208`). Recreating system UI without perfection makes the app look broken (`hig/09 windows`). Changing a consolidated mental model is risky and is only worth it with a test that proves a clear win (`vid/03 wwdc2017_802`).

Support: `hig/00 design-principles` (Familiarity); `hig/03` (insight 4: the system video player, file browser, printing and help as the default); `hig/09 windows`; `hig/13 gestures` (do not use a familiar gesture for a unique action, nor a unique gesture for a standard action); `vid/03 wwdc2017_802` (the iOS "sharrow" glyph preferred over a generically good share icon); `vid/03 wwdc2017_809` (start from the SDK's patterns); `vid/05 wwdc2019_808` (do not recreate what UIKit delivers); `vid/00 meet-with-apple_255` (Slack: "don't make me think"); `vid/17 wwdc2026_251` (do not recreate the context menu); `vid/17 wwdc2026_250` (metaphors neither too literal nor too abstract; consistency of behavior and of position).

### 1.4 Clarity and simplicity, which are not minimalism

What it says: include only what is necessary, with a clear hierarchy, recognizable controls and concise language. Simplicity is the absence of friction, not hiding everything in a single place; sometimes simplifying means adding context.

Why: a clear app answers on every screen "where am I", "what can I do" and "where can I go" (`vid/15 wwdc2025_359`), the same signage questions Apple already described in 2017 as wayfinding (`vid/03 wwdc2017_802`). A closed hamburger menu does not communicate what it contains (`vid/09 wwdc2021_10126`; `vid/15 wwdc2025_359`). The 2026 example is the play control that gains the remaining time when resuming a video: more information, simpler to decide (`vid/17 wwdc2026_250`).

Support: `hig/00 design-principles` (Simplicity: "simplicity is not minimalism", focus on what is useful); `hig/02 writing` (fewer words, every word necessary); `hig/08 tab-bars` (tabs always visible); `vid/03 wwdc2017_802` (visibility and wayfinding); `vid/09 wwdc2021_10126`; `vid/15 wwdc2025_359`; `vid/17 wwdc2026_250`; `vid/15 wwdc2025_404` (there is no minimum word quota).

### 1.5 Agency, forgiveness and control in people's hands

What it says: take the person straight to the task, let them explore without locking them into fixed flows, make actions reversible and confirm only what is destructive and irreversible. In intelligent systems, the final decision remains human.

Why: people engage more when they control the experience at their own pace; forgiveness sustains agency because it gives the confidence that it is always possible to go back (`vid/17 wwdc2026_250`). Gestures must be able to be redirected and interrupted at any moment, because thought and gesture happen in parallel (`vid/04 wwdc2018_803`). In generative AI, people must be able to discard, revert and redo, and destructive actions must not be automated (`hig/14 generative-ai`).

Support: `hig/00 design-principles` (Agency); `hig/04 undo-and-redo`; `hig/03 feedback` and `modality`; `hig/14 generative-ai`; `hig/15 machine-learning` (immediate and persistent corrections; never rely on corrections to compensate for low quality); `vid/04 wwdc2018_803`; `vid/06 wwdc2019_803`; `vid/17 wwdc2026_250`; `vid/17 wwdc2026_227` (do not delegate critical thinking to the tools).

### 1.6 Immediate, causal feedback

What it says: every action needs a response, before, during and after the touch. Feedback has to make obvious what caused it and combine visuals, sound and haptics in harmony.

Why: people are very sensitive to latency; delay breaks the sense that the interface is an extension of the body (`vid/04 wwdc2018_803`). A button with no pressed state seems not to respond (`hig/07 buttons`). A stalled progress indicator is read as a freeze (`hig/11 progress-indicators`). For feedback to be useful, what caused it needs to be obvious (`vid/05 wwdc2019_810`).

Support: `hig/03 feedback`, `playing-haptics` (consistent causal relationship); `hig/11 progress-indicators`; `vid/03 wwdc2017_802` (feedback for status, completion, warning and error); `vid/04 wwdc2018_803`, `wwdc2018_804` (perceived affordance, feedforward, feedback); `vid/05 wwdc2019_810` (causality, harmony, usefulness); `vid/10 wwdc2021_10278`.

### 1.7 Responsibility: privacy, minimal data, the right moment and trust

What it says: be transparent about what the app does, ask for permission at the moment the feature needs it, collect only what is necessary, anticipate misuse and protect people.

Why: Apple treats privacy as a fundamental human right; no intelligent system is worth that sacrifice (`vid/07 wwdc2020_10086`). Asking for data without context is the landlord who demands documents before showing the apartment (`vid/03 wwdc2017_816`). Urgency misrepresented in a notification breaks trust (`hig/03 managing-notifications`). On visionOS privacy becomes architecture: the app does not know where the person is looking until they act (`hig/13 eyes`; `vid/13 wwdc2023_10073`; `vid/16 wwdc2025_303`).

Support: `hig/00 design-principles` (Responsibility); `hig/02 privacy`; `hig/03 managing-accounts`, `managing-notifications`; `hig/15 healthkit`, `id-verifier`; `hig/16 sign-in-with-apple`, `wallet` (ask for an age threshold, not a date of birth); `vid/03 wwdc2017_816`; `vid/07 wwdc2020_10162` (location privacy); `vid/08 wwdc2020_10087` (what happens on the device stays on the device); `vid/17 wwdc2026_250` (safeguards for AI, up to removing the feature).

### 1.8 Flexibility and inclusion from the first draft

What it says: design for everyone, treating accessibility and inclusion as a foundation, at the same level as color and typography, and not as a later layer. Disability is a spectrum and is part of the human experience.

Why: solutions designed for a specific need become features for everyone, like the Apple Watch large type watch face (`vid/09 wwdc2021_10308`) or curb ramps (`vid/16 wwdc2025_316`). Inclusion handled at the end is reactive and there is no time left to fix it (`vid/10 wwdc2021_10304`). The inclusion gap is the distance between what a body can do and what the design expects of it (`vid/16 wwdc2025_316`).

Support: `hig/00 design-principles` (Flexibility); `hig/01 accessibility`, `inclusion`; `hig/17` (Foundations puts Accessibility and Inclusion next to Color and Typography); `vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`; `vid/09 wwdc2021_10275`, `wwdc2021_10308`; `vid/10 wwdc2021_10304`; `vid/16 wwdc2025_316`.

### 1.9 The body, the context and the device as the ruler

What it says: each platform is designed from how it is held, seen and used: distance, posture, attention span, input method. You do not port an interface from one platform to another.

Why: each platform's practices derive from observation of real use, not from abstract aesthetics (`hig/00`, insight 1). The Apple Watch "is not a miniature iPhone" (`vid/02 wwdc2015_802`, `wwdc2015_805`). The Mac arrow pointer did not work on the iPad because it would be a high-precision tool for low-precision controls (`vid/07 wwdc2020_10640`). On visionOS, visual and vestibular comfort is a prerequisite (`hig/02 motion`, `spatial-layout`; `vid/13 wwdc2023_10078`).

Support: `hig/00` (Designing for iOS, iPadOS, macOS, tvOS, visionOS, watchOS, games, iPhone Duo); `hig/01 immersive-experiences`; `hig/02 spatial-layout`; `vid/01 tech-talks_801`, `_802`, `_10884` (principles derived from the geometry of the hardware); `vid/07 wwdc2020_10206` (a good iPad app is not a middle ground between iPhone and Mac); `hig/15 mac-catalyst`; `vid/13 wwdc2023_10072`, `_10073`, `_10078`.

### 1.10 Craft: nothing is random

What it says: every decision is deliberate, from an optical alignment to a click sound. Craft includes maintaining and evolving the design after launch.

Why: quality implies that nothing is random (`vid/04 wwdc2018_801`); details are designed even when they seem obvious (`vid/04 wwdc2018_804`). For every feature shipped there are dozens of discarded sketches and prototypes (`vid/00 meet-with-apple_208`). Design is a continuous commitment that does not end at launch (`hig/00 design-principles`).

Support: `hig/00 design-principles` (Craft); `hig/01 icons` (optical alignment, not geometric); `vid/03 wwdc2017_823` (optical weight, line thickness and optical positioning of glyphs); `vid/03 wwdc2017_815`; `vid/04 wwdc2018_801`, `_804`; `vid/06 wwdc2019_239` (craft in the code too); `vid/17 wwdc2026_250`.

### 1.11 Delight is the sum, not decoration

What it says: identify the emotion you want to provoke and let it shape the design. Delight is not confetti added at the end.

Why: delight emerges from the sum of freedom, safety to explore, familiarity and flexibility (`hig/00 design-principles`); it is the sum of the consideration put into the product (`vid/17 wwdc2026_250`). Visual effects need to stay pleasant long after the novelty wears off (`vid/14 wwdc2024_10151`).

Support: `hig/00 design-principles` (Delight); `vid/17 wwdc2026_250`; `vid/14 wwdc2024_10151`; `vid/03 wwdc2017_820`; `vid/09 wwdc2021_113` (the Apple Design Award "Delight and fun" category); `hig/12 widgets` (surprising on special occasions).

### 1.12 Restraint: interruption, color, effect and sound are scarce credits

What it says: alerts, notifications, accent color, animation, haptics, sound and material effects should be used sparingly and always with purpose.

Why: interrupting the person is a credit that gets spent (`hig/03`, insight 1); interrupting is a privilege (`vid/04 wwdc2018_806`). Alerts lose impact if used in excess (`hig/03 feedback`; `hig/09 alerts`). Accent color used widely dilutes the impact (`hig/01 branding`). Often the right decision is to add neither sound nor haptics (`vid/05 wwdc2019_810`; `vid/03 wwdc2017_803`, "Silence is golden"). Liquid Glass should be limited to the most important elements (`vid/15 wwdc2025_284`).

Support: `hig/01 branding`, `color`; `hig/02 motion`, `materials`; `hig/03 feedback`, `playing-haptics`; `hig/09 alerts`, `action-sheets`; `vid/03 wwdc2017_803`, `_813`; `vid/04 wwdc2018_806`; `vid/05 wwdc2019_810`; `vid/14 wwdc2024_10188` (use animations with intention and purpose); `vid/15 wwdc2025_284`; `vid/16 wwdc2025_219`.

### 1.13 Honesty of state and of language

What it says: the interface shows the real, current state, without embellishing or hiding. System components always mean the same thing; a model's limitations and confidence are communicated clearly.

Why: a badge only counts unread notifications, and imitating a badge is deceptive (`hig/12 notifications`). A determinate indicator with an unrealistic pace looks deceptive (`hig/11 progress-indicators`). Controls and complications need to reflect the real state (`hig/12`, insight 1). In ML, factual attribution ("because you downloaded X") builds trust where a raw percentage does not (`vid/06 wwdc2019_803`; `hig/15 machine-learning`).

Support: `hig/11 activity-rings`, `progress-indicators`; `hig/12 controls`, `complications`, `notifications`, `widgets`; `hig/14 generative-ai` (warn that generated content may contain errors); `hig/15 machine-learning`; `vid/06 wwdc2019_802` (Pixelmator Photo makes the model's adjustment visible and editable), `wwdc2019_803`; `vid/11 wwdc2022_110342` (self-sufficient chart description).

---

## 2. How Apple builds an interface, from the problem to the screen

No single session describes the whole process. The steps below consolidate what the sessions and the guidelines describe, in the order in which they appear most often. Several sessions insist that the process is iterative and that steps get walked through again (`vid/02 wwdc2016_805`; `vid/15 wwdc2025_359`: "Design is never really finished").

### Step 1. Ask why the thing should exist

- Before sketching any screen, ask whether what is being built has purpose (`vid/17 wwdc2026_250`).
- Ask why people use the app (`vid/11 wwdc2022_10001`). Everyone on the team should be able to answer what human good the product serves (`vid/10 wwdc2021_10304`, ideation phase).
- Dig past the surface need to the real need: Streaks Workout does not solve "getting healthy", it solves inertia and boredom (`vid/04 wwdc2018_802`).
- In immersive environments, the same question appears as "why are we building this environment, what qualities should it convey and how will it be used" (`vid/17 wwdc2026_234`); in custom environments, the emotional function of the space comes before the geometry (`vid/14 wwdc2024_10087`).

### Step 2. Define for whom, with specificity

- The audience cannot be "everyone"; "you are not the user" (`vid/02 wwdc2016_805`).
- Turn what that person prefers, values and does into customer goals; define app goals (how it should look and feel); leave business goals out of design decisions (`vid/02 wwdc2016_805`).
- Designing for an extreme case can make the design more coherent and reach more people (`vid/04 wwdc2018_802`).
- Think along the axes of diversity and the extremes of use, not the average person (`vid/10 wwdc2021_10304`); involve real people with disabilities ("Nothing about us without us", `vid/16 wwdc2025_316`).
- Observe the platform and the physical context of use: distance, posture, attention span, inputs (`hig/00` designing-for-*).

### Step 3. List everything the app could do, without judging, and then cut

- List every imaginable feature, with no good or bad idea at this stage (`vid/02 wwdc2016_805`; `vid/15 wwdc2025_359`).
- Imagine how and when people would use the app; then clean up: remove what is not essential, rename what is not clear, group what belongs together. Apple calls this information architecture (`vid/15 wwdc2025_359`).
- Rank features by importance from the point of view of the person using them, not the person developing them (`vid/09 wwdc2021_10126`).
- The same filter appears for system surfaces: not every action becomes a shortcut; the criteria are repetition value, viability by voice and usefulness in many contexts (`vid/06 wwdc2019_806`); one or two habitual shortcuts are enough (`vid/13 wwdc2023_10193`); for the Apple Watch, the question is what information to show if there were ten seconds of attention (`vid/13 wwdc2023_10138`).

### Step 4. Structure navigation and content

- Decide what deserves a tab by asking what is truly essential; each extra tab is one more decision for the person (`vid/15 wwdc2025_359`). Tabs reflect the information hierarchy and are for navigation, not for action (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`).
- Use push to go down the hierarchy and modal for a self-contained task (`vid/11 wwdc2022_10001`; `hig/03 modality`).
- Use the toolbar to answer "where am I" (the screen title, not the brand) and "what can I do" (the screen's actions) (`vid/15 wwdc2025_359`).
- Organize content by real behavior and motivation, not by technical taxonomy (`vid/09 wwdc2021_10126`); group by time, seasonality, progress or patterns to reduce choice overload (`vid/15 wwdc2025_359`).
- Apply progressive disclosure: show only what is necessary and reveal more on demand (`hig/01 layout`; `vid/03 wwdc2017_802`, the 80/20 rule and the print dialog).

### Step 5. Start with what is already known

- Start with the screen that will certainly be needed, using an existing app as a reference (layout, color, typography), instead of waiting for the whole app to be mapped out (`vid/02 wwdc2016_805`; `vid/02 wwdc2014_223`).
- Start from the SDK defaults before customizing; write out the use cases and the edge cases and only then ask whether it is worth customizing (`vid/03 wwdc2017_809`).
- In platform redesigns, recompile and see what migrates for free as a baseline (`vid/00 meet-with-apple_256`); adopt first and redesign afterwards (`vid/00 meet-with-apple_257`).

### Step 6. Generate many alternatives and only then critique

- After a first version that is good enough, ask repeatedly "what could we do differently?" varying density, typography, image proportion, containers and navigation. In the 2016 example there were eleven variations before the critique (`vid/02 wwdc2016_805`).
- Start with many hand sketches and choose directions that are really distinct (`vid/02 wwdc2014_223`).
- Never judge during generation; do not settle for the first idea (`vid/02 wwdc2016_805`).
- With coding agents in 2026, the same method: ask for multiple named variations with specific prompts, remix the favorite elements and repeat; vague prompts anchor on a bad starting point (`vid/17 wwdc2026_227`).

### Step 7. Prototype, raising fidelity little by little

- Three questions before prototyping: what needs to be real, what can be fake, where the person will use it (`vid/02 wwdc2014_223`).
- Move from static images to animation and then to real interaction; prototype code is disposable (`vid/02 wwdc2014_223`).
- Any tool that shows images and responds to interaction works, including Keynote (`vid/03 wwdc2017_818`).
- Prototype the interaction together with the visual, never afterwards; an interactive demo is worth more than static designs (`vid/04 wwdc2018_803`).
- Solve the interaction with low-fidelity prototypes, even with text buttons only, before investing in the visual (`vid/06 wwdc2019_802`, Flow by Moleskine).
- Test with real data early, because real data is rarely as clean as imagined data (`vid/11 wwdc2022_110340`); bring real content and edge states into the prototypes (`vid/17 wwdc2026_227`).

### Step 8. Show it to real people, on the device and in context

- Show the prototype to the real audience without defending the result; ask whether the person knows how to do the task, whether it is easy, how to improve it; then discuss what worked, where they got stuck and what ideas came up (`vid/02 wwdc2014_223`).
- Do not argue, defend or dismiss the feedback; test in context, on the real device (`vid/03 wwdc2017_818`).
- Ask someone who has never used the app to narrate out loud what they are thinking while using it (`vid/03 wwdc2017_802`).
- Test in the place where it will be used: the "make toast" button was tested on an iPhone, in the bedroom, in the morning (`vid/04 wwdc2018_804`).
- Iterate labels from the reaction: the heart and the thumb were misread until the text "Suggest toast like this" solved it (`vid/09 wwdc2021_10126`).
- On visionOS and with haptics the device is mandatory: perception is only reliable in the headset (`vid/14 wwdc2024_10096`, `wwdc2024_10152`; `vid/16 wwdc2025_303`); haptics are not reproduced in the simulator (`vid/10 wwdc2021_10278`).

### Step 9. Visual design: hierarchy, type, color and shape working together

- Review how typography, color and imagery work together; the impact comes from the whole, not from isolated pieces (`vid/15 wwdc2025_359`).
- Make the most important element larger or higher in contrast; use the system text styles; choose a palette with simple rules; use semantic colors (`vid/15 wwdc2025_359`).
- Express hierarchy through layout and grouping, not through decoration; align shapes with concentricity (`vid/16 wwdc2025_356`).
- System details are in Section 3.

### Step 10. Writing as part of the design

- Writing is not filler added later. For each screen: Purpose, Anticipation, Context, Empathy (PACE) (`vid/11 wwdc2022_10037`).
- Define the voice first and then vary the tone according to the situation (`hig/02 writing`; `vid/14 wwdc2024_10140`).
- Remove filler words, avoid repetition, lead with the why, keep a word list (`vid/15 wwdc2025_404`).
- Name features by testing belonging, expectation and whether they work in any language, and by saying the name out loud in an everyday sentence (`vid/17 wwdc2026_290`).
- Read the text out loud (`vid/11 wwdc2022_10037`; `vid/15 wwdc2025_404`).

### Step 11. Sound and haptics as design layers

- Think about sound from the start: the app sends frequent notifications, sound can play a brand role, how the app would be understood without a graphical interface (`vid/03 wwdc2017_803`).
- Ask what the object would be in the physical world and how it would sound and feel; apply causality, harmony and utility; build additively, visual, then audio, then haptics (`vid/05 wwdc2019_810`).
- Test candidates side by side and recombine pieces from different assets when no ready-made pair matches (`vid/10 wwdc2021_10278`).

### Step 12. Accessibility and inclusion running through every step

- Plan accessibility and internationalization from the start; test with VoiceOver, the maximum text size and keyboard navigation; handle gaps with a plan and a date (`vid/10 wwdc2021_10304`).
- Support multiple senses, offer customization, adopt the accessibility APIs, track the inclusion debt (`vid/16 wwdc2025_316`).
- Simulate the limitation on your own product: the game Ordia was tested in monochrome and with color blindness filters (`vid/06 wwdc2019_802`).

### Step 13. Communicate the work

- Shared terminology between design and engineering, a single source of truth, show more than tell (`vid/03 wwdc2017_809`).
- Designers and engineers side by side looking at the real build, especially when the material cannot be replicated in the design tools (`vid/00 meet-with-apple_208`).
- When presenting: define each problem in one sentence with explicit agreement, tell it as a story, speak about the experience in the first person, treat all feedback as data (`vid/04 wwdc2018_811`).

### Step 14. Ship, cut with judgment and keep evolving

- Faced with a deadline, cut to do fewer things well for everyone; shipping is not the end point (`vid/10 wwdc2021_10304`).
- Prioritize the rollout by risk and frequency of use (`vid/00 meet-with-apple_255`, Slack).
- Keep the interface up to date with the platform's capabilities; icon changes should be deliberate, because accumulated familiarity is part of the value (`hig/00 design-principles`; `vid/03 wwdc2017_822`, lineage).
- Try to break your own design to find out whether it works (`vid/17 wwdc2026_234`).

---

## 3. The system

Consolidated rules and numbers. When two sources diverge on a number, both appear, with an indication of which is guideline and which is speech.

### 3.1 Typography

Families and general rules
- Two system families: San Francisco (SF Pro, SF Compact, SF Mono, rounded and per-script variants, such as SF Arabic) and New York, a serif; both in variable format with dynamic optical sizes (`hig/02 typography`). In 2022 SF gained the width axis: Condensed, Compressed and Expanded, in addition to Regular; for most cases, two or three styles are enough (`vid/11 wwdc2022_110381`).
- System font by platform: SF Pro on iOS, iPadOS, macOS, tvOS and visionOS; SF Compact on watchOS, with SF Compact Rounded in complications (`hig/02 typography`).
- Prefer the Regular, Medium, Semibold and Bold weights; avoid Ultralight, Thin and Light, especially in small text; thin fonts call for sizes larger than recommended (`hig/02 typography`; `hig/01 accessibility`).
- Minimize the number of typefaces; too many typefaces obscure the hierarchy (`hig/02 typography`). In 2017 the spoken recommendation was to use two to three text styles per screen (`vid/03 wwdc2017_812`).
- Use the system text styles instead of sizes set "by eye": they carry hierarchy and automatic Dynamic Type support (`hig/02 typography`; `vid/15 wwdc2025_359`).
- Do not embed the system fonts in the app; in faithful mockups, adjust the tracking, because at runtime the system adjusts the tracking at each size (`hig/02 typography`).
- Custom font: legible at every size, with Dynamic Type and Bold Text implemented manually; it usually works well for titles with the system font in the body (`hig/01 branding`; `hig/02 typography`). Typography should be functional before it is expressive (`vid/17 wwdc2026_251`). To choose one, start from the intended use and the desired impression, understand structure and contrast, compare candidates at the same point size and do not choose because the name matches the theme (`vid/03 wwdc2017_815`).

Default and minimum sizes (`hig/01 accessibility`; `hig/02 typography`; `hig/00 designing-for-games`)

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

The 2024 games session repeats the same numbers for iPhone, iPad (17 and 11) and Mac (13 and 10) and recommends using scroll views instead of shrinking the type when space runs short (`vid/14 wwdc2024_10085`). Widgets: 11 pt or more (`hig/12 widgets`).

Dynamic Type on iOS and iPadOS, Large size (default), as size and leading, in points (`hig/02 typography`)
- Large Title 34/41; Title 1 28/34; Title 2 22/28; Title 3 20/25; Headline 17/22; Body 17/22; Callout 16/21; Subhead 15/20; Footnote 13/18; Caption 1 12/16; Caption 2 11/13.
- At the largest accessibility size (AX5): Body 53/62, Large Title 60/70.
- macOS (without Dynamic Type): Body 13/16, Headline 13/16 in Bold, Large Title 26/32 (`hig/02 typography`; `vid/08 wwdc2020_10104`, text styles centered on the 13 pt body, with no size slider in the system).
- tvOS: Title 1 76/96, Body 29/36, Caption 2 23/30 (`hig/02 typography`).
- watchOS, Large size (40, 41 and 42 mm): Body 16/18.5, Large Title 36/38.5 (`hig/02 typography`).

Scale and reading rules
- Support text magnification of at least 200%, or 140% on watchOS (`hig/01 accessibility`).
- If the text can grow, it should grow; use the available width; do not truncate; scale glyphs along with the text (`vid/05 wwdc2019_244`). At large sizes, swap side-by-side layouts for stacked ones and reduce columns; keep primary elements at the top (`hig/02 typography`; `vid/08 wwdc2020_10020`).
- Do not enlarge tab titles along with the content when that is not important (`hig/02 typography`).
- Tight leading reduces the line height by 2 pt and loose leading increases it by 2 pt on iOS and macOS; on watchOS the adjustment is 1 pt (spoken example: Body with a 22 pt line goes to 20 or 24) (`vid/07 wwdc2020_10175`). Do not use tight leading with three or more lines (`hig/02 typography`).
- Tracking moves in step with the optical size: in SF Pro it goes from +41 thousandths of an em at 6 pt to 0 from 80 pt on (`hig/02 typography`). The switch between the Text and Display designs happens today between 17 and 28 pt; before, the cut was 20 pt. For truncated strings, prefer the automatic tracking tightening to manual kerning (`vid/07 wwdc2020_10175`).
- Readability margins limit the line length, because lines that run to the default margin get too long for the eye (`vid/03 wwdc2017_812`).
- visionOS: stronger weights (Body in Medium instead of Regular; titles in Bold instead of Semibold) and slightly larger tracking; white text by default; text without a background in bold and without a shadow; 2D text, not 3D; text facing the person (billboarding); Extra Large Title 1 and 2 for editorial layouts (`hig/02 typography`; `vid/13 wwdc2023_10076`, `wwdc2023_10072`).
- Right-to-left languages: the guideline mentions about 2 pt more in the RTL font next to Latin in uppercase (`hig/02 right-to-left`); the session on Arabic mentions 10% more and zero tracking when the font is not optimized, with opacity applied to the whole word (`vid/12 wwdc2022_110441`).
- Mac Catalyst with the iPad idiom: 17 pt text becomes 13 pt (77% scale) (`hig/15 mac-catalyst`; `vid/05 wwdc2019_809`).

### 3.2 Color

- Use color to communicate, not to decorate; do not use the same color for different meanings (`hig/01 color`).
- System colors already come with light, dark and increased contrast variants; a custom color needs all four variants; even single-mode apps need to supply light and dark for the adaptivity of Liquid Glass (`hig/01 color`).
- A semantic color describes the purpose, not the value (`vid/05 wwdc2019_808`; `vid/15 wwdc2025_359`). Do not hard-code system color values in code and do not redefine the semantics, such as using the separator color for text (`hig/01 color`).
- Never use color alone to differentiate, to indicate interactivity or to convey essential information; add shape or text; support Differentiate Without Color (`hig/01 color`, `accessibility`; `vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`).
- Contrast: text up to 17 pt, 4.5:1; text at 18 pt or in bold, 3:1 (the WCAG AA criterion used by the Accessibility Inspector) (`hig/01 accessibility`). Dark Mode: a minimum of 4.5:1 and, for custom colors in small text, aim for 7:1 (`hig/01 dark-mode`). Tint colors: 4.5:1 or more (`vid/05 wwdc2019_808`). The 2021 session calls the 4.5:1 with Increase Contrast a "rough rule", because combinations that pass can still be hard to read (`vid/09 wwdc2021_10275`).
- Accent color with judgment: reserve it for primary actions and status indicators (unread badge, selected tab) (`hig/01 branding`). In Liquid Glass, apply color to the background of the primary action, not to symbols and text, and not to several controls at once (`hig/01 color`). Tint only to convey meaning, such as a call to action, never for visual effect (`vid/15 wwdc2025_323`, `wwdc2025_284`). Tinting every element makes nothing stand out (`vid/16 wwdc2025_219`).
- Over colorful content, prefer monochrome toolbars and tab bars; avoid a label color similar to the content background (`hig/01 color`; `hig/07 buttons`, `toolbars`; `hig/08 tab-bars`).
- To express the brand through color, take the color to the content layer, where it scrolls under the glass controls (`hig/01 branding`; `vid/17 wwdc2026_251`, moving the color from the bars to the content).
- Dark Mode: do not offer an app-specific appearance setting; test Auto, Increase Contrast and Reduce Transparency; iOS uses base backgrounds (which recede) and elevated ones (which come forward) (`hig/01 dark-mode`). Think of dimmed lights, not inverted colors (`vid/05 wwdc2019_808`). In 2026, not supporting Dark Mode is described as a negative experience on such a personal device (`vid/17 wwdc2026_251`). Dark Mode is not supported on visionOS or on watchOS (`hig/01 dark-mode`).
- Fills and most separators are semitransparent; there are six opaque grays for when transparency creates optical illusions (`vid/05 wwdc2019_808`).
- Color has cultural meaning: red is danger in some cultures and positive in others; white is mourning in some places and purity in others; in Stocks with the mainland China region, a gain appears in red (`hig/01 color`, `inclusion`; `vid/09 wwdc2021_10275`).
- Wide color: Display P3 at 16 bits per channel, exported as PNG, with a color profile in every image (`hig/01 color`, `images`). Ask first whether the content calls for P3; convert the profile, never assign it (`vid/03 wwdc2017_821`).
- By platform: on macOS, the accent color the person chooses replaces the app's, and interfaces should be more neutral (`hig/01 color`; `vid/05 wwdc2019_809`); on tvOS, do not indicate focus by color alone (`hig/01 color`); on visionOS, color with restraint over the glass, preferring white text and symbols and color on backgrounds or whole buttons (`hig/01 color`; `vid/13 wwdc2023_10076`); on watchOS, background color with a function, not as adornment (`hig/01 color`; `vid/13 wwdc2023_10026`, `wwdc2023_10138`); on CarPlay, a limited palette, never the same color for interactive and non-interactive, and testing in a real car (`hig/14 carplay`).
- Fixed-color elements do not change: Activity rings (Move 250,17,79; Exercise 166,255,0; Stand 0,255,246), always over black (`hig/11 activity-rings`); page control indicators should not be colored (`hig/09 page-controls`).

### 3.3 Materials

- Liquid Glass forms a functional layer of controls and navigation that floats above the content; it is not used in the content layer (use standard materials there), except in transient controls such as sliders and toggles during interaction (`hig/02 materials`). Applying it to a content table view competes with the rest and confuses the hierarchy (`vid/16 wwdc2025_219`).
- Use it with restraint; it is an interactive layer under the fingertips, so limit it to the most important elements and prefer system controls (`hig/02 materials`; `vid/15 wwdc2025_284`).
- Never glass over glass; elements on top of Liquid Glass use fill, transparency and vibrancy (`vid/16 wwdc2025_219`). Nearby pieces of glass in different containers behave inconsistently; group them in a common container (`vid/15 wwdc2025_323`, `wwdc2025_284`).
- Two variants that never mix. Regular: the versatile, adaptive one, indicated when the background can harm legibility (alerts, sidebars, popovers with text). Clear: only over media-rich content, with a 35% dimming layer over light content (`hig/02 materials`); the 2025 session requires three conditions together: media-rich content, dimming that does not harm the content, and bold, bright content above (`vid/16 wwdc2025_219`).
- The material adapts: small elements switch between light and dark according to what passes behind them; large elements, such as menus and sidebars, do not switch, because it would be distracting; as it grows, the glass simulates greater thickness (`vid/16 wwdc2025_219`). In UIKit, larger glass becomes more opaque (`vid/15 wwdc2025_284`).
- Standard materials on iOS: ultra thin, thin, regular (the default) and thick. Choose by semantic meaning, never by apparent color; thicker gives contrast, thinner preserves context; avoid quaternary over thin and ultra thin (`hig/02 materials`; `vid/05 wwdc2019_808`). Use the system's vibrant colors over materials (`hig/02 materials`).
- The scroll edge effect is not decorative: only behind floating interface, one per view. Soft is the default on iOS and iPadOS; hard is more common on macOS and in dense interfaces, interactive text and pinned headers; the two do not mix (`hig/09 scroll-views`; `vid/16 wwdc2025_356`). Use it in place of a solid background under controls (`hig/01 layout`).
- Remove custom backgrounds and borders from bars; hierarchy comes from layout and grouping (`vid/16 wwdc2025_356`; `vid/15 wwdc2025_284`; `hig/07 toolbars`).
- Accessibility modifies the material automatically: Reduced Transparency makes the glass more frosted, Increased Contrast makes it predominantly black or white with a border, Reduced Motion removes the elasticity (`vid/16 wwdc2025_219`).
- visionOS: windows use glass, which adapts to the ambient light and has no dark mode; avoid opaque windows; a darker material separates sections, a lighter one draws attention to interactive elements; do not stack light materials (`hig/02 materials`; `hig/09 windows`; `vid/13 wwdc2023_10076`).
- macOS: a translucent sidebar, never a solid color, an image or a pattern, because the vibrancy signals which window has focus (`vid/05 wwdc2019_809`).
- watchOS: materials give context in full-screen modals and should not be removed (`hig/02 materials`); there are four background materials, Ultra Thin to Thick (`vid/13 wwdc2023_10138`).

### 3.4 Layout and spacing

Principles
- Order by importance: what matters goes near the top and the leading edge (`hig/01 layout`).
- Alignment communicates relationship; indentation communicates subordination; group with negative space, containers or separators (`hig/01 layout`). Proximity, grouping and mapping follow the 2017 principles (`vid/03 wwdc2017_802`).
- Decide layout by size class, not by device or orientation; keep the same functionality when the size class changes (`hig/01 layout`; `vid/03 wwdc2017_812`).
- Respect safe areas, margins and system guides (`hig/01 layout`; `vid/01 tech-talks_801`).
- Extend background content under sidebars and bars with the background extension effect (`hig/01 layout`; `vid/16 wwdc2025_356`).
- Concentricity: the inner radius plus the padding gives the outer radius (`vid/13 wwdc2023_10076`). Three shapes: fixed (a constant radius), capsule (a radius equal to half the height) and concentric (the parent's radius minus the padding) (`vid/16 wwdc2025_356`).
- Layout changes from resizing should not be destructive: return to the initial state when possible (`vid/15 wwdc2025_208`).
- macOS: nothing critical at the bottom of the window, because people tend to push that edge off the screen (`hig/01 layout`; `hig/08 sidebars`; `hig/09 windows`; `vid/05 wwdc2019_809`).

Hit targets and controls (`hig/01 accessibility`; `hig/00 designing-for-games`; `hig/07 buttons`)

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 44 x 44 pt | 28 x 28 pt |
| macOS | 28 x 28 pt | 20 x 20 pt |
| tvOS | 66 x 66 pt | 56 x 56 pt |
| visionOS | 60 x 60 pt | 28 x 28 pt |
| watchOS | 44 x 44 pt | 28 x 28 pt |

- Padding around controls: about 12 pt with a bezel and about 24 pt without a bezel (`hig/01 accessibility`; `hig/13 pointing-devices`; `vid/07 wwdc2020_10640`).
- The hit area can be larger than the visual area, and should be in small controls (`vid/04 wwdc2018_804`).
- visionOS: centers at least 60 pt apart, with 16 pt or more between elements (`hig/01 layout`; `hig/02 spatial-layout`; `hig/13 eyes`). A 44 pt button needs 8 pt around it; stacks of buttons, 16 pt; list and menu items, 4 pt of padding; ornaments overlap the bottom edge of the window by 20 pt (`vid/13 wwdc2023_10076`). Buttons of 60 pt or more get 4 pt of padding so the hover does not overlap; default sizes Mini 28, Small 32, Regular 44, Large 52, Extra large 64 pt (`hig/07 buttons`). For 3D objects at one meter, 60 pt correspond to about 2.5 degrees, or 4.4 cm (`vid/16 wwdc2025_303`).
- watchOS: at most three buttons with a glyph or two with text side by side (`hig/01 layout`). The 2015 talk gave 80 x 80 px for circular controls on the 42 mm watch and never more than three buttons side by side (`vid/02 wwdc2015_805`).

Structural measurements
- tvOS: a safe area with 60 pt at the top and bottom and 80 pt at the sides (`hig/01 layout`); the 2019 session spoke of 90 pt at the sides and 60 pt at the top and bottom (`vid/05 wwdc2019_211`). Focus grids with 40 pt of horizontal space and a 100 pt vertical minimum, from 860 pt per column in two columns to 160 pt in nine (`hig/01 layout`). A tab bar 68 pt tall, 46 pt from the top (`hig/08 tab-bars`). A split view with one third and two thirds (`hig/06 split-views`).
- macOS: a menu bar of 24 pt; the app name in the About item at 16 characters or fewer (`hig/07 the-menu-bar`); the thin split view divider at 1 pt (`hig/06 split-views`).
- Toolbar: a title of fewer than 15 characters; about three groups at most; leading, center and trailing zones; a single prominent primary action in the trailing zone (`hig/07 toolbars`). Mac tab view: at most six tabs (`hig/06 tab-views`). The iPad's customizable tab bar: a default list of five or fewer (`hig/08 tab-bars`). The visionOS tab bar: up to six items (`vid/13 wwdc2023_10076`).
- Segmented control: up to five to seven segments in wide interfaces, about five on iPhone (`hig/10 segmented-controls`). Radio buttons in groups of two to five (`hig/10 toggles`). Page control: above about ten dots it becomes hard to count (`hig/09 page-controls`).
- Sheets: large and medium detents, the latter at about half the height (`hig/09 sheets`).
- Widgets: a default margin of 16 pt and 11 pt for internal groupings (`hig/12 widgets`; `vid/07 wwdc2020_10103`); in the small widget, at most four pieces of information (`vid/07 wwdc2020_10103`). Live Activities: a margin of 14 pt on the Lock Screen, shared with notifications; a Dynamic Island radius of 44 pt (`hig/12 live-activities`; `vid/13 wwdc2023_10194`).
- Snippets: the guideline gives a maximum height of 400 pt for the custom view (`hig/12 snippets`); the 2025 session recommends not going beyond 340 pt (`vid/16 wwdc2025_281`).
- visionOS: a default window of 1280 x 720 pt, positioned about two meters away, with an apparent width of about three meters (`hig/09 windows`); prolonged reading at least one meter away (`hig/13 eyes`); a limit of about 1.5 m from the head in the progressive and full styles; progressive from 120 to 360 degrees (`hig/01 immersive-experiences`); an alert accessory view up to 154 pt tall with a radius of 16 pt (`hig/09 alerts`).
- iPhone X: 375 x 812 pt, 145 pt taller than the 4.7 inch screen (`vid/01 tech-talks_801`). Apple Watch Series 7: 176 x 215 pt (41 mm) and 198 x 242 pt (45 mm) of active area (`vid/01 tech-talks_10884`).
- Drag: drag image after about 3 pt of movement (`hig/03 drag-and-drop`); a swipe is recognized after a hysteresis of about 10 pt (`vid/04 wwdc2018_803`). The iPadOS pointer (2020): a 19 pt circle; toolbar buttons 37 pt tall (`vid/07 wwdc2020_10640`).

### 3.5 Icons and symbols

App icon
- Sizes: 1024 x 1024 px for iOS, iPadOS and macOS (rounded rectangle) and visionOS (circle); 1088 x 1088 px on watchOS (circle); 800 x 480 px on tvOS, with two to five layers and parallax (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`).
- Layers with no mask applied, content centered; the system applies the mask, specular highlights, shadows and blur; do not include "baked" bevels, shadows or glows (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`). In Icon Composer, up to four groups (`vid/15 wwdc2025_361`).
- Simplicity: one concept with few shapes; text only if essential; prefer illustration to photo; do not replicate the interface or Apple hardware (`hig/01 app-icons`). Metaphor, simplicity, connection and lineage; test on the Home Screen, inside a folder and at small size, squinting your eyes (`vid/03 wwdc2017_822`).
- Consistent appearances across default, dark, light translucent and tinted, without swapping elements between variants (`hig/01 app-icons`); in mono mode, at least one white element (`vid/15 wwdc2025_361`).
- With the new material: avoid realistic 3D objects and complex perspectives, prefer a front view; translucency in moderation ("Less is more"); avoid sharp edges and thin lines; prefer the System Light and System Dark gradients to pure white or black (`vid/16 wwdc2025_220`).

Interface icons and glyphs
- Simplified, with familiar metaphors; consistent in size, detail, weight and perspective; weight matched to the adjacent text; optical alignment with padding when needed; vector format; accessibility label for custom icons (`hig/01 icons`).
- Design glyphs as a set: normalize optical weight and line thickness; position by the optical center, like Play shifted a few pixels to the right; test in context and on the device (`vid/03 wwdc2017_823`).
- Prefer universal concepts and gender-neutral human figures (`hig/01 icons`, `inclusion`; `vid/03 wwdc2017_819`, `wwdc2017_823`).
- Use the same symbol for the same action on all devices; when there is no clear visual shortcut (Select, Edit), use text; for closely related actions, the symbol appears once for the group (`vid/16 wwdc2025_356`). Reserve the ellipsis for overflow (`hig/00 designing-for-iphone-duo`).
- Respect each platform's conventions even with a style of your own, like the share icon (`vid/17 wwdc2026_251`; `vid/03 wwdc2017_802`).

SF Symbols
- Nine weights, from ultralight to black, matched to the SF weights; three scales relative to the cap height (`hig/02 sf-symbols`); small about 20% smaller and large about 30% larger than medium (`vid/07 wwdc2020_10207`).
- Specify in typographic points, like text; do not force width and height; align by the baseline next to text (`vid/05 wwdc2019_206`; `vid/07 wwdc2020_10207`).
- Rendering modes: monochrome, hierarchical, palette and multicolor; choose by intent and confirm in context, even with automatic mode (`hig/02 sf-symbols`; `vid/09 wwdc2021_10349`; `vid/11 wwdc2022_10157`). Variable color represents change over time, not depth (`hig/02 sf-symbols`; `vid/11 wwdc2022_10157`).
- Outline goes with text, toolbars, navigation bars and lists; fill gives emphasis in iOS tab bars, swipe actions and selection; a symbol in a circle helps at small size (`hig/02 sf-symbols`; `vid/09 wwdc2021_10097`). Provide the outline version; the system chooses fill in the tab bar (`vid/14 wwdc2024_10147`; `vid/09 wwdc2021_10349`).
- Using SF Symbols in app icons, logos or brands is forbidden (`hig/02 sf-symbols`).
- Custom symbols start from an existing symbol and from the template, with closed paths, the same number and order of paths across variants; three drawings generate the other variants by interpolation (`hig/02 sf-symbols`; `vid/09 wwdc2021_10250`; `vid/13 wwdc2023_10257`).
- The library was described as having more than 1,000 symbols in 2019, more than 3,000 in 2021, more than 4,000 in 2022, more than 5,000 in 2023, more than 6,000 in 2024 and more than 7,000 in 2026 (`vid/05 wwdc2019_206`; `vid/09 wwdc2021_10097`; `vid/11 wwdc2022_10157`; `vid/13 wwdc2023_10197`; `vid/14 wwdc2024_10188`; `vid/17 wwdc2026_251`).

### 3.6 Motion

- Motion with purpose, never for the animation itself; optional, complemented by haptics and sound; brief, precise feedback; avoid animating frequent interactions, which the system already animates; let the person cancel instead of waiting (`hig/02 motion`).
- Fluidity comes from behavior, not from prescribed animation: instant response; gestures that can be redirected and interrupted; entry and exit along the same path; the interface grows in the direction of the final state; elastic edges, never a dead stop; one-to-one tracking; content moves with the finger in relative position (`vid/04 wwdc2018_803`).
- Springs: two design parameters, damping and response; start with 100% damping; use bounce (the example cites 80%) only when the originating gesture has momentum; project the end point from the velocity (`vid/04 wwdc2018_803`). In 2026 the agents session describes ease and spring with stiffness, damping and mass (`vid/17 wwdc2026_227`).
- Instant touch confirmation; slow animations or animations in fade make the control feel slow (`vid/04 wwdc2018_804`). A double tap delays the single tap by about half a second (`vid/04 wwdc2018_803`).
- Continuity: the zoom transition keeps the same elements visible (`vid/14 wwdc2024_10145`); a button can transform into the menu it opens (`vid/00 meet-with-apple_208`; `vid/15 wwdc2025_284`); glass elements materialize by modulating light instead of a simple fade (`vid/16 wwdc2025_219`); on watchOS, the same object is animated between pages to give permanence (`vid/13 wwdc2023_10026`).
- Duration limits: Live Activities animations and widget update animations up to 2 seconds (`hig/12 live-activities`, `widgets`); interactive overlays on tvOS with a minimum delay of 0.5 s to pause (`hig/03 playing-video`); games between 30 and 60 fps (`hig/02 motion`); AR scene updated 60 times per second (`hig/14 augmented-reality`).
- Reduce Motion: reduce automatic and repetitive animations; tighten the springs; follow the gesture; avoid animating depth on the z axis; swap x, y and z transitions for fades; avoid animating blur (`hig/01 accessibility`); offer cross-fade (`vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`); in custom hover, offer a cross-fade alternative (`vid/14 wwdc2024_10152`).
- visionOS: avoid motion in the periphery; large moving objects become translucent; reposition with a fade; do not rotate the world; offer a stationary frame of reference; avoid sustained oscillation near 0.2 Hz (`hig/02 motion`). Avoid head-locked content, prefer lazy follow; align the horizon; keep the expansion point slow and within the field of view; dark to light transitions slower (`vid/13 wwdc2023_10078`).
- Hover on visionOS: instant effects, with a delay or ramped; a delay avoids flicker; effects that reveal content call for longer delays; keep anchoring elements; start from a visible element; avoid unexpected motion and do not apply it to heavily used views such as toolbar buttons (`vid/14 wwdc2024_10152`; `vid/16 wwdc2025_303`).
- Progress indicators always in motion and with a uniform rhythm; do not alternate between spinner and bar (`hig/11 progress-indicators`).
- Symbol animation with intent: Bounce for confirmation, Scale for persistent focus, Pulse for continuous activity, Replace for state change; in excess, they distract (`hig/02 sf-symbols`; `vid/13 wwdc2023_10197`; `vid/14 wwdc2024_10188`).

### 3.7 Haptics and sound

Haptics
- Use the system patterns for their documented meaning; keep a consistent causal relationship; complement visuals and sound, matching intensity and sharpness to the animation; do not overdo it; prefer short haptics; make them optional; do not interfere with the camera, gyroscope or microphone (`hig/03 playing-haptics`).
- Patterns: on iOS, notification, impact and selection; on the Magic Trackpad, alignment, level change and generic; on watchOS, Notification, Up, Down, Success, Failure, Retry, Start, Stop and Click (`hig/03 playing-haptics`).
- Custom blocks: transient and continuous events, with intensity and sharpness from 0 to 1 (`hig/03 playing-haptics`; `vid/05 wwdc2019_520`, `wwdc2019_810`).
- Causality, harmony and usefulness; often the right decision is not to add (`vid/05 wwdc2019_810`; `vid/10 wwdc2021_10278`, "Don't add feedback just because you can"). The density of the haptics should match the visual density (`vid/10 wwdc2021_10278`).
- Synchrony is perceived: shifting the sound by 10 ms relative to the haptics changes the experience; the same vibration feels more precise with a crisp sound (`vid/03 wwdc2017_803`).
- Without real touch (direct touch in visionOS, virtual game controls), compensate with visual and sound feedback on every contact; touch controls have a pressed state, sound and haptics (`hig/13 game-controls`; `vid/13 wwdc2023_10073`; `vid/14 wwdc2024_10085`, `wwdc2024_10094`).

Sound
- The system volume governs the output; the app only adjusts relative levels; choose the audio category by actual use; do not repurpose audio controls (`hig/03 playing-audio`).
- Never communicate important information by sound alone (`hig/03 playing-audio`; `hig/12 notifications`).
- Notification sound: recognizable as belonging to that app, aligned with its aesthetic, discreet and repeatable (the team lives with the sound for a week), clean. Interface sound: rare, quieter than the notification sound, always possible to turn off. Test on the final device and with headphones (`vid/03 wwdc2017_803`).
- The building blocks of sound: timbre, frequency (a high pitch suggests a small object), duration (repeated sounds, short) and volume (interface sounds, subtle); button clicks sound better in two beats, on press and on release; intermediate states may not need sound (`vid/04 wwdc2018_804`).
- visionOS: prefer having sound, because an app with no sound can seem broken; use spatial audio, fixed or tracked; vary repetitive sounds (`hig/03 playing-audio`); randomize pitch and amplitude; curate the best version of reality, not the most literal one (`vid/13 wwdc2023_10271`).
- Numbers: audio on watchOS at 64 kbps HE-AAC (`hig/03 playing-audio`); tvOS does not play sounds to accompany alerts and notifications (`hig/03 playing-audio`).

### 3.8 Writing

Voice, tone and clarity
- Define the voice by the audience and by familiar vocabulary; adjust the tone to the context, serious in a detected outage and celebratory in an achievement (`hig/02 writing`). Apple's voice is guided by clarity, simplicity, friendliness and helpfulness; qualities go up or down according to the situation, never to zero (`vid/14 wwdc2024_10140`).
- Be clear, use fewer words, read aloud, write for everyone, no jargon; consider the purpose of each screen (`hig/02 writing`; `vid/11 wwdc2022_10037`, PACE).
- Remove filler ("simply", "quickly"), interjections and apologies that add no meaning; avoid repetition; lead with the why ("To get reservation updates, enter your phone number."); keep a word list with the chosen term, the avoided terms and the definition (`vid/15 wwdc2025_404`).
- Refer to the person as "you"; avoid "the user"; reserve "we" for the company or avoid it, especially in errors (`hig/01 inclusion`; `hig/02 writing`).
- Gender-neutral language, no colloquial expressions of excluding origin, humor with caution (`hig/01 inclusion`; `vid/11 wwdc2022_10037`).
- Implementation terms do not leak into the interface: "HealthKit", "NFC", "tag", "scene", "popover" and "panel" are swapped for the language of the people using it (`hig/15 healthkit`, `nfc`; `hig/09 windows`, `popovers`, `panels`).

Label and message patterns
- Action-oriented buttons, almost always with a verb ("Send" works better than "Let's do it!"); avoid "Click here"; use "tap" on touch devices; consistent capitalization by element type; in flows, "Get Started", then "Continue" or "Next" consistently, and "Done" at the end (`hig/02 writing`).
- Errors: near the problem, without blaming, saying how to fix it ("Choose a password with at least 8 characters" instead of "That password is too short"); no "oops" (`hig/02 writing`). Empty states with a next step (`hig/02 writing`).
- Alerts: what happened, why the person is seeing it, how to proceed (`vid/03 wwdc2017_813`). A title that describes the situation, never just "Error", in up to two lines; a complete sentence in sentence case with punctuation, a fragment in title case without a period; buttons of one or two words with a verb; "OK" only in an informational alert; never "Yes" and "No"; always "Cancel" to cancel (`hig/09 alerts`). Name the specific action: "Cancel Subscription" and "Keep Subscription" (`vid/11 wwdc2022_10037`).
- Menus: a verb for actions, title case, no articles, an ellipsis when the action asks for more information; toggling labels such as "Show Map" and "Hide Map" (`hig/07 menus`). Toolbar: a useful title with fewer than 15 characters, never the name of the app (`hig/07 toolbars`).
- Tooltips: 60 to 75 characters, starting with a verb, sentence case, without a final period (`hig/03 offering-help`). Tips: one or two sentences; a title with a direct action phrase; if the feature requires more than three actions, it is too complex for a tip (`hig/03 offering-help`; `vid/13 wwdc2023_10229`).
- Permission purpose strings: a short, complete, specific sentence, in the active voice, in sentence case, ending in a period (`hig/02 privacy`).
- Notifications: a short title in title case without a period; the body in complete sentences; no app name or icon; generic text ("New comment") for when previews are hidden (`hig/12 notifications`).
- Voice and Siri: short dialogue, in spoken language; specific questions ("Which soup?" instead of "Which one?"); no app name, no person's name, no first person; listen to the dialogue several times (`hig/16 siri`; `vid/06 wwdc2019_806`; `vid/07 wwdc2020_10071`). Prompts as a question, not as a label ("When is the deadline?") (`vid/09 wwdc2021_10283`).
- Action button labels of up to three words, verb in the present tense (`hig/13 action-button`); App Clip Card titles up to 30 characters and subtitles up to 56 (`hig/14 app-clips`); Apple Pay errors up to 128 characters (`hig/14 apple-pay`).
- Machine learning: language of consequence ("Suggest less pop music" instead of "dislike"); factual attributions ("Because you've read nonfiction", not "love") (`hig/15 machine-learning`). Generative AI: specific feedback during generation, not a generic "Processing" (`hig/14 generative-ai`).
- Feature names: they belong to the set, they meet the expectation, they work in any language; test by saying the name in an everyday sentence (`vid/17 wwdc2026_290`).
- Localization changes the length, direction and abbreviations of the text; prefer terms that translate in a similar way ("photo" instead of "picture") (`vid/11 wwdc2022_10037`; `vid/03 wwdc2017_819`).

### 3.9 Accessibility

- An accessible interface is intuitive, perceivable and adaptable (`hig/01 accessibility`).
- Vision: Dynamic Type at all sizes, including the accessibility sizes; minimum contrast; increased contrast variants; never color alone; VoiceOver describing interface and content (`hig/01 accessibility`). Descriptive VoiceOver labels ("Account settings, button" instead of the name of the glyph) (`vid/09 wwdc2021_10275`); describe images that carry meaning, exclude decorative ones, group image and caption, announce layout changes, support the rotor (`hig/16 voiceover`). Bold Text also thickens non-textual elements that have a legibility function (`vid/09 wwdc2021_10275`).
- Hearing: captions, subtitles, audio description and transcripts; haptics and visual signals for people who do not perceive the audio (`hig/01 accessibility`).
- Mobility: large, well-spaced controls; simple gestures; an alternative to every gesture, such as a button in addition to the swipe; labels for Voice Control; support for Switch Control, AssistiveTouch and Full Keyboard Access (`hig/01 accessibility`). Error tolerance, no timeouts when Switch Control is active, and private data exposed for the shortest possible time (`vid/07 wwdc2020_10019`).
- Cognition: simple, familiar actions; avoid timed elements that dismiss themselves; in Assistive Access, split flows into single-interaction screens and confirm twice for actions that are hard to reverse (`hig/01 accessibility`).
- Motion and light: Reduce Motion, control over automatic playback, Dim Flashing Lights (`hig/01 accessibility`); Auto-play Video Previews and Prefer Cross-fade Transitions (`vid/05 wwdc2019_244`).
- Respect the person's display preferences even when the affected effect is part of the app's visual identity (`vid/08 wwdc2020_10020`).
- Charts: accessibility labels with context, Audio Graphs, keyboard navigation and Switch Control, never require interaction for critical information (`hig/05 charts`); labels spelled out, the date before the value ("June 1, 36 pancakes") (`vid/11 wwdc2022_110340`).
- Forms: no character limit and no banning of hyphens or accents in names; a single full name field; gender with a broad spectrum and a privacy option (`vid/09 wwdc2021_10275`).
- visionOS: always more than one way to interact; custom gestures do not receive hand input while VoiceOver is active (`hig/13 eyes`; `hig/16 voiceover`); one-handed mode and alternative interaction systems (`vid/14 wwdc2024_10094`, `wwdc2024_10096`).
- Numbers spoken in the sessions, as context and not as a guideline: 285 million people blind or with low vision (`vid/03 wwdc2017_811`); more than 300 million with some form of color blindness (`vid/06 wwdc2019_802`); color blindness in almost 5% of the population (`vid/09 wwdc2021_10275`); a third of people with some degree of motion sensitivity (`vid/05 wwdc2019_244`); people with disabilities are 15% of the world population (`vid/10 wwdc2021_10304`); about one in seven people has some disability (`vid/16 wwdc2025_316`).

---

## 4. Platform differences that change design decisions

The underlying rule is to treat every platform with the same intention and the same care, deriving the decisions from how the device is used (`hig/00 design-principles`, Flexibility; `hig/00`, insight 1). Below, only what actually changes a decision.

### iPhone (iOS)
- Used in the hand, on the move, from minutes to more than an hour; controls are easier to reach in the middle and at the bottom of the screen; limit visible controls; allow swipe to go back and for actions in list rows (`hig/00 designing-for-ios`).
- The tab bar floats over the content at the bottom, in Liquid Glass, and can minimize on scroll; search can be a dedicated tab on the trailing edge or a field in the bottom toolbar, which rises above the keyboard (`hig/08 tab-bars`, `search-fields`; `vid/15 wwdc2025_323`; `vid/17 wwdc2026_292`). Search moved to the bottom for thumb reach (`vid/00 meet-with-apple_208`).
- A modal is dismissed by a button in the top toolbar or a swipe down; sheets with detents and a grabber; in compact, popovers give way to sheets (`hig/03 modality`; `hig/09 sheets`, `popovers`).
- A switch only inside a list row; outside it, a button that behaves as a toggle; do not use a slider for volume (`hig/10 toggles`, `sliders`).
- Offer a context menu or an edit menu for an item, never both (`hig/07 context-menus`).
- A launch screen is required and almost identical to the first screen (`hig/03 launching`).
- In the iPhone X geometry: fill the entire screen, respect safe areas, keep controls centered in landscape, do not decorate the Home indicator (`vid/01 tech-talks_801`).

### iPad (iPadOS)
- A large screen and multiple combined inputs: minimize modals and full-screen transitions, show more content, keep context (renaming inline instead of in a modal) (`hig/00 designing-for-ipados`; `vid/07 wwdc2020_10206`).
- A good iPad app is not a middle ground between iPhone and Mac (`vid/07 wwdc2020_10206`).
- The tab bar at the top, convertible into a sidebar; when in doubt, start with the tab bar; a sidebar when the content is deeply nested (`hig/08 tab-bars`; `vid/14 wwdc2024_10147`; `vid/15 wwdc2025_208`).
- Freely resizable windows; each document in its own window, with a descriptive name; window controls on the leading edge of the toolbar (`hig/09 windows`; `vid/15 wwdc2025_208`).
- The menu bar hidden until it is revealed, centered; never hide menu items, dim them (`hig/07 the-menu-bar`; `vid/15 wwdc2025_208`).
- Pointer: in 2020, adaptive precision, a 19 pt circle and magnetism (`vid/07 wwdc2020_10640`); in iPadOS 26, one-to-one tracking, without magnetism, with a glass highlight (`vid/15 wwdc2025_208`).
- Keyboard shortcuts for all common actions; Full Keyboard Access takes care of control navigation (`vid/07 wwdc2020_10206`; `hig/13 keyboards`, `focus-and-selection`).
- Apple Pencil marks at the instant of the touch, with no mode; hover shows a preview, never triggers an action (`hig/13 apple-pencil-and-scribble`).
- Browser-style navigation only for complex hierarchies; tables go back to being lists in compact (`vid/11 wwdc2022_10009`).

### Mac (macOS)
- Stationary use, several windows and apps, high-precision inputs: more density, fewer nested levels, resizable windows, keyboard shortcuts, customization (`hig/00 designing-for-macos`).
- The menu bar is the complete inventory of commands, in a fixed order (App, File, Edit, Format, View, the app's menus, Window, Help); every toolbar item also exists as a menu command; unavailable items are disabled, not hidden (`hig/07 the-menu-bar`, `toolbars`).
- Controls at the edges bring no ergonomic benefit; flow from top to bottom; nothing critical at the bottom of the window (`vid/05 wwdc2019_809`; `hig/15 mac-catalyst`).
- More neutral color; the accent color the person chose prevails; a translucent sidebar (`hig/01 color`; `vid/05 wwdc2019_809`; `vid/08 wwdc2020_10104`).
- No Dynamic Type; 13 pt body (`hig/02 typography`).
- Mini, Small and Medium controls follow a rounded rectangle for high density; Large and X-Large use a capsule (`vid/16 wwdc2025_356`).
- Users expect a context menu on every object (`hig/15 mac-catalyst`); Main, Key and Inactive window states with distinct appearances (`hig/09 windows`); settings in their own window with Command-comma (`hig/04 settings`).

### Apple TV (tvOS)
- Viewed from eight feet or more, with a remote: the focus system, edge-to-edge art, subtle animations, legible at a distance (`hig/00 designing-for-tvos`).
- Focus is not indicated by color alone; items grow when they gain focus, so the spacing has to account for that; up to five visual states per focusable item; avoid a pointer (`hig/01 color`, `layout`; `hig/06 lockups`; `hig/13 focus-and-selection`).
- Content first: something already playing on open, fewer steps, metadata only when there is interest (`vid/05 wwdc2019_211`).
- Minimize text entry; ask for sign-in and sign-up on another device (`hig/03 managing-accounts`; `hig/10 text-fields`).
- Back opens the parent screen; in an active game, it opens the pause menu; distinguish a press from a tap and ignore accidental taps during live video (`hig/13 remotes`).
- No sounds for alerts and notifications (`hig/03 playing-audio`).

### Apple Vision Pro (visionOS)
- The device brings the content to the person; visual and physical comfort is a priority; choose the minimum level of immersion for each moment and start in the Shared Space (`hig/00 designing-for-visionos`; `hig/01 immersive-experiences`; `vid/13 wwdc2023_10072`).
- Eyes aim, hands select; 60 pt targets; rounded shapes; system hover applied outside the app's process, for privacy (`hig/13 eyes`; `vid/13 wwdc2023_10073`; `vid/16 wwdc2025_303`).
- Content in the field of view, in landscape, anchored in space and not to the head, beyond arm's reach; flat text; subtle depth with a purpose; dynamic scale (`hig/02 spatial-layout`; `vid/13 wwdc2023_10072`, `wwdc2023_10078`).
- There is no dark mode; the glass adapts to the light; heavier typography (`hig/02 materials`; `vid/13 wwdc2023_10076`).
- Vertical tab bar to the left of the window; toolbar at the bottom edge as an ornament; do not create a vertical toolbar; centered sheets; close button in the top left corner (`hig/08 tab-bars`; `hig/07 toolbars`, `ornaments`; `vid/13 wwdc2023_10076`).
- There is no full-screen mode; the expansion comes from the window or from the Digital Crown (`hig/03 going-full-screen`).
- Find the "key moment" that only exists spatially, instead of porting the iOS app into a window (`vid/13 wwdc2023_10072`; `vid/14 wwdc2024_10086`).
- Sound is expected; an app without sound can seem broken (`hig/03 playing-audio`).

### Apple Watch (watchOS)
- Glanceable interactions, of less than a minute (`hig/00 designing-for-watchos`); in 2015 the stated goal was about five seconds (`vid/02 wwdc2015_802`); in 2023, about ten seconds at most with glanceable information (`vid/13 wwdc2023_10309`).
- "Apple Watch is not a miniature iPhone": essential subset, shallow hierarchy (`vid/02 wwdc2015_802`, `wwdc2015_805`); focused and highly specialized apps (`vid/13 wwdc2023_10026`).
- Since watchOS 10, the Digital Crown is the primary navigation, always with a touch equivalent; vertical paging preferred over horizontal; each page the height of one screen; Dial, Infographic and List layouts (`hig/13 digital-crown`; `vid/13 wwdc2023_10026`, `wwdc2023_10138`).
- In watchOS 7, long-press menus were eliminated in favor of visible buttons; the primary action is never in a More menu (`vid/07 wwdc2020_10171`).
- Avoid loading indicators and indeterminate progress indicators; prefer to give notice through a notification when it finishes (`hig/03 feedback`, `loading`).
- Complications, Smart Stack and notifications often matter more than the app; notifications were described as the primary interaction on the watch (`hig/00 designing-for-watchos`; `vid/04 wwdc2018_806`).
- The black bezel works as padding; "bigger is better" (`vid/02 wwdc2015_805`); background color with a function (`vid/13 wwdc2023_10026`).
- Apps do not add options to the system Settings app (`hig/04 settings`); videos of up to 30 seconds (`hig/03 playing-video`).

### iPhone Duo
- Two screens, several poses and a hinge: build to resize with size classes, margins and safe areas, without fixed widths; keep the functionality and the relative position of the controls across poses (`hig/00 designing-for-iphone-duo`).
- Toolbars, tab bars and navigation controls move to the side, on the vertical axis, except on the inner screen in portrait; do not override that placement (`hig/00 designing-for-iphone-duo`).
- Reserved regions (cameras and fold); grids with an even number of columns; avoid extreme layout changes when folding (`hig/00 designing-for-iphone-duo`).
- The four technical sessions about the iPhone Duo have no transcript in this base (Section 8).

### CarPlay
- Made for the person driving: nothing should require the iPhone, which may be in the trunk; errors appear in CarPlay; no automatic playback and no changing the overall volume; important content in the upper half (`hig/14 carplay`).
- The next generation of the CarPlay design system is co-branded with the automaker: it should not look only like Apple nor like a copy of the native system (`vid/14 wwdc2024_10112`).

---

## 5. Evolution of Apple's design thinking by period

The reading by period uses the sessions present in the base. Where a video has no date in the file, the date is not inferred beyond the system version cited in the speech itself.

### 2014 to 2016: method, prototyping and the birth of the watch
- The method appears explicitly: make fake apps, show them to people and learn from the feedback, raising the fidelity from images to animation and interaction (`vid/02 wwdc2014_223`); define the app by its audience and its goals, generate eleven alternatives before criticizing (`vid/02 wwdc2016_805`). Keynote is treated as a real design tool.
- The Apple Watch forces a mindset of its own: personal communication, holistic design with the bezel, light interaction measured in seconds, and the list of ten pitfalls (`vid/02 wwdc2015_802`, `wwdc2015_805`).
- In games, "technology alone is not enough": zero friction on first contact, teach by playing, design for touch instead of porting controls (`vid/02 wwdc2014_602`).

### 2017: the named fundamentals
- "Essential Design Principles" names the conceptual base: "human interface" instead of "user interface", wayfinding, feedback, visibility, consistency, mental models, proximity, grouping, mapping, affordance, progressive disclosure and symmetry, and recalls that the HIG date back to 1978 (`vid/03 wwdc2017_802`).
- A short series covers each craft separately: alerts, glyphs, app icons, fonts, P3 color, sound, a global audience, first launch, rich notifications, prototyping in 60 seconds, communication between design and engineering, size classes (all of `vid/03`).
- The geometry of the iPhone X introduces the Safe Area and the principle of filling the screen without cutting off controls (`vid/01 tech-talks_801`, by the iOS 11 version cited).

### 2018: fluidity, intention and quality
- The interface starts to be described as an extension of the mind and of the body: response, redirection, springs and momentum projection, coming out of the work on the iPhone X gesture (`vid/04 wwdc2018_803`).
- Intention and quality become a theme: radical simplification, extreme focus, personality and direct communication (`vid/04 wwdc2018_802`); quality as time, effort and care (`vid/04 wwdc2018_801`); the entire life of a button (`vid/04 wwdc2018_804`).
- Notifications gain quiet delivery and grouping; interrupting becomes a privilege (`vid/04 wwdc2018_806`). Presenting design work starts to be treated as part of the craft (`vid/04 wwdc2018_811`).

### 2019: system and senses
- iOS 13 redefines the system: Dark Mode with semantic colors, materials, base and elevated backgrounds, card sheets, the context menu in place of Peek and Pop, and the launch of SF Symbols (`vid/05 wwdc2019_808`, `wwdc2019_206`).
- Sound and haptics become design with principles of their own (causality, harmony, utility) and an API of their own (`vid/05 wwdc2019_810`, `wwdc2019_520`).
- Visual accessibility as first class: Dynamic Type, Reduce Motion, Differentiate Without Color (`vid/05 wwdc2019_244`).
- Machine learning gains a design language: multiple options, attribution, translated confidence, limitations, calibration and corrections (`vid/06 wwdc2019_803`). iPad apps arrive on the Mac with the rule of rethinking, not porting (`vid/05 wwdc2019_809`).

### 2020: adaptation, intelligence and precision
- iPadOS gains an identity of its own (sidebar, flattened navigation, pointer with adaptive precision) (`vid/07 wwdc2020_10206`, `wwdc2020_10640`).
- iOS 14 brings the menus closer to touch and to the Mac; widgets and App Clips inaugurate the app as a contextual layer that appears in the right place and at the right time (`vid/07 wwdc2020_10205`, `wwdc2020_10103`, `wwdc2020_10172`).
- Intelligence is declared a design practice, and privacy, a human right (`vid/07 wwdc2020_10086`; `vid/08 wwdc2020_10087`, `wwdc2020_10088`, `wwdc2020_10200`).
- watchOS 7 swaps hidden menus for visible actions (`vid/07 wwdc2020_10171`); macOS Big Sur adopts full-height sidebars and unified toolbars (`vid/08 wwdc2020_10104`); location privacy and interface typography get dedicated sessions (`vid/07 wwdc2020_10162`, `wwdc2020_10175`).

### 2021: inclusion and discoverability
- Inclusion becomes a process with phases, axes of diversity and intersectionality (`vid/10 wwdc2021_10304`) and practice in content, language, color and forms (`vid/09 wwdc2021_10275`); accessibility described as a central mission of the Apple Watch (`vid/09 wwdc2021_10308`).
- Discoverability replaces tutorials: prioritize, give visual cues, suggest gestures with an equivalent button, organize by behavior, give control over personalization (`vid/09 wwdc2021_10126`).
- SF Symbols 3 brings the hierarchical and palette modes; Shortcuts actions should be useful, modular, multimodal, clear and discoverable (`vid/09 wwdc2021_10097`, `wwdc2021_10283`). Spatial interaction between devices appears with the U1 chip (`vid/09 wwdc2021_10245`).

### 2022: clarity of content and language
- Charts get two sessions on when and how to use them (`vid/11 wwdc2022_110342`, `wwdc2022_110340`); writing for interfaces gets the PACE method (`vid/11 wwdc2022_10037`); navigation on iOS is reorganized around tabs that reflect hierarchy (`vid/11 wwdc2022_10001`).
- Structural localization for Arabic (`vid/12 wwdc2022_110441`; `vid/11 wwdc2022_10034`); SF gains widths and SF Symbols 4 gains variable color (`vid/11 wwdc2022_110381`, `wwdc2022_10157`).
- The iPad with resizable windows calls for reorganized toolbars and document menus (`vid/11 wwdc2022_10009`).

### 2023: spatial computing and the redesign of the watch
- visionOS arrives with principles of spatial design, input by eyes and hands, vision and motion science, spatial UI and immersive sound; familiarity with iOS is kept on purpose (`vid/13 wwdc2023_10072`, `_10073`, `_10076`, `_10078`, `_10271`).
- watchOS 10 is described as the biggest change since the launch: Smart Stack, a grid derived from the curvature of the screen, the Digital Crown as navigation (`vid/13 wwdc2023_10026`, `_10138`, `_10309`).
- SF Symbols 5 gives motion to the symbols; Live Activities gain layouts by context; TipKit formalizes education inside the app (`vid/13 wwdc2023_10197`, `_10194`, `_10229`).

### 2024: spatial maturing and unification
- visionOS dominates the year's design sessions: key moment, environments, custom hover, input in games, narrative experiences; testing on the device is repeated as a rule (`vid/14` insights; `vid/14 wwdc2024_10086`, `_10096`, `_10152`).
- Tab bar and sidebar become the same structure in iPadOS 18; SwiftUI animations start to animate UIKit and AppKit (`vid/14 wwdc2024_10147`, `_10145`).
- "Anything your app does should be an app intent" widens the role of the system surfaces (`vid/14 wwdc2024_10176`); personality through voice and tone gains practical exercises (`vid/14 wwdc2024_10140`).

### 2025: Liquid Glass
- A new material unifies the visual language across platforms: functional layer over the content, lensing, continuous adaptation, concentricity, Regular and Clear variants; Apple places it in a lineage that runs through Aqua, the iOS 7 blurs, the iPhone X, the Dynamic Island and visionOS (`vid/16 wwdc2025_219`, `wwdc2025_356`).
- Icons, controls, toolbars, sheets and search are redesigned; the recurring message is to remove old customizations so the material can work (`vid/15 wwdc2025_323`, `_284`, `_361`; `vid/16 wwdc2025_220`).
- The fundamentals come back in the form of process (structure, navigation, content, visual design) and of lean writing (`vid/15 wwdc2025_359`, `_404`); inclusion is redefined by the inclusion gap (`vid/16 wwdc2025_316`).
- In the Meet with Apple series, outside teams report on adoption: brand in the content layer, search at the bottom, prototyping on device, caution with glass performance (all of `vid/00`).

### 2026: consolidation of the principles and of the method
- "Principles of great design" rewrites the principles into nine, adding Forgiveness, and treats AI as a responsibility of whoever designs (`vid/17 wwdc2026_250`).
- Brand gains an explicit two-layer model (UI and content) (`vid/17 wwdc2026_251`); naming features becomes a method (`vid/17 wwdc2026_290`); search goes back to being a decision of position and scope (`vid/17 wwdc2026_292`).
- Code agents enter the exploration process, under human supervision (`vid/17 wwdc2026_227`); immersive environments follow pre-production, production and post-production (`vid/17 wwdc2026_234`).
- The guidelines gain the iPhone Duo page, with a change log of September 9, 2026 (`hig/00 designing-for-iphone-duo`).

Three lines run through all the periods and show continuity, not rupture: prototyping and testing with real people (2014 to 2026), the interface layer that steps back for the content (from "content first" in 2019 to the two-layer model in 2026) and accessibility, which goes from being a session topic to being a condition of every session.

---

## 6. Anti-patterns Apple explicitly condemns

Structure and navigation
1. Hamburger menu to hide the main navigation (`vid/03 wwdc2017_802`; `vid/09 wwdc2021_10126`; `vid/15 wwdc2025_359`).
2. Hiding, disabling or switching tabs automatically; using the tab bar for actions; a generic "Home" tab that duplicates other tabs (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`; `vid/04 wwdc2018_802`).
3. Modal used because the animation is pleasing, modal that becomes an "app inside the app", stacked modals, more than one alert at the same time (`vid/05 wwdc2019_808`; `hig/03 modality`; `hig/09 sheets`, `popovers`; `vid/11 wwdc2022_10001`).
4. Putting all of a view's actions behind a single button or hiding a primary action in a "More" menu (`hig/07 pull-down-buttons`; `vid/07 wwdc2020_10205`, `wwdc2020_10171`).
5. Leaving the only way to do something in a gesture, in a context menu, in a dynamic menu with a modifier key or in a nearby interaction (`hig/07 context-menus`, `the-menu-bar`; `hig/13 gestures`, `nearby-interactions`; `vid/09 wwdc2021_10126`).
6. Hiding unavailable menu items in the menu bar instead of dimming them (`hig/07 the-menu-bar`; `vid/15 wwdc2025_208`).
7. Nesting scroll views in the same orientation (`hig/09 scroll-views`).

Interface and system
8. Recreating system components (windows, context menus, video player, purchase confirmation) without need; the imperfect replica looks broken or dated (`hig/09 windows`; `hig/03 playing-video`; `hig/15 in-app-purchase`; `vid/05 wwdc2019_808`; `vid/17 wwdc2026_251`).
9. Redefining standard gestures and shortcuts for other functions, or inventing a new gesture for a standard action (`hig/13 gestures`, `keyboards`, `pointing-devices`; `hig/04 undo-and-redo`).
10. Liquid Glass in the content layer, glass over glass, mixing Regular and Clear variants, custom backgrounds in bars (`hig/02 materials`; `vid/16 wwdc2025_219`, `wwdc2025_356`; `vid/15 wwdc2025_284`; `vid/00 meet-with-apple_256`, nested glass).
11. Scroll edge effect as decoration or where there is no floating interface (`hig/09 scroll-views`; `vid/16 wwdc2025_356`).
12. Custom button with no pressed state; buttons that do not look like buttons; button shape on content that is not clickable (`hig/07 buttons`; `vid/02 wwdc2015_805`).
13. Primary role on a destructive button; Cancel as the default button in a destructive alert (`hig/07 buttons`; `hig/09 alerts`).
14. Destructive actions in quick menus with no confirmation somewhere else (`vid/07 wwdc2020_10205`).
15. Pointer with magnetism without a custom shape; decorative pointer effects; instructional text next to the pointer (`vid/07 wwdc2020_10640`; `hig/13 pointing-devices`).

Brand and color
16. Launch screen as a brand screen; logo repeated throughout the app; brand competing with the content (`hig/01 branding`; `hig/03 launching`; `vid/17 wwdc2026_251`).
17. Color as the only means of conveying information; color hard-coded; redefining the semantics of system colors; tinting everything (`hig/01 color`, `accessibility`; `vid/16 wwdc2025_219`).
18. The app's own appearance setting in place of the system Dark Mode (`hig/01 dark-mode`).
19. Using Activity rings, the Apple Health icon, AirPlay or the Apple Pay mark as decoration, as a button or as an altered element (`hig/11 activity-rings`; `hig/15 healthkit`; `hig/14 airplay`, `apple-pay`).
20. SF Symbols in app icons or logos; replicas of Apple hardware (`hig/02 sf-symbols`; `hig/01 app-icons`, `icons`).

Icons
21. Text, photos or interface screenshots in the app icon; baked shadows, bevels and highlights; exporting the layer with the mask already applied (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`).
22. Emoji in place of a symbol in quick actions (`hig/07 home-screen-quick-actions`).

Permissions, data and trust
23. Asking for permissions when the app opens without need; pre-alert screens with "Allow" or that nudge people into tracking (`hig/02 privacy`; `vid/03 wwdc2017_816`; `vid/17 wwdc2026_250`).
24. Requiring an account before showing value; asking for a password from people who use Sign in with Apple; burying account deletion (`hig/03 managing-accounts`; `hig/16 sign-in-with-apple`).
25. Notifications for marketing without consent, Time Sensitive for promotion, several notifications for the same subject, a notification only to open the app, a badge for something other than unread messages (`hig/03 managing-notifications`; `hig/12 notifications`; `vid/04 wwdc2018_806`).
26. Making subscription cancellation difficult (`hig/15 in-app-purchase`).
27. AI that makes the person think they are talking to a human, automates destructive actions or presents facts without verified data (`hig/14 generative-ai`); raw confidence percentages and attributions that assume tastes ("love") (`hig/15 machine-learning`; `vid/06 wwdc2019_803`).

Feedback, onboarding and text
28. Long mandatory tutorials, onboarding that teaches the system, a floating arrow or hand pointing out where to tap (`hig/03 onboarding`; `vid/03 wwdc2017_811`; `vid/09 wwdc2021_10126`).
29. An alert when the app starts, an alert that is only informative, an alert for a common action that can be undone, an alert with an error code, an alert as a patch for an avoidable problem (`hig/09 alerts`; `vid/03 wwdc2017_813`).
30. Asking for a rating on the first launch or in the middle of a task (`hig/03 ratings-and-reviews`).
31. A progress indicator that is stopped or moves at an unrealistic pace; vague descriptions such as "loading" (`hig/11 progress-indicators`).
32. "Yes" and "No" on buttons, ambiguous "OK", generic "Confirm", "oops", "Click here", jargon and filler (`hig/09 alerts`; `hig/02 writing`; `vid/11 wwdc2022_10037`, `wwdc2022_10169`; `vid/15 wwdc2025_404`).
33. Choosing a font because the name matches the theme, the "Lack of Typographic Imagination" (`vid/03 wwdc2017_815`).

Platforms and body
34. Porting the interface of one platform to another: Watch as a miniature iPhone, console controls overlaid on touch, an iPad layout scaled on the Mac (`vid/02 wwdc2015_802`, `wwdc2014_602`; `hig/15 mac-catalyst`).
35. On visionOS: content locked to the head, depth in text, oscillation near 0.2 Hz, motion in the periphery, rotating the world, too many windows, requiring physical movement, custom gestures without need (`hig/02 spatial-layout`, `motion`; `vid/13 wwdc2023_10078`; `vid/14 wwdc2024_10094`).
36. On CarPlay, requiring the iPhone or showing errors on it (`hig/14 carplay`).
37. Truncating text when the size increases, ignoring accessibility preferences because the effect is part of the identity (`vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`).

---

## 7. Checklist for reviewing an interface against the Apple standard

Answer yes or no. Each question indicates the source that supports it.

Purpose and structure
1. Does each screen clearly answer "where am I", "what can I do" and "where can I go"? (`vid/15 wwdc2025_359`; `vid/03 wwdc2017_802`)
2. Does every feature present have a clear purpose for the person using it, and has what is not essential been cut or moved to progressive disclosure? (`hig/00 design-principles`; `vid/17 wwdc2026_250`; `hig/01 layout`)
3. Do the tabs represent the real hierarchy, with short, specific labels, with no actions in the tab bar and no generic tab that duplicates others? (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`)
4. Is push used to go down the hierarchy and modal only for a self-contained task, with a title that names the task and an obvious way out? (`vid/11 wwdc2022_10001`; `hig/03 modality`)
5. Is the content ordered by importance, from the top and the leading edge, and grouped by real behavior? (`hig/01 layout`; `vid/09 wwdc2021_10126`)
6. Does every action available in a gesture, a context menu or a hidden menu also exist in a visible place? (`hig/07 context-menus`; `hig/13 gestures`; `vid/09 wwdc2021_10126`)

System and platform
7. Were system components, symbols and behaviors used where they exist, and does each customization have an explicit reason? (`hig/03`, insight 4; `vid/03 wwdc2017_809`; `vid/17 wwdc2026_251`)
8. Does the layout use size classes, safe areas and margins, and keep the same functionality when the size changes, with no destructive changes? (`hig/01 layout`; `vid/15 wwdc2025_208`)
9. Was the interface designed for this platform, and not ported from another? (`vid/07 wwdc2020_10206`; `vid/02 wwdc2015_802`; `hig/15 mac-catalyst`)
10. On the Mac, is every command in the menu bar, with standard shortcuts, and do unavailable items appear dimmed? (`hig/07 the-menu-bar`, `toolbars`)

Content and brand
11. Is the content the dominant element, and does the brand live in the content layer, with no repeated logo and no brand launch screen? (`hig/01 branding`; `hig/03 launching`; `vid/17 wwdc2026_251`)
12. Is Liquid Glass only in the controls and navigation layer, with no glass over glass, no custom backgrounds in the bars and with the right variant? (`hig/02 materials`; `vid/16 wwdc2025_219`, `wwdc2025_356`)

Typography and color
13. Does the text use system text styles or a custom font with Dynamic Type, respecting the platform's default and minimum size? (`hig/02 typography`; `hig/01 accessibility`)
14. Does the interface stay legible, without truncating useful information, at the largest accessibility size? (`hig/02 typography`; `vid/05 wwdc2019_244`)
15. Does the contrast reach 4.5:1 for text up to 17 pt and 3:1 for text of 18 pt or bold, in light, dark and increased contrast modes? (`hig/01 accessibility`, `dark-mode`)
16. Does no information depend on color alone? (`hig/01 color`; `vid/05 wwdc2019_244`)
17. Are the colors semantic, with light, dark and increased contrast variants, and does the accent color appear only in primary actions and states? (`hig/01 color`, `branding`; `vid/15 wwdc2025_323`)

Interaction and feedback
18. Does every interactive target meet the platform minimum (44 x 44 pt on iOS, 60 pt on visionOS, 28 x 28 pt on the Mac) with adequate spacing? (`hig/01 accessibility`; `hig/07 buttons`)
19. Does every custom control have normal, pressed and disabled states, and does it respond immediately? (`hig/07 buttons`; `vid/03 wwdc2017_811`; `vid/04 wwdc2018_804`)
20. Do gestures follow the platform standard, can they be interrupted, and do they have a button alternative? (`hig/13 gestures`; `vid/04 wwdc2018_803`; `hig/01 accessibility`)
21. Do destructive actions use the destructive style, stay out of quick menus, and can they be undone or do they ask for confirmation when the loss is unexpected and irreversible? (`hig/03 feedback`; `hig/04 undo-and-redo`; `vid/07 wwdc2020_10205`)
22. Is progress determinate whenever possible, always moving and with an option to cancel? (`hig/11 progress-indicators`)
23. Does loading show something as soon as possible and never leave an empty screen? (`hig/03 loading`)
24. Do animations have a purpose, are they brief, do they respect Reduce Motion and do they avoid blocking the next action? (`hig/02 motion`; `hig/01 accessibility`)
25. Do haptics and sound follow documented meanings, are they synchronized with the visuals, are they rare and can they be turned off? (`hig/03 playing-haptics`; `vid/05 wwdc2019_810`; `vid/03 wwdc2017_803`)

Writing
26. Do buttons use specific verbs, without "Yes" and "No" and without an ambiguous "OK"? (`hig/02 writing`; `hig/09 alerts`; `vid/11 wwdc2022_10037`)
27. Do error messages stay near the problem, avoid blaming and say how to fix it? (`hig/02 writing`; `vid/03 wwdc2017_813`)
28. Has the text been read aloud and is it free of filler, repetition, jargon or implementation terms? (`vid/15 wwdc2025_404`; `vid/11 wwdc2022_10037`; `hig/15 healthkit`, `nfc`)
29. Are capitalization and terminology consistent, with a word list for the app? (`hig/02 writing`; `vid/15 wwdc2025_404`)
30. Do empty states say the next step, and does an empty search show the term that was searched? (`hig/02 writing`; `vid/17 wwdc2026_292`)

Responsibility
31. Are permissions asked for at the moment the feature needs them, with a specific purpose string, and only for what is necessary? (`hig/02 privacy`; `vid/03 wwdc2017_816`; `vid/07 wwdc2020_10162`)
32. Can the person use the app without an account until the account is essential, and can they delete the account inside the app? (`hig/03 managing-accounts`)
33. Do alerts and notifications have honest urgency, are they rare and actionable, and does the badge count only unread items? (`hig/03 managing-notifications`; `hig/09 alerts`; `hig/12 notifications`)
34. Do AI features indicate where there is AI, allow undo and redo, warn about errors and have safeguards against harm? (`hig/14 generative-ai`; `vid/17 wwdc2026_250`)

Accessibility and inclusion
35. Do all elements have descriptive VoiceOver labels, are decorative images excluded and is the reading order logical? (`hig/16 voiceover`; `vid/09 wwdc2021_10275`)
36. Do language, images, names and gender options include people, without stereotypes? (`hig/01 inclusion`; `vid/09 wwdc2021_10275`)
37. Does the app work with Switch Control, Voice Control, Full Keyboard Access and without depending on a single sense? (`hig/01 accessibility`; `vid/16 wwdc2025_316`)

Process
38. Has the interface been tested on the real device, in the real context and with people from the audience, without defending the design during the test? (`vid/02 wwdc2014_223`; `vid/03 wwdc2017_818`; `vid/16 wwdc2025_303`)

---

## 8. Limits of this base

- The text layer came from text and the visual layer came from images that were actually viewed. The 18 files in `kb-en/hig/` and the 18 in `kb-en/videos/` were distilled from the text of the guidelines and of the transcripts. Chapter 9, the "What the illustrations show" sections in the articles and the "What the images show" sections in the cards came from the frame sheets and the illustration sheets, each one with a checked code.
- The illustrations in the guidelines were viewed: 552 sheets covering 1,342 images and the 61 demonstration videos on the pages themselves. Every article with an illustration carries the "What the illustrations show" section. The alternative text is still cited when the image does not let something be read, and the divergences between image and official description are recorded.
- The video frames were viewed: 3,072 sheets from 175 videos, with one frame at every scene change and at least one every 12 seconds, which gives 26,869 frames from 63.3 hours. Each card in `kb-en/videos/` says how many sheets were viewed. Continuous motion appears as a difference between still frames, and an effect too fast for the interval may not appear.
- The sessions without an official transcript got a local automatic transcript, made with Whisper and marked as unofficial in the card itself: `meet-with-apple_270`, `meet-with-apple_274`, `tech-talks_111461`, `tech-talks_111462`, `tech-talks_111463`, `tech-talks_111466`, `wwdc2020_20022` and `wwdc2026_8012`. Thirteen videos have neither file nor transcript at the source and remain without a card.
- The session `wwdc2023_10115` got a card of its own, written from the entire official transcript and checked sentence by sentence against it.
- Extensive tables were not reproduced in the distilled files: the complete tracking tables by point size, the tables of RGB values of the system colors and parts of the tables of complication and widget dimensions were left summarized (`hig/02 typography`; `hig/01 color`; `hig/12`). The numbers in Section 3 are the ones the files carry.
- Divergences between sources were kept in plain view instead of resolved: eight principles in the guidelines and nine in the 2026 session; tvOS side safe area of 80 pt in the guidelines and 90 pt in the 2019 session; maximum snippet height of 400 pt in the guidelines and 340 pt in the 2025 session; RTL font adjustment of about 2 pt in the guidelines and 10% in the session about Arabic; iPadOS pointer with magnetism in 2020 and without magnetism in 2025. Guidelines and sessions come from different moments; the more recent one was not presumed correct without the source saying so.
- Numbers spoken in the sessions (population statistics, metrics from partner apps, conversion rates) are context of the speech, not guidelines, and were not verified in another source.
- There is content overlap between sessions recorded with different ids (`wwdc2019_223` brings together `wwdc2019_520` and `wwdc2019_810`; `wwdc2022_10034` and `wwdc2022_110441`; ASL versions from 2021 and 2022), and sessions that do not deal with interface design (`wwdc2019_239`, `wwdc2021_10317`, much of `wwdc2025_247`). One card in `vid/14` (`wwdc2024_10086`) contains an observation unrelated to the video, flagged in the file itself, which was ignored.
- The durations recorded in the first collection were associated with the wrong video because of a collection error; they were corrected on 15/09/2026 by measuring the files, which matches Apple's server.
- This synthesis does not claim that the sessions present exhaust Apple's design catalog nor that the guidelines are complete; it covers exactly the 36 files indicated.

---

## What only the images show

This chapter comes from a reading layer that did not exist when the previous sections were written. The 3,072 sheets of frames extracted from the videos and the 552 sheets of illustrations from the guidelines were viewed one by one, distilled into 333 visual syntheses with the code of each sheet checked, and consolidated into the 14 files in `kb-en/visual_essence/`. What follows is a paraphrase of those syntheses. Each item carries in parentheses where it was viewed: the guidelines page by the article slug and the image number, the session by id and the frame sheet. Items supported by a single source are marked as single source. This partly fills the limit declared in section 8, which recorded that the video frames had not yet been viewed and that the images in the guidelines had only come in through the alternative text.

### Grid, measurement and spacing

1. Component measurement is taught as a relationship, not as a number: double arrows dimension width, height and breathing room with no printed value at all. The notation, however, is not rigid. In `hig image-views` (img 0628) and `hig ornaments` (img 0825) the horizontal arrow sits above for the width and the vertical one on the right for the height, but in `hig panels` (img 0835) the horizontal one drops below the component, and in `hig boxes` (img 0183) and `hig collections` (img 0252) the four arrows dimension padding, margin and spacing between cells, not width and height.
2. The number only appears where there is a contract: a file to export, a third-party mark, an area reserved by the system (`hig apple-pay` img 0144 and 0145, minimum height of 30, minimum widths of 100 and 140 and a margin of one tenth of the height; `hig game-center` img 0496, 0497, 0500, 0501, 0505 and 0511, masks and crops dimensioned in pt; `hig icons` img 0623, a margin of 10 per cent as the only numeric measurement on a page of 29 illustration sheets).
3. The tvOS safe area is drawn as a pink band with the values written in red, and the images confirm the divergence between the two sources: 60 at the top and at the bottom with 80 on the sides in the guidelines plate, against 60 and 90 in the slide of the 2019 session, which also dimensions the Carousel at 125, 365 and 90 (`hig layout` img 0686; `vid wwdc2019_211` sheet 0019).
4. The hit target is larger than the painted drawing, and the slack doubles when the button has no frame of its own: 12 on each side for the button with a bezel, 24 for the small symbol and for the text-only button (`hig pointing-devices` img 0861 to 0863; `vid wwdc2020_10640` sheet 0018; `vid wwdc2023_10076` sheet 0009, a 60pt rectangle around the heart with 8pt of inner margin on all four sides).
5. The system floors appear written on the screen, and in several videos the number is not said in the speech: an entire slide carries only "44 x 44" and "Points" (`vid wwdc2017_811` sheet 0005). The table that pairs each value with the component at real size, 17 points of standard body text with 11 as the minimum and 28 points as the standard target on the Mac, has a single source (`vid wwdc2024_10085` sheets 0010 and 0011), and there the relationship inverts: the notes record values said in the speech that the screen never shows.
6. The annotation layer has a color of its own and is never confused with the interface: pink and red mark reserved space and dimensions in the guidelines, yellow plays the same role in the sessions, and aqua green and dotted orange come in when three quantities need to coexist in the same frame (`hig layout` img 0686 and 0687; `hig app-clips` img 0069 and 0070; `vid wwdc2023_10076` sheets 0009 to 0015; `vid wwdc2020_10207` sheet 0016).
7. The corner radius of an element flush against the edge is derived from the screen radius and the offset, not chosen by hand (`vid meet-with-apple_257` sheet 0007, the corners of the inner cards following the curvature of the device itself; `vid wwdc2023_10076` sheet 0011, the label adding inner radius and padding over the same album cell). Only one of the sources isolates the geometry with flat color and no content inside, the green filling the entire screen until it coincides with the outline of the device (`vid tech-talks_111461` sheet 0005).
8. More space becomes more information, never bigger information: what multiplies is the column, the row or the section, and the typographic scale stays where it is (`hig widgets` img 1287 to 1290, the Calendar widget gains columns and an hour ruler until it stretches to four days; `hig designing-for-iphone-duo` img 0437 and 0438, four columns by four rows on the outer screen and six by four on the inner one; `vid tech-talks_111461` sheet 0001).
9. Optical centering is taught as a measured offset, with the glyph rising a few pixels and the padding absorbing the difference, and the guide even going inside the drawing (`hig icons` img 0564 to 0566; `vid wwdc2020_10207` sheets 0010 and 0011; `vid wwdc2019_206` sheet 0019, baseline offsets annotated at minus 3.5 and plus 4.5).

### Hierarchy and typography

10. The typographic scale is delivered as a table with the point size declared, in two forms that do not repeat each other: each row rendered in the very style it names, from the large title at 34 to the captions at 12 and 11 (single source: `vid wwdc2025_359` sheet 0012), and a matrix crossing content size category with text style, with the point value in each cell (single source: `vid tech-talks_802` sheet 0005).
11. The difference in typographic scale between macOS and iOS is resolved by a single factor: the Mac column carries 13, 11 and 9 points, and the iOS one only gets values when the label becomes a 77 percent scale, reaching 26.2 in the large title and 7.7 in the smaller caption (single source: `vid wwdc2019_809` sheet 0012).
12. Text hierarchy is a scale of decreasing contrast, always in the same order and with no new box, border or color. In four levels it appears as label, secondary, tertiary and quaternary (`hig dark-mode` img 0422 to 0424, the same scale repeated over black, over elevated dark gray and over white) and as title, subtitle, placeholder and disabled (`vid wwdc2019_808` sheets 0005 and 0006). The same logic appears reduced to three levels, primary, secondary and tertiary, in pills of decreasing opacity (`vid wwdc2023_10138` sheet 0013).
13. An icon next to text is a typographic problem, not a graphic one: the alignment is proven with the cap height and baseline guides drawn in, and the symbol sits slightly above the baseline (`hig sf-symbols` img 1015 to 1017, the same plus symbol next to the word in small, medium and large; `vid wwdc2020_10207` sheet 0002; `vid wwdc2021_10097` sheet 0003).
14. Matching the numeric point size across different scripts produces imbalance and not consistency: at the same point size only Latin touches both guides, and Arabic and Hebrew come out balanced with a slightly larger size (single source: `hig right-to-left` img 0953 and 0954).
15. The box has to be designed to grow: the same confirmation box is visibly taller in Thai, and the day header spelled out in Arabic takes up much more space than the single letter in English, with the component structure identical (`vid wwdc2022_10037` sheets 0014 and 0015; `vid wwdc2022_110381` sheet 0010, the same screen in Spanish, English and Chinese with only the text changing).
16. Degradation enters as a design subject: the plates show what disappears first when space runs out, and they show the damage when nothing was decided (`hig toolbars` img 1164 and 1165, the overflow menu collapses even the More button itself; `hig typography` img 1199 and 1200, at the largest accessibility size the name breaks into two lines and the footer icons overlap the text; `hig text-fields` img 1140 to 1142, cut off at the edge, break into two lines and truncation with an ellipsis; `vid wwdc2022_10009` sheet 0005, the icons in the central section of the bar disappear before the groups at the ends).
17. Reading starts with the conclusion in plain language and goes down to the evidence: title, short sentence, and only then the chart or the stack of actions (`hig charts` img 0242; `hig column-views` img 0342; `hig action-sheets` img 0025).
18. When there is one value that matters, it takes the screen alone in enormous type with a minimal caption (`vid meet-with-apple_274` sheet 0007; `vid wwdc2017_803` sheet 0012; `vid wwdc2019_803` sheet 0011). The empty frame that precedes the data, part of the same technique, appears in a single source (`vid wwdc2025_247` sheet 0001).
19. A symbol has metrics of its own and is audited in a weight by scale matrix, the same one the tool delivers ready made instead of computing in real time (`hig sf-symbols` img 1014, 27 samples of the same symbol in nine columns from Ultralight to Black by three rows of scale; `vid wwdc2020_10207` sheet 0010, export template of three rows by nine columns; `vid wwdc2019_206` sheets 0008 and 0009).

### Color, material and depth

20. Color is published as a verifiable value, not as an impression: a minimal card with the three RGB values beside it, repeated over a white background and over a black background with the value identical in both (`hig color` img 0270 to 0341; `hig activity-rings` img 0031 to 0033, reddish pink 250, 17, 79, lime green 166, 255, 0 and cyan 0, 255, 246; `hig color-wells` img 0253, the RGB value connected by a line to the center of the button).
21. The iOS gray scale runs from 28, 28, 30 to 242, 242, 247, and the plates show that at the extremes the contrast with the background practically disappears, the lightest over white and the darkest over black (single source: `hig color` img 0318 to 0341).
22. No state lives on hue alone: it is doubled by shape, fill, size or text, and the cost of not doing that is demonstrated with color wheels simulated for three types of color blindness (`hig accessibility` img 0010 and 0011, two circles that differed only in tone get a white check on the green one and an octagon with a white X on the red one; `hig charts` img 0243, systolic in dots and diastolic in diamonds; `vid wwdc2019_244` sheet 0005; `hig widgets` img 1296 to 1298, the semantic green for high disappears when the tinted appearance applies a single purple).
23. Dark mode is a swap of values inside a fixed structure: position, rulers, dimensions and accent color do not move, only background and luminosity change (`hig color-wells` img 0253; `hig app-icons` img 0080 to 0082; `hig icons` img 0561 to 0567, the blue of the selected item is identical in both modes and only the ellipsis switches from black to white; `hig dark-mode` img 0413 and 0414).
24. A complex illustration in dark mode is not solved with a border: the internal values are redone, with clothes, chairs and hair getting lighter, while a single shape icon only needs a thin outline (single source: `hig dark-mode` img 0415 to 0419).
25. Translucent material has no color of its own, it takes the tone of what is behind it, and for that reason it can only be judged over genuinely colored content (`hig materials` img 0771 to 0773, the same circle turns dark gray over a starry sky and whitish over a beach photo; `hig color` img 0263; `vid wwdc2019_808` sheet 0011, four levels of material over an orange gradient; `vid wwdc2026_8012` sheet 0007, the canvas switches from solid gray to a gradient and only then does the refraction appear, going back to gray right after).
26. Translucency is tested against the worst possible background, and not against the background chosen for the mockup (`vid wwdc2023_10076` sheets 0006 and 0007, the panel stays still while the background video switches to sea, elephant, green field and dinosaurs; `vid wwdc2025_361` sheet 0015, the same icon against seven backgrounds in sequence; `vid wwdc2023_10072` sheet 0003, the glass window almost disappears against the light wall).
27. Gamut management is shown as geometry and as a numeric consequence: the sRGB triangle entirely contained inside the Display P3 one, and the color picker dropping from 255, 0, 0 to 236, 0, 0 and then 234, 51, 35 in the conversion (`hig color` img 0268; `vid wwdc2017_821` sheet 0008).
28. Contrast is measured with the number on the screen, and the failing value appears struck through next to the passing one (`vid wwdc2019_808` sheet 0008, the ratio annotated on each panel with a red X and a green check; `vid wwdc2020_10020` sheet 0009, a calculator with samples, RGB values and the result of 4.5 to 1 plus a badge stating which sizes and weights that ratio meets; `vid wwdc2021_10275` sheet 0023, the same game dialog box in two versions with the ratio annotated next to each one).
29. In three dimensional space hierarchy comes from sharpness, transparency and distance, not from scale and shadow, and the panels float in front of the scene without coinciding with the outline of what is behind them (`hig app-icons` video 004; `hig alerts` videos 002 and 003; `hig eyes` video 009; `vid wwdc2023_10075` sheet 0004; `vid wwdc2023_10072` sheet 0012).
30. Glass is reserved for the frame and the chrome, with a single opaque element per composition, and the data stays solid (`vid wwdc2024_10086` sheet 0012; `vid wwdc2024_10116` sheet 0002, a glass playback bar floating below the screen and not attached to it; `vid wwdc2023_10271` sheet 0003).
31. The translucent capsule with fully rounded corners is the default shape of the floating control: the geometry stays constant and the adaptation happens in the tone inherited from the background (`vid wwdc2025_219` sheets 0002, 0004 and 0006, the same three icon capsule changes tone over yellow flowers and over a dune without changing shape; `hig tab-bars` img 1108; `hig typography` img 1194, plant names in a translucent capsule so they stay legible over the scenery).

### States, transition and motion

32. A state change preserves the box: nothing shifts, grows or recomposes around it, and the space for the final state is reserved from the initial one (`hig buttons` img 0191 and 0192, "Checkout" becomes "Checking out" with a spinner at the leading edge with no perceptible change in size; `hig controls` img 0409 and 0410; `hig eyes` video 009 sheet 0002, the hover changes only the background highlight of the row being looked at).
33. The middle frame is shown on purpose, because it is the one that teaches the mechanism, and the written specification usually omits it (`hig drag-and-drop` video 008, the file first lands as a flat labeled card and only then the 3D object is born small and grows, gaining craters; `hig buttons` video 007, the tooltip appears with a delay and smaller before reaching its final size and opacity; `vid wwdc2018_803` sheet 0011, a third square labeled "Hinting" appears between the initial and the final state; `vid wwdc2024_10116` sheet 0002).
34. The animated property is the one that carries meaning, opacity, tone or fill, while position and size stay still (`hig gestures` video 010 sheet 0001, the background of the heart button lightens from translucent gray to solid white with nothing changing place; `vid wwdc2018_804` sheet 0010, the pressed state made only by darkening the same color; `vid wwdc2021_10126` sheet 0010, the shutter goes from translucent to solid as the recognition advances).
35. Sibling elements animate out of phase, because simultaneous animation on everything reads as a rendering failure (single source: `hig sf-symbols` videos 045, 046 and 051, each symbol shrinks and comes back out of phase with the others and only one layer pulses at a time). The offset by layers of different speed is what builds the parallax of the tvOS icon, with card and ring almost still and the face sweeping across the scene (`hig images` video 012).
36. Focus and selection are distinct things and need two visual languages, otherwise the person thinks they have already chosen when they are only navigating (`hig menus` img 0790 with a solid fill for the momentary one against img 0796 with a discreet checkmark in the margin for the persistent one; `hig pickers` img 0845 and 0846 against img 0849; `vid wwdc2020_10205` sheet 0004, a checkmark on the active item and a color highlight on the focused row, two treatments in the same menu).
37. The active state announces itself with a filled area, almost never with an underline or text color alone, because the fill survives a small screen, color blindness and a background with an image (`hig segmented-controls` img 0996 to 0999; `hig tab-bars` img 1108; `hig outline-views` img 0826, the selected row in solid red with white text; `hig page-controls` img 0832 to 0834, the dot of the current page is the only filled one). The outline is not forbidden: in the symbol grid the selected cell is marked by a blue outline (`vid wwdc2022_10158` sheets 0002 and 0003).
38. The unavailable button is the same button faded, not a different gray button: it keeps the hue and changes the saturation so it stays recognizable (`hig researchkit` img 0927 and 0929, the same yellow in a pale version while nothing has been selected; `hig buttons` img 0193 to 0196, the visionOS unavailable button appears dimmed next to the selected one that inverts the contrast).
39. A wait with no estimate gets a shape of its own and a caption, instead of reusing the determinate bar and promising an end the system cannot deliver (`hig progress-indicators` img 0911 and 0912, an indeterminate bar as a wave and a gray spinner always accompanied by status text; `hig tap-to-pay-on-iphone` img 1126, 1127 and 1132; `hig wallet` img 1265 and 1266, the partial green bar becomes a check when it delivers).
40. The empty is never empty: it is the same box with a neutral fill, which keeps rhythm and line height stable across loading, no data and loaded (`hig widgets` img 1312 and 1313, three lighter yellow bars become the three lines of real text; `hig workouts` img 1335, a metric with no data filled with dashes and the label intact; `vid wwdc2015_805` sheet 0005, a reserved rectangle labeled "PHOTO" that becomes a spinner and finally a photo).
41. Animation is documented in static material in three ways, always freezing the extremes and the middle side by side: juxtaposition of poses (`vid wwdc2021_110142` sheet 0007, the same dial with two and then three positions of the foot; `vid wwdc2021_10308` sheet 0007, a row of five thumbnails with the finger in a slightly different position), double exposure (`vid wwdc2022_10131` sheet 0008, the same person in two semitransparent poses overlaid in the same frame) and selective blur (`vid wwdc2021_10308` sheet 0011, the hand blurred while the screen reacts). In a still image, eight capsule strokes at 45 degrees with decreasing opacity are enough to suggest rotation (single source: `hig loading` img 0732).
42. Every ephemeral component is born anchored to its origin, connected by a tip, a line or a continuous shape, and loses the anchor only when it stops being a response to a tap and becomes structure (`hig dock-menus` img 0469; `hig edit-menus` img 0471, a thin line connecting the tip of the bar to the selection handle; `hig color-wells` img 0253, a continuous teardrop shape connecting the closed button and the popover; `vid wwdc2020_10206` sheet 0007, the same list becomes a fixed column and the arrow disappears along with the overlay).
43. On tvOS focus elevates the element, which grows, lightens toward white, gains a shadow and moves up a layer, and the layout has to reserve the clearance of the larger state instead of that of the resting one (`hig lockups` img 0734 to 0738; `hig focus-and-selection` img 0485 and 0486; `hig layout` img 0687, pink bands filling the padding around the focused card; `hig game-center` img 0501, the same asset exported at 659 by 371, 618 by 348 and 548 by 309 pt).

### Comparison of right and wrong

44. The verdict lives in a layer separate from the artifact, in a standardized badge, often in its own isolated image instead of overlaid on the example, so that the example keeps serving as a pixel reference (`hig branding` img 0186 and 0188, badges centered on a white background with no interface element alongside; `hig airplay` img 0044 and 0045, badges in their own cells; `hig toolbars` img 1166 to 1169, badges beside and never on top; `vid wwdc2021_10283` sheet 0004, where the pair of badges is standardized but sits against the top corner of the screen being evaluated).
45. There is a third degree between approved and rejected, the orange or yellow warning, and it means risk and not error (`vid wwdc2023_10078` sheet 0006, looking down and to the sides gets a green check and looking up and diagonally gets an orange warning; `vid wwdc2026_321`, orange for the problematic practice and green for the corrected one across eight sheets between 0005 and 0014; `vid wwdc2021_10250` sheet 0014, trio of badges with the yellow exclamation beside the two green ones).
46. The comparative pair literally reuses the same screen, the same photo and the same fictional text, because two differences at once destroy attribution (`hig apple-pay` img 0135 to 0143, the same two buttons changing one variable at a time: size, order, alignment, corner radius; `hig focus-and-selection` img 0485 to 0489, the same button at the same point of the same beach photo; `vid wwdc2020_10103` sheet 0012, two note cards that differ only in whether or not they carry the word before the time).
47. The wrong one is drawn with the same care as the right one and gets the name of the defect, and in some cases it appears with no correct counterpart beside it (`vid wwdc2018_803` sheet 0015 with the label "Too much visual change" and sheet 0010 with "Not spatially consistent"; `hig camera-control` img 0209 to 0212, the ruler with "1 EV" passes and the same ruler with only "1" is marked as wrong; `vid wwdc2020_10104` sheets 0008 and 0020, red X in the corner with no approved version beside it, including in a code block whose own comment warns of the blurred result).
48. The rule of always exposing the modal's exit is deliberately inverted in the antechamber of a permission request (`hig sheets` img 1032 to 1036, where gathering back, close and confirm at the same time is the pattern to avoid; `hig privacy` img 0898 and 0899, where the pre-permission screen is rejected precisely for gaining an exit). On the same page, and only on it, a financial incentive, a rising benefit chart and a reproduction of the real alert with the desired button circled are also rejected (single source: `hig privacy` img 0900 to 0903).

### Component anatomy

49. The component's zones are named in the art itself, by a thin line that leaves the element and ends in a label outside the drawing, which creates shared vocabulary without cropping the capture (`hig charts` img 0235, callouts for grid line, plot area, mark, axis, tick and axis value label; `hig complications` img 0344, watch face with labels connected to Top Left, Date, Middle, Bottom Left, Bottom Middle and Bottom Right; `hig status-bars` img 1104; `vid wwdc2020_10172` sheet 0011).
50. The opening of a component is a dimensioned technical spec, not an app capture: the piece appears isolated, with width and height measurement arrows, before any discussion of behavior (`hig pop-up-buttons` img 0883; `hig steppers` img 1107; `hig text-views` img 1143; `hig toggles` img 1147; `hig web-views` img 1285).
51. Action hierarchy is fill weight, and the destructive one is marked by the text color and by the position, never by the whole background, which would make it the heaviest element on the screen (`hig buttons` img 0190, primary in solid blue, destructive on a light gray background with red text; `hig action-sheets` img 0027; `hig machine-learning` img 0748, filled, outlined and plain text in the same column; `vid wwdc2018_806` sheet 0013, destructive in red separated into a second confirmation layer inside the same card; `vid wwdc2020_10205` sheets 0008 and 0009, destructive above the neutral one and never beside it).
52. The height ceiling of a snippet's customizable area is dimensioned at 400 pt between the dialog block at the top and the pair of buttons at the base, and it is worth noting that this is the guidelines value, while the 2025 session says 340 pt, a divergence already recorded in section 8 (single source: `hig snippets` img 1091).

### Process and tools

53. Exploration is shown in volume and in reduction, with the stages countable in the image and without the speech giving the counts (`vid meet-with-apple_270` sheet 0002, 14 loose notes in the brainstorm, 8 after simplifying, three clusters and finally five, two and one; `vid wwdc2014_223` sheets 0007 to 0009, a sheet of paper covered with dozens of pen wireframes with blue dots marking four of them and a magnifier enlarging the list one; `vid wwdc2024_10140` sheet 0006, from no notes to about sixteen, then regrouped into columns with two blue header post-its).
54. The real tool enters the frame with the panels open and the values legible, almost always in the same three-zone skeleton, navigation on the left, stage in the center, inspector on the right, and the animation parameters are treated as product controls (`hig app-icons` img 0079, Icon Composer with opacity at 100 percent, blend mode normal, "Liquid Glass Effects" on, image in SVG, x and y position at 0 pt and scale at 100 percent; `vid wwdc2021_10250` sheet 0005; `vid wwdc2026_8012` sheets 0002 to 0007; `vid wwdc2014_223` sheet 0019, duration of 0.60 s and delay of 0.50 s with matching by object, word or character; `vid wwdc2018_803` sheet 0024, stiffness rising from 40 to 100 and damping from 10 to 40 with the ball changing along with it).
55. The placeholder proves that the structure works on its own, but only real content and the worst case reveal truncation, absence and label ambiguity, and the two stages appear as distinct steps of the work (`hig live-activities` img 0701 to 0703, black shapes named by callout lines in place of real content; `vid wwdc2026_227` sheets 0007 to 0009, the solid color cover gives way to real covers and comments with relative time, and the edge cases are named in the preview list itself, among them long content, empty club and crowded club; `vid wwdc2026_290` sheet 0003, the card's value is zeroed out while keeping the label to test the tone in the worst case; `vid wwdc2026_292` sheet 0014, the empty state carries the term in quotation marks with a deliberate typo).

### How Apple presents and demonstrates

56. The progress indicator for an entire session is the topic list itself, resolved only by weight and opacity of the same text in the same position, with no bar, numbering, icon or selection frame, and the notes repeatedly record that the speech never comments on the technique (`vid wwdc2017_802` sheets 0010, 0012 and 0013; `vid wwdc2019_802`, the same row of six words across eleven sheets between 0002 and 0039; `vid tech-talks_111462` sheets 0003, 0008 and 0015; `vid wwdc2022_10139` sheet 0006; `vid wwdc2025_317` sheet 0002; `vid wwdc2026_250` sheets 0004, 0006, 0008, 0010, 0012 and 0014).
57. Nothing shows up already complete: list, table, grid and diagram grow one item per frame, what has already entered does not move, and the next item is usually pre-visible in gray before it lights up (`vid wwdc2017_819` sheet 0002; `vid wwdc2020_10206` sheet 0024; `vid wwdc2022_10131` sheets 0002 to 0005, from one item to four, and sheet 0010, reaching seven; `vid meet-with-apple_255` sheets 0003 and 0004, the row of principles grows from one to five with a new illustration beside each item).
58. Code and result share the frame and the translucent highlight walks from snippet to snippet while the screen stays still, with an honest limit noted in the material itself: in several sequences the rendered result does not change while the code grows, and there the image proves nothing (`vid wwdc2018_803` sheet 0032, the rectangle travels from decelerationRate to the nearest corner line; `vid tech-talks_111462` sheet 0007; `vid wwdc2024_10151` sheets 0002 to 0019, a rigid convention of code on the left and device on the right; `vid wwdc2020_10175`, where the limit is recorded).
59. The color of the diagrams carries a fixed taxonomy that the speech does not declare, and the meaning holds from the beginning to the end of the piece (`vid wwdc2019_223` sheet 0009, light blue for transient events and orange for continuous; `vid tech-talks_111463` sheet 0009, blue for navigation container, red for content and green for layout; `vid wwdc2019_520` sheets 0001 and 0002, green for the subject of the talk, blue for the already existing APIs and red for the hardware; `vid wwdc2025_273`, red for the view's frame, yellow for the composed container's frame and dashed blue for what the layout system sees).
60. The closing is a component, not improvisation: the flat background gives way to a photograph of a physical object, almost always on a wooden table, the recommendations enter one line per frame, and the cross reference lives in a thin footer with the title on the left and the year on the right, entering last (`vid wwdc2024_10145` sheet 0009; `vid wwdc2026_321` sheet 0015; `vid wwdc2025_316` sheet 0017; `vid wwdc2023_10026` sheet 0008; `vid wwdc2025_247` sheets 0020 and 0027; `vid wwdc2023_10258` sheet 0002).
