# ess-01, recurring visual patterns

Basis: 53 visual syntheses of the HIG, from `accessibility` to `game-center`.

## Every page opens with a single icon drawn over a dashed construction grid, with a centered guide circle and diagonals
- Evidence: accessibility (img 0000, silhouette symbol with a dotted rectangular and circular grid and diagonals marking center and proportions)
- Evidence: carplay (img 0230, "C" with a play triangle over a dashed grid and guide circle)
- Evidence: designing-for-games (img 0433, controller with a dotted grid, centered circle and diagonal X, handles following the diagonals)
- Evidence: entering-data (img 0472, field inscribed in the circle and only the pencil crossing the boundary at the top right)
- Evidence: file-management (img 0479, document centered on the crossing of the guides and inscribed in the dashed circle)
- What this teaches about building interfaces: Apple shows the scaffolding together with the shape, and each silhouette is born anchored to a circle and a pair of axes instead of free drawing. To build an icon system, defining the grid and the inscribed circle first and deriving every shape from them gives coherence between pieces made at different times.

## The color of the opening gradient classifies the subject by family, and the internal shape is the only variable
- Evidence: designing-for-ios, ipados, macos, tvos, visionos, watchos, iphone-duo and designing-for-games, all in a green gradient with the same composition (img 0433 to 0436, 0456 to 0459)
- Evidence: airplay, carekit, carplay, augmented-reality and game-center in a blue gradient (img 0039, 0216, 0230, 0160, 0490)
- Evidence: boxes, collections, column-views, charts, collaboration-and-sharing, drag-and-drop, entering-data, feedback and file-management in an orange-to-red gradient (img 0183, 0252, 0342, 0234, 0246, 0470, 0472, 0478, 0479)
- Evidence: action-button, always-on, apple-pencil-and-scribble, camera-control, digital-crown, eyes and focus-and-selection in a pink-to-purple gradient (img 0024, 0052, 0147, 0200, 0461, 0473, 0481)
- What this teaches about building interfaces: color does the taxonomy work before any text, and the reader knows which chapter they are in just from the palette. In a product, reserving hue to indicate the content family and letting shape indicate the specific item avoids depending on a label.

## Devices and objects are reduced to three or four recognizable strokes, with no texture or superfluous detail
- Evidence: designing-for-ios (img 0434, iPhone reduced to frame, top notch and home bar)
- Evidence: designing-for-games (img 0433, controller reduced to body, directional cross and two buttons, with no triggers or grip)
- Evidence: designing-for-watchos (img 0459, case with two side protrusions and two lugs)
- Evidence: app-icons (img 0083 and 0084, Podcasts in concentric circles and Home in nested layers down to the door)
- What this teaches about building interfaces: recognition comes from the silhouette and two or three markers, not from fidelity. When drawing icons, cutting everything that does not distinguish the object from its neighbors is what keeps legibility at small size.

## Component measurement is dimensioned with a bidirectional double arrow and no number, while an exportable asset and a third-party mark receive a numeric dimension
- Evidence: boxes (img 0183, four red double arrows dimensioning padding and margin, no number printed)
- Evidence: collections (img 0252, outer margin arrows plus two smaller marks for the spacing between cells, with no values)
- Evidence: buttons (img 0189, red arrows for the width of the capsule and the spacing between two buttons, with no numbers)
- Evidence: apple-pay (img 0144 and 0145, pink outline with minimum height of 30, minimum width of 100 and of 140, margin of 1/10 of the height)
- Evidence: game-center (img 0496, 0497, 0500, 0501, 0505, 0511, squares and rectangles with values in pt for mask, crop and focus sizes)
- What this teaches about building interfaces: proportion and breathing room are taught as a relationship, and the number only appears when someone needs to export a file or protect a mark. Specifying a design system by the relationship between measurements, and fixing numbers only at the contract points, lets the layout scale across screen sizes.

