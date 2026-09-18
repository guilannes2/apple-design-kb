# Inputs

## Action button (slug: action-button)

### What it governs
Governs the behavior of the Action button on iPhone and Apple Watch: how an app offers a quick action to this configurable physical button, and how it responds to single or combined presses.

### Why
The central idea is to give instant access to a function the person already uses frequently, in the same spirit as talking to Siri or tapping into Spotlight. Apple avoids having the app "re-teach" what the system already teaches: since the system shows on its own how to configure the button, the app should not repeat that guidance or compete with it.

### Do and avoid
- Offer a set of the app's essential functions for the Action button.
- Don't create an App Shortcut just to open the app: the icon, widgets and Apple Watch complications already cover that.
- Write a short label for each action, in title case, starting with a verb, in the present tense, without articles or prepositions.
- Keep the label to three words at most (example given: "Start Race" instead of "Started Race" or "Start the Race").
- Let the system explain how to use the Action button with the app; don't repeat that guidance on your own.
- On iOS, keep the person in the current context: use Live Activities and snippets instead of opening the whole app.
- On watchOS, prefer that the second press continue or advance the action, rather than interrupting it.
- Think carefully before offering more than one secondary function on watchOS, because that increases cognitive load.
- To stop a task (not just pause it), offer that option inside the interface itself, not via the button.
- Pause the current function when the person presses the Action button together with the side button, except in diving apps, where pausing can be dangerous.

### Exact specifications
No number, measurement or duration is given in the text for this article.

### Platform differences
Supported only on iOS (iPhone) and watchOS (Apple Watch); not supported on iPadOS, macOS, tvOS or visionOS. On Apple Watch Ultra, the button also covers activity-related actions, including workouts and dives.

### Links to other articles
Workouts, Digital Crown, App Shortcuts, Live Activities.

<!-- visual:action-button -->
### What the illustrations show
Basis: 1 illustration sheet viewed (1 image, in light appearance), code checked; no videos.
- The only illustration is a sketch in purple over a pink-to-lilac gradient: a short horizontal arrow points to the right, toward an inverted L shape (a short vertical segment that curves and ends in a horizontal stroke), a reading that suggests the side of the watch with the button on the edge (img 0024).
- Over the drawing there is a dotted construction grid with a circle and rectangles, plus diagonal, vertical and horizontal axes centered on the point where the arrow meets the L shape (img 0024).
- The piece follows the same sketch-with-geometric-grid pattern seen in the accessibility page icon, changing the palette to gradient shades of purple (img 0024).
<!-- /visual:action-button -->

## Apple Pencil and Scribble (slug: apple-pencil-and-scribble)

### What it governs
Governs how an iPad app should respond to Apple Pencil as a marking instrument and pointer, and how Scribble converts handwriting into text in any text field.

### Why
Apple anchors the design in the behavior of real-world marking instruments: the person already has expectations of how physical pencils and pens work, and the app should honor those expectations instead of requiring a special mode. The central priority is the feeling of direct, immediate connection between the tip of the Pencil and the content on the screen, without accidental gestures that cause data loss.

### Do and avoid
- Let the person switch freely between Apple Pencil and their finger; controls that don't respond to the Pencil feel broken.
- Allow making a mark the instant the Apple Pencil touches the screen, without requiring a button tap or mode switch first.
- Use tilt (altitude), force (pressure), orientation (azimuth) and barrel roll to vary the thickness and intensity of the stroke.
- When responding to pressure, prefer affecting continuous properties, such as ink opacity or brush size.
- Make sure the Pencil appears to directly manipulate only the content it touches; avoid disconnected actions in other parts of the screen.
- Design for use with the left hand and the right hand; avoid positioning controls where either hand could cover them, and consider allowing them to be repositioned.
- On hover, show a preview of the dimensions and color of the mark the current tool will make; avoid continuously changing the preview as the distance changes.
- Don't use hover to start an action, especially a destructive action.
- Prefer showing a preview value near the middle of the dynamic range, not at the extremes.
- Consider using hover to reveal interactions close to where the person is marking, such as a size menu when using Squeeze or a modifier key.
- Prefer restricting the hover preview to Apple Pencil, not to a pointing device, to avoid confusion.
- Respect the person's setting for the double-tap gesture (switch tool/eraser, current/previous tool, show/hide color picker, or nothing); if the system's default behavior doesn't make sense in the app, it's still possible to use the gesture to switch interaction mode.
- If offering custom double-tap behavior, give a control for the person to choose that mode, but don't turn it on by default.
- Avoid using double tap for an action that modifies content, especially a destructive action that's hard to undo.
- Treat squeeze (Apple Pencil Pro) as a single, quick gesture, with a discrete action, not a continuous one; display the result promptly and near the tip of the Pencil.
- Define squeeze actions that are non-destructive and easy to undo.
- Use barrel roll only to modify the type of mark (for example, rotating the angle of a marker), not for navigation or to display other controls.
- With Scribble, let the person write anywhere text is accepted, without needing to tap or select the field first.
- Make Scribble available everywhere it makes sense to write, even outside a formal text field (example: creating a reminder by writing below the last item).
- Avoid displaying autocomplete text while the person writes, since it can interfere visually; hide placeholder text as soon as writing begins.
- Keep the text field still while the person writes; if moving or resizing can't be avoided, defer the change until writing pauses.
- Avoid automatic text scrolling while the person writes or edits, so as not to disrupt text selection.
- Give enough room to write; grow the text field before or when the person pauses writing, never during writing.
- In PencilKit, avoid Dark Mode's dynamic color adjustment when the person draws over existing content (such as a PDF or photo), to keep the marking sharp.
- Consider custom undo and redo buttons in a compact environment, since the standard tool picker only includes them in a regular environment; also consider supporting the standard three-finger gesture for undo/redo in any environment.

### Exact specifications
No numerical value is given in the body of the article's text. The images describe an Apple Pencil tilted 45 degrees from a horizontal line (according to the image description), but this is not presented as an interface specification in the text.

### Platform differences
Feature exclusive to iPadOS; not supported on iOS, macOS, tvOS, visionOS or watchOS.

### Links to other articles
Entering data (Undo and redo is cited within the text for the three-finger gesture).

<!-- visual:apple-pencil-and-scribble -->
### What the illustrations show
Basis: 4 illustration sheets viewed (13 images, all in light appearance), codes checked; no videos.
- The opening is a zigzag scribble with variable thickness, in dark purple over a pink-to-purple gradient, with a rectangular grid and construction circle overlaid (img 0147).
- Altitude: the tilted Pencil rests its tip on a plane indicated by a gradient blue shadow, darker near the tip, and an arc of dotted blue strokes on the right marks the tilt angle from horizontal (img 0148).
- Pressure: the drawn line starts thin and light gray and gradually thickens and darkens until it becomes black and thick near the tip; a gradient blue triangle below repeats the idea of increasing intensity from left to right (img 0149).
- Azimuth: the Pencil balances on its tip over a dotted blue circle with degree markings all the way around, and a darker mark at one point indicates the orientation (img 0150).
- Each physical property gets its own graphic measurement system (arc, progressive thickness, degree circle), all in the same accent blue color (img 0148, img 0149 and img 0150).
- For two-handed use, the iPad in landscape has three stacked blue circular controls on each side edge (eyedropper, brush, comment); the left hand with the Pencil in the bottom left corner covers part of the controls on that side, and the right hand, in the other image, covers the ones on the right side (img 0151 and img 0152).
- The hover preview is a blue ellipse under the Pencil's tip hovering over a gray rectangle, in three sizes: small, at the low extreme, marked with a gray X; medium, near the middle of the range, marked with a green check; large, at the high extreme, shown with no badge (img 0153 to img 0157).
- In Scribble, two stacked "Name" fields compare width: the narrow one cuts off the handwriting and gets a gray X on the left; the wide one fits the whole name and gets a green check on the left, with the badges next to the field itself (img 0158).
- The set of drawing commands changes arrangement between environments: on the iPad in landscape, a full bottom bar with undo and redo on the left, illustrated pens and brushes, a color picker with a larger active black circle among smaller swatches, and add and more options on the right; on the iPhone in portrait, the top bar carries back, undo, more options and an orange confirmation circle, and below sits only a reduced palette with brushes and color, with no undo at the bottom edge (img 0159).
Recorded divergences: the official description of img 0151 and img 0152 speaks of controls obscured in gray and controls on the other side highlighted, but in the images viewed, all six controls have the same solid blue, with no opacity difference between the sides.
<!-- /visual:apple-pencil-and-scribble -->

