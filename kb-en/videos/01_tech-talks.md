# tech-talks

## Discover the Apple Design Resources (id: tech-talks_111427, 5.6 min)

Basis: transcript and 8 of 8 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/tech-talks/111427/.

Central thesis: the Apple Design Resources (UI kits for Sketch and Figma, hardware bezels, Icon Composer, SF Symbols) exist so that anyone with an app idea can express it quickly with high fidelity to the final result, creating a common language between designer and engineer.

The design process Apple describes: first, go to developer.apple.com/design/resources to see everything that is made available. In Figma, load the kits through the UI's own asset panel or through the Apple Community page, where the platform UI kits and technology templates are published. In Sketch, activate the libraries through the settings panel (Library pane), just by checking a box. When assembling a screen, use the ready-made examples (iPhone, iPad), which bring the main component already in the context of other elements, saving assembly time. To check the appearance in dark mode, in the speech the presenter describes selecting the frame with the components, going to the design panel, appearance section, choosing the menu with the swatch book icon and selecting dark, which redraws all the components of that frame. It is also recommended to open the kits' original files to see the internal guides for color, materials and text styles.

Principles stated and why: the kits are treated as a design product in themselves ("designers making design tools for other designers"), so they need to be organized and easy to use; use the Human Interface Guidelines together with the kits, because the kits alone do not explain where, when and why to use each component; keep the files synchronized with operating system changes, notifying the user when a library changes and allowing them to accept the update, so that the mockup continues to be a faithful representation of the final product.

Concrete interface-building techniques: the video is about where to find and how to load the resources, it does not describe specific layout, typography or color values.

Examples cited: Figma's asset panel and Apple Community page (sources of the UI kits and technology templates in Figma); Sketch's library pane (activation by checkbox); composition examples for iPhone and iPad within the kits; switching to dark mode within Figma as a visual fidelity test.

Quotes: "designers who are making design tools for other designers" and "everyone is really literally speaking the same language".

<!-- visual:tech-talks_111427 -->
### What the images show
Basis: 8 of 8 frame sheets viewed, all codes checked.
- Design tools in real use on screen, not described from outside: Figma with an asset library panel and layers panel, Sketch with an artboard named by iPhone model and a library panel, and Icon Composer with a properties panel listing rendering mode, gradients, color and background (sheets 0001 and 0003).
- Light and dark pair of the same component: the same share sheet reappears with identical text, icons and positions, inverting only background and text color, and the layers panel names the second frame as the dark version (sheet 0004, q0031 to q0034).
- Anatomy of that share sheet: header with title and close button, row of circular avatars with name below, grid of action icons and a text list of actions with icon on the left, ending in an edit actions button (sheet 0004).
- Structure of the resource pages: horizontal bar of category icons by platform and by resource type, with download cards grouped by system right below (sheet 0002), and, in the product bezels section, blocks in a three-column grid with the name in bold, available formats and date and size in small gray (sheet 0001).
- Fixed template of the guideline pages: large component title, definition paragraph, side box of supported platforms with device icons and an example card on a gradient background that changes color depending on the component, pink for tables, orange for dropdown buttons, orange and pink for popovers (sheet 0005, q0038 to q0041).
- Kit gallery on the community page: cards each in a different solid color, with a white outline pictogram at the center, bold title below and small metrics in the footer, in a five-column grid, mixing kits by platform and cards for specific technologies (sheet 0003).
- Real extent of the example catalog, which the speech only mentions in passing: dozens of thumbnails organized in a grid by component category, most in monochrome wireframe with a few already-colored variations, including keyboard on iPhone and iPad side by side and lock screens with overlapping notification cards (sheet 0006, q0046 to q0052).
- Sketch's color picker open over the iPhone mockup at two moments, with a checkered grid of hues, a full spectrum bar, recent swatches at the base and an opacity control (sheets 0003 and 0004); in Icon Composer the color control appears in another form, as gradient adjustments with a primary field and a percentage (sheet 0001).
- Style panels within the Sketch file: large circular color swatches in a row, a grayscale next to it and a block of text styles repeated in a light column and a dark column (sheet 0005).
- Home screen mockup faithful to the real system: grid of icons over a gradient wallpaper, a dock of four icons and a search bar in the footer, with widgets listed in the layers panel alongside (sheet 0004).
- The site itself suggesting the material it documents: the featured banner has a translucent blue gradient background cut by a lighter diagonal stripe, with title, subtitle and two text links below (sheet 0002).
- Only data-capture flow shown in the video: the Feedback Assistant window with a sidebar of saved items, a form of stacked labeled fields, two triage dropdown menus, a file drag zone and a solid purple submit button against a secondary gray one (sheet 0007).
- Title slide on a light gray background with black text aligned left, higher contrast than the dark slides seen in the other video in the batch (sheet 0002).
Visual proportion: full-screen tool and site captures predominate, interspersed with the presenter sitting at a desk with a laptop and notebook, and sheet 0008 brings only a final cut frame with no interface.
Recorded divergences or limits: on sheet 0008 the notes record that the remaining spots in the frame grid are empty because the video ends shortly after, leaving a single real transition frame, with no interface to describe.
<!-- /visual:tech-talks_111427 -->

## Prepare your app for iPhone Duo (id: tech-talks_111461, 10.2 min)

Basis: transcript and 9 of 9 frame sheets viewed, codes checked. Local automatic transcript made with Whisper, not Apple's official one; proper names and terms may have hearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111461/.

Central thesis: David Jackson, engineering manager on the UI Frameworks team, explains that the iPhone Duo forces the app to change size in each posture (open, closed, rotated or folded), and that because of this the good practices of flexible, adaptive layout matter more than ever. An app well made for the device decides the layout by size classes, uses the standard navigation and presentation components, respects safe areas and asymmetric margins and turns to reserved regions when it needs its own interface.

The design process Apple describes:
1. Understand the starting point without doing anything: the app already works on iPhone Duo even without having been compiled with the iOS 27 SDK. With the device closed, it occupies the space to the left of the status bar and the camera; open, it appears at a familiar size and proportion.
2. Take advantage of the work already done for resizing iPhone apps: with the iOS 27 SDK adopted, the app extends to the left of the status bar area on the inner screen.
3. Compile with the iOS 27.1 SDK to occupy the whole screen: the app goes all the way to the edge, and the standard navigation and toolbar buttons start to be arranged vertically, below the status bar.
4. Download Xcode 27.1, choose the iPhone Duo simulator in Device Hub (also spelled "DeviceHub"; uncertain term in the automatic transcript) and use the control buttons at the bottom of the screen to open, close, rotate or fold the device.
5. With the app using the whole screen, look for layout problems in each posture and apply the general practices of flexible layout, so that the app resizes correctly on any platform.
6. Apply the iPhone Duo-specific guidance: standard navigation and presentations, bars, safe areas, margins, testing in split-screen multitasking and reserved regions.
7. Check everything with Xcode's app modernization skill, now called App Precisability (uncertain term in the automatic transcript).
In the final recap the order is: download Xcode 27.1, simulate the app on iPhone Duo through DeviceHub, follow the adaptive layout practices presented and try the App Precisability skill.

Principles stated and why:
- Flexible layout is more important than ever. Why: the app needs to resize to fit every posture, open, closed, rotated or folded.
- iPhone Duo is a continuation of an old adaptation, not a break. Why: iPhone apps have already adapted to new screen sizes and formats and to special regions like Dynamic Island; the Duo brings a new screen format and a new camera position. In iOS 27 people can already make the app bigger than ever through iPhone mirroring on the Mac, and opening and closing the Duo works the same way. The app can react to other size class limits, but it remains an iPhone app.
- The best layouts are adaptive across a continuum of devices. Why: they do not assume screen size or device capability from the "user interface ADM" (uncertain term in the automatic transcript) and use tools like size classes to differentiate small and large layouts.
- Size classes express the experience the app should offer depending on the available space. Why: the horizontal and vertical classes are loosely tied to the available space in each dimension.
- Do not decide layout by interface orientation, just as you do not decide by Idiom; use size classes. Why: on the inner screen the orientation behaves differently and does not respect the interface orientations the app supports.
- Avoid referring to the main screen in code and, if possible, to any screen. Why: on a device with two screens that reference is ambiguous and will be deprecated in a future version. Prefer local concepts.
- Use the standard navigation patterns. Why: they are a great way to adapt to every iPhone Duo posture, and the components are fully adaptive.
- Respect the safe areas. Why: it ensures the app's controls stay reachable and that the app stays entirely visible.
- Do not assume that insets on opposite sides are equal; treat each side separately. Why: safe areas tend to be asymmetric, especially on iPhone Duo, where vertical buttons can appear on the left side in landscape and in split-screen multitasking.
- Layout margins are also asymmetric. Why: this lets foreground content get closer to the vertical buttons and the status bar without losing the margin on the opposite side.
- Test the handling of safe areas in different configurations, with no exception for split screen. Why: content arranged vertically can appear on either side of the app.
- iPhone Duo is a great opportunity to support landscape orientation (said right after explaining that the orientation on the outer screen behaves like on any iPhone). Why: people may want to prop the phone up like a tent.

Concrete interface-building techniques, with exact numbers when spoken:
- The speech gives no numeric interface value (points, sizes, margins, radii, durations). The numbers spoken are only version numbers: the iOS 27 SDK, the iOS 27.1 SDK, Xcode 27.1, the iOS 26 concentricity APIs and the "WW26" session (uncertain term in the automatic transcript).
- Size classes: in SwiftUI, read from the environment; in UIKit, from the trait collection.
- Size class combinations on iPhone Duo. External screen, like on other iPhones: in portrait, regular vertical class and compact horizontal; in landscape, compact vertical and horizontal. Internal screen: regular horizontal and vertical, because the extra space allows showing more content, like sidebars.
- Orientation: on the external screen it behaves like on any iPhone; on the internal screen it does not respect the supported orientations.
- Screen access: use environment, trait collection or the scene's limits (bounds); if it is really necessary to access the screen, get it dynamically from the window scene.
- Corners: for the interface to fit perfectly into the screen's corners, use the iOS 26 concentricity APIs, updated for the Duo's screen formats. In SwiftUI, Concentric Rectangle; in UIKit, UI Corner Configuration.
- Full screen and orientation: the Duo still respects the "UI requires full screen" key, but the app still resizes when the person opens or closes the device. The Duo respects the supported orientations, but the app is scaled on the internal screen, including in split-screen multitasking.
- Column navigation: Navigation Split View in SwiftUI or UI Split View Controller in UIKit. With the device closed, the columns collapse into a single navigation stack; open, the columns appear side by side and also overlapping.
- Tabs: Tab View in SwiftUI and UI Tab Bar Controller in UIKit adapt to every posture. By default the tabs appear on the internal and external screens and lay out vertically when it fits. On the internal screen it is possible to choose a sidebar with richer navigation: in SwiftUI, set the default tab bar placement to sidebar; in UIKit, set the preferred placement to sidebar.
- Sheets: on the external screen they can have vertically arranged buttons; on the internal screen they are centered. Popovers, context menus and alerts also adapt to each posture.
- Bars: navigation bars, toolbars and tab bars stay outside the safe area and, on their own, avoid the system interface, such as the status bar, and hardware features, such as the camera. Horizontal bars provide insets on top and bottom; vertical bars provide insets on the start and end sides (leading and trailing).
- Foreground inside the safe area: interactive controls go inside it. In SwiftUI the content already sits within the safe area by default; in UIKit, with manual layout, use the view's safe area insets, or use Auto Layout pinning the views to the safe area layout guide.
- Background outside the safe area: background elements, such as art that goes edge to edge, can occupy the whole space and pass behind the toolbars and the sidebars. In SwiftUI, "ignore safe area"; in UIKit, use the view's bounds.
- Split-screen test in the Device Hub: view the app on the internal screen, drag the app by the start indicator (home indicator) at the bottom to one side of the screen, wait for the drop area to appear, and then drag it to the other side.
- Reserved regions, new in iOS 27.1: an API for the app's own interface to use as much of the screen as possible without colliding with the system interface. In SwiftUI, "reserved region", to position elements outside the safe area safely while maximizing usable space; in UIKit, UI View Reserved Region. Recommended for custom bars or edge-to-edge interfaces, and also for interfaces that adapt to the fold.
- Summary of safe area practices given in the talk: use standard bars, which adapt to the safe area on their own; align interactive or visible foreground content to the safe area, letting the background pass through it; consider and test safe areas and asymmetric margins; in more complex layouts, consider reserved regions.

