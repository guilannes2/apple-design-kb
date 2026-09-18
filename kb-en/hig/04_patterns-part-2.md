# Patterns (part 2)

## Settings (slug: settings)

### What it governs
When and how to offer customization options, whether in the system's Settings app, in the app's own settings area, or within the task screen itself.

### Why
Apple starts from the premise that people want apps and games to "just work," but value being able to adjust the experience to their own needs. Every setting costs two things: the person has to interrupt what they were doing to open the settings area, and each extra option is one more decision competing against the approach of "a good default configuration for the largest number of people." That's why the text treats the existence of a setting as something to justify, not as one more neutral feature.

### Do and avoid
- Offer defaults that already deliver the best experience for most people, instead of asking them to decide before they even start using the app.
- Minimize the number of settings offered; too many options makes the experience less tailored and makes it harder to find the right option.
- Make settings available the way people expect to find them (a conventional keyboard shortcut, for example).
- Don't ask for information in settings that the system can already detect on its own (a connected controller, Dark Mode active, etc.).
- Respect the system's settings as a whole and avoid duplicating, inside your app, options that are already global (accessibility, scrolling, authentication); duplicating confusingly implies that the system setting might not apply to your app.
- Put only general, rarely changed options in a dedicated settings area (window configuration, save-game behavior, keyboard mapping, account options).
- Prefer to leave task-specific options (show/hide part of the view, reorder a collection, filter a list) available on the screen where they affect the result, instead of isolating them in a separate settings area, which disconnects the option from its context and hides the result until the person goes back to the task.
- In games, adjusting the approach to a specific task tends to happen as part of the gameplay itself, not as a settings option.
- Add only the most rarely changed options to the system's Settings app; if it makes sense, offer a button that opens that Settings screen directly from your interface.

### Exact specifications
The text does not give numbers, measurements or exact values for this article.

### Platform differences
- iOS, iPadOS, tvOS, visionOS: no additional considerations.
- macOS: choosing the Settings item in the App menu opens the custom settings window, typically with a toolbar of buttons that switch between "panes" of related settings. Include the Settings item in the App menu (and, if there are document-level options, also in the File menu). Dim the minimize and maximize buttons of the settings window, since the standard Command-Comma (,) shortcut makes it unnecessary to keep it in the Dock, and the window already adjusts to the size of the current pane. Use a non-customizable toolbar, always visible, that indicates the active button. Update the window title according to the visible pane; if there are no multiple panes, use the title "App Name Settings." Restore the last viewed pane when reopening the window.
- watchOS: apps and games don't add custom settings to the system's Settings app; the alternative is to make a small number of essential options available at the bottom of the main view, or a "More" menu to reconfigure objects.

### Links to other articles
Onboarding (related).

---

<!-- visual:settings -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 1001), code checked; no video.
- The icon is a red gear with sixteen teeth, three internal spokes and a central hole, over an orange gradient (img 1001).
- The construction grid is overlaid and visible, with rectangular lines, diagonals and a guide circle concentric to the gear, showing a design built over a radial and rectangular mesh (img 1001).
- The gear's internal spokes are aligned with the grid's diagonals, a sign that the symbol's geometry follows the mesh (img 1001).
- The cover repeats the language of the searching and right-to-left openings cited in the notes: a simple icon tinted orange, a rectangular grid with a guide circle and color linked to Apple's six-color logo (img 1001).
<!-- /visual:settings -->

## Undo and redo (slug: undo-and-redo)

### What it governs
How to offer undo and redo so that people can predict the result of each undo or redo action.

### Why
Undo and redo give people easy ways to reverse actions and help them explore and try out a new interface or task safely. Because people often undo repeatedly until they notice some change, they can lose track of which previous action undo is actually reversing, which produces unintended changes and frustration. The design priority, therefore, is to help the person predict the effect of undo/redo and make the result clearly visible.