## Right and wrong are judged by a fixed pair of badges, gray X in a gray circle and green check in a green circle, almost always in their own isolated image
- Evidence: branding (img 0186 and 0188, badges isolated and centered on a white background, with no interface element alongside)
- Evidence: airplay (img 0044 and 0045, badges in their own cells, not paired in the same image)
- Evidence: accessibility (img 0004 to 0007, low-contrast button with X and royal blue button with check)
- Evidence: eyes (img 0475 and 0477, X for the square inner area and check for the circular one)
- Evidence: camera-control (img 0209 to 0212, ruler with "1 EV" receives a check and the same ruler with "1" receives an X)
- What this teaches about building interfaces: the verdict is a standardized signal separate from the example, so the example never becomes a deformed illustration made to look wrong. In internal documentation, keeping both cases visually identical and placing the judgment outside them forces the real difference to become evident.

## One example at a time changes a single variable, reusing the same composition, the same content and the same framing
- Evidence: branding (img 0185 and 0187, the same airport map, changing only whether the brand color is on the controls or on the content)
- Evidence: focus-and-selection (img 0485 to 0489, the same pill button at the same point of the same beach photo, varying only the state)
- Evidence: apple-pay (img 0135 to 0143, the same two buttons swapping one variable at a time: size, order, alignment, corner radius)
- Evidence: activity-rings (img 0034 and 0035, Summary screens with the same header, the same date and the same avatar, changing only the card)
- Evidence: app-clips (img 0072 to 0075, the errors come one at a time: oval proportion, then gradient, then shadow)
- What this teaches about building interfaces: the fictional content is kept constant on purpose so the eye can only notice the variable under study. When presenting design options, literally reusing the same screen and swapping one attribute prevents the decision from being contaminated by accidental differences.

## The before and after use the same background to teach that it is a two-step flow, not two independent screens
- Evidence: action-sheets (img 0026 and 0027, the same Mail composition screen, changing only the presence of the overlaid sheet)
- Evidence: activity-views (img 0037 and 0038, the same note in the background before and after tapping Share)
- Evidence: disclosure-controls (img 0467 and 0468, the same save dialog collapsed and expanded, with the name field intact at the top)
- Evidence: controls (img 0409 and 0410, the same pill control open and locked)
- What this teaches about building interfaces: the continuity of the background is what communicates cause and effect. A transition that swaps the entire screen loses the link between the action and the result, and the pair of states over the same base is the cheap way to preserve it.

## Anatomy is taught with callout lines that name each part inside the image itself
- Evidence: charts (img 0235, callouts for grid line, plot area, mark, axis, tick and axis value label over the same histogram from the cover)
- Evidence: controls (img 0400, "Symbol image" on the left and "Value" on the second line of the text block)
- Evidence: carekit (img 0219, header with disclosure indicator, horizontal separator and content subview)
- Evidence: app-shortcuts (img 0092, callout line naming "Parameter" the blue, underlined variable portion of the sentence)
- Evidence: complications (img 0344, watch face with thin lines connecting labels to the Top Left, Date, Middle, Bottom Left, Bottom Middle and Bottom Right zones)
- What this teaches about building interfaces: naming the zones of a component in the artwork itself creates shared vocabulary between whoever draws and whoever implements. An annotated diagram is worth more than a text list of slots, because it ties the name to the position.

## The same component crosses platforms with identical structure, changing only the arrangement of elements and the background material
- Evidence: alerts (img 0047 to 0051, identical title and description on iPhone, Mac, tvOS, Vision Pro and Watch, with buttons side by side or stacked and an opaque, semitransparent, glass or gradient background)
- Evidence: app-icons (img 0078, the same Photos flower swapping only the frame: rounded square, elongated rectangle and circle)
- Evidence: game-center (img 0492, the same Game Overlay covers the entire screen on iPhone and becomes a vertical strip on the trailing edge on iPad)
- Evidence: complications (img 0367, 0380, 0387 and 0397, the same "LON 6:09" data recomposed on a single line, stacked over a circle and stacked in two colors according to the family)
- What this teaches about building interfaces: what travels between platforms is the information hierarchy, not the layout. Modeling the component by content and leaving arrangement and material as platform parameters is what lets a single definition serve very different screens.

