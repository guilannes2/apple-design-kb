# Patterns (part 1)

Knowledge base about the interaction pattern articles from the Apple Human Interface Guidelines: data presentation, collaboration, drag and drop, entering data, feedback, file management, full screen, launching apps, live viewing, loading, accounts, notifications, modality, multitasking, help, onboarding, audio, haptics, video, printing, ratings, and search.

## Charting data (slug: charting-data)

What it governs: how and when to use charts to communicate data clearly, instead of dumping text or tables.

Why: a chart draws visual attention, so Apple treats that prominence as something to be used responsibly, communicating exactly what the person needs to learn about the data that matters to them. The central idea is gradualness: reveal complexity gradually, and examine the data at multiple levels (macro, subsets, individual points) to discover what is worth highlighting.

Do and avoid:
- Use a chart when you want to highlight important information from a data set; if you only need to offer the data without analysis, prefer a searchable, sortable list or table.
- Keep the chart simple; let the person choose when they want more detail, instead of packing everything in at once.
- Make every chart accessible, with accessibility labels that describe values and components, plus accessibility elements for interaction.
- Prefer common chart types (bar, line) because people already know how to read them; if you invent a new type, teach how to interpret it (the example cited is the individual animation of the Activity Rings when pairing the Watch with the iPhone).
- Examine the data at the macro level (totals, averages), the middle level (useful subsets), and the individual level (specific points) to enrich the chart.
- Add descriptive text (titles, subtitles, annotations) to reinforce what is actionable; descriptive text does not replace accessibility labels.
- Size the chart according to functionality, theme and level of detail: large enough for detail and interactivity, small when it is only a glanceable preview.
- Maintain visual consistency between multiple charts in the app, changing type or style only to highlight real differences.
- Maintain continuity (same type, colors, annotations, layout, text) between charts that represent the same data set at different levels of detail.

Exact specifications: the text does not include specific numbers, measurements or proportions.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: Charts (related component).

<!-- visual:charting-data -->
### What the illustrations show
Basis: 1 illustration sheet (img 0231 to 0233) viewed, code checked; the page has no video.
- The opening is a sketch of a bar chart: four vertical bars that rise and then fall, resting on a baseline, in dark red outline over an orange gradient, with a dashed grid and a construction guide circle (img 0231).
- In Stocks, the AAPL detail screen shows price and change, a period selector with "1M" marked and a single filled green line chart for that period, with a horizontal axis of days (23, 30, 7, 14, 21) and a vertical price axis from 277 to 312 (img 0232).
- In Health, the Activity screen opens with the colored ring and three numeric metrics (Move, Exercise, Stand) and then stacks three vertical bar charts, one per metric, each with its own color (red, green and cyan), its own vertical scale and the same hour-of-day axis; a block of "About Activity" text closes the screen (img 0233).
- The two screenshots show two approaches to presenting data: a single detailed line chart, with a selectable period (img 0232), against three smaller, parallel bar charts, each with its own scale, that summarize different metrics for the same day on the same screen (img 0233).
<!-- /visual:charting-data -->

## Collaboration and sharing (slug: collaboration-and-sharing)

What it governs: how to offer real-time sharing and collaboration using the system interfaces (share sheet, sharing popover, collaboration button) and the integration with Messages.

Why: Apple wants collaborating to feel like a natural extension of the system, not an isolated feature of the app. The reasoning is to reduce friction in setup (simple permissions, summarized in phrases) and to keep people aware, via the collaboration button and notifications in Messages, that the content is shared and of who is involved.

Do and avoid:
- Place the Share button in a convenient location, such as a toolbar, to make it easy to start sharing.
- Customize the share sheet or the sharing popover only if necessary, to offer the file-sharing types the app supports.
- Write concise phrases that summarize the sharing permissions, such as "Only invited people can edit" or "Everyone can make changes".
- Offer a simple set of sharing options; keep the number of custom choices to a minimum and group them clearly.
- Display the Collaboration button prominently as soon as collaboration begins, typically next to the Share button.
- Offer custom actions in the collaboration popover only if necessary; the middle section is for custom items, without overloading it with information.
- Customize the title of the collaboration management button of the modal view if it makes sense in the app (the default is "Manage Shared File").
- Consider posting collaboration event notifications in Messages, including a universal link to the relevant view in the app.

Exact specifications: the text does not include specific numbers, measurements or proportions.

Platform differences:
- iOS, iPadOS, macOS: no additional considerations beyond the general ones. Starting with iOS 16, the system share sheet includes ways to choose the file-sharing method and set permissions; iPadOS 16 and macOS 13 bring similar appearance and functionality in the sharing popover.
- tvOS: feature not available.
- visionOS: by default, the system supports screen sharing for an app running in the Shared Space, streaming the current window to other collaborators; if someone transitions the app to a Full Space during sharing, the system pauses the stream for the other people until the app returns to the Shared Space.
- watchOS: in a SwiftUI app, use ShareLink to present the system share sheet.

Links to other articles: Activity views; SharePlay (for real-time activities across devices); Managing accounts (related to authentication and permissions, mentioned indirectly).

<!-- visual:collaboration-and-sharing -->
### What the illustrations show
Basis: 2 illustration sheets (img 0246 to 0251) viewed, codes checked; the page has no video.
- The opening shows a thick dark red stroke circle, open on one side, with a person icon inside and a smaller circle filled with a white check overlapping at the base, over an orange gradient with a dashed grid and a guide circle (img 0246).
- The five screenshots reuse the same document from the notes app on iOS, "Nature Walks", with the same leaf drawing and handwritten annotations, and change only the overlaid controls; the didactic focus stays on the interface elements, not on the content (img 0247 to img 0251).
- The Share button sits in the top right corner, next to the "..." button, in a top bar that also carries the back arrow, with the large title below (img 0247).
- The share sheet opens below the title with, in order, a "Collaborate" selector accompanied by the permission phrase and a disclosure arrow, four collaborator avatars with initials and a green status dot, and two rows of four actions each: AirDrop, Messages, Mail and Reminders; Copy, Export as Markdown, Markup and More (img 0248).
- The permission phrase is taught through a pair with identical layout, the same avatars and the same actions, changing only the summary in the same place above the avatars: "Only invited people can edit." and then "Everyone can make changes." (img 0248 and img 0249).
- With collaboration active, an orange circular button with a two-people icon appears in the top bar, to the left of Share and "...", with prominence like that of Share (img 0250).
- This button's popover is organized into three vertical blocks: at the top, message, video and audio tabs, with the message tab selected in orange; in the middle, "Latest Updates" and "Current Participants" with empty-state text; at the bottom, a green toggle switched on for "Participant Cursors" and list items with an icon on the right, "Show All Activity", "Show Highlights" and "Manage Shared Note" (img 0251).
<!-- /visual:collaboration-and-sharing -->

## Drag and drop (slug: drag-and-drop)

What it governs: how to implement drag and drop (moving or copying selections of photos, text and other content) between source and destination, within the same container, across different containers or between apps.

Why: the logic of moving versus copying follows what people already expect from the physical world and from other systems: the same container tends to move, different containers tend to copy, and between apps it always copies. Continuous feedback during the drag exists so that the person feels in control of a process with multiple possible outcomes.

Do and avoid:
- Support drag and drop as much as possible throughout the app; system components (text fields and text views) already come with built-in support.
- Offer alternative ways to perform the same action (menu commands) when drag and drop is inconvenient or impossible; in iOS/iPadOS, use accessibility APIs to allow drag and drop via assistive technologies.
- Decide move vs. copy according to what most people expect: the same container tends to move, different containers tend to copy; prefer the behavior least prone to frustration or data loss.
- Support dragging multiple items when it makes sense; in iPadOS the person can add items to the group without stopping the drag.
- Prefer allowing a drag-and-drop operation to be undone; ask for confirmation before completing operations that cannot be undone (example: Finder asks for confirmation when dragging a file into a write-only folder).
- Consider offering multiple versions of the dragged content, from the highest to the lowest fidelity, so the destination can choose the best version it accepts.
- Consider supporting spring loading, which allows activating controls (buttons, segmented controls) by dragging the selected content over them.
- Show a translucent drag image as soon as the person drags the selection about 3 points; keep it until the drop.
- Modify the drag image to preview the outcome, if it helps clarity; use drag flocking to visually group multiple dragged items.
- Show whether a destination can accept the dragged content (insertion point, highlight, or a "not allowed" symbol such as `circle.slash` from SF Symbols); remove the feedback when the content moves away from the destination.
- When the drop fails or lands on an invalid destination, give visual feedback (returning to the source, or a scale/fade suggesting evaporation).
- When accepting drops: scroll the destination content automatically when necessary; choose the richest version of the content that the app accepts; extract only the relevant part of the content (example: Mail extracts only the name and email from a dragged contact); check the Option key at the moment of the drop (forces copy behavior within the same container); give feedback when the transfer of the dropped content takes a while; give feedback when the drop starts a task (such as printing); apply the correct style to the dropped text (keeping the original font/style when both support it, or applying the destination's style); keep the content's selection state at the destination after the drop, updating the source as needed.

Exact specifications: display the drag image as soon as the person drags the selection by about 3 points.

Platform differences:
- Not supported on tvOS or watchOS.
- iOS, iPadOS: allow multiple simultaneous drag activities; on iPadOS the person can select an app icon, start dragging and select additional icons before dropping all of them on a different Home Screen or in a folder, requiring support for adding items during the drag (with flocking) and accepting multiple simultaneous drops.
- macOS: consider allowing dragging app content to the Finder, in a format the app can reopen later (example: Calendar drags an event as an `.ics` file); it is possible to use a clipping (temporary container) for dragged content, which has no relation to the Clipboard; allow dragging a selection in an inactive window (background selection) without bringing the window to the front; when possible, allow dragging individual items from an inactive window without affecting the existing background selection; consider displaying a badge (filled oval with a number) during multi-item drag operations; consider changing the pointer's appearance (copy, drag link, item disappearing, operation not allowed) according to the situation; as much as possible, allow selecting and dragging with a single movement.
- visionOS: when possible, launch the app to handle content dropped in empty space, associating a user activity with the draggable content (example: dropping a URL in empty space opens Safari; content supported by Quick Look opens Quick Look).

Links to other articles: Universal Control (dragging content between Mac and iPad); Pointers (pointer appearance on macOS).

<!-- visual:drag-and-drop -->
### What the illustrations show
Basis: 1 illustration sheet (img 0470) and 2 video sheets (video 008) viewed, codes checked.
- The opening sums up the gesture with two shapes and a cursor, with no text: two rounded rectangles of the same size partially overlapping and a large pointer arrow in the lower right of the composition, pointing up and to the left, into the pair, over an orange gradient with a dotted grid and guide circle (img 0470).
- In video 008 (sheet 0001, q001 to q003), the starting point on visionOS is a Files window with the Recents list showing the file "meteor.usdz", with size and date, and a context menu open next to it, all over the real room in the background.
- From q003 to q004 the menu disappears, the window switches to showing a grid of thumbnails with Select and Search buttons, and the file's white square icon appears crossing the right edge of the panel.
- In q005 the icon has already detached from the window and floats alone over the room, without any app frame; at the same time the source grid switches to showing only three files, without the meteor.
- From q005 to q008 the icon moves continuously through the air, goes near the arm of the sofa, descends toward the center of the table and stabilizes just above the tabletop; in q009 it gains the label "meteor" and a small blue indicator, which suggests the system recognized the drop point.
- In sheet 0002, the file first lands as a flat labeled card on the table (q010); then a small rocky 3D object is born above it (q011) and grows, gaining craters and texture (q012).
- From q013 to q015 the meteor keeps floating above the table, without resting on it, and rotates slowly showing other faces, while the label and indicator remain visible on the tabletop below.
Recorded divergences: the alt text of img 0470 speaks of an arrow pointing to the upper left corner, but the artwork shows a mouse cursor, not a separate directional arrow. The official description of video 008 checks out in essence, but does not mention the context menu before the drag (q001 to q003), the flat labeled card stage before the 3D object (q009 to q010), nor the meteor's continuous rotation at the end (q013 to q015).
<!-- /visual:drag-and-drop -->

## Entering data (slug: entering-data)

What it governs: how to design data entry to reduce tedium and error, whether by pre-filling information already available in the system, or by supporting all available input methods.

Why: entering data is tedious regardless of the method; Apple prioritizes minimizing the volume of data the person needs to provide manually and validating early to avoid the frustration of correcting errors only at the end of a long form.

Do and avoid:
- Get information from the system whenever possible (settings, location permission, calendar) instead of asking the person to type it.
- Be clear about the data needed, using a prompt in the field (like "username@company.com") or an introductory label ("Email"); you can pre-fill with reasonable default values.
- Use a secure text field when appropriate, for sensitive data, typically displaying a small filled circle per character typed.
- Never pre-fill a password field; always ask the person to type it or use biometric or keychain authentication.
- When possible, offer choices (picker, menu, selection component) instead of requiring text typing.
- Let the person provide data by dragging and dropping or pasting, when it makes sense.
- Dynamically validate field values as soon as the person enters them, giving feedback as soon as it detects a problem; for numeric data, consider a number formatter that accepts only numeric values and can format them (decimal places, percentage, currency).
- When data entry is required, make it clear that the person must fill in what's mandatory before proceeding (for example, disabling a Next or Continue button until the fields are filled in).

Exact specifications: the text does not bring specific numbers, measurements or proportions.

Platform differences:
- iOS, iPadOS, tvOS, visionOS, watchOS: no additional considerations.
- tvOS: you can configure a digit entry view to hide the typed digits (`isSecureDigitEntry`). On visionOS, when using the system's text field, the system shows the typed data only to the person using the device, not to others present; a secure text field automatically blurs when using AirPlay.
- macOS: consider using an expansion tooltip to show the full version of text that is cut off or truncated in a field, when the field is too small to display the entire data.

Links to other articles: Managing accounts (never pre-fill password); Text fields; Virtual keyboards; Keyboards; Offering help (expansion tooltip on macOS/visionOS).

<!-- visual:entering-data -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0472), code checked; the page has no video or interface screen capture.
- The opening represents data entry in an abstract way: a rectangular text field with rounded corners with three filled dots inside, in dark red artwork over an orange gradient (img 0472).
- A tilted pencil overlaps the upper right corner of the field, with its tip touching the interior, indicating the action of writing or editing (img 0472).
- The composition follows a dotted grid and a central guide circle: the body of the field is inscribed in the circle, and only the pencil crosses that boundary at the upper right, which gives a sense of movement entering the field (img 0472).
<!-- /visual:entering-data -->

