# ess-11 (video batch, 19 talks)

## The topic list is the only progress indicator, resolved only by weight and color within the same typographic body
- Evidence: wwdc2023_10229 (sheet 0001, q0005; sheet 0002, q0014; sheet 0005, q0039; sheet 0007, q0062; sheet 0009, q0081; current item in strong black, the rest in light gray)
- Evidence: wwdc2024_10112 (sheets 0001, 0006, 0008, 0010 and 0012; the list starts from one item and reaches five, and the section cards receive their subitems one by one)
- Evidence: wwdc2024_10140 (sheet 0001, q0004; sheet 0005, q0039 to q0041; sheet 0008, q0065 and q0066; sheet 0011, q0098; the notes explicitly record that there is no progress bar)
- Evidence: wwdc2024_10176 (sheet 0005, q0041; sheet 0006, q0048 and q0053; the same list of four subtopics changes only which item is bold)
- Evidence: wwdc2024_10096 (sheets 0002, 0006, 0007, 0008, 0011, 0013 and 0015; the column with "Setting", "Interactions" and "Audience" reappears at every block turn and the speech never comments on it)
- What this teaches about building interfaces: position in a sequence can be communicated without any component at all, only by contrast of weight and opacity within a list that never changes place. The inactive item remains legible, so the whole map stays available while the focus remains unambiguous.

## The code is taught by a translucent highlight that shifts between frames, never by rewriting the block
- Evidence: wwdc2023_10229 (light blue rectangle over the newly added line in almost every code sheet: sheet 0003, q0019 to q0020; sheet 0006, q0049 to q0050; sheet 0007, q0058 to q0059; sheet 0009, q0074 to q0075)
- Evidence: wwdc2024_10151 (sheet 0017, q0145 to q0149, in which the text does not change between frames and only the highlight migrates from token to token, from the function name to the offset, the color and the position)
- Evidence: wwdc2024_10145 (sheet 0003, q0020 to q0021, the highlight leaves matchedTransitionSource and goes to the sourceID inside the zoom modifier; it returns in sheets 0006, 0007 and 0008)
- Evidence: wwdc2024_10152 (sheets 0004 to 0011, light blue background always over the newly added excerpt, a feature the speech does not mention)
- Evidence: wwdc2024_10147 (sheet 0004, q0031 and q0032; sheet 0005, q0044 and q0045; sheet 0008, q0070 to q0072, with three callouts entering at once)
- Evidence: wwdc2024_10094 (sheets 0005, 0006 and 0011, translucent purple highlight advancing line by line, with no visible cursor)
- What this teaches about building interfaces: pointing to the change with a background layer costs less reading than redoing the block, and it dispenses with a cursor, arrow or caption. The same holds in product: when something changes inside a text or a list, marking the delta preserves the context around it.

## Right and wrong appear with the same fidelity, separated by a green check seal and a red X seal outside the artifact
- Evidence: wwdc2023_10229 (sheet 0003, q0021 to q0023, "Recommended" panels with three cards and a green check against "Not recommended" with four cards and a red X, each bad example labeled by its defect)
- Evidence: wwdc2024_10085 (sheet 0003, q0019 and q0020, failed download alert; sheet 0006, q0051 to q0054, disproportionate HUD on iPad mini with an X and the corrected version with no marking; sheet 0008, q0064 to q0070, compared framings; sheet 0017, q0146 to q0153, the same HUD goes from X to check when the buttons swap sides)
- Evidence: wwdc2024_10116 (sheet 0008, q0069 to q0072, three pairs under rule titles, among them neutral-tone thumbnails approved against thumbnails with colored borders disapproved)
- Evidence: wwdc2024_10176 (sheet 0003, q0025 and q0026, four fixed chips with an X against a single chip with an editable parameter and a check; sheet 0004, q0030, a two-by-two grid separating gesture action from task action)
- Evidence: wwdc2024_10145 (sheet 0006, q0047 to q0049, the same slide goes from X to check when the state reset comments enter the previously empty functions)
- What this teaches about building interfaces: the verdict lives in a layer separate from the example, with redundant color and shape, and the wrong example is drawn with the same care as the right one. Labeling which defect each bad variant carries teaches more than just pointing to the good one.