## Camera Control (slug: camera-control)

### What it governs
Governs how a camera app uses the physical Camera Control button on iPhone 16 and iPhone 16 Pro to open the camera experience and adjust values through an overlay with sliders and pickers.

### Why
The overlay exists to give quick access to adjustments without overloading the viewfinder with duplicated controls; Apple prioritizes a large, distraction-free viewfinder, since people appreciate as clean a capture preview as possible.

### Do and avoid
- Use SF Symbols to represent the function of each control; the system does not support custom symbols. The symbols do not represent the control's current state.
- Keep control names short, because labels follow Dynamic Type sizes and long names can obscure the viewfinder.
- Include units or symbols alongside a slider's value (for example, EV, %, or a custom string) to give context.
- Define prominent values for a slider, that is, the most chosen values or ones evenly spaced, such as the main increments of the zoom factor; the system makes it easier to stop at those values.
- Leave room for the overlay in the viewfinder; position the app's UI outside the areas the overlay occupies, both in portrait and landscape.
- Minimize distractions in the viewfinder: avoid duplicating controls (sliders, toggles) in the app's UI when the system overlay displays them.
- Enable or disable controls according to the camera mode (for example, disable video controls when taking photos); it is not possible to remove or add controls at runtime.
- Position frequently used controls closer to the center, for quick access, and less used ones at the edges; the system remembers the last control used in the app when the overlay is reopened.
- Allow launching the app's experience from anywhere, including the locked device, by creating a locked camera capture extension.

### Exact specifications
No number, measurement, duration or proportion is given in the text.

### Platform differences
Supported only on iOS (iPhone 16 and iPhone 16 Pro); not supported on iPadOS, macOS, watchOS, tvOS or visionOS.

### Links to other articles
SF Symbols, Controls.

<!-- visual:camera-control -->
### What the illustrations show
Basis: 4 illustration sheets viewed (16 images, all in light appearance), codes checked; no videos.
- The opening draws the iPhone's silhouette in a thick dark purple outline over a pink to purple gradient, with a wide arrow pointing to the device's bottom right edge, where the button sits, under a dashed grid and guide circle (img 0200).
- An annotated diagram over the iPhone drawing uses two callout lines: one points to the physical button as a small horizontal strip on the edge, the other points to the gray area just below as the region where the overlay appears, making explicit the spatial relationship between the two (img 0201).
- The overlay lives in a black strip at the top of the screen: a row of five control icons, with the active one highlighted in orange and its name, "ZOOM", in orange centered below the row (img 0202).
- The slider has its own design: a ruler of thin white vertical dashes with a thicker orange dash at the center and the value in orange below; zoom ("1x") and exposure ("0 EV") use exactly the same ruler, changing only the value's label (img 0203, img 0205 and img 0206).
- The picker is a row of four short dots, with the chosen option filled in orange and larger than the gray ones, and the option's name spelled out in orange below (img 0204).
- In the row of icons, the active control stands out by color and by size: the flash's filled bolt and the filters' three overlapping circles appear in orange and larger than their neighbors, with "FLASH" and "FILTERS" as labels (img 0207 and img 0208).
- Value pair with context: the ruler with "1 EV" gets a green check, and the same ruler with just "1", without a unit, gets a gray X; the design is identical and only the label text varies (img 0209 to img 0212).
- In the same side by side night lake scene, the row of icons and the "ZOOM" label form a horizontal strip at the top in portrait and migrate to the right side in landscape, with the white shutter changing position, keeping the overlay next to the physical button's edge (img 0213).
- Clean viewfinder against duplicated viewfinder, in the same framing: in the first there is only the "1x" label in orange in the top left corner and the central white shutter; in the second the app repeats zoom values stacked vertically to the left of the shutter ("2", "1x" in orange, ".5"), in addition to the top label (img 0214 and img 0215).
- The language repeats across the overlay's controls: active item in orange, accompanied by a label in orange right below, whether icon, ruler or dots (img 0202 to img 0209).
<!-- /visual:camera-control -->

## Digital Crown (slug: digital-crown)

### What it governs
Governs the use of the Digital Crown as physical input on the Apple Vision Pro (volume, immersion, recentering, accessibility, exiting the app) and on the Apple Watch (primary navigation from watchOS 10, scrolling, data inspection).

### Why
On the Apple Watch, the Digital Crown takes on the role of primary navigation because lists, tabs and pages are organized vertically, and turning the crown is the most natural way to move through them without blocking the screen with a finger. Tactile feedback through detents exists to give scrolling a physical feel, reinforcing the perception of progress.

### Do and avoid
- Anchor the app's navigation to the Digital Crown from watchOS 10; always reinforce these interactions with on-screen touch equivalents.
- Consider using the Digital Crown to inspect data when navigation is not necessary (example given: in World Clock, turning the crown advances the time of a selected location).
- Provide visual feedback in response to interactions with the Digital Crown; without this feedback, people assume that turning the crown has no effect.
- Update the interface at the same speed the person turns the Digital Crown, to give precise control; avoid updating at a pace that makes it hard to select values.
- Use the standard haptic feedback when it makes sense in the app; disable detents if they do not match the app's animation, and consider switching from per-row detents to linear detents in tables with rows of very different heights.
- Do not respond to presses on the Digital Crown: watchOS reserves this interaction for system functionality, such as revealing the Home Screen.

### Exact specifications
No number, measurement or duration is given in the text.

### Platform differences
Supported on visionOS (Apple Vision Pro) and watchOS (Apple Watch); not supported on iOS, iPadOS, macOS or tvOS. On the Apple Vision Pro, visionOS apps do not receive direct information from the Digital Crown; it serves system functions (volume, immersion, recenter, Accessibility, exiting the app).

### Links to other articles
Feedback, Action button, Immersive experiences.

<!-- visual:digital-crown -->
### What the illustrations show
Basis: 1 illustration sheet viewed (3 images, all in light appearance), code checked; no videos.
- The opening, in a purple and magenta gradient with dotted grid and guide circle, draws the crown seen from the side as an oval shape with horizontal grooves for the knurling and, on the left, a thick curved arrow pointing up and to the left that suggests the turn; crown and arrow are contained within the central guide circle (img 0461).
- On the Apple Vision Pro, a real close-up profile photograph shows the index finger over the small, knurled circular button on the side, between the temple's fabric strap and the visor, with no screen or interface visible (img 0462).
- On the Apple Watch, the real photograph of the watch with the sleep app active (blue bar chart of stages) gets a red outline around the crown, and the side button just below is left unhighlighted, isolating exactly which control is the Digital Crown (img 0463).
- The page combines a schematic opening icon with real product photos on two devices: on the Vision Pro the crown is indicated by the finger resting on it, and on the Apple Watch by a red outline drawn over the photo (img 0461, img 0462 and img 0463).
<!-- /visual:digital-crown -->

## Eyes (slug: eyes)

### What it governs
Governs how gaze works as an interaction target in visionOS: how the system highlights an element when the person looks at it (hover effect) and how to design components that are easy to target with the eyes.

### Why
Privacy is an explicit principle: visionOS does not tell the app where the person is looking before a tap, to preserve privacy; the app only knows when the component is actually activated. Design for visual comfort seeks to avoid quick, repeated eye adjustments, because that tires and distracts; rounded shapes help because the eye tends to be drawn to corners, making it harder to keep focus on the center of a shape.