## Feedback (slug: feedback)

What it governs: how to communicate status, success/failure, warnings and opportunities for correction as the person interacts with the app.

Why: the central principle is to match the importance of the information with the level of interruption of the delivery. Passive status can be passive in its presentation; a risk of data loss needs to interrupt, because the person only has a chance to avoid the problem if warned in time.

Do and avoid:
- Make all feedback accessible, using multiple channels (color, text, sound, haptics), to reach more people in different contexts (muted, looking away, using VoiceOver).
- Consider integrating status feedback directly into the interface, near the items it describes, instead of requiring action or leaving the current context (example: Mail shows the unread message count in the toolbar).
- Use alerts to deliver critical and, ideally, actionable information; alerts lose impact if used in excess or for unimportant information.
- Warn when the person starts a task that can cause unexpected and irreversible data loss; do not warn when data loss is the expected result of the action (example: Finder does not warn every time the person throws a file away).
- When it makes sense, confirm that a significant task or action was completed (example: confirmation of a successful Apple Pay transaction); reserve this type of confirmation for sufficiently important activities, since people normally expect the action to succeed.
- Show when a command cannot be executed and help the person understand why (example: Maps warns that it cannot give directions between the same origin and destination location).

Exact specifications: the text does not bring specific numbers, measurements or proportions.

Platform differences:
- iOS, iPadOS, macOS, tvOS, visionOS: no additional considerations.
- watchOS: avoid displaying an indeterminate progress indicator (like a loading indicator) in a watchOS app; an animated indicator can make the person think they need to keep paying attention to the screen. Prefer ensuring they will receive a notification when the process finishes.

Links to other articles: Playing audio; Playing haptics; Motion; Alerts.

<!-- visual:feedback -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0478), code checked; the page has no video or interface screen capture.
- The opening is a card with rounded corners with an orange gradient, lighter at the top left and darker and reddish at the bottom right, with no device frame, no text and no interface elements (img 0478).
- The concept is drawn as a dark red arrow pointer surrounded by six short strokes in a radial arrangement, suggesting the response to a click (img 0478).
- The construction is left exposed: a dashed rectangular mesh in the background, apparently three columns by three rows, and a dashed circle concentric with the pointer, with the ring of strokes centered exactly on the arrow's axis (img 0478).
<!-- /visual:feedback -->

## File management (slug: file-management)

What it governs: how apps that handle documents and files should integrate with the system's file navigation (Finder on Mac, Files on iPhone/iPad/Vision Pro), create, open, save and present file previews.

Why: Apple starts from the principle that people already have a mental model of the platform's file system (via Finder or Files), so a custom file browser should respect that basic layout instead of reinventing it. For saving, the philosophy is that the person's work should always be preserved by default, without requiring an explicit "save" action.

Do and avoid:
- Use the app's menus and keyboard shortcuts to create and open documents; on iPadOS and macOS, offer familiar commands like New and Open; include an Add (+) button to create a new document (on macOS, the add action goes in the File menu).
- If you need a custom file browser, respect the person's understanding of the platform's file system; you can show the most relevant part when opening (Documents folder, iCloud, most recent location), but allow navigating the rest of the file system.
- Help the person trust that their work is always preserved, unless they cancel or delete; in general, avoid requiring an explicit save action, making periodic automatic saves while editing and when closing the file or switching apps.
- Hide file extensions by default, but let the person choose to see them; reflect the current choice across all save or open interfaces.
- Use a Quick Look viewer to allow previewing a file even when the app can't open it.
- Consider implementing a Quick Look generator if the app produces custom file types, so Finder, Files and Spotlight can show previews of the documents.

Exact specifications: the text does not give specific numbers, measurements or proportions.

