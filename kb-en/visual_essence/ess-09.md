# ess-09: recurring visual patterns (18 WWDC 2021 and 2022 videos)

## The session outline becomes a progress bar, and the hierarchy is made only with weight and opacity, with no box, icon or numbering
- Evidence: wwdc2022_10139 (sheet 0006, q0046 to q0048; sheet 0008, q0069 to q0070; sheet 0010, q0086)
- Evidence: wwdc2022_10037 (sheet 0003, q0021 and q0022; sheet 0006, q0053; sheet 0009, q0078; sheet 0013, q0115)
- Evidence: wwdc2022_10169 (sheet 0002, q0016; sheet 0004, q0034; sheet 0009, q0074; sheet 0013, q0110 and q0111)
- Evidence: wwdc2022_10015 (sheets 0005 to 0010, q0054, q0058, q0064, q0078, q0087 to q0089)
- Evidence: wwdc2022_10001 (sheets 0002, 0009, 0013 and 0018, q0010 to q0014, q0077 and q0078, q0113 to q0117, q0154)
- Evidence: wwdc2022_10157 (sheet 0002, q0014 and q0015; sheet 0006, q0048; sheet 0008, q0069 and q0072)
- Evidence: wwdc2022_10131 (sheet 0002, q0010; sheet 0005, q0045; sheet 0006, q0046)
- What this teaches about building interfaces: an indicator of where the person is in the journey does not need its own component, it is enough to keep the whole list visible and change the weight and opacity of the current item. Same text, same position, no new box.

## Nothing appears whole at once: lists, grids and tables grow item by item, and the new item enters by fading in from nearly illegible opacity
- Evidence: wwdc2022_10131 (sheet 0004, q0034 to q0036; sheet 0010, q0083, from one item to seven)
- Evidence: wwdc2021_10304 (sheet 0014, q0123 to q0124; sheet 0015, q0127 to q0131; sheet 0025, q0222 to q0224)
- Evidence: wwdc2022_10139 (sheet 0018, q0159 to q0161; sheet 0019, q0163 to q0165)
- Evidence: wwdc2022_10158 (sheet 0011, q0097 to q0099; sheet 0012, q0100 to q0106)
- Evidence: wwdc2022_10009 (sheet 0012, q0100 to q0103, with the check circles appearing one by one; sheet 0016, q0140 to q0142)
- Evidence: wwdc2022_10037 (sheet 0016, q0137 to q0139, subitems in light gray before turning full white)
- Evidence: wwdc2021_10283 (sheet 0009, q0079 to q0081; sheet 0010, q0082 and q0083)
- What this teaches about building interfaces: progressive disclosure is a focus tool, not an effect. What has already entered stays on screen to give context, and the new item stands out through the transitioning opacity, not through a different color or marker.

## Right and wrong are marked by a graphic badge attached to the screen being judged, a green check against an X or a warning triangle, with no caption explaining the convention
- Evidence: wwdc2021_10283 (sheet 0004, q0033 to q0035; sheet 0007, q0056 to q0060; sheet 0011, q0091 to q0093)
- Evidence: wwdc2022_10037 (sheet 0004, q0034 to q0036; sheet 0011, q0094 to q0099; sheet 0012, q0103 to q0106)
- Evidence: wwdc2022_10001 (sheet 0006, q0049 to q0051, tab bar with a red X against a reorganized version with a green check)
- Evidence: wwdc2022_10157 (sheet 0006, q0046 and q0047, two sliders side by side, one with a yellow warning and the other with a green check)
- Evidence: wwdc2022_10169 (sheet 0010, q0088, two versions of the same snippet with a red X and a green check in the top corner)
- What this teaches about building interfaces: the comparative pair works because both sides share the same template and only the point under discussion changes. The verdict stays in a small badge in the corner, never in an explanatory sentence inside the example.

## The proof is made by the difference between two nearly identical frames: everything freezes and a single element changes
- Evidence: wwdc2022_10157 (sheet 0008, q0066 to q0068, three identical silhouettes with only the third turning from white to gray)
- Evidence: wwdc2022_10131 (sheet 0007, q0056 to q0058, the card stays in exactly the same position on the screen while the 3D background rotates)
- Evidence: wwdc2022_10158 (sheet 0003, q0022 and q0023, the speaker wave goes from one bar to two as the field goes from 0% to 51%)
- Evidence: wwdc2022_10009 (sheet 0014, q0118 to q0124, a toggle goes from gray to blue between two nearly identical frames)
- Evidence: wwdc2022_10139 (sheet 0017, q0148 against q0151, the same parameter in true and false, with the status bar disappearing and coming back)
- Evidence: wwdc2021_10349 (sheet 0004, q0032 to q0033, the variant line enters the code and the list icons go from outline to filled)
- What this teaches about building interfaces: to demonstrate a behavior, hold all other variables constant. The comparison between two nearly identical states proves cause in a way that a text description does not.