### Do and avoid
- Always give people more than one way to interact with the app, supporting accessibility features.
- Design for visual comfort: keep the necessary objects within the field of view; avoid requiring multiple quick eye adjustments, whether from a large area or from multiple depth levels.
- Position content at a comfortable viewing distance; for reading or prolonged engagement, aim for at least one meter of distance.
- Prefer using the system's standard UI components, which respond consistently to gaze.
- Minimize visual distractions; movement (especially in peripheral vision) involuntarily draws the gaze, so revealing content near what the person is looking at can divert their attention.
- Give enough space around each item to make it easier to target: use a margin of at least 16 points around each item's bounds, or position items so their centers are always at least 60 points apart.
- Avoid repetitive patterns or textures that fill the field of view, since the eyes can lock onto different elements, giving the impression of distinct depths.
- Consider subtle visual cues to encourage the person to look at the most likely item (position near the center of the field of view, smooth movement, increased contrast, variations in color or scale); prefer cues that are noticeable without being exaggerated.
- Prefer rounded shapes for interactive items, because the eye is drawn to corners.
- In components made up of more than one element, define an overall containing shape that visionOS can highlight as a whole.
- When creating custom hover effects, define two states (with and without the effect); the system decides when to apply the effect outside the app's process, so the app does not know the exact moment and cannot run code that depends on knowing when the person is looking.
- Prefer a custom hover effect to emphasize a special moment in the experience; too many custom effects dilutes the impact, distracts and can cause visual discomfort.
- Choose the right delay: no delay (default) for subtle effects or ones that invite interaction; short delay when the person needs to look and interact quickly (such as the expansion of tabs in a tab bar); longer delay when the effect shows additional information, such as a tooltip.
- Keep one or more of the element's primary views unchanged between the two states of the hover effect, to give visual stability.
- Thoroughly test custom hover effects, preferably using the Apple Vision Pro.

### Exact specifications
- Minimum margin around each interactive item: 16 points.
- Alternative: item centers always at least 60 points apart from each other.
- Comfortable viewing distance for reading or extended use: at least 1 meter.

### Platform differences
Exclusive to visionOS; not supported on iOS, iPadOS, macOS, tvOS or watchOS.

### Links to other articles
Immersive experiences, Gestures, Spatial layout, Accessibility, Depth, Focus and selection.

<!-- visual:eyes -->
### What the illustrations show
Basis: 2 illustration sheets (5 images, in light appearance) and 3 video sheets (24 frames from a video) viewed, codes checked.
- The opening draws a front-facing eye in a dark purple stroke, with an almond-shaped outline, a filled circular iris and a smaller pupil left hollow in white, centered and inscribed in the guide circle of the dotted grid over a pink and purple gradient (img 0473).
- The shape comparison uses the same outer medium gray square, with the same color and size, and varies only the lighter inner area: a square with straight corners in one version, a circle in the other (img 0474 and img 0476).
- The badges are in separate images: a white X in a light gray circle for the square version and a white checkmark in a green circle for the circular version (img 0475 and img 0477).
- In the video, the visionOS Settings app appears in passthrough over a real room with a guitar, a window with blinds and an armchair; the screen has two columns, a side list on the left with General selected and a detail panel on the right (video eyes 009, sheet 0001, q001).
- The two panels are translucent cards with rounded corners floating over the environment; inside the detail panel, the items group into smaller rounded blocks that bring together related pairs, such as About with Software Update and AirDrop with Handoff, with a thin separator between items in the same block (video eyes 009, sheets 0001 to 0003).
- The typographic hierarchy brings the title "General" in emphasis at the top of the panel and the items in smaller white text below, and it does not change throughout the clip (video eyes 009, sheet 0002, q010 to q018).
- Between q001 and q024 the camera, the side list and the groups never change position; the only variation is a subtle difference in brightness in one row at a time of the detail panel, consistent with hover moving from row to row (video eyes 009, sheets 0001 to 0003).
- The hover does not move or resize anything: it only changes the background highlight of the targeted row, without recomposing the rest of the screen (video eyes 009, sheet 0002, q010 to q018).
Recorded divergences: the official description talks about several settings receiving hover in sequence as the gaze moves; at the resolution of the frame grid it was not possible to identify with confidence which row is highlighted in each frame.
<!-- /visual:eyes -->

## Focus and selection (slug: focus-and-selection)

### What it governs
Governs how focus (the visual indicator of which component an interaction will affect) works in component-based navigation, using inputs such as remote, game controller or keyboard, and how focus differs from selection.

### Why
Focus exists so that the person always knows where they are within the app; changing focus without the person's interaction forces them to spend time looking for the newly focused item, delaying the task. That is why relying on the system's focus effects guarantees consistency and predictability, since these effects have been precisely tuned for interactions with Apple devices.

