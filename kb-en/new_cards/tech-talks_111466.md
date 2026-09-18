## Design for iPhone Duo (id: tech-talks_111466, 10.8 min)

Basis: transcript (frames not viewed yet). Local automatic transcript made with Whisper, it is not Apple's official one; proper names and terms may carry hearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111466/.

Central thesis: Two designers from Apple's design team, Marcos and Vince, present the iPhone Duo, the first foldable iPhone, and argue that the app should feel like a single experience that adapts to the device's different screen sizes and positions. To do this, instead of a layout tailored to each position, the way is to target two size classes, move the controls to the side and keep the app freely resizable.

The design process Apple describes:
1. The speech does not describe an internal design process in steps; it only says that the team learned a lot by adapting their own apps to the iPhone Duo. What follows is the order of the session's script.
2. First understand the device's principles: closed, compact and familiar; open, the largest screen ever made on an iPhone; and the positions of use (partially folded like a book, propped on a table like a laptop with the inner screen facing the person, or standing propped on its edges).
3. Understand how the system reorganizes the interface: controls on the side on the outer and inner screens, content moved away from the fold when the device is partially folded, a new 50/50 split screen and picture in picture pinned to the top.
4. Adapt the app by targeting two size classes, with layout margins and horizontal safe area insets, without designing a layout for each position.
5. Evaluate whether an optional layout for the table-propped position is worth it, keeping the same controls and the same hierarchy.
6. Map the existing iPhone app's controls to the side column and handle the exceptions.
7. Resolve the outer screen's asymmetry by choosing between shifting the content, centering on the whole screen or combining the two approaches.
8. Choose a strategy for the inner screen: split view, content optimized for the wide screen or tab bar presented as a sidebar.
9. Check the behavior of sheets in each position and use system components to inherit the fold avoidance.

Principles stated and why:
- Closed, the device is compact and familiar and fits comfortably in the hand; open, it reveals the largest and most immersive screen ever made on an iPhone. Why: it's the best possible screen for apps and content on a device that still fits in a pocket.
- Several ways to hold and prop up the device. Why: it gives flexibility and lets the person use the device however they want, in any situation.
- On the outer screen, buttons and controls that normally sit at the top and bottom move to the right side. Why: it maximizes vertical space, makes it easier to reach with the right thumb and creates a continuous area on the left for the content, comparable to that of an iPhone with a traditional proportion. On the inner screen the controls also move to the side, for the same reason of vertical space and reach.
- With the device partially folded like a book, the content moves out of the central region. Why: text and images become easier to read away from the curve, buttons and interactive elements become easier to hit on the sides, and the curve becomes a natural divider of the layout.
- In portrait, partially folded, the interactive elements move down to the bottom half. Why: they become easier to reach and the device stays stable on the surface.
- The new split screen is built on top of the iPhone's home gesture. Why: it feels fluid and familiar; the two halves work independently, so you can keep one task on one side while using the other.
- In the split screen, the controls stay on the outer edge; an app on the left side moves the controls to the left edge. Why: they stay within thumb's reach and away from the central region.
- Do not design a layout for each position; target size classes and avoid fixed widths, breakpoints or metrics tied to a specific screen. Why: people use the device in many positions and the app needs to look good in all of them; whoever already uses these tools should have an app that already adapts.
- A special layout for the table position needs to have the same controls and the same overall hierarchy as the other positions. Why: functionality should not be tied to a specific position.
- Horizontal bars only remain on the inner screen in portrait. Why: there is vertical space to spare for the content there.
- On the outer screen, most of the content needs to be shifted. Why: so it doesn't stay hidden behind the controls.
- Some interfaces should still center on the whole screen, without shifting. Why: this works well for immersive, highly visual interfaces that don't scroll, as long as there is certainty that the controls on the right won't block interactive elements.
- On the inner screen, do not just deliver a stretched iPhone app.
- The hierarchy should not change between the outer and inner screens, and functionality should not be limited to one position. Why: people can open and close the device frequently while using the app, so it needs to be predictable and consistent inside and out.
- The tab bar as sidebar doesn't suit every app. Why: it works better in information-dense apps.
- Keep interactive elements out of the curve region whenever possible. Why: the team found that buttons are hard to tap when they fall exactly on the fold. Scrollable content doesn't need to avoid this region.