Platform differences:
- tvOS, visionOS, watchOS: no additional considerations (watchOS and tvOS typically don't have a document navigation interface).
- iOS, iPadOS: starting with iOS 18 and iPadOS 18, document-based apps can use the system document launcher, a full-screen experience with three parts: a title card (app name and two app-specific buttons), a background image with optional accessories around the title card, and a sheet with the file browser and optional app controls. The title card's primary button typically creates a new document; the secondary one can offer additional options (example: Numbers uses "Start Writing" and "Choose a Template"). The background should be clearly distinct from the accessories and the title card (solid color, gradient or pattern), avoiding complex images. Be careful with the positioning of the accessories to keep the app name and buttons visible. Use animation with restraint (smooth, repetitive animations). An app can also create a file provider app extension to import, export, open and move documents, showing only documents appropriate to the current context, allowing a destination to be chosen when exporting/moving, and avoiding a custom toolbar inside the extension (which already carries its own toolbar in the modal view).
- macOS: prefer the standard file browser (Finder) to a custom one, unless there's an important reason for your own; a custom one can include "open recent", filtering by criteria, multiple selection, and customization of the Open button's title (for example, "Insert"). Provide a save interface that allows changing the file's name, format and location (default title "Untitled" until named); you can extend the Save dialog with an accessory view of app-specific options. You can create a Finder Sync app extension to express sync status and control within Finder (badges, contextual menu items, toolbar buttons for global sync). Help avoid loss of work if the person turns off autosave (the "Ask to keep changes when closing documents" option in Desktop & Dock settings): show that the document has unsaved changes and present a save dialog when closing, quitting the app, logging out or restarting; use a dot on the document window's close button and next to the name in the Window menu when autosave is off (don't show it when autosave is on); you can add "Edited" to the title in the title bar, removing it as soon as autosave occurs or the person saves explicitly.

Links to other articles: Toolbars; File menu; Printing; Documents, SwiftUI (developer documentation).

<!-- visual:file-management -->
### What the illustrations show
Basis: 1 illustration sheet (img 0479 and img 0480) viewed, code checked; the page has no video.
- The opening is a document with the top right corner folded inward, in a thick dark red outline with no fill, centered at the crossing of the guides and inscribed in the dashed circle, over the orange card with a rectangular and circular grid (img 0479).
- The document launcher on iPad in landscape occupies the screen in two parts: on top, a title card with its own lilac gradient background and organic shapes; below, a sheet with the file browser (img 0480).
- The accessories sit on the sides of the title: a robot mascot on the left and a branch of stylized flowers on the right, with the app name in large black typography at the center (img 0480).
- The primary action is a solid blue button, "Start Writing", right below the app name, standing out against the illustrated background (img 0480).
- The sheet uses a neutral white background and standard controls: Recents, Shared and Browse text tabs, with Browse selected in blue, view, folder, grid and search icons in the top right corner, the app name repeated in the header with a chevron and "+ Create Document" as the only item in the list (img 0480).
- The screen separates into layers what is the app's brand (illustrated background, mascot, title and primary button) from what is a standard system control (neutral file browser at the bottom) (img 0480).
<!-- /visual:file-management -->

## Going full screen (slug: going-full-screen)

What it governs: how and when to offer full screen mode on iPhone, iPad and Mac, expanding a window to occupy the whole screen and offer a distraction-free environment.

Why: full screen mode serves concentration and immersion (games, media, complex tasks). The underlying principle is to preserve essential access: even in full screen, the person should not lose access to necessary controls or feel like they've lost control over when to exit the mode.

Do and avoid:
- Support full screen mode when it makes sense: games, media viewing (videos, photo slideshows), or in-depth tasks that benefit from a distraction-free environment.
- If necessary, adjust the layout in full screen mode, but don't resize the window programmatically; keep essential content prominent and adjustments subtle enough to not cause visually abrupt transitions.
- Keep giving access to essential resources and controls so the task can be completed without leaving full screen (example: a full-screen media experience needs to keep playback controls persistently available or easy to reveal).
- Except in games, allow the Dock to be revealed while the iPadOS or macOS app is in full screen; to prevent accidental reveal during a game, you can ask iPadOS to ignore an initial swipe from the bottom edge, or hide the Dock entirely on macOS.
- After the person switches to another app and comes back, help them resume where they left off (for example, a game or slideshow should pause automatically when exiting).
- Let the person choose when to exit full screen mode; don't expect it to end automatically when switching apps or finishing an absorbing activity.
- Prioritize content by temporarily hiding toolbars and navigation controls; allow the hidden elements to be restored with a familiar gesture (tapping, swiping down, or moving the cursor to the top); keep controls visible when they're essential for navigation or tasks.

Exact specifications: the text does not give specific numbers, measurements or proportions.

Platform differences:
- Not supported on tvOS, visionOS or watchOS (Apple TV and Apple Watch already fill the screen by default; Apple Vision Pro has no full screen mode because the person can expand the window or use the Digital Crown for a more immersive experience).
- iOS, iPadOS: consider deferring system gestures to avoid accidental exits; by default, the Home Screen indicator hides shortly after switching to the app and reappears when interacting with the bottom of the screen, allowing a swipe to exit; if this results in unexpected exits, it's possible to enable two swipes instead of one.
- macOS: use the full screen experience provided by the system (ensures compatibility with, for example, the camera housing area on some Mac models). In a game, don't change the display mode when entering full screen (the person expects to control the display mode). Always let the person choose when to enter full screen, preferring the window's Enter Full Screen button, the View menu item, or the Control-Command-F shortcut; avoid a custom menu of window modes; in a game, you can offer a custom toggle that turns full screen on and off.

Links to other articles: Layout; Multitasking; Windows; The menu bar; Immersive experiences (visionOS).

<!-- visual:going-full-screen -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0536), code checked; the page has no video or interface screen capture.
- The opening is a gradient card that goes from orange yellow, on the left, to reddish orange, on the right, with the rectangular and circular construction grid overlaid (img 0536).
- The idea of expansion is drawn with two thick red arrows pointing outward in opposite directions: the one at top left points up and to the left, the one at bottom right points down and to the right (img 0536).
- The two arrows sit on the same diagonal, from the top left corner to the bottom right, and this line crosses the center of the guide circle (img 0536).
Recorded divergences: the official alt text describes the arrows on a vertical line, but in the image the line joining them is clearly diagonal.
<!-- /visual:going-full-screen -->

## Launching (slug: launching)

What it governs: how to design the app or game's start, from the opening tap to the first screen being ready, including the launch screen when required by the platform.

Why: the central philosophy is that launching needs to be instantaneous and imperceptible. The launch screen is not a moment for brand expression; its only function is to reinforce the perception of speed, so it should be nearly identical to the actual first screen, to avoid creating an unpleasant flash in the transition.

Do and avoid:
- Launch instantaneously; people sometimes don't want to wait more than a few seconds.
- If the platform requires it, provide a launch screen (iOS, iPadOS, tvOS); macOS, visionOS and watchOS don't require one.
- If you need a splash screen, consider displaying it at the start of the onboarding flow, or right after launch finishes if there is no onboarding.
- Restore the previous state when relaunching the app, so the person continues where they left off; restore granular details as much as possible (scroll position, window state and location).
- For the launch screen: don't make it part of an onboarding flow or a splash screen, and it is not an opportunity for artistic expression; design it nearly identical to the actual first screen (same solid color if applicable, same current orientation and appearance mode of the device); avoid including text, since the launch screen's content doesn't change and isn't localized; don't make it promotional, avoiding looking like a splash screen or an "About" window, with no logos or brand elements unless they are a fixed part of the first screen.

Exact specifications: the text does not give specific numbers, measurements or proportions (only "no more than a few seconds", without an exact value).

Platform differences:
- macOS, watchOS: no additional considerations (they do not require a launch screen).
- iOS, iPadOS: launch in the appropriate orientation; if the app supports portrait and landscape, launch in the device's current orientation; if the interface runs in only one orientation, launch in that orientation and let the person rotate the device if necessary; landscape-only interfaces need to respond correctly regardless of whether the person rotates left or right.
- tvOS: unlike the layered images used in much of a tvOS app, the launch screen is static; in a live-viewing app, consider starting playback automatically shortly after opening the app, after a few seconds of inactivity.
- visionOS: consider launching in the Shared Space even if the app is fully immersive, giving more context about the app while it loads and allowing you to present a control to open the fully immersive experience.

Links to other articles: Onboarding; Loading; Layout; Live-viewing apps.

<!-- visual:launching -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0679), code checked; the page has no video or interface screen capture.
- The opening shows a square with rounded corners with an arrow inside pointing to the upper right corner, suggesting the transition to a new state (img 0679).
- The drawing is done in solid dark red over the orange gradient card, which gives strong contrast between the shape and the background (img 0679).
- The composition relies on the grid of rectangular dotted lines and a central alignment circle, the same construction system as the openings of other sections (img 0679).
Recorded divergences: the official description mentions only the overall orange tinting and does not note that the square and the arrow are dark red.
<!-- /visual:launching -->

## Live-viewing apps (slug: live-viewing-apps)

What it governs: how to prioritize and present live content in TV/streaming apps, including the electronic program guide (EPG) and cloud DVR recording.

Why: the premise is that whoever opens a live-viewing app came to watch, so every design decision aims to reduce the interval between opening the app and seeing the content play, and to make it clear, at any moment, that that content is live (different from VOD).

Do and avoid:
- Highlight live content with prominence and easy access; if it is on the first tab, the person does not need to tap more than once to start watching.
- Let the person tap once, or not at all, to start playback (example: a Watch Now button over the featured content, which disappears and starts full-screen playback immediately).
- Make live content feel live: playing the content is the best way, but it also helps to mark it somehow (badge, symbol, sash) in a collection titled "Live".
- Consider indicating the progress of the live content playing, via a progress bar or other indicator, so the person knows where they will "land".
- Give additional actions and viewing alternatives (record, restart, download, favorite), always in the same order throughout the app (example: Watch, Start Over, Record, Favorite); if the content reappears at other times, show that information.
- Consider using a content footer to navigate between channels during playback, with subtle treatment (darkening) to keep text legible; clearly identify the thumbnail of the content playing now (badge or tint on the progress bar); match the footer categories with those of the EPG; design a simple and predictable way to invoke and dismiss the footer (example: if swiping up invokes it, swiping down dismisses it).
- Give instant visual feedback when switching channels, both to confirm the right channel and to give time for loading.
- Match the audio with the current context: when live content starts playing, the audio should continue even when navigating in the background, but stop when the person leaves the live tab.
- In the EPG: prominently display the current information (program, channel, time) and make it easy to return to playback; make navigation effortless (pagination, scroll, jump); consider a "My Channels" or "Favorites" group; group content into familiar categories (Movies, TV Shows, Kids, Sports, Popular), using the same categories in the content footer; allow navigating the EPG without leaving the current content (picture-in-picture or background playback).
- In cloud DVR: allow starting/stopping recording from the info panel; allow scheduling recording of a future program in a detail view, with the option to record only that episode or all future ones; help specify precisely what to record (current episode, only new episodes, only games of specific teams); allow playing and deleting content, adjusting recording settings; consider offering automatic storage management, overwriting the oldest or already watched content.

Exact specifications: the text does not give specific numbers, measurements or proportions.

Platform differences: no specific additional considerations cited beyond the nature of the article (aimed at tvOS/streaming); the text states "No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS."

Links to other articles: Remotes; Playing video.

<!-- visual:live-viewing-apps -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0731), code checked; the page has no video or interface screen capture.
- The opening draws a stylized television, a rectangle with very rounded corners with a small horizontal foot underneath, in red over an orange gradient (img 0731).
- Inside the screen there is a centered red play triangle, which joins the idea of TV and playback into a single icon (img 0731).
- The dashed grid has horizontal, vertical and diagonal lines and a guide circle; it shows that the TV rectangle and the play circle share the same geometric center and that the rectangle's corners align with the diagonal rays (img 0731).
<!-- /visual:live-viewing-apps -->

## Loading (slug: loading)

What it governs: how to design the loading of content (assets, levels, data) so it does not disrupt the experience, ideally finishing before the person notices.

Why: Apple starts from the principle that an empty screen is interpreted as a problem in the app; the response is to always show something (placeholder), keep the person occupied with other possible actions while it loads in the background, and use appropriate progress indicators (determinate when the time is known, indeterminate when it is not).

Do and avoid:
- Show something as soon as possible; use placeholder text, graphics or animations while the content loads, replacing them as the real elements become available.
- Let the person do other things in the app while waiting for loading; loading in the background gives access to other actions (example: a game can load content while the player learns about the next level or views a menu).
- If loading is inevitably long, give something interesting to see while waiting (gameplay hints, tips, presentation of new features); calculate the remaining time as precisely as possible.
- Improve install and launch time by downloading large assets in the background; consider using the Background Assets framework to schedule downloads (level packs, 3D models, textures) for right after installation, during updates, or other non-disruptive moments.
- Clearly communicate that the content is loading and how long it may take; use a determinate indicator when you know the duration, indeterminate when you do not.
- For games, consider creating a custom loading screen with animations and elements that match the game's style, instead of the standard indicators.

Exact specifications: the text does not give specific numbers, measurements or proportions.

Platform differences:
- iOS, iPadOS, macOS, tvOS, visionOS: no additional considerations.
- watchOS: as much as possible, avoid showing a loading indicator in the watchOS experience, since people expect quick interactions; in situations where content needs a second or two to load, it is better to show a loading indicator than a blank screen.

Links to other articles: Launching; Progress indicators; Background Assets (developer documentation).

<!-- visual:loading -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0732), code checked; the page has no video or interface screen capture.
- The opening is the classic spinning activity indicator: eight capsule-shaped strokes arranged as rays around a common center, in red over an orange gradient (img 0732).
- Each stroke has a different opacity, from darkest and most opaque at the top to nearly transparent at the intermediate positions, a device that suggests rotation in a still image (img 0732).
- The construction grid explains the positioning: the guide circle passes through the outer tips of the eight strokes, and the horizontal, vertical and diagonal lines mark equal angular intervals of 45 degrees (img 0732).
<!-- /visual:loading -->

## Managing accounts (slug: managing-accounts)

What it governs: when and how to ask the person to create an account, how to authenticate (Sign in with Apple, passkeys, biometrics), and how to support account deletion.

Why: the golden rule is to ask for an account only when essential functionality requires it; the stated goal is to reduce the barrier to entry, defer commitment as much as possible and provide trust and convenience via Sign in with Apple or passkeys, avoiding the need for the person to remember multiple credentials.