### Do and avoid
- Rely on the focus effects provided by the system; consider creating custom effects only if absolutely necessary.
- Avoid changing focus without the person's interaction. The exception is when the person is moving focus with a device that has discrete, directional movements (keyboard, remote, controller) and the previously focused item disappears: in that case, moving focus to a nearby item is acceptable; outside that scenario, it is better to simply hide the focus indicator.
- Be consistent with the platform when bringing focus to items: on iPadOS and macOS, Full Keyboard Access covers buttons, sliders and toggles, so the app only needs to support focus for content elements (list items, text fields, search fields); on tvOS, the app needs to ensure that every onscreen element is reachable by focus.
- Indicate focus with visual appearances consistent with the platform (example: on iPadOS/macOS, white text and a background highlight in the app's accent color for focused items in a list, and default text color with gray highlight for unfocused items).
- In general, use a focus ring for a text or search field, but use a highlight for a list or collection.
- On iPadOS 15 and later, the focus system supports keyboard interactions for navigating text fields, text views and sidebars, as well as collection views and other custom views.
- Avoid supporting keyboard navigation for controls such as buttons, segmented controls and switches on iPadOS; let Full Keyboard Access handle that.
- On iPadOS, pressing Tab moves focus between focus groups (areas such as sidebar, grid, list); pressing an arrow key supports directional focus, limited to navigation between items in the same focus group.
- Onscreen components can indicate focus through the halo effect (a customizable focus ring, applicable to custom views and to fully opaque content inside a cell) or through the highlighted appearance (the component's text uses the app's accent color; it occurs automatically when selecting a collection view cell with content configurations defined).
- Customize the halo effect when necessary; by default the system infers the shape of the halo from the shape of the item, but it is possible to adjust rounded corners, Bézier paths, or the position of the halo if another component occludes it.
- Ensure that focus moves through custom views sensibly; by default, focus traverses focus groups in reading order (from start to end, top to bottom); adjust by identifying a container as a single focus group when necessary.
- Adjust the priority of an item within a focus group to reflect its importance; when a group receives focus, its primary item also automatically receives focus.
- On tvOS, in a full-screen experience, let people use gestures to interact with the content, not to move focus, because the full-screen item does not show focus.
- On tvOS, avoid showing a pointer; people expect to navigate through a fixed number of items by changing focus, not by dragging a small pointer across a large screen. If the app requires a pointer, make sure it is clearly visible and well integrated.
- On tvOS, design the interface to accommodate components in multiple focus states (up to five visually distinct states: unfocused, focused, chosen, selected, unavailable); provide assets for the larger focus size, since focusing generally increases the scale of the item.

### Exact specifications
No number, measurement or duration is given in the text.

### Platform differences
- Not supported on iOS or watchOS.
- iPadOS 15+: focus system with Tab (between focus groups) and arrow keys (directional focus within the group); halo and highlight effects.
- tvOS: universal directional focus by swiping on the remote or keyboard arrow keys; up to five distinct visual states per focusable item.
- visionOS: uses the same focus system as iPadOS and tvOS for input by keyboard or connected game controller; the hover effect (gaze) is different from the focus system and is not related to it.

### Links to other articles
Eyes, Keyboards.

<!-- visual:focus-and-selection -->
### What the illustrations show
Basis: 3 illustration sheets viewed (9 images, all in light appearance), codes checked; no videos.
- The opening, in a pink-to-purple gradient with a rectangular and circular grid, shows in solid dark purple a thick ring with four small triangular arrows pointing outward (up, down, left, right) and a filled disc at the center, a shape that evokes locking focus (img 0481).
- On iPadOS, in a grid of six photos in two rows and three columns, the focused photo receives a thick, continuous blue halo that follows the rectangle of the cell, with straight corners and hugging the edge of the photo (img 0482).
- In the same grid, the halo variant has rounded corners and sits slightly away from the edge of the photo, with visible breathing room; the shape changes between the two versions, the blue color remains (img 0482 and img 0483).
- In the highlighted list appearance, among seven items with an empty star and "Title", the second one gets a rounded light gray background, the star goes from outline to filled and the icon and text turn red, the app's accent color, all without halo or elevation; the rest stay black on white, with no highlight (img 0484).
- On tvOS, the states are shown with the same pill-shaped button, at the same point on the same beach photo, varying one thing at a time: unfocused, the pill is translucent gray, lets the sand texture show through faintly, has black text and is the smallest in the series (img 0485).
- Focused, the pill turns opaque white, with no transparency, and becomes larger, with large black text (img 0486).
- Highlighted and selected also use an opaque white pill with black text, at a size visually similar to the focused button (img 0487 and img 0488).
- Unavailable returns to the translucent gray background and uses grayish text with much lower contrast, the dimmest button in the sequence (img 0489).
Recorded divergences: the official description says the highlighted button is the same size as the unfocused button, but in the image it appears to be the size of the focused button, with the caveat of the margin of error from reading it at thumbnail size (img 0487); the difference in shadow between states mentioned in the description is not distinguishable at the resolution viewed (img 0488).
<!-- /visual:focus-and-selection -->

## Game controls (slug: game-controls)

### What it governs
Governs how a game supports input from physical game controllers and from each platform's standard interaction methods (touch, remote, mouse and keyboard), including onscreen virtual controls, physical button mapping and game-specific keyboard shortcuts.

### Why
Apple recommends supporting both physical controllers and the platform's standard methods because not every player has access to a physical controller, and because players value being able to use the interaction method they are already familiar with; the goal is to reach the broadest possible audience.

### Do and avoid
- Decide whether it makes sense to show virtual controls over the game content; try to reduce overlap by associating actions with direct in-game gestures when possible (example: tapping objects to select them instead of a virtual selection button).
- Position virtual buttons where they are easy to reach, respecting device limits, guides and safe areas; do not overlap the Home indicator or the Dynamic Island on iPhone; position frequently used buttons near the player's thumb, avoiding the circular regions for movement and camera; position secondary controls (such as menus) at the top of the screen.
- Ensure minimum control size: 44x44 pt for frequently used controls, 28x28 pt for less important controls, such as menus.
- Always include visible and tactile pressed states; combine the pressed state with sound and haptics.
- Use symbols that communicate the action the button performs (for example, a weapon for attack); avoid abstract shapes or naming based on the physical controller, such as A, X or R1.
- Show and hide virtual controls according to gameplay, reducing visual clutter and helping the player focus (example: hiding movement controls until the player touches the screen).
- Combine functionality into a single control; consider redesigning mechanics that require pressing multiple buttons simultaneously or in sequence; take advantage of gestures such as double tap and touch and hold for variations of the same action.
- Map movement to the left side of the screen and camera to the right side, as expected; use the largest possible input area; for movement, prefer showing a virtual thumbstick where the thumb lands, instead of a fixed position; for camera, prefer direct touch instead of a virtual thumbstick.
- Support the platform's standard interaction method as an alternative to physical controllers, since a game controller is an optional purchase.
- On tvOS and visionOS, it is possible to require a physical game controller; the App Store displays a "Game Controller Required" badge in that case; even so, check for the controller's presence and request its connection gracefully, since the person may open the game without one connected.
- Automatically detect whether a controller is paired and obtain its profile, instead of requiring manual configuration.
- Customize onscreen content to match the connected controller, since actual colors and symbols may differ from the Game Controller framework's standard names.
- Map controller buttons to the expected UI behavior outside of gameplay: A activates a control; B cancels an action or goes back to the previous screen; left shoulder navigates left between screens or sections; right shoulder navigates right; left/right thumbstick and directional pad move selection; Home/logo is reserved for system controls; Menu opens game settings or pauses gameplay. The X, Y, left trigger and right trigger buttons have no standardized UI behavior defined.
- Support multiple connected controllers, using labels and glyphs that match the controller actively in use; in multiplayer, use labels and symbols specific to each player's controller.
- Prefer symbols, not text, to refer to game controller elements, since the Game Controller framework provides SF Symbols for most elements.
- On the keyboard, prioritize single-key commands, which are faster and easier, especially during simultaneous use of a mouse or trackpad; test the comfort of the key binding on an Apple keyboard, considering remapping Control (^) to Command (⌘) when coming from a non-Apple keyboard; take into account the physical proximity of keys when defining related commands (example: number keys for inventory categories); let players customize the key bindings.
- On visionOS, make the spatial game controller (such as the PlayStation VR2 Sense) behave similarly to hand input: support looking at an object and pressing the left or right trigger for indirect interaction, or reaching and pressing the trigger for direct interaction.

### Exact specifications
- Minimum size of frequently used virtual controls: 44x44 pt.
- Minimum size of less important virtual controls (menus): 28x28 pt.

### Platform differences
No additional platform-specific considerations for iOS, iPadOS, macOS or tvOS beyond what has already been described; not supported on watchOS. On visionOS, there is specific guidance for spatial game controls and correspondence with hand input.

### Links to other articles
Designing for games, Gestures, Keyboards, Playing haptics, Touch Controller, Game Controller.

<!-- visual:game-controls -->
### What the illustrations show
Basis: 3 illustration sheets viewed (10 images, all in light appearance), codes checked; no videos.
- The opening draws a directional cross in solid dark purple outline, inscribed in the guide circle of the construction grid, over a gradient from pink to purple (img 0513).
- The pressed state of a virtual button appears in line art: the right hand holds the iPhone in landscape and the thumb presses the button with X, which becomes darker, filled and with a thicker outline than the triangle and square buttons beside it, with an extra line around it suggesting glow; a larger circular button occupies the bottom left corner (img 0515).
- The virtual buttons in this illustration reuse the language of physical controls, with triangle, square and X symbols in a column (img 0515).
- The mapping from input to action is drawn as two gray circles linked by an arrow: the controller button with the square symbol leads to the in-game action represented by a hand making a grabbing gesture, each side with its own text label (img 0516).
- The same virtual thumbstick, in the same scene and framing, changes with use: in motion it becomes opaque white and clearly visible, with a small curved arrow indicating direction; at rest it turns translucent dark gray, with no highlighted outline or arrow (img 0517 and img 0518).
- Simple tap and touch and hold are differentiated on the same gray button with a flame icon: the first has a complete ring around it, the second a partial ring, like an incomplete circular progress indicator (img 0519).
- The screen split is done over a single game image cut in half by colored frames: left half with a red border for movement controls, right half with a cyan border for camera controls (img 0520).
- The diagram of the physical controller, in light gray outline seen from the front, labels the shoulder buttons, triggers and thumbsticks in left and right pairs (the left one higher, the right one lower), plus the small menu button at the top center and the directional cross; the four action buttons on the right, in a diamond, are left unlabeled (img 0521).
- The SF Symbols app on the Mac appears with the Gaming category selected in the sidebar, 234 symbols, in a grid of icons with the technical name under each one (img 0522).
Recorded divergences: the official description of img 0514 talks about a diagram with the ideal positioning of touch controls, but the image viewed is entirely blurred and no marking, arrow or positioning zone is legible.
<!-- /visual:game-controls -->

## Gestures (slug: gestures)

### What it governs
Governs the vocabulary of physical gestures (tap, swipe, drag and others) that people use to directly manipulate objects in an app or game, on touch-sensitive screens, in the air, or on input devices such as trackpad, mouse, remote or a game controller with a touch surface.

### Why
Consistency is the central principle: since people expect most gestures to work the same way regardless of context, using a familiar gesture for an action exclusive to the app (or inventing a unique gesture for a standard action) breaks that expectation. Custom gestures are only justified for specialized, frequent tasks that standard gestures don't cover.

### Do and avoid
- Give the person more than one way to interact with the app, since many prefer or need to use voice, keyboard or Switch Control; don't assume that a specific gesture is always available.
- Respond to gestures consistently with people's expectations; avoid using a familiar gesture like tap or swipe for an action exclusive to the app, and avoid creating a unique gesture for a standard action, like activating a button or scrolling a view.
- Treat gestures with as much responsiveness as possible, providing feedback that helps predict the outcome and, if necessary, communicate the extent and type of movement required.
- Clearly indicate when a gesture isn't available; without this communication, the person may think the app has frozen or that they're performing the wrong gesture.
- Add custom gestures only when necessary, for specialized, frequent tasks not covered by existing gestures (example: a game or drawing app); the custom gesture needs to be discoverable, simple to perform, distinct from other gestures, and never the only way to carry out an important action.
- Make custom gestures easy to learn, offering moments in the app to teach them and testing in real usage scenarios.
- Use shortcut gestures to complement standard gestures, not replace them; even with a shortcut, keep the familiar form (example: a Back button in the toolbar, in addition to an edge swipe gesture).
- Avoid conflicting with gestures that access the system UI, such as the edge swipe on watchOS or rolling the hand to access system overlays on visionOS.
- On iOS and iPadOS, consider allowing simultaneous recognition of multiple gestures when it improves the experience, such as in a game with a joystick and fire buttons operated at the same time.
- On visionOS, offer both indirect gestures (looking to focus and manipulate at a distance, such as quickly bringing finger and thumb together) and direct gestures (physically touching the object, working best within reach and for infrequent use, since keeping the arms raised is tiring).
- On visionOS, support standard gestures everywhere possible, even while offering custom gestures.
- On visionOS, prefer indirect gestures for UI and common components like buttons; reserve direct and custom gestures for objects that invite close-range interaction or game-specific movements.
- On visionOS, avoid requiring specific movements or body positions as the only form of input; consider alternative inputs.
- On visionOS, when designing custom gestures, prioritize comfort, continually testing ergonomics; avoid requiring the arms to be raised for a long time; be cautious with complex gestures involving multiple fingers or both hands, considering an alternative with less movement; avoid custom gestures that require a specific hand.
- On visionOS 2+, reserve the area around the person's hand for system overlays (Home and Control Center) and their gestures; avoid anchoring content to the hands or wrists, or position it outside the hand's immediate area; consider deferring the system overlay behavior in immersive apps, requiring a tap to reveal the Home indicator, when it makes sense to keep the person in the narrative.
- Use caution with custom gestures that involve rolling the hand, wrist and forearm, a movement reserved for revealing system overlays.
- On watchOS 11+, use double tap with care: avoid setting it as the primary action in views with lists, scroll views or vertical tabs, since it conflicts with standard navigation; choose the most used button in a view with no scrolling as the primary action (example: the play/pause button in a media controls view).

### Exact specifications
No numeric measurement (pt, px, ms) is given in the text; the specifications table lists only the standard gestures and the platforms on which each one is supported, with no values.

### Platform differences
- iOS, iPadOS: also support three-finger swipe (undo to the left, redo to the right), three-finger pinch (copy when pinching in, paste when pinching out), a four-finger swipe exclusive to iPadOS (switching between apps), and shake (undo/redo).
- macOS: primary interaction via keyboard and mouse; standard gestures also available on Magic Trackpad, Magic Mouse or a game controller with a touch surface.
- tvOS: standard gestures via a compatible remote, Siri Remote, or a game controller with a touch surface.
- visionOS: supports indirect and direct gestures; standard direct gestures include touch, touch and hold, touch and drag, double touch, swipe, two-handed pinch (zoom) and two-handed pinch with circular motion (rotate); there are also system gestures for overlays (Home, Control Center) via looking at the palm of the hand.
- watchOS: support for double tap starting with watchOS 11 to scroll lists and scroll views, advance between vertical tabs, and trigger a primary action defined by the app; it also works on custom notification actions, acting on the first non-destructive action.

### Links to other articles
Feedback, Eyes, Playing haptics, Accessibility, Apple Pencil and Scribble, Standard gestures (Pointing devices, Remotes, Game controls).

<!-- visual:gestures -->
### What the illustrations show
Basis: 2 illustration sheets (8 images, in light appearance) and 3 video sheets from two videos (6 and 11 frames, viewed in full), codes checked.
- The opening draws a hand in thick dark purple outline, with the index finger extended and the other fingers folded, and a curved line that starts at the base of the index finger, curves around the hand from behind and ends above it, suggesting a swipe in an arc to the right (img 0528).
- The custom gesture appears within the real context of a game on visionOS: a living room with a "14 score" scoreboard floating on the left and a media control bar, both hands forming a heart with thumbs and index fingers, and a pink and purple droplet-shaped glow effect coming out above the gesture as a visual response (img 0529).
- In simple line art, the open hand with the palm facing up has, above and around it, a dashed blue circle, larger than the hand itself, that marks the area reserved for system overlays (img 0530).
- The line art sequence separates the reveals: without the circle, a small gray circular button with a circle icon appears above the palm (img 0531); with the hand turned, back facing the viewer, a status pill appears above it with time, battery with percentage, Wi-Fi and a round volume button on the right (img 0532). The two reveals never appear in the same image.
- The simple line art is used to teach system zones and states, and the photography is used for behavior in context (img 0530 to img 0535).
- Standard in Shared Space and in Full Space: the same real hand, palm up and with the same gray button above it, is shown over a real room and then over an immersive forest; only the background changes (img 0533 and img 0534).
- Deferred behavior: the hand covered by a bulky white spacesuit glove, palm up over a starry sky, with no button above it (img 0535).
- Indirect gesture, first phase: in a bar of three circular buttons (share, heart, more) at the top of a translucent window, the background of the heart button progressively lightens from translucent gray to almost white, while the other two don't change and the icon stays grayed out, with no defined outline (video gestures 010, sheet 0001, q001 to q004).
- Indirect gesture, second phase: from q004 to q005 the button switches to a solid opaque white background with the heart in a sharp black outline, and stays that way at q006; at no point do position, size or the other buttons change. An inset in the bottom right corner shows, seen from above, two hands over a gray surface (video gestures 010, sheet 0001, q004 to q006).
- Direct gesture: in a room in passthrough, a red column with horizontal dividers, suggesting stacked blocks, sits on a light-colored tabletop; the hand appears at the bottom right edge at q003, approaches the base at q004 and, at q005, with fingers extended touching the base, two blocks spin in the air, one of them showing a white face; by q006 the hand has already left and three red cubes remain scattered side by side (video gestures 011, sheet 0001, q001 to q006).
- In the direct gesture there is no highlight or halo before contact, and the response is physical, with falling and rotation, instead of a change in appearance like the button in the indirect gesture (video gestures 011, sheet 0001, q004 to q006, compared to video gestures 010).
- From q006 to the end the cubes stay still, with slight camera reframings, and the clip ends with no 2D interface element on screen (video gestures 011, sheets 0001 and 0002, q006 to q011).
Recorded divergences: the official description of video 010 says the inset shows the hand making the indirect touch of thumb and index finger, but at the resolution viewed only two hands with a light area near the fingers can be made out, without confirming the exact gesture; in video 011 the description talks about three stacked blocks, and the initial count isn't legible in the frames because of the shadows and the uniform color, though the final result of three cubes is consistent.
<!-- /visual:gestures -->

## Gyroscope and accelerometer (slug: gyro-and-accelerometer)

### What it governs
Governs the use of the device's gyroscope and accelerometer data for real-time motion-based experiences.

### Why
The principle is to use motion data only when it brings a tangible benefit to the person; Apple discourages collecting data just for the sake of collecting it, and recognizes that motion-based gestures can be physically difficult for some people to replicate precisely, besides affecting battery life.

### Do and avoid
- Use motion data only to offer a tangible benefit (example: a fitness app using the data to give feedback on activity and overall health, or a game using it to improve gameplay).
- Provide text explaining why the app needs to access motion data; this text appears in the system's permission request on the first access attempt.
- Outside of active gameplay, avoid using accelerometers or gyroscopes for direct interface manipulation, since some motion-based gestures can be difficult to replicate precisely, physically challenging for some people, and affect battery use.

### Exact specifications
No number, measurement or duration is given in the text.

### Platform differences
Available on iOS, iPadOS and watchOS; tvOS apps can use gyroscope data from the Siri Remote. No additional platform-specific considerations beyond this; there is no mention of support on macOS or visionOS.

### Links to other articles
Feedback, Core Motion.

<!-- visual:gyro-and-accelerometer -->
### What the illustrations show
Basis: 1 illustration sheet viewed (1 image, in light appearance, no dark version in the batch), code checked; no videos.
- The opening icon draws the gyroscope as interlocking hollow rings, rather than as solid shapes: an outer circle and two oval links crossed in an X, in dark purple over a pink-to-purple gradient (img 0537).
- A straight diagonal stroke crosses the set corner to corner and suggests the gyroscope's rotation axis (img 0537).
- Over the drawing there is a fine grid of horizontal, vertical lines and a pair of diagonals, plus dashed concentric circles; it is a discreet construction guide, with no dimensions or numbers (img 0537).
- The card has rounded corners and a wide proportion, and the piece uses a single ink color over the gradient, which links the icon to one of the colors of the six-color logo within a chromatic system by section (img 0537).
<!-- /visual:gyro-and-accelerometer -->

## Keyboards (slug: keyboards)

### What it governs
Governs the use of a physical keyboard as essential input (text, games, app control) and standard and custom keyboard shortcuts, including Full Keyboard Access.

### Why
Standard keyboard shortcuts exist to function consistently across the whole system and in most apps, letting the person transfer the knowledge they already have to new experiences; that is why the general rule is not to reappropriate a standard shortcut, unless the original action simply does not make sense in the experience.

### Do and avoid
- Support Full Keyboard Access when possible (available on iOS, iPadOS, macOS and visionOS), allowing navigation and activation of windows, menus, controls and system features using only the keyboard.
- On iPadOS, avoid supporting keyboard navigation for controls such as buttons, segmented controls and switches; let Full Keyboard Access handle control activation, navigation to all onscreen components, and gesture-based interactions such as drag and drop.
- Respect the standard keyboard shortcuts that work in other apps and in the system; for a frequently used exclusive action, prefer creating a custom shortcut rather than reusing a standard shortcut associated with another action.
- In games, people expect certain standard shortcuts (such as Command-Q to quit), but also expect to be able to modify the key bindings of each game according to personal play style.
- In general, do not reappropriate standard keyboard shortcuts for custom actions; only consider redefining a standard shortcut if its original action does not make sense in the experience (example given: an app without text editing can reuse Command-I, normally Italic, for "Get Info").
- Define custom keyboard shortcuts only for the app's most-used specific commands; defining too many shortcuts can make the app seem hard to learn.
- Use modifier keys in the expected way (example: Command while dragging moves items as a group; Shift while drag-resizing constrains to the original proportion; holding an arrow key moves the selected item by the smallest unit defined by the app until the key is released).
- Prefer Command as the main modifier in a custom shortcut; use Shift as a complementary secondary modifier; use Option sparingly, for less common commands or advanced features; avoid using Control as a modifier, since the system uses it extensively in features and shortcuts throughout the system.
- Avoid using an additional modifier with characters that are not available on all keyboards; if you need a modifier other than Command, prefer using it only with alphabetic characters.
- List modifier keys in the correct order when there is more than one: Control, Option, Shift, Command.
- Avoid adding Shift to a shortcut that already uses the upper character of a two-character key (example: the Hide Status Bar shortcut is Command-Slash, and the Help shortcut is Command-Question Mark, not Shift-Command-Slash).
- Let the system localize and mirror shortcuts automatically as needed, including in right-to-left layouts.
- Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command (example: avoid Shift-Command-Z for something unrelated to undo/redo, since people associate Command-Z with undo).
- On visionOS, write descriptive shortcut titles, since the shortcuts interface shows a flat list by category, with no submenu titles to provide context.

### Exact specifications
The full table of standard macOS shortcuts is reproduced in the text (for example, Command-Space for Spotlight, Command-C to copy, Command-Q to quit, etc.), with no associated numeric measurement values, these are key combinations, not physical measurements. The correct order of modifiers in a custom shortcut is: Control, Option, Shift, Command.

### Platform differences
No additional platform-specific considerations for iOS, iPadOS, macOS or tvOS beyond what is described; not supported on watchOS. On visionOS, keyboard shortcuts appear in a shortcuts interface displayed by holding down the Command key on a connected keyboard, organized like the iPad or Mac menu bar, but showing all relevant categories in a single view; when a physical keyboard is connected on visionOS, the system displays a virtual keyboard overlay with autocomplete and other controls.

### Links to other articles
Virtual keyboards, Entering data, Pointing devices, Game controls, Focus and selection, Right to left.

<!-- visual:keyboards -->
### What the illustrations show
Basis: 2 illustration sheets (5 images, in light appearance) and 2 video sheets (10 frames, visionOS section) viewed, codes checked.
- The opening draws a keyboard seen from above: a rectangle with rounded corners with rows of square keys and one long key at the bottom as a space bar, on a purple card in gradient, with a rectangular dotted grid and a large centered circle, the same construction scheme as the openings seen in blue and yellow (img 0671, compared to img 0644 and img 0667).
- The four modifier glyphs form a single set: thin black outline, no fill and no color, isolated on a white background, in proportion similar to each other and much smaller than the opening illustration (img 0672 to 0675).
- Command is a four-loop clover connected by straight lines, and Shift is an upward arrow in outline, with a narrow rectangular body and a triangular tip (img 0672, img 0673).
- Option is made of segments in a lying-down Z with a short horizontal stroke aligned to the top, and Control is a shallow, wide inverted V, like a flattened circumflex (img 0674, img 0675).
- The static material is limited to the icon and the glyphs: no image shows an app screen, a full physical keyboard or a shortcuts table (img 0671 to 0675).
- In the video, the scene is real and domestic: a round light wood table seen from above, a white physical keyboard and white trackpad, hands typing; the only visionOS interface element is a narrow, dark brown, translucent bar, floating above the keyboard, with small white text in the center and controls at the ends (video 014, sheet 0001, q001 to q009).
- The text inside the bar changes with every frame as the fingers change position, which appears to be real-time typing, although the text is too small to read with confidence (video 014, sheet 0001, q001 to q003).
- The bar varies slightly in width between frames, narrower in q004 and q005 and a bit wider in q006, keeping the text centered (video 014, sheet 0001).
- The bar's position stays fixed relative to the keyboard, above and a bit to the left, from the first to the last frame, while the hands change pose without moving from place; the notes read this as the overlay taking the physical keyboard, not the hands, as its spatial reference (video 014, sheet 0001 q001 to sheet 0002 q010).
Recorded divergences: the official description talks about a virtual window with the typed text and suggestions, but the 10 frames show only a narrow strip, with no large window or separate suggestions list; the bar's text is too small to read, so the suggestions can only be confirmed by the bar's presence, not by its content.
<!-- /visual:keyboards -->

## Nearby interactions (slug: nearby-interactions)

### What it governs
Governs experiences that integrate the presence of nearby people and objects using Ultra Wideband hardware and the Nearby Interaction framework, such as transferring audio by bringing devices close together.

### Why
The central principle is to root the interaction in people's natural physical perception of the world around them: Apple looks for inspiration by observing how the task would work in the physical world, and prioritizes nearby, contextually relevant information to create experiences that feel organic. Privacy is preserved through randomly generated device identifiers that last only for the duration of the interaction session.

### Do and avoid
- Consider the task from the physical world's perspective to find inspiration (example: physically bringing devices close together to transfer a song, instead of using only the app's UI).
- Use distance, direction and context to inform the interaction, prioritizing nearby, contextually relevant information (example: the iOS share sheet suggesting the closest contact facing forward using information from devices with the U1 chip).
- Consider how changes in physical distance can guide the interaction, mirroring the expectation that perception of an object sharpens as you get closer to it (example: when searching for an AirTag, the display transitions from a directional arrow to a pulsing circle as the person gets closer).
- Provide continuous feedback that reflects the dynamism of the physical world and reinforces the connection between the interaction and the task (example: continuous updates of direction and proximity when searching for a lost item in Find My).
- Consider using multiple types of feedback (visual, audible, haptic) for a more holistic experience, coordinating the type of feedback with the task and the current context (visual when the person interacts with the screen; audible and haptic when interacting with the environment).
- Avoid using a proximity interaction as the only way to accomplish a task, since not everyone can experience it.
- Encourage the person to hold the device in portrait orientation, since holding it in landscape can reduce the precision and availability of distance and direction information; if the feature only supports portrait, prefer giving implicit visual feedback rather than instructing explicitly.
- Design for the device's directional field of view, since the sensor has a specific field of view, similar to that of the Ultra Wide camera on iPhone 11 and later; outside that field, the app can receive distance but not relative direction.
- Help the person understand how objects in between (people, animals, large objects) can reduce the precision or availability of the information; consider adding guidance about this in onboarding or a tutorial.

