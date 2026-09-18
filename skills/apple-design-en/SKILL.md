---
name: apple-design
description: Locks the model into Apple's design system. Use whenever an interface, screen, flow, component, app or website is being designed, reviewed or built and the result must look and behave like Apple's own work. Loads a distilled base of the Human Interface Guidelines and the WWDC design sessions, with verified visual evidence, and forbids anything outside it. Triggers on "Apple", "HIG", "iOS", "iPadOS", "macOS", "visionOS", "watchOS", "SwiftUI", "Liquid Glass", "design system", "Apple standard", "the Apple way", "review this screen", "how Apple would do it", "interface", "UI", "screen", "app", "dashboard", "landing page".
---

# Apple Design

With this skill active, the only design system allowed is Apple's, exactly as Apple publishes it. Everything you design, review or build comes from three places and nowhere else: the `kb-en/` base of this repository, the files in this folder and Apple's own pages, consulted on the spot. Whatever is not in those three places does not exist for you.

Path to the base (adjust it if you install outside the repository):

```
KB=~/Downloads/apple-design-kb/kb-en
SKILL=~/Downloads/apple-design-kb/skills/apple-design-en
```

## The four laws

1. Only Apple's design system. Components, navigation patterns, typography, color, materials, spacing, motion, writing and accessibility come from the base. No Material Design, Fluent, Bootstrap, default library theme, aesthetic of your own or "personal touch". If the platform is not Apple's, such as a website or a web app, apply the same principles, the same values and the same checklist with the closest equivalent components, and say that it is an adaptation.
2. Inventing is forbidden. No value, component, behavior or "Apple rule" comes from your memory. If the base does not have the answer, research it using the protocol below. If the research finds nothing, say that Apple does not publish a rule about it and propose the most conservative option derived from the principles, marked as your own inference.
3. Never break an Apple rule. Before delivering, run the screen through `checklist.md` and check that no item from `anti-patterns.md` slipped in. If the person asks for something that violates a rule, do not implement it: show the rule, cite the source and offer the alternative Apple uses for the same problem.
4. Every decision has a source. Each choice of component, value or behavior comes with the guidelines page or the session that supports it, in the citation format below.

## How to work

1. Define the platform before you draw anything. Read `platforms.md` and chapter 4 of `$KB/00_APPLE_ESSENCE.md`. Design the interface for the platform it runs on and never port it from another.
2. Structure before styling. Chapter 2 of the essence lays out the process in thirteen steps. Navigation and content come before color and shape.
3. Choose system components. For each element, open the page's card in `$KB/hig/` by running Grep on the slug, for example `(slug: buttons)`, and use what the page governs, the values and the "What the illustrations show" section. Use a custom component only with an explicit, cited reason.
4. Apply the system. `system.md` has the values for typography, color, materials, layout, icons, motion, haptics, writing and accessibility. They are the only numbers you can use without researching.
5. Write as part of the design. Buttons use a specific verb, error messages sit near the problem and assign no blame, and empty states give the next step. It is all in the writing section of `system.md`.
6. Review with the checklist. Answer the 38 questions in `checklist.md`. Any "no" is a blocker, not an observation.
7. Deliver with the compliance table. Every delivery ends with a three-column table: decision, source, status. "Compliant" is the decision that the cited source supports the way it is written. "Adaptation" is the closest equivalent on a platform that is not Apple's. "Inference" is what you derived from the principles without a source saying it, and it includes every deviation from one of Apple's own examples. The cited source has to say what the line claims. If it says something else, or the opposite, the line is an inference and explains the difference.

## Research protocol

When the base has no answer, research before answering. The sources come in this order, and only the first one that answers counts:

1. The Human Interface Guidelines at developer.apple.com/design/human-interface-guidelines.
2. The sessions at developer.apple.com/videos, with the transcript from the page itself.
3. The documentation at developer.apple.com/documentation and the Apple Design Resources.
4. One of Apple's own apps that solves the same problem, described with the source where you saw it.

Use the web search and reading tools that your session offers. Cite the URL. Record what you found in the answer and, if the project maintains the base, add a file to `$KB/supplements/` with the date, the URL and the paraphrase. If those sources turn up nothing, there is no Apple rule, and the answer says so.

## How to cite

- Guidelines page: `hig buttons`, with the URL of the card when the person asks for it.
- Session: `vid wwdc2025_219`, and the frame sheet when the claim comes from the frames: `vid wwdc2025_219 sheet 0007`.
- Illustration: `hig layout img 0686`.
- Research done on the spot: the full URL and the date.
- When a sentence carries two sources, each one has to support the sentence on its own. If only one supports it, cite only that one.

## Files in this folder

| File | What it is |
|---|---|
| `system.md` | The values of the visual system, copied from section 3 of the essence |
| `platforms.md` | What changes between iPhone, iPad, Mac, Apple TV, Vision Pro, Apple Watch, iPhone Duo and CarPlay |
| `anti-patterns.md` | The 37 patterns Apple condemns, with the source of each one |
| `checklist.md` | The 38 review questions, with the source of each one |
| `SYSTEM_PROMPT.md` | The portable version of these rules, for any language model |

## Map of the base

| Where | What it has |
|---|---|
| `$KB/00_APPLE_ESSENCE.md` | Nine chapters: philosophy, process, system, platforms, evolution, anti-patterns, checklist, limits and what only the images show |
| `$KB/hig/00` to `17` | One card per guidelines page, by theme |
| `$KB/videos/00` to `17` | One card per session, by year |
| `$KB/visual_synthesis_hig/<slug>.md` | What the illustrations of a page show |
| `$KB/visual_synthesis_videos/<id>.md` | What the frames of a video show |
| `$KB/VISUAL_VERIFICATION.md` | How the reading of the images was proven and the limits |

## Limits you declare

- The base paraphrases Apple. A direct quote has at most 15 words.
- A number mentioned in a talk is not a guideline. The cards mark the origin, and you repeat the mark.
- A number holds only for the platform and the context in which the card gives it. An iPadOS value does not carry over to the iPhone, nor does a value for one component carry over to another.
- When the base records two values for the same thing, present both with the origin of each one.
- The frames were read by sampling, one at each scene change and at least one every 12 seconds. When the note says something could not be seen, that is what you say.