Do and avoid:
- Ask for an account only if essential functionality requires it; otherwise, let the person use the app or game without an account.
- Explain the benefits of creating an account and how to sign up, with a brief and friendly description on the login screen.
- Defer login as much as possible; let the person feel the app's value before asking for commitment (example: a shopping app can allow free browsing, asking for login only at the time of purchase).
- If not using Sign in with Apple in an iOS, iPadOS, macOS or visionOS app, prefer using a passkey, which eliminates the need to create or type passwords; if passwords are still needed, reinforce security with two-factor authentication.
- Always identify the authentication method offered (for example, a "Sign In with Face ID" button instead of a generic "Sign In").
- Refer only to the authentication methods available in the current context (do not mention Face ID on a device that does not offer it).
- In general, avoid offering an app-specific setting to opt in to biometric authentication, since that is turned on at the system level.
- Avoid using the term "passcode" to refer to account authentication, so as not to confuse it with the device unlock passcode.
- About account deletion: if it helps create an account in the app, it must also help delete it, not just deactivate it, respecting regional legal requirements about deletion and the right to be forgotten; if legal requirements require keeping accounts or information (such as digital health records) or following a specific process, clearly describe the situation. Provide a clear way to start deletion inside the app; if deletion cannot be done in the app, provide a direct link to the web page where it can be done, and make the link easy to find (not buried in Privacy Policy or Terms of Service). If Sign in with Apple was used to create the account, revoke the associated tokens when deleting. Offer a consistent deletion experience, whether in the app or on the website, avoiding a flow that is longer or more complicated than the other. Consider allowing deletion to be scheduled for the future, but also offer the option of immediate deletion. Say when the deletion will complete and notify when it is done. If the app supports in-app purchases, help the person understand how billing and cancellation work when deleting the account (billing for an auto-renewable subscription continues through Apple until the person cancels it, regardless of deleting the account; after deleting, the person needs to cancel the subscription or request a refund); even if the person did not purchase the subscription through the app, account deletion must still be supported.
- About TV provider accounts: many popular providers allow system-level login, eliminating app-by-app authentication; use TV Provider Authentication for more efficient onboarding; avoid showing a logout option when the person is logged in at the system level; if logout needs to be included, it should direct to Settings > TV Provider; never instruct logging out by adjusting privacy controls (Settings > Privacy is not a logout mechanism, it only manages which apps access the provider account).

Exact specifications: the text has no specific numbers, measurements or proportions.

Platform differences:
- iOS, iPadOS, macOS, visionOS: no additional considerations.
- tvOS: most people interact via remote control, not a keyboard, so ask for the minimum information necessary; prefer to let the person use another device to sign up or authenticate (when configuring associated domains, Apple TV can securely suggest credentials, including Sign in with Apple); when signed into a shared account, avoid asking to choose the profile every time it becomes the current user (on tvOS 16+, the app can share credentials between users while keeping profile and individual data separate); minimize data entry, asking the person to visit a website on another device if more information needs to be gathered; if email is needed, show the email keyboard screen with a list of recently typed addresses.
- watchOS: use iCloud sync to give access to Keychain, enabling autofill of username and password and preservation of app settings.

Links to other articles: Onboarding; Sign in with Apple; Helping people manage their subscriptions; Providing help with in-app purchases.

<!-- visual:managing-accounts -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0751), code checked; the page has no video or interface screen capture.
- The opening represents the account with a person icon, circular head and half-moon shoulders, over an orange gradient (img 0751).
- The person sits inside a thick red circular ring, hollow and unfilled, that works as a profile frame (img 0751).
- The construction uses two concentric layers: besides the horizontal, vertical and diagonal dashed grid, a smaller guide circle just inside the ring marks the inner radius of the frame (img 0751).
<!-- /visual:managing-accounts -->

## Managing notifications (slug: managing-notifications)

What it governs: how to ask for permission, classify by interruption level and deliver notifications, including integration with Focus and rules for marketing notifications.

Why: the central logic is trust: the app must accurately represent the urgency of each notification, because the person has several ways to adjust how they receive them (including turning everything off), and a notification that uses high urgency for low-priority information breaks that trust.

Do and avoid:
- Permission must be obtained before sending any notification; the system lets the person change that decision in settings, including silencing all notifications (except government alerts in some locations).
- Identify the types of notification the app can send: direct communication (calls, messages) uses communication notifications (via SiriKit intents, allowing customization by Siri); the rest use noncommunication notifications, with an interruption level defined by the system for each one.
- Build trust by accurately representing the urgency of each notification.
- Use the Time Sensitive level only for notifications relevant in the present moment; help the person understand the benefits of letting Time Sensitive notifications break through a Focus or scheduled delivery; the notification needs to be about an event happening now or within an hour.
- Do not use notifications for marketing or promotional content unless the person explicitly agrees; never use the Time Sensitive level for a marketing notification.
- Ask for explicit permission if you want to send promotional or marketing notifications, with an interface (alert, modal view) that describes the types of information and gives a clear way to opt in or out.
- Make sure the person can manage notification settings within the app, beyond the initial permission request.

Exact specifications:
- The system defines four interruption levels for noncommunication notifications: Passive (information to view at a calm pace), Active (default; information the person might like to know when it arrives), Time Sensitive (information that has a direct impact and requires immediate attention) and Critical (urgent health and safety information, extremely rare, typically from government agencies or health/home apps).
- Behavior table by level: Passive does not override scheduled delivery, does not break through Focus, does not override the Ring/Silent switch; Active is the same (all "No"); Time Sensitive overrides scheduled delivery (Yes) and breaks through Focus (Yes), but does not override Ring/Silent (No); Critical overrides scheduled delivery (Yes), breaks through Focus (Yes) and overrides the Ring/Silent switch (Yes).
- A Time Sensitive notification needs to be about an event that is happening now or will happen within an hour.
- A specific entitlement is required to send a Critical notification, since it can override the Ring/Silent switch and break through scheduled delivery and Focus.

Platform differences:
- iOS, iPadOS, macOS, tvOS, visionOS: no additional considerations.
- watchOS: by default, the notification settings the person uses for apps on iPhone apply to the same apps on Apple Watch; it is possible to manage these settings through the Apple Watch app on iPhone, or access per-notification options (such as Mute 1 Hour or Turn off Time Sensitive) by swiping left when the notification arrives on the watch.

Links to other articles: Privacy; Settings; User Notifications (developer documentation).

<!-- visual:managing-notifications -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0752), code checked; the page has no video or interface screen capture.
- The opening draws a notification bell only in a thick red outline, unfilled, over an orange gradient (img 0752).
- The only filled element is a small circle overlapping the upper right corner of the bell, which serves as a point of contrast and suggests an alert indicator attached to the bell (img 0752).
- The set sits on the grid of dashed lines and the guide circle used in the other openings (img 0752).
<!-- /visual:managing-notifications -->

## Modality (slug: modality)

What it governs: when and how to present content in modal mode (alerts, sheets, popovers, separate windows, full screen experiences) that prevents interaction with the parent view until an explicit dismissal action.

Why: modality takes the person out of the current context and requires an action to exit, so it should only be used when there is a clear benefit: delivering critical information, confirming or modifying a recent action, helping with a distinct and well-delimited task without losing the previous context, or offering immersion/focus in a complex task.

Do and avoid:
- Present content modally only when there is a clear benefit for focus or choices that affect the content or device.
- Keep modal tasks simple, short and lean; a complicated modal task makes the person lose track of the task they suspended when entering the modal view.
- Avoid creating a modal experience that feels like "an app within the app"; presenting a hierarchy of views inside a modal can create confusion about how to step back; if the modal task needs to contain subviews, offer a single path through the hierarchy and avoid buttons that could be confused with the button that dismisses the modal.
- Consider using a full screen modal style for in-depth content or a complex task (videos, photos, camera, or multi-step tasks like marking up a document or editing a photo); in visionOS, when running alongside other apps in the Shared Space, this presentation fills a window; if the person transitions the app to a Full Space, it can become a more immersive experience.
- Always give an obvious way to dismiss a modal view, following platform conventions (on iOS, iPadOS and watchOS, typically a button in the top toolbar or swiping down; on macOS and tvOS, a button in the main content view).
- When necessary, help avoid data loss by obtaining confirmation before closing a modal view that would lose content generated by the person; explain the situation and give ways to resolve it (example: on iOS, an action sheet with an option to save).
- Make it easy to identify the task of a modal view: give it a title that names the task, or additional text that describes or guides it.
- Let the person dismiss a modal view before presenting another one; several modal views visible at the same time create visual disorder; although an alert can appear over everything else (including other modal views), never show more than one alert at the same time.

Exact specifications: the text has no specific numbers, measurements or proportions.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: Sheets; Alerts; Popovers; Action sheets; Activity views; Going full screen; Immersive experiences (visionOS).

<!-- visual:modality -->
### What the illustrations show
Basis: 1 illustration sheet viewed, with a single image (img 0799), code checked; the page has no video or interface screen capture.
- The opening shows two overlapping rounded rectangular windows: one behind and to the left, another larger one in front and to the right, covering part of the first (img 0799).
- Only the front window has a title bar with three dots at the top, above a rectangular body; the one behind does not have this detail (img 0799).
- Both windows use the same translucent red over the orange background, with no difference in opacity, color or darkening; the hierarchy comes only from the overlap and the title bar exclusive to the front window (img 0799).
- A grid of vertical, horizontal and radial diagonal dotted lines, with a guide circle, covers the whole composition and marks the axes used to draw and align the two windows (img 0799).
Recorded divergences: the official description says the composition suggests focus on the front window, but the image does not mark the back window as inactive through opacity or color; the focus reads only through the overlap and the three-dot bar.
<!-- /visual:modality -->

## Multitasking (slug: multitasking)

What it governs: how an app should behave when the person switches to another app (pausing, saving context, responding to audio interruptions, finishing background tasks) and how multitasking manifests on each platform.

Why: the premise is that the person expects multitasking and may think something is wrong if the app does not allow it; since the app never knows when multitasking will be initiated, it needs to always be ready to save and restore context, and handle interruptions (audio, for example) the way the system and other apps expect.

Do and avoid:
- Pause activities that require attention or active participation when the person switches apps (games, media apps), making sure nothing is lost; when they return, let them continue as if they had never left.
- Respond gently to audio interruptions: pause audio indefinitely for primary audio interruptions (music, podcasts, audiobooks); temporarily lower the volume or pause for short interruptions (GPS turn-by-turn notifications), restoring the original volume or playback when the interruption ends.
- Finish tasks the person started in the background (asset downloads, video processing) even if they switch apps, completing them before suspending, if the task does not need further input.
- Use notifications with restraint: you may notify when an important or time-sensitive task finishes while the app is suspended or in the background; avoid notifying for routine or secondary tasks, letting the person check when they return.

Exact specifications: the text does not give specific numbers, measurements or proportions.