## Each piece of the interface gets a text label connected to the element by a thin line, and the vocabulary names the screen piece by piece
- Evidence: wwdc2022_10001 (sheets 0003 to 0017, almost every mockup carries a label connected by a straight line, from navigation bar to inactive action and dismiss)
- Evidence: wwdc2022_10034 (sheets 0004 to 0006, q0036 to q0049, one label per new component discussed)
- Evidence: wwdc2022_10169 (sheet 0010, q0086 and q0087; sheet 0013, q0116; sheet 0014, q0119 and q0123; sheet 0015, q0130, with a thin vertical line separating label and image)
- Evidence: wwdc2022_10009 (sheet 0015, q0128 to q0130, annotation correcting the naming directly over the real capture)
- Evidence: wwdc2021_10283 (sheet 0014, q0119 to q0121, a line connecting the label to the block and a vertical bracket grouping the list below)
- What this teaches about building interfaces: naming the piece in the image itself removes the ambiguity between the term and the pixel. The same screen appears several times, with only the annotated part changing.

## The same image appears twice, first clean and then annotated or completed, isolating exactly what the layer adds
- Evidence: wwdc2022_10169 (sheet 0010, q0086 and q0087, same capture without and with the label)
- Evidence: wwdc2021_10288 (sheet 0010, q0086, the card existed with only the title in the previous frame and gains the row of four icons)
- Evidence: wwdc2022_10037 (sheet 0002, q0013 to q0015, the Apple Music library first appears with only the colored icons and then with the labels alongside)
- Evidence: wwdc2022_10157 (sheet 0004, q0034 to q0036, the finished table receives the new badge and then disappears to leave the title alone)
- What this teaches about building interfaces: showing the screen without the labels before showing it with them is a legibility test performed in front of the audience. What cannot be understood without text needs text.

## Table comparison that isolates one variable per row, repeating the same content in every row so that only the parameter changes
- Evidence: wwdc2021_10349 (sheet 0003, q0021 to q0025, four color variations, three font sizes and three image scales of the same label)
- Evidence: wwdc2022_10157 (sheet 0004, q0028 to q0033, mode table assembled in stages with the same seven symbols in fixed columns)
- Evidence: wwdc2022_10034 (sheet 0008, q0064 to q0069, the same word repeated from the thinnest weight to the thickest, alongside a real app using those weights)
- Evidence: wwdc2022_10158 (sheet 0011, q0094 to q0098, four final versions of the same icon side by side with the mode name below)
- What this teaches about building interfaces: to choose a token value, assemble the same piece across all the options on the same screen. The difference appears through direct comparison, not through memory from one slide to the next.

## Regular grid of thin-stroke icons, white on black, with a short caption centered below, uniform spacing and no box separating items
- Evidence: wwdc2021_10304 (sheet 0002, q0010, twenty icons in four rows of five; the same grid returns on sheet 0019, q0167 to q0169)
- Evidence: wwdc2022_10157 (sheet 0002, q0017 and q0018; sheet 0003, q0019 and q0020, grids of about eight columns by four rows with uniform visual weight)
- Evidence: wwdc2022_10169 (sheet 0013, q0109, palette of fifteen circles in five by three; sheet 0014, q0126, sixteen types with a circular icon and label below)
- Evidence: wwdc2022_10158 (sheet 0006, q0046 to q0050, grid of twenty-seven icons in three rows of nine to show the combinatorial explosion)
- Evidence: wwdc2021_10288 (sheet 0010, q0086, four icons in a row with equal spacing and short centered captions)
- What this teaches about building interfaces: an inventory is shown in a regular grid, with no frame per item and no color, because the subject is quantity and stroke consistency. Color comes in later, when the subject becomes state.

## An item is pulled out of the grid and enlarged on its own at the exact moment the speech addresses it
- Evidence: wwdc2021_10304 (sheet 0002, q0011 to q0012; and sheet 0013, q0109 then q0112 and q0113, where two icons move closer together and come to share a single caption combining both conditions)
- Evidence: wwdc2021_10283 (sheet 0004, q0028 and q0029, the five principles first lined up and then isolated with their rules stacked)
- What this teaches about building interfaces: zooming within the same graphic system preserves the memory of the set. The person still knows where that item came from because the drawing did not change, only the scale.

## The abstract geometric diagram is paired with the real screen in the same frame, and the two change together
- Evidence: wwdc2022_10001 (sheet 0002, q0017; sheet 0011, q0092 to q0094; sheet 0012, q0100 and q0101, where the highlighted node changes from city to route and the capture alongside changes in the same proportion)
- Evidence: wwdc2022_10009 (sheet 0010, q0082 to q0086, three-block diagram on a white background followed by the literal application of the same grouping on the real screen)
- Evidence: wwdc2022_10169 (sheet 0007, q0059 to q0063, parameter tree in plain text alongside the screens where those combinations appear)
- Evidence: wwdc2022_10131 (sheet 0007, q0055, labeled cube connected to two rectangles in perspective; sheet 0008, q0061 and q0062, trapezoid extending from the device to represent field of view)
- Evidence: wwdc2021_10283 (sheet 0009, q0073 to q0076, fan-shaped lines extending from the base of the block to the property icons, with the real menu screen alongside)
- What this teaches about building interfaces: the mental model and the product stay in the same frame so the abstraction does not become loose theory. A rectangle, a line and the color of the active path are enough to draw hierarchy.

