# ess-04, recurring visual patterns

Basis: 21 visual syntheses read from beginning to end, 4 HIG pages (widgets, windows, workouts, writing) and 17 videos (meet-with-apple 208, 254, 255, 256, 257, 270, 274; tech-talks 801, 802, 803, 10884, 111427, 111461, 111462, 111463, 111466; wwdc2014_223).

## The list of topics stays on screen with the current item in white and the rest dimmed, and it is the list that marks the chapter turn
- Evidence: meet-with-apple_270 (agenda of three topics with the item in progress highlighted and internal submenus in the same pattern, sheet 0001, q0003 to q0009)
- Evidence: meet-with-apple_274 (agenda in a column beside the presenter, section item fully white and the others in gray, sheet 0001, q0002 to q0009)
- Evidence: tech-talks_111462 (agenda slides in black and white, without icon, repeated four times throughout the video, sheet 0003 q0019 and q0025, sheet 0008 q0071, sheet 0015 q0131)
- Evidence: tech-talks_10884 (list of principles first whole over two dimmed watches, then with the section item in bold, sheet 0001 q0008, sheet 0008 q0064, sheet 0009 q0073)
- Evidence: tech-talks_803 (the three principles as a progress trail, ending with all three in white to signal the close, sheet 0001 q0005 and q0006, sheet 0006 q0052)
- What this teaches about building interfaces: navigation state can be communicated by text weight and opacity alone, without color, without icon and without a selection frame. The same list serves as summary, position indicator and transition, with a single attribute varying.

## A label connected by a straight line to a part of the screen is the standard anatomy device, always over an interface already shown clean before
- Evidence: meet-with-apple_208 (callout lines on Conversation Headers, Composer, Create Menu and Tab Bar, and in the article on Title, Byline, Image and Paragraph, with the labels entering after the clean screen, sheet 0023 q0203 to q0204, sheet 0027 q0235 to q0238)
- Evidence: meet-with-apple_270 (anatomy of the list row drawn with straight lines connecting Image to the thumbnail, Subtitle to the secondary text and Selection button to the blue circle, sheet 0008, q0068 to q0072)
- Evidence: tech-talks_111463 (instructional labels positioned outside the device frame, next to the area they identify, without altering the interface, sheet 0013, q0114 to q0116)
- Evidence: tech-talks_10884 (defect label with a vertical line pointing to the left edge, between a frame without a label before and another without a label after, sheet 0003, q0019 to q0021)
- Evidence: tech-talks_803 (arrow callouts, one per frame, over the same offer screenshot, sheet 0004, q0031 to q0033)
- What this teaches about building interfaces: the annotation never replaces the screen, it enters and exits over a real screenshot the reader has already seen intact. Naming each region with the name the team uses is what turns a mockup into a specification.

## The judgment of right and wrong comes as a visual pair, marked by a circular seal, green check on one side and red X on the other
- Evidence: tech-talks_801 (the pair of red circle with X and green circle with check appears at least six times in the same format, on rotation, icons glued to the corners, scroll bar and button in the safe area, sheet 0005 q0037 and q0045, sheet 0006 q0046 and q0047, sheet 0007 q0056, q0057, q0061 and q0062)
- Evidence: meet-with-apple_270 (three degrees in the same sequence, yellow alert on the bar with five labeled tabs, red X on the customized bar with colored pills and green check on the native bar with icon and label, sheet 0003 q0024 to q0027, sheet 0004 q0028 to q0034)
- Evidence: widgets (StandBy pair, the clock and the Weather without a card receive a green check, the Weather that keeps the rounded card with shadow receives an X, img 1317 to img 1321)
- Evidence: tech-talks_111462 (green check on the code block that uses a navigation container and red X on the one that instantiates the bar directly, sheet 0004, q0034 and q0035)
- Evidence: meet-with-apple_256 (two nearly identical phones labeled with and without nested glass, making visible the double translucency that the speech only describes, sheet 0004, q0034 and q0035)
- What this teaches about building interfaces: the wrong example is worth more when it is almost identical to the right one. Changing a single variable, keeping everything else frozen and stamping the verdict makes the eye find the difference without depending on the text.

