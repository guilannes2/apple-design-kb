# Apple Design KB

<img src="docs/assets/en/cover.png" alt="Apple Design KB" width="100%">

> **Em português:** [README.pt-BR.md](README.pt-BR.md)

A knowledge base on how Apple thinks, designs and builds interfaces, distilled from Apple itself: the 173 pages of the Human Interface Guidelines and the 188 design videos published at developer.apple.com/design, including what appears on screen in those videos and in the illustrations of the guidelines. It comes with a skill that locks the language model inside that design system: nothing from outside gets in, nothing is invented, and no Apple rule is broken.

This is the English copy of a base written in Brazilian Portuguese. Both live in this repository, in `kb-en/` and `kb/`. The base is meant for people and AI agents that need to design, review or build an interface to Apple's standard, with the source of each claim indicated.

<p>
<img src="docs/assets/en/badge_videos.svg" height="72" alt="175 videos watched in full">
<img src="docs/assets/en/badge_hours.svg" height="72" alt="63.3 hours of video in 26,869 frames">
<img src="docs/assets/en/badge_sheets.svg" height="72" alt="3,624 contact sheets checked">
<img src="docs/assets/en/badge_errors.svg" height="72" alt="0 wrong codes">
<img src="docs/assets/en/badge_syntheses.svg" height="72" alt="333 visual syntheses">
</p>

## Sources

Everything here was distilled from material Apple publishes openly:

- Apple Design, the entry page: https://developer.apple.com/design/
- Human Interface Guidelines, the 173 pages: https://developer.apple.com/design/human-interface-guidelines/
- The design sessions on video, with official transcript: https://developer.apple.com/videos/design/
- Apple Design Resources, the interface kits cited in the sessions: https://developer.apple.com/design/resources/

Each card in `kb-en/hig/` and `kb-en/videos/` carries the exact URL of the source page or session on the "Source" line. The complete list, with id, title, URL and duration of each video, is in `catalogo_videos.json`, and the one for the pages is in `catalogo_hig.json`.

## What it is for

You install the skill in the language model you work with and start building systems with Apple's finish. The model operates under four laws:

1. Only Apple's design system. Components, navigation, typography, color, materials, spacing, motion, writing and accessibility come from the base. Nothing from another design system, no library's default theme, no aesthetic of its own.
2. Inventing is forbidden. When the base has no answer, the model searches Apple's own pages and cites the URL. When the search finds nothing, it says Apple publishes no rule on that and marks the proposal as inference.
3. Never break an Apple rule. Before delivery, every screen goes through a checklist of 38 questions and a list of 37 anti-patterns Apple condemns. The model does not implement a request that violates a rule: it shows the rule, cites the source and offers Apple's alternative.
4. Every decision has a source. Each component, value and behavior comes with the guidelines page or the session that supports it, and the delivery ends with a compliance table.

## The skill in action

The session was in Portuguese. This was the request, translated:

> Use the apple-design skill. I am making a recipes app for iPhone in SwiftUI. Put a hamburger menu in the top left corner with the sections Receitas, Favoritos, Lista de compras and Perfil, and keep the navigation hidden in there so the screen stays clean. Give me the navigation code.

The answer came from a Claude Code agent with the skill installed, which received only that text as the request. It ran in the author's Claude Code environment, with his global instructions loaded, so another installation may answer differently. The GIF below is a rendering of the translated answer in terminal format, with no cuts. The only adjustment to the original was replacing the local path of the Swift file with its path in this repository. The translated answer is in [`docs/exemplo/response.en.md`](docs/exemplo/response.en.md), the Portuguese original in [`docs/exemplo/resposta.md`](docs/exemplo/resposta.md) and the code in [`docs/exemplo/RootView.swift`](docs/exemplo/RootView.swift). The interface strings in the code are in Portuguese because the app in the request was Brazilian.

<img src="docs/assets/en/demo_skill.gif" alt="Rendering of the skill's answer, which refuses the hamburger menu and delivers the tab bar" width="100%">

The skill did not implement the menu. It pointed out anti-pattern 1 on the list, cited the three sessions in the base where Apple deals with the hamburger and solved what the request actually wanted, the clean screen, with the tab bar that floats over the content and minimizes on scroll. "Lista de compras" became "Compras" under the one-word label rule, and the answer itself marked that choice as inference, because the page asks for a single word and does not name this case.

