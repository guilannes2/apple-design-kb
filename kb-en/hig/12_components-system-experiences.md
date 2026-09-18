# Components / System experiences

## App Shortcuts (slug: app-shortcuts)

### What it governs
Governs how an app exposes its main functions or content to be triggered from outside it, via Siri, Spotlight, Shortcuts, Action Button or a press of the Apple Pencil, using App Intents.

### Why
Apple starts from the premise that the most valuable interaction is the one that skips opening the app. An App Shortcut is available from installation, even before first use, because it represents an action the app already knows how to do, not a learned personalization. At the same time, after the person uses the app, shortcuts can reflect their choices (like recent contacts in FaceTime), which shows the intent to bring automation closer to the real context of use. The limitation to short activation phrases and to few optional parameters comes from the logic of voice interaction: something that sounds complicated when said out loud tends to be hard to remember or pronounce correctly.

### Do and avoid
- Prefer adopting app schemas for common types of functionality, leaving App Shortcuts for exclusive features or content not covered by schemas.
- Offer App Shortcuts for the app's most common and important tasks, prioritizing the ones the person completes without leaving the current context.
- Allow a single optional parameter per shortcut when it makes sense, with predictable and familiar values, since the person will not have the list of options in view.
- Ask for clarification when an optional piece of information is missing, suggesting a default (for example, the most recently used type) and presenting short alternatives.
- Keep voice interactions simple; if the phrase sounds complicated when spoken, it is probably hard to remember or pronounce.
- Avoid embedding too much information in a single parameter (the example given, "Start sleep meditation with nature sounds", is cited as a problematic double parameter); ask for additional information in a following step if it is really necessary.
- Make App Shortcuts discoverable within the app itself, with occasional hints when the person performs common actions.
- Respond to engagement with the shortcut using dialogue spoken by Siri and visuals such as snippets and Live Activities.
- Use snippets to display static information or dialogue options; use Live Activities for continuous access to information that changes over a period, such as timers and countdowns.
- Provide enough detail for interaction on audio-only devices (AirPods, HomePod), including all critical information in the full dialogue text.
- Provide brief, memorable activation phrases, and natural variants; the app name is required in the phrase, but the rest can be creative.
- Use title case when referring to App Shortcuts or the Shortcuts app (and keep "Shortcuts" plural); use lowercase when referring to individual shortcuts (not App Shortcuts nor the Shortcuts app).

### Exact specifications
- Each app can include up to 10 App Shortcuts.

### Platform differences
- iOS, iPadOS: App Shortcuts can appear in the Top Hit area of Spotlight when searching for the app, or in the Shortcuts area below. Each shortcut uses an SF Symbols symbol or a preview image of the item it links to directly. The initial order in Spotlight and in the Shortcuts app follows the order defined by the developer (most important first); after the person starts using the shortcuts, the system reorders them prioritizing the most used.
- macOS: App Shortcuts are not supported; however actions created with App Intents are supported, and the person can build custom shortcuts with them in the Mac's Shortcuts app.
- visionOS, watchOS: no additional considerations.
- tvOS: not supported.

### Links to other articles
Siri, Snippets, Live Activities.

---

<!-- visual:app-shortcuts -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has no video.
- The search result with App Shortcuts is built as a single rounded horizontal bar, white and translucent, over a card with an orange-to-pink gradient, with four items side by side, each with its own label (img 0091).
- The shape separates the item types: the Notes app appears first, with a square icon and the label "Notes", and the three following shortcuts use red circular icons with a pencil symbol (img 0091).
- The same row combines an action shortcut, "New Note", with content shortcuts that open existing notes by name, "Meeting Agenda" and "Dog Names" (img 0091).
- Each content shortcut carries a thumbnail of the note itself behind the symbol, with ruled lines or the list of names visible, which makes the item recognizable by its content (img 0091).
- The card for a single shortcut on a white background has a small cup icon on the left and the phrase "Order a Vanilla Latte" in black, with the variable part highlighted in blue and underlined (img 0092).
- A callout line coming from below names that part as "Parameter", annotating within the card itself the difference between the fixed text of the phrase and the variable value (img 0092).
<!-- /visual:app-shortcuts -->

## Complications (slug: complications)

### What it governs
Governs the design of complications, the elements that display relevant, up-to-date information on the Apple Watch face.

### Why
The premise is that people prefer apps with powerful complications because that gives quick access to data that matters without needing to open the app. The text is explicit: the behavior people appreciate most in a complication is not the shortcut to open the app, it is the display of relevant information that always feels current. That is why a static complication, with no meaningful data, tends to lose prominent space on the watch face the person chose. The limit on daily updates per app reflects an arbitration of system resources: since the number of updates and timeline entries is limited, the app needs to choose the times that most add value to the data displayed.

### Do and avoid
- Identify essential, dynamic content the person wants to see quickly; avoid static complications with no meaningful data.
- Support as many complication families as possible to be available on more watch faces; if there is no useful data for a family, provide at least an image that represents the app (such as the icon) to allow opening the app from the watch face.
- Consider creating multiple complications per family to take advantage of shareable, app-centered watch faces.
- Define a different deep link for each supported complication, leading to the most relevant part of the app; complications that always open the same area seem less useful.
- Be careful with privacy: with the Always-On display, the information can be visible to people other than the one wearing the watch.
- Choose carefully when to update the data, considering that the number of daily updates and stored timeline entries is limited.
- Choose the ring or gauge style according to the data: closed for a percentage of a total, such as a battery indicator; open when the minimum and maximum values are arbitrary or do not represent a percentage, such as a speed indicator; segmented, similar to open, for values within a range defined by the app, useful for fast-changing values.
- Make sure images look good in tinted mode (tinted): avoid using color as the only means of communicating important information, and provide, when necessary, an alternative tinted version of a colored image that does not look good desaturated.
- In general, use line widths of two points or more in complication content, because thinner lines are hard to see quickly, especially with the person in motion.
- Provide a set of static placeholder images for each supported complication, used while the system checks whether it can generate a localized placeholder.
- Prefer using WidgetKit to develop complications starting with watchOS 9; for earlier versions, use the CLKComplicationDataSource protocol from ClockKit.

### Exact specifications
Starting with watchOS 9, the system organizes complications into families (circular, corner, inline, rectangular) with recommended layouts; complications from earlier versions use legacy templates (nongraphic) that do not take on the color the person selected.

Circular, regular image (by case size 40mm / 41mm / 44mm / 45mm-49mm):
- Image: 42x42 pt / 44.5x44.5 pt / 47x47 pt / 50x50 pt (84x84, 89x89, 94x94, 100x100 px @2x)
- Closed gauge: 27x27 pt / 28.5x28.5 pt / 31x31 pt / 32x32 pt
- Open gauge: 11x11 pt / 11.5x11.5 pt / 12x12 pt / 13x13 pt
- Stack (not text): 28x14 pt / 29.5x15 pt / 31x16 pt / 33.5x16.5 pt
- Default text (SwiftUI): Rounded style, Medium weight, size 12 pt (40mm), 12.5 pt (41mm), 13 pt (44mm), 14.5 pt (45mm/49mm)

Circular extra-large (for the X-Large watch face):
- Image: 120x120 pt / 127x127 pt / 132x132 pt / 143x143 pt
- Open gauge: 31x31 pt / 33x33 pt / 33x33 pt / 37x37 pt
- Closed gauge: 77x77 pt / 81.5x81.5 pt / 87x87 pt / 91.5x91.5 pt
- Stack: 80x40 pt / 85x42 pt / 87x44 pt / 95x48 pt
- Default text: Rounded, Medium, size 34.5 pt (40mm), 36.5 pt (41mm), 36.5 pt (44mm), 41 pt (45mm/49mm)

Placeholders for the circular family (38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm):
- Circular:, / 42x42 pt / 44.5x44.5 pt / 47x47 pt / 50x50 pt
- Bezel:, / 42x42 pt / 44.5x44.5 pt / 47x47 pt / 50x50 pt
- Extra Large:, / 120x120 pt / 127x127 pt / 132x132 pt / 143x143 pt

Corner (40mm / 41mm / 44mm / 45mm-49mm):
- Circular: 32x32 pt / 34x34 pt / 36x36 pt / 38x38 pt
- Gauge: 20x20 pt / 21x21 pt / 22x22 pt / 24x24 pt
- Text: 20x20 pt / 21x21 pt / 22x22 pt / 24x24 pt
- Placeholder (38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm):, / 20x20 pt / 21x21 pt / 22x22 pt / 24x24 pt
- Default text: Rounded, Semibold, size 10 pt (40mm), 10.5 pt (41mm), 11 pt (44mm), 12 pt (45mm/49mm)

Inline, utilitarian small (38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm):
- Flat: 9-21x9 pt / 10-22x10 pt / 10.5-23.5x21 pt / N/A / 12-26x12 pt
- Ring: 14x14 pt / 14x14 pt / 15x15 pt / 16x16 pt / 16.5x16.5 pt
- Square: 20x20 pt / 22x22 pt / 23.5x23.5 pt / 25x25 pt / 26x26 pt