## Translucent materials with a visibly blurred and darkened background support temporary layers, and the video shows this without commenting on it
- Evidence: wwdc2022_10037 (sheet 0007, q0056 to q0058, the action sheet enters over the previous blurred screen, and q0060 and q0061 repeat the blurred background in the central alert)
- Evidence: wwdc2021_10283 (sheet 0003, q0019 to q0022, list of actions in frosted glass on the menu bar and white cards over a blurred wallpaper)
- Evidence: wwdc2022_10169 (sheet 0009, q0078 to q0080, translucent snippet letting the home screen icons show through blurred, with the four label color levels annotated on top)
- Evidence: wwdc2021_10349 (sheet 0007, q0055 and q0056, the third button in the row shows frosted glass blurring the background behind the arrow)
- Evidence: wwdc2022_10015 (sheet 0009, q0073 to q0077, the management screen reappears semi-transparent over another app in the background)
- What this teaches about building interfaces: the temporary layer is identified by its material, not by a border. The content below stays legible as context, blurred and darkened enough not to compete.

## Color has a fixed, reserved function, and red is kept only for destroying
- Evidence: wwdc2022_10037 (sheet 0010, q0088 to q0090, red remove button on the left and neutral blue on the right; sheet 0009, q0080 and q0081, only the recommended action in strong green and the secondary one in gray)
- Evidence: wwdc2022_10015 (sheets 0008 and 0009, communication buttons in filled orange, colored status dots and red reserved for the stop sharing button)
- Evidence: wwdc2022_10001 (sheet 0016, q0136 and q0137, action sheet with two stacked buttons and the destructive one in red)
- Evidence: wwdc2021_10304 (sheet 0022, q0195 to q0198, inside the floating card only the delete action appears in red)
- Evidence: wwdc2022_10139 (sheet 0006, q0051; sheet 0008; sheet 0014, where green consistently marks entry into the shared experience without the speech stating the convention)
- What this teaches about building interfaces: reserving a color for one consequence only works if it never appears with another role. The recommendation highlight is also color, so the screen needs at most one colored action at a time.

## Active state and selection are marked by solid fill or blue outline, never only by position
- Evidence: wwdc2021_10317 (sheet 0006, q0050, three-view segmented control with the active item filled in solid green)
- Evidence: wwdc2021_10288 (sheet 0002, q0015, blue square outline around the selected icon, and the inspector switching to the multiple selection label)
- Evidence: wwdc2022_10157 (sheet 0005, q0038 and q0039, open dropdown menu with the active item highlighted in blue)
- Evidence: wwdc2022_10158 (sheets 0002 and 0003, selected cell with blue outline in the grid; sheet 0009, q0073 to q0080, layer rows selected as a blue block)
- Evidence: wwdc2021_10349 (sheet 0003, q0026 and q0027, tab bar with the active tab in blue)
- What this teaches about building interfaces: selection needs a redundant signal, shape plus color, because position alone does not survive a dense grid, color blindness or a small screen.

## A green circular new badge in the corner and a gray box surrounding the newly added line mark what changed that year
- Evidence: wwdc2021_10349 (sheet 0003, q0027; sheet 0004, q0028 and q0033; sheet 0005, q0045; sheet 0006, q0049, always the gray box on the new line plus the green badge)
- Evidence: wwdc2022_10158 (sheet 0011, q0097 to q0099; sheet 0012, q0100 to q0106, green badge in the top right corner of the summary cards)
- Evidence: wwdc2022_10157 (sheet 0004, q0034, the finished table receives the green badge before giving way to the feature title)
- Evidence: wwdc2021_10288 (sheet 0010, q0082, card with a green circular badge next to the title)
- Evidence: wwdc2021_10283 (sheet 0016, q0138 to q0140, the already configured screen carries a green new badge and the other carries a yellow alert)
- What this teaches about building interfaces: the difference between what already existed and what is new deserves its own graphic marker, distinct from the approval marker, even if both are green.

## The component is presented as a fixed template with variable content, and the same anatomy reappears in different contexts
- Evidence: wwdc2022_10015 (sheet 0010, q0079 to q0085, banners with a circular avatar on the left, two lines of text, blue button and dismiss X, repeated for edit, comment, mention, creation and deletion)
- Evidence: wwdc2022_10139 (sheet 0002, q0013; sheet 0004, q0029; sheet 0015, the same banner design covering different events; and sheet 0008, q0064 and q0066, the card keeps its frame, title and button while the internal list switches from stripes to avatars)
- Evidence: wwdc2022_10037 (sheet 0005, q0040 to q0045 and sheet 0006, q0046 to q0050, the same introduction template in distinct contexts; sheet 0013, q0109 to q0112, empty states of two apps with identical skeleton)
- Evidence: wwdc2021_10304 (sheets 0018, 0019 and 0020, the Memory card always with a background photo, icons at the top, bold title and subtitle at the base)
- Evidence: wwdc2022_10001 (sheet 0004, q0035 and q0036; sheet 0005, q0037 and q0038, detail screens with cover, title, a two by two grid of metrics and scrollable blocks below)
- What this teaches about building interfaces: when the frame is constant and only the content changes, the person learns the component once and recognizes it anywhere. Empty states and alerts benefit from a shared skeleton.