## The hierarchy between actions comes from fill and weight, with the destructive one marked in red in the text and not in the background
- Evidence: buttons (img 0190, primary with solid blue background and white text, destructive with light gray background and red text, secondary with light gray background and black text)
- Evidence: alerts (img 0046, secondary in light pink and primary in strong red with larger bold text)
- Evidence: action-sheets (img 0027, "Delete Draft" in red and "Save Draft" in black, both in the same pill shape)
- Evidence: file-management (img 0480, primary action as the single solid blue button right below the app name)
- What this teaches about building interfaces: a single action per screen gets solid fill, and danger is signaled by text color so it does not compete in weight with the main action. Painting the entire destructive button red would turn it into the heaviest element on the screen, which is the opposite of what is wanted.

## A single accent color runs through the entire screen, and the unselected item never receives it
- Evidence: carekit (img 0217 to 0229, red appears in checks, the day selector, chart bars, the log button and contact actions, with secondary backgrounds and buttons in white and gray)
- Evidence: camera-control (img 0202 to 0208, orange marks the active icon, the central line of the ruler, the chosen point and all the value labels)
- Evidence: color (img 0262, the selected tab bar item carries blue on the icon and the label, and the unselected one stays black in light mode and white in dark mode, with a gray label)
- Evidence: focus-and-selection (img 0484, the highlighted item gets a filled star, red icon and text, and the rest remain black on white)
- What this teaches about building interfaces: the accent color is a scarce resource and only marks state or action, never decoration. Applying it to the inactive item destroys the reading of state, which is the only thing it should communicate.

## Color never carries the information alone, always doubled by shape, symbol, fill or size
- Evidence: accessibility (img 0010 and 0011, two circles that only differed in hue gain a white check on green and an octagon with a white X on red)
- Evidence: charts (img 0243, systolic in small red dots and diastolic in black and white diamonds, with the shape marker repeated in the header)
- Evidence: carekit (img 0219, 0223 and 0224, filled red circle with a check for done and an outline-only circle for pending)
- Evidence: camera-control (img 0204, 0207 and 0208, the active option turns orange and also becomes larger than its neighbors, with the name spelled out below)
- What this teaches about building interfaces: any state that only exists in hue disappears for part of the users and in low-contrast photos. The practical rule is to guarantee a second channel, shape or fill or size or text, before choosing the color.

## A color swatch is documented as a minimal card with the RGB value alongside, with no name and no context of use
- Evidence: color (img 0270 to 0341, square with rounded corners with three RGB values, each card repeated over a white background and over a black background with an identical value)
- Evidence: activity-rings (img 0031 to 0033, reddish pink 250, 17, 79, lime green 166, 255, 0 and cyan 0, 255, 246)
- Evidence: color-wells (img 0253, text label with the RGB value connected by a line to the center of the button, treating the current color as specification data)
- What this teaches about building interfaces: color is delivered as a verifiable value and not as an impression. In your own system, publishing the token with the numeric value visible over both backgrounds keeps anyone from resampling the color from a screenshot.

## In dark mode the geometry does not move: position, rulers and structure stay identical, and only the background and internal values change
- Evidence: color-wells (img 0253, structure, rulers and text position identical, with the popover turning wine brown and the white box becoming a light, semitransparent outline)
- Evidence: app-icons (img 0080 to 0082, the gear and the position of each guide do not change, background and lines switch to black and white)
- Evidence: dark-mode (img 0413 and 0414, the four swatches change only slightly in saturation while the square goes from light gray to nearly black)
- Evidence: color (img 0255 to 0258, the same Notes screen in standard light, increased contrast light, standard dark and increased contrast dark, with the button keeping the yellow background and changing only the symbol)
- What this teaches about building interfaces: theme is a swap of values inside a fixed structure, not a second layout. When the position changes between light and dark, it is a sign that color was used to solve a composition problem that should have been solved in the geometry.