Inline, utilitarian large (Flat, 38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm): 9-21x9 pt / 10-22x10 pt / 10.5-23.5x10.5 pt / N/A / 12-26x12 pt.

Rectangular (40mm / 41mm / 44mm / 45mm-49mm):
- Large image with title: 150x47 pt / 159x50 pt / 171x54 pt / 178.5x56 pt (with automatic corner radius of 4 pt)
- Large image without title: 162x69 pt / 171.5x73 pt / 184x78 pt / 193x82 pt
- Standard body: 12x12 pt / 12.5x12.5 pt / 13.5x13.5 pt / 14.5x14.5 pt
- Text gauge: 12x12 pt / 12.5x12.5 pt / 13.5x13.5 pt / 14.5x14.5 pt
- Default text: Rounded, Medium, size 16.5 pt (40mm), 17.5 pt (41mm), 18 pt (44mm), 19.5 pt (45mm/49mm)

Legacy templates: circular small, modular small, modular large, extra large, each with its own image size tables per case (38mm, 40mm/42mm, 41mm, 44mm, 45mm/49mm), including Ring, Simple, Stack and Placeholder formats.

### Platform differences
Not supported on iOS, iPadOS, macOS, tvOS or visionOS; exclusive to watchOS.

### Links to other articles
Watch faces (the text points to it for the concept of a shareable watch face centered on complications).

---

<!-- visual:complications -->
### What the illustrations show
Basis: 14 of 14 illustration sheets opened, all codes checked; the page has no video and only brings light versions of the sheets.
- The opening is a position vocabulary diagram: a stylized watch face with thin lines connecting labels to the zones Top Left (Earth), Date, Middle (rectangular agenda card), Bottom Left (activity rings), Bottom Middle (compass with "315° NW") and Bottom Right (temperature with a low and high range) (img 0344).
- Every example is a slot on a black background: square in most families (Circular, Corner, Circular small, Modular small, Extra large) and wide rectangle in Inline, Rectangular, Modular large and one case of Circular with curved text (img 0345 to img 0397, img 0353).
- The closed ring wraps a symbol or number: vivid red covering about 90% around a music note, with the rest in dimmed red (img 0345), green almost closed with a slight overlap at the starting point around "100" (img 0346) and blue covering about 85% around "85" (img 0355).
- The open arcs use a gradient and leave the base for an icon or abbreviation: green to violet with a small sun near 6 o'clock (img 0347), multicolor arc with "AQI" below "42" (img 0348) and, in the temperature ones, low and high as smaller colored numbers below the value, green for the low extreme and orange or red for the high (img 0349, img 0358).
- In the Circular family there are also slots without a gauge: a stack of text with "AAPL" in white and the quote in green (img 0352), a red sunset icon above the time in white (img 0351) and just the Breathe app icon, with no text (img 0350).
- Curved text following the edge appears only in Corner and one Circular case, always in uppercase or compact letters: the curved agenda at the top with "FRI" in red and a large "23" in white (img 0353), "CUP" in white with the time zone in orange (img 0365) and the stopwatch in orange with a small icon (img 0366).
- The Corner gauges follow the curve of the corner: a thick curved orange bar above "14:59" with a stopwatch icon (img 0363) and a short green to orange arc next to "72°", with the extremes at the ends and an orange dot marking the current position (img 0364); there is also a sun icon behind a cloud over a rounded dark blue background (img 0362).
- Inline occupies a wide black rectangle in a horizontal band: light gray text on one line, such as "LON 6:09" and "11:00AM PHOTO SHOOT" (img 0367, img 0371), two white gauges side by side (img 0368, img 0369) or a realistic image of the moon on the left with the rest empty (img 0370).
- Rectangular organizes three left-aligned lines with color hierarchy, title in blue, value in white and secondary line in gray (img 0372); the variation swaps the third line for an icon in the title and a blue progress bar at about 70% at the base (img 0373), and the heart rate one puts "2 MINS AGO" in red above a line graph with a vertical axis of 102 and 52 and a horizontal axis from 12AM to 6PM (img 0374).
- In Modular large, the first colored line works as the title and the rest comes in white, such as "Cupertino, CA" in red (img 0389), "Final Score" in light blue (img 0390) and "Wednesday" in red over a much larger "Mar 9" (img 0391); in columns, yellow labels CAL, MIN and HOUR sit to the left of the values in white (img 0388), a pattern that Modular small repeats with CP and MH in purple (img 0381).
- The same data is recomposed according to the family: "LON 6:09" stays on a single line in Inline (img 0367), stacked in salmon over a reddish brown circle in Circular small (img 0380) and stacked in orange and white in Modular small and Extra large (img 0387, img 0397); the sunset with time repeats across five families (img 0351, img 0360, img 0379, img 0386, img 0396) and "68°" grows to occupy almost the entire width in Extra large (img 0385 compared with img 0395).
- In Circular small, less saturated colors and darkened background circles predominate: a beige ring around a drop (img 0375), a stopwatch in salmon with no ring (img 0377), "68°" in pale yellow over a darkened circle (img 0378) and a sunset in white over a dark gray circle (img 0379).
Recorded divergences: in the opening the tone is more an orange and pink gradient than the uniform red described (img 0344); in img 0367 "LON" and "6:09" appear side by side on one line, not stacked as the official description says; in img 0390 there are no grid lines separating columns, unlike the gridded table described; the Breathe icon is teal in img 0350 and predominantly blue in img 0359; the curved text in img 0353 was only read approximately.
<!-- /visual:complications -->

## Controls (slug: controls)

### What it governs
Governs the design of controls, buttons or toggles that give quick access to an app feature from the Control Center, the Lock Screen or the Action Button.

### Why
The central logic is that a control exists to represent, compactly and without opening the app, the state and the action of a specific feature. Since the control appears in contexts with little or no text (for example, just the symbol on the Lock Screen), the symbol alone needs to carry the meaning of the action, hence the requirement to choose a descriptive symbol and to provide versions for the two states of a toggle. The requirement to redact sensitive information when the device is locked, and for authentication for actions that affect security, reflects the same concern present in Live Activities and widgets: these elements stay visible to third parties and must not leak private data or allow critical actions without identity confirmation.

### Do and avoid
- Offer controls for actions that bring the greatest benefit without needing to open the app; for example, starting a Live Activity directly from a control.
- Update controls when the person interacts with them, when an action is completed, or remotely via push notification, accurately reflecting the state and whether the action is still in progress.
- Choose a descriptive symbol that suggests the control's behavior; for toggles, provide a symbol for both states (the example given is `door.garage.open` and `door.garage.closed`).
- Use symbol animations to highlight state changes: animate the transition between states in toggles; for buttons with a duration action, animate indefinitely while the action is occurring and stop when it completes.
- Select a tint color aligned with the app's brand; the system applies it to the toggle's symbol in the active state, and also to the value and symbol shown in the Dynamic Island when the action is triggered by the Action Button.
- Help the person provide additional information needed for the action (for example, choosing which specific light to control), requesting configuration already at the first addition of the control; reconfiguration can happen at any time.
- Provide hint text for the Action Button, using verbs, to explain what happens when pressing and holding.
- Include a placeholder if the control's title or value can vary, shown in the controls gallery of the Control Center, the Lock Screen, or before assigning it to the Action Button.
- Hide sensitive information when the device is locked, and you can specify whether the symbol's own state should also be redacted (in that case, the system shows the symbol in its off state).
- Require authentication for actions that affect security, such as locking/unlocking a door or starting a car.
- If the app supports camera capture, it is possible to create a control that leads directly to the app's camera experience even with the device locked; any task beyond capture requires unlocking.
- Use the same camera UI in the app and in the control's camera experience, so the transition feels continuous.
- Provide instructions to help the person understand how to add the control that opens this camera experience.

### Exact specifications
No numeric value (measurement, duration, size) is provided in this article.

### Platform differences
- iOS, iPadOS, macOS: no additional considerations.
- watchOS, tvOS, visionOS: not supported.

### Links to other articles
Live Activities, Widgets, Action button, Branding, SF Symbols.

---

