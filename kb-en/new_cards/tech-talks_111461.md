## Prepare your app for iPhone Duo (id: tech-talks_111461, 10.2 min)

Basis: transcript (frames not viewed yet). Local automatic transcript made with Whisper, it is not Apple's official one; proper names and terms may carry hearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111461/.

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