### Do and avoid
- Help people predict the result of undo and redo as much as possible: on iPhone, describe the result in the alert that appears when the device is shaken, giving the option to confirm or cancel; in undo/redo menu items, customize the label to identify the result (e.g.: "Undo Typing", "Redo Bold").
- Show the result of an undo or redo, especially when the most recent action affects an area no longer visible on the screen; in these cases, highlight the effect (for example, scroll the document to show the restored paragraph), so the person doesn't think the action had no effect and repeat it needlessly.
- Let the person undo multiple times; avoid unnecessarily limiting the number of undos or redos, since the expectation is being able to undo every action back to a logical step such as opening a document or saving the work.
- Consider allowing several changes to be reverted at once, whether a set of incremental adjustments to the same property, or all the changes since the document was opened or last saved.
- Offer undo and redo buttons only when necessary; the default expectation is to start undo/redo through the means already supported by the system (the Edit menu on macOS, keyboard shortcuts on Mac and iPad, shaking the iPhone). If dedicated buttons are important, use the system's standard symbols and place them in a toolbar.

### Exact specifications
The text does not give numbers, measurements or exact values for this article.

### Platform differences
- visionOS: no additional considerations. Not supported on tvOS or watchOS.
- iOS, iPadOS: avoid redefining the standard undo and redo gestures (three-finger swipe, shaking the iPhone), at the risk of confusing people and making the experience unpredictable. The undo/redo alert title already automatically includes the prefix "Undo " or "Redo " (with the trailing space); you need to supply one or two additional words describing what is being undone or redone, such as "Undo Name" or "Redo Address Change".
- macOS: place the undo and redo commands in the Edit menu and support the standard keyboard shortcuts; the expectation is to find them at the top of the Edit menu and use Command-Z and Shift-Command-Z, respectively.

### Links to other articles
Feedback, Pointing devices, Standard keyboard shortcuts, Edit menu (related).

---

<!-- visual:undo-and-redo -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 1205), code checked; no video.
- The symbol is a circular, reddish-orange icon with a hooked arrow that starts at the bottom right, rises and curves left to its tip, which matches the official reading of returning to the start (img 1205).
- A grid of dashed vertical, horizontal and diagonal lines, with a thin circle concentric to the icon, marks the proportions and centering of the symbol within the frame (img 1205).
- The color is built in layers: an orange gradient background, lighter on the left and darker on the right, with the icon in a more saturated red on top; the predominant tone is orange, not pure red (img 1205).
- It's a conceptual opening illustration, not a real interface capture, in the same pattern of a symbol over a construction grid tinted in the theme color that the notes point to in typography and virtual-keyboards (img 1205).
<!-- /visual:undo-and-redo -->

## Workouts (slug: workouts)

### What it governs
How to design a workout or fitness experience (for Apple Watch, iPhone or iPad) that helps people reach their goals, using the device's activity data and familiar components to display metrics.

### Why
People use Apple Watch during many types of workouts and may carry an iPhone or iPad during activities such as walking, wheelchair use and running; larger or more stationary devices (iPad Pro, Mac, Apple TV), on the other hand, tend to be used for live or recorded workout sessions, alone or with other people. The central reasoning is to reduce friction and distraction during physical effort: show only what matters at the moment, make the active session recognizable at a glance and keep legibility even with the body in motion.

### Do and avoid
- In a watchOS fitness app, use workout sessions to provide useful data and relevant controls; since watchOS keeps the app on screen between wrist raises during an active session, it's important to show the data that matters most (time elapsed or remaining, calories burned, distance covered) and offer relevant controls such as lap or interval markers.
- Avoid distracting the person with irrelevant information during the workout; they don't need, for example, to review the list of available workouts or access other parts of the app while working out.
- Use a distinct visual appearance to indicate an active workout; the metrics screen usually serves this purpose because the values update in real time, and an exclusive layout reinforces that distinction.
- Provide workout controls that are easy to find and tap, including pause, resume and stop, with clear feedback for the start and end of the session.
- Help people understand the health information recorded when the sensor isn't available during the workout (for example, water can prevent heart rate measurement, but the app can still record distance swum and calories); when supporting the Swimming or Other types, explain the situation with language similar to that used in the system's Workout app.
- Provide a summary at the end of the session, confirming that the workout has ended and displaying the recorded information; consider reinforcing the summary by including the Activity rings, so the person can check their current progress.
- Discard extremely brief workout sessions: if a session ends a few seconds after it starts, automatically discard the data or ask whether the person wants to log it as a workout anyway.
- Make sure the text stays legible while the person is moving: use large fonts, high-contrast colors and organize the text so the most important information is easy to read.
- Use the Activity rings correctly: it's an element designed by Apple, with one or more rings whose colors and meanings correspond to those of the Activity app; use them only for their documented purpose, not as a generic decorative element.