<!-- visual:controls -->
### What the illustrations show
Basis: 3 of 3 illustration sheets opened, all codes checked; the page has no video and only brings light versions of the sheets.
- The opening is a stylized cutout of Control Center in monochrome pink with no text, with translucent circular buttons (airplane, AirPlay, Wi-Fi, signal, Bluetooth, link, globe) grouped together and a larger Wi-Fi button taking up more space in the bottom left corner (img 0399).
- The anatomy is taught with callout lines over a control with rounded corners on a light-textured background: a moon symbol on the left, labeled "Symbol image", and on the right two stacked lines, the title on top and the detail below, the latter labeled "Value" (img 0400).
- In the real Control Center on iPhone, over a blurred dark background, the grid shows Wi-Fi active in blue, Bluetooth in blue and cellular signal in green, and the silence control appears active as a white circle with a crossed-out bell, with brightness and volume below, plus a media card and Focus at the bottom (img 0401).
- The same silence control appears on three surfaces: in the Control Center grid (img 0401), as a translucent circular button at the bottom of the Lock Screen next to the flashlight (img 0402) and in the expanded Dynamic Island, with a crossed-out bell and the word "Silent" in red over the app grid (img 0403).
- The tint color is taught with a pair of the same large circular control: a white lightbulb with no color in the off state (img 0404) and a lightbulb filled in vivid yellow in the on state (img 0405).
- The configurable control is a long rectangle with a moon in a gray circle on the left and the word "Option" accompanied by up and down arrows, indicating that a value can be chosen (img 0406).
- The Action Button's hint text is shown as a pair: with the pill on "Ring" and a white bell, the hint over the icons says "Hold for Silent" (img 0407); with the pill on "Silent" and a crossed-out red bell, it says "Hold for Ring" (img 0408), that is, the hint starts with a verb and names the result of holding, not the current state.
- The hiding of sensitive data is a before and after of the same pill-shaped control: unlocked, on a white background with a yellow lightbulb, title in black and detail in gray (img 0409); locked, on a dark background with a white lightbulb and the text swapped for two light gray bars, one short and one long, without changing shape or size (img 0410).
Recorded divergences: the notes indicate that the official description does not always clarify when the image is a real screenshot, as in img 0401, img 0402, img 0403, img 0407 and img 0408, and when it is an illustration.
<!-- /visual:controls -->

## Live Activities (slug: live-activities)

### What it governs
Governs how an app communicates the progress of an activity, event or task in visible places in the system (Dynamic Island, Lock Screen, StandBy, the Mac menu bar, the Apple Watch Smart Stack, CarPlay Dashboard) without requiring the person to open the app.

### Why
The central idea is that a Live Activity goes beyond a one-off notification: it delivers frequent status updates over a period of time and allows interaction with the information shown, serving as a "unified home" for alerts and indicators of an activity in progress. The limitation to short to medium duration activities (up to eight hours) and the focus on essential information stem from the principle that the Live Activity needs to stay relevant and glanceable, not a replica of the app's screen. The rules for concentric margins and alignment around the TrueDepth camera (Dynamic Island) exist because the physical shape of the screen cutout imposes a geometry that, if ignored, produces visual tension, elements "poking through" the rounded contour or looking misaligned.

### Do and avoid
- Offer Live Activities for tasks and events with a defined start and end, prioritizing short to medium durations that do not exceed eight hours.
- Focus on the most important information for a quick glance; the Live Activity does not need to show everything, and the person can tap to open the app and see more details.
- Do not use Live Activity for advertisements or promotions.
- Avoid showing sensitive information, since the Live Activity is visible in public places such as the Lock Screen or the Always-On display; prefer showing a harmless summary and letting a tap lead to the app to see the sensitive content, or redact the sensitive views and let the person configure whether they want to show them.
- Create a Live Activity that matches the app's aesthetic and visual personality, in both light and dark mode, to reinforce recognition.
- If you include a brand mark (logo mark), show it without a container and do not use the app's full icon.
- Do not add elements to the app that call attention to the Dynamic Island.
- Make sure the text is easy to read: use large text, with a stronger weight (medium or above), and use small text with restraint.
- Adapt to different screen sizes and presentations, using the values in the specifications section as a reference.
- Adjust the size and position of elements for efficient use of space, showing only what is necessary for the content.
- Use familiar layouts and templates with standard system margins and recommended text sizes, available in the Apple Design Resources.
- Use consistent margins and concentric positioning: align the content's corner radius to the Live Activity's outer corner radius by subtracting the margin, via the SwiftUI container (ContainerRelativeShape).
- When separating a block of content, use a container with an inset shape or a thick line; do not draw content all the way to the edge of the Dynamic Island.
- Dynamically change the height of the Live Activity on the Lock Screen or in the expanded presentation according to the amount of information available.
- Do not customize the background color of the compact, minimal and expanded presentations (fixed opaque black background); it is possible to customize the background color of the Lock Screen presentation, ensuring sufficient contrast, especially in Always-On with reduced luminance.
- Use color to express the app's identity; strong colors help the Live Activity stand out among others.
- Tint the color of the key line (the visible outline on a dark background/Dark Mode) to match the content.
- Use system or custom transitions and animations with a maximum duration of two seconds; the system does not animate on Always-On displays with reduced luminance.
- Animate layout changes while preserving as much of the existing layout as possible, moving elements to their new positions instead of removing them and animating them back in.
- Avoid overlapping elements; prefer animating elements out and animating them back in at a new position, using fade-in/fade-out for list items that do not move.
- Make sure tapping the Live Activity opens the app at the right location, directly related to the content.
- Focus on simple, direct actions; limit interactivity, preferably to a single element, reserved for essential functionality that the person activates once or temporarily pauses/resumes (music playback, workouts, audio recording).
- Consider allowing the person to respond to event or progress updates with a button or toggle.
- Start the Live Activity at appropriate moments and make it easy to turn off in the app; offer controls within the app itself (for example, a button to stop following a game).
- Offer an App Shortcut that starts the Live Activity, for example via the Action Button.
- Update the Live Activity only when there is new content; keep the same display if the status does not change.
- Alert only for essential updates that require attention; alerts light up the screen and play a sound by default. Avoid alerting too frequently or for non-crucial updates, and do not use push notifications alongside Live Activities for the same updates.
- Let the person follow multiple events with a single Live Activity that uses a dynamic layout and switches between events, instead of creating separate Live Activities.
- End the Live Activity immediately when the task or event finishes; consider setting a custom dismissal time, proportional to the duration of the activity (in most cases, 15 to 30 minutes is appropriate).
- Start the design with iPhone and then refine it for other contexts (StandBy, CarPlay, Apple Watch).

### Compact presentation
- Focus on the most important, dynamic and up-to-date information.
- Ensure visual unity between the leading and trailing elements (separated by the TrueDepth camera), using consistent color and typography.
- Keep the content as narrow as possible and snug against the TrueDepth camera, without obscuring key information in the status bar and without extra padding; keep the layout balanced between the two sides.
- When tapped, take the person directly to the related details in the app; make sure the leading and trailing elements lead to the same screen.

### Minimal presentation
- Make sure the Live Activity is recognizable: show updated information instead of just a static logo, if possible (the example given is the Timer showing the time remaining instead of a fixed icon).

### Expanded presentation
- Keep the relative positioning of elements to create a coherent layout across presentations, with predictable expansion.
- Wrap the content tightly around the TrueDepth camera, avoiding empty space.

### Lock Screen presentation
- Do not replicate the notification layout; create a layout specific to the content of the Live Activity.
- Choose colors that work well on a customized Lock Screen, using custom background color and tint and using opacity with restraint.
- Ensure sufficient contrast in Dark Mode and on the Always-On display; by default the Live Activity uses a light background in light mode and a dark background in dark mode.
- Check the automatically generated color for the dismiss button, which matches the Live Activity's background and foreground colors, adjusting via `activitySystemActionForegroundColor(_:)` if necessary.
- Use standard margins to align the design with notifications.

### StandBy presentation
- Update the layout for StandBy, considering a custom layout that makes use of the extra space.
- Consider using the default background color in StandBy, which blends the Live Activity with the device's frame and allows a slightly larger scale since it does not need to accommodate the margins around the TrueDepth camera.
- Use standard margins and avoid extending graphic elements to the edge of the screen.
- Check the design in Night Mode, in which the system applies a red tint.

### CarPlay
- On CarPlay, the system automatically combines the leading and trailing elements of the compact presentation into a single layout on the CarPlay Dashboard.
- The same Live Activity design applies to CarPlay and Apple Watch; although Live Activities on Apple Watch can be interactive, the system disables interactive elements on CarPlay.
- Consider creating a custom layout if the Live Activity benefits from larger text or additional information, declaring support for the supplementary family `ActivityFamily.small`.
- Be cautious about including buttons or toggles in the custom layout, since CarPlay disables them; prefer showing time-based content instead of controls if the person is likely to look at the Live Activity while driving.

### Exact specifications

Maximum animation duration: 2 seconds (there is no animation on Always-On with reduced luminance).

Standard layout margin on the Lock Screen: 14 points.

Dismissal time after the activity ends: recommended 15 to 30 minutes (the Live Activity is removed immediately from the Dynamic Island and CarPlay when it ends; on the Lock Screen, the Mac menu bar and the watchOS Smart Stack it remains for up to four hours, unless a custom time is set).

CarPlay dimensions: Live Activity at 240x78 pt, 240x100 pt, 170x78 pt. Smart Display Zoom settings: Widescreen 1920x720 pt, Portrait 900x1200 pt, Standard 800x480 pt.

iOS dimensions (all in points):
- Screen 430x932: compact leading and trailing 62.33x36.67; minimal (width as a range) 36.67 to 45x36.67; expanded (height as a range) 408x84 to 160; Lock Screen (height as a range) 408x84 to 160.
- Screen 393x852: compact leading and trailing 52.33x36.67; minimal 36.67 to 45x36.67; expanded 371x84 to 160; Lock Screen 371x84 to 160.