## The glass material absorbs the color of what is behind it, and the control keeps its own tone over any background
- Evidence: color (img 0263, share button over a photo of flowers and a mountain appears visibly tinted pink and blue)
- Evidence: color (img 0261, the circular blue button with a white check does not change tone over a white background or over a black background, only the surrounding background inverts)
- Evidence: controls (img 0399, 0401 and 0402, translucent circular buttons in Control Center and at the bottom of the Lock Screen over a blurred dark background)
- Evidence: buttons (video 006, sheet 0001, q007 and q008, menu with a bluish translucent background that appears to come from the content behind it)
- What this teaches about building interfaces: translucency creates belonging to the context without requiring the component to change definition. The price is that legibility has to be guaranteed by the element itself, not by the background that changes with every screen.

## In visionOS the hierarchy comes from sharpness, transparency and depth, not from scale, and the panels float in front of the scene
- Evidence: app-icons (video 004, sheet 0001, front row sharp and the back row blurred and cropped at the top)
- Evidence: alerts (video 003, sheets 0001 to 0003, the alert forms in front of the window and the whole set becomes progressively more transparent as it moves through the room)
- Evidence: alerts (video 002, sheet 0001, the alert never coincides with the outline of the window behind it, appearing offset in q003 and closer to the center in q004)
- Evidence: eyes (video 009, sheets 0001 to 0003, translucent panels with rounded corners floating over the real room)
- What this teaches about building interfaces: in three-dimensional space, what used to be resolved by size and shadow is now resolved by focus and distance. Whoever designs for these screens needs to treat depth as a dimension of hierarchy with the same seriousness given to contrast.

## State change preserves the box: nothing shifts, grows or recomposes around it
- Evidence: buttons (img 0191 and 0192, "Checkout" becomes "Checking out" with a spinner at the leading edge, keeping shape and background color with no perceptible change in size)
- Evidence: eyes (video 009, sheet 0002, q010 to q018, the hover only changes the background highlight of the targeted row, without shifting or resizing anything)
- Evidence: controls (img 0409 and 0410, the sensitive data becomes two gray bars without changing the shape or size of the control)
- Evidence: buttons (video 006, sheet 0001, q006 to q008, the more-options button lightens and then becomes solid white while its neighbors stay gray)
- What this teaches about building interfaces: reserving the space of the final state from the initial state eliminates the layout jump, which is the main source of tap error. Swapping color, fill and content inside a fixed box resolves almost all visual feedback.

## Menus and panels are born anchored to their origin, connected by a point, a line or a continuous shape
- Evidence: dock-menus (img 0469, balloon with a triangular point pointing back at the origin icon)
- Evidence: edit-menus (img 0471, thin line connecting the left tip of the bar to the upper-left handle of the selection)
- Evidence: color-wells (img 0253, continuous teardrop shape connecting the closed button to the open popover)
- Evidence: context-menus (img 0398, menu anchored just below and to the right of the cursor, not centered on the screen)
- Evidence: buttons (video 006, sheet 0001, q007 and q008, the menu is born anchored just below the button, partially cropped and then whole)
- What this teaches about building interfaces: the visual connection answers the question "where did this come from" at no cost in attention. A panel that appears centered forces the user to reconstruct the cause, and the gain from positioning it at the origin is greater than that of a perfect alignment.