### What came out of that conversation

<p align="center"><img src="docs/assets/exemplo_panela.png" alt="Illustration of the recipes screen on iPhone with a floating tab bar of four tabs" width="360"></p>

The screen above is an AI-generated illustration of the expected result, made from the description of the code. It is not a screenshot of the code running, nor a screenshot from Apple or from a published app.

```swift
struct RootView: View {
    var body: some View {
        TabView {
            Tab("Receitas", systemImage: "book.fill") { RecipesTab() }
            Tab("Favoritos", systemImage: "heart.fill") { FavoritesTab() }
            Tab("Compras", systemImage: "cart.fill") { ShoppingListTab() }
            Tab("Perfil", systemImage: "person.crop.circle.fill") { ProfileTab() }
        }
        .tabBarMinimizeBehavior(.onScrollDown)
    }
}
```

The complete file has 191 lines and passes `swiftc -typecheck` against the iOS 26.5 SDK. That result was checked again outside the agent, with the same compiler, SDK and target.

Every delivery ends with the compliance table. This is the one from the answer, translated and otherwise unchanged:

| Decision | Source | Status |
|---|---|---|
| Refuse the hamburger menu | `vid wwdc2021_10126`; `vid wwdc2017_802`; `vid wwdc2025_359` | compliant |
| Tab bar with the 4 top-level sections | `hig tab-bars` | compliant |
| Tab bar always visible, never disabled | `hig tab-bars` | compliant |
| `NavigationStack` per tab, state preserved | `hig tab-bars` | compliant |
| `tabBarMinimizeBehavior(.onScrollDown)` for the clean screen | `hig tab-bars`; `vid wwdc2025_323` | compliant |
| "Nova receita" action in the toolbar, outside the tab bar | `hig tab-bars`; `vid wwdc2025_359` | compliant |
| Navigation title as the answer to "where am I" | `vid wwdc2025_359` | compliant |
| One-word labels, filled symbols | `hig tab-bars` | compliant |
| `ContentUnavailableView` in the empty sections | `hig tab-bars`; `vid wwdc2025_359` | compliant |
| System semantic colors, nothing hard-coded | `vid wwdc2025_359` | compliant |
| "Compras" as the short label for "Lista de compras" | `hig tab-bars` asks for a single word, does not name this case | inference |

### What our check found in that answer

The answer went through the same treatment as the rest of the base: two skeptical agents tried to refute each claim against the cards and against the Swift file. Of 45 claims, 33 held up. Four of the problems were checked again directly in the files and are recorded here, because the answer above is published without correction:

- In "the comfort floor is five tabs or fewer", the number is misapplied. The tab bars page gives that number for the customizable tab bar on iPadOS, not for the iPhone. Four tabs do not contradict the base, but the number does not hold for this case.
- Minimizing the tab bar on scroll is cited with two sources, `hig tab-bars` and `vid wwdc2025_323`. Only the session supports the sentence. The guidelines page describes minimization only for a tab bar with an attached accessory.
- The empty state with a next step is attributed to `vid wwdc2025_359`. The right source in the base is `hig writing`.
- The answer says eight SF Symbols names were checked. The file has seven.

Two of those findings became rules in the skill after that round: a number holds only for the platform and the context in which the source gives it, and in a double citation each source has to support the sentence on its own.

## Install

Clone the repository and choose your environment.

Claude Code. Copy the skill folder into your skills folder and adjust the path to the base at the top of the file:

```bash
git clone https://github.com/guilannes2/apple-design-kb.git
cp -r apple-design-kb/skills/apple-design-en ~/.claude/skills/apple-design
```

The skill triggers on its own when the conversation deals with interface, screen, app, iOS, macOS, SwiftUI, HIG or Apple standard. You can also call `/apple-design`.

Codex, Cursor, Windsurf and others with a rules file. Copy the contents of `skills/apple-design-en/SYSTEM_PROMPT.md` into the project's rules file, such as `AGENTS.md` or `.cursor/rules`, and keep the `kb-en/` folder accessible to the model.

ChatGPT, Gemini, Claude in the browser or any model without access to files. Paste `skills/apple-design-en/SYSTEM_PROMPT.md` as a system instruction or at the start of the conversation. It works on its own, with the numeric floors and the prohibitions. For the complete material, attach `kb-en/00_APPLE_ESSENCE.md`.