## The same screen is repeated side by side with a single variable changing, and it is the repetition that proves the rule
- Evidence: widgets (the same small Stocks widget, identical layout, in full color, light, tinted and monochrome, changing only color and opacity, img 1296 to img 1300)
- Evidence: meet-with-apple_255 (the same workspace screen in five theme variations, identical structure, only header color and accent color changing, sheet 0006, q0047 to q0051)
- Evidence: meet-with-apple_257 (four iPhones labeled iOS 12, 14, 18 and 26 with the same screenshot framed, sheet 0001, q0007 and q0008)
- Evidence: tech-talks_111461 (the same content under a footer caption naming the SDK version, single column, two-column grid and four-card grid, sheet 0001 q0005 to q0009, sheet 0002 q0010)
- Evidence: tech-talks_111466 (grid of six renders of the same app in every device pose, repeated twice with different content, sheet 0006 q0047 and q0048, sheet 0011 q0093 and q0094)
- What this teaches about building interfaces: if the layout can withstand changing theme, system generation, device and pose without reorganizing, it is a system and not a drawing. The proof is assembling the variants in the same composition, not claiming that it works.

## Code and result stay in the same frame, with the line in question highlighted and the highlight moving while the mockup stays still
- Evidence: tech-talks_111462 (systematic juxtaposition of a comment naming the API, a snippet with syntax highlighting and the mockup beside it, across ten sheets, with the blue highlight switching snippet between frames while Mail stays identical, sheet 0007, q0061 to q0062)
- Evidence: tech-talks_10884 (code panel beside the watch, with the margin modifier line inserted and an orange arrow connecting the snippet to the corresponding element on the screen, sheet 0003, q0022 to q0026)
- Evidence: tech-talks_111461 (panels pairing SwiftUI and UIKit in the same frame or in immediate sequence, beside the render, sheet 0003 q0024 and q0025, sheet 0005 q0037 to q0038, sheet 0006 q0052 to q0054)
- Evidence: meet-with-apple_270 (API name overlaid on the mockup itself as an annotation, on the screen title and on the filled blue circle button, sheet 0005 q0045, sheet 0007 q0055 to q0058)
- Evidence: tech-talks_111463 (code assembled line by line, with a temporary blue highlight that disappears in the following frame to signal that the line has settled, sheet 0007, q0060 to q0063)
- What this teaches about building interfaces: a layout decision only becomes transferable when the person sees which line produces which pixel. Temporary highlighting directs the eye better than numbering or caption.

## Measurement appears written on the drawing itself, in dimensions and arrows, and the speech almost always does not state the number
- Evidence: meet-with-apple_270 (blue guides in brackets around the hexagonal icon and annotations of 40px, 20px and 10px on the margins of the achievement card, with the speech not citing values, sheet 0014 q0125 and q0126, sheet 0015 q0127 and q0128)
- Evidence: tech-talks_801 (lines, arrows and numbers in light blue over the outlines, with the same pair of blocks switching the unit between frames, first pixels and then points, sheet 0001, q0008 to q0009)
- Evidence: tech-talks_802 (rectangles dimensioned in pixels for each watch size and icon specification with exact measurements in pixels and points for notification and home screen, sheet 0001 q0004 to q0009, sheet 0006 q0053)
- Evidence: tech-talks_10884 (the 41 mm dimension beside the pair of boxes and the 41 mm and 45 mm dimensions together in the following render, sheet 0001, q0004 and q0005)
- Evidence: windows (the opening reduces the window to a silhouette with no content, with double-headed measurement arrows on the right and bottom edges, img 1324)
- What this teaches about building interfaces: spacing and size numbers belong in the image, not in the caption. The person building needs the dimension beside the element, with the unit explicit, because pixel and point are not interchangeable.

## Layers of solid or semi-transparent color are pasted over the screenshot to make visible a zone that has no shape of its own
- Evidence: tech-talks_802 (the watchOS screen structure is assembled in colored zones over a sample layout, blue title bar, gray margin strip, purple scroll area strip, and then the strips disappear, sheet 0003, q0019 to q0027)
- Evidence: tech-talks_801 (solid green blocks labeled as safe area reused in different contexts, and two color layers separating a red navigation bar from indented green content, sheet 0003 q0024 to q0027, sheet 0004 q0029 to q0030)
- Evidence: tech-talks_111461 (green filling the entire screen to demonstrate concentricity with no content around it, and semi-transparent blue that changes meaning between frames, from the whole content area to a narrow strip on the left edge, sheet 0005 q0037 and q0038, sheet 0006 q0052, sheet 0007 q0055 to q0057)
- Evidence: tech-talks_111466 (solid gray strip between the text columns labeled as layout margin and blue strip on the right edge labeled as safe area inset, switching color and position from one frame to the other, sheet 0006, q0050 and q0051)
- What this teaches about building interfaces: margin, safe area and reserved region are invisible rectangles that govern the layout. Painting them in distinct colors, one per concept, keeps them from being confused with each other.