## The videos reveal the intermediate step that the written description omits
- Evidence: alerts (video 002, sheet 0001, the alert does not appear directly, first there is a context menu with "Recover" and "Delete", and the Delete option stays highlighted for about half a second)
- Evidence: drag-and-drop (video 008, sheets 0001 and 0002, the file first lands as a flat labeled card on the table and only then does the 3D object appear small and grow, gaining craters and texture)
- Evidence: buttons (video 007, sheet 0001, the tooltip appears with a delay, smaller in q003, and only in q004 does it reach its final size and opacity)
- What this teaches about building interfaces: the transition is the product, not decoration between two states. When you only read the final specification, the steps that explain the change are left out and the implementation comes out abrupt.

## The density of the grid changes with the available width and the same elements redistribute, without disappearing
- Evidence: designing-for-iphone-duo (img 0437 and 0438, the Home Screen goes from four columns by four rows on the outer screen to six by four on the inner one, with the shortcuts column fixed at the right edge on both)
- Evidence: designing-for-iphone-duo (img 0452, the Calculator goes from four columns by five rows to five columns by four rows on the wider, shorter screen)
- Evidence: camera-control (img 0213, the row of icons and the label form a horizontal strip at the top in portrait and migrate to the right side in landscape)
- Evidence: apple-pencil-and-scribble (img 0159, the full iPad bar in landscape becomes a top bar plus a reduced palette on iPhone in portrait)
- What this teaches about building interfaces: adapting means reorganizing the same material, not cutting functionality. Defining the set of elements first and then the arrangement rules by width avoids the mutilated versions that appear when each size is designed from scratch.

## The controls stay attached to the edge of the content or the hardware they serve
- Evidence: camera-control (img 0201 and 0213, the overlay appears in the region just below the physical button and follows its edge when the device rotates)
- Evidence: designing-for-iphone-duo (img 0451 and 0453, in Split View each app uses a strip of controls on its own outer edge, and in Mail the leading pane carries its controls at the top and the trailing pane on the right vertical edge)
- Evidence: apple-pencil-and-scribble (img 0151 and 0152, the controls stay on both side edges of the iPad precisely because the hand holding the Pencil covers one of the sides)
- What this teaches about building interfaces: the position of the control is decided by the ergonomics of the gesture and the physical origin of the action, not by the symmetry of the screen. Duplicating the control on both edges is preferable to choosing one side when the hand can come from either one.

## Pink and red are the color of annotation: measurement, reserved clear space and protected area
- Evidence: app-clips (img 0069 and 0070, the clear space is a pink band with the same x measurement repeated on every side of each code)
- Evidence: augmented-reality (img 0177 and 0179 to 0182, the minimum clear space of the glyph and of each badge is marked by a translucent pink frame)
- Evidence: apple-pay (img 0144 and 0145, measurement diagrams with a pink outline and dimensions in points)
- Evidence: accessibility (img 0016, dashed red outlines over the tap areas that touch each other with no space between them)
- What this teaches about building interfaces: the annotation layer has its own color and is never confused with the real interface. Reserving an exclusive color for specification overlays is what makes it possible to mark invisible spaces, such as tap area and protective margin, without cluttering the example.

## In tvOS focus enlarges the element, and the asset needs to be born in distinct sizes for that
- Evidence: focus-and-selection (img 0485 and 0486, the pill without focus is translucent gray and the smallest of the series, and with focus becomes opaque white and larger)
- Evidence: game-center (img 0501, three concentric rectangles with the image at 659x371 pt, the in-focus size at 618x348 pt and the out-of-focus size at 548x309 pt)
- What this teaches about building interfaces: in an interface controlled from a distance, focus needs a change in area and opacity, not just in edge. This requires planning the art with scale margin from the export stage on.

## The stylized illustration simplifies and sometimes loses a layer that the real capture has
- Evidence: activity-views (img 0036 compared to img 0038, the stylization has two rows and the real capture adds a row of its own for contacts, separating contacts, apps and actions into three bands)
- Evidence: action-sheets (img 0025 compared to img 0027, the diagram isolates the card with width and height dimensions, without an iPhone and without a position on the screen)
- Evidence: activity-rings (img 0029 compared to img 0030 and 0034, the percentage written next to each ring only exists in the conceptual diagram, and on the real screens the values come as a pair of current value and goal)
- What this teaches about building interfaces: the diagram serves to teach proportion and names, and the capture serves to check real density. Implementing from the diagram alone tends to produce a screen with less information than the component actually carries.

