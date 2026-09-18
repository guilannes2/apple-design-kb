# Platform differences

Literal copy of section 4 of the essence (`kb-en/00_APPLE_ESSENCE.md`). An interface is designed for the platform it will run on, never ported from another.

## Platform differences that change design decisions

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