### Exact specifications
The text does not give numbers, measurements or exact values for this article (no font sizes, durations or numeric proportions are specified).

### Platform differences
- iOS, iPadOS, watchOS: no additional considerations beyond those already described.
- Not supported in macOS, tvOS or visionOS.

### Links to other articles
Activity rings (related).

---

<!-- visual:workouts -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened (img 1333 to 1337), codes checked; no video.
- The cover is a running figure in red silhouette on an orange background, with rectangular and circular construction guides, including a circle centered on the figure's torso (img 1333).
- The workout controls screen on Apple Watch is all black, with the time and the "Paused" state in green at the top and four large buttons in a 2x2 grid, each with its own color and icon for its function: End red with an X, Resume olive yellow with a circular arrow, New green with a plus sign, Segment gray with a circle and the number 1 (img 1334).
- The metrics screen stacks five lines of data vertically, with the green walking icon in the top left corner and the time on the right; the elapsed time, in yellow, is the largest line on the screen, above active calories, heart rate, average pace and distance (img 1335).
- The quick-reading hierarchy in the metrics comes only from font size and a colored context icon next to the value, like the red heart for heart rate, with no background color to highlight it (img 1335).
- A metric with no data appears filled with dashes, keeping the average pace label in place (img 1335).
- The media screen shows the no-playback state: a large gray rectangle with a smartphone icon and the text "Not Playing", three controls for back, play and forward below, and an iPhone icon next to the time at the top (img 1336).
- The three screens in the flow use the same black background and the same time in the top corner as a common anchor, varying only the central content between button grid, metrics stack and playback controls; dot page indicators signal three screens, at the bottom on the controls screen and on the right side on the metrics screen (img 1334, 1335, 1336).
- Correct use is marked by an isolated badge, a white checkmark in a green circle, with no other element on the sheet; the example image it accompanies is not on this sheet (img 1337).
<!-- /visual:workouts -->

## What this group reveals about the Apple way

1. Configuration is treated as a cost, not as a free resource: in "settings", the central guideline is not "how to build an options screen" but "when this option should not even exist", with the right default replacing the question asked to the person (settings).
2. There is an explicit hierarchy for where an option should live, from most contextual to most distant: inside the task screen itself, then in the app's settings area, and only last in the system's Settings app, always prioritizing keeping the option close to where it takes effect (settings).
3. The system as the sole authority over global preferences appears twice with the same logic: in settings, not duplicating systemwide options inside the app; in undo-and-redo, always preferring the undo mechanisms already supported by the system (Edit menu, shortcuts, shake) over custom buttons (settings, undo-and-redo).
4. The predictability of an action's result is treated as a design requirement, not as a copy detail: the undo-and-redo text explicitly asks that the person be able to predict the effect before acting, and that the result stay visible even outside the current screen area (undo-and-redo).
5. Apple treats the user's body as a design variable in physical contexts: in workouts, large font and high contrast exist because the person is moving, not for aesthetic preference (workouts).
6. Brand elements with fixed meaning (Activity rings) are cited as a resource to reuse, but with the caveat of using them "only for the documented purpose", indicating that Apple protects the semantics of its own components against free reuse (workouts).
7. Each article has a "Platform considerations" section that treats the absence of a platform as relevant information ("Not supported in..."), not as an omission; this appears in undo-and-redo (not supported in tvOS and watchOS) and in workouts (not supported in macOS, tvOS and visionOS), reinforcing that the design of a feature is always conditioned by the platform, not universal by default.
8. Even in advanced features (multibatch undo, workout session, settings panel on macOS), the fallback guidance is always the same: less interruption to the person's main flow, whether by avoiding opening a separate window or avoiding forcing undo action by action (settings, undo-and-redo, workouts).
9. In none of the three articles does Apple define a numeric reference value (size, time, contrast); the precision required in these cases is one of behavior and decision hierarchy, not visual measurement, which contrasts with HIG visual component articles that usually bring pt/px.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/settings.md, 52 lines read, to the end: yes (file ends in the "Change log" section).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/undo-and-redo.md, 37/38 lines read, to the end: yes (file ends in the "Videos" section).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/workouts.md, 40/41 lines read, to the end: yes (file ends in the "Videos" section).