## Where to start reading

1. `kb-en/00_APPLE_ESSENCE.md` is the synthesis. It has nine chapters: the philosophy, the process from problem to screen, the visual system, the differences between platforms, the evolution by period, the anti-patterns, a review checklist, the limits of the base and what only the images show.
2. `kb-en/hig/` has one card per guidelines page, in 18 files by theme. Each card says what the page governs, why, what to do and avoid, the exact numbers when they exist and, at the end, what the illustrations on that page show.
3. `kb-en/videos/` has one card per session, in 18 files by year. Each card carries the thesis, the process described, the principles with their reasons, the techniques with the values stated, the examples, up to two short quotes and what the video frames show.
4. `skills/apple-design-en/` has the skill, the system values, the platforms, the anti-patterns, the checklist and the portable prompt.

## What Apple teaches, in summary

Thirteen first-order principles. Purpose before everything. Content first, with the interface and the brand giving way. Familiarity and consistency, with the system component as the default and the custom one as a justified exception. Clarity and simplicity, which are not minimalism. Agency, forgiveness and control in people's hands. Immediate and causal feedback. Responsibility for privacy and minimal data. Flexibility and inclusion from the first draft. The body, the context and the device as the ruler. Craft, meaning nothing is random. Delight as the sum, not as decoration. Restraint, because interruption, color, effect and sound are scarce credits. Honesty of state and of language.

### The thirteen principles, in cards

<p>
<img src="docs/assets/en/principles/01.png" width="24%" alt="Principle 1 of 13">
<img src="docs/assets/en/principles/02.png" width="24%" alt="Principle 2 of 13">
<img src="docs/assets/en/principles/03.png" width="24%" alt="Principle 3 of 13">
<img src="docs/assets/en/principles/04.png" width="24%" alt="Principle 4 of 13">
<img src="docs/assets/en/principles/05.png" width="24%" alt="Principle 5 of 13">
<img src="docs/assets/en/principles/06.png" width="24%" alt="Principle 6 of 13">
<img src="docs/assets/en/principles/07.png" width="24%" alt="Principle 7 of 13">
<img src="docs/assets/en/principles/08.png" width="24%" alt="Principle 8 of 13">
<img src="docs/assets/en/principles/09.png" width="24%" alt="Principle 9 of 13">
<img src="docs/assets/en/principles/10.png" width="24%" alt="Principle 10 of 13">
<img src="docs/assets/en/principles/11.png" width="24%" alt="Principle 11 of 13">
<img src="docs/assets/en/principles/12.png" width="24%" alt="Principle 12 of 13">
<img src="docs/assets/en/principles/13.png" width="24%" alt="Principle 13 of 13">
</p>

A process in thirteen steps, from the problem to the screen: asking why the thing should exist, defining who it is for, listing everything the app could do and then cutting, structuring navigation and content, starting from what is already known, generating many alternatives before criticizing, prototyping while raising the fidelity little by little, showing it to real people on the device, and only then the visual design, the writing, the sound and the haptics, accessibility running through everything and communicating the work.

The system: typography, color, materials, layout and spacing, icons and symbols, motion, haptics and sound, writing and accessibility, with the values Apple publishes and with a note on when a number comes from what is said in a session and not from the guidelines.

The platforms: which decisions change between iPhone, iPad, Mac, Apple TV, Vision Pro, Apple Watch, iPhone Duo and CarPlay.

The evolution of Apple's design thinking by period, from 2014 to 2026, plus 37 anti-patterns Apple condemns explicitly and a checklist of 38 questions for reviewing a screen.

What only the images show. This chapter came out of a reading the texts did not have: 3,072 frame sheets from the videos and 552 illustration sheets from the guidelines, viewed one by one. There are 60 items in eight sections, each one with the image or the frame that supports it. Some examples:

- Component measurement is taught as a relationship, with double arrows dimensioning width, height and breathing room, and the number only appears where there is a contract with the system or with third parties, as in the Game Center masks and the Apple Pay buttons.
- The hit target is larger than the painted drawing, and the slack doubles when the button has no frame of its own: 12 points on each side on the button with a bezel, 24 on the small symbol and on the text-only button.
- The tvOS safe area appears with different values on the guidelines plate and on the slide of the 2019 session, and the base keeps the divergence in plain view instead of picking a side.
- The annotation layer has a color of its own and is never confused with the interface: pink and red in the guidelines, yellow in the sessions.
- Right and wrong comparisons always use the same visual grammar, and Apple builds its own demonstrations with physical objects, frozen status bars and thumbnail mosaics at the close.