### Exact specifications
No number, measurement or duration is given in the text.

### Platform differences
No additional considerations for iPadOS; not supported on macOS, tvOS or visionOS. On iOS (iPhone), the Nearby Interaction APIs provide distance and direction to a peer device. On watchOS, they provide only distance, and every watchOS app participating in a proximity interaction must be in the foreground.

### Links to other articles
Feedback, Ultra Wideband availability, Nearby Interaction (framework).

<!-- visual:nearby-interactions -->
### What the illustrations show
Basis: 1 illustration sheet viewed (1 image, in light appearance), code checked; no videos.
- The opening sketch is tinted in a tone between purple and magenta and sits on the same line grid and the same guide circle as the other HIG opening pages (img 0806).
- The central shape is a large circle with a thick outline with a smaller solid dot inside, read as a person or sensor seen from above (img 0806).
- To the right of the circle there are two concentric curves shaped like waves, folded over a vertical axis, and they appear only on that side (img 0806).
- Direction is communicated through asymmetry: the waves do not wrap around the circle, they arrive from a single side, which reinforces the idea of a source coming from a specific direction, in line with the official description (img 0806).
<!-- /visual:nearby-interactions -->

## Pointing devices (slug: pointing-devices)

### What it governs
Governs the use of pointing devices (trackpad, mouse) to navigate the interface and initiate actions, including the iPadOS pointer system (shapes, content effects, magnetism, accessories) and the standard macOS pointers and gestures.