## Interaction state is recorded in the difference between two consecutive frames, with the rest of the layout frozen
- Evidence: tech-talks_111462 (the inbox icon shows a loose number beside it and in the following frame a red circular badge over the icon itself, with no other change, sheet 0012, q0107 to q0108)
- Evidence: meet-with-apple_257 (the same tide chart card appears flat and frontal in one frame and tilted in perspective in another, making visible the effect that only appears during touch, sheet 0004, q0033 and q0035)
- Evidence: meet-with-apple_208 (the message cell slides and turns blue with the keep-as-unread action, above the fixed buttons, sheet 0017, q0149 to q0150)
- Evidence: widgets (the same Reminders widget side by side, seven empty circles and then the first and third filled in solid red, with no other layout change, img 1307 and img 1308)
- Evidence: tech-talks_801 (three states labeled with the same behavior name, the start indicator as a thin line, with a blue circle suggesting the touch, and back to the simple line, sheet 0008, q0065 to q0067)
- What this teaches about building interfaces: state is documented by pair, not by description. Freezing everything that does not change is what makes the reader see the one thing that changes.

## Placeholder and scaffolding reuse the geometry of the final content instead of leaving it empty
- Evidence: widgets (three lighter yellow bars of decreasing widths on the yellow card become the three lines of real text in the loaded version, img 1312 and img 1313)
- Evidence: tech-talks_802 (the content area filled in solid green whenever the point is the available space and not the content, plus wireframes with an X image placeholder and filler text, sheet 0001 q0004 and q0005, sheet 0004 q0030 to q0033)
- Evidence: wwdc2014_223 (gray rectangles covering the navigation bar, thumbnails and tab bar of the Music app screen used as scaffolding, and five cells filled by repeating the same few photos, sheet 0010 q0082 to q0085, sheet 0011 q0091 to q0097)
- Evidence: workouts (a metric with no data appears filled with dashes, keeping the average pace label in place, img 1335)
- What this teaches about building interfaces: empty is never empty, it is the same box with neutral filler. This keeps the rhythm and line height stable between loading, no data and loaded.

## The list grows item by item while the previous ones stay intact, and each new item swaps the image beside it
- Evidence: meet-with-apple_255 (the row of principles grows from one to five, each with a line-drawing figure illustration and a name in small text below, sheets 0003 and 0004, q0019 to q0032)
- Evidence: meet-with-apple_256 (the list of takeaways is built item by item, always with a different example image beside it, sheets 0004 and 0005, q0034 to q0038)
- Evidence: tech-talks_111463 (the container diagram assembles in layers, navigation containers in blue, then content containers in red, then layout containers in green inserted between the two previous bands, sheet 0009, q0073, q0078 and q0079)
- Evidence: tech-talks_802 (the type scale table is built in two stages, first the smaller styles and then the four larger ones added above, sheet 0005, q0042 to q0044)
- Evidence: meet-with-apple_274 (the scale numbers are revealed one by one from left to right on cards with a translucent dark green background, sheet 0002, q0016 to q0018)
- What this teaches about building interfaces: progressive revelation without reflow. What has already entered does not move, what enters occupies space already reserved, and the change of context happens in the panel beside it.

## The vocabulary is fixed by an abstract diagram before any real interface enters the scene
- Evidence: tech-talks_111461 (size class explained first through gray rectangles with measurement arrows, orange on the horizontal and blue on the vertical, and unlabeled shapes representing the folded device, before any app, sheet 0003 q0024 to q0025, sheet 0004 q0028 to q0030)
- Evidence: wwdc2014_223 (two rectangles labeled Slide 1 and Slide 2 with circles as generic elements, connected by an arrow whose label changes while the drawing stays the same, and only then does the real tool capture enter, sheet 0021, q0181 to q0189)
- Evidence: tech-talks_801 (the scale factor becomes a diagram of three circles of increasing size with labels below, associated with each device, before any capture, sheet 0001, q0003 and q0004)
- Evidence: tech-talks_10884 (the button system is presented as a diagram of two named columns, with color coding by hierarchy, green for primary, gray for secondary and blue for toolbar, sheet 0006, q0046 to q0050)
- Evidence: tech-talks_111463 (the concept of arrangement is built in three diagram stages, an inputs box, an empty outputs box and the arrow connecting the two once filled, sheet 0010, q0086 to q0088)
- What this teaches about building interfaces: naming the structure with empty shapes before showing the app keeps the person from confusing the rule with the example. The diagram isolates the variable, the capture afterward only confirms it.