Corner radius of the Dynamic Island: 44 points, with the same rounded shape as the TrueDepth camera.

Width of the Dynamic Island by device (compact/minimal and expanded, in points): iPhone 17 Pro Max 250/408; iPhone 17 Pro 230/371; iPhone Air 250/408; iPhone 17 230/371; iPhone 16 Pro Max 250/408; iPhone 16 Pro 230/371; iPhone 16 Plus 250/408; iPhone 16 230/371; iPhone 15 Pro Max 250/408; iPhone 15 Pro 230/371; iPhone 15 Plus 250/408; iPhone 15 230/371; iPhone 14 Pro Max 250/408; iPhone 14 Pro 230/371.

iPadOS dimensions (Lock Screen, height as a range, in points): screen 1366x1024 → 500x84 to 160; 1194x834 → 425x84 to 160; 1012x834 → 425x84 to 160; 1080x810 → 425x84 to 160; 1024x768 → 425x84 to 160.

macOS dimensions: use the same values as iOS.

watchOS dimensions (Smart Stack, in points, by case size): 40mm → 152x69.5; 41mm → 165x72.5; 44mm → 173x76.5; 45mm → 184x80.5; 49mm → 191x81.5.

### Platform differences
- iOS, iPadOS: no additional considerations beyond those already described in the presentations.
- macOS: active Live Activities automatically appear in the menu bar of a paired Mac, using the compact, minimal and expanded presentations; clicking it opens iPhone Mirroring to display the app.
- watchOS: when started on iPhone, the Live Activity appears at the top of the paired Apple Watch's Smart Stack; by default it combines the leading and trailing elements of the compact presentation. Without a watchOS app, tapping opens a full-screen view with a button to open the app on the paired iPhone; with a watchOS app, tapping opens the watchOS app. It is possible to create a custom watchOS layout with more information and interactive functionality, but the same CarPlay cautions regarding buttons/toggles apply, since the custom watchOS layout is also used on CarPlay.
- tvOS, visionOS: not supported.

### Links to other articles
App Shortcuts, Widgets, Dark Mode, Always On, CarPlay, StandBy.

---

<!-- visual:live-activities -->
### What the illustrations show
Basis: 7 of 7 illustration sheets opened, all codes checked; the page has no video.
- The opening stacks two Dynamic Islands: on top, a dashed, empty red pill over the summarized scoreboard, and below it the full scoreboard with teams, icons, pitchers and the game situation, suggesting the passage from the simple shape to the full content (img 0700).
- The presentations are labeled with callout lines over the iPhone frame and with no real content: compact is two black shapes on both sides of a red pill, "Leading side" and "Trailing side" (img 0701); minimal is a pill attached to the island, "Minimal (attached)", and a separate black circle, "Minimal (detached)" (img 0702); expanded is a single black shape almost the width of the device, with the red pill centered at the top (img 0703).
- On the Lock Screen, the Live Activity is a rounded black banner in the bottom third, with blue icons on the left and two lines of text on the right, and the dynamic data "8 minutes" in blue (img 0704); the same card also appears overlaid at the top of the Home Screen, covering part of the icon grid (img 0705).
- Legibility is shown in a pair: small "GATE" and "C15" in two lines next to the pill (img 0707) against just "C15", larger and heavier (img 0709), with isolated markers of a gray X and a green check (img 0708, img 0710); the approved version trades content for size and weight.
- A thin red border outlines the entire expanded capsule as a margin guide, and the "Contact Juan C." button with a speech bubble sits in a separate rounded dark bar, below the delivery content (img 0711).
- The concentric margin is checked with the capsule outlined in red: a light blue circle pressed against the border, with no breathing room (img 0712), the bag and cup icon with a small gap (img 0713), and the same icon in an almost identical position, which the official caption marks as close to the border without crossing into the curve (img 0714).
- To separate a block, the "Text" bar glued to the bottom and both sides, with no corners of its own, is the error (img 0715); the alternatives are a rounded-corner rectangle, inset and with visible margin on the sides and bottom (img 0716), or a light blue horizontal line with "Text" below it, with no box (img 0717).
- Alignment to the rounded perimeter is checked with the content deliberately blurred inside a dashed red box: too far from the right border (img 0718) and shifted close to the rounded corner without crossing it (img 0719).
- In compact, the error is the empty space between the pill that represents the camera and the block with "8min", which leaves the shape wide and unbalanced (img 0720); the correction brings the two closer and reduces the total width (img 0721).
- In expanded, a dashed red line marks the empty strip between the camera and the start of the content (img 0722); in the corrected version, the block starts closer to the camera's level, without that strip (img 0723).
- The StandBy flight card is solid, wide blue, with the content inside a dashed rectangle: airline, route SFO to NRT with a plane and dotted flight path, time to landing, departure and terminal (img 0706); in Night Mode the same layout appears entirely in shades of red over black, with no blue (img 0724).
- The adaptation to watchOS comes in a chain: the iPhone compact with an icon on the left and "8min" on the right (img 0725); the standard Smart Stack, a white card with "From Delivery App" in gray at the top and the icon and "8 min" pushed to opposite corners of the base (img 0726); and the custom layout, with a bold title, "Arriving in" and "8 min" stacked on the left and a light blue progress ring with the icon centered on the right (img 0727).
Recorded divergences: in img 0706 the dashed line marks the content area inside the blue card, not the outer border that the official description associates with the 2x scale; the padding difference between img 0713 and img 0714 is too subtle to measure by eye and was read from the official caption; in img 0717 the line looks thin, even though the text talks about a thick line; the sheet for img 0708 shows only the error marker, with no context image.
<!-- /visual:live-activities -->

## Notifications (slug: notifications)

### What it governs
Governs the content, actions and badges of notifications, the mechanism by which an app delivers timely, high-value information that the person understands quickly.

### Why
The central principle is that the person turns on notifications to receive quick updates in a succinct way, and that they respond to notifications when it suits them, not immediately. This explains the rule against repeated notifications for the same subject (it clutters the Notification Center and can lead the person to turn off all notifications from the app) and against task instructions that depend on the person remembering them after dismissing the notification. The refusal to use badges for anything other than a count of unread notifications follows the same reasoning about interface honesty found in other articles in the group: a system component must always mean the same thing, or the person loses the ability to trust it.

### Do and avoid
- Provide concise, informative notifications.
- Avoid sending multiple notifications for the same subject, even if the person hasn't responded.
- Avoid notifications that instruct the person to perform specific tasks within the app; if it makes sense, offer simple actions right in the notification instead.
- Use an alert, not a notification, to display error messages.
- Handle notifications gracefully when the app is in the foreground: notifications don't appear, but the app still receives the information; present it in a way that's noticeable but not intrusive, such as incrementing a badge or discreetly inserting the data into the current view (the example given is Mail simply adding the message to the list of unread items).
- Avoid including sensitive, personal or confidential information in a notification, since you can't predict the context in which the person will receive it.
- When the notification has a title, the system displays it at the top; in a direct communication notification, the system automatically shows the sender's name; in a notification not related to communication, it shows the app's name if no title is provided.
- Create a short title when it gives context to the content; use title-style capitalization and no ending punctuation.
- Write succinct, easy-to-read content, using complete sentences, sentence case and correct punctuation, without truncating manually (the system truncates when necessary).
- Provide generically descriptive text for when notification previews are turned off in Settings, giving enough context without revealing too much detail (examples cited: "Friend request", "New comment", "Reminder", "Shipment"), with sentence-style capitalization.
- Avoid including the app's name or icon in the text, since the system already automatically displays a large version of the icon (or the contact image badged with the icon, in communication notifications).
- Consider providing a sound to complement notifications; if using a custom sound, make sure it's short, distinctive and well produced, but don't rely on it to communicate important information, since the person may not hear it. It's not possible to schedule a vibration to go along with the sound.
- The notification can present up to four action buttons to perform tasks without opening the app; offer actions that make sense in context, with a short label in title case describing the result, with no app name or extra information.
- Avoid providing an action that only opens the app, since that clutters the detail view.
- Prefer nondestructive actions; if a destructive action is necessary, ensure enough context to avoid unintended consequences (the system gives a distinct appearance to actions identified as destructive).
- Provide a simple, recognizable interface icon for each notification action, displayed on the trailing side of the action's title.
- Use a badge only to show how many unread notifications exist; don't use a badge for numeric information unrelated to notifications (weather data, dates, stock prices, scores).
- Make sure badging isn't the only method of communicating essential information, since the person can turn it off.
- Keep badges up to date, updating as soon as the person opens the corresponding notifications (reducing the count to zero removes all related notifications from the Notification Center).
- Avoid creating a custom image or component that imitates the appearance or behavior of a badge.

### Exact specifications
Up to four action buttons per notification (a limit common to iOS/iPadOS and to watchOS long looks).