Concrete interface-building techniques, with exact numbers when spoken:
- The speech does not give interface values in points, pixels, font sizes, colors or durations. The numbers stated are structural counts: the 50/50 split of the split screen, the two size classes, the two-column layout and the three options for the inner screen.
- Size classes: compact width on the outer screen and regular width on the inner screen. Avoid fixed widths, breakpoints and metrics for a specific screen. Build with layout margins and horizontal safe area insets and think of the app as freely resizable.
- Closed outer screen: wider and shorter than that of a traditional iPhone. The right side column houses the top bar, the app's toolbars and navigation controls like the back button, plus the redesigned status bar and the Dynamic Island, which expands vertically when Live Activities arrive.
- Shared vertical space: the app's controls share the side column with dynamic system elements (Live Activities and the status bar). Without enough space, the app's controls automatically collapse into an overflow menu.
- Mapping of the iPhone app's controls: top toolbar buttons go to the top of the vertical space; bottom toolbar buttons go to the base; the tab bar stays aligned at the bottom. Exception: items too wide for the space on the right, like a text button or a "segment to control" (uncertain term in the automatic transcription), stay in the navigation bar.
- Horizontal bars: kept only on the inner screen in portrait.
- Fold: content moves out of the center with the device partially folded; in portrait, the interactive elements go to the bottom half.
- Split screen: dragging an app to the side creates the 50/50 split into two independent halves; controls on the outer edge of each half.
- Picture in picture: the video can be pinned to the top of the screen and the current app resizes vertically to fill the remaining space; when partially folded, the video comes to occupy half the screen, and apps adjust vertically to the different video sizes in real time.
- Optional layout for the table position, designed for hands-free use: media on top and tappable controls on a stable base below.
- Asymmetric layouts on the outer screen, which the speech calls "layers" (uncertain term in the automatic transcription), with three approaches: (a) shift the content, which happens on its own when the app aligns to the horizontal safe area insets; (b) center on the whole screen without shifting, for immersive, highly visual interfaces without scrolling; (c) combine a full-width background image or header with recessed scrollable content in the foreground, keeping every interactive element inside the scrollable area so that nothing stays covered.
- Inner screen, three options: split views that show several levels of the app's hierarchy at the same time; content optimized for the wide screen, for example a vertical stack that reorganizes into two columns when there is more horizontal space; and, for apps with a tab bar, presenting the tab bar as a sidebar.
- Sheets on the outer screen: by default the sheet's controls also move to the side. You can prevent this by turning off the vertical bar on the sheet, which works well for sheets with a single toolbar button; in that case the sheet stops right before the front camera and the status bar repositions itself.
- Sheets on the inner screen, in landscape and in portrait: use the standard horizontal bars. With the device partially folded, sheets slide to the side so they don't rest on the fold.
- Fold avoidance: behavior that pushes interactive elements away from the fold when the device is partially folded, built into system components like sheets, alerts, menus, toolbar buttons and others. Use these components whenever possible to get the same behavior in the app. Scrollable content doesn't need to avoid the region.

Examples cited:
- Positions of use (partially folded book, laptop on the table, standing on its edges): teach that the app needs to work in many configurations without a design for each one.
- Split screen to keep one task on one side while using the other half: teaches that the halves are independent and that the controls go to the outer edge.
- Video in picture in picture pinned to the top, which grows to half the screen when folding: teaches that apps need to adjust vertically in real time.
- Hands-free use with the device on the table, with media on top and controls below: teaches that a layout per position is optional and cannot change controls or hierarchy.
- Apple's own apps adapted to the iPhone Duo: the team learned that several approaches work well depending on the content's style.
- Health app with the tab bar presented as a sidebar on the inner screen: teaches that the sidebar works better in information-dense apps.
- Sheet with a single toolbar button and the vertical bar turned off: teaches when it's worth preventing the sheet's controls from migrating to the side.

Quotes:
"Apps should feel like a single experience adapting to the different display sizes and poses."
"You don't want to tie functionality to a specific pose."