## The abstract diagram comes before the real product and then the two appear paired
- Evidence: wwdc2024_10112 (sheet 0002, q0011 to q0013, thin blue outline wireframe with no fill showing the cluster and app grid, and only in q0014 to q0021 do the photorealistic steering wheel renderings enter)
- Evidence: wwdc2023_10309 (sheet 0003, q0024 to q0027, diagrams with a pink dotted frame and placeholder text, and sheet 0004, q0028 to q0032, each diagram placed right next to its corresponding real widget)
- Evidence: wwdc2024_10151 (sheet 0007, q0061 to q0062, the three-by-three mesh of dots with white lines is deformed by dragging before any code appears)
- Evidence: wwdc2024_10152 (sheet 0003, q0023 to q0026, the capsule with the avatar is broken down into inactive, active and expanded states before it becomes an API)
- Evidence: wwdc2024_10116 (sheets 0004 and 0005, q0037 to q0040, named boxes connected by an arrow draw the anatomy of the components before the first Swift block)
- What this teaches about building interfaces: the diagram defines anatomy and slots, the product proves that the anatomy holds up. Pairing them side by side is the most economical way to show that an abstract template accepts real content without deforming.

## Labels stay off the screen and reach the element through a thin leader line, instead of covering the pixel under discussion
- Evidence: wwdc2024_10085 (sheet 0004, q0028 and q0029, lines connecting the bar to the "Show progress" label and the buttons to "Allow replay"; sheet 0007, q0060 to q0063, semitransparent safe area rectangles with callouts to Home indicator and Dynamic Island; the notes record that this annotation is not described in the speech)
- Evidence: wwdc2024_10147 (sheet 0008, q0066 to q0069, horizontal bracket under the tabs carrying "Customizable", then "Pinned" pointing to the magnifying glass and "Sidebar only" pointing to a code excerpt)
- Evidence: wwdc2024_10087 (sheet 0006, q0047 to q0049, technical cutaway drawing of the gallery receiving zone labels in three steps, first the central section, then five, finally the sixth)
- Evidence: wwdc2023_10257 (sheet 0011, q0094 to q0095, two outlined cubes with arrows labeled by the scale percentage and by the weight compensation, with the stroke visibly thicker in the second one)
- What this teaches about building interfaces: annotating over the real capture dispenses with the parallel diagram that ages along with the product. The label lives in the margin, connected by a thin stroke, and the screen remains whole and verifiable underneath.

## The artifact is assembled piece by piece in the order the pieces depend on one another
- Evidence: wwdc2024_10116 (sheet 0001, q0005 to q0009, first the AVFoundation box fed by the film icon, then the arrow and the RealityKit box, then AVKit above connected to four smaller blocks, in the same dependency order the speech describes)
- Evidence: wwdc2023_10229 (sheet 0004, q0028 to q0030, the tip card first gets a title, text and close button, then the star icon, then the blue action button, always next to the corresponding code; sheet 0006, q0049 to q0054, the per-event rule grows in four chained steps)
- Evidence: wwdc2024_10094 (sheet 0011, q0091 to q0093, the control detection flow starts from one box and ends branched into two smaller boxes with mini code excerpts inside)
- Evidence: wwdc2023_10257 (sheet 0011, q0097 to q0099 and sheet 0012, q0100, the constraints card grows from the title to the four complete rules)
- Evidence: wwdc2024_10087 (sheet 0002, q0016 to q0018, the blockout comes out of the primitives menu and turns into planes and a ramp forming the volume of the environment)
- What this teaches about building interfaces: the order of appearance carries information that the finished diagram loses. Assembling on screen in the real dependency order teaches the architecture along with the drawing, without needing to narrate the hierarchy.

## Only one variable changes at a time, with the component isolated on a neutral background and the fixed data at the center
- Evidence: wwdc2024_10112 (sheet 0004, q0029 to q0036, the same gauge with "60" at the center has the ring thickening in black until it covers almost the whole circle and only then switches to a petrol blue gradient; sheet 0005, q0038 to q0045, the analog alternative emerges through the transformation of the same component)
- Evidence: wwdc2024_10151 (sheets 0009 to 0011, q0079 to q0093, the transition is accumulated on the same avatar, first with no effect, then scale, then scale with opacity, finally the struct that adds blur, rotation and glow)
- Evidence: wwdc2024_10086 (sheet 0003, q0025 to q0027, the same object goes from a translucent silhouette to a wireframe with exploded parts and the final render inside the room)
- Evidence: wwdc2024_10087 (sheet 0004, q0028 and q0029, the same trunk in a dense triangular mesh and then in a decimated mesh, with the label changing along with it)
- Evidence: wwdc2023_10258 (sheet 0005, q0037 to q0045, the wifi router alternates between solid blue and a dimmed tone according to the boolean, and only then does the second effect enter chained)
- What this teaches about building interfaces: to prove that an attribute matters, freeze everything else. A neutral background, the same framing and a single delta per frame make the comparison verifiable and keep the improvement from being credited to the wrong variable.