### Platform differences
- iOS, iPadOS, macOS, tvOS, visionOS: no additional considerations.
- watchOS: notifications occur in two stages, short look and long look; it's also possible to view them in the Notification Center; on supported devices, the person can double-tap to respond.
  - Short look: appears when the wrist is raised and disappears when it's lowered. Avoid using it as the only way to communicate important information, since it appears briefly; maintain privacy, avoiding potentially sensitive information in the title.
  - Long look: provides more detail; the person can scroll vertically or use the Digital Crown; it can be dismissed by tapping or lowering the wrist. It can be static or dynamic; the static interface displays the message and additional static text/images; the dynamic interface gives access to the full content and more visual configuration options. The system uses the static interface as the default when the dynamic one is unavailable (no network, or the iPhone companion app is unreachable). Provide, at minimum, the static interface; preferably also provide the dynamic one. The general structure (sash at the top with icon and app name, Dismiss button at the bottom below all custom buttons) can't be changed, but the sash area and the background of the content area can be customized (solid color or a blurred/translucent appearance on the sash). By default, the background of the content area is transparent; to match the background of other system notifications, use white at 18% opacity, or a custom brand color. It's possible to offer up to four custom actions below the content area, in addition to the Dismiss button always present at the bottom.
  - Double tap: when responding by double tap, the system selects the first nondestructive action as the response; so the order of custom actions matters, and it's a good idea to put the most-used action at the top of the list.

### Exact specifications (watchOS)
Default background opacity to match other system notifications: white with 18% opacity.

### Links to other articles
Managing notifications, Alerts.

---

<!-- visual:notifications -->
### What the illustrations show
Basis: 1 illustration sheet viewed (3 images, all in light appearance), code checked; no videos.
- The opening image is a specification diagram, not just a conceptual drawing: over the mockup of a notification, ruler guides in the shape of an H (width) and an I (height) appear, marking margins and internal alignments (img 0810).
- The standard anatomy is legible in this diagram: app icon on the left with width guides on both sides, title in the center with a dotted line indicating the extent of the text and height guides above and below, description right below with the same marking, and the "now" timestamp in the top right corner with its own width guide (img 0810).
- The whole set rests on a semitransparent rectangular card with rounded corners, with the notification tinted red and orange (img 0810).
- The watchOS short look is a vertical card in which the large circular icon, over a dark purplish blue gradient background, occupies most of the upper area, with a bold title and a short preview of the content below (img 0811).
- The long look appears inside the watch screen, with the time at the top, a small circular icon in the card's top left corner, "now" on the right, a bold title, body text and two full-width action buttons (img 0812).
- In the long look, the second action button is cut off by the bottom edge of the screen, a visual cue indicating that the content continues and can be scrolled (img 0812).
- The difference between the two stages is built through the proportion between image and text: in the short look the icon dominates and the text is minimal; in the long look the icon shrinks to a badge in the corner and the space becomes that of the text and buttons (img 0811 and img 0812).
Recorded divergences: the official description of img 0810 speaks only of a stylized representation of a notification, but the image viewed is a diagram with measurement markings (H and I guides) over the layout.
<!-- /visual:notifications -->

## Snippets (slug: snippets)

### What it governs
Governs snippets, compact views displayed in response to an action performed via Siri, Spotlight or the Shortcuts app, showing a result or requesting confirmation.

### Why
The distinction between a confirmation snippet and a result snippet reflects two distinct needs of voice/intent interaction: confirming before acting (with the possibility of options that affect the result) versus just informing the outcome, which requires no further action. The rule of omitting the spoken dialogue text from the snippet's visual representation and using the custom view to communicate the information visually avoids redundancy between what Siri says and what the person sees, recognizing that speech and reading are complementary channels, not identical ones.

### Do and avoid
- Ensure legibility: check for sufficient contrast between the snippet's custom content and the background provided by the system, in both appearances (light and dark), and keep margins consistent.
- Keep the content concise, since snippets exist for quick, lightweight interactions; create custom views with a maximum height of 400 points to ensure all the content stays visible.
- Take into account that fonts render at varying sizes according to the person's text size preference.
- For a result snippet, if you need to give more detail, deep link to the content in the app instead of including it in the custom view.
- Choose a descriptive label for a confirmation snippet's primary button (for example, "Order" instead of "OK" or "Proceed" for ordering coffee); if no label is specified, the system default is "Continue".
- Communicate the snippet's purpose visually; don't rely on showing the dialogue text to convey the purpose. Prefer omitting the dialogue from the visual representation and using the custom view to convey the information (the text gives an explicit example of incorrect use, in which the dialogue repeats information already shown in the custom view, and a correct example, in which the dialogue is omitted from the visual part).

### Exact specifications
Maximum height of a snippet's custom view: 400 points.

Components: a confirmation snippet includes two system-provided buttons (a secondary Cancel and a primary button with a customizable label); a result snippet includes a single Done button that dismisses the view.

### Platform differences
- iOS, iPadOS, macOS: no additional considerations.
- tvOS, visionOS, watchOS: not supported.

### Links to other articles
Siri, App Shortcuts, Live Activities.

---

<!-- visual:snippets -->
### What the illustrations show
Basis: 2 illustration sheets viewed (8 images, all in light appearance), codes checked; no videos.
- The opening illustration has measurement arrows at the top (horizontal) and on the right side (vertical) of the calendar card, treating width and height as deliberate dimensions of the component, and a dashed outline around the event block suggesting the customizable region; over the orange and red gradient, the "Done" button appears in red (img 1088).
- The snippet is a floating card over the previous screen, with the home screen blurred in the background and the status bar visible; it does not take up the whole screen (img 1089 and img 1090).
- The confirmation snippet separates content and actions: the app card, in dark red with an image of the coffee and a row with a round minus/plus stepper, sits above; the two buttons sit at the base, outside the colored card, with a light gray "Cancel" on the left and a wider blue "Order" on the right (img 1089).
- The result snippet has a single blue "Done" button taking up the width of the card, with no cancel option; the content uses a nearly full green progress bar and a row of four circular icons (img 1090).
- The anatomy diagram divides the card into three regions labeled by a side key: dialogue at the top, lilac custom view in the center with the vertical dimension of the maximum height of 400 pt, and at the base the pair of buttons, secondary gray on the left and primary blue on the right; it is the only image that carries the numeric value (img 1091).
- Wrong pair: the dialogue text at the top repeats names, date and time that the inner card already shows with a calendar icon, title and participants, and the image receives the gray X badge in a circle (img 1092 and img 1093).
- Right pair: the opening calendar snippet (img 1088), now with no dialogue text at all, with title and participants only inside the view's dashed block and a blue "Done" button, marked with a white check in a green circle (img 1094 and img 1095).
- Accent colors such as magenta pink and dark red identify the app's content, contrasting with the rest of the card in neutral gray and white (img 1089, img 1092 and img 1094).
<!-- /visual:snippets -->

## Status bars (slug: status-bars)

### What it governs
Governs the status bar, the strip at the top edge of the screen that displays the time, carrier, Wi-Fi signal and battery level.

### Why
The central recommendation, obscuring the content under the status bar, starts from the fact that its background is transparent by default, which can confuse the person when trying to interact with controls visible behind it without succeeding. The permission to hide it temporarily during full screen media recognizes that the status bar can distract when the person's attention is on the content, but the prohibition on hiding it permanently preserves basic access to time and connectivity without forcing the person to leave the app.

### Do and avoid
- Obscure the content under the status bar; since the background is transparent by default, prefer using a scroll edge effect to position a blurred view behind the status bar, keeping it legible and not suggesting that the content behind it is interactive.
- Consider temporarily hiding the status bar when displaying full screen media, for a more immersive experience (the example given is the Photos app hiding the status bar when browsing photos in full screen).
- Avoid hiding the status bar permanently, since without it the person needs to leave the app to see the time or the Wi-Fi connection; allow it to be shown again with a simple, discoverable gesture (in the Photos example, a single tap brings it back).

### Exact specifications
No numeric value is provided in this article.

### Platform differences
- iOS, iPadOS: no additional considerations.
- macOS, tvOS, visionOS, watchOS: not supported.

### Links to other articles
No related article is cited in the body of the text.

---

<!-- visual:status-bars -->
### What the illustrations show
Basis: 1 illustration sheet viewed (3 images, all in light appearance), code checked; no videos.
- The opening enlarges the iPhone status bar elements, with the time on the left and, on the right, cellular signal, Wi-Fi and a full battery; each element drops down through a thin vertical line to a label naming what it represents (time with location, signal bars, Wi-Fi strength, battery at 100%). It is a didactic piece, not a real capture (img 1104).
- The Wi-Fi callout line is the longest and crosses under the cellular signal label (img 1104).
- With the status bar visible, it sits directly over the photo at the top of the screen, and right below it comes a translucent navigation bar with a back arrow on the left, the photo's date and time in the center and a more options button with three dots on the right (img 1105).
- In the hidden version, the same photo with the same framing takes up the whole frame, with no status bar and also no navigation bar; the two interface layers disappear together (img 1106).
- The recommendation to hide the status bar in full screen media is demonstrated by an almost identical pair in which only the presence of the bars varies, without the X and check badges used on other pages (img 1105 and img 1106).
<!-- /visual:status-bars -->