## Related items are grouped in rounded blocks with a thin separator, and the division carries meaning
- Evidence: eyes (video 009, sheets 0001 to 0003, the items in the detail panel are grouped into smaller rounded blocks that join related pairs, like About with Software Update and AirDrop with Handoff)
- Evidence: dock-menus (img 0469, four items divided into two groups by a dividing line, with "Show Recents" and "Open" forming the second)
- Evidence: carekit (img 0219 and 0229, header with title and disclosure indicator, horizontal separator and content subview below)
- Evidence: collaboration-and-sharing (img 0251, popover in three vertical blocks: channel tabs at the top, state in the middle, toggle and list items at the bottom)
- What this teaches about building interfaces: grouping is the first layer of hierarchy, before typography and color. A long list without blocks forces you to read everything, while three blocks let you jump straight to the right region.

## Text comes before the data and before the action: title, then short description, then the chart or the buttons
- Evidence: charts (img 0242, the card brings first the heavy rain alert title and a subtitle in plain language, and only then the bar chart)
- Evidence: action-sheets (img 0025, internal hierarchy of title, description and stack of three actions in the same pill shape)
- Evidence: app-clips (img 0054, bold title, two-line description, button on the right and discreet attribution below)
- Evidence: column-views (img 0342, detail panel stacked by importance: large thumbnail, larger bold name, short line of format and size, and only then the label and value pairs)
- What this teaches about building interfaces: the reading starts with the conclusion in plain language and goes down to the evidence. A chart or a list of actions placed before the sentence that explains what is happening transfers the work of interpreting to the user.

## The active state is distinguished by fill and by size at the same time, and selection can have two levels
- Evidence: column-views (img 0342, weak highlight on the column whose selection has already advanced and solid red background on the item with active focus, making the cascade visible)
- Evidence: buttons (img 0193 to 0196, the selected visionOS button inverts the contrast, with a solid white inner circle and black outline icon, and the unavailable one appears dimmed)
- Evidence: camera-control (img 0204, the chosen option is filled in orange and larger than the gray ones)
- Evidence: carekit (img 0217, complete days with a filled red check and the selected day with a thicker outline)
- What this teaches about building interfaces: when focus, selection and completion exist at the same time, a single visual device is not enough. Separating fill for "completed" and outline or size for "where I am" keeps both legible in the same row.

## In watchOS the alert and the action sheet share the same construction, with buttons colored by function instead of neutral
- Evidence: alerts (img 0051, title and description centered in white over a dark blue to purple gradient, with the primary in green and the secondary in a purple and magenta gradient)
- Evidence: action-sheets (img 0028, close X in the top left corner, title and description centered and two large stacked pill buttons, the action in green and the Cancel in a purple and magenta gradient)
- What this teaches about building interfaces: on a very small screen the button occupies almost the entire width, so the difference between the options needs to come from the color of the button itself, not from position or text weight.

## Single-source findings