Platform differences:
- Not supported on watchOS.
- iOS: on iPhone, multitasking lets you use FaceTime or watch video in Picture in Picture while using another app.
- iPadOS: it is possible to see and interact with windows from several different apps at the same time; a single app can also support multiple open windows; apps can be used full screen or windowed; when windowed, the behavior is resizable and similar to macOS, with system controls for common tiling configurations, entering full screen, minimizing and closing windows; the system identifies the front window by coloring its window controls and casting a shadow over the windows behind it; apps do not control or receive any indication of the multitasking configurations the person chooses; videos and FaceTime calls can also play in Picture in Picture over other content, regardless of whether the apps are full screen or windowed.
- macOS: multitasking is the default experience, since people usually run more than one app at a time, switching between windows and tasks; macOS applies shadows to give a sense of layered windows on the desktop, and other visual effects to differentiate window states.
- tvOS: it is possible to browse or navigate content while also playing movies or shows in Picture in Picture (where supported).
- visionOS: on Apple Vision Pro, it is possible to run multiple apps at the same time in the Shared Space, seeing and switching between windows and volumes; only one window is active at a time in the Shared Space, becoming active when the person looks at it, while the previous one becomes more translucent and appears to recede along the z axis; closing an app window in the Shared Space transitions the app to the background without ending it; when the app is the Now Playing app, closing its window automatically pauses audio playback (it is possible to resume it in Control Center without opening the window); avoid interfering with the multitasking behavior provided by the system (visionOS applies a "feathered" mask to the window the person looks away from, and changing the appearance of the window's edges interferes with this feedback); do not pause video playback in a window when the person looks away from it (as in macOS, playback started in one window continues while viewing or performing a task in another); be prepared for situations where audio may "duck" (lower), unless the app is the current Now Playing app.

Links to other articles: Layout; Windows; Playing video; Playing audio; Managing notifications.

<!-- visual:multitasking -->
### What the illustrations show
Basis: 2 illustration sheets (img 0801 to 0805) and 2 video sheets (video 016) viewed, codes checked.
- The opening is already the split view layout itself: two identical rectangular columns side by side, separated by a thin gap, inside a larger rounded outline, over the geometric grid and the guide circle (img 0801).
- The iPhone app switcher stacks the app cards in a cascade, lightly overlapping, with rounded corners and a shadow between them; the front card is sharper, the visible cards show snippets of the apps' content (Mail, a music library with a "Not Playing" bar, a third one cut off on the right) and there are recent app icons at the bottom, over a blurred background (img 0802).
- The FaceTime call that continues in another app appears as a small, rounded photo of the person, floating in the bottom left corner over the open email, and not as a separate panel (img 0803).
- The iPad app switcher in landscape organizes the open apps in a two-row grid, three thumbnails on top and two below, each with the actual content rendered, with the Dock below and the time at the top (img 0804). Compared to the iPhone, the format swaps the cascade for a grid (img 0802 and img 0804).
- With windows on iPad, the front window, larger and overlapping, casts a visible shadow over the Maps window behind it and shows colored dot controls in the top left corner; the back window does not show these colored controls. Both float over the wallpaper, with the Dock below (img 0805).
- In video 016 (sheet 0001, q001 to q009), two translucent windows coexist side by side in visionOS, Notes on the left and Settings on the right, each with its own content and its top bar of round buttons, with the edges almost touching; from q004 to q006 the background scenery changes from a shelf with plants to a wall with a guitar, and the relative position of the windows does not change.
- In sheet 0002 (q010 to q018), the windows are closer together; in q012, q016 and q018 a bright, light vertical band appears exactly on the left edge of Settings, at the border with Notes, while in the other frames this edge is an ordinary straight line. The alternation is consistent with the fade applied to the edge of the window that loses focus, a localized and subtle effect.
Recorded divergences: in the still frames of video 016 it is not possible to see which window is active at each instant. The change in background scenery, from plants to guitar, appears in the frames and is not mentioned in the official description.
<!-- /visual:multitasking -->

## Offering help (slug: offering-help)

What it governs: how to offer contextual help (tips, tooltips) when the experience is not fully self-explanatory, including the rules for creating tips with TipKit and tooltips (help tags) on macOS/visionOS.

Why: the underlying philosophy is that the most effective experience is approachable and intuitive on its own; contextual help is the fallback resource, and it should be directly tied to the action or task the person is doing right now, easy to dismiss or avoid if not needed.

Do and avoid:
- Let the app's tasks guide the types of help needed: for simple one or two step tasks, an inline view that succinctly describes the task; for complex or multi-step tasks, consider a tutorial.
- Use relevant and consistent language and imagery in the help content, appropriate to the current context (for example, not showing game controller tips in a Siri Remote context) and consistent with the platform's terms (not saying "click" for an iPhone button, or "tap" for a Mac menu item).
- Make all help content inclusive.
- Avoid inflating the help content by explaining how standard components or patterns work; describe the specific action or task that a standard element performs in your app; if the app introduces a unique control or expects nonstandard use of an input device, guide briefly, preferring animation or graphics over a long description.
- About tips (TipKit): use the tip type most appropriate to the interface (popover tip to preserve the content flow; inline tip to ensure the surrounding information stays visible; annotation-style to point to a specific UI element; hint-style when not tied to a specific piece of UI); use tips for simple features, easy to describe and complete in a few steps (if a feature requires more than three actions, it is probably too complicated for a tip); make tips short, actionable and engaging, with direct, action-oriented language, limited to one or two sentences, avoiding promotional content or content related to another feature; set eligibility rules (based on a parameter or event) for tips to reach the right audience, showing only when the person can benefit; when there is more than one tip, set the display frequency to a reasonable cadence (for example, once every 24 hours); if there is an image or symbol associated with the feature, consider including it in the tip, preferring the filled variant; if the feature is already represented by an image the tip connects directly to, avoid repeating the same image in the tip and in the UI; use buttons to direct to settings or more information related to the feature.

Exact specifications:
- If a feature requires more than three actions, it is probably too complicated for a tip.
- Consider setting the display frequency of tips, for example, once every 24 hours.
- On macOS/visionOS, limit the tooltip content to at most 60 to 75 characters (localization tends to change the length of the text).

Platform differences:
- iOS, iPadOS, tvOS, watchOS: no additional considerations.
- macOS, visionOS: a tooltip (called a help tag in the user documentation) shows a small, transient view that briefly describes how to use a component; in apps running on the Mac (including iPhone and iPad apps), tooltips appear when the person holds the pointer over an element; in visionOS apps, a tooltip can appear when the person looks at an element or holds the pointer over it. Describe only the control the person showed interest in; explain the action or task the control starts (often starting with a verb, such as "Restore default settings"); in general, avoid repeating the control's name in the tooltip; be brief, limiting it to 60-75 characters (allowing for sentence fragments and omitting articles); use sentence case (more casual and approachable), omitting final punctuation unless required by the app's style; consider offering context-sensitive tooltips, with different text for different states of the control.

Links to other articles: Onboarding; Feedback; Writing; Help menu; TipKit (developer documentation).

<!-- visual:offering-help -->
### What the illustrations show
Basis: 3 of 3 illustration sheets opened (img 0813 to 0823), all codes checked; no video.
- The opening art leaves the symbol's own geometric construction visible: a question mark inside two concentric circles, crossed by dotted rectangular and radial guides radiating from the center, over an orange gradient (img 0813).
- The tip has a fixed anatomy across all variants: a rounded-corner card, bold title, description below, close X in the top right corner and a triangular arrow pointing to the related element, in the example a filled blue star (img 0814, 0815, 0816, 0821, 0822).
- In the popover, the card floats over the content and the body text behind it appears dimmed, without being displaced (img 0814).
- In the annotation, the card enters the page flow: there is a block of text above and another below, and the surrounding content is pushed rather than covered (img 0815).
- Wrong and right pair for the symbol inside the tip: a blue outline-only star next to the title gets the gray X marker in a gray circle; a solid blue star, in the same structure, gets the green circle with a white check. The sheet is a 2x2 grid with the marker next to each variant (img 0817 to 0820).
- Against redundancy, two nearly identical versions of the same annotation tip pointing to the star on the screen: one repeats the star next to the title, the other stays text-only and avoids repeating the symbol (img 0821 and 0822).
- The macOS tooltip is built differently from the iPhone tip: a light gray rectangular box, no arrow, no bold title, a single line of text right below the pointer, resting over the back button of a Finder window with traffic lights, title "Documents" and a Favorites sidebar (img 0823).
Recorded divergences: in the notes, the Annotation and Hint frames (img 0815 and 0816) have the same composition, with no perceptible constructed difference beyond the card's position; the distinction the official text makes between the two types is not legible in the image.
<!-- /visual:offering-help -->

## Onboarding (slug: onboarding)

What it governs: how to design an app or game's introduction flow (when necessary), including splash screens, optional tutorials, contextual tips and permission requests during the introduction.

Why: the ideal, according to Apple, is that people understand the app simply by experiencing it; onboarding is a necessary exception, not the rule, and when it exists it should be quick, fun and optional, because teaching too much overloads and reduces retention. Onboarding only happens after launching ends, never as part of it.

Do and avoid:
- Teach through interactivity: people retain better when they perform the task they are learning, rather than just viewing instructional material; offer an interactive experience where the person can try an action, discover a feature or experiment with a game mechanic safely.
- Consider offering a collection of context-specific tips, instead of a single onboarding flow; contextual tips help people learn while progressing through the app, focusing on a single action at a time.
- If you need a prerequisite onboarding flow, design a brief, pleasant experience that does not require memorizing a lot of information; a quick, fun onboarding is more likely to be completed; teaching too much overloads and reduces retention.
- If it makes sense to offer a separate tutorial, consider making it optional; if the person skips it on the first launch, do not present it again on subsequent launches, but make it easy to find later (in a help area, account or settings).
- Keep the onboarding content focused on the experience the app offers; the person does not need to learn how to use the system or the device there.
- Display a splash screen briefly if necessary, with an attractive graphic and concise messaging; display it just long enough to absorb the information at a glance, without seeming to delay the experience.
- Do not let large downloads get in the way of onboarding; consider including enough media and content in the software package to avoid waiting.
- Avoid displaying licensing details in the onboarding flow; let the App Store show agreements and legal notices; if you need to include them in onboarding, integrate them in a balanced way, without getting in the way of the experience.
- Defer non-essential configuration or customization flows, offering reasonable defaults so most people can start interacting without additional setup.
- If the app needs access to private data or resources before it can function, consider integrating the permission request into the onboarding flow, to show why it needs it and the benefits of granting it; otherwise, present the request when the person accesses the specific feature that depends on that data or resource.
- Prefer letting the person try the app before asking for ratings or purchases, since the response tends to be more positive after some engagement.

Exact specifications: the text does not include specific numbers, measurements or proportions.

Platform differences: no additional consideration for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: Launching; Feedback; Offering help; TipKit; Requesting permission.

<!-- visual:onboarding -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0824), code checked; no video and no dark version in this sheet.
- The motif is a hand with open fingers waving, drawn in a continuous dark red stroke in sketch style, which confirms the official welcome reading (img 0824).
- The construction is exposed: dotted rectangular grid lines and a guide circle centered on the palm cross the drawing, the same reference grid pattern seen in the offering-help artwork (img 0824).
- The support is a rounded-corner rectangle with an orange gradient background, in the same system as the other HIG opening illustrations: a thick, continuous dark red stroke and a visible rectangular and circular construction grid (img 0824).
<!-- /visual:onboarding -->

## Playing audio (slug: playing-audio)