## The layout is tested by compression on screen: the window shrinks, the text truncates, items drop in order
- Evidence: wwdc2022_10009 (sheet 0005, q0037 to q0039, the icons in the toolbar's central section disappear first and the groups at the ends remain; sheet 0003, q0024 to q0027, the title truncates gradually until it cuts the last letter)
- Evidence: wwdc2021_10283 (sheet 0002, q0012 to q0018, the two-column grid on iPhone becomes a compact vertical list on Apple Watch)
- Evidence: wwdc2022_10169 (sheet 0011, q0091 and q0092, the same confirmation card on the watch and on the phone, with adjusted spacing and icon)
- Evidence: wwdc2022_10015 (sheets 0003, 0006 and 0007, the same block hierarchy on iPad, iPhone and Mac, changing only the window frame, cursor and menu bar)
- What this teaches about building interfaces: decide in advance which item disappears first. Narrowing behavior is a design decision, not a result of whatever the layout happens to do on its own.

## Localization is shown as a real layout change, with the interface mirrored and the box growing, never as a concept
- Evidence: wwdc2022_10034 (sheet 0003, q0021 to q0027, gray wireframe and then the screens in Arabic with the mirrored composition; sheet 0004, q0028 to q0032, the carousel numbering goes from 1, 2, 3 with arrows on the right to 3, 2, 1 with arrows on the left; sheet 0012, q0102 to q0107, grid of pairs with purple highlight only on the icons that actually flip)
- Evidence: wwdc2022_10037 (sheet 0014, q0121 to q0124, the same box becomes visibly taller in Thai and mirrored in Hebrew; sheet 0015, q0127, spelled-out day headers in Arabic taking up much more space than the single letter in English)
- Evidence: wwdc2022_10001 (sheet 0012, q0105 and q0106, the screen reappears entirely mirrored in Hebrew, with the back button, icons, alignment and the annotations themselves switched to the other side)
- Evidence: wwdc2021_10288 (sheet 0002, q0018, the inspector lists the writing systems covered by a symbol, one line per writing system)
- What this teaches about building interfaces: the layout has to be designed to grow in height and width and to mirror entirely, and the flip is selective, some symbols flip and others do not.

## A small screen lives on maximum contrast and few elements, and the same family accepts opposite extremes of density
- Evidence: wwdc2021_10308 (sheet 0003, q0026, time at the top, index in uppercase, large value, variation in green and status in gray at the bottom over solid black; sheet 0004, q0034, just the time digits in pure yellow taking up almost the entire screen)
- Evidence: wwdc2021_110142 (sheet 0003, q0025, same typographic ladder in the Stocks app; sheet 0004, q0029 versus q0032, a dense watch face with date, weather and three complications next to a watch face with only the giant time)
- Evidence: wwdc2022_10037 (sheet 0008, q0066 and q0069 to q0072, colored icon or ring aligned with the time, bold title, smaller body and stacked full-width rectangular buttons)
- What this teaches about building interfaces: on a small surface, contrast sustains readability and the hierarchy is purely vertical. The same language needs to cover both the dense version and the single-data-point version.

## The control lives over the camera image, inside the field of attention, not in a separate bar
- Evidence: wwdc2022_10131 (sheet 0002, q0013 to q0016, minimal HUD with a marked distance line, scanning icon and circular button; sheet 0005, q0037 and q0038, a single vertical line and the large value at the top; sheet 0008, q0070 to q0072, out-of-frame indicator with short text and a directional arrow)
- Evidence: wwdc2021_10304 (sheet 0004, q0034 and q0035, dotted line, large numeric label and thin progress bar inside the device's semitransparent frame; sheet 0003, q0026 and q0027, yellow rectangles marking each stretch of recognized text in the viewfinder)
- Evidence: wwdc2022_10037 (sheet 0010, q0083, the Panorama orientation arrow stays centered in the viewfinder)
- Evidence: wwdc2021_10317 (sheet 0013, q0110 and q0112, telemetry in a small monospaced font overlaid on the video, with no box or background)
- What this teaches about building interfaces: when the task happens in the image, the indicator goes in the image, small, with no solid background, and only the value that matters gets a large size.

## Real-time updating is proven by the number that changes between two consecutive frames
- Evidence: wwdc2021_10317 (sheet 0008, q0071 to q0072, the countdown drops two seconds from one frame to the next)
- Evidence: wwdc2022_10131 (sheet 0005, q0037 to q0038, the measurement value changes between frames)
- Evidence: wwdc2022_10158 (sheet 0003, q0022 and q0023, the percentage field moves off zero and the icon's drawing reacts)
- Evidence: wwdc2022_10009 (sheet 0014, q0118 to q0124, the repeat field value changes inside the same floating card, without opening a new screen)
- What this teaches about building interfaces: continuous feedback needs a stable numeric target on screen, always in the same place, so that only the value moves.

## Measurement and threshold are annotated on the image itself, with the number written next to the example
- Evidence: wwdc2022_10034 (sheet 0011, q0091 to q0094, the same text labeled with 0, 10 and 20 percent spacing, with a thin bar marking the join between letters at the higher value; q0095 and q0096, the opacity value annotated below the example)
- Evidence: wwdc2022_10158 (sheet 0004, q0031 to q0036, segmented horizontal bar with numeric markings and an indicator dot, with the icon lighting up in parts; sheet 0005, q0039 to q0041, the same scale with thresholds broken at 34% and 68%)
- Evidence: wwdc2021_10288 (sheet 0004, q0035; sheet 0005, q0038 to q0040, color picker with a percentage value alongside it and a color list with its own percentages per line)
- Evidence: wwdc2022_10131 (sheet 0002, q0013 to q0016, the measurement overlaid on the silhouette; sheet 0008, q0070, a percentage scale marker appearing over the object)
- What this teaches about building interfaces: a number in the image turns opinion into specification. A continuous-range control becomes understandable when the thresholds are drawn, not described.

## The element's internal structure is exposed as a vertical list of named layers, one line per layer with a thumbnail
- Evidence: wwdc2021_10288 (sheet 0006, q0054, layer list with thumbnail and color name; sheet 0007, q0059 to q0060, the list goes from one line to two with the active one in blue outline)
- Evidence: wwdc2022_10157 (sheet 0006, q0052; sheet 0007, q0058, q0061 and q0062, diamonds stacked in a light isometric perspective, numbered from the base to the top, with a depth-order axis starting from sheet 0009)
- Evidence: wwdc2022_10158 (sheet 0008, q0064 to q0071, the list evolves from one entry to three named per level, each line with a square thumbnail, name, percentage field and action icons)
- Evidence: wwdc2021_10349 (sheet 0006, q0049 to q0053, up to three colors mapped to named categories, with the category dimming when the drawing doesn't have that layer)
- What this teaches about building interfaces: when an element has parts, show the named stack next to the result. A layer that doesn't exist stays visible and dimmed, instead of simply disappearing from the list.

## The authoring tool appears on screen in its three-column layout, categories on the left, grid in the center, inspector on the right
- Evidence: wwdc2021_10288 (sheet 0001, q0009 and sheet 0002, with the sidebar separating fixed categories from the user's collections by a divider, item counter in the header and inspector alternating between empty and detail)
- Evidence: wwdc2022_10157 (sheet 0003, q0023 and q0024, switching the category in the sidebar swaps the central grid entirely)
- Evidence: wwdc2022_10158 (sheets 0002, 0003 and 0007 to 0011, the inspection panel always keeps the same vertical order of sections)
- Evidence: wwdc2022_10034 (sheet 0013, q0109 and q0110, the same app on the Mac with sidebar, grid and detail panel showing the list of covered scripts)
- What this teaches about building interfaces: navigating, listing and inspecting call for three stable regions. The inspector keeps the order of sections even when their content changes with the selected mode.

## Code appears in minimal doses, always glued to the rendered result within the same frame
- Evidence: wwdc2021_10349 (sheets 0001 to 0007, code on the left in colored monospace and result on the right, from the first example to the final table, with the notes recording that this structure is not stated in the speech)
- Evidence: wwdc2022_10139 (sheet 0012, q0105 and q0106; sheet 0014, q0119 to q0123; sheet 0017, where the line on a black screen coexists in the same frame with the iPhone frame, one short line per concept, with no editor and no numbering)
- What this teaches about building interfaces: one line per concept, always next to the visible effect. The code works as a caption for the behavior, not as a snippet to copy.

## The frame captures the animation midway, with the new screen partially over the old one
- Evidence: wwdc2022_10001 (sheet 0010, q0082 and q0083, the new screen covers almost all of the previous one coming from the right; sheet 0012, q0104, two screens overlapping diagonally between list and detail)
- Evidence: wwdc2022_10015 (sheet 0009, q0073 to q0077, the popover dissolves under the management screen until it becomes sharp)
- Evidence: wwdc2021_10288 (sheet 0003, q0019 to q0027, the capture darkens in stages, the title enters semitransparent over the still-visible screen and the app reappears behind the text at the end)
- Evidence: wwdc2021_10304 (sheet 0020, q0172 to q0173, four cards go from an overlapping fan to an aligned, evenly spaced row)
- Evidence: wwdc2022_10037 (sheet 0010, q0088 to q0090, the same alert in three brightness variations, recording a fade in)
- What this teaches about building interfaces: the transition is part of the component. Partial coverage coming from one direction tells the relationship between the screens, and the dissolve marks a change of context without changing place.

## Continuous movement is represented inside a still frame, through the juxtaposition of poses, double exposure or blur
- Evidence: wwdc2021_110142 (sheet 0007, q0055 and q0056, the same watch face with two foot positions side by side and then three, building the animation's progression without video)
- Evidence: wwdc2022_10131 (sheet 0008, q0065 to q0066, the same person in two semitransparent poses overlapping in the same frame)
- Evidence: wwdc2021_10308 (sheet 0007, q0058 to q0060, a row of five thumbnails of the same watch face with the finger in a slightly different position; sheet 0011, q0097 to q0099, the hand appears blurred while the screen reacts)
- What this teaches about building interfaces: to document animation in static material, freeze the extreme frames and the middle one, side by side. Selective sharpness separates what moves from what stays still.

## The screen's presentation regime changes according to the subject: layout comes isolated on a neutral background, gesture and context come filmed on the person's body
- Evidence: wwdc2021_10304 (sheets 0003, 0010, 0011, 0014, 0018, 0019, 0022 and 0023, captures always centered on a black background or inside a drawn frame with notch and status bar, never with a hand holding the phone)
- Evidence: wwdc2021_113 (sheet 0008, q0071; sheet 0009, q0073; sheet 0014, almost every frame, with real hands touching, dragging and typing on iPad and iPhone)
- Evidence: wwdc2021_110142 (sheet 0011, q0093, q0094 and q0099, each screen appears paired with a close-up of the hand performing the corresponding gesture)
- Evidence: wwdc2021_10308 (sheet 0004, q0031 and q0032, a finger touches the screen directly and the text scrolls between one frame and the next)
- What this teaches about building interfaces: show the hand when the subject is reach, touch and posture, and remove the hand when the subject is grid, spacing and hierarchy. The framing decides where the attention goes.

## The device or window frame comes in as a platform signal, not as decoration
- Evidence: wwdc2021_10349 (sheet 0005, q0039 to q0042, a simulated macOS window with the three colored buttons serves as the frame to show the mode switch in that context)
- Evidence: wwdc2022_10015 (sheets 0003, 0006 and 0007, the same hierarchy across three devices, changing only the frame, cursor and menu bar; on the Mac, the permissions menu becomes a text list with no icons)
- Evidence: wwdc2021_10304 (sheets 0003, 0010 and 0014, the captures come inside a frame with notch and status bar)
- Evidence: wwdc2021_110142 (sheet 0003, q0020 and q0025, the screen appears on the watch with the band, recorded as a real context of use)
- What this teaches about building interfaces: the frame communicates which system that rule applies to and why controls change shape between platforms.

## The flow is shown in full, screen by screen, in the order it happens, with real screens from the system
- Evidence: wwdc2022_10015 (sheet 0003, q0019 to q0027, document open, sharing popover, message composition with the card attached, recipient change, entry alerts and the final collaboration popover)
- Evidence: wwdc2022_10139 (sheet 0014, q0119 to q0126, share sheet rising from the bottom, choosing friends with preview and keyboard, and the result as an invitation bubble in the conversation)
- Evidence: wwdc2022_10001 (sheet 0017, q0145 to q0152, pushing within the form, modal covering the screen, photo picker in a grid with a numbered indicator and the return to the form already with the thumbnail marked)
- Evidence: wwdc2021_10283 (sheet 0012, q0100 to q0107, the same parameter resolved first in the Mac editor and then by voice, with the selection screen next to the question card)
- What this teaches about building interfaces: the value is in the seams. Showing where you enter from, what changes in the middle and how you go back exposes the points where the flow breaks.

## Before any product screen comes a narrative opening that stages the problem
- Evidence: wwdc2022_10015 (sheet 0001, q0008 and q0009; sheet 0002, q0010 to q0015, the email icon turns into an avatar with an envelope badge and then all the badges turn into the messages icon, staging the channel switch)
- Evidence: wwdc2022_10139 (sheets 0001 to 0005, two and a half minutes of staging almost entirely in black and white with a circular vignette on the close-ups, with an abrupt cut to the colored studio at q0042)
- Evidence: wwdc2022_10037 (sheet 0001, q0008 and q0009, the cursive word appears inside the screen of a beige Macintosh and in the next frame it leaves the frame, bigger and in a colored gradient, in the same handwriting)
- Evidence: wwdc2022_10157 (sheet 0001, q0007 to q0009, a grid of three columns by four rows with the same word in several languages and scripts, a red heart as the only exception to the color)
- What this teaches about building interfaces: the thesis comes before the screen. The opening establishes the problem with image and typography, without asking the person to already know how to read the product.

## Physical analogy and real object replace the screen when the subject is a concept
- Evidence: wwdc2021_10283 (sheet 0002, q0010 to q0016, colored building blocks snapping together next to the action blocks to explain modularity)
- Evidence: wwdc2022_10139 (sheet 0009, q0077, close-up of the hand landing on the arm of a record player, with no screen at all in the scene; sheet 0019, q0163 to q0165, photographed handcrafted objects marking the turn toward the close)
- Evidence: wwdc2022_10009 (sheet 0016, q0140 to q0142, a still life of a toy and a bowl stays fixed on the right while the bullets enter one per cut)
- Evidence: wwdc2021_10308 (sheets 0001 to 0013, the articulated wooden mannequin on a circular pedestal repeats from sheet to sheet as scenic continuity between interviewees)
- What this teaches about building interfaces: a recognizable object carries the concept without jargon and gives a stable visual anchor while the text changes beside it.

## The gray wireframe appears as a real stage of the process, not as a figure of speech
- Evidence: wwdc2022_10034 (sheet 0003, q0021 to q0027, the same three screens reduced to gray blocks for title, image, text, pagination dots and tab bar, and only afterward back as real screens)
- Evidence: wwdc2022_10037 (sheet 0004, q0033 to q0036, the rejected version of the alert is a dense wireframe with title, alert icon, two paragraphs and a large red button, against the approved version reduced to icon, short title, one sentence and a capsule button)
- Evidence: wwdc2022_10139 (sheet 0016, q0143 and q0144, a simulated mind map with colored sticky notes connected by thin lines to a central node, with a drawing bar at the bottom)
- What this teaches about building interfaces: the low-fidelity draft proves structure without discussing color, and serves as the wrong side of a pair when the problem is excess content.

## Accessibility is shown as a data structure, not as appearance
- Evidence: wwdc2021_10349 (sheet 0002, q0014 to q0018, the drawing of the symbol is replaced in the right column by the text that would be read out loud, first generic, then the technical name and finally the descriptive caption)
- Evidence: wwdc2022_10037 (sheet 0015, q0133 to q0135, each sticker appears with its technical identifier in quotation marks next to the description, the three pairs stacked one by one)
- Evidence: wwdc2021_10304 (sheet 0011, q0091 to q0096, the photo passes through the photos app, through the Markup tool with the description option and arrives in the conversation with the description written by the person in a separate bubble)
- What this teaches about building interfaces: the description is a named field that accompanies the element, and it needs to be designed together with the drawing, not afterward.

## The video itself applies accessibility and attribution, with a fixed interpreter in the corner and credits inside the image
- Evidence: wwdc2021_110142 (sheet 0001, q0001 to q0009, the interpreter's frame always appears in the same position and composition, treated as permanent across all sheets)
- Evidence: wwdc2021_113 (sheets 0001 to 0019, fixed square portrait of the interpreter on a light gray background to the right of the main scene)
- Evidence: wwdc2021_10308 (sheets 0006 to 0008, the character rights notice stays fixed in the bottom left corner of the watch's own screen)
- Evidence: wwdc2021_10317 (sheet 0007, q0057 to q0060, attribution captions always in the bottom right corner, keeping the position across images from different sources)
- What this teaches about building interfaces: persistent accessibility and credit elements get a reserved position that never changes, and the rest of the layout is designed around that reservation.

## Person and product identification follows a fixed caption template, with no background box
- Evidence: wwdc2021_113 (sheet 0004, q0036; sheet 0005, q0037 to q0042, larger name in white and smaller title in gray, two lines aligned left; and sheets 0006 to 0033, the app badge in the bottom left corner with icon, name and status label changing only the word)
- Evidence: wwdc2021_10317 (sheet 0020, q0176, the logotype shown combines an icon on the left and a text block on the right with two weights in the name and tagline in uppercase with increased tracking)
- What this teaches about building interfaces: a name and qualifier pair in two weights, aligned left and with no background, is enough to identify over any image, as long as the video's contrast is controlled.

## The end of a block and the end of the session have a standardized form: a footer referencing another session and a centered institutional card in black
- Evidence: wwdc2021_10288 (sheet 0008, q0072; sheet 0010, q0089, name of another session on the left and event year on the right, separated once by a thin line; sheet 0011, q0095, closing with the apple and the event name centered)
- Evidence: wwdc2022_10157 (sheet 0011, q0099; sheet 0012, q0100, same footer pattern with small text on the left and event acronym on the right)
- Evidence: wwdc2022_10009 (sheet 0016, q0140 to q0142, the closing slide accumulates bullets and ends with a footer pointing to another session)
- Evidence: wwdc2021_10308 (sheet 0014, q0123 and q0124) and wwdc2022_10131 (sheet 0011, q0092 to q0093, where between the last two frames only the weight and the tone of the text change)
- What this teaches about building interfaces: a predictable, quiet closing avoids competing with the content, and the cross-reference has a fixed place instead of becoming just another list item.

## The event's institutional opening uses a grid of hundreds of thumbnails of people followed by a particle explosion
- Evidence: wwdc2021_10308 (sheet 0001, q0001 and q0002, mosaic of faces in light blue rounded rectangles with tiny icons overlapping, followed by particles as a transition)
- Evidence: wwdc2021_10317 (sheet 0001, q0001 to q0002, grid of circular avatars with overlapping pills and then two confetti explosions over the same unchanged grid)
- What this teaches about building interfaces: repeating a small module in a regular grid creates scale and a sense of community without any item needing to be legible.

## Single-source findings

- The external vector editor appears with rulers, a blue guide and a red guide crossing the icon, and a position, size, opacity and shadow panel, and returning to the app goes through a replacement modal dialog with the confirm button in blue as the default action: wwdc2021_10288 (sheet 0006, q0047 to q0051).
- Paste as text and paste as image produce different and visible results: in the first case the symbol stays on the same baseline, color and weight as the word next to it, as if it were a character; in the second it becomes an object with selection handles and numeric fields for position and size: wwdc2021_10288 (sheet 0008, q0066; sheet 0009, q0080).
- The availability inspector stacks two entries for the same design, the current name with a line per rendering mode and version number on the right, and below it the deprecated name marked with a warning triangle: wwdc2021_10288 (sheet 0003, q0019).
- Duplicated content between tabs is drawn as columns with the items below and, in the next frame, the same names repeated under more than one column inside dashed boxes: wwdc2022_10001 (sheet 0007, q0062 and q0063).
- The modal's navigation bar is broken down annotation by annotation on the same screen, including the list of possible alternative labels for the right button and that button's grayed-out state while the form is incomplete: wwdc2022_10001 (sheet 0015, q0130 to q0135).
- The same close button is judged by context: acceptable in an editorial article with no data entry and problematic in a filter screen whose items get a selection mark between one frame and the next: wwdc2022_10001 (sheet 0016, q0138 to q0142).
- The toolbar customization panel shows the icons in rounded squares with a yellow dashed outline indicating that they are draggable, and the document body stays still while only the bar above it changes: wwdc2022_10009 (sheet 0004, q0029 to q0032).
- The edit menu exists in two variants with the same internal item order, horizontal and compact next to the text for touch, vertical in a list with an icon on the right for pointer: wwdc2022_10009 (sheet 0007, q0056 to q0060).
- Find and replace changes shape depending on the keyboard: a dropdown menu with advanced options anchored above the virtual keyboard, and a compact bar at the bottom with a field, results counter and arrows when there is a physical keyboard: wwdc2022_10009 (sheet 0008, q0064 to q0066).
- Multiple selection without an edit mode: the title is replaced by a count, the cards get highlighted and each label in the actions menu repeats the number of items: wwdc2022_10009 (sheet 0011, q0091 to q0096).
- Notification consolidation only becomes evident when comparing frames: the stack of individual banners accumulates, the older ones fade and the whole stack is replaced by a single banner with a count of people and documents, with the button label changing along with it: wwdc2022_10015 (sheet 0010, q0082 to q0086).
- The typographic study takes the letter out of context and breaks it down into four positional forms in a row, each with a position label below, before showing the full grid of glyph variations: wwdc2022_10034 (sheet 0007, q0055 to q0058).
- Two numeral systems are separated by a simple caption under each number and then applied in four contexts, including a calculator with a mirrored keypad and a watch face with clearly distinct shapes and colors between the versions: wwdc2022_10034 (sheet 0014, q0118 to q0124).
- The closing combines the guidelines page open on a laptop with a grid collage bringing together thumbnails of almost all the examples already shown in the session: wwdc2022_10034 (sheet 0015, q0127 to q0132).
- The environment onboarding uses three screens with identical structure, with a short uppercase title, body, page indicators as dots and a full-width button, and overlays green and red icons on the camera image to indicate surface and light state: wwdc2022_10131 (sheet 0006, q0048 to q0052).
- Scanning progress is a thumbnail of a three-dimensional floor plan in the corner that gains shapes with each frame, accompanied by thin neon outlines tracing walls and furniture already detected, with cancel and done in opposite corners at the top: wwdc2022_10131 (sheets 0004 and 0009, q0031 and q0032, q0074 to q0078).
- Occlusion as a depth cue is demonstrated with the virtual object partially hidden behind real blocks on the table, right after the list of five cues in plain text: wwdc2022_10131 (sheet 0009, q0080 and q0081).
- The asymmetry of what each participant sees is shown with three identical frames, and in a following frame the one on the left starts showing question marks instead of the answer while the button's text changes: wwdc2022_10139 (sheet 0013, q0109 and q0111).
- The session details sheet separates who is on the call from who is in the activity, with a block for what is playing, a count of active people, a red leave button and a distinct text status per person: wwdc2022_10139 (sheet 0015, q0130 to q0133).
- The curation of invocation synonyms is shown as visible list editing, with an option already struck through that disappears in the next frame while the lines below a certain point darken: wwdc2022_10169 (sheet 0006, q0046 and q0047).
- The equivalence between spoken dialogue and visual component is stated as an equation, with an equal sign between the snippet plus supporting dialogue and the full dialogue: wwdc2022_10169 (sheet 0010, q0089 and q0090).
- The dynamic reordering of suggestions is proven with pairs of screens in which the card in the first position swaps items between frames, with the shortcuts app on the left and the suggestions on the right: wwdc2022_10169 (sheet 0012, q0103 to q0107).
- The degree of immersion of a screen is judged in the image: the slide about customizing a watch face accumulates lines of text next to the rich editing screen and gets an X in the last frame, followed by the simple case of just switching watch faces: wwdc2021_10283 (sheet 0005, q0040 to q0044).
- The three states of a parameter appear in the same block shape with a caption below, no value, default value and the always-ask option, each next to the device that resolves that case: wwdc2021_10283 (sheet 0015, q0127 to q0129).
- The process diagram changes shape within the narrative, from a horizontal line with five words and colored dots to a ring with no dots, with a triangular arrow at the top marking the current step and the ring actually rotating between frames: wwdc2021_10304 (sheet 0007, q0055 to q0057; sheet 0016, q0141 to q0142).
- The same icons from the axis grid reappear as a semitransparent caption in the lower band of a real filmed scene, annotating context about everyday life: wwdc2021_10304 (sheet 0008, q0070).
- An icon change is communicated only through a visual pair, with no label, with the old glyph next to the new one in the same thin stroke and the same color: wwdc2021_10304 (sheet 0024).
- The navigation contrast between two system apps is placed side by side: one screen has back and forward arrows before the title and the other, denser and with collapsible sections in the sidebar, has no control of that kind at all: wwdc2022_10009 (sheet 0009, q0076 versus q0079).
- The custom symbol is deliberately designed in a simplified shape, a solid cube with a grid pattern on the faces, omitting details of the real object to survive at small sizes: wwdc2022_10158 (sheet 0007).
- The contrast failure is shown as a concrete failure: the version inside a circle in monochrome becomes almost a black disc with no detail, and the fix appears in the next frame with two eraser-type layers identified by a hatched thumbnail: wwdc2022_10158 (sheets 0010 and 0011, q0085 to q0093).
- The phone game HUDs shown at the awards share the same layout, controls on the left, skill cluster in an arc in the bottom right corner, health bar above the character and minimap at the top: wwdc2021_113 (sheets 0028, 0033 and 0034).
- Assisted reading is shown by the difference between two frames of the same text, with the highlighted word changing position and color, from yellow to blue, to indicate the progress of the narration: wwdc2021_113 (sheet 0007, q0060 to q0061).
- The separation of a rocket's stages is communicated through an exploded-view diagram, two components isolated and spaced apart over a neutral background, with no caption at all: wwdc2021_10317 (sheet 0012, q0105).