Examples cited:
- The three stages described in the talk for the app on iPhone Duo (without the iOS 27 SDK, with the iOS 27 SDK, with the iOS 27.1 SDK): in each one the app occupies more screen space, until it reaches the edge with the standard buttons arranged vertically under the status bar.
- iPhone mirroring on the Mac in iOS 27: allows the app to be bigger than ever, and opening and closing the Duo works the same way; the app can react to other size class limits, but it remains an iPhone app.
- Phone propped up like a tent: justifies taking advantage of iPhone Duo to support landscape.
- Sidebar on the internal screen: example of the extra content that regular classes allow, both in layout and in the option of tabs as sidebar.
- Vertical buttons on the left side in landscape and in split screen: a concrete case of asymmetric safe area and of why to treat each side separately.
- Background art that goes edge to edge passing behind bars: a case of content that can ignore the safe area.
- App modernization skill introduced in the session "Modernize Your UI Kit App" (later written as "Modernize your UIKit app"; uncertain term in the automatic transcript), renamed in Xcode 27.1 as App Precisability (uncertain term in the automatic transcript) and now with support for SwiftUI and iPhone Duo: an efficient way to check whether the app follows every adaptive layout practice.
- Complementary sessions cited: "Leverage multiple displays and screens on iPhone Duo" (about the device's screens), "Raise the bar with iPhone Duo" (about vertically arranged content) and "Strike a pose" with adaptive layouts on iPhone Duo (about reserved regions and interface that adapts to the fold; title said ambiguously in the automatic transcript).

Quotes:
"The best app layouts are adaptive across a continuum of devices." (David Jackson)

<!-- visual:tech-talks_111461 -->
### What the images show
Basis: 9 of 9 frame sheets viewed, all codes checked.

- The side-by-side comparison of the same content across different SDK versions is the opening device, always with a footer caption naming the version: a single-column list under "pre-iOS 27.0 SDK built apps" (sheet 0001, q0005 and q0006), a two-column grid with one extra card under "iOS 27.0 SDK built apps" (sheet 0001, q0008 and q0009) and a four-card grid under "iOS 27.1 SDK built apps" (sheet 0002, q0010). The on-screen text label fixes a difference that the talk describes only in words.
- Size class is explained first through abstract geometry, with no real app at all: gray rectangles with colored measurement arrows, orange for the horizontal dimension and blue for the vertical, with the labels compact and regular (sheet 0004, q0028 and q0030), plus two unlabeled gray shapes, one folded at an angle like a half-open book and the other closed with rounded corners (q0029). Before that, a simple rectangle gains arrows and the labels horizontal and vertical to anchor the vocabulary (sheet 0003, q0024 to q0025).
- The code panels appear pairing SwiftUI and UIKit in the same frame or in immediate sequence, next to the device render or the shape that represents it: size class environment against trait collection (sheet 0003, q0024 and q0025), ConcentricRectangle against UICornerConfiguration (sheet 0005, q0037 to q0038), defaultTabBarPlacement against the equivalent property of the tab bar controller (sheet 0005, q0045; sheet 0006, q0046), safeAreaInsets against ignoresSafeArea (sheet 0006, q0052 to q0054).
- Solid color and semitransparent layer mark screen regions in two distinct ways. The green fills the entire screen, with corners coinciding with the device's outline, to demonstrate concentricity with no app content around it (sheet 0005, q0037 and q0038). The blue is a semitransparent layer over the content and changes meaning between frames: first it covers the whole content area (sheet 0006, q0052 and q0053), then it goes edge to edge at the bottom (sheet 0007, q0055 and q0056) and finally shrinks to a narrow strip only on the left edge (sheet 0007, q0057), making visible the asymmetry that the talk describes.
- A slide of measurements places two labeled arrows pointing inward on the same device, "Layout Margin" over a purple band on the left and "Safe Area Inset" over a blue band on the right (sheet 0007, q0058), separating in the image two concepts that the talk treats in consecutive sentences.
- A design tool on the Mac, with a window named "iPhone", reappears twice to prototype the device's poses with the same content: open, closed next to a solid black panel and fully open in book format (sheet 0002, q0011 to q0013), and then the same detail screen in open pose and compressed in closed pose (sheet 0007, q0060 and q0061). It is a construction step that the talk does not detail beyond mentioning Xcode's Device Hub.
- The navigation components get a footer caption naming what is on screen, "NavigationSplitView" and "TabView", over pairs of mockups of Mail and a health app in two device sizes (sheet 0005, q0042 to q0045).
- The adaptation of sheets appears in the difference between consecutive frames: the overlaid sheet changes content and one of the devices starts showing buttons arranged vertically on the left edge of the screen (sheet 0006, q0046 to q0047).
- Newly launched features are marked inside the slide itself: a rectangular "NEW" badge in the top right corner of the slide that carries the code label UIViewReservedRegion (sheet 0008, q0064 and q0065) and a green circular "27.1" badge on the agent-coding slide (sheet 0008, q0069 and q0070).
- The screen shows a code agent interface integrated into the editor that the talk does not name in this passage: next to the Swift code, the next frame gains a prompt bubble with a resizing best-practices instruction and the status line "Updating main screen references" (sheet 0008, q0069 to q0070).
- The rules are delivered as short lists in white typography on black, with the items appearing gradually: "Orientation" goes from one to three items (sheet 0004, q0032 to q0033), "Screen" gains a second item (q0034 to q0035), the safe area summary closes with three points (sheet 0008, q0067) and the closing lists three concrete actions (sheet 0009, q0073).
- The topic list "Getting Started", "Flexible Layout" and "iPhone Duo Layout" works as a chapter marker, reappearing with the current item in bold and the others dimmed (sheet 0001, q0004; sheet 0002, q0015), an orientation that the talk does not verbalize at each cut.
- The history of resizing is visual: a grid of six thumbnails of the same Mail screen in different formats and proportions, including the open foldable, later receives the title "Evolution of iPhone apps" with a straight rectangular, semitransparent iPhone highlighted at the center (sheet 0002, q0017 and q0018).

Visual proportion: of the 75 frames recorded, sixteen show only the presenter, in short cuts between blocks; the rest are topic slides, device renders with a real app, code panels, design tool windows and a few opening and transition frames.

Recorded divergences or limits: sheet 0008 notes that the label "Agentic Coding" appears on screen without being said in the speech of the segment, being a visual addition from the slide; the synthesis of the sheets notes that the design tool on the Mac is not described in detail by the speech, which mentions only Xcode's Device Hub.
<!-- /visual:tech-talks_111461 -->

## Design for iPhone Duo (id: tech-talks_111466, 10.8 min)

Basis: transcript and 13 of 13 frame sheets viewed, codes checked. Local automatic transcription done with Whisper, not Apple's official one; proper names and terms may have hearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111466/.

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

Concrete interface-building techniques, with exact numbers when stated:
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

<!-- visual:tech-talks_111466 -->
### What the images show
Basis: 13 of 13 frame sheets viewed, all codes checked.

- The column of controls fixed to the right edge is not shown once and explained, it is repeated nearly identical across several system apps: mail with trash, archive, reply and compose stacked (sheet 0003, q0019, q0020 and q0023), calls with the controls inside a vertical capsule (q0021), reminders with the icon bar outside the content block (q0026), FaceTime with circular buttons and the end-call one in red at the bottom of the column (sheet 0004, q0028), and the music player (sheet 0012, q0108). The speech states the pattern in general terms; the image shows that it is the same in at least five apps.
- The measurements appear drawn over the real capture, not in a separate diagram: a solid gray band between the text columns labeled "Layout Margin" (sheet 0006, q0050) and a blue band covering the right edge labeled "Horizontal Safe Area Inset" (sheet 0006, q0051; sheet 0009, q0076, this one with the label written outside the device frame). From one frame to the next the annotation changes color and position, moving from the center of the text to the edge of the screen.
- The two size classes are named in writing under the devices, "Compact Width" on a single narrow screen and "Regular Width" on a wide screen with list and message side by side, with the same email content in both (sheet 0006, q0049).
- The grid of six renders of the same app in every pose, closed in portrait, closed in landscape, open flat and folded at varying angles, appears twice in the video with different content, email and list editor (sheet 0006, q0047 and q0048; sheet 0011, q0093 and q0094). It is the visual argument for a single adaptable interface, with no redesign per pose.
- The reorganization when folding is shown by consecutive frames with the same content: the full-screen video comes to occupy the upper half with the conversation below (sheet 0005, q0043 to q0044), the player controls move down to the lower half (sheet 0004, q0031 to q0032), and the FaceTime participant thumbnail changes position (sheet 0004, q0028 to q0029).
- The split-screen pattern is named on screen with the label "Split View" under the capture (sheet 0010, q0084), while the other examples appear without a label in Maps, Messages, Music, Health and Photos (sheets 0004, 0005, 0010, 0011 and 0012), including compared across two device sizes with the split keeping the same proportion (sheet 0010, q0087).
- In split-screen pairs each half anchors its own controls to the outer edge, the left app to the left and the right app to the right (sheet 0005, q0037 to q0040), and swapping position between the two apps keeps this anchoring (q0039 to q0040).
- The sidebar in place of the tab bar appears in a single app, the health one, with a vertical list of categories with icon and text in the left column and the sleep score card on the right (sheet 0010, q0090; sheet 0011, q0091).
- The case of the immersive interface with no offset is shown by direct contrast: the level app with a centered green circle on the narrow device comes to fill the entire screen with green on the open, wide device (sheet 0009, q0077 to q0078), while the other examples keep the content set back away from the controls.
- The gain in width reorganizes the content into more columns: the same list-editing screen gains additional icon columns when moving from the narrow device to the wide one (sheet 0011, q0097 to q0098) and then shares the space with the corresponding task list when the device is folded (q0099).
- Highlight bands mark control groups inside the side column: a gray band falls exactly over the four action icons at the bottom, separating that group from the rest (sheet 0008, q0067 to q0068), and a white pill button "Select" appears in the upper corner in a following frame (q0070 to q0071).
- The typographic hierarchy by opacity appears on the music screen: the current lyric line in full white and the following ones in light gray, with no playback control visible in the frame (sheet 0006, q0054).
- The hardware is presented with no interface at all, in studio renders over a neutral white background, showing the geometry of the device, the front camera notch and, in close-up, the rounded edge and a button (sheet 0002, q0017 and q0018).
- Black title cards with two lines, one in gray and the other in white, open the video and reappear identical at the section turn (sheet 0001, q0004; sheet 0006, q0046).

Visual proportion: of the 112 frames recorded, twenty-seven show only the presenters, alone or the two together; the other three quarters are device renders with real apps in use, annotated comparisons, system screens, title cards, hardware renders and blurred transitions.

Recorded divergences or limits: sheet 0007 notes that the gray band covering the lower half of one of the devices cannot be interpreted with certainty from the image alone; sheet 0012 notes that the speech deals with sheets while the frames show split screens of other apps, with no visible direct relation; sheet 0002 notes that the hardware renders have no direct content relation to the sentence about controls said in the same passage.
<!-- /visual:tech-talks_111466 -->

## Raise the bar with iPhone Duo (id: tech-talks_111462, 15.7 min)

Basis: transcript and 20 of 20 frame sheets viewed, codes checked. Local automatic transcription done with Whisper, not Apple's official one; proper names and terms may have hearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111462/.

Central thesis: In iPhone Duo, the first iPhone with multiple screens and a wider ratio, the controls that normally sit at the top and bottom (navigation bar, toolbar and tab bar) move to the side, where they are easier to reach and leave the vertical space for the content; they are the same components adapted to a different layout. To take advantage of this, the app needs to be recompiled with the new SDKs, use the bars from the system's containers, prepare the custom items for the vertical axis and declare overflow priorities so the system can adapt.

The design process Apple describes:
1. Understand the device and the principle: the wider silhouette gives horizontal space, the controls move to the side, the position stays the same when opening to the inner screen in landscape, and when opening in portrait, the larger screen returns to the familiar layout with horizontal bars.
2. Enable the new behavior: recompile the app with the most recent SDKs and use the bars provided by the navigation containers, instead of hand-assembled bars.
3. Understand where the content is positioned: navigation, toolbar and tab bar coexist in a shared region, with their own rules for Split View, inspectors, sheets and right-to-left languages.
4. Audit the toolbar's current configuration and make sure the controls follow the recommended order, from top to bottom.
5. Prepare the toolbar content for the vertical axis: provide title and icon for each item, adjust the axis when the default does not fit, reduce text-only items and adapt the custom views.
6. Manage the overflow: decide whether the toolbar or the tab bar compresses first, consolidate the app's own overflow into a single system-managed menu and assign visibility priorities.
7. Assess whether the app or a specific sheet should disable the vertical bar.
8. Closing: the idea was born from asking whether the bars really needed to stay at the top and bottom; the final outline repeats four steps (recompile with the new SDKs, audit the bars, update custom items, assign overflow priorities).

Principles stated and why:
- Every designer is an engineer and every engineer is a designer. Why: you need to understand both sides to build a great app.
- Top and bottom controls move to the side in the wide ratio. Why: it takes advantage of the width, preserves vertical space for the content and makes the controls easier to reach.
- The position of the bars stays the same when opening the device to the inner screen in landscape, and in portrait the larger screen returns to the familiar horizontal bars. The speech does not give a specific why; it only notes that they are the same components, adapted to a different layout.
- Keep the controls associated with their container, even though it is tempting to change the axis of all of them. The speech presents this as a summary of the previous rules: in complex layouts, items only move to the vertical axis when the container is at the edge of the screen.
- Expanded inspectors do not get their own vertical bar, since the Detail column already has one. Why: avoid confusion.
- The bar stays on the same side of the device in right-to-left languages; the content adapts around it and it remains fixed. Why: the bar is aligned to the hardware.
- Vertically, the items keep a clear hierarchy from top to bottom, with main navigation at the top and prominent actions next.
- Keep control positioning consistent. Why: not every pose uses vertical bars, and people should not have to relearn where the actions are.
- Vertical bars work better with symbol-only items. Why: unlike horizontal ones (fixed height, flexible width), vertical ones have fixed width and flexible height.
- Provide all of the item's information up front and let the system choose the representation for each context. Why: even an image item needs a title, because the system uses it when the item goes into the overflow or into an expanded form.
- Related items stay on the same axis. Why: an item that alternates between symbol and text, like the edit button, should not go to the vertical bar even if the symbol would fit in it.
- Minimize title-only items and custom views with text and image. Why: this way more content can go into the vertical bar, and in most cases these items can use the symbol representation.
- Ask whether the text only reinforces the symbol or carries its own information. Why: if it is supplementary, the symbol alone usually communicates the action clearly; if it carries meaningful information, the control should stay in the horizontal bar.
- Accessory bars remain attached to the keyboard, without moving to the vertical axis (the speech does not give the why).
- The app should not create additional spacing, whether the bar is horizontal or vertical (the speech does not give the why here and refers to Maria's video at DubDub25, a term uncertain in the automatic transcription).
- In navigation-focused experiences, the toolbar compresses first. Why: the main destinations remain accessible. This is the default behavior.
- In task-oriented experiences, the tab bar compresses first. Why: preserve the frequently accessed actions.
- Consolidate the app's own overflow into a single system-managed menu; not every existing menu should become overflow.
- The ellipsis is the standard overflow symbol on iPhone, so it should be reserved for that use, without bringing in symbols from other platforms, and other menus should get a distinct symbol. The reason given is simply that it is the standard symbol.
- When assigning priorities, think about what people access most often: frequently used actions should be among the last to go into the overflow. Likewise, controls that show important status, like items with a badge, stay visible for longer. Why, for these: preserve quick reading (glanceability).
- Most apps are good candidates for the vertical bar, but there are cases where it is worth disabling the bar. Why: in a single-page app with a heavy layout at the bottom, the horizontal layout can let the content expand fully; in a sheet full of controls with a single item, the vertical bar would reduce the available space.
- Result sought: content with a sense of space and accessible controls, the same familiar experience made for a completely new iPhone.

Concrete interface-building techniques, with exact numbers when spoken:
- The speech doesn't give numeric interface values (points, sizes, spacing, durations). The numbers mentioned are contextual: imagining the bars rotating 90 degrees into a vertical stack; badge API added in iOS 26; Maria's video at DubDub25 (uncertain term in the automatic transcription); What's new in SwiftUI from WWDC 26.
- Enablement: recompile with the latest SDKs. For other behaviors enabled by recompiling, the speech points to the session Prepare Your App for iPhone Duo.
- Containers in SwiftUI: use the toolbar modifier together with Navigation Stack or Navigation Split View; use Tab View.
- Containers in UIKit: prefer UINavigationController and UITabBarController, which manage their own bars; set the toolbar items on the view controller and place it inside a navigation controller, instead of creating a custom UIToolbar. In custom bars, the content of subcomponents such as UIToolBar, UINavigationBar or UITabBar is not taken into account.
- Shared region: navigation, toolbar and tab bar coexist in a shared region, in combinations that depend on the layout.
- Split View: only the Detail column takes part in the vertical bar; items in the other columns stay horizontal. Expanded inspectors don't get a bar of their own.
- Sheets: on the external screen, if the sheet already has a toolbar, it appears on the vertical bar; on the internal screen, they're centered by default with horizontal items. With the Preferred Placement API, a sheet positioned on the left has no vertical bar and one positioned on the right gets one.
- Right-to-left languages: the bar stays on the same side of the device and the content adapts around it.
- Item order: the top is reserved for primary navigation, such as back or close, followed by prominent actions, such as complete (done). With a navigation controller, the back button is added automatically.
- Custom back or close buttons: in SwiftUI, placement cancellation action; in UIKit, leading item with leftItemSupplementsBackButton set to false, which is the default.
- Prominent actions: in SwiftUI, placement top bar pinned trailing; in UIKit, pinned trailing group.
- The remaining items keep their original grouping, with a vertical spacer visually separating the top and bottom placements, even when unified into a single bar.
- Item representation: the app provides an icon and a title. In the top and bottom bars, the item prefers to show the icon (share button); without an icon, it shows the text (edit button); in the overflow, it shows title and icon. This doesn't change with vertical bars.
- Axis choice by the system: items described in the speech as Text-only items with an icon (uncertain term in the automatic transcription), such as back and share, move to the vertical axis; text-only items, such as edit, stay on the horizontal axis. Using Label in SwiftUI or the title and image properties of UIBarButtonItem already prepares the item.
- By default, SwiftUI and UIKit infer the axis from the item's content. To adjust it, there's the new AxisBehavior API.
- The system edit button stays on the horizontal bar automatically. Custom item that toggles between symbol and text: use the horizontal only axis behavior.
- A custom view in UIKit or a more complex view in SwiftUI stays horizontal by default; if it has a vertical representation, set the preferred vertical axis behavior to allow it to go to the vertical bar.
- Badge: instead of keeping the inline count, use a badge on the icon to turn an item with text and symbol into a symbol-only item; adopt the iOS 26 badge API for standard system appearance across all devices.
- Custom views on the vertical bar: they must fit within the bar's fixed width or have a layout adapted to vertical; consider adjusting metrics for the vertical representation.
- Detecting the vertical bar: read the toolbar vertical edge environment property or trait, inside the item's content view or custom view. The value is populated when the items can go on the vertical axis and is nil or unspecified when they can't.
- Material: like the horizontal bars, the vertical bar has no scroll edge effect by default, but gains a background when the Reduce Transparency accessibility setting is on; the content of custom views must stay legible in any case.
- Spacers: flexible ones have zero size on the vertical axis by default; fixed ones still respect the minimum size.
- If the bars haven't been updated to the new design yet, or the items haven't been grouped at the leading and trailing edges yet, the speech says now is the time to do it.
- Overflow: on the external screen in landscape, items overflow more because there's less vertical space; the bar also overflows when competing elements appear, such as the keyboard or picture in picture in OpenPortrait (uncertain term in the automatic transcription).
- Toolbar compression behavior API: configures, per view, whether the toolbar or the tab bar compresses first.
- System overflow menu: toolbar overflow menu in SwiftUI; additional overflow items in UIKit.
- Visibility priority: toolbar visibility priority lets you assign each item a high, low or custom priority, controlling the order in which they collapse. Prioritize by groups first, then, if needed, within each group. Visibility priority APIs exist in SwiftUI and UIKit.
- Disabling the vertical bar: the toolbar vertical behavior and preferred vertical bar behavior APIs.

Examples cited:
- Maria's app: it was already resizable, but the bars stayed horizontal. It teaches that recompiling with the new SDKs and using the containers' bars is still needed.
- Notes uses a toolbar, Clock uses a tab bar and Fitness uses both a toolbar and a tab bar. It teaches that the shared region receives different combinations depending on the layout.
- Share and edit buttons: they show how the system chooses between icon and text and which axis each item ends up on.
- The Clock edit button, which toggles between symbol and text: it doesn't go to the vertical bar, because related items must stay on the same axis.
- Custom selection button: uses the horizontal only axis behavior.
- Compass view in the top right corner: a custom view that supports a vertical representation and so gets the preferred vertical axis behavior.
- Inbox with the inline count swapped for a badge: it becomes a symbol-only item, suited to the vertical bar.
- Cart button with the total value in dollars: the text carries information of its own, so it stays on the horizontal bar.
- Custom action panel: it hides the titles and gets a little shorter when there's a vertical bar, freeing up space for other content.
- Podcast view: a navigation experience in which the toolbar compresses first, the default.
- Games app: a task-oriented experience in which the tab bar compresses first.
- Compose in Mail and new note in Notes: frequent actions that should be among the last to go to the overflow.
- Calculator: a single-page app with a heavy layout at the bottom, a candidate for keeping the horizontal layout.
- A sheet full of controls with only the close button: a candidate for disabling the vertical bar so as not to reduce the space.
- Closing joke: asked if there was anything else, the answer is that it's in the overflow menu.

Quotes:
"What if bars didn't have to be at the top and the bottom?"

<!-- visual:tech-talks_111462 -->
### What the images show
Basis: 20 of 20 frame sheets viewed, all codes checked.

- The video's thesis is demonstrated with the same app on two axes: the climbing app appears with the horizontal tab bar at the bottom and then with the same three icons stacked on the right edge, in the same order, with the header and list unchanged (sheet 0003, q0023 and q0027). Only the bar changes axis, nothing else.
- Right and wrong are marked inside the code, with a green check on the block that uses a navigation container and a red X on the block that instantiates the toolbar directly, and next to it the water app showing the thin vertical bar that results from the approved path (sheet 0004, q0034 and q0035).
- The juxtaposition of code and result is systematic, one sheet after another: a comment naming the API, a snippet with syntax highlighting and the corresponding mockup next to it (sheets 0004, 0007, 0008, 0010, 0011, 0012, 0014, 0016, 0018 and 0019). In one case the blue highlight moves to a different snippet between consecutive frames while the Mail mockup stays identical, drawing the eye to the line in question (sheet 0007, q0061 to q0062).
- The grouping inside the vertical bar is shown in isolation, with no app around it: close and send stuck together at the top, an empty vertical spacer and a loose icon below (sheet 0008, q0067), in a frame next to the one with the code for the group pinned to the end of the bar, which appears alongside the Mail mockup (q0066).
- The bar staying on the same side in a right-to-left language is shown by two calendars side by side, one in English and the other in Arabic: the content text mirrors, the column of icons stays on the right edge in both (sheet 0007, q0055).
- The difference between a text item and a symbol item appears in a device comparison: on the regular device, "Edit" as text and the share icon coexist on the horizontal bar at the top; on the foldable, the share icon migrates to the vertical side bar and "Edit" stays where it was (sheet 0010, q0082 to q0085), with the label-with-image code next to it.
- An instruction gets a typographic card all to itself, large white text centered on black, entering with a fade from low contrast to full white: "Provide titles." (sheet 0010, q0088 to q0089).
- The item that toggles between text and symbol is shown in both states: the world clock moves from the "Edit" text button to an orange confirmation circle, and each row of the list gets a red removal indicator (sheet 0011, q0095 to q0096); in a later frame, the code that forces the horizontal axis for this type of button appears next to another app, the trip planning one (q0099).
- The swap of the inline count for a badge is made with a pair of frames with the rest of the layout frozen: the inbox icon shows a loose number next to it and then a red circular badge on the icon itself (sheet 0012, q0107 to q0108). The same badge reappears on the calendar's vertical bar (sheet 0018, q0159).
- New APIs get a green circular "NEW" seal added in the following frame, without changing the code shown (sheet 0014, q0119 to q0120), and then overlaid on the device mockup (q0122).
- A single frame abandons the screen mockup and uses a spatial metaphor: controls in loose capsules floating in perspective over a checkered floor, grouped by proximity, with the red play button off to the side (sheet 0009, q0074). There's no equivalent in any other sheet.
- The ellipsis gets treatment as a reserved symbol: a whole frame with three dots enlarged on black, with nothing else (sheet 0017, q0145), and then the same symbol at the bottom of a vertical panel of five trip icons, separated from the rest by a slight gap (sheet 0017, q0150).
- The cases for disabling the vertical bar come in a device comparison: the calculator goes from a compact vertical numeric grid on the regular device to a widened horizontal strip on the foldable, with the same button count (sheet 0019, q0164), and the text formatting panel keeps the content centered with the side bar reduced to three icons (sheet 0019, q0165 and q0166).
- The inspector case is shown with a shape editor: the side bar disappears, the canvas gets the spotlight and then a "Properties" panel opens on the right with labeled fields on the left and values on the right, opacity at 100 percent and position coordinates (sheet 0006, q0046 to q0048). On the same sheet, the new list dialog appears with a vertical bar when it takes up the whole screen and with a horizontal bar at the top when it becomes a panel next to a side column (sheet 0006, q0052 and q0053).
- Black-and-white agenda slides, with no icon, with the current topic in white and the rest in gray, appear four times throughout the video (sheet 0003, q0019 and q0025; sheet 0008, q0071; sheet 0015, q0131), and the closing repeats the pattern with the title and three actions appearing below it (sheet 0020, q0172 to q0173).

Visual proportion: of the 175 recorded frames, about ninety-five show only the presenters, alone or the two in conversation; the rest are app mockups on a regular and foldable device, code blocks, agenda slides and isolated frames of hardware and spatial metaphor.

Recorded divergences or limits: the synthesis of the sheets notes that the side-by-side duplication of mockups and the juxtaposition of code and result are editorial choices of the presentation that the speech does not describe, dealing only with axis and orientation in words; sheet 0013 records a pair of frames with no difference in content, just repetition of the same pair of mockups.
<!-- /visual:tech-talks_111462 -->

## Strike a pose with adaptive layouts on iPhone Duo (id: tech-talks_111463, 18.0 min)

Basis: transcript and 15 of 15 frame sheets viewed, codes checked. Local automatic transcription done with Whisper, it is not Apple's official one; proper names and terms may have mishearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111463/.

Central thesis: On iPhone Duo, the hinge and the cameras create reserved regions, and good design depends on knowing when to adapt: move, resize or reorganize what already exists (the displacement pattern) to keep content and controls visible, reachable and unobstructed in any pose. For this, Apple presents the reserved regions API, for hand-built layouts, and the arrangements (split and overlay), layout containers for two views, always adapting only when it improves the experience.

The design process Apple describes:
1. Understand the device: several screens, each with its own size class, which should sound familiar to anyone who already designs for resizing; hardware features (the hinge and the two cameras of the external and internal screens) shape the available space and are called reserved regions, to be treated like any other area the layout already adapts to.
2. Understand each screen: on the external one, the camera is always present and system toolbars and tab bars are arranged vertically inside the new safe area; on the internal one, the interface can adapt to the fold or to the new FaceTime camera when active; with the device partially folded like a book, the fold divides the internal screen into several usable regions.
3. Know when to adapt: many interfaces flow naturally around the reserved regions; others call for an intentional approach, displacement.
4. Choose the scope of the displacement: from a button to an entire container or larger parts of the layout.
5. Decide where the element goes, guided by its purpose and by the device's pose (like a book or resting on a table), prioritizing what is contextual when more than one region serves.
6. Consider how the element adapts to the new surroundings: position and size are the most common changes, but other visual properties can also change.
7. Implement with the reserved regions API in SwiftUI or UIKit, querying division and occlusion regions, active or inactive.
8. Take advantage of the system components that already adapt to the fold and, for two-view layouts, use arrangements, choosing between split and overlay and recognizing when an arrangement is not the right tool.
9. Final preparation checklist: audit the app's centralized layouts; consider whether they can be turned into a two-column layout or which displacement pattern makes sense; use standard system containers and presentations, which bring a lot of behavior for free; in custom horizontal split or overlay layouts, consider the arrangement view to handle the layout on every supported device; identify the highest-priority controls positioned manually and adopt the Reserved Regions API for custom displacement where needed.
10. To use the hinge beyond layout, there is another API that responds to the fold state, covered in the session Leverage Multiple Displays and Scenes on iPhone Duo.

Principles stated and why:
- Content and controls that cross the fold behave like a photo spread across the two pages of a book. Why: near the spine, parts of the image become hard to see and it stops being read as a continuous image.
- On the internal screen, if the FaceTime camera viewfinder is central to the experience, keep important content and controls outside that area (the speech does not give a reason beyond that).
- Displacement adjusts the frame of existing elements according to the available space. Why: keep important content visible, reachable and unobstructed, even with the device partially folded.
- Choose the scope that matches the content: an element that adapts independently moves alone; elements that work together move together. Why: preserve the relationship between them.
- Be careful with excessive movement. Why: moving an element too far from its origin weakens the visual relationship between the two.
- Continuous scrolling content (articles, feeds, documents and lists) does not get displaced. Why: these experiences already adapt through scrolling, and moving them between regions can interrupt continuity.
- The purpose of the content decides where it goes, and that place can change as the device is used.
- With the device folded like a book, alerts go to the trailing side. Why: they end up closer to where they will appear when the device closes and the experience continues on the external screen.
- With the device resting on a table, the top region serves content that benefits from visibility at a distance, and the bottom one serves interactive controls. Why: the alert stays easy to find on top, and at the bottom the tappable elements have a more stable surface for touch.
- When several regions serve, prioritize the contextual one, as on iPhone the focused search sits above the keyboard (the speech gives the example, not a separate reason).
- Action sheets, alerts, menus and popovers are lightweight contextual experiences that can appear over a reserved region; the main goal is to keep them fully visible, and the system repositions them automatically.
- What all the examples have in common is moving, resizing or reorganizing what already exists; keeping content, functionality and layouts available. Why: people should have access to the full experience, whatever way they use the iPhone Duo.
- Inactive regions serve high-level decisions about the app, such as preferring an even number of columns in grids when there is a division region, active or not (the speech does not give the reason).
- When choosing an arrangement, follow first the patterns the app already uses. Why: HStack and VStack translate naturally into split, and ZStack into overlay, with built-in support for iPhone Duo.
- With no existing pattern, use overlay when there is a clear foreground and background relationship between the views. Why, in the example given: since the background content can be scrolled over the overlay, there is no problem with it being partially covered sometimes.
- Use split when the relationship is primary and detail. Why: it is important that neither of the two views is covered.
- Do not place navigation containers, such as Navigation Split View, inside an arrangement view. Why: arrangement views do not provide navigation infrastructure.
- Do not place arrangement views inside List and Scroll View. The reason given is just the nature of these scrollable views.
- Adaptive layouts should move, resize and adapt only when it makes the experience better, so the app feels designed for each pose.

Concrete interface-building techniques, with exact numbers when spoken:
- Numbers stated: 50/50 split of the columns in Reminders; the fold's division region, with the device open and flat, is inactive and has zero width; system-provided arrangements available in iOS 27.1; an arrangement organizes two views. The speech does not give point, margin or duration values.
- External screen: camera always present; system toolbars and tab bars arranged vertically inside the new safe area (refers to the session Raise the Bar with iPhone Duo).
- Basic displacement: an element centered with the device open moves, when folded, to the region that serves its purpose.
- Context menu: when selecting a photo in an album, instead of centering the menu in the trailing region, photo and menu move together and align around the fold.
- Search: with the device open, the field takes advantage of the extra space; when folded, width and position adapt to sit over the view being searched.
- System split view: keeps the two columns visible by adjusting the width and positioning them in a 50/50 split.
- Custom grid: preserve the outer margins and increase the spacing around the hinge, keeping each container within its region, so that all the grid items remain interactive when folded.
- Reserved regions in SwiftUI: query with a geometry proxy coming from a geometry reader or from the "non-geometry change modifier" (uncertain term in the automatic transcription), using the geometry proxy's new reserved region method to get the view's regions.
- Reserved regions in UIKit: reserved region method available on UIView.
- The frame property of a reserved region lets you incorporate it into your own layout.
- State: a region can be active or inactive; by default only the active ones are returned, and the inactive ones are obtained with the include inactive query option of the reserved region method.
- Division reserved region: represents the fold, because it divides a larger area into several smaller ones; it is only active when the device is folded.
- Occlusion region: does not divide areas, it occludes; it works as smaller frames inside the view's bounds. The FaceTime camera is an occlusion region, queried by passing the occlusion type to the reserved region method; it is active when the camera is active.
- System components that adapt to the fold: navigation containers such as navigation stacks, navigation split views and "tap views" (uncertain term in the automatic transcription); content containers such as List and Scroll View.
- Arrangements: layout containers positioned between the navigation ones and the content ones, which organize two views according to a set of rules. The inputs considered are the horizontal and vertical size class, the width-to-height ratio and the presence of active division regions; the outputs are whether the view appears and, if it appears, what its frame is. This function from inputs to outputs is the arrangement.
- SwiftUI: add an arrangement view inside the navigation stack, passing a primary view and a secondary one.
- UIKit: use UIArrangementViewController as the root view controller of the UINavigationController and configure the primary and secondary view controllers.
- Style: configured with the arrangement view style modifier; the default is split.
- Split arrangement: divides the bounds between the primary view and the secondary one; by default it splits horizontally when the view is wider than tall and vertically when it is taller than wide.
- Restricting axes: axes method of the split arrangement style. If the split cannot divide on the primary axis, the arrangement view shows only one view; in the example, with the view taller than wide and only horizontal division, only the player appears.
- UIKit for the same case: update arrangement method of the UIArrangementViewController with the UI split arrangement type configured with horizontal axis.
- Overlay arrangement: unlike split, which prefers side by side, it prefers to position the content with one view above or below the other; when the device is folded, it switches to preferring the primary and secondary side by side.
- Overlay Z-index in SwiftUI: overlay arrangement Z-index environment property, which changes as the device is folded and unfolded; in the example, used to switch between the collapsed and expanded version of the up next view.
- Overlay Z-index in UIKit: StateForViewPlacement method of the UIArrangementViewController and Z-index property of the returned state.

Examples cited:
- iPadOS window controls: an example of an area layouts already adapt to, of how reserved regions should be treated.
- A book with a photo spread across both pages: shows why content that crosses the fold loses readability.
- Photo album with a context menu: elements that work together move together and align around the fold.
- Alert in book pose (trailing side) and in resting-on-table pose (top region): the destination depends on how the device is used.
- Media controls in the bottom region with the device on the table: touchable controls gain a stable surface.
- Search field on iPhone and on iPhone Duo: prioritize the contextual.
- Reminders: the system split view adjusted to 50/50.
- Fitness design in a grid: outer margins preserved and greater spacing around the hinge.
- Grid with an even number of columns when there is a division region: use of inactive regions for high-level decisions.
- Podcasts app on iPad and on iPhone Duo: the transcript splits the layout in half; when hiding it on the folded iPhone Duo, the now playing view does not return to the center as on iPad and stays restricted to the left region defined by the fold, keeping the controls reachable and unobstructed; with the device rotated to portrait, there is no split and the transcript appears inline. It is also the example of a primary-and-detail relationship that calls for split.
- Harry's audio notes app, with player and up next: demonstrates split with a restricted axis, overlay with collapsed state and Z-index; the final answer is split, because the up next list details the playback state instead of being the player's background. In one passage the speech calls the app "Audio Node app" (uncertain term in the automatic transcript).
- Accessibility Reader: controls in the foreground and readable content in the background, a case of overlay.
- Sessions cited: Raise the Bar with iPhone Duo and Leverage Multiple Displays and Scenes on iPhone Duo.

Quotes:
"great design for iPhone Duo hinges on knowing when to adapt."
"Adaptive layouts help your app feel thoughtfully designed for every pose."

<!-- visual:tech-talks_111463 -->
### What the images show
Basis: 15 of 15 frame sheets viewed, all codes checked.
- The same app appears in a single panel with the device flattened and in two columns aligned to the physical halves when folded, with the hinge acting as the layout divider: Translate and Reminders (sheet 0006, q0049 to q0053) and the podcast app (sheet 0010, q0082 to q0084). The images give the before and after screen by screen, while the speech describes the behavior in general terms.
- Notes and the audio recorder already appear in two columns, with no equivalent flattened pair for the notes: Notes in a single frame, with the screen rendered over the curvature of the fold (sheet 0001, q0009), and the recorder with list and waveform in two frames that differ by the angle of the fold and by the time counter, not by the number of columns (sheet 0002, q0016 and q0017).
- Floating elements reposition to the hinge band instead of staying centered: the Music "New Folder" dialog is centered with the screen flattened (sheet 0005, q0040), goes through a blurred transition frame (q0041), and reappears over the fold with the device at two different angles (q0037, q0038). In the same interval, the video player's transport controls move off of the image (q0043) and become a compact group in the hinge band, below the video (q0044).
- Component anatomy recorded in the captures: Photos context menu as a vertical list with an icon to the left of each action and the destructive item in red at the end (sheet 0004, q0031); modal dialog with a text field and two side-by-side buttons over a blurred background (q0036); Reminders card grid in 2 columns by 3 rows, with a distinct color per category, which on folding separates into cards on one side and a list on the other (sheet 0006, q0052 and q0053).
- A grid that crosses the fold is recorded with no right-or-wrong label: the Photos "Countries" grid continues across both halves, with no apparent repositioning of the content (sheet 0004, q0032 to q0033), in the same interval where the title card reads "Be mindful of excessive movement." (q0030).
- The code is built line by line, with a temporary blue highlight and a green circular "NEW" badge: empty GeometryReader, then the division-regions query highlighted with the badge, then the same line already without the highlight, then a second line mapping the regions to frames (sheet 0007, q0060 to q0063). The loss of the highlight in the following frame is the visual signal that the line has become part of the settled code.
- Two variations of the same API call appear in sequence for different region types: the version with the parameter to include inactive regions (sheet 0008, q0064) and the occlusion version (q0067), accompanied by a minimalist screen diagram with a pill-shaped cutout in the top right corner representing the camera (q0069).
- The system containers diagram assembles in layers, one per frame: first "Navigation Containers" with three named blue icons, then "Content Containers" with two red icons, then "Layout Containers" in green inserted between the two previous bands, with a NEW badge (sheet 0009, q0073, q0078 and q0079). The color codes the container family, and each icon draws the component itself, with a bar at the base for the tab one and two columns for the split one.
- The abstract concept of arrangement is also built in three diagram steps: a blue inputs box with a single button, then three input buttons next to an empty green outputs box, then the arrow connecting inputs to outputs already filled with visibility and frames (sheet 0010, q0086 to q0088).
- Code and diagram split the screen into two columns, and the diagram changes even when the code does not change: the primary and secondary boxes appear side by side, then stacked with no visible change in the code, then the code gains the highlighted axis constraint, and finally the diagram shows only the primary box, with the UIKit equivalent highlighted (sheet 0011, q0094 to q0099).
- The style switch is shown over the same screenshot: split and then overlay in the "Queue" app with no apparent change in the capture (sheet 0012, q0101 and q0102), and then the z-index logic and the collapsed-and-expanded enum being assembled in the code while the screenshot alternates between just the player bar and the full list with the player integrated at the top (q0103 to q0106).
- Didactic labels sit outside the device's frame, next to the area they identify, annotating the same capture without changing the interface: "Foreground" and "Background" over the Notes screen, with the player bar highlighted by a rectangle (sheet 0013, q0114 and q0115), and "Player" and "Transcript" over the podcast screen (q0116).
- Title cards in white text on black work as an index parallel to the speech, with hierarchy by size and weight: the two adaptation patterns (sheet 0003, q0022), "Scope" (q0027), "Properties" (sheet 0006, q0048), "Follow your existing app patterns." (sheet 0013, q0110) and "Next steps" (sheet 0014, q0125).
- The final list of recommendations is built item by item, keeping the previous ones unchanged (sheet 0014, q0126; sheet 0015, q0127 and q0128), and the API name inside it is set apart from the body text by a monospaced font with a highlighted background.
- Abstract illustrations over a fine grid represent a reserved region with no real interface: a rectangle with a rounded square at the center (sheet 0003, q0026) and the rectangle with the camera cutout already cited (sheet 0008, q0069). In these two sheets the rest of the frames are title card, code block and presenter shot, with no real app capture alongside.
- The only product still shows the device closed like a book, seen from a corner, light metal body, two stacked lenses at the outer edge, and the time 9:41 partially visible at the fold (sheet 0001, q0007).
Visual proportion: most of the frames are screen, that is, app capture, code block, diagram or title card, and the minority is presenter shots in the studio; there are entire sheets with no presenter on screen (sheets 0006 and 0011), and the human shots are denser at the opening and the close (sheets 0001, 0002, 0014 and 0015), without disappearing in the middle sheets.
Recorded divergences or limits: a black frame carries barely legible ghost text, read with uncertainty by the notes (sheet 0003, q0025); a UIKit code block appears with overlapping, blurred text, hard to read in full (sheet 0012, q0100); two frames show a gray rectangle with no label or content, flagged in the notes as a possible transition or a placeholder that did not load (sheet 0014, q0122 and q0123); and between two frames of sheet 0011 the diagram changes from side by side to stacked with no visible change in the code.
<!-- /visual:tech-talks_111463 -->

## Meet Apple Watch Series 7 (id: tech-talks_10884, 15.2 min)

Basis: transcript and 10 of 10 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/tech-talks/10884/.

Central thesis: the Apple Watch Series 7 gained larger active content areas and a display with a subtle wraparound effect at the edges, and because of that apps should become larger, clearer and quicker to understand at a glance (larger, clearer, more glanceable).

The design process Apple describes, presented by three designers (Deena Khattab, Jennifer Patton and Matthew Koonce): first map the hardware differences (two new case sizes, display curvature, thinner bezel, larger corner radius); from these differences, derive three design principles; then show, with examples of system apps and SwiftUI code snippets, how to apply each principle to margins, typography, color, buttons and keyboard.

Principles stated and why: enlarge the UI components to take advantage of the larger content area, which improves usability; revise typography and color to create a clearer information hierarchy; revise navigation and wayfinding to reinforce the sense of place at a quick glance, since the Apple Watch was always designed for light, glanceable experiences.

Concrete interface-building techniques, with exact numbers when spoken:
Layout: two case sizes, 41 mm and 45 mm; active content area of 176 by 215 points on the 41 mm and 198 by 242 points on the 45 mm; because of the greater corner curvature, content needs to inset inward; taller status bars, accompanied by a larger scroll clearance margin at the bottom of the screen; generous layout margins on the Series 7. In the speech, the presenter describes using the .scenePadding modifier in SwiftUI to apply the system's default margin, recommended only for text content that would be distorted or cut off at the edges (such as a stock's current price and the text "Nasdaq" in the Stocks app example); a chart from the same layout was left without this modifier, because it can go all the way to the edge of the screen.
Hierarchy and navigation: large titles arrived on watchOS this year; in table views with scroll, the large title transitions into the status bar during scroll; both the root level and subviews receive the large title; in fixed views that do not scroll, the title can be brought inside the content area (Timer case) or removed when unnecessary, decoupling the title from Back-button navigation; in other fixed views, the status bar remains the best place for the title (World Clock detail case). In SwiftUI, by default on watchOS 8 all navigation titles are large and tinted by the app's accent color; the .navigationBarTitleDisplayMode modifier turns off the large title on a specific view, and subsequent views in the hierarchy inherit that mode.
Color: color should help with wayfinding, with information hierarchy, and signal the app's personality. The accent color is configured in the asset catalog and automatically colors the navigation bars; in the Mail example, listItemTint was set to the app's accent color at 30 percent opacity.
Buttons: a system of rounded rectangular buttons for views with scroll and pinned buttons (fixed at the bottom) for fixed views; on the Series 7 the secondary button's color scheme was simplified and side-by-side buttons went from a divided lozenge shape to side-by-side pill shapes; the pinned button's shape was designed from the curvature of the display itself, to harmonize with the hardware; button height stays the same on devices before the Series 7, so no layout change is needed to adopt them. In SwiftUI, buttons use a bordered button style with automatic border shape by default: capsule shape outside a scroll view and rounded rectangle inside it; there is also the bordered prominent style, which applies the accent color to the button (used in Alarms).
Typography: the Series 7 uses the same default type sizes as the Series 6, large for 40 mm and 41 mm, extra large for 44 mm and 45 mm, gaining more characters per line than previous devices; three larger type sizes were added for accessibility, called AX1, AX2 and AX3; a Smart Type Suggestions feature in setup identifies whether the person already uses large type on iPhone and suggests an equivalent size on the watch.
Symbols and writing: it is recommended to complement text labels with SF Symbols; in list-navigation apps, use outlined symbols in the app's accent color, aligning symbol style and color across platforms for consistency and accessibility (examples: Mail, Phone).
Interaction and keyboard: because of the larger screen area, a full keyboard was added, designed with no borders around the keys, to encourage swipe to type and avoid the feeling that it is easy to mistap; the delete key was taken out of the keyboard and moved to the text field, freeing up space; the keyboard allows customizing the autofill type for cases like passwords and two-factor authentication; the accessories to the left and right of text fields can be customized with SF Symbols, with the app's accent color recommended to reinforce that they are tappable.

Examples cited: Stocks teaches the use of .scenePadding for text near the edge; Settings illustrates large titles at the root level and in subviews; Timer shows the title brought into the content area; World Clock detail shows a case where the title stays in the status bar; Mindfulness teaches the use of System Teal as the app's key color with System Gray pulled back; Mail shows a blue background reinforcing app identity and listItemTint at 30 percent; Tips uses bright yellow platters to differentiate itself from other carousel-navigation apps, like Workout, and reinforce continuity of experience across platforms; Alarms list shows a primary scrolling button and the bordered prominent style; UIPickerView shows buttons side by side in pill shape.

Quotes: "apps for Apple Watch Series 7 should be larger, clearer, and more glanceable" and "deriving the shape of the button from the shape of the display itself".

<!-- visual:tech-talks_10884 -->
### What the images show
Basis: 10 of 10 frame sheets viewed, all codes checked.
- The measurements in points appear written next to the hardware renders themselves, not only spoken: the pair of black boxes carries the 41 mm dimension (sheet 0001, q0004) and the next render, with several overlapping colored boxes, carries the 41 mm and 45 mm dimensions at the same time (q0005).
- An annotation points out the layout defect directly on the screen: the label "Too close to edge" with a vertical line pointing to the left edge, next to the stock price, between an unlabeled frame before and another unlabeled frame after (sheet 0003, q0019 to q0021).
- The fix is shown as a cause-and-effect relationship: a code panel next to the rendered watch, with the margin modifier line inserted and highlighted first under the price block, then after the footer text, and an orange arrow connecting the code snippet to the corresponding element on the screen (sheet 0003, q0022 to q0026). The watch switches sides between the frames, and the chart in the same layout also appears highlighted in the code, consistent with the different treatment the speech gives it.
- The pair of title states is shown side by side with the code: the comment changes from large titles to inline titles, the display mode modifier line is highlighted, and the watch screen goes from a large orange title occupying the top to a small title aligned to the left next to the back arrow (sheet 0004, q0034 to q0036).
- App identity color is demonstrated by accumulating watches in the scene, one at a time: first Mindfulness in aqua green, then Mail in blue next to it, then Tips with a yellow card (sheet 0005, q0038 to q0041), leaving the difference visible through direct comparison rather than description.
- The authoring tool comes into frame: a laptop screen shows the accent color editor and then the project's file browser, before the scene returns to the code panel with the list item tint line highlighted by a box (sheet 0005, q0042 to q0045).
- The button system is presented as a two-column diagram with labeled columns, separating buttons in scrolling views from buttons in fixed views, with color coding by hierarchy, green for primary action, gray for secondary and dismiss, blue for toolbar; the same diagram reappears with the title changed from current buttons to Series 7 buttons, keeping the same structure and colors (sheet 0006, q0046 to q0050).
- The buttons fixed at the bottom appear in pill shape side by side, a gray cancel button and a green start button, and the scene zooms in on the bottom of the screen, where the numeric wheels remain partially visible above the buttons (sheet 0006, q0051 to q0054).
- The button style modifiers are highlighted one by one alongside the render: automatic shape with bordered style on the cancel and start buttons, and bordered prominent style on the orange add alarm button, each case followed by a close-up crop of the screen on the button itself (sheet 0007, q0059 to q0063). The button color follows its function, with red for stop, orange for add and green for start (sheet 0007).
- The difference in text space between case sizes is shown by two watches with the same email message and size labels annotated under each one, followed by a close-up on the larger one with the message body open (sheet 0008, q0065 and q0066).
- The type size adjustment appears on the iPhone screen, with a slider between a small "A" and a large "A" and a continue button, and in the next frame the watch appears alongside it already showing the text at the chosen size (sheet 0008, q0068 and q0069).
- Cross-platform consistency is composed literally: iPad, iPhone and watch side by side displaying the same mailbox screen, with the same folder, star and flag icons across all three widths (sheet 0008, q0072).
- The keyboard is drawn without outlines around the keys, and the delete icon sits inside the text field rather than between the keys; a key icon in the corner of the field signals a password or authentication context (sheet 0009, q0074 to q0076).
- A yellow highlight box surrounds only the word in the search field, drawing attention to a wording detail without altering the interface (sheet 0009, q0079), and the closing card appears first with two features listed (q0081) and then with three, plus a thin separator above two reference links (sheet 0010, q0082).
- The list of design principles functions as a chapter marker and reappears throughout the video: first in full, over two dimmed watches (sheet 0001, q0008), then with the current section's item in bold and the rest dimmed (sheet 0008, q0064; sheet 0009, q0073), a structural cue that the speech does not verbalize at every cut.
Visual proportion: the notes do not record any presenter frame in the scene; the 82 frames are watch screens, hardware renders, diagrams, code panels and text cards, with the code panel next to the render appearing in four distinct sheets.
Recorded divergences or limits: two Mindfulness frames appear identical, with no perceptible difference (sheet 0005, q0038 and q0039); the three close-up frames on the cancel and start buttons are also indistinguishable at this resolution, and the notes record that the subtle difference described in the speech between simple pill and faceted shape is not visible in the still images (sheet 0006, q0052 to q0054); and two frames of the mailbox screen show no perceptible difference (sheet 0008, q0070 and q0071).
<!-- /visual:tech-talks_10884 -->

## Designing for Apple Watch Series 4 (id: tech-talks_802, 9.4 min)

Basis: transcript and 7 of 7 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/tech-talks/802/.

Central thesis: the Apple Watch Series 4 brings larger displays with rounded corners and thinner borders, and Apple advises updating layouts to use system margins and safe areas instead of fixed values, so the app can benefit from the extra space without clipping content.

The design process Apple describes: comparing the new case and display dimensions with the previous ones, placing the new sizes (40 mm and 44 mm) within the existing size spectrum, recommending the use of the Design Resources to create accurate mockups by watch size, and then explaining how WatchKit automatically adapts the status bar, title, margins and scroll clear areas to the new screen format.

Principles stated and why: deliver the same information and the same actions regardless of screen size, because the four case sizes coexist; design the layout targeting the dimensions in the middle of the spectrum (40 and 42 mm) and ensure it scales down (38 mm) and up (44 mm); extend graphic elements and button backgrounds almost edge to edge, but keep text aligned to the margin, to follow the curvature of the new corners without clipping text content.

Concrete interface-building techniques, with exact numbers when spoken:
Case sizes: new 40 mm and 44 mm, versus the previous 38 mm and 42 mm. Display dimensions: previous 38 mm, 272 by 340 pixels; previous 42 mm, 312 by 390 pixels; new 40 mm, 324 by 394 pixels; new 44 mm, 368 by 448 pixels. The new 40 mm display is 12 pixels wider and 4 pixels taller than the display of the old 42 mm.
Layout: the status bar and title area are indented, creating left and right margins that extend vertically through the content, called System Minimum Layout Margins; graphic elements and button backgrounds should extend beyond these margins, almost edge to edge, down to a standard margin of 1 pixel on each side; text should align to the left margin, starting from the left edge of the text in the status bar. In scroll views there are scroll clear areas at the top and bottom of the content, which push text and buttons into the visible area at the end of a scroll; for single-screen views that should not scroll, Xcode offers the Fixed to screen edges attribute in the attribute inspector.
Compatibility: an app that is not recompiled runs on the Series 4 at the 38 mm dimensions (on a 40 mm watch) or 42 mm (on a 44 mm watch), centered on the screen; recompiling for watchOS 5, the app comes to occupy the full width and height of the new display, provided the WatchKit elements are implemented relative to the container, and not at fixed widths.
Haptics: the Series 4 Digital Crown introduces new haptics, with detents (clicks) produced by default on every rotation, delivering tactile feedback in common interactions like scrolling a list or selecting an item in a picker; it is recommended to evaluate whether UI events tied to Digital Crown rotation remain aligned with this new tactile feedback.
Typography: watchOS 5 expanded the Dynamic Type Library with four larger sizes, Large Title and Titles 1, 2 and 3; the default content category varies by case size, Small for 38 mm, Large for 40 mm and 42 mm, XLarge for 44 mm.
Visual assets: it is recommended to produce graphics as PDFs with a scale factor of 2, placed in the Universal 2x box of the asset catalog, with the Auto Scaling property set to Automatic; this scales the graphics 9 percent down on 38 mm displays and 10 percent up on 44 mm displays; two new app icon sizes were introduced to cover the 44 mm interface (short look notification and Home screen icon).

Examples cited: no third-party app is cited; the video uses only generic system elements (status bar, title area, scroll views, SpriteKit/SceneKit) as an example of adaptation to the new display.

Quotes: "Series 4 watches have new displays with larger dimensions" and "the border around it is thinner, bringing more attention to interactive elements".

<!-- visual:tech-talks_802 -->
### What the images show
Basis: 7 of 7 frame sheets viewed, all codes checked.
- The comparison of screen sizes is done through rectangles dimensioned in pixels, alternating between abstract and applied representation: watch pairs with a plain green screen with no dimension, then rectangles with the resolutions of the two older sizes, then the new ones, then real app screens, and finally the four sizes side by side under the new generation's label (sheet 0001, q0004 to q0009).
- The physical watch mockup, with case and band, serves as a recurring frame, and the content area appears filled in solid green as a placeholder whenever the point is the available space and not the content (sheet 0001, q0004 and q0005; sheet 0004, q0030 and q0031).
- The watchOS screen structure is progressively assembled in colored zones over a sample layout: empty black screen, then the blue title bar with title and clock, then the gray margin strip, then the purple scroll clearance area strip at the base, then the filler text block with a button below, and finally a numeric stepper with a blue button, already without the color strips (sheet 0003, q0019 to q0027). The colors per zone are a screen-only resource, the speech names the zones without describing them this way.
- The configuration tool enters the frame at the exact point of the option: the Xcode attributes inspector with the attribute for pinning the view to the screen edges checked, next to the watch with the same stepper and button from the previous sheet (sheet 0004, q0028), and then the same frame with the transition card overlaid (q0029).
- An inner dashed outline marks margin and inset within the screen area, and wireframes with an "X" image placeholder plus filler text represent the structure before the final content (sheet 0004, q0030 to q0033).
- The typographic scale appears as a complete grid table, crossing content size category in the columns with text style in the rows and the value in points in each cell, built in two stages: first the smaller styles, then the four larger styles added above (sheet 0005, q0042 to q0044). The speech cites the new styles, the image delivers all the numeric values.
- The system text size adjustment screen, with a slider between small and large "Aa" and a sample sentence, appears overlaid on the table already blurred in the background, linking the specification to the control the person uses (sheet 0005, q0045).
- Apple's own supporting material is shown on screen: the guidelines page on the Mac with three columns per watch size range (sheet 0002, q0013) and a template file open in a design app, with an interface elements panel by size, a component list and a palette with a gray cancel button plus the same confirm button repeated in seven colors, plus the properties panel with position, transform, borders, fills and shadows (q0014 and q0015).
- The asset production flow is shown inside Xcode's Asset Catalog, with the project icon in the universal boxes and the attributes panel showing any screen width and automatic scale, first in context and then in close-up (sheet 0006, q0049 to q0052).
- The icon specification carries exact measurements in pixels and points for two contexts, notification and home screen, illustrated by concentric circles (sheet 0006, q0053), and the same specification reappears overlaid on a guidelines page in the same sheet.
- Isolated white text cards mark the presentation structure between the visual blocks, including the layout title (sheet 0002), the app update one (sheet 0004), the haptic feedback and scrollable views ones (sheet 0005) and the graphic production one, plus the instruction to prepare the graphic at 2x scale and save as PDF (sheet 0006).
- The closing shows the Apple Developer site resources page, with an embedded video and a documentation list, before the final black slide with the logo and the 2018 copyright notice (sheet 0007, q0055 to q0057).
Visual proportion: the notes do not record any presenter-on-camera frame; the whole video is composed of watch mockups, dimensioned rectangles, Xcode and system app captures, tables, wireframes and text cards.
Recorded divergences or limits: in the resolution enumeration on sheet 0001 the notes record the pixel dimension of the 38, 42 and 40 mm sizes, but the 44 mm one appears labeled with no number read in the frame; and between two frames of the design editor the only recorded difference is the position of the cursor or the selection (sheet 0002, q0014 and q0015).
<!-- /visual:tech-talks_802 -->

## Designing for Subscription Success (id: tech-talks_803, 9.2 min)

Basis: transcript and 6 of 6 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/tech-talks/803/.

Central thesis: a good subscription experience needs to be effortless, transparent and engaging (effortless, transparent, engaging), because the common perception is that subscribing is complicated, confusing and time-consuming.

The design process Apple describes: work on each of the three principles separately. To be effortless, make the offer visible without looking like a disposable ad and always make the option to subscribe available in Settings or Account, besides removing friction by reducing the number of steps and postponing personalization requests until after sign-up. To be transparent, put together a single, glanceable screen with value proposition, call to action, login, restore purchase, terms and multiple price tiers, following the App Review guidelines. To be engaging, let the person try the app before deciding, through a free trial, unlocking most of the app with one premium feature reserved, or content sampling.

Principles stated and why: be visible, because people should not have to search for how to subscribe; do not present the subscription as a pop-up or notification, because these formats are made to be dismissed and the subscription should not be; remove friction, because each extra step reduces the conversion rate, according to data from the video itself; be glanceable, because most people decide to subscribe from their phone, in a few seconds; offer multiple tiers, because different people want to commit for different periods (day, week, month, two years); let people try before buying, by the same logic as trying on clothes, visiting an open house or test-driving a car before deciding.

Concrete techniques, with exact numbers when stated: data from one month of use of the three largest entertainment streaming apps in the United States (names removed from the speech) shows that a subscription flow with three clicks had a conversion rate of 61 percent; with four clicks, conversion dropped to 48 percent; with nine clicks, conversion dropped to 7 percent.

Examples cited: New York Times, which keeps a persistent but discreet subscribe button on every article, and offers 10 free articles a month for non-subscribers, letting the person choose what to read as a sample; HER, a dating app, which offers the subscription at the moment the person tries to use the rewind feature (undoing an accidental "swipe"), with a light animation showing the offer values right when there is manifest interest; MLB At Bat, cited as an example of a glanceable screen that brings together value proposition, call to action, login, restore purchase and clear terms in a single view; Sleep Cycle, which unlocks most of the features for free and reserves the Trends feature, shown with a blur effect, as a sample of what the subscriber would go on to see.

Quotes: "make your subscription effortless, transparent, and engaging" and "less clicks, less friction, will equal more conversion and more subscribers".

<!-- visual:tech-talks_803 -->
### What the images show
Basis: 6 of 6 frame sheets viewed, all codes checked.
- The list of the three principles works as a progress track throughout the video, with the item in focus in white and bold and the others dimmed in gray, reappearing at every section turn and ending with all three in white, with no hierarchy, to signal the close (sheet 0001, q0005 and q0006; sheet 0003, q0027; sheet 0004, no frame number in the notes; sheet 0006, q0052). The speech does not verbalize this marker.
- A large, isolated emoji illustrates an abstract concept, always between a text slide and the next app capture: the face with the hand over a purple background for the frustration of subscribing, next to the reaction sentence (sheet 0001, q0004), a dress, a house and a car in two columns for the analogies of trying before deciding (sheet 0005, q0039) and a group of people to represent the audience (sheet 0006, q0051).
- The news app example shows the blue subscribe button fixed at the top of every article screen, first on one screen and then on three side by side (sheet 0001, q0008 and q0009), and the same three screens reappear with the two negations overlaid, separating subscription from ad and from notification, before the text stands alone in frame (sheet 0002, no frame number in the notes).
- The anatomy of the offer modal appears complete in a real capture: a card overlaid on the content with a darkened background, a profile photo relevant to the context, dot page indicators, three price options with the longest one highlighted in solid color and a discount badge, and the restore purchase link in discreet text below (sheet 0002, q0014).
- The same card reappears with the title and photo swapped, keeping identical structure, hierarchy and positions, which shows the modal as a reusable template and not as a single screen (sheet 0002, q0014 to q0015).
- The permanent subscription alternative is shown inside the app's settings screen, with the subscribe item listed among account options and a restore subscription item close by, in two captures side by side that close one sheet and open the next (sheet 0002, no frame number in the notes; sheet 0003, q0019 and q0020).
- The conversion data turns into a double bar chart with a numeric label above each bar and a color legend per metric, clicks required in light blue against conversion rate in yellow, reused across three framings with no change in data and then darkened to serve as the background for the conclusion sentence (sheet 0003, q0022 to q0025).
- The offer screen of a baseball app is annotated with arrow callouts, one per frame, pointing first at restore purchase, then at the multiple price tiers, then at the terms and conditions (sheet 0004, q0031 to q0033), a technique of direct annotation over a real capture.
- Next, the complete checklist of eight mandatory elements of a subscription screen appears in a column next to the same capture, turning the individual callouts into a closed list (sheet 0004, q0034).
- The capture itself shows the anatomy of the single offer screen: title, value proposition in one sentence, subscription features link, two price buttons, subscriber login button, legal cancellation text with terms links and, in the footer, the restore purchase line (sheet 0004, q0029 and q0030).
- The stacked button hierarchy appears on the onboarding screen of a streaming service: primary action in solid blue at the top, sign in and restore purchase below as secondary actions, over a background of show covers (sheet 0005, q0042).
- The locked premium feature is shown as an image, not as a description: the trends chart of a sleep app appears blurred behind the subscriber-exclusive content notice, with the note in the footer (sheet 0005, q0044 and q0045).
- The free sample mechanism appears as a notice component at the top of the article screen, informing how many free articles remain for the month, in a piece with an opening photo (sheet 0006, q0046).
- Dimming and focus guide the reading between slide and capture: the settings screens stay blurred behind the text about removing friction (sheet 0003, q0021), and the list plus the capture dim before the simplification sentence overlays the screen with an app grid icon (sheet 0004, q0035 and q0036).
- Short greetings in the corner mark the change of addressee for each section, directed at the general audience, at subscribers and at lawyers (sheets 0001, 0003, 0004 and 0005).
Visual proportion: the notes do not record any presenter-on-camera frame; every frame is a text slide, emoji, chart or real app capture, with the opening on a title slide with presenter credit and the closing on a black card with the Apple logo and the copyright notice.
Recorded divergences or limits: on sheet 0001 the notes identify the news app with a caveat, as New York Times style, and only on sheet 0006 do they record the name without a caveat; the three bar chart frames differ only by camera framing, with no change in data (sheet 0003, q0022 to q0024); and the two final trend chart frames have practically identical composition and camera (sheet 0005, q0044 and q0045).
<!-- /visual:tech-talks_803 -->

## Designing for iPhone X (id: tech-talks_801, 12.8 min)

Basis: transcript and 9 of 9 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/tech-talks/801/.

Central thesis: the iPhone X's Super Retina display, with rounded corners, sensor housing and Home indicator, requires apps to use the Safe Area layout guide and UIKit and Auto Layout layout margins to fill the entire screen without cutting off or hiding critical controls and information.

The design process Apple describes: first review the scale and dimensions of the new display; then show how standard UIKit components (navigation bars, table views, tab bars, toolbars) adapt automatically; then present the Safe Area layout guide as new in iOS 11 and explain its difference from the iPhone 8; finally, guide on the manual adjustments needed in apps with custom controls, in landscape orientation, in the status bar and in the Home indicator's behavior.

Principles stated and why: the app or game should always fill the display it runs on, because black bars at the top or bottom make the app look small and inconsistent with the other apps on the iPhone X; any element too close to the edges or corners of the viewport can be cut off by the rounded corners or covered by the sensor housing, so critical controls and information need to be inset; in landscape, centered controls and information work better, because asymmetric layouts that change position depending on the device's rotation hurt muscle memory and create inconsistency; the Home indicator must always be clearly visible, and that's why iOS dynamically adjusts its appearance (dark over light backgrounds, light over dark backgrounds) and it should not receive visual adornments like brackets or bezels that draw too much attention to it; features like edge protection and indicator auto-hide lead to a less consistent experience and should be used only when absolutely necessary.

Concrete interface-building techniques, with exact numbers when stated:
Scale and assets: the iPhone X display has a 3x image scale factor; the recommendation is to use PDFs, since they are resolution-independent and reduce app size, and when rasterized images are needed, to include the 2x and 3x resolutions in the asset catalog.
Dimensions: the display measures 375 points wide by 812 points tall, equivalent to 1125 by 2436 pixels on a 3x display; the 375 points of width are equal to the width of the 4.7 inch displays of the iPhone 6, 7 and 8, so there is no difference in the amount of information in the narrower dimension; the 812 points of height are 145 points more than a 4.7 inch display, giving about 20 percent more room for content.
Safe Area and layout margins: on the iPhone 8, with no bars visible, the Safe Area is the same size as the viewport; with the status bar visible, the top edge of the Safe Area moves down to accommodate it, and it is inset further to accommodate the navigation bar and toolbar or tab bar. On the iPhone X, the Safe Area already comes inset from the top and bottom even with no bar visible in portrait, to protect content from the sensor housing, the rounded corners and the Home indicator; in landscape, it is inset from the sides and from the Home indicator for the same reason. Layout margins, a separate guide inside the Safe Area, keep content margins consistent across apps and help align content to controls like navigation bar buttons. UIView exposes the Safe Area insets and layout margin values as properties, even for those who don't use Auto Layout. iPhone 6, 7, 8 and X all belong to the same compact width size class (compact width), so an app's layout should be consistent across these devices.
Aspect ratio: backgrounds designed for the iPhone 8's 16:9 aspect ratio appear cropped on the sides on the iPhone X if scaled to fill, or with letterbox if scaled to fit; the opposite happens with backgrounds designed for iPhone X displayed on iPhone 8, cropped at the top and bottom or with pillarbox; the recommendation is to compose images so that critical visual information remains visible at any aspect ratio.
Status bar and Home indicator: the status bar is taller on the iPhone X and no longer changes height during background tasks, such as a call or location tracking, to keep a more consistent experience; it's recommended to leave negative space around the Home indicator, keeping all non-scrollable content inside the Safe Area; edge protection, when enabled on the bottom edge, requires two swipes to exit the app, the first raises the indicator and enables the control, the second actually exits; auto-hide makes the indicator fade if the screen isn't touched for a few seconds and reappear on touch, recommended only for passive experiences with infrequent touch; vertically scrollable views, such as tables and collection views, should extend to the bottom of the display, and not be restricted by the Safe Area.

Examples cited: no third-party app is cited; the examples are the standard UIKit components themselves (navigation bars, table views, tab bars, toolbars) and full-screen scenes via SpriteKit or SceneKit, used to illustrate automatic and manual adaptation to the new display.

Quotes: "iPhone X's super retina display gives you more space to display content" and "Because edge protection leads to an inconsistent user experience".

<!-- visual:tech-talks_801 -->
### What the images show
Basis: 9 of 9 frame sheets viewed, all codes checked.
- The image scale factor becomes a diagram of three circles of increasing size, with labels below and association to each device, first next to the title and then isolated in its own larger composition (sheet 0001, q0003 and q0004). The speech only mentions the scale verbally.
- The measurements appear as graphic annotation over the outlines, with lines, arrows and numbers in light blue, and the same pair of comparison blocks switches the unit between frames, first in pixels of width and height, then in points of equal width on both devices (sheet 0001, q0008 to q0009).
- The extra height is isolated visually instead of just being added: the new device's block appears with the additional strip highlighted in green at the top, separated from the blue part shared with the smaller display, with the three measurements annotated (sheet 0002, q0010).
- The Home indicator gains emphasis through overlay, with a yellow bar appearing at the bottom of an outline that in the previous frames was empty (sheet 0002, q0012 to q0013).
- Solid green blocks labeled as safe area work as a reused annotation layer across different contexts: filling almost the whole screen on a device with no notch, inset below the navigation bar in a real screenshot of an email app, and inset from the top and bottom on the new device even with no bar visible (sheet 0003, q0024 to q0027).
- Screenshots of the same app are stacked with transparency and aligned to compare sizes: the favorites list in three layers, then the same overlay with device outlines zoomed in further, and the five-icon tab bar compared across four aligned layers (sheet 0002, q0017 and q0018; sheet 0003, q0020).
- Two color layers separate bar and content in the landscape form: the red navigation bar goes from inset to extended edge to edge between two frames, while the content lines highlighted in green remain inset, making visible that one rule applies to the bar and another to the cell (sheet 0004, q0029 to q0030).
- A light blue strip marks the side inset on the left edge of the two compared devices, and the size class label identifies that both belong to the same compact width (sheet 0004, q0033 to q0036).
- The pair of wrong and right marks, red circle with "X" and green circle with "check", appears at least six times in the same colored circle with white icon format: in the rotation from portrait to landscape and in the comparison between the two displays (sheet 0005, q0037 and q0038), in the icons stuck to the four corners marked as wrong against the same inset icons marked as right (sheet 0005, q0045; sheet 0006, q0046 and q0047), in the scroll bar and the weather screen stuck to the edges marked as wrong (sheet 0007, q0056 and q0057) and in the button centered inside the safe area against the thin bar stuck to the bottom edge (sheet 0007, q0061 and q0062).
- The cropping and the letterboxing of a background image are demonstrated with two blue blocks illustrating a tree, with an arrow indicating the direction of adaptation between the two devices and a white outline marking the area that would be cropped; in the next frame the arrow reverses and the crop moves to the other block, showing both directions of the same problem (sheet 0005, q0039 to q0043).
- Three states labeled with the same behavior name show the Home indicator as a thin white line, then with a blue circle over it suggesting the touch, then back to the plain line, illustrating a gesture that the speech describes only in running text (sheet 0008, q0065 to q0067).
- The full-screen case appears as a pair: the video occupying the whole screen with the subtle indicator at the bottom and, in the next frame, the same video with a title bar with date and playback controls overlaid (sheet 0008, q0070 to q0071).
- The anatomy of the standard lists is recorded and repeated across sizes: favorites with circular avatar, bold name, contact type in gray, info button on the right and tab bar at the bottom (sheet 0002, q0016 to q0018); inbox with title, edit button, search bar, bold sender, preview and date aligned to the right, kept identical across the three compared devices (sheet 0006, q0051, q0053 and q0054).
- Apple's reference material appears on screen at the start and the end: the bar glyphs documentation page, the design resources page with an example panel showing title, text field, switch and action buttons (sheet 0001, q0005 to q0007), and the final card with the guidelines address (sheet 0009, q0073).
Visual proportion: the notes record no presenter frame on screen; the 73 frames are title cards, annotated diagrams, device outlines and screenshots of system apps, with a predominance of side-by-side comparisons and colored annotation layers over the interface.
Recorded divergences or limits: one frame shows an overlapping context menu with illegible text due to transparency (sheet 0003, q0021); the notes on sheet 0006 record that the speech comments on the taller status bar covering content positioned by a fixed value, but the images in that range don't show this case directly; and several pairs of frames repeat with no perceptible change (sheet 0001, q0001 and q0002, and q0006 and q0007; sheet 0002, q0011 and q0012; sheet 0003, q0024 and q0025; sheet 0007, q0058 and q0059; sheet 0008, q0068 and q0069).
<!-- /visual:tech-talks_801 -->

## What this group reveals about the Apple way

- With each new hardware geometry (the rounded corners of the Series 4, the wraparound of the Series 7, the sensor housing and corners of the iPhone X), Apple starts from exact physical measurements in points and pixels and only then derives UI principles from them, instead of starting from an abstract aesthetic idea (ids: 801, 802, 10884).
- Mechanisms such as Safe Area, System Minimum Layout Margins and .scenePadding play the same role on different platforms: a system layer that automatically insets content from edges and corners, taking the manual calculation of fixed values off the designer (ids: 801, 802, 10884).
- Compatibility is treated as a design requirement, not just an engineering one: apps that are not recompiled keep working, centered within the old dimensions, and only gain the extra space when recompiled with elements relative to the container instead of fixed widths (ids: 802, 801).
- Color and typography appear explicitly as tools of identity and hierarchy, not just style: the accent color reinforces the function of each app (Mail, Tips, Mindfulness), and extra type sizes arrive first for accessibility (AX1 to AX3) before becoming a general design resource (id: 10884).
- Even in business UX decisions, such as the subscription one, the design prescription is anchored in quantitative behavior data (clicks versus conversion), in the same logic of "less friction, better result" used in layout decisions (id: 803).
- The official design tools (Figma, Sketch, Design Resources) are positioned as the link between designer and engineer, with automatic file updates when Apple changes the kits, to keep the mockup faithful to the final product (id: 111427).

## No transcript

- tech-talks_111461: now has its own card in this file, with the basis indicated on the card.
- tech-talks_111466: now has its own card in this file, with the basis indicated on the card.
- tech-talks_111462: now has its own card in this file, with the basis indicated on the card.
- tech-talks_111463: now has its own card in this file, with the basis indicated on the card.

These four files have only title, source, duration and description; none has a body of spoken transcript, so nothing was summarized from them.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111427.md, 13 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111461.md, 4 lines read, to the end: yes (file has only a header, no transcript).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111466.md, 4 lines read, to the end: yes (file has only a header, no transcript).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111462.md, 4 lines read, to the end: yes (file has only a header, no transcript).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111463.md, 4 lines read, to the end: yes (file has only a header, no transcript).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_10884.md, 11 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_802.md, 73 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_803.md, 7 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_801.md, 16 lines read, to the end: yes.