- Icon Composer appears as a real tool, with named layers in nested groups on the left, art in the center and properties on the right: opacity 100%, blend mode normal, solid fill, "Liquid Glass Effects" on, image in SVG, x and y position at 0 pt and scale 100% (app-icons, img 0079).
- The icon appearance grid is 3 by 2 with a label under each cell: colored default, light translucent and light tinted on top, dark, dark translucent and dark tinted on the bottom (app-icons, img 0089).
- The safe zone of the tvOS icon is a dashed rectangle inside the art, and the shape fits entirely within it with visible margin to the outer edge (app-icons, img 0090).
- Depth through overlap, over a checkerboard transparency background: the approved outer circle has no outline and uses a semi-transparent fill that lets the checkerboard show through, and the solid one looks like it rests on top of it (app-icons, img 0085 to 0088).
- Complex illustration in dark mode is not resolved with an outline, but by redoing the internal values: clothes and chairs become white or light gray and hair lightens, while a simple single-shape icon only needs a thin outline (dark-mode, img 0415 to 0419).
- The label hierarchy is a four-level scale with decreasing contrast, label, secondaryLabel, tertiaryLabel and quaternaryLabel, repeated in the same order over black, over elevated dark gray and over white (dark-mode, img 0422 to 0424).
- Gamut management is shown in the chromaticity diagram with two triangles, sRGB entirely contained within Display P3 (color, img 0268).
- The same Stocks rally is a green line in English and red in Chinese, with identical values and curve (color, img 0259 and 0260).
- The iOS grayscale goes from 28, 28, 30 to 242, 242, 247, and at the extremes the contrast with the background nearly disappears, the lightest over white and the darkest over black (color, img 0318 to 0341).
- Payment validation error is signaled only by red text in the field and in the label, without an alert icon and without changing the layout, both in the app and on the web (apple-pay, img 0103 to 0105).
- The Apple Pay mark enters a row with other payment brands, all in the same size and shape, treated as a brand and not as a button (apple-pay, img 0146).
- The App Clip Code has a minimum diameter of 3/4 inch, occupies exactly a 60 degree slice when applied to a cylindrical surface, and its clear space is the same x dimension repeated on all four sides (app-clips, img 0061, 0067 to 0070).
- The Action Button hint names the result of holding, not the current state: with the pill on "Ring" the hint says "Hold for Silent", and with the pill on "Silent" it says "Hold for Ring" (controls, img 0407 and 0408).
- A failed numeric value is one that appears without a unit: the ruler with "1 EV" passes and the same ruler with just "1" is marked as an error (camera-control, img 0209 to 0212).
- Duplicating in the viewfinder the values the overlay already shows is the error exemplified, with zoom stacked to the left of the shutter in addition to the top label (camera-control, img 0214 and 0215).
- The alternative to the swipe gesture is a red minus button always visible in edit mode, because with swipe the "Delete" button covers part of the title and subtitle (accessibility, img 0017 and 0018).
- Adaptive color matters because the default systemRed looks practically the same over a light and dark background, while the accessible variant darkens and saturates in light mode and lightens pulling toward pink in dark mode (accessibility, img 0008 and 0009).
- Assistive Access reduces the Camera to three large targets on a black background, and the next screen swaps the two options for a large preview, shutter button and back (accessibility, img 0021 and 0022).
- visionOS Zoom is a circular lens that magnifies only the region under it, over a floating window in a real environment (accessibility, img 0023).
- In head Pointer Control the content moves under a fixed target, instead of a cursor moving over still content (accessibility, video 001, sheets 0001 and 0002).
- Each physical property of the Apple Pencil gets its own graphic measurement system in the same blue color: a degree arc for altitude, progressive thickness for pressure and a graduated circle for azimuth (apple-pencil-and-scribble, img 0148 to 0150).
- The Pencil hover preview fails when too small and passes at the medium size of the range (apple-pencil-and-scribble, img 0153 to 0157).
- A field that is too narrow cuts off Scribble handwriting, and the wide field that fits the entire name is the approved one (apple-pencil-and-scribble, img 0158).
- The storage bar is a single horizontal bar divided into nine segments of distinct colors, separated by thin white space, with a dot and text legend below (charts, img 0244).
- The axis can be fixed or dynamic depending on the data: battery level keeps the axis from 0% to 100%, and the steps chart changes the top of the axis from 6,000 in the week view to 10,000 in the month view (charts, img 0239 to 0241).
- The screen reader focus indicator appears as an outline rectangle covering only the relevant portion of the chart, not the entire chart (charts, img 0245).
- The collaboration permission phrase is taught by swapping only the one-line summary above the avatars, "Only invited people can edit." and then "Everyone can make changes." (collaboration-and-sharing, img 0248 and 0249).
- The Game Center circular mask is 512 pt touching the four edges of the 512x512 pt square on iOS, iPadOS, macOS and visionOS, but 200 pt centered in a 320x320 pt square on tvOS (game-center, img 0496 and 0497).
- The challenge art is a 1920x1080 pt rectangle with a central crop area of 1465x1080 pt, which preserves the full height and discards narrow margins on the sides (game-center, img 0505 and 0511).
- The system provides a dark gradient at the base of the art to give legibility to the overlaid text, instead of requiring the developer to darken the image (game-center, img 0504 and 0510).
- The locked achievement card is a uniform gray circle with a padlock and no visible title, while the earned one has a colored image, a date arcing around it and legible text (game-center, img 0493).
- The disclosure of the macOS save dialog makes the window itself grow until it becomes a full file browser, with sidebar, columns, search and New Folder, without touching the name field at the top (disclosure-controls, img 0467 and 0468).
- In landscape on the iPhone Duo's external screen, the toolbar and tab bar never appear full at the same time: either the toolbar collapses into an ellipsis button, or the tab bar collapses into a single button (designing-for-iphone-duo, img 0454 and 0455).
- The inner camera region sits inside the fold region, at the center of the open screen (designing-for-iphone-duo, img 0440 and 0445).
- In Notes with the device fully open the list column is much narrower than the content column, and partially folded the two become the same width (designing-for-iphone-duo, img 0446 and 0447).
- The eight design principles are communicated only by isolated pictograms, without text, caption, photography or screen, all in the same green gradient and the same stroke (design-principles, img 0425 to 0432).
- The combo box proves free entry through the detail of the text cursor right after a value that is not among the options in the open list (combo-boxes, img 0343).
- The document launcher separates into layers what is the app's brand, illustrated background, mascot, large title and blue primary button, from what is a standard system control, the neutral file browser at the bottom (file-management, img 0480).
- The iPadOS focus halo appears in two variants in the same photo grid, one flush against the edge with square corners and another set apart with rounded corners, keeping the same color (focus-and-selection, img 0482 and 0483).
- The Digital Crown is isolated in two different ways in real product photos: by a finger resting on it on Vision Pro and by a red outline drawn over the photo on Apple Watch, with the side button right below left unhighlighted (digital-crown, img 0462 and 0463).
- A content shortcut carries behind the symbol a thumbnail of the note itself, with staff lines or the list of names visible, which makes it recognizable by its content and not by its label (app-shortcuts, img 0091).
- The open App Clip is a complete functional screen, with a list of items, prices, quantity controls and an order button with a count, not a preview of the app (app-clips, img 0055).
- In CareKit the four task styles reuse the same white card and swap only the subview, and the header summarizes what remains, like "1 remaining" (carekit, img 0219 to 0223).
- AR coaching and relocalization reuse the same translucent, dotted surface indicator, changing only the text and adding a "Start Over" button in the case of interruption (augmented-reality, img 0162 and 0172).
- Sufficient and insufficient lighting are the same scene at the same angle, just in a light and dark tone, presented without a right or wrong marker (augmented-reality, img 0173 and 0174).
- The 3D rotation hint highlights the face of the cube and circles it with a curved arrow, and the 2D alternative swaps this for a "Rotate" label in a dark capsule below the object (augmented-reality, img 0168 and 0169).
- The passcode diagram dimensions the breathing room around each block, above the title, on the sides of the row of boxes, between the boxes, between boxes and keyboard and between keyboard and bottom edge (digit-entry-views, img 0460).
- Text selection is built with a highlighted background over the word, a vertical cursor on the right and two circular handles at the ends, one above on the left and another below on the right (edit-menus, img 0471).