## Top Shelf (slug: top-shelf)

### What it governs
Governs the Top Shelf area of the Apple TV Home Screen, which displays featured content in a rich way above the rows of apps in the Dock.

### Why
The idea is that Top Shelf is the opportunity to lead the person directly to the most relevant content as soon as they select the app in the Dock, with no intermediate steps. That's why the carousel templates prioritize buttons that lead straight to playback or to more information. The recommendation to avoid ads and prices comes from the logic that the person has already featured the app because they trust it; showing advertising there would break that already established relationship of trust.

### Do and avoid
- Help the person get straight into the content; the Carousel actions and Carousel details templates include, by default, a primary button to start playback and a More Info button to open the app in a details view.
- Feature new content (releases, recent episodes, upcoming movies and shows) and avoid promoting content the person has already bought, rented or watched.
- Personalize the person's favorite content, showing targeted recommendations and allowing them to resume playback or an active game.
- Avoid showing ads or prices; displaying purchasable content is acceptable, but prefer focusing on new, exciting content, showing prices only when interest has been demonstrated.
- Show dynamic, engaging content that helps attract the person and encourages watching more; if necessary, provide static images, but prefer creating layered images for a dynamic experience.
- If you do not provide the recommended dynamic full screen content, provide at least one static image as a fallback, displayed when the app is focused in the Dock and no full screen content is available; tvOS mirrors and blurs the image to fit 1920 pixels wide in the 16:9 ratio.
- Avoid suggesting interactivity in a static image, since it is not focusable.

### Dynamic layouts

Carousel actions: focuses on video and full-screen images with discreet controls; works well for content the person already knows, such as user-generated content or continuations of a franchise. Provide a concise title and, if necessary, a brief subtitle.

Carousel details: extends carousel actions, allowing you to include information about the content (synopsis, cast, metadata). Provide a title that identifies the current content, displayed near the top of the screen; above the title you can include a concise phrase or attribution to the app.

Sectioned content row: shows a single labeled row of sectioned content, useful for highlighting recently viewed, new or favorite content; the content is focusable, allowing quick scrolling, and a label appears when an item comes into focus. Provide enough content to fill the full width of the screen and include at least one label.

Scrolling inset banner: shows a series of large images that occupy almost the full width of the screen, with automatic timer-based scrolling until the person focuses on one; the sequence returns to the start after the last image. Provide three to eight images (a minimum of three is recommended for the effect to work; more than eight makes it harder to navigate to a specific image). If you need text, add it to the image itself (this layout does not show labels below the content), including the text also in the image's accessibility label so VoiceOver reads it.

### Exact specifications
- Static fallback image: 2320x720 pt (2320x720 px @1x, 4640x1440 px @2x).
- Poster (2:3): actual size 404x608 pt (808x1216 px @2x); safe/focused zone 380x570 pt (760x1140 px @2x); unfocused size 333x570 pt (666x1140 px @2x).
- Square (1:1): actual size 608x608 pt (1216x1216 px @2x); safe/focused zone 570x570 pt (1140x1140 px @2x); unfocused size 500x500 pt (1000x1000 px @2x).
- 16:9: actual size 908x512 pt (1816x1024 px @2x); safe/focused zone 852x479 pt (1704x958 px @2x); unfocused size 782x440 pt (1564x880 px @2x). When mixing image sizes in the same row, 16:9 images scale to 500 pixels in height when combined with poster or square.
- Scrolling inset banner: actual size 1940x692 pt (3880x1384 px @2x); safe/focused zone 1740x620 pt (3480x1240 px @2x); unfocused size 1740x560 pt (3480x1120 px @2x).
- Recommended number of images for scrolling inset banner: three to eight.

### Platform differences
Not supported on iOS, iPadOS, macOS, visionOS or watchOS; exclusive to tvOS.

### Links to other articles
Apple Design Resources (for the layout templates and layered images).

---

<!-- visual:top-shelf -->
### What the illustrations show
Basis: 2 illustration sheets viewed (5 images, all in light appearance), codes checked; no videos.
- The opening organizes the screen into two bands: a "Featured Content" title over a row of four large image cards, which represents the Top Shelf, and below a row of five circular app icons, which represents the app grid (img 1187).
- It's the only image with simulated app content; the others are abstract technical diagrams, one per image proportion (img 1187 to img 1191).
- The 2:3 poster diagram stacks three concentric rectangles with annotation rulers on the right: outer gray outline for the actual size, intermediate light blue line for the safe zone in focus, and inner solid blue area, the smallest, for the unfocused size (img 1188).
- Square 1:1 and 16:9 repeat exactly the same scheme, with the same three labels, the same order from outside to inside and the same blue code; only the proportion of the rectangle changes (img 1189 and img 1190).
- In all formats the unfocused size is the innermost and smallest solid layer (img 1188 to img 1191); in the three fixed-proportion diagrams this indicates that the actual artwork needs margin beyond the unfocused visible area (img 1188 to img 1190).
- In the scrolling banner, a wide and short band, the order of the rulers changes: the safe zone in focus label points to the outermost thin edge and the actual size label to the intermediate line, reversing the position of these two labels relative to the three previous diagrams (img 1191).
<!-- /visual:top-shelf -->

## Watch faces (slug: watch-faces)

### What it governs
Governs the design and sharing of watch faces, the view the person chooses as the main one on watchOS, and how an app can configure shareable watch faces that highlight its complications.

### Why
The watch face is described as the center of the watchOS experience, and the ability to share configured watch faces (since watchOS 7) reflects the logic that a well-curated watch face, with the app's complications already configured, offers a ready experience without requiring the person to configure anything on their own. This serves both engagement (a fitness instructor sharing a watch face with her students) and app discovery, since whoever adds the watch face without having the app installed is prompted to install it.

### Do and avoid
- Help the person discover the app by sharing watch faces that highlight its complications; ideally support multiple complications to compose a curated experience.
- For some watch faces, it's possible to specify a system accent color, images or styles.
- If the person adds the watch face without having the app installed, the system prompts for installation.
- Display a preview of each shared watch face, highlighting its advantages; you can get a preview by emailing the watch face to yourself through the Watch app on iOS, which includes an illustrated device frame suitable for display on websites and in apps. Alternatively, you can replace the illustrated frame with a high-fidelity hardware frame, available in Apple Design Resources, and compose it over the preview.
- Try to offer shareable watch faces for all Apple Watch devices. Some watch faces are available starting with Series 4 (California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, Solar Dial), and Explorer is available starting with Series 3 with cellular. If you use one of these watch faces in the configuration, consider offering a similar configuration using a watch face available on Series 3 or earlier, clearly labeling the devices supported by each shareable watch face.
- Respond gracefully if the person chooses an incompatible watch face: the system sends an error to the app when this happens on Series 3 or earlier; consider immediately offering an alternative configuration with a compatible watch face, instead of displaying an error, and help the person understand, alongside the previews, that they may receive an alternative watch face if they choose one incompatible with their device.

### Exact specifications
No specific numeric value (measurement, duration, etc.) is given; the article cites only watch face names and the minimum hardware generations required (Series 4 for the named list; Series 3 with cellular for Explorer).

### Platform differences
Not supported on iOS, iPadOS, macOS, tvOS or visionOS; exclusive to watchOS.

### Links to other articles
Apple Design Resources.

---

<!-- visual:watch-faces -->
### What the illustrations show
Basis: 1 illustration sheet viewed (1 image, in light appearance), code checked; no videos.
- The opening works as a comparative showcase: three watch faces side by side, each cropped inside a rounded rectangle with a dashed outline and connected by a vertical line to its name written below (img 1284).
- The three examples show distinct information arrangements: Solar Graph with a large digital time, day of the week, solar curve and temperature; round analog GMT with hands, a 24-hour marking on the edge, an activity indicator in the upper corner and numeric data at the base; Unity Lights with thin white hands and curved scales in the corners for decibels, date and temperature (img 1284).
- The set uses a diagonal gradient from orange to reddish pink in the background, rather than a uniform red tint (img 1284).
Recorded divergences: the official description only speaks of a stylized representation of a series of watch faces tinted red; the image shows the three names in full (Solar Graph, GMT, Unity Lights) with a connecting line between each watch face and its name, which the description does not mention.
<!-- /visual:watch-faces -->

## Widgets (slug: widgets)

### What it governs
Governs the design of widgets, which give quick access to essential information and focused app interactions in contexts beyond the app itself (Home Screen, Lock Screen, Mac desktop, Apple Vision Pro surfaces, Apple Watch Smart Stack, CarPlay).

### Why
The article's recurring principle is the balance between information density and glanceability: a widget that's too sparse seems unnecessary, a widget that's too dense stops being glanceable. The insistence on dynamic content ("prefer information that changes throughout the day") stems from the observation that, if the content never changes, the person tends not to keep the widget in a prominent position. The multiple rules about rendering modes (full-color, accented, vibrant) and about how each platform applies these modes exist because the same widget needs to adapt to the appearance personalization the person chooses (light, dark, tinted, translucent light), without losing legibility or meaning conveyed only by color.

