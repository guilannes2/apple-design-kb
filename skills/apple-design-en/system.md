# Apple's visual system: values and rules

Literal copy of section 3 of the essence (`kb-en/00_APPLE_ESSENCE.md`): typography, color, materials, layout and spacing, icons and symbols, motion, haptics and sound, writing and accessibility. The numbers here are the only ones the skill may use without researching.

## The system

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