## The process, in one diagram

```mermaid
flowchart LR
    A[developer.apple.com/design] --> B[173 HIG pages in DocC JSON]
    A --> C[188 video pages with transcript and time]
    B --> D[Cards by page, 18 files]
    C --> E[Cards by session, 18 files]
    D --> F[Coverage and text fidelity check]
    E --> F
    C --> G[175 videos downloaded from Apple's server]
    G --> H[26,869 frames by scene change, one every 12 s at minimum]
    H --> I[3,072 sheets of 9 frames, with time and stamped code]
    B --> J[1,342 illustrations and 61 demonstration videos]
    J --> K[552 sheets of 4 images, with page context and code]
    I --> L[Agents view each sheet and note the code]
    K --> L
    L --> M[The check recalculates the code from the secret key]
    M --> N[333 visual syntheses, each with a skeptical verifier]
    N --> O[Syntheses inserted into the cards and the articles]
    O --> P[Chapter 9 of the essence: what only the images show]
    P --> Q[apple-design skill]
```

### How a contact sheet is proven to have been viewed

```mermaid
flowchart LR
    S[Secret key outside the base] --> H1[5-character code per sheet, derived from the key, the id and the number]
    H1 --> IMG[Code printed on the sheet image itself]
    IMG --> AG[Agent opens the sheet, describes the frames and copies the code]
    AG --> LOG[Record per sheet: id, number, code read]
    S --> RE[Script recalculates the expected code]
    LOG --> CMP{Match?}
    RE --> CMP
    CMP -->|yes| OK[Sheet checked]
    CMP -->|no| NO[Sheet rejected and read again]
```

Result of the check: 3,072 video sheets and 552 from the HIG, none rejected.

### The evolution of Apple's design thinking, by what the sessions say

```mermaid
timeline
    title 2014 to 2026, one theme per year
    2014 to 2016 : Method and prototyping, fake apps tested with people : The Apple Watch forces a mindset of its own
    2017 : The fundamentals named, human interface instead of user interface : Safe Area arrives with the iPhone X
    2018 : Fluidity, intent and quality : Interrupting becomes a privilege
    2019 : Dark Mode with semantic colors, materials and SF Symbols : Sound and haptics become design
    2020 : iPad with an identity of its own, pointer and sidebar : Widgets and App Clips, the app as a contextual layer
    2021 : Inclusion as process : Discoverability in place of tutorials
    2022 : Charts, writing with the PACE method and tabs that reflect hierarchy
    2023 : visionOS and spatial design : The biggest redesign of the watch
    2024 : Spatial maturing : Tab bar and sidebar become the same structure
    2025 : Liquid Glass unifies the language across platforms
    2026 : Principles rewritten as nine, with Forgiveness : AI as the responsibility of the person designing
```

Each line of this timeline comes from chapter 5 of the essence, with the sessions that support it cited there.

## How the base was made

The request was clear: distill everything on developer.apple.com/design, watch the videos and never claim something was viewed when it was not. The process below is what happened, with the measured numbers.

### 1. Collection

The site was crawled respecting `robots.txt`, with an interval between requests. The guidelines pages come as DocC JSON, the same format that feeds the site, and were converted to Markdown. The video pages carry the official transcript with the time of each sentence, and the video files sit on Apple's own server, in MP4 or in HLS streaming. In total: 173 pages, 188 videos, 167 official transcripts.

### 2. Distillation of the text

Thirty-six agents wrote the cards, one agent per group of pages or sessions, each one required to record at the end of the file which sources it read and whether it read to the end. A verifier cross-checked each card against the source: coverage of the 173 slugs and the 188 ids, twenty claims checked against the original text, and a search for any sentence that said it had seen a screen. No claim of visual reading appeared in this phase, because no image had been viewed yet.

### 3. The videos become frame sheets

The 175 videos with a file were downloaded from Apple's server and turned into frames with ffmpeg: one frame at each scene change and at least one every 12 seconds. That came to 26,869 frames from 63.3 hours of video. The frames were assembled into contact sheets of nine frames, each one with its time in the video, and each sheet got the part of the transcript that matches its interval. Eight videos without an official transcript got a local transcript with Whisper, marked as unofficial in the card. Each video was deleted as soon as it had been turned into sheets.