### Why
On the Mac, the pointing device is typically combined with the keyboard; on iPad and Vision Pro, it is an additional way to interact, without replacing touch, eyes or gestures. Systemic consistency is central: people expect the same gestures to work the same way in every app or game, and to be able to move fluidly between input modes without learning different interactions for each one.

### Do and avoid
- Be consistent in responding to mouse and trackpad gestures, since people expect most gestures to work the same way throughout the system.
- Avoid redefining system-level trackpad gestures, even in a game with custom app-specific gestures; remember that people can customize these gestures.
- Offer a consistent experience in the app, whether the person is using gestures, eyes, a pointing device or keyboard.
- Let the person use the pointer to reveal and hide controls that minimize or disappear automatically (example: revealing Safari's minimized toolbar by holding the pointer over it on iPadOS).
- Offer a consistent experience when holding a modifier key while interacting with objects, ensuring the same result when dragging with touch or with the pointer.
- On iPadOS, allow multiple selection in custom views when necessary; on iPadOS 15+, clicking and dragging the pointer over multiple items selects them, expanding into a visible rectangle; standard non-list collection views support this by default.
- On iPadOS, distinguish between pointer input and finger input only if it adds value (example: a scrubber that allows clicking an exact search point with the pointer).
- On iPadOS, support the system's content effects when possible: highlight (rounded translucent rectangle with slight parallax, applied by default to bar buttons, tab bars, segmented controls and edit menus), lift (subtle parallax with a raised appearance, applied by default to app icons and Control Center buttons) and hover (generic effect with customizable scale, tint or shadow, without transforming the pointer's default shape).
- Use highlight for a small element with a transparent background; use lift for a small element with an opaque background; use hover for large elements.
- Prefer the pointer appearances provided by the system for standard buttons and text entry areas.
- Add padding around interactive elements to create comfortable touch regions; in general about 12 points of padding around elements with a bezel works well, and about 24 points around elements without a bezel.
- Create contiguous touch regions for custom bar buttons, avoiding having the pointer briefly return to its default shape between adjacent buttons.
- Specify the corner radius of a nonstandard element that receives the lift effect, if its shape is not a standard rounded rectangle (for example, a circle).
- Prefer pointer effects provided by the system for custom elements that behave like standard elements.
- Use pointer effects consistently throughout the app.
- Avoid creating gratuitous, purely decorative pointer and content effects.
- Keep custom pointer shapes simple, so their meaning is instantly understandable.
- Consider custom annotations with useful information when holding the pointer over an element (example: X and Y values in a chart area; width and height of a resizable image in Keynote).
- Avoid displaying instructional text next to the pointer, which can make the app seem complicated.
- Consider the interaction between shadow, scale and spacing when defining custom hover effects; reserve scale for elements that can grow without squeezing neighboring elements (it does not work well, for example, for a table row); for elements with little surrounding space, consider a hover effect with tint, but without scale or shadow; do not use shadow without scale, because an element without scale does not appear to move closer to the viewer even with shadow implying elevation.