## Code on the left and the result inside the device frame on the right, on the same screen and with a frozen layout
- Evidence: wwdc2024_10151 (sheets 0002 to 0019, rigid convention of monospaced code on the left and device on the right, always in that order)
- Evidence: wwdc2024_10152 (sheets 0004 to 0007, 0011 and 0012, the Vision Pro simulator running the video app the whole time, with the profile button physically demonstrating the effect the code just declared)
- Evidence: wwdc2024_10145 (sheet 0003, fixed two-column layout, monospaced block on the left and iPhone mockup on the right, changing only the highlight)
- Evidence: wwdc2024_10147 (sheet 0005, q0044 and q0045, when the search tab line enters the code, the magnifying glass icon appears at the top of the device's sidebar, in the same frame)
- Evidence: wwdc2023_10258 (sheets 0004 to 0011, the icon or the drawn control placed right next to the block that generates it, including the very light blue background button next to the antenna icon in sheet 0006, q0048 to q0053)
- What this teaches about building interfaces: cause and effect in the same framing eliminate the reader's short-term memory load. The layout does not move between frames, so any movement in the image is information, not compositional noise.

## Opacity and saturation carry state, both in the product and in guiding the eye
- Evidence: wwdc2024_10085 (sheet 0003, q0027 and sheet 0004, q0028 and q0029, locked chapter at reduced opacity with a wait notice, orange button for completed and green for current)
- Evidence: wwdc2024_10140 (sheet 0008, q0067 to q0070, the progressive highlight lights up a word of the title together with the corresponding block while the footer, button and other blocks lose opacity, following the screen's reading order)
- Evidence: wwdc2023_10309 (sheet 0007, q0055 and q0056, the medication widget is enlarged in a white balloon while the others stay dimmed and translucent in the background)
- Evidence: wwdc2024_10094 (sheets 0007 and 0008, q0062 and q0064, three equal rectangles in a row with the state under discussion painted solid and the rest only in a light gray outline)
- Evidence: wwdc2024_10096 (sheet 0012, q0100 to q0106, the scene loses saturation and contrast down to near white to signal exiting the portal)
- What this teaches about building interfaces: dimming the surroundings is cheaper than enlarging, moving or framing what is in focus, and the same mechanism serves for unavailability, for selection and for didactic emphasis. Since the dimmed item stays in place, the layout never jumps.

## Platform adaptation is proven by the same interface in different frames, recomposing columns instead of scaling the screen
- Evidence: wwdc2024_10085 (sheet 0001, q0004 to q0008, the same game scene on MacBook, iPad and iPhone; sheet 0006, q0051 to q0054, the HUD is repositioned and resized on iPad mini instead of being shrunk as a whole)
- Evidence: wwdc2024_10147 (sheet 0010, q0088 to q0090 and sheet 0011, q0091 to q0093, the same sidebar in a macOS window with the three colored dots, in a floating visionOS window over a 3D room and on widescreen TV as a dark list with no device frame)
- Evidence: wwdc2023_10229 (sheet 0002, q0010 to q0013, iPad and MacBook in double exposure and an Apple Watch displaying the same tip card in a compact version with an "Open" button)
- Evidence: wwdc2024_10145 (sheet 0002, q0018, iPad in a three-column grid and iPhone in a two-column grid, same card design)
- Evidence: wwdc2024_10098 (sheet 0003, q0020 and q0021, iPhone and watch side by side and then the same delivery card now below the watch face)
- What this teaches about building interfaces: responsiveness is recounting columns, repositioning controls and changing density, never proportional reduction. The component keeps its anatomy and changes arrangement.

## The same card template repeats across contexts, and the content is the only thing that changes
- Evidence: wwdc2024_10098 (sheets 0003, 0005 and 0007, translucent dark background, well-rounded corners, graphic element on the left and status text on the right, including the music variation with a circular pause button; sheet 0007, q0056, the customized coffee card keeps margins and proportions identical to the standard ones)
- Evidence: wwdc2024_10140 (sheets 0003, 0004 and 0005, notification card with dark translucent material, blurred colored glow behind it, circular icon on the left, bold title, smaller secondary text and a timestamp in the top right corner)
- Evidence: wwdc2024_10176 (sheets 0002 to 0007, a white pill with a circular colored icon on the left, a verb in black and a parameter in blue serves as notation for the entire video, varying only the content)
- Evidence: wwdc2023_10309 (sheet 0005, q0042 to q0045, the same frame with three dashed circles receives app icons, weather complications and contact photos)
- What this teaches about building interfaces: when the template does not vary, the eye stops relearning the reading at every instance and starts comparing content. Its own identity fits inside it through color and icon, without touching margin or proportion.

## The intermediate frame of the animation is shown on purpose, not just the two ends
- Evidence: wwdc2024_10116 (sheet 0002, q0015 to q0016, the single screen appears unfolding into two semitransparent rectangular screens, a state that neither the speech nor a final frame would show)
- Evidence: wwdc2024_10145 (sheet 0001, q0004 to q0005, a semitransparent card with the purple beads appears being pulled out of the grid before the editing screen exists)
- Evidence: wwdc2024_10152 (sheet 0003, q0023 to q0026, the capsule emerges already wide but empty, that is, the expanded shape before the text enters)
- Evidence: wwdc2024_10140 (sheet 0013, q0112 to q0114, the alert's blue button first appears dimmed and then solid while the background lightens, registering the entrance as animation)
- Evidence: wwdc2024_10112 (sheet 0005, q0038, a dark capsule shape serves as a transition frame between the digital gauge and the analog one)
- What this teaches about building interfaces: transition is a state with its own anatomy, which needs decisions about shape, opacity and order. Designing only the before and after hands the animation engine the part the user looks at most.

## The breadth of a system shows through a catalog in a grid of identical cells, with a short label underneath
- Evidence: wwdc2023_10258 (sheet 0002, q0010 to q0012, the seven effects in four columns by two rows, blue icons of the same stroke weight and the same size, a small centered label below, with no card and no border)
- Evidence: wwdc2024_10112 (sheet 0006, q0048, a mosaic with about twenty thumbnails of gauges and widgets; sheet 0012, q0100 and q0101, ten dark cards of the same size in two rows of five, labeled by category)
- Evidence: wwdc2023_10257 (sheet 0010, q0080 to q0084, a grid of 27 folder icons in three rows by nine columns; sheet 0012, q0101, a catalog of the same 3D box combined with different frames and badges in uniform cells)
- Evidence: wwdc2024_10176 (sheet 0002, q0013 and q0014, the single enlarged phrase gives way to ten real examples in two columns of five, all in the same style)
- Evidence: wwdc2024_10094 (sheet 0004, q0034, five gesture icons in two rows, three on top and two below, all in the same thin-line language)
- What this teaches about building interfaces: variety only stays legible when the template does not vary. Cells of equal size, the same stroke weight and a short caption below turn a large inventory into a single reading.

## A combinatory rule becomes a matrix, with color only inside the cell
- Evidence: wwdc2023_10258 (sheet 0004, q0032, a table crossing the seven effects with the four behaviors, subtle zebra striping, a small gray header and the green checkmark as the only element of color)
- Evidence: wwdc2023_10257 (sheet 0012, q0106 and sheet 0013, q0112 to q0113, a size-by-weight matrix drawn in a thin outline that becomes visibly sparser when the compatibility value changes in the footer)
- Evidence: wwdc2024_10094 (sheet 0012, q0101, a matrix crossing input types with space types, each cell with a circled green checkmark or red X and one column highlighted by a blue halo)
- What this teaches about building interfaces: when the question is "does this combination exist", the matrix answers without text. The grid stays in a thin, neutral outline, color enters only in the cell mark, and changing a filter empties the matrix in front of the reader.

## Translucency is used as a layer that never competes, with only one opaque element per composition
- Evidence: wwdc2024_10086 (sheet 0010, q0088 to q0090, a dark glass panel with a sidebar and a grid of covers fixed in space, shown from three angles with no base and no extra frame; sheet 0012, q0101 and q0102, the translucent background lets the room show through and the logo is the only opaque identity element)
- Evidence: wwdc2024_10116 (sheet 0002, playback bar in glass material floating below the screen, not attached to it)
- Evidence: wwdc2024_10096 (sheet 0016, q0141 to q0144, a semitransparent dark card with rounded corners anchored to the real floor, which grows into a menu with two stacked buttons and returns to its reduced state)
- Evidence: wwdc2023_10271 (sheet 0003, q0021 and q0026, a keyboard with round translucent glass keys and slight relief floating at an angle; sheet 0003, q0027 and sheet 0004, translucent panels with a date and location header over a dark background)
- What this teaches about building interfaces: glass is for the frame and the chrome, not for the data. Letting the environment pass through the panel and reserving opacity for identity or content keeps the hierarchy legible over any background.

## With every new block, a small green badge that is always the same marks only what is new
- Evidence: wwdc2023_10257 (sheet 0008, q0067, a "NEW" badge next to the equation diagram that introduces symbol components)
- Evidence: wwdc2024_10145 (sheet 0007, q0056, a circle with "NEW" over the half-second spring callout, with the line also highlighted in blue)
- Evidence: wwdc2024_10147 (sheet 0004, q0031 to q0035, a circular green badge on the same line as the title when the API is new, within a fixed slide anatomy)
- Evidence: wwdc2024_10152 (sheet 0002, q0014 and sheet 0011, q0095, the badge appears on the slide for the custom effects API and then on the empty effect used in the accessibility alternative, never decoratively)
- What this teaches about building interfaces: a new-item marker only works as long as it stays scarce, constant in shape and color and anchored to the exact element, not to the header of the entire screen.

## The closing swaps the screen for a photograph of a physical object, and the conclusions enter one per frame
- Evidence: wwdc2024_10116 (sheet 0009, q0073 to q0078, light blue earphones on wood with a blurred cup in the background, black text on the left and the two lines appearing one per frame; the notes record the same pattern in another video from the batch)
- Evidence: wwdc2024_10145 (sheet 0009, q0078 to q0081, a photograph of the physical bracelet on a reflective surface, a large title on the left and the list growing one line per frame)
- Evidence: wwdc2024_10152 (sheet 0012, q0103 to q0105, handcrafted objects on a wooden table on the right and three recommendations entering one by one on the left)
- Evidence: wwdc2024_10140 (sheet 0015, q0131, a still life of a mug and iPhone on a light table with the title in the top left corner)
- Evidence: wwdc2023_10229 (sheet 0010, q0089 and q0090, translucent colored cubes and the back of an iPhone on a light table next to three recommendations, the third in a lighter gray)
- Evidence: wwdc2024_10094 (sheet 0012, q0104 to q0106, a still-life photograph on wood receiving the three recommendations and then a reference line in the footer)
- What this teaches about building interfaces: changing register at the end marks the closing better than a list slide. The calm image occupies half the composition, and the text enters slowly so that the last reading is not dense.

## A thin footer separated by a line holds credit and cross-reference, with two alignment points
- Evidence: wwdc2023_10258 (sheet 0002, q0012, a footer separated by a thin horizontal line crediting another session on the left and the event on the right)
- Evidence: wwdc2024_10145 (sheet 0009, q0078 to q0081, a two-line footer table with the feature name on the left and the event year on the right, separated by a thin line)
- Evidence: wwdc2024_10152 (sheet 0001, q0007, a circular badge with the version in the top right corner and a footer citing the previous session about apps in windows)
- Evidence: wwdc2024_10151 (sheet 0012, a gray footer bar citing a previous session as a cross-reference)
- What this teaches about building interfaces: metadata does not compete with content when it lives in a strip separated by a one-pixel line, with left and right in fixed roles. It is the same mechanics as a status bar.

## Empty frames and blank screens work as punctuation between blocks
- Evidence: wwdc2024_10140 (sheet 0001, q0006 and q0008; sheet 0002, q0013 and q0015; sheet 0003, q0024 and q0026, always in pairs around a frame of the presenter, a feature that only appears in the image sequence)
- Evidence: wwdc2024_10152 (sheet 0005, q0044; sheet 0007, q0057 and q0062; sheet 0010, q0088, empty white frames, ghost images of the previous code faded out and an isolated green circle in the center)
- Evidence: wwdc2024_10151 (sheets 0012 to 0018, an iPad with a blank screen appears between code blocks as an editing pause, with no content)
- Evidence: wwdc2024_10176 (sheets 0001, 0003 and 0004, fully white or black frames at the cuts between the presenter and the graphics)
- What this teaches about building interfaces: empty space is a rhythm device, not waste. A short interval before a dense block separates topics better than a dividing line or a background color change.

## 3D object only gains size when the scene brings a human figure and a contact shadow
- Evidence: wwdc2024_10087 (sheet 0003, q0023 to q0025, a faceless gray polygonal figure with simplified proportions standing on a circle marked on the floor, serving as a scale ruler inside the scene at real size)
- Evidence: wwdc2024_10096 (sheet 0003, q0021 to q0026, a thin-line human silhouette with an elliptical shadow on the ground marking anchoring, kept identical across the three content types so that only the blue volume changes)
- Evidence: wwdc2024_10086 (sheet 0002, q0015 and q0016, the whole jet engine floats inside a room with plants and armchairs and then receives the user's hand touching the internal compartment; sheet 0009, the race car rendered at full scale with legible textures)
- What this teaches about building interfaces: scale is a relationship, never a number. A reference figure and a contact shadow say more about the size of a spatial element than any measurement written beside it.

## Sound is drawn as concentric rings or spheres coming out of a marked point in space
- Evidence: wwdc2023_10271 (sheet 0002, q0016, white concentric rings with a gradient from the center outward coming out of a point on the room floor, the notation repeated on sheet 0011, q0093, at several simultaneous points, and on sheet 0010, q0089, with speakers built into the niches)
- Evidence: wwdc2024_10086 (sheet 0008, a domestic environment drawn only in gray lines with concentric translucent blue spheres around a standing human figure)
- What this teaches about building interfaces: an invisible phenomenon needs a fixed, reusable notation. The same drawing applied in different contexts becomes vocabulary, and the environment can stay in wireframe so that the notation is the only element with visual weight.

## Single-source findings

- A numeric measurement paired with the element at real size, large number on the left and device frame on the right: "17pt Default" and "11pt Minimum" for body text on iPhone and iPad, and "44pt Default" with "28pt Minimum" for a touch target appearing in two steps over the same menu, plus "28pt Default" for Mac with a cursor resting on the button (wwdc2024_10085, sheet 0010, q0087 to q0090; sheet 0011, q0094, q0095 and q0097). The notes themselves record that the Mac values cited in the speech never actually appear on screen.
- The economy of a symbol system shown as visual arithmetic: a grid of 27 folder icons in three rows by nine columns on one side and, on the other, just three drawings labeled as the extremes and the middle of the weight scale (wwdc2023_10257, sheet 0010, q0080 to q0084).
- An explicit bridge between tool and code inside the tool itself: a two-line context menu offering to copy the current configuration to Swift or to Objective-C (wwdc2023_10257, sheet 0003, q0023).
- A tone scale as an interface component rather than a concept: four horizontal bars labeled by attribute, each with a dotted track and a rectangular blue marker whose position indicates intensity, stacked in a rounded-corner card and repeated in three different scenarios for a direct comparison of positions (wwdc2024_10140, sheet 0012, q0102 to q0104; sheet 0013, q0109 to q0111 and q0116 and q0117).
- A voice definition method documented in visual stages: a title with no note at all, two notes, about sixteen scattered around, regrouped into loose clusters and finally organized into columns with two blue header sticky notes standing out from the yellow ones, then compacted into stacks with a slight offset suggesting paper thickness (wwdc2024_10140, sheet 0006, q0049 to q0054; sheet 0007, q0055 and q0056).
- An abstract placeholder before any concrete content: five generic verb chips stacked with the parameter represented by an empty gray bar, showing the shape of the structure before a real example (wwdc2024_10176, sheet 0003, q0023).
- An emotional journey drawn as a staircase of bars with increasing and decreasing height, with the step reached in dark gray, the following ones in light gray and a facial expression emoji above each step; in a second pass the generic blocks are swapped for real product photos without changing the structure (wwdc2024_10096, sheet 0015, q0128 to q0132).
- Degree of participation quantified by a count of thumbnails: the same isometric diagram gains below it a bar of scenes linked by thin blue arrows, whose number grows from zero to four, five and six as the label moves from little to a lot of interaction, closing with two stacked thumbnails representing alternative outcomes (wwdc2024_10096, sheet 0014, q0121 to q0126).
- A debugging interface shown as a real product overlaid on the example: four sliders at the top of the iPhone screen, labeled time, amplitude, frequency and decay, each with a white circular handle over a thin gray track, with the handle of one of them changing position between two frames (wwdc2024_10151, sheet 0019, q0166 to q0168).
- Internal text hierarchy explained with nested blue boxes drawn over the blurred code, the outer layout box containing the line and the line containing a row of runs and run slices with ellipses indicating continuity; in the next frame the diagram disappears and the code becomes legible again (wwdc2024_10151, sheet 0014, q0125 and q0126).
- Editorial convention for removal in code: struck-through text over the line being replaced when the comment changes to remove content, and in the next frame the struck-through lines disappear, leaving only the final, shorter version (wwdc2024_10116, sheet 0006, q0050 and q0051).
- Spatial mixing annotated with emojis positioned over the photograph: two frogs at the left and right edges of the night photo, then three grouped on the left plus one isolated on the right, then the one on the right much larger to suggest getting closer (wwdc2023_10271, sheet 0008, q0071 to q0072; sheet 0009, q0074 to q0077).
- A blockout stage left visible in the scene itself: groups of cardboard boxes taking the place of benches and seats across several sheets, a detail the screen delivers and the speech does not mention (wwdc2024_10087, sheets 0004, 0005, 0007 and 0008).
- An attention guide as an animated glowing outline rather than a static state: the empty disc that invites loading a track gains a pulsing ring around the music icon (wwdc2024_10086, sheet 0014, q0122 and q0123).
- A variable font proven with the glyph isolated on a plain white background: the number "35" centered appears in a thin weight, then in a much heavier weight, then back to thin, with no other element on the screen (wwdc2024_10112, sheet 0003, q0025 to q0027).
- A state machine recycled to teach four different scenarios: two circles for appeared and disappeared linked by two curved arrows with the callbacks as named points along them, changing only the scenario subtitle and the position of the red dot, with a red dot and a hollow white one simultaneous in the canceled case, all paired with the real transition happening beside it (wwdc2024_10145, sheets 0004 and 0005, q0032 to q0040).
- A didactic classification attached to the example: three real cards each receive below them the label for the reason they exist, progress, action and importance, a side-by-side comparison device that the speech does not state in these terms (wwdc2024_10098, sheet 0006, q0046 to q0048).
- A rule of exclusivity staged through composition: three overlapping cards cropped at the edges with the center one always enlarged and in focus while the others stay partly out of frame (wwdc2024_10098, sheet 0006, q0051 to q0053).
- Behavior branching with a fixed color code: gray boxes for the fixed entry and exit states, green boxes for the interaction steps and thin black arrows, and the high point when the linear sequence of four boxes turns into a grid of six parallel options with a light blue outline (wwdc2024_10096, sheet 0013, q0112 to q0117).
- The colors of the diagram boxes reappear as syntax colors in the code, green for experience controller and manager, purple for the player and dark blue for the browser, creating an association between concept and implementation that the speech does not put into words (wwdc2024_10116, sheets 0005 and 0006).
- An install bar annotated with time and state: a band split into a blue section labeled playable and a gray section labeled not downloaded, which in the next frame gains the annotations of fifteen minutes and background download, and then appears overlaid on the footer of the real gameplay with the blue section advancing every frame (wwdc2024_10085, sheet 0003, q0021 to q0026).
- Letterbox studied with four different fills in consecutive frames, from the original scene to white, to a dark blue gradient and back to the scene, illustrating the options to fill with art or neutralize (wwdc2024_10085, sheet 0009, q0075 to q0078).
- The difference between physical controller and touch resolved by arrow direction: input and game boxes linked by a single arrow in the controller-with-TV case, and the same pair with a double arrow in the touch case, there with the virtual HUD of D-pad, action buttons and two joystick circles overlaid on the scene (wwdc2024_10085, sheet 0014, q0122 to q0125).
- Panel modularity shown through successive recomposition of the same space: three modules, then five smaller ones, then three again with different content, each module delimited by a thin line inside a rounded-corner container, and in a couple of frames the modules disappear, only the wallpaper remains and they come back in a thin, semi-transparent horizontal strip (wwdc2024_10112, sheet 0009, q0076 to q0081).
- Recap as its own screen of thumbnails: under the title, three real photos of the same size with straight edges in a row recapping the three moments already shown, first only the title and then the title with the photos (wwdc2024_10096, sheet 0011, q0094 to q0095).