### Do and avoid
- Choose simple ideas related to the app's main purpose; include timely content and relevant functionality.
- Create a widget that gives quick access to the content the person wants; replicating the app icon adds little additional value.
- Prefer dynamic information that changes throughout the day; if the content never seems to change, the person may not keep the widget in a prominent position.
- Look for opportunities to surprise and delight, such as a unique visual treatment on special occasions.
- Offer widgets in multiple sizes when that adds value; small widgets tend to show a single piece of information, larger sizes support additional layers. Avoid simply expanding the content of a small widget to fill a larger area; it's more important to create a widget at the size that best represents the content than to offer all sizes.
- Balance information density: sparse layouts seem unnecessary, overly dense layouts are less glanceable; if the layout is too dense, consider a larger size or replacing text with graphics.
- Display only information directly related to the widget's main purpose, even in larger sizes with more data.
- Use brand elements carefully (colors, typography, stylized glyphs) to make the widget recognizable without overlapping the useful information; a small logo in the upper right corner is enough when the widget shows content from multiple sources.
- Choose between displaying content automatically or allowing personalization, depending on whether the information requires configuration (the example given is the Stocks widget, which requires choosing the symbols, versus the Podcasts widget, which displays recent content automatically).
- Avoid mirroring the widget's appearance inside the app itself, so as not to confuse the person about its behavior.
- Make it clear when authentication adds value, for example with a message like "Sign in to view reservations" when the person is signed out.

### Content update
- Keep the widget up to date, finding the appropriate frequency based on how often the data changes and when the person needs to see new data; if the person checks the widget more often than it can update, consider displaying text stating when the data was last updated.
- Use the system's functionality to update dates and times, since the widget's update frequency is limited.
- Use animated transitions to draw attention to data updates, with a duration of up to two seconds.

### Interactivity
- The person taps or clicks the widget to open the corresponding app; it can also include buttons and toggles for additional functionality without opening the app (the example given is the Reminders widget with toggles to mark tasks complete).
- Offer simple, relevant functionality, reserving complexity for the app.
- Make sure the interaction opens the app at the correct location, with a deep link direct to details and actions related to the widget's content.
- Offer interactivity while keeping the widget glanceable and organized; avoid creating app-like layouts inside the widget, and pay attention to the size of tap targets. Inline accessory widgets offer only one tap target.

### Margins and padding
- Use standard margins to ensure readability: the standard margin width for most widgets is 16 points; tighter margins of 11 points can work for groupings of content like charts, buttons or background shapes. Widgets use smaller margins on the Mac desktop and on the Lock Screen, including in StandBy.
- Coordinate the corner radius of the content with the corner radius of the widget, using a SwiftUI container (ContainerRelativeShape).

### Text in widgets
- Prefer the system font, text styles and SF Symbols; if using a custom font, use it with moderation, ensuring quick legibility (it works well to use a custom font only on large text and SF Pro on smaller text).
- Avoid very small font sizes; in general, use fonts of 11 points or larger, since text smaller than 11 points can be hard to read.
- Avoid rasterizing text; always use text elements and styles to ensure good scaling and to allow VoiceOR to read the content. In iOS, iPadOS and visionOS, widgets support Dynamic Type sizes from Large up to AX5 when using Font or custom(_:size:).

### Use of color
- Use color to enhance the widget's appearance without competing with the content.
- Convey meaning without relying exclusively on specific colors, since widgets can appear monochromatic (with or without a custom tint) and, on watchOS, the system can invert colors depending on the chosen watch face; use text and iconography in addition to color to express meaning.
- Use full-color images with judgment: when the person chooses a tinted or translucent light appearance, the system desaturates colored images by default; it is possible to choose to render images in full color even in these cases, but this draws special attention to the widget, which can look out of place. Consider reserving full-color images to represent media content (such as an album cover), at dimensions smaller than the widget's size.

### Rendering modes
- Full-color: support both light and dark appearances, preferring light backgrounds in the light appearance and dark backgrounds in the dark one; consider using the system's semantic colors for text and background, or color variants in the asset catalog.
- Accented: groups the widget's components into an accented group and a primary group. On iPhone, iPad and Mac, the system tints the primary and accented content white; on Apple Watch, it tints the primary content white and the accented content in the color of the chosen watch face.
- Vibrant: ensure sufficient contrast for legibility. In this mode, the opacity of an image's pixels determines the strength of the blurred background material effect (fully transparent pixels let the background material show through as is); the brightness of the pixels determines the vibrancy on the Lock Screen (lighter gray values give more contrast, darker values give less). Render content like images, numbers and text at full opacity; use white or light gray for the most prominent content and darker gray values for secondary elements, using opaque grayscale values instead of white opacities for the best effect.

### Previews and placeholders
- Design a realistic preview for the widget gallery, highlighting the widget's capabilities; it can display real data, but if it takes a while to load, display realistic simulated data.
- Design placeholder content that helps recognize the widget, combining static interface components with semi-opaque shapes representing dynamic content (rectangles of different widths suggesting lines of text, circles or squares in place of glyphs and images).
- Write a succinct description of the widget, starting with an action verb (examples given: "See the current weather conditions and forecast for a location", "Keep track of your upcoming events and meetings"); avoid unnecessary phrases that reference the widget itself, like "This widget shows...", "Use this widget to...", "Add this widget". Use accessible language and sentence-style capitalization.
- Group the widget's sizes and provide a single description, so it doesn't look like each size is a different widget.
- Consider coloring the Add button, after the person chooses the app in the gallery, to reinforce the brand.

### Exact specifications

Standard margin: 16 points (most widgets); tighter margins of 11 points for internal groupings.

Minimum recommended font size: 11 points.

Maximum animation duration on data update: 2 seconds.

Scale allowed for widgets in visionOS (size adjustment by the person): 75% to 125%.

iOS dimensions by screen size (portrait, pt): the table relates Small, Medium, Large, Circular, Rectangular and Inline for ten screen sizes, from 320x568 to 430x932. Examples: 430x932 screen → Small 170x170, Medium 364x170, Large 364x382, Circular 76x76, Rectangular 172x76, Inline 257x26; 320x568 screen → Small 141x141, Medium 292x141, Large 292x311 (Circular, Rectangular and Inline not available, N/A).

iPadOS dimensions: the table relates, for nine screen sizes (from 768x1024 to 1192x1590, the latter with Display Zoom on "More Space"), the Canvas and Device values for Small, Medium, Large and Extra large. Example: 1024x1366 screen, Canvas → Small 170x170, Medium 378.5x170, Large 378.5x378.5, Extra large 795x378.5; Device → Small 160x160, Medium 356x160, Large 356x356, Extra large 748x356.

visionOS dimensions (in points and in millimeters at 100% scale): Small 158x158 pt (268x268 mm); Medium 338x158 pt (574x268 mm); Large 338x354 pt (574x600 mm); Extra large 450x338 pt (763x574 mm); Extra large portrait 338x450 pt (574x763 mm).

watchOS dimensions (Smart Stack, pt): 40mm 152x69.5; 41mm 165x72.5; 44mm 173x76.5; 45mm 184x80.5; 49mm 191x81.5.

### Platform differences
- macOS: no additional considerations.
- tvOS: not supported.
- iOS, iPadOS: widgets on the Lock Screen are functionally similar to watch complications and also follow the design principles of Complications, in addition to widget principles; in many cases a design for complications also works well for widgets on the Lock Screen and vice versa. The app can offer widgets on the Lock Screen in three formats: inline text above the clock, and circular and rectangular shapes below the clock. It should support the Always-On display on iPhone, using gray levels with sufficient contrast under reduced luminance. It should consider offering Live Activities for real-time updates, since widgets don't show real-time information; widgets and Live Activities share frameworks and design similarities, and it's good practice to develop them together.
  - StandBy and CarPlay: on iPhone in StandBy, the system displays two small widgets from the system family side by side, enlarged to fill the Lock Screen. Supporting StandBy also ensures good functioning in CarPlay, which uses the same small widget with the background removed, enlarged to fit the Widgets screen grid. Limit the use of rich images or color to convey meaning in StandBy; instead, take advantage of the extra space by enlarging and reorganizing text, and don't use background colors to blend with the black background. In low-light conditions in StandBy, the system renders the widgets in monochromatic appearance with a red tint.