### Exact specifications
- Recommended padding around interactive elements with a bezel: about 12 points.
- Recommended padding around interactive elements without a bezel (including symbols): about 24 points.

### Platform differences
- No additional considerations for iOS; not supported on tvOS or watchOS.
- iPadOS: full pointer system with shapes, content effects (highlight, lift, hover), pointer accessories and magnetism (applied by default to elements with lift and highlight, but not to hover; also applied to text entry areas).
- macOS: wide range of customizable mouse and trackpad gestures (primary click, secondary click, scrolling, smart zoom, swipe between pages, swipe between full-screen apps, Mission Control, Lookup, tap to click, force click, pinch zoom, rotation, Notification Center, App Exposé, Launchpad, Show Desktop); standard set of pointer styles (arrow, closed hand, contextual menu, crosshair, disappearing item, drag copy, drag link, horizontal I beam, open hand, operation not allowed, pointing hand, resize down/left/left-right/right/up/up-down, vertical I beam).
- visionOS: it is possible to connect an external pointing device or keyboard and use them together with eyes and hands; looking at an element and moving the pointer automatically brings focus to the element under the pointer; the area the person is looking at determines the pointer's context; with a device that supports gestures (trackpad, mouse), the pointer hides during the gesture, reappearing where the person is looking when moved.

### Links to other articles
Entering data, Keyboards.

<!-- visual:pointing-devices -->
### What the illustrations show
Basis: 6 illustration sheets (23 images, in light appearance) and 9 video sheets from 6 videos (035 to 039 with one sheet each, 040 with four) viewed, codes checked.
- The opening is a mouse-style pointer arrow in dark purple over a pink and purple gradient, with a dashed grid and concentric circle overlaid (img 0860).
- The hit target is always drawn the same way: the element centered inside a larger translucent pink rectangle, with red dimension marks on all four sides; a solid blue button with a bezel and white text gets 12 on each side (img 0861).
- A small information symbol in a blue circle and a button without a bezel, with only blue text, get 24 on all four sides, which shows that a small or frameless element gets double the touch margin (img 0862, img 0863, compared to img 0861).
- The custom annotation appears next to a selected gray rectangle, with white square handles at the corners and midpoints and a central handle with arrows; next to it, a dark label shows width and height in points (img 0864).
- The pointer gallery uses isolated black icons on white, with no grid or dimension marks; the meaning comes from the shape of the stroke and small badges under the arrow, such as a green circle with a plus, a gray circle with an X and a translucent gray circle with a prohibited sign (img 0865 to 0882; badges in img 0869, img 0870, img 0874).
- The shapes include hands with a black outline, the closed fist with a white fill and the open hand with the index finger extended in a glove style, a vertical text cursor made of two opposing strokes connected by a thin line and its horizontal version of opposing brackets joined at the center, and a thin cross-shaped crosshair; the resize pointers form a straight-bar system with one or two arrows coming out of the center, covering the four directions and the two axes (img 0866, img 0873, img 0875, img 0872, img 0882, img 0868, img 0876 to 0881).
- In a Calendar event form, the pointer turns into a vertical text bar next to the URL and Notes fields and goes back to being a gray circle in the space between them; the cycle repeats twice across the seven frames (video 035, sheet 0001, q001 to q007).
- The active tab's highlight is a background behind the icon and title: a light rounded pill with a blue icon and text in Photos, with the inactive tab dimmed and without a background; a dark rectangular box behind "World Clock" in orange in Clock, with "Alarm" in gray (video 036 and video 039, sheet 0001, q001 to q007).
- In the iPadOS Dock, the only sign of the pointer under an icon is a dark, translucent oval smudge next to the Messages icon in the first frame; in the rest, all icons are the same size, with no visible shadow or elevation (video 037, sheet 0001, q001 to q007).
- In an alert with the red "Discard Changes" button, the pointer's circle darkens and grows as it approaches the button and lightens and shrinks as it moves away, in a repeated cycle, while the button's fill does not change color (video 038, sheet 0001, q001 to q007).
- In visionOS, the Safari window floats with a dark translucent frame, rounded corners and a centered address bar; the top controls (close, app icon) appear only when it gains focus and disappear when it loses it, and a thumbnail of the hand on the trackpad stays anchored in the bottom left corner throughout the recording (video 040, sheet 0001 q006, sheet 0004 q033).
- Scrolling is continuous and granular, revealing new blocks from top to bottom in each frame, while the angle and position of the window in space vary slightly even when the content is stationary; scrolling keeps working with or without focus on the frame (video 040, sheet 0002 q015 to q018, sheet 0003 q019 to q027, sheet 0004 q034 to q036).
Recorded divergences: in videos 036 and 039 the highlight stays fixed on the active tab in every frame, without the slide between tabs that the official description narrates; in video 037 only the Messages icon shows any sign of the effect, without Safari and Music rising as the description says; in video 038 what changes is the pointer's circle, while the description says the button's background darkens; in video 035 the cycle appears twice, and the description talks about only one transition. The notes attribute part of this to the sampling of few frames, which may not capture fast transitions.
<!-- /visual:pointing-devices -->