What it governs: how an app should play audio while respecting system volume, silent mode, headphone routing and audio session categories (Solo ambient, Ambient, Playback, Record, Play and record), as well as handling interruptions.

Why: the central rule is that system volume always governs the final output, and the app only adjusts relative internal levels; the choice of audio category should honestly reflect the nature of the sound (essential or not, needs to mix with other audio or not) to meet the person's expectation about silence, volume and headphones.

Do and avoid:
- Adjust levels automatically when necessary, but do not adjust the overall volume; the app can adjust relative, independent levels for a good audio mix, but system volume always governs the final output.
- Allow audio rerouting when possible (for example, to a stereo, car radio or Apple TV), unless there is a compelling reason not to allow it.
- Use the volume view provided by the system (with a level slider and rerouting control) for audio adjustments; it is possible to customize the slider's appearance.
- Choose an audio category that matches the app or game's sound usage, avoiding interrupting another app's audio unnecessarily.
- Respond to audio controls (Control Center, headphone controls) only when it makes sense: it is acceptable to respond if the app is actively playing audio, in a context clearly related to audio, or connected via Bluetooth/AirPlay; otherwise, avoid interrupting another app's audio when activating a control.
- Avoid repurposing audio controls; if the app does not support certain controls, do not respond to them.
- Consider creating custom audio player controls only if you need commands that the system does not support (custom fast-forward/rewind increments, or related content such as a sports scoreboard).
- Notify other apps when the app finishes playing temporary audio, signaling the audio session so other apps know when they can resume.
- About interruptions: determine how to respond to audio session interruptions (for example, avoiding interrupting the current audio for an incoming call, unless the person chooses to answer); at the end of an interruption, determine whether to resume playback automatically, considering whether the interruption is resumable (like a call) or not resumable (like when the person starts a new playlist).

Exact specifications:
- Audio category table (AVAudioSession.Category): Solo ambient (non-essential sound but silences other audio; responds to the silent switch; does not mix with other sounds; does not play in the background); Ambient (non-essential sound and does not silence other audio; responds to the silent switch; mixes with other sounds; does not play in the background); Playback (essential sound, can mix with other audio; does not respond to the silent switch; may or may not mix; can play in the background); Record (recorded sound; does not respond to the silent switch; does not mix; can record in the background); Play and record (recorded and played sound, possibly simultaneous; does not respond to the silent switch; may or may not mix; can record and play in the background).
- watchOS: use 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding) encoding for good quality with lower data requirements.

Platform differences:
- iOS, iPadOS: use the system's sound services to play short sounds and vibrations (Audio Services).
- macOS: notification sounds mix with other audio by default.
- tvOS: the system plays audio only when the person starts it, through interactions in apps and games or device calibrations; tvOS does not play sounds to accompany components such as alerts or notifications.
- visionOS: subtle, expressive sounds are everywhere, reinforcing experiences and giving essential feedback when looking at a virtual object and using gestures; the system combines audio algorithms with information about the person's physical surroundings to produce Spatial Audio, sound perceived as coming from specific locations in space, not just from speakers; avoid communicating important information using sound alone; audio playback from the Now Playing app pauses automatically when the app's window is closed, and audio from an app that is not the Now Playing app can "duck" when looking at another app; prefer playing sound (an app without sound can seem lifeless or even broken, especially in an immersive moment); design custom sounds for custom UI elements; use Spatial Audio for an intuitive, engaging experience, especially in a fully immersive context; consider defining a variety of locations from which the app's sounds can originate (when the person moves a window playing audio, the sound keeps coming directly from the window); consider varying sounds that could be perceived as repetitive over time (example: the system subtly varies the pitch and volume of the virtual keyboard sounds); decide between fixed sound (fixed, as if pointed at the person, regardless of the direction they look) or tracked sound (tracked, perceived as coming from a specific object); example cited: Mindfulness uses fixed sound to immerse the person in a peaceful environment.
- watchOS: the system manages audio playback; an app can play short clips while active in the foreground, or longer audio that continues even when lowering the wrist or switching apps; use the recommended encoding values (64 kbps HE-AAC); consider presenting a Now Playing view to control current or recent audio without leaving the app, which also shows information about the current source (which can be another app on Apple Watch or iPhone) and automatically selects the current or most recent source.

Links to other articles: Playing video; Feedback; Multitasking (response to audio interruptions); MusicKit, AVAudioSession (developer documentation).

<!-- visual:playing-audio -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0850), code checked; no video.
- The conceptual icon is a speaker in a thick dark red stroke, with three curved sound waves of increasing size coming out to the right, per the official description (img 0850).
- The dotted construction grid is visible over the drawing, with rectangular lines and a guide circle centered on the speaker's body (img 0850).
- The set repeats the system of the section-opening illustrations: rounded-corner rectangle, overlaid construction grid and gradient background tinted in the thematic color, here orange (img 0850).
<!-- /visual:playing-audio -->

## Playing haptics (slug: playing-haptics)

What it governs: when and how to use system and custom haptic feedback (haptics), including the patterns defined per platform (notification, impact, selection on iOS; alignment, level change, generic on Magic Trackpad; and the set of watchOS haptics).

Why: the underlying logic is clear causality: each haptic needs to reinforce a cause and effect relationship consistent with the action that generates it, so that the person learns to associate certain patterns with certain experiences; using the same pattern for opposite outcomes (positive and negative) creates confusion.

Do and avoid:
- Use the system's haptic patterns according to their documented meanings; if the documented use case does not make sense in your app, use a generic pattern or create your own, where supported.
- Use haptics consistently throughout the app, building a clear causal relationship between each haptic and the action that triggers it.
- Prefer using haptics to complement other feedback (visual, auditory); when they are in harmony, the experience feels more natural; match the intensity and sharpness of the haptic with the intensity and sharpness of the animation it accompanies; it is possible to sync sound with haptics.
- Avoid overusing haptics; a haptic may feel perfect occasionally, but tiresome if played frequently; test with users to find the balance (the best haptic experience is one the person may not even consciously notice, but misses when it is turned off).
- In most apps, prefer short haptics that complement discrete events; long haptics can improve gameplay, but in an app they can dilute the meaning of the feedback and distract from the task (on Apple Pencil Pro, continuous or very long haptics do not tend to clarify the writing/drawing experience and can make holding the pencil less pleasant).
- Make haptics optional: let the person turn them off or silence them, making sure they can still enjoy the app or game without them.
- Be aware that playing haptics can impact other experiences: since they produce enough physical force to be felt, make sure they do not interfere with device features such as camera, gyroscope or microphone.
- About custom haptics: use the two basic building blocks, transient events (brief and compact, like taps or impulses) and continuous events (sustained vibrations); it is possible to control the sharpness and intensity of any event; combine transient and continuous events, varying sharpness and intensity, and including optional audio, to create a wide range of haptic experiences.

Exact specifications: the text does not provide numbers, force measurements or exact durations for haptics.

Platform differences:
- iOS: on supported iPhone models, use standard UI components (toggles, sliders, pickers) that play system haptics designed by Apple by default; when it makes sense, use a feedback generator to play one of several predefined patterns in the categories notification (feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle), impact (a physical metaphor to complement a visual experience, such as feeling a tap when a view snaps into place or a thud when two heavy objects collide) and selection (feedback while the values of a UI element are changing).
- macOS: when a Magic Trackpad is available, the app can provide one of three haptic patterns in response to a drag operation or force click: Alignment (indicates alignment of a dragged item, such as aligning shapes in a drawing app, scaling an object, positioning at a preferred location, or reaching the start/end of a video scrubber); Level change (indicates movement between discrete pressure levels, such as when pressing a fast-forward button in a video player); Generic (general feedback when the other patterns do not apply).
- watchOS: Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, giving a more tactile experience when scrolling content; by default, the system provides linear haptic detents felt when turning the Digital Crown; some system controls, such as table views, provide detents as new items enter the screen. watchOS defines a set of haptics, each with a specific meaning: Notification (something significant or out of the ordinary happened and requires attention; the system plays the same haptic when a local or remote notification arrives); Up (an important value increased above a significant threshold); Down (an important value decreased below a significant threshold); Success (an action completed successfully); Failure (an action failed); Retry (an action failed but can be tried again); Start (an activity began, used when starting a timer or activity that the person can explicitly start and stop; usually followed by the Stop haptic); Stop (an activity stopped, used when stopping a timer or other previously started activity); Click (the sensation of a dial clicking, communicating progress in predefined increments or intervals; overusing it reduces its usefulness and can be confusing when clicks overlap).

Links to other articles: Feedback; Gestures; Core Haptics (developer documentation); Apple Pencil (for haptics on Apple Pencil Pro).

<!-- visual:playing-haptics -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0851) and 18 demonstration videos (017 to 034), one sheet each, all opened with checked codes.
- The opening art uses three thick dark red outlined circles, slightly overlapping in a horizontal row, with a denser core where the strokes cross; the rectangular dotted grid and a centered diamond or guide circle are visible over the orange gradient (img 0851).
- Videos 017 to 025 share a timeline notation: light gray horizontal baseline, light green band with dashed texture as a fixed reference near the start, pulses drawn as solid green vertical bars whose height tracks the force, and a dotted vertical guide with a small dot on each end, which sits at the left margin in q001 (0.0 s) and at the right margin in q002 (0.5 s), suggesting progressive reveal of the pattern; the exception is the error, in which the guide already appears near the left center in q001 (videos 017 to 025, frames q001 and q002; video 019).
- In the notification patterns, success ends with two bars, one slightly higher than the other (video 017, q002); warning also ends with two bars, with heights that look closer together, a difference too subtle to state with certainty (video 018, q002); error reaches four bars with a jagged profile, with one bar in the middle of the sequence clearly higher than its neighbors, a more pronounced irregularity than in success and warning, and in q001 it already shows two hatched bands and two solid bars of quite different heights (video 019).
- In the impacts there is a single pulse, and the bar height grows in the order light, medium and heavy; in heavy it occupies almost the entire distance between the baseline and the usable top of the frame (videos 020, 021 and 022, q002).
- Rigid has a tall bar, close to that of heavy, which appears slightly shifted to the left; soft has a low bar, similar to that of light, which looks a bit wider; selection has a moderate height and the bar is visibly narrower than all of the impact ones (videos 023, 024 and 025, q002).
- Videos 026 to 034 switch notation: thin, isolated pink bars for discrete pulses, a triangular fan of blue and pink vertical lines that grows and then narrows for the continuous vibration that decays, and a tail of light dots; a white time marker, a vertical line with small dots at the ends, leaves the start, passes through the peak of the fan and reaches the end of the tail, and in q004 and q005 the complete drawing reappears with the marker at the end, suggesting repetition of the cycle (video 026, frames q001 to q005).
- The number of isolated pulses at the start is the main identity code among these haptics: two in Notification, Up and Down, three in Success and just one in Start (videos 026, 027, 028, 029 and 032).
- Up has a blue vibration body that is visibly taller, longer and denser than that of Notification; Down repeats the same shape as Up, with no inversion or visible difference in proportion (videos 026, 027 and 028, q001).
- Stop is built as two identical copies of the pulse, fan and tail drawing, side by side in the same frame, with the marker between the two copies in q002; in q004 the pair reappears with no visible marker inside the cropped frame (video 033, q001 to q004).
- Failure and Retry abandon the separate pulses: a filled rectangular pink block, with dense and irregular internal peaks, followed by a short blue dotted tail, without the gaps between pulses seen in the other shapes (videos 030 and 031).
- Click is the most discreet drawing in the set: inside the pink bar there is only a short, low-amplitude wavy stroke, with no decay fan, followed by an almost straight, long dotted line to the end of the frame (video 034).
Recorded divergences: the audio described in the official caption is not verifiable from the image (video 017); the height difference between success and warning is too subtle to state with certainty (video 018); rigid and heavy are not distinguishable beyond the similar height (video 023); Retry has no visual mark that separates it from Failure, against the expectation of distinct shapes for distinct meanings (video 031); the alternative captions from 026 to 034 are generic and do not mention the time marker, cycle repetition or pulse count, which only the images show.
<!-- /visual:playing-haptics -->