## The authoring tool enters the frame with panels and menus open, at the exact point of the option being discussed
- Evidence: wwdc2014_223 (open menus for oval-shaped mask, special characters and the export dialog with PNG chosen, plus the Arrange panel with readable size and position, sheet 0010 q0089 and q0090, sheet 0012 q0102 to q0104, sheet 0015 q0130 and q0131, sheet 0023 q0201 to q0205)
- Evidence: tech-talks_111427 (Figma with an asset library and layers, Sketch with an artboard named after an iPhone model, and Icon Composer with a properties panel listing rendering mode, gradients, color and background, sheets 0001 and 0003)
- Evidence: tech-talks_802 (the Xcode attributes inspector with the attribute for pinning the view to the edges checked, next to the clock with the same content as the previous sheet, and the Asset Catalog with the attributes panel in close-up, sheet 0004 q0028, sheet 0006 q0049 to q0052)
- Evidence: meet-with-apple_270 (the tab bars page of the guidelines, the design resources page with the templates, and the SF Symbols app with categories, a grid of symbols and a weight selector, sheet 0004 q0036, sheet 0005 q0037 to q0041)
- Evidence: tech-talks_10884 (the laptop screen shows the accent color editor and the project's file browser before the scene returns to the code panel, sheet 0005, q0042 to q0045)
- What this teaches about building interfaces: showing where the option lives in the tool is part of the instruction. Without the panel open, the rule stays known but not executable.

## A plain-text card on black punctuates the presentation, one short sentence per frame and no supporting image
- Evidence: meet-with-apple_274 (the transition cards always follow the same model, a single short sentence left-aligned, white on black, no image, sheet 0004, sheet 0008 q0066 to q0071, sheet 0009)
- Evidence: tech-talks_111462 (an instruction gets a typographic card of its own, large white text centered on black, entering with a fade from low contrast to full white, sheet 0010, q0088 to q0089)
- Evidence: tech-talks_111463 (white title cards on black function as an index parallel to the speech, with hierarchy by size and weight, sheet 0003 q0022 and q0027, sheet 0006 q0048, sheet 0013 q0110, sheet 0014 q0125)
- Evidence: tech-talks_111466 (black title cards with two lines, one in gray and one in white, open the video and reappear identical at each section turn, sheet 0001 q0004, sheet 0006 q0046)
- Evidence: tech-talks_802 (isolated white text cards mark the structure between the visual blocks, including the layout title and the graphic production title, sheets 0002, 0004, 0005 and 0006)
- What this teaches about building interfaces: an entire screen dedicated to one sentence is a rhythm device. Maximum contrast and the absence of any other element create the pause, with no need for animation.

## A result is proven with a giant number and a minimal caption, preferably in a before and after format
- Evidence: meet-with-apple_208 (statistics in large serif type with two greater-than signs between the old and new value, and a small sans-serif caption, sheet 0015, q0129 to q0132)
- Evidence: meet-with-apple_254 (build time and app size in large typography in a before and after format connected by a double arrow, and search usage reduced to a single multiplier, sheet 0007, q0059 to q0061)
- Evidence: meet-with-apple_274 (statistic slides with the largest type on the sheet, percentage in saturated green, gray arrow pointing down on the left and white caption below, left-aligned on black, sheet 0007, q0056 to q0060)
- Evidence: tech-talks_803 (the conversion figure becomes a double bar chart with a numeric label above each bar and a color legend by metric, reused across three framings and then darkened to become the background for the closing sentence, sheet 0003, q0022 to q0025)
- What this teaches about building interfaces: extreme hierarchy between value and label, with the number dominating the composition, is the same principle as single-data widgets. The before and after pair carries the comparison with no need for an axis or a scale.

## Color has a fixed function within the system presented, it never decorates
- Evidence: tech-talks_10884 (the button diagram uses green for primary action, gray for secondary and dismiss, blue for toolbar, and in the renders the color follows the function, red to stop, orange to add, green to start, sheet 0006 q0046 to q0050, sheet 0007 q0059 to q0063)
- Evidence: workouts (four buttons in a two-by-two grid, each with the color and icon of its function, end in red, resume in olive yellow, new in green, segment in gray, img 1334)
- Evidence: meet-with-apple_270 (the indigo accent color is annotated across two state uses on the same screen, completed in the checkmarks and the selected tab, while lime green stays restricted to progress bars as a non-semantic color, sheet 0013 q0112 to q0117, sheet 0014 q0120 to q0123)
- Evidence: tech-talks_111463 (color codes the container family in the diagram, blue for navigation, red for content, green for layout, and the destructive item in the context menu is in red at the end of the list, sheet 0004 q0031, sheet 0009 q0073 to q0079)
- Evidence: widgets (in the Stocks widget the semantic green for a rise disappears when the tinted appearance applies a single purple to the background, text and chart, img 1296 to img 1298)
- What this teaches about building interfaces: a color must always mean the same thing within one screen and across screens. When the display mode erases the semantic color, the information needs to survive through another channel.

## The structure stays the same and only the density changes as the screen grows, with columns entering instead of type sizes increasing
- Evidence: widgets (the size progression of the Calendar widget is done by adding columns and an hour ruler, not by increasing font size, and the extra-large size extends the ruler to four days, img 1287 to img 1290)
- Evidence: meet-with-apple_257 (on iPad, a fixed sidebar with search and sections plus a grid of cards on the right, and on iPhone the same cards stacked vertically, sheet 0005, q0045)
- Evidence: tech-talks_111466 (the same list-editing screen gains additional icon columns when moving from the narrow device to the wide one, and then splits the space with the task list when folded, sheet 0011, q0097 to q0099)
- Evidence: tech-talks_111461 (the same content in a single column, in a two-column grid with one extra card and in a four-card grid, according to the SDK, sheet 0001 q0005 to q0009, sheet 0002 q0010)
- Evidence: widgets (in visionOS the same scene adapts its density to distance, from afar a cover and small text, up close an extra block with four lines of track names, img 1322 and img 1323)
- What this teaches about building interfaces: more space is more information, not bigger information. The unit that multiplies is the column, the row or the section, and the type scale stays where it is.

## Translucent controls float over the content instead of occupying their own opaque bar
- Evidence: meet-with-apple_208 (player with three translucent circular buttons over colored content, bottom bar with five translucent circular icons over a photo and pill-shaped filter chips, sheet 0002 q0017, sheet 0004 q0032 and q0033)
- Evidence: meet-with-apple_254 (small circles with a central icon marking points of interest over the product photo and a translucent side navigation bar anchored to the left without covering the photographic content, sheet 0006, q0046, q0048 and q0049)
- Evidence: widgets (the inline accessory format appears as a single line in a translucent strip, with no card, and the circular one uses a small icon over a translucent circle, img 1292 and img 1294)
- Evidence: windows (the visionOS window floats over the room with a glass background that lets the environment show through slightly, img 1330)
- What this teaches about building interfaces: when the content is the photo or the map, the chrome needs to yield optical space. Translucency plus circular or pill shape keeps the control legible without cutting a rectangle out of the content.

## Controls anchor to the outer edge and change axis without changing order
- Evidence: tech-talks_111466 (the column fixed to the right edge repeats almost identically across at least five system apps, email, calls, reminders, FaceTime and music, sheet 0003 q0019 to q0026, sheet 0004 q0028, sheet 0012 q0108)
- Evidence: tech-talks_111462 (the same app appears with the horizontal tab bar at the bottom and then with the same three icons stacked on the right edge, in the same order, with header and list unchanged, sheet 0003, q0023 and q0027)
- Evidence: meet-with-apple_254 (vertical action bar on the right edge of the full-screen content, translucent icons stacked with a numeric counter below each one, a pattern that reappears across several screens, sheets 0001, 0005 and 0006, q0004 and q0041)
- Evidence: tech-talks_111466 (in split-screen pairs each half anchors its own controls to the outer edge, and swapping position between the two apps keeps this anchoring, sheet 0005, q0037 to q0040)
- What this teaches about building interfaces: the action bar is an ordered set that can rotate from horizontal to vertical without reordering or renaming. Anchoring to the outer edge, and not the reading edge, is what keeps the thumb's reach in any pose.

## The list row always has the same anatomy, icon on the left, label in the center and control or chevron on the right
- Evidence: meet-with-apple_257 (the same left alignment across three different screens, station detail, support and settings, with a colored icon in a rounded square, label and action on the right, whether chevron, button or toggle, sheet 0005 q0041, sheet 0007 q0060)
- Evidence: meet-with-apple_208 (settings screen with a colored icon on the left and chevron on the right on each item, and a dark menu with icons to the left of the items and switches on the right, sheet 0004 q0035, sheet 0038 q0335)
- Evidence: meet-with-apple_270 (a catalog of controls in named rows, pop-up button, stepper, toggle and slider, all in the same row structure, sheet 0009, q0073)
- Evidence: writing (the setting label is a card on a black background with a short title on the left and a green switch on the right, and a supporting sentence in light gray below, img 1341)
- What this teaches about building interfaces: this row is the system's most reused component. Icon, label and terminal control form a single template that absorbs settings, actions, navigation and destructive items without inventing new layout.

## A new feature gets a badge inside the slide itself, added in a following frame without changing the content
- Evidence: tech-talks_111462 (a green circular badge added in the following frame without changing the code shown, and then overlaid on the device mockup, sheet 0014, q0119 to q0120 and q0122)
- Evidence: tech-talks_111461 (a rectangular badge in the top right corner of the slide that carries a code label, and a green circular badge with the version number on the following slide, sheet 0008, q0064, q0065, q0069 and q0070)
- Evidence: tech-talks_111463 (a green circular badge entering together with the highlighted line for region queries, and then in the layout container diagram, sheet 0007 q0060 to q0063, sheet 0009 q0079)
- What this teaches about building interfaces: the badge is a layer that comes in and out, not part of the content. This makes it possible to reuse the same slide after the new feature stops being new, just by removing the mark.

## The app's brand color invades Apple's presentation material and system components
- Evidence: meet-with-apple_255 (section slide in a purple and magenta gradient with the app icon on the right, and the stage backdrop in the same color family for much of the video, sheet 0001 q0006 to q0008, sheet 0008)
- Evidence: meet-with-apple_274 (the logo's green repeats as an accent in the statistic numbers, in the circular badges of the questions and in the closing, sheets 0007, 0010 and 0011)
- Evidence: widgets (in the gallery, the add widget button appears in the app's brand color, yellow in Notes and blue in Weather, with the identical modal card in both, img 1314 and img 1315)
- Evidence: meet-with-apple_254 (a circular design system badge with a percentage indicator and a palette of square swatches next to a screen with a three-item tab bar, sheet 0003, q0019)
- What this teaches about building interfaces: identity comes in through accent and a handful of elements, not by rewriting the component. The card, the bar and the button remain the system's own, only the highlight color changes.

## Sketch and prototype appear as a stage of the work, with the stages countable in the image
- Evidence: wwdc2014_223 (a sheet covered in dozens of pen wireframes appears as a photograph, with blue dots marking four specific sketches and a circular magnifying glass enlarging the list one, sheets 0007 to 0009, q0055 to q0073)
- Evidence: meet-with-apple_270 (real post-its in countable stages, 14 loose notes in the brainstorm, 8 after simplifying, three clusters and finally labeled with five, two and one note, without the speech giving the counts, sheet 0002, q0013 to q0018)
- Evidence: meet-with-apple_208 (the same channel list repeated across three iPhones to compare three prototyped headers, concentric, capsule and gradient, with the list anatomy constant, sheet 0021, q0183 to q0187)
- Evidence: tech-talks_111461 (a design tool on the Mac reappears twice to prototype the device's poses with the same content, open, closed and in book form, sheet 0002 q0011 to q0013, sheet 0007 q0060 and q0061)
- What this teaches about building interfaces: exploration shows itself in volume and in reduction, and the count of options is information. Prototyping the structural variant before the finish is what makes it possible to compare three headers with the same list underneath.

## Concentricity, the inner corners follow the curvature of the device
- Evidence: meet-with-apple_257 (in the slide about increased concentricity, the corners of the inner cards follow the curvature of the device's own corners, something the speech only addresses in the abstract, sheet 0007, q0058)
- Evidence: tech-talks_111461 (green fills the entire screen with the corners coinciding with the device's outline, with no app content around it, and the code pairs the concentric shape in SwiftUI with the corner configuration in UIKit, sheet 0005, q0037 to q0038)
- What this teaches about building interfaces: the corner radius of an element attached to the edge is derived from the screen's radius and the offset, not chosen by hand. Demonstrating this with a flat color, with no content, isolates the geometry.

## The closing is standardized, three concrete actions and the logo, with the same template throughout the series
- Evidence: tech-talks_111461 (the closing lists three concrete actions in white typography on black, sheet 0009, q0073)
- Evidence: tech-talks_111462 (the closing repeats the agenda pattern, with the title and three actions appearing below it, sheet 0020, q0172 to q0173)
- Evidence: tech-talks_111463 (the final list of recommendations is built item by item keeping the previous ones, with the API name differentiated by a monospaced font and highlighted background, sheet 0014 q0126, sheet 0015 q0127 and q0128)
- Evidence: tech-talks_802 (the site's resources page appears before the final black slide with the logo and the copyright notice, sheet 0007, q0055 to q0057)
- Evidence: meet-with-apple_256 (the title slide and the closing frame with the logo follow the same template as the group's other videos, sheets 0001 and 0007, q0059)
- What this teaches about building interfaces: closing is a component, not improvisation. Three actions, a reference link and the series' visual signature, always in the same place, make the material recognizable and reusable.

## HIG page openings are monochrome illustrations built over a visible grid and guide circles
- Evidence: workouts (the cover is a running figure in a red silhouette over an orange background, with rectangular and circular construction guides, including a circle centered on the torso, img 1333)
- Evidence: writing (a yellow monochrome opening, a rounded-corner clipboard crossed diagonally by a pencil, overlaid on rectangular grid lines and a central guide circle, in the same logic as the openings of other pages, img 1338)
- Evidence: windows (the opening reduces the window to a silhouette with no content, with three round buttons, translucent bubbles and measurement arrows on the edges, img 1324)
- What this teaches about building interfaces: Apple's own illustrations leave the construction grid in view, one color per theme. Reducing the subject to silhouette and guides is what makes each cover look like it belongs to the same family without repeating the drawing.

## Single-source findings

- The typographic hierarchy of the same screen is annotated twice, first by system style and then by family variant, with the title in one width, the subtitle in another and the captions in condensed (meet-with-apple_270, sheet 0011 q0095 to q0099 and sheet 0012 q0100 to q0108).
- The complete typographic scale comes as a grid table, crossing content size category in the columns with text style in the rows and the value in points in each cell, and right after, the system screen with the size slider appears overlaid on the blurred table, linking the specification to the control the person uses (tech-talks_802, sheet 0005, q0042 to q0045).
- The checklist of the eight required elements of a subscription screen appears in a column next to the real screenshot, turning the earlier one-off callouts into a closed list (tech-talks_803, sheet 0004, q0034).
- The same offer modal reappears with title and photo swapped and identical structure, hierarchy and positions, showing that it is a reusable template and not a single screen (tech-talks_803, sheet 0002, q0014 to q0015).
- The animation parameters are treated as product design controls, with values readable on screen, duration of 0.60 s, direction from bottom to top, start on click, delay of 0.50 s, and in the smart transition panel the option to match by object, word or character with eased acceleration at both ends (wwdc2014_223, sheets 0019, 0022 and 0025, q0168 to q0171 and q0190 to q0192).
- The physical scale is checked by staging the comparison, with the document zoomed out to 25 percent on the laptop next to a real iPhone held in hand, in the same scene (wwdc2014_223, sheet 0013, q0114 to q0117).
- The document size is customized per piece instead of using a standard slide, 640 by 1136 for the full screen, 640 by 2020 for the long list and 1000 by 1000 for the map (wwdc2014_223, sheets 0031 and 0033, q0277 and q0291 to q0296).
- The alignment of the fake text is done through a transparency template, with the background turning semitransparent so the reference app's text resurfaces from behind and serves as a guide for position and body before typing over it (wwdc2014_223, sheet 0011, q0097 to q0099).
- The design system is audited as a catalog in debug mode, four screens labeled by component with all variations stacked, alerts, chips, emblems and buttons, shown in light mode and then dark with only the background and surfaces inverted (meet-with-apple_274, sheet 0006, q0049 to q0054).
- The information architecture is audited through a tree diagram with rectangular nodes colored by category in hierarchical columns and the top nodes in yellow, with flow labels by task (meet-with-apple_254, sheet 0003, q0021 to q0026).
- Internal messages from the team itself become slide material, bubbles with a circular avatar, bold name, timestamp, body and reactions, stacked in cascade and listing the redesign targets (meet-with-apple_255, sheet 0005, q0038 and q0039).
- The permanence of the anchoring in a right-to-left language is proven by two calendars side by side, one in English and the other in Arabic, with the text mirroring and the icon column staying on the right edge in both (tech-talks_111462, sheet 0007, q0055).
- The ellipsis receives treatment as a reserved symbol, with an entire frame just for the three enlarged dots on black and then the same symbol at the base of a vertical panel, separated from the rest by a slight space (tech-talks_111462, sheet 0017, q0145 and q0150).
- The case of disabling the sidebar is shown by the calculator, whose compact number grid becomes a widened horizontal strip on the foldable device while keeping the same button count (tech-talks_111462, sheet 0019, q0164).
- The hinge becomes a layout divider, with floating elements moving from the center to the fold strip, the new folder dialog and the player's transport controls dropping to that axis (tech-talks_111463, sheet 0005, q0037 to q0044).
- An immersive app is the declared exception to the inset, with the green circle centered on the narrow device coming to fill the entire screen on the open device, while the other examples keep the content away from the controls (tech-talks_111466, sheet 0009, q0077 to q0078).
- The watchOS keyboard is designed with no outlines around the keys, with the delete icon inside the text field and not between the keys, and a key icon signaling a password context (tech-talks_10884, sheet 0009, q0074 to q0076).
- The extra height of a new display is isolated as a green strip at the top of the block, separate from the blue part shared with the smaller display, with the three dimensions annotated, instead of appearing just as a larger number (tech-talks_801, sheet 0002, q0010).
- Screenshots of the same app are stacked with transparency and aligned to compare sizes, the favorites list in three layers and the five-icon tab bar in four aligned layers (tech-talks_801, sheet 0002 q0017 and q0018, sheet 0003 q0020).
- The guideline pages follow a fixed template, a large component title, a definition paragraph, a side box of supported platforms with device icons and an example card on a gradient background whose color changes with the component (tech-talks_111427, sheet 0005, q0038 to q0041).
- The only data capture flow shown is the Feedback Assistant window, with a sidebar of saved items, a form of stacked labeled fields, two triage menus, a file drag zone and a solid purple submit button against a gray secondary one (tech-talks_111427, sheet 0007).
- On macOS the three window states are differentiated by three channels at the same time, button color, stacking depth and text label, and the key window of the illustration is the color panel, not the app's main window (windows, img 1327).
- On visionOS the two container styles are distinguished by shape before any content, the window as a thin, double, tilted plane in monochromatic blue with dashed outlines and the volume as a translucent cube with dashed faces and a more solid bottom face (windows, img 1328 and img 1329).
- The same message changes tone through color, temperature and composition along with the words, the severe warning in a dark blue and purple gradient with the emergency button above the dismiss button, and the achievement on a blurred colorful background with an activity ring and a concrete number (writing, img 1339 and img 1340).
- The support text of a toggle describes only what happens with the function on, without explaining the off state (writing, img 1341).
- On Apple Watch the same event card gets three treatments depending on context, a strip with a textured beige background and light pink stroke, a rectangular complication with a solid black background and red stroke, and a light card floating prominently over black in the Smart Stack (widgets, img 1303 to img 1305).
- In low light StandBy turns everything monochromatic red, including the watch face numbers, and the widget on visionOS gains a thick white frame, shadow and depth while preserving full colors (widgets, img 1299 to img 1302 and img 1317 to img 1321).
- Three screens of the same flow on Watch use the black background and the time in the upper corner as a common anchor, varying only the central content between a button grid, a stack of metrics and playback controls, with dot page indicators changing position between them (workouts, img 1334 to img 1336).
- The graphic production instruction appears written on a text card, prepare the graphic at 2x scale and save as PDF (tech-talks_802, sheet 0006).
- One isolated frame abandons the mockup and uses a spatial metaphor, controls in loose capsules floating in perspective over a checkered floor, grouped by proximity, with the red button set apart, with no equivalent on any other sheet of the video (tech-talks_111462, sheet 0009, q0074).
- The exact point where the demonstration stops being real and becomes staged is visible, the camera preview aimed at the dish switches, at the tap of the shutter, to a static photo inside the posting screen, and then a grid of eighteen nearly identical thumbnails of that same screen works as a frame-by-frame storyboard (wwdc2014_223, sheets 0036 and 0037, q0316 to q0328).
- A code agent interface integrated into the editor appears on screen without being named in the speech, with a prompt bubble asking for resizing best practices and a status line for an update in progress (tech-talks_111461, sheet 0008, q0069 to q0070).