## Remotes (slug: remotes)

### What it governs
Governs the use of the Siri Remote as the main input method for Apple TV: a combination of clickpad and touch surface for gestures such as swipe and press, focus-based navigation, and specific buttons (Back, Play/Pause).

### Why
The remote exists so that people feel connected to the content on the screen even at a distance, from across the room. Consistency with the tvOS focus system is central: moving focus always in the same direction as the gesture reinforces the connection between the person and the content they are watching.

### Do and avoid
- Prefer using standard gestures for standard actions; redefining or repurposing the remote's standard behaviors causes confusion and complexity, unless the person is actively playing a game.
- Be consistent with the tvOS focus experience, combining gestures with the focus system in familiar ways, such as always moving focus in the same direction as the gesture.
- Provide clear feedback about what happens when the person makes gestures in the app (example: lightly resting the thumb on the remote shows where to swipe down to reveal an information area).
- Define new gestures only when it makes sense in the app; within gameplay, custom gestures can be fun, but outside it people expect standard gestures.
- Differentiate between press and tap, and avoid responding to an inadvertent tap; press is intentional and works well for choosing a button, confirming a selection or starting an action during gameplay; tap is for navigation or showing additional information, but an inadvertent tap can occur when resting the thumb, picking up, moving or handing the remote to another person, so avoid responding to taps during live video playback.
- Consider using the position of a tap (up, down, left, right on the touch surface) to help with navigation or gameplay, only when it makes sense and is intuitive and discoverable.
- In almost all cases, pressing the Back button should open the parent of the current screen (at the app's top level, the Apple TV Home Screen; inside the app, defined by the app's hierarchy, not necessarily the previous screen). The exception is during active gameplay: respond to Back by opening an in-game pause menu, to avoid repeated accidental presses that interrupt the game; with the pause menu open, another Back closes the menu and resumes the game. Holding Back always goes to the Home Screen from anywhere.
- Respond correctly to the Play/Pause button during media playback: it should play, pause or resume.
- In apps with EPG (electronic program guide), respond to the remote's EPG navigation buttons as expected: a "guide" or "browse" button opens the EPG; "page up"/"page down" navigate within the guide; avoid responding to these buttons in any other way while the person is navigating the EPG. During content playback (outside the EPG), "page up"/"page down" change the channel. Without EPG support in the app, the system routes these presses to the device's default guide app.

### Exact specifications
No number, measurement or duration is given in the text.

### Platform differences
Exclusive to tvOS (Apple TV); not supported on iOS, iPadOS, macOS, visionOS or watchOS.

### Links to other articles
Gestures, Focus and selection, Buttons, EPG experience, Providing Channel Navigation.

<!-- visual:remotes -->
### What the illustrations show
Basis: 1 illustration sheet viewed (1 image, in light appearance), code checked; no videos.
- The opening sketch is a Siri Remote in dark purple over a pink-to-purple gradient, with a vertical rectangular body with rounded corners (img 0921).
- The drawing follows the physical layout of the real remote: a large circle at the top as the touch surface, two small circles side by side just below it and, to the right of that pair, a vertical elongated shape for the media and volume buttons (img 0921).
- A grid of rectangular guides covers the entire composition, and the concentric guide circle is centered at the top of the remote, coinciding with the circular touch surface, so that the circular element of the real object serves as an anchor for the icon's geometry (img 0921).
- The piece repeats the grid discipline of other opening illustrations in the same family, such as the printer and the privacy hand, and the purple color corresponds to one of the six colors of the original logo, according to the official description (img 0921).
<!-- /visual:remotes -->

## What this group reveals about the Apple way

- Privacy is a structural limit, not just a stated policy: visionOS deliberately does not tell the app where the person is looking until the actual touch (eyes), and Nearby Interaction uses random identifiers limited to the session's duration (nearby-interactions).
- Every new input is anchored in a preexisting physical or systemic expectation before it earns a custom behavior: Apple Pencil behaves like a real marking instrument (apple-pencil-and-scribble), nearby interactions are inspired by how the task would work in the physical world (nearby-interactions), and custom gestures are only justified when "not covered by existing gestures" (gestures, game-controls).
- Potentially destructive or irreversible actions get an extra design barrier against accidents: double tap and squeeze on Apple Pencil avoid destructive actions (apple-pencil-and-scribble), hover should never start an action (apple-pencil-and-scribble), and the Apple TV remote avoids responding to inadvertent taps, especially during live video (remotes).
- The system is always the source of truth for standard behavior, and the app should avoid competing with the guidance the system itself already provides: the Action button (action-button), standard keyboard shortcuts (keyboards), Full Keyboard Access (keyboards) and standard trackpad gestures on macOS (pointing-devices) all follow this same rule.
- Continuous, immediate feedback is treated as a requirement, not a luxury, in any input that depends on proximity, pressure or movement: Digital Crown (digital-crown), Camera Control (camera-control), nearby interactions (nearby-interactions) and gestures in general (gestures) require a visible response to what the person is doing.
- Each platform has its own focus/targeting system coherent with its primary input hardware, and Apple avoids mixing paradigms: directional focus on tvOS, focus groups on iPadOS, eye hover on visionOS (focus-and-selection, eyes), each one mapped to the dominant physical device of that platform.
- There is a clear hierarchy of input priority by device: on the Mac, keyboard and pointer are the standard pair; on iPad and Vision Pro, the pointing device is "additional", never replacing touch, eyes or gestures (pointing-devices); on Apple Watch, the Digital Crown has been the primary navigation since watchOS 10, but is always reinforced with touch on the screen (digital-crown).
- Touch targets and interaction regions have consistent minimum values built around "finger and comfort", not pixel precision: 44x44 pt for frequent virtual game controls and 28x28 pt for less important ones (game-controls), 16 pt of margin or 60 pt between centers for items in visionOS (eyes), 12 pt and 24 pt of padding around elements with and without a bezel on iPadOS (pointing-devices).
- Customization is always bounded by restraint: custom keyboard shortcuts only for the most used commands (keyboards), custom hover effects only for "special moments" (eyes), game key bindings with a good combination of nearby keys, but always remappable by the player (game-controls).
- Text and physical writing (Scribble) receive treatment separate from keyboard input, prioritizing naturalness over features like autocomplete, which come to be treated as distractions during handwriting (apple-pencil-and-scribble).
- Symbols instead of text or abstract labels is a recurring pattern for communicating control function universally: SF Symbols in Camera Control (camera-control) and in game controls (game-controls), modifier key symbols on the keyboard (keyboards).

## Reading evidence

| File | Lines read | Read to the end |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/action-button.md | 39 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/apple-pencil-and-scribble.md | 87 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/camera-control.md | 60 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/digital-crown.md | 48 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/eyes.md | 65 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/focus-and-selection.md | 69 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/game-controls.md | 86 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/gestures.md | 121 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/gyro-and-accelerometer.md | 26 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/keyboards.md | 184 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/nearby-interactions.md | 45 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pointing-devices.md | 131 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/remotes.md | 42 | yes |

All 13 articles in the "Inputs" group (index 13 of the hig list) were read in full with the Read tool, in a single call per file, with no truncation reported by the tool. No article is just a collection index page; all have complete text of their own.