## Playing video (slug: playing-video)

What it governs: how to use the system video player (aspect-fill and aspect/fit-to-screen modes, Picture in Picture), integrating with the TV app, and how the recommendations change across platforms for loading screens and playback exit.

Why: the central guideline is to use the system player to give a familiar and consistent experience; when a custom player is truly necessary, it should reference the behavior and interface of the system player, because a subtle deviation causes frustration since the person does not know which usual interactions still work.

Do and avoid:
- Use the system video player for a familiar and convenient experience; if the app truly needs a custom player, reference the behavior and interface of the system player.
- Always display video content in its original aspect ratio; padding embedded (letterbox/pillarbox) in the video frame itself can prevent the system from scaling correctly according to the playback mode, making videos appear smaller both in full screen and in fit-to-screen, and preventing correct display in edge-to-edge contexts, such as Picture in Picture on iPad.
- Provide additional information when it adds value (image, title, description) on iOS, iPadOS, tvOS and visionOS, keeping it limited so as not to obscure media playback.
- Support the interactions the person expects, regardless of the input device (for example, pressing Space on a connected keyboard to play/pause on Apple Vision Pro, Mac, iPhone, iPad and Apple TV; familiar and intuitive gestures with the Siri Remote on Apple TV).
- If the person needs to access playback options or content-specific information in the tvOS app, consider adding a custom transport control or content tab, offering only the most useful actions and information, helping them return quickly to the viewing experience.
- Avoid letting audio from different sources mix when switching modes (for example, between full screen and Picture in Picture); mixed audio is an unpleasant and frustrating experience.
- About integration with the TV app: ensure a smooth transition (the TV app fades to black during the transition and does not show your app's launch screen; maintain visual continuity by showing your own black screen immediately before starting or resuming content); show the expected content immediately, jumping straight from the black screen to the content, avoiding splash screens, detail screens, intro animations or any barrier; avoid asking whether the person wants to resume playback, resuming automatically without asking for confirmation; play or pause playback when Space is pressed on a connected Bluetooth keyboard; make sure the content plays for the correct viewer (if the app supports multiple profiles, automatically switch to the profile specified by the TV app before starting playback; if the request does not specify a profile, ask the person to choose before starting); use the previous end time when resuming playback of a long clip.
- About content loading: avoid showing loading screens when possible; if loading takes more than two seconds, consider showing a black loading screen with a centered activity spinner, with no content around it; start playback immediately, showing the loading screen only until enough content has loaded, continuing to load the rest in the background; minimize the loading screen's content (branding or images in moderation), keeping the background black for a smooth transition.
- About playback exit: show a contextually relevant screen, displaying the detail view of the content that was being watched, with the option to resume playback; if there is no detail view, show a menu with that content or the app's main menu; be prepared for an immediate exit, preparing the exit view as soon as possible after receiving the playback notification.

Exact specifications:
- Full-screen mode (aspect-fill) is the default for wide video (2:1 to 2.40:1); the video scales to fill the screen, and cropping can occur at the edges.
- Fit-to-screen mode (aspect) is the default for standard video (4:3, 16:9 and anything up to 2:1) and ultrawide video (above 2.40:1); the entire video stays visible, with letterboxing or pillarboxing as needed.
- If loading takes more than two seconds, consider showing a black loading screen with a centered spinner.
- tvOS: implement a minimum delay of 0.5 seconds to pause the media and display an interactive overlay (quizzes, polls, progress check-ins).
- visionOS: to support scrubbing, provide a set of thumbnails 160 px wide each.
- watchOS: prefer short video clips, no more than 30 seconds.
- watchOS, recommended encoding table for media assets: H.264 High Profile video codec; video bit rate 160 kbps at up to 30 fps; full-screen resolution 208x260 px (portrait); 16:9 resolution 320x180 px (landscape); audio 64 kbps HE-AAC (the audio encoding values apply to both movies and audio-only assets).

Platform differences:
- iOS, iPadOS, macOS: no additional considerations.
- tvOS: favor the content when showing logos or non-interactive overlays over the video; a small, discreet logo or a countdown timer can be appropriate, but avoid large, distracting overlays; some devices are prone to image retention, so it's better to keep overlays short and prefer translucent graphics in Standard Dynamic Range (SDR) over opaque, bright content; for interactive overlays (quizzes, polls), implement a minimum delay of 0.5 seconds when pausing the media, and give a clear way to dismiss the overlay and resume playback.
- visionOS: help the person stay comfortable while playing video, letting them choose when to start, using a small window for playback (resizable if desired) and making sure they can see their surroundings during playback; in a fully immersive experience, avoid letting virtual content obscure playback or the transport controls (the system automatically positions the player in a predictable location that offers optimal viewing); avoid automatically starting a fully immersive playback experience without warning; create a thumbnail track if you want to support scrubbing (160 px wide thumbnails); avoid expanding an inline video player to fill a window (inline video needs to be 2D, and the window's content must remain visible around the player); use a RealityKit video player if you need to play video in a view such as a splash screen or transitional view, since in those cases the person doesn't need playback controls or system integration (dimming, view anchoring); the RealityKit video player automatically uses the correct aspect ratio for 2D and 3D video and supports closed captions, and can also play video as a special effect on the surface of a view or custom object.
- watchOS: the system manages video playback; apps can play short clips while active in the foreground; you can use a movie element to embed inline clips or play a clip in a separate interface; prefer short clips of no more than 30 seconds (long clips use more disk space and require keeping the wrist raised for longer, causing fatigue); use the recommended sizes and encoding values, avoiding scaling video clips (it affects performance and results in a lower-quality appearance); avoid creating a poster image that looks like a system control; consider creating a poster image that represents the clip's content, helping the person decide whether to watch, avoiding images unrelated to the content or that could be mistaken for a control.

Links to other articles: Playing audio; Feedback; Keyboards; Remotes; AVKit, HTTP Live Streaming (developer documentation).

<!-- visual:playing-video -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened (img 0852 to 0859), codes checked; no video.
- The cover is a play button, a dark red circle with a white triangle, over an orange gradient, crossed by a horizontal, vertical and diagonal dashed grid that forms an X and a circle concentric to the icon (img 0852).
- The diagrams repeat the frame of an iPhone lying on its side, with a gray outline in img 0853, and a three-color code that the caption names: light blue for the AVKit safe area, lilac purple for the video and pink for the embedded padding (img 0853, 0855, 0857, 0858, 0859); the video rectangle has a centered camera icon (img 0853, 0858).
- The caption that names the three colors only appears on the second sheet, after the colors have already been used without explanation in the first illustrations (img 0857 in relation to 0853 and 0855).
- 4:3 video without padding: the purple rectangle is wider than the blue screen and extends equally past the device's left and right edges, with no pink strip at all (img 0853).
- The same 4:3 video with embedded padding gains two narrow pink vertical strips attached to the sides of the purple rectangle, extended to the device's edges (img 0855).
- Right and wrong are not shown by varying the scene, but with separate badges next to the equivalent illustration: a green circle with a white check for the version without padding and a gray circle with a white X for the version with padding (img 0854 and 0856, paired with 0853 and 0855); per the notes, the page's caption associates the correct badge with the full-screen 4:3 video (img 0854).
- 21:9 video without padding: a thin light blue strip crosses the width of the screen at the top as the safe area, and a dark blue outlined rectangle with the camera in the center occupies almost the entire screen, from top to bottom, taller than the safe area (img 0858).
- 21:9 video with padding: two horizontal pink letterbox strips above and below the video rectangle, between it and the device's edges (img 0859).
- Rule common to both sheets: the video extends past the safe area equally at the relevant edges, the sides in 4:3 and top and bottom in 21:9, and the padding always appears as a thin pink strip attached exactly at those edges (img 0853, 0855, 0858, 0859).
<!-- /visual:playing-video -->

## Printing (slug: printing)

What it governs: how to integrate the system's print functionality into iOS, iPadOS, macOS and visionOS apps, including custom printer and document options on macOS.

Why: the guidance is discoverability and transparency: put the print action in standard system locations, and hide or disable the option when there's nothing to print or no printer available, so as not to frustrate people with a command that can't be executed.

Do and avoid:
- Make printing discoverable, placing the print action in standard system locations (a Print item in the File menu of a macOS app; in an iOS or iPadOS app, a toolbar button that opens an action sheet); if the macOS app has a toolbar, consider also placing a Print button, but as an optional button the person adds when customizing the toolbar.
- Present the print option only when it's possible; if there's nothing on screen to print, or no printer available, dim the Print item in the File menu (macOS) or remove the Print action from the action sheet (iOS/iPadOS); if you implement a custom print button, dim or hide it when printing isn't possible.
- Present relevant print options (page range selection, multiple copies, double-sided printing) using the view the system provides, if it makes sense and the printer supports it.
- On macOS, if the app offers specific options the system doesn't offer, consider creating a custom category in the print panel, with a unique name (such as the app's name) and options that improve the app's printing experience (example: Keynote offers presentation-specific options, such as printing presenter notes, slide backgrounds and skipped slides).
- If the app supports document-specific page settings, consider presenting a page setup dialog with rarely changed settings (page size, orientation, scale); avoid implementing features the system already offers (such as page orientation or reverse-order printing).
- Make sure interdependencies between options are clear (example: if double-sided printing is available, the option to print on transparencies becomes unavailable).
- Separate advanced features from frequently used features, considering a disclosure control to hide advanced options until they're needed, labeled "Advanced Options".
- Consider letting the person preview the effect of a setting (example: updating a thumbnail to show the effect of changing a tone control).
- Consider storing modified settings together with the document, at least until the document is closed, in case the person wants to print again.

Exact specifications: the text doesn't provide specific numbers, measurements or proportions.

Platform differences:
- No additional considerations for iOS, iPadOS or visionOS. Not supported on tvOS or watchOS.
- macOS: see the points detailed above (custom category in the print panel, page setup dialog, interdependencies between options, disclosure control for advanced options, settings preview, storing settings with the document).

Links to other articles: File management; File menu; UIPrintInteractionController, NSDocument (developer documentation).

<!-- visual:printing -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0889), code checked; no video.
- The icon reduces a printer seen from the front to simple shapes: a rounded handle or top opening, a rectangular body with rounded corners, a sheet coming out of the front slot with two horizontal lines in place of the printed text and a small circle in the top right corner as an indicator light (img 0889).
- The construction mesh stays visible behind the drawing: rectangular dashed lines and a circle concentric to the printer's body, showing deliberate symmetry and geometric alignment (img 0889).
- The dark red silhouette sits over a gradient from orange to orange-yellow; orange is the shade the official caption links to the six colors of Apple's original logo (img 0889).
- The scheme is the same as the stylized cover illustrations of other pages cited in the notes, such as pop-up buttons and popovers: a silhouette in a theme color over a gradient, with proportion guides exposed (img 0889).
<!-- /visual:printing -->