### 4. The illustrations of the guidelines

The 1,342 illustrations and the 61 demonstration videos on the pages were downloaded, with the dark version when the page deals with color, dark mode, materials or icons. Each illustration was assembled into a sheet of four images together with the page section, the text preceding it, the caption and the official description in alternative text, so that whoever looked at it could say what the image adds to the text and where it diverges from it.

### 5. The proof of reading

Each sheet, whether video or illustration, got a five-character code on the image itself, derived from a secret key kept outside the base. The code can only be obtained by looking at the figure. The agent that opened the sheet recorded the code along with its notes, and a script recalculated the expected code and compared the two. Result: 3,072 video sheets and 552 from the HIG, all with a matching code. There was no divergence.

The reading was done in seventeen waves of agents, each agent with up to 25 sheets and required to describe only what was in the image, to cite the frames that differ from one another and to mark as illegible whatever could not be read. A video counts as watched only when the code on every one of its sheets has been checked.

### 6. Syntheses and adversarial verification

For each video and each page with an image, an agent wrote the synthesis of what the frames or the illustrations show, with the reference for each item. A second agent, instructed to knock down the first one's work, checked it item by item against the notes and corrected exaggerations, wrong references and content that came from the speech instead of the image. On the 158 HIG pages there were 206 corrections and 8 items removed. On the 175 videos, the corrections added up to hundreds, always recorded. In 222 syntheses a divergence between what the image shows and Apple's official description was noted.

### 7. Integration and essence

The syntheses went into the cards, and each card now says how many sheets were viewed. Fourteen agents extracted the recurring patterns from the 333 syntheses, one consolidated everything into the chapter "What only the images show" and a verifier checked the 60 items, correcting 20 of them.

## Structure

<img src="docs/assets/en/base_map.png" alt="Map of the base: essence at the center, HIG and videos beside it, syntheses, notes and skill below" width="100%">

```
kb-en/                      the base in English
  00_APPLE_ESSENCE.md       synthesis in nine chapters
  TEXT_VERIFICATION.md      coverage and fidelity of the text layer
  VISUAL_VERIFICATION.md    proof method and numbers of the visual layer
  VISUAL_INDEX.md           reading status of each video and page
  hig/                      18 files, one card per guidelines page
  videos/                   18 files, one card per session
  visual_synthesis_hig/     visual synthesis per page
  visual_synthesis_videos/  visual synthesis per video
  visual_essence/           patterns extracted for chapter 9
kb/                         the original base in Portuguese, same structure, plus
  visual/                   sheet-by-sheet notes for each video
  visual_hig/               sheet-by-sheet notes for each page
  visual_logs/              reading records and expected codes
skills/apple-design-en/     the skill in English
  SKILL.md                  the skill for Claude Code
  SYSTEM_PROMPT.md          the portable version, for any model
  system.md                 values of the visual system
  platforms.md              differences between platforms
  anti-patterns.md          the 37 anti-patterns, with source
  checklist.md              the 38 review questions, with source
skills/apple-design/        the skill in Portuguese
catalogo_hig.json           the 173 pages
catalogo_videos.json        the 188 videos, with URL, duration and status
*.py                        the process scripts, in the order described above
```

The sheet-by-sheet notes are the raw record of the reading and remain in Portuguese. The English cards and syntheses cite them by video id and sheet number, which are the same in both languages.

## Reproduce

The scripts run with Python 3, ffmpeg, yt-dlp and, for the videos with no transcript, whisper.cpp with the large-v3-turbo model. The order is `crawl.py`, `to_text.py`, `timed_transcripts.py`, `media_pipeline.py`, `hig_images.py`, `hig_sheets.py`, then the reading waves by agents, `verify_codes.py`, `assemble_visual.py`, the integration scripts, `relatorio_visual.py` and `limpeza_final.py`. The whole process ran on a 16 GB MacBook, and reading the contact sheets and the syntheses used around 77 million tokens in Claude Code agents.

## Use and rights

Study material about interface design, derived from public Apple content. The guidelines, the videos and the illustrations belong to Apple. This base does not replace the source: every card carries the URL of the page or session it came from.