- visionOS: widgets are 3D objects that the person positions on a horizontal or vertical surface; the widget persists in position even when Apple Vision Pro is turned off and back on, with scale consistent to the real world. They appear in full color by default, but switch to accented mode when the person customizes with tint colors from palettes provided by the system; it's possible to customize the frame width of widgets in the elevated style. There are no system-level light/dark appearances in visionOS (exception cited: the Music poster widget offers its own light/dark theme option generated from the album art). Design should be adapted to the spatial context (living rooms, kitchens, offices), testing across the full range of the system's color palettes and lighting conditions.
  - Thresholds and sizes: two distance thresholds, simplified (viewing from a distance) and default (viewing up close). At the distance threshold, show a simplified version with fewer details, larger typography and no interactive elements; up close, show more detail with smaller typography, keeping shared elements between the two thresholds for continuity. Choose the widget family size suited to the real context where the person will place it (table, wall, sideboard).
  - Mounting styles: elevated (default, works on horizontal and vertical surfaces, tilts slightly backward on horizontal surfaces and casts a soft shadow; on vertical surfaces it can sit flush, like a picture frame) and recessed (only on vertical surfaces, the content appears recessed into the surface, creating a cutout-like depth effect). Choose the style based on the content: elevated for content that should stand out (reminders, media, glanceable data); recessed for immersive or ambient content (weather, editorial content). It's possible to restrict the widget to a single supported style.
  - Treatment styles: paper (printed appearance, more solid, responds to ambient light by darkening or lightening; the example given is the Music poster widget) and glass (layered appearance, visually separates foreground and background, keeping foreground elements always bright and legible regardless of ambient light; the example given is a news widget with editorial background images and sharp headlines in the foreground).
- watchOS: by default widgets in the Smart Stack use a black background; consider a custom background color that conveys additional meaning (the example given is the Stocks app using a red background for a drop and green for a rise). It's possible to encourage the system to display or raise the widget's position in the Smart Stack by providing relevance information (based on location or on system actions in progress, such as a workout).

### Links to other articles
Layout, Dark Mode, Complications, Live Activities, StandBy, CarPlay.

---

<!-- visual:widgets -->
### What the illustrations show
Basis: 10 illustration sheets viewed (38 images, all recorded as light appearance), codes checked; no videos.
- The Calendar widget's size progression is made by adding columns, not by increasing font size: the small shows only the day and two events; the medium has the same height and double the width, with today and tomorrow in two columns; the large adds a vertical hour ruler with a red line at the current time and events positioned over it; the extra large extends the ruler to four days, with today's column visibly wider. The events always follow the same pattern of a lilac bar with a colored vertical stroke on the left (img 1287, img 1288, img 1289 and img 1290). The Music extra large portrait, in turn, stacks blocks, cover art in the upper half and metadata in the lower half over a light background (img 1291).
- The accessory formats swap the card for their own shapes with adapted typography: circular with a small icon over a translucent circle and only the time of the next event; corner with curved text following the arc of the watch face, time in white and title in red over black; inline as a single line in a translucent band, with no card; rectangular with two stacked event lines (img 1292, img 1293, img 1294 and img 1295). On the iPhone Lock Screen, the inline text sits above the large clock and the circular widgets below it (img 1316).
- The same small Stocks widget, with the same layout, changes only color and opacity between appearances: in full color it keeps the black background and the semantic green for a gain; in light it becomes desaturated and translucent, letting the background show through; tinted applies a single purple to background, text and chart, erasing the green; on the iPad Lock Screen it becomes monochromatic brown over a brown background (img 1296, img 1297, img 1298 and img 1300).
- On Apple Vision Pro the widget becomes an object with a thick white frame, shadow and depth, preserving the full colors; in StandBy it appears larger, in monochromatic red over total black (img 1299, img 1301 and img 1302).
- On Apple Watch the same event card takes on three treatments: a band with a textured beige background and a light pink stroke separating time and title; a rectangular complication with a solid black background, red stroke and white and gray text; in the Smart Stack, a light card with a red stroke floating, standing out over the black around it (img 1303, img 1304 and img 1305).
- The small Weather widget shows the typographic hierarchy: small location with icon at the top, huge temperature in the center, condition and high and low smaller at the bottom, over a blue gradient (img 1306).
- The toggle state is shown by the same Reminders widget side by side: seven tasks with empty circles and, in the other version, the first and third circles filled in solid red, with no other layout change (img 1307 and img 1308). The medium watchlist widget aligns each row in three columns, name, small green chart and value with variation (img 1309).
- In full color, the light and dark versions of the Notes widget swap only the body background and the text color (white with black text, black with white text); the yellow brand bar at the top remains identical (img 1310 and img 1311).
- The placeholder uses the same geometry as the final content: three lighter yellow bars of decreasing widths on the yellow card become the three lines of real text in the loaded version (img 1312 and img 1313).
- In the gallery, a modal card rises from the bottom with title, description, widget thumbnail, page indicator and an "Add Widget" button in the app's brand color, yellow in Notes and blue in Weather (img 1314 and img 1315).
- StandBy pair: right is the analog clock and Weather in white over black, with no card or frame, with a green check badge; wrong is Weather keeping the rounded blue card with the Home Screen shadow, standing out from the black, with a gray X badge. In low light everything turns monochromatic red, including the watch face numbers (img 1317 to img 1321).
- In visionOS, the same scene in a white frame in perspective adapts density to distance: seen from afar it has cover art and small text with no track list; seen up close the card becomes larger and gains an extra block with four lines of track names (img 1322 and img 1323).
Recorded divergences: the captions distinguish standard StandBy and low-light StandBy for img 1301 and img 1302, but the notes record that the difference is not distinguishable to the eye; both use the same red over black.
<!-- /visual:widgets -->

## What this group reveals about the Apple way

1. Strict honesty of state: in almost every article in the group (controls, complications, notifications, widgets, live-activities) there is the same underlying rule, the component needs to reflect the real, current state, never a frozen or misleading state; badges only count unread notifications, complications must not be static, controls need to update after every interaction. Supported by: controls, complications, notifications, widgets.

2. Privacy as a design constraint, not just a policy one: several components are exposed to other people's eyes (Always-On display, Lock Screen, short glances at the wrist) and the design response is always the same, redact/hide sensitive information and show only an innocuous summary, leaving the detail inside the authenticated app. Supported by: complications, live-activities, notifications, controls.

3. Spoken text (Siri) and visual text are not interchangeable: in both App Shortcuts and Snippets, Apple explicitly separates what Siri says from what appears on screen, even recommending omitting the dialogue from the visual representation so as not to duplicate information. Supported by: app-shortcuts, snippets.

4. Physical geometry dictates layout rules: the rounded shape of the Dynamic Island (around the TrueDepth camera) and the corner radius of widgets generate extremely specific rules for concentric margins, blur to align edges, and the use of ContainerRelativeShape, showing that the device's physical hardware directly shapes the HIG rules, not just abstract UI conventions. Supported by: live-activities, widgets.

5. Numeric specification changes granularity according to the risk of error: highly geometric components replicated across many screen sizes (complications, widgets, top-shelf, live-activities) come with extensive tables of points and pixels per device size; more conceptual components without fixed geometry (notifications, status-bars, watch-faces, controls) bring no numeric value at all. Supported by: complications, widgets, top-shelf, live-activities, notifications, status-bars, watch-faces, controls.

6. Recurrence of the "less is more useful" principle: all glanceable components in the group (widgets, complications, live-activities, notifications) share the same warning, show only the essential information, with a deep link to the app when more detail is needed; excess density is treated as a design failure, not as a feature. Supported by: widgets, complications, live-activities, notifications.

7. The brand must appear without competing with function: in controls, live-activities, widgets and top-shelf, Apple allows the use of brand color and visual identity, but always with the caveat that the brand cannot obscure functional information or imitate system components (for example, not replicating the appearance of a badge, not using the app's full icon as a logo mark). Supported by: controls, live-activities, widgets, top-shelf.

8. Cross-device modularity as a design requirement, not an add-on: Live Activities and widgets need to be designed from the start for multiple presentations (compact, minimal, expanded, Lock Screen, StandBy, CarPlay, watchOS, visionOS), and the text explicitly recommends starting with iPhone and then adapting, instead of designing each platform in isolation. Supported by: live-activities, widgets, complications.

9. Where action is possible, it should be minimal and singular: controls, notifications and live-activities recommend limiting interactivity to a few elements (ideally one), with a preference for non-destructive actions and for avoiding "app-like" layouts inside a component that should be glanceable. Supported by: controls, notifications, live-activities, widgets.

10. Technical legacy is treated with pragmatism, not hidden: in both complications and App Shortcuts there is explicit acknowledgment of earlier frameworks (ClockKit, legacy templates) and clear migration guidance (prefer WidgetKit, prefer app schemas over individual App Shortcuts when applicable), showing that the HIG documents the technological transition, not just the final ideal state. Supported by: complications, app-shortcuts.

## Reading evidence

| File | Lines read | Read to the end |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/app-shortcuts.md | 64 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/complications.md | 224 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/controls.md | 60 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/live-activities.md | 270 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/notifications.md | 90 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/snippets.md | 49 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/status-bars.md | 22 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/top-shelf.md | 84 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/watch-faces.md | 26 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/widgets.md | 285 | yes |

All 10 files in the group were read in full in a single Read call each, with no sign of truncation (no file came close to the standard reading limit). No article in this group is merely a collection index page with no text of its own.