## Ratings and reviews (slug: ratings-and-reviews)

What it governs: when and how to ask for ratings and reviews within the app, using the prompt provided by the system.

Why: the premise is that delivering a great overall experience is the best way to encourage positive ratings, but the timing of the request is crucial: asking too early, before the person has formed an opinion about the app's value, can even generate negative feedback.

Do and avoid:
- Ask for a rating only after the person has shown engagement with the app or game (for example, on completing a level or a significant task); avoid asking at first launch or during onboarding, because the person has not yet had time to form a clear opinion, and may even leave negative feedback if they feel the request came too early.
- Avoid interrupting the person while they perform a task or play; look for natural pauses or stopping points where the rating request is less disruptive.
- Avoid insisting with repeated requests, which can annoy and even negatively influence the opinion of the app; consider waiting at least one or two weeks between requests, asking again after the person shows additional engagement.
- Prefer the prompt provided by the system, which checks for previous feedback and, if there is none, shows an in-app prompt asking for a rating and an optional written review; the person can provide feedback or dismiss the prompt with a single tap or click, and can choose to stop receiving these prompts for all installed apps.
- Weigh the cost benefit of resetting the rating summary when releasing a new version: resetting makes the ratings reflect the current version, but results in fewer ratings overall, which can discourage downloads.

Exact specifications: the system automatically limits the display of the prompt to three occurrences per app within a period of 365 days.

Platform differences: no additional consideration for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: Ratings, reviews, and responses; RequestReviewAction (StoreKit, developer documentation).

<!-- visual:ratings-and-reviews -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0919 and 0920), code checked; no video.
- The cover is a five-pointed star in dark red divided vertically: the left half filled in a darker solid tone and the right half only in outline, letting the orange background show through, which confirms the official reading of a partial rating (img 0919).
- The star is drawn over a grid of rectangular guides and a concentric circle, in the same construction system as the other tinted covers (img 0919).
- The rating request on macOS is a white card with a shadow, arranged top to bottom: generic app icon in the upper left corner, made of light gray concentric lines; title in the form of a question, "Enjoying App Name?"; secondary explanatory text; divider line; horizontal row of five stars; dismiss button at the base (img 0920).
- The five stars appear in blue outline and all empty, with no rating chosen beforehand, unlike the partial rating fixed on the cover (img 0920 compared to 0919).
- There is a single dismiss action, the light gray "Not Now" button at full width at the base, with no separate confirm button, because tapping a star is already the action itself (img 0920).
<!-- /visual:ratings-and-reviews -->

## Searching (slug: searching)

What it governs: how to offer search within an app (search field, scope, suggestions, history) and how to integrate the app's content with system-wide search via Spotlight.

Why: the underlying guideline is to give the person a single, clearly identified place to find anything they are looking for in the app, personalizing the experience with what is known about how they interact (recent searches, suggestions, completions, corrections), always balancing convenience with privacy about search history.

Do and avoid:
- If search is important, give it a primary position in the app or in the view (example: in the Notes app, a search field sits in the bottom toolbar alongside other important actions; in apps that use tab bars, such as Photos and Apple TV, search is a dedicated tab).
- Try to make the app's content searchable through a single location; for apps with clearly distinct sections, it can still be useful to offer local search (example: in the iOS Music app, search works as a filter on the current view when searching among songs and albums).
- Clearly display the current scope of a search, using descriptive placeholder text, scope bars and tokens, or a title that reinforces what is being searched (example: in Mail there is always a clear reference to the mailbox being searched).
- Provide suggestions to make searching easier, showing recent searches before typing or predictive suggestions while typing, helping the person search faster and type less.
- Take privacy into account before displaying search history; the person may not like their history appearing where others can see it; if you display it, provide a way to clear it.
- About system-wide search (Spotlight): make the app's content searchable in Spotlight, sharing indexable content with descriptive metadata; define metadata for custom file types via a Spotlight File Importer plug-in; use Spotlight to offer advanced file search capabilities within the app's context (for example, a button that instantly starts a Spotlight search based on the current selection); prefer using the system-provided open and save views, which generally include a built-in search field for searching and filtering the entire system; implement a Quick Look generator if the app produces custom file types, helping Spotlight and other apps show previews of the documents.

Exact specifications: the text does not include specific numbers, measurements or proportions.

Platform differences: no additional consideration for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: Search fields; Scope bars and tokens; File management; Quick Look; Core Spotlight (developer documentation).

<!-- visual:searching -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0994), code checked; no video.
- The icon is a red magnifying glass with the handle pointing toward the lower right diagonal, over an orange gradient (img 0994).
- The rim of the magnifying glass is concentric with the grid's guide circle, which shows that it was drawn over the reference circular mesh (img 0994).
- The grid's diagonals coincide with the tilt of the handle, and the mesh also includes horizontal and vertical lines (img 0994).
- It is the only image on the page and follows the pattern of the covers of other pages cited in the notes, such as right-to-left, scroll-views and search-fields: visible geometric grid and tinting in one of the colors of the six-color logo, here orange, indicating a common modular mesh rather than freehand drawing (img 0994).
<!-- /visual:searching -->

## What this group reveals about the Apple way

1. Urgency is a scarce resource regulated by contract: Apple formally defines interruption levels (Passive, Active, Time Sensitive, Critical in `managing-notifications`) and requires an entitlement for the highest level, in a logic that repeats in `feedback` (reserving alerts for what is truly critical) and in `ratings-and-reviews` (never asking for a rating at a moment that interrupts the task). The common denominator is: interrupting the person is a credit that gets spent, not a button that gets pressed.

2. Trust in the system matters more than the app's one-off will: in `managing-notifications`, a Time Sensitive marketing notification is prohibited even with the person's explicit consent; in `managing-accounts`, the app is required to support account deletion even when the subscription was purchased outside it. The platform protects the person from the developer's own decisions.

3. "Downplay" and "not a branding opportunity" appear as a recurring principle: the launch screen (`launching`) is explicitly not branding; the tvOS loading screen (`playing-video`) should minimize branding while keeping a black background; the onboarding splash screen (`onboarding`) should be brief enough not to seem like a delay. Apple treats transition moments as neutral by design, reserving brand expression for the actual content.

4. The system component is always the default option, and custom is the justified exception: this appears almost word for word in `playing-video` ("use the system video player"), `file-management` ("use the default file browser unless you have an important reason"), `printing` ("avoid implementing features the system already offers") and `offering-help` (system tooltips via `help(_:)`). Building from scratch is treated as a risk of breaking expectations, not as an opportunity for differentiation.

5. Data loss is the red line that always requires confirmation, but only when it is unexpected: `drag-and-drop`, `modality` and `feedback` repeat the same rule with the same exception, warn when the loss is surprising and irreversible, but never warn when it is the obvious, expected result of the person's action (the example of the Finder not warning when throwing a file away appears almost identical in `feedback` and is echoed in `drag-and-drop`).

6. Every pattern that involves short text has an implicit or explicit character ceiling: tooltips on macOS/visionOS (`offering-help`) have a limit of 60 to 75 characters; TipKit tips must fit in one or two sentences; sharing permission phrases (`collaboration-and-sharing`) are described as "succinct phrases". Apple treats conciseness as a functional requirement, not a stylistic one.

7. Deferring is treated as good practice in almost every initial flow: deferring login for as long as possible (`managing-accounts`), deferring non-essential settings in onboarding (`onboarding`), deferring rating requests until there is real engagement (`ratings-and-reviews`), and even using the Background Assets framework to defer large downloads until after installation (`loading`, `onboarding`). The first contact must be unobstructed.

8. Audio, haptics and video share the same vocabulary of "response to context, not redefinition of the control": `playing-audio` says not to repurpose audio controls; `playing-haptics` says not to redefine the meaning of a documented haptic pattern; both converge on the same central idea from `feedback`, which is to preserve the causal relationship the person has learned between an action and its sensory response.

9. The platform treats "live" (visionOS Shared Space, tvOS live-viewing, calls) with its own media continuity rules: in `multitasking`, `playing-video` and `live-viewing-apps`, the expected behavior is that audio and video keep playing when the person looks at another window or navigates in parallel, and only stop when they deliberately leave the context (see also audio "duck" on visionOS and the Now Playing app).

10. Developer documentation and design text walk side by side with unusual frequency: almost every article in the group references a specific API (`SecureField`, `RequestReviewAction`, `AVAudioSession.Category`, `UIFeedbackGenerator`, `NSHapticFeedbackPerformer`, `DocumentGroupLaunchScene`), showing that the HIG in this "Patterns" group are written to be implemented letter by letter, not just used as inspiration.

11. visionOS is treated as a platform of recurring exceptions to the pattern of the others, not as just another row in the table: in almost every article in the group (`going-full-screen`, `modality`, `multitasking`, `playing-audio`, `playing-video`, `drag-and-drop`) visionOS gets its own section that redefines central concepts (full screen, audio, window activation) in spatial terms (Shared Space, Full Space, Spatial Audio, tracked vs. fixed sound).

12. watchOS is treated as the platform of extreme economy of attention and resources: it avoids loading indicators (`loading`, `feedback`), limits video clips to 30 seconds (`playing-video`), uses 64 kbps HE-AAC to reduce data (`playing-audio`, `playing-video`), and prefers not to show rating requests or visible asynchronous processes, always in the name of reducing the time the person needs to keep their wrist raised or their attention on the watch.

## Reading evidence

| File | Lines read | Read to the end |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/charting-data.md | 45 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/collaboration-and-sharing.md | 51 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/drag-and-drop.md | 73 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/entering-data.md | 41 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/feedback.md | 38 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/file-management.md | 80 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/going-full-screen.md | 49 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/launching.md | 50 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/live-viewing-apps.md | 44 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/loading.md | 39 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/managing-accounts.md | 58 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/managing-notifications.md | 54 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/modality.md | 47 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/multitasking.md | 69 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/offering-help.md | 65 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/onboarding.md | 41 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/playing-audio.md | 75 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/playing-haptics.md | 81 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/playing-video.md | 98 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/printing.md | 31 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/ratings-and-reviews.md | 30 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/searching.md | 41 | yes |

All 22 files in the group were read in full with the Read tool, with no truncation (no file came close to the tool's limit) and no need to read in parts. No article in the group is just a collection index page; all have complete text of their own.
