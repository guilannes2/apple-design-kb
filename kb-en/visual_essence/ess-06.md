# ess-06: recurring visual patterns

Batch of 15 WWDC videos (2018 and 2019). Each pattern below appears in at least two different sessions.

## The session agenda stays on screen the whole time, with one item in full white and the others in gray
- Evidence: wwdc2018_806 (sheet 0005, q0042 to q0045; reappears on sheets 0009, 0014 and 0016; the notes record that the speech does not verbalize the change)
- Evidence: wwdc2019_239 (sheet 0003, q0022 to q0025, list of eight words with no numbering or marker, resumed on sheets 0008, 0010, 0015, 0021, 0023 and 0025)
- Evidence: wwdc2019_802 (fixed list of six words reappearing on sheets 0002, 0005, 0010, 0014, 0015, 0019, 0033 and 0039)
- Evidence: wwdc2019_520 (sheet 0014, q0118 to q0120; sheet 0015, q0128 to q0132)
- Evidence: wwdc2019_803 (green index card with four outputs, sheet 0017, q0145 to q0150; the same card returns for the four inputs on sheet 0029, q0254 to q0256)
- What this teaches about building interfaces: opacity alone already solves "where am I" without a progress bar, numbering or a new component. The same element serves as index, position marker and recap.

## Lists and tables grow one item per frame and never appear already complete
- Evidence: wwdc2018_803 (sheets 0041 to 0043, q0373 to q0378, one or two bullets per frame, with the next one previewed in gray)
- Evidence: wwdc2019_211 (sheet 0018, q0158 to q0161, the list of best practices goes from one criterion to three)
- Evidence: wwdc2019_803 (sheet 0009, q0080 and q0081, the checklist starts with one item and reaches four on sheet 0010)
- Evidence: wwdc2018_804 (sheet 0004, q0028 to q0033, bullets stacked with no graphic marker, one line per frame)
- Evidence: wwdc2019_223 (sheet 0020, q0174 to q0180, the comparison table stays several frames with just one column before the second one enters)
- What this teaches about building interfaces: progressive disclosure is attention control, not decoration. No item disappears when the next one enters, so the reader keeps the accumulated context.

## The measurement appears written on top of the drawing, not only in the speech
- Evidence: wwdc2018_803 (sheet 0035, q0311 to q0313, dashed circle labeled "Hysteresis 10pt" over the photo)
- Evidence: wwdc2019_206 (magenta dimension layer over the same test layout, with the values 18, 16, 29 and 90, sheet 0007, q0061 to q0063; and container heights 24, 36 and 44 for the same 17 point text, sheet 0005, q0040 to q0043)
- Evidence: wwdc2019_211 (sheet 0019, q0165 to q0168, two safe area frames with 60 at top and bottom and 90 on the sides, against 125, 365 and 90 in the Carousel)
- What this teaches about building interfaces: the spacing decision becomes verifiable when the number is anchored to the pixel it describes. The comparison between two specifications reads at a glance because both drawings use the same scale.

## The hit target is drawn larger than the visible button
- Evidence: wwdc2018_803 (sheet 0034, q0304 to q0306, the Calculator's "9" button gets an outer dashed circle with a dot at the edge; on sheet 0035, q0307, the same around the "8")
- Evidence: wwdc2018_804 (translucent white circle marking the finger always next to the edge of the button and never in the center, sheet 0009, q0080; sheet 0010, q0082 to q0084; sheet 0012, q0103 to q0105)
- Evidence: wwdc2019_803 (sheet 0034, q0298 to q0303, blue patches covering an area larger than the keyboard's drawn key, then removed)
- What this teaches about building interfaces: the target is larger than the painted shape, and that slack only exists if it is specified. Showing the touch at the edge, not the center, is the proof that the component tolerates imprecise aim.

## Code is read with a highlight band that moves line by line between frames
- Evidence: wwdc2018_803 (sheet 0032, q0282 to q0287, gray rectangle moving from decelerationRate to the nearest corner line)
- Evidence: wwdc2019_520 (sheet 0012, q0100 to q0105, light blue band following the speech, with a gray comment always above the relevant line)
- Evidence: wwdc2019_223 (sheet 0029, q0254 to q0261, semitransparent blue rectangle highlighting the line under discussion)
- Evidence: wwdc2019_244 (sheet 0002, q0016 to q0018, the band leaves the conditional and goes to the fallback line)
- Evidence: wwdc2019_206 (sheet 0021, q0187 to q0188, the blue highlight appears only in the next frame, over the line that changed)
- What this teaches about building interfaces: when the content is dense and unchanging, the reading cursor is what changes. A translucent rectangle moves the focus without rewriting anything around it.

## Negation is a graphic mark over the text itself, with the original still legible
- Evidence: wwdc2018_802 (sheet 0010, q0085 to q0086, steps 1 and 2 of the workout get a strikethrough and the original numbering stays visible)
- Evidence: wwdc2019_802 (sheet 0008, q0065, the list of seven steps appears over the photo of the court with items 4 and 5 struck through)
- Evidence: wwdc2018_801 (sheet 0027, q0235, the term gets a stroke cutting through the word instead of being negated only in the speech)
- Evidence: wwdc2018_803 (sheet 0037, q0329, large red X over a class name while the other two stay intact above)
- What this teaches about building interfaces: deleting the item destroys the comparison. Striking it through keeps the before and the after in the same frame, and that is how you prove something was eliminated.

## Right and wrong pairs come with a label that names the defect
- Evidence: wwdc2018_803 (sheet 0015, q0127 to q0129, two circles highlighted in red with the label "Too much visual change"; sheet 0010, q0090, a screen gets "Not spatially consistent" next to it)
- Evidence: wwdc2018_811 (sheet 0004, q0032 to q0034, and sheets 0005 to 0008, items with a green circular checkmark icon for do and red with an "x" for avoid, one per frame)
- Evidence: wwdc2019_244 (sheet 0006, q0049 to q0054, the colored circles turn into a green checkmark and a red "X" in the same list layout)
- What this teaches about building interfaces: the error needs a name, not only an appearance. The label turns an aesthetic judgment into a criterion another person can repeat.

## Comparison isolates one variable at a time, everything else equal
- Evidence: wwdc2018_803 (sheet 0005, q0040, four hands touching the same circle labeled "no lag", "50ms", "100ms" and "200ms"; sheet 0015, q0131 to q0137, the same shape at 30fps and 60fps and then Normal, Motion Blur and Motion Stretch)
- Evidence: wwdc2018_804 (sheet 0007, q0062, nine button variations at once, three shapes by three treatments)
- Evidence: wwdc2019_206 (sheet 0013, q0110 to q0113, two twin screens with the same sentence and the same layout, changing only the icon, one marked as the old system and the other as the new one)
- Evidence: wwdc2019_211 (sheet 0016, q0142 to q0144 to sheet 0017, q0149 to q0153, the same Carousel composition gains a synopsis and a technical sheet on the right)
- Evidence: wwdc2018_801 (sheet 0024, q0212 to q0216, grid of twelve variations of the same letter in three rows by four columns)
- What this teaches about building interfaces: the grid of variations settles the discussion that switching between screens does not. Seeing everything together reveals the family; seeing one at a time reveals the effect.

## Before and after in the same framing, marked by a discreet label
- Evidence: wwdc2019_104 (sheet 0030, q0262 to q0264, the photo appears with the label "ORIGINAL" in the corner and in the next frame with no label and a different color)
- Evidence: wwdc2019_206 (sheet 0026, q0226 to q0227, the same popover loses two words and gains inline icons, the size of the surrounding font)
- Evidence: wwdc2019_802 (sheets 0021 and 0022, the old demo with fixed values on the bottom bar against the gesture based version with a popup and numbered ruler)
- What this teaches about building interfaces: when the framing does not change, the difference jumps out on its own. A small label in the corner replaces a whole slide of explanation.

## Diagrams are built by addition and erase what is not under discussion
- Evidence: wwdc2018_804 (sheet 0003, q0021 to q0026, cycle of six nodes with three erased to leave only one in strong white; the move repeats on sheet 0009, q0076 to q0078, and the notes record that the speech does not describe the device)
- Evidence: wwdc2019_803 (the "Interface" box with the person icon on sheet 0004, q0036, gains the "Model" layer on sheet 0006 and subdivides on sheet 0007, q0055 to q0058, up to the four items on each side on sheet 0016)
- Evidence: wwdc2019_211 (sheet 0021, q0183 to q0189, the class hierarchy lights up in three stages, first the green box, then the orange ones, then the blue ones)
- Evidence: wwdc2019_520 (sheet 0001, q0008 and q0009, system layer diagram with color by band and a camera cut closing in on the relevant section)
- Evidence: wwdc2018_803 (sheet 0007, q0057 and q0058, the same four blocks go from a row with an arrow to a two by two grid)
- What this teaches about building interfaces: a diagram only survives an hour long session if it can be reused across states. Rearranging the same blocks communicates a different relationship without introducing new vocabulary.

## Color carries a fixed meaning that the speech never states
- Evidence: wwdc2019_223 (light blue for transient events and for the haptic track, orange for continuous and for ramps, sheet 0009; the notes record that it is a convention of the material, not of the spoken text)
- Evidence: wwdc2019_520 (green reserved for the band that contains the talk's subject, blue for the already existing APIs, red for the hardware, sheets 0001 and 0002)
- Evidence: wwdc2019_206 (sheet 0012, q0104 to q0108, green for system symbol, blue for custom, purple for a regular image)
- Evidence: wwdc2019_104 (sheets 0003 and 0004, q0020 to q0034, categories in neon pink and blue outline while the rest come out in solid white, with no mention in the speech)
- Evidence: wwdc2019_239 (sheet 0004, q0034 to q0036, two identical trees distinguished only by the yellow of the Xcode group against the blue of the Finder folder)
- What this teaches about building interfaces: a palette of three to four colors with a fixed role makes the diagram explain itself across dozens of slides. Color becomes an implicit legend, and changing the meaning midway would break everything.

## The layout stays still and only the value changes between two frames
- Evidence: wwdc2018_802 (sheet 0020, q0172 to q0173, the slider changes position and color with the list below intact; sheet 0010, q0082 and q0083, the counter goes from 2/20 to 3/20)
- Evidence: wwdc2019_104 (sheet 0027, q0242 to q0243, Temperature goes from 9% to 15% and Tint from 5% to 8% in the same panel)
- Evidence: wwdc2019_802 (sheet 0006, q0047 and q0048, same header, same title and same two numbers, changing only the media in the card's footer)
- Evidence: wwdc2018_803 (sheet 0024, q0209 to q0214, STIFFNESS rises from 40 to 100 and DAMPING from 10 to 40 with the ball changing position along with it)
- Evidence: wwdc2019_211 (sheet 0010, q0088 to q0089, the neutral chevron gains a translucent blue background circle when it comes into focus)
- What this teaches about building interfaces: state is difference, and the difference is only legible when the rest does not move. This holds equally for proving a feature and for designing it.

## Transition is shown in the middle, as an intermediate state, never as a cut
- Evidence: wwdc2019_211 (sheet 0011, q0096 and q0098, two posters on screen at the same time, one leaving and one entering, with the synopses blending together; sheet 0039, q0345 to q0349, wipe with a light vertical band)
- Evidence: wwdc2018_806 (sheet 0015, q0134 and q0135, a card is pulled out of the stack and shifted to the right to be explained on its own)
- Evidence: wwdc2018_803 (sheet 0011, q0094 to q0098, a third square labeled "Hinting" appears with a glow between the initial state and the final one, and then the real card comes next, growing)
- Evidence: wwdc2018_802 (sheet 0007, q0055 to q0061, the same screenshot grows across seven frames revealing a label, note labels and a pause icon)
- Evidence: wwdc2018_801 (sheet 0016, q0136 to q0139, the active agenda item grows bold while the rest fade out until they disappear, turning into a section card)
- What this teaches about building interfaces: the middle frame is what teaches the mechanism. Designing the transition as a state, not as an effect, is what allows it to be interrupted and reversed.

## The component is pulled out of the screen and dissected on its own
- Evidence: wwdc2018_803 (sheet 0040, q0352 to q0355, the switch appears outside of any app, then just the knob floating with a shadow and without the track, isolating the elevated plane)
- Evidence: wwdc2019_802 (sheet 0034, q0299 to q0304, the native switch enlarged in both states and then small inside the real panel, with a translucent circular highlight linking the two)
- Evidence: wwdc2018_806 (sheet 0022, the notification card drawn as a flat rectangle outside any device frame, in the format of a specification piece)
- Evidence: wwdc2019_206 (sheet 0006, q0048 and q0049, five volume icons in a row with the technical name written below each one)
- What this teaches about building interfaces: taking the piece out of context exposes layer, shadow and state, which the full screen hides. The return to the real context, in the next frame, is what keeps the piece from turning into an abstraction.

## A colored outline points to the exact component inside the photo or the screenshot
- Evidence: wwdc2019_223 (sheet 0021, q0185 to q0189, a thin green circle over the home button, the crown and the selector, in three frames lined up)
- Evidence: wwdc2019_520 (sheet 0002, q0015 and q0017, a rounded green outline box over the photo of the device's interior, labeled as the haptic engine)
- Evidence: wwdc2019_211 (sheet 0017, q0152 and q0153, a hollow cyan outline box only around the new block, then only around the new column)
- Evidence: wwdc2019_244 (sheet 0005, q0041, and sheet 0006, q0051, a fixed green outline pointing to the newly arrived item on the Settings screens)
- Evidence: wwdc2019_802 (sheet 0032, q0283 to q0285, a light blue outline marking the share icon that appeared between the two map screens)
- What this teaches about building interfaces: the hollow annotation does not cover what is underneath, so it serves to direct the eye without falsifying the screen. It is the same reasoning as a temporary focus in the real UI.

## The same component appears on several devices at the same time
- Evidence: wwdc2018_806 (sheet 0021, q0188 and q0189, an annotation diagram with lines linking corresponding elements between phone and watch, in place of the screenshots; sheet 0026, q0226 to q0229, three pairs side by side with the watch more compact)
- Evidence: wwdc2019_802 (sheet 0038, q0335 to q0338, iPad and iPhone side by side displaying the same color editor in a cross, at the same layout proportion)
- Evidence: wwdc2019_520 (sheet 0002, q0013, a row of six iPhones with a real springboard under the phrase about consistency across products)
- What this teaches about building interfaces: the consistency argument needs both sizes in the same frame. Linking the equivalent elements with a line is clearer than describing the correspondence in text.

## The interface never appears on its own: it comes in a device frame or mockup
- Evidence: wwdc2019_104 (sheet 0006, q0046 to q0051, iPad, MacBook and iPhone in a real frame or mockup with a visible notch, resting on a pedestal or in perspective)
- Evidence: wwdc2019_803 (sheet 0018, q0160 and q0161, the examples enter the device frame with the native interface reproduced, never as a loose sketch)
- Evidence: wwdc2018_802 (sheet 0003, q0020, the map appears inside the device when the scene is one of use or demonstration)
- Evidence: wwdc2019_223 (sheet 0008, q0064 to q0070, two iPhones in a realistic frame with notch and watch, labeled as real world and digital world)
- What this teaches about building interfaces: the frame restores scale and reading distance, which a cropped screenshot loses. Without it, every component looks bigger than it is in the hand.

## The prototype is photographed in hand, outside the slide
- Evidence: wwdc2018_804 (sheet 0008, q0069 and q0070, a hand holding a physical iPhone against a blurred light background; sheets 0011 and 0013, the same screen enlarged on the big screen with a hand in the foreground holding the real device)
- Evidence: wwdc2019_520 (sheet 0011, q0092 to q0094, the only segment with a physical device, a red circle running across the screen as the device is tilted, with the word "Demo" overlaid)
- Evidence: wwdc2018_803 (sheet 0006, q0052 and q0053, an iPhone held in hand switching from Messages to the multitasking screen in the middle of the gesture)
- Evidence: wwdc2018_802 (sheet 0011, q0097, a photo of hands with the device displaying the back of the card that served as the initial prototype)
- What this teaches about building interfaces: gesture, tilt and thumb reach can only be demonstrated with the physical object. The screenshot proves layout; the photo in hand proves ergonomics.

## The design tool enters the scene with panels and readable values
- Evidence: wwdc2019_206 (sheet 0009, q0073 to q0077, the stroke propagates cell by cell in the Sketch template with the export panel open; sheet 0015, q0132 to q0135, the Xcode panel with Point Size, Scale and Weight and blue centering guides)
- Evidence: wwdc2019_244 (sheet 0003, q0019 to q0022, a MacBook with the environment overlay panel and the Dynamic Type control next to the simulator running the app)
- Evidence: wwdc2019_239 (sheet 0016, q0140 to q0143, the scheme's checkboxes being checked one at a time, in the same order as spoken)
- Evidence: wwdc2018_803 (sheet 0024, q0209 to q0214, a panel of three sliders for mass, stiffness and damping with scale and value next to the animated ball)
- Evidence: wwdc2019_802 (sheet 0029, q0254 to q0256, animation software with canvas, layers, timeline and keyframes, and the character's expression changing between frames)
- What this teaches about building interfaces: showing the panel with the values makes the result reproducible. Whoever watches comes away knowing which control to adjust, not just which effect to admire.

## Process artifacts come in as proof, from the sketch to the specification board
- Evidence: wwdc2019_802 (sheet 0002, q0011 to q0013, a real board with primary and secondary palettes, a component state table, a typographic specification with a full alphabet and hand-annotated pencil concept art; sheet 0037, q0325 to q0329, three fidelity levels of the same editor, from gray boxes to the final version)
- Evidence: wwdc2019_104 (sheet 0021, q0182, and sheet 0026, q0227, behind-the-scenes collages with hand sketches on paper and wireframes)
- Evidence: wwdc2018_802 (sheet 0011, q0097, a playing card photographed as the initial prototype; sheets 0014 and 0015, a form and patent drawings in thin line with numbered pieces in exploded view)
- Evidence: wwdc2018_801 (sheet 0024, q0212 to q0216, the typographic caricature technique shown in steps, from the thin-line letter to the grid of twelve variations)
- What this teaches about building interfaces: the path to the final form is an argument, not behind-the-scenes footage. Showing the earlier, ugly version validates the decision that survived.

## What cannot be seen becomes a graph next to the screen, and the text file gets an immediate graphic equivalent
- Evidence: wwdc2018_803 (sheet 0009, q0077 to q0079, the finger's vertical acceleration curve appears next to the screens, almost flat, then with a drop, then with a green peak marking the instant of the pause)
- Evidence: wwdc2019_520 (sheet 0014, q0123 to q0126, two graphs stacked on the same time axis show the continuous block losing height exactly in the region affected by the parameter)
- Evidence: wwdc2019_223 (sheet 0033, q0289 to q0297, the file is assembled key by key in JSON and right after the same values reappear as two bars for intensity and sharpness)
- What this teaches about building interfaces: feel and timing need visual representation to become a design object. Placing the raw data and the graphic form side by side teaches how to read one through the other.

## A statistic is an image: a huge number, a tiny caption, nothing more
- Evidence: wwdc2019_803 (sheet 0011, q0094 and q0096, "75%" over the word Accuracy; sheet 0012, q0102 and q0103, the same composition with the Face ID ratio)
- Evidence: wwdc2018_802 (sheet 0016, q0136 to q0140, an isolated number with a small gray caption, then a dense grid of human pictograms with a single one highlighted in white)
- Evidence: wwdc2019_244 (sheet 0003, q0023 to q0024, the statistic about motion sensitivity enters attached to the same app screen already on stage, with no separate slide)
- Evidence: wwdc2019_802 (sheet 0038, q0335 to q0338, a large number with the caption of color names next to the two screens)
- What this teaches about building interfaces: a number without graphic context does not stick; placed right against the screen it describes, it becomes a consequence. The size contrast between number and caption creates the whole hierarchy.

## A single word or phrase alone in large type on black punctuates the reasoning
- Evidence: wwdc2019_104 (absolute black background, one word at a time in white sans serif and centered, from the first title on sheet 0001 to each new award on sheets 0032, 0036 and 0045)
- Evidence: wwdc2018_802 (sheet 0001, q0007 to q0009, and sheet 0028, q0244 to q0246, the isolated word card is the dominant device and keeps only the final label of the reasoning)
- Evidence: wwdc2018_806 (sheets 0003 and 0008 to 0011, short phrases in large white type serving as a divider between blocks, almost always with no product image alongside)
- Evidence: wwdc2019_520 (sheet 0017, q0149 and q0150, two questions in large type on a black screen, with no other element)
- Evidence: wwdc2019_239 (sheet 0024, q0208 to q0211, the same short phrase grows in three sizes until it occupies the screen on its own)
- What this teaches about building interfaces: the slide holds the conclusion, the speech carries the argument. An empty screen is rhythm, and it works because the rest of the session is dense.

## A giant pictogram or emoji carries the concept in place of text
- Evidence: wwdc2018_801 (sheet 0015, q0131 to q0134, isolated emojis of a thinking face, sunglasses and piano, centered on a black background with a lot of empty space around them)
- Evidence: wwdc2019_520 (sheet 0007, q0056 to q0060, each type of event appears as a column with an icon that carries the metaphor, hammer, violin and loudspeaker)
- Evidence: wwdc2018_811 (sheet 0002, q0011 to q0013, the entire structure of the talk is a diagram of three pictorial icons with a short caption below, revisited at the close on sheet 0010)
- Evidence: wwdc2018_806 (sheet 0007, q0061 to q0063, a thinking face emoji appears between the two permission routes before the modal disappears)
- What this teaches about building interfaces: a well-chosen symbol holds a concept for an entire session and returns as an anchor in the summary. A short caption below keeps the symbol from depending on interpretation.

## Action hierarchy by color and area: primary filled, secondary neutral, destructive red and separated
- Evidence: wwdc2019_104 (sheet 0022, q0197, secondary action in neutral gray against the primary in lime yellow and with a larger area, in the same bar)
- Evidence: wwdc2018_806 (sheet 0004, q0033 to q0035, solid blue marking the recommended action among stacked buttons; sheet 0013, q0110 to q0113, the destructive button in red separated from the others in a second confirmation layer within the same card)
- Evidence: wwdc2019_211 (sheet 0009, q0078 to q0081, solid white "Play" stacked over gray "More Info", anchored in the bottom third)
- Evidence: wwdc2019_803 (sheet 0031, q0272 to q0275, full-width blue button at completion and, on the Settings screen, the destructive action in red below the switches)
- What this teaches about building interfaces: visual weight and size communicate consequence before the label is read. Separating the destructive action from the group is part of the design, not a detail.

## Selection is an outline or highlight color over an item that does not change shape
- Evidence: wwdc2019_802 (sheet 0004, q0034, three identical option cards with the active one in a yellow outline; sheet 0008, q0069, the same pattern in another app with a red outline)
- Evidence: wwdc2019_104 (sheet 0028, q0249 to q0251, the aspect ratio bar shows all the options and highlights the chosen one in orange, with the photo turning square in the following frame)
- Evidence: wwdc2019_211 (sheet 0028, q0246 to q0249, circular avatars with a selection ring on the active one; sheet 0010, q0085 and q0086, a pagination dot turns into a blue rectangular shape)
- Evidence: wwdc2019_239 (sheet 0016, q0136 to q0138, plain text list with the chosen item in blue and a selection mark, with no icon or gauge)
- What this teaches about building interfaces: keeping the shape and size of every item and changing only the marker preserves the readability of the grid. Selection needs to be recognizable from a distance, not subtle.

## Blocks of solid color come before the real interface to fix proportion
- Evidence: wwdc2019_211 (sheet 0008, q0069 to q0071, large green rectangle for the content and small rectangles below for dock and row, with no text or image inside; sheet 0032, q0281 and q0282, orange tab bar and yellow content changing vertical position)
- Evidence: wwdc2019_239 (sheet 0005, q0037 to q0042, vertical rectangles in screen format going from a disordered cloud to a regular grid and then to blocks linked by a line)
- Evidence: wwdc2019_802 (sheet 0037, q0325, low-fidelity prototype with gray rectangular boxes and text, with no color and no icon)
- Evidence: wwdc2018_803 (sheet 0030, q0266 to q0270, rectangle divided into four corner regions in a thin outline, with a yellow rectangle jumping between them)
- What this teaches about building interfaces: proportion and position are decisions that come before color, icon and text. Content-free blocks keep the discussion from slipping into finishing touches too early.

## In a game, the interface disappears: the HUD stays minimal and in the corners
- Evidence: wwdc2019_802 (sheet 0015, q0129 to q0131, only a pause icon in the top left corner throughout the whole sequence; sheets 0024 and 0025, q0215 to q0224, only the level indicator and a button in the opposite corner, with no health bar)
- Evidence: wwdc2019_104 (sheets 0041 to 0043, q0361 to q0385, circular count badges, scoreboard and level label in thin white typography in the corners, with no frame)
- Evidence: wwdc2018_801 (sheet 0020, q0176 to q0178, isometric environment with a translucent puzzle grid over the scene, with no numbers, buttons or tutorial visible)
- What this teaches about building interfaces: when the content is the experience, every persistent element needs to justify its own presence. Corners and translucency are what is left when everything else is cut.

## The HUD layout does not move while the world and the numbers change
- Evidence: wwdc2019_104 (sheet 0024, q0199 to q0216, speedometer, timer and icons keep an identical position through a night street, tunnel and wet highway, with the speed varying from frame to frame and ephemeral achievement texts appearing and disappearing without shifting anything)
- Evidence: wwdc2019_802 (sheet 0003, q0021 to q0027, race HUD with position and speedometer rising from 85 to 110 and 146, and the mode badge appearing between two frames without changing the rest)
- What this teaches about building interfaces: an ephemeral element enters its own layer and never pushes the layout. A fixed position is what makes it possible to read a number in motion.

## The least glamorous screens come in as proof, settings included
- Evidence: wwdc2018_806 (sheet 0012, q0108, and sheet 0013, q0115 to q0117, three different configuration screens sharing the same list component with a switch on the right, varying only the icon and description line)
- Evidence: wwdc2019_244 (sheet 0004, q0031 to q0032, the Settings list gains one item per frame, and the new one gets a green outline on sheet 0005, q0041)
- Evidence: wwdc2019_802 (sheet 0032, q0281 to q0283, the game's cohesion is demonstrated by going all the way to the settings screen, with native switches aligned to the right of the labels)
- Evidence: wwdc2019_803 (sheet 0031, q0274 and q0275, Settings with green switches and a destructive action in red closing the calibration flow)
- What this teaches about building interfaces: a system proves itself on the boring screen, where the standard component appears without makeup. Repeating the same list component in three contexts is the argument for coherence.

## The presenter is subordinate to the content, almost never alone on screen
- Evidence: wwdc2019_206 (during the demonstrations he is reduced to a thumbnail in the bottom left corner, and alone only at the opening, during transitions and at the close)
- Evidence: wwdc2019_520 (the slide skeleton already provides for the presenter small, centered or on the right, below or beside the text, throughout the whole talk)
- Evidence: wwdc2018_806 (sheet 0015, the code slide has the presenter semitransparent behind the block, and frames of just the presenter are restricted to standalone close-ups)
- Evidence: wwdc2019_244 (across the eight sheets none is recorded with only the presenter; even the principle slides show her small in the scene)
- Evidence: wwdc2019_211 (in a good part of the sheets he appears small beside the projection, not in its place)
- What this teaches about building interfaces: the frame of the presentation follows the same rule as the interface, content first and reduced chrome. The person enters as scale and rhythm, not as subject.

## Quotes have their own constant anatomy, and never mix with a list
- Evidence: wwdc2018_801 (sheet 0003, q0026 and q0027, and sheet 0004, q0030 to q0036, large block with name and role in small gray text right below, while the interviewer's question uses a different alignment and no attribution)
- Evidence: wwdc2018_811 (sheets 0003, 0004, 0008 and 0009, large centered phrase in quotation marks with the author's name small and gray below, always on its own screen)
- What this teaches about building interfaces: giving its own component to a type of content keeps the reader from having to decide whose voice it is. Attribution fixed in the same place supports long quotes broken across several frames.

## Semitransparent overlay stitches the screen to the physical world
- Evidence: wwdc2018_802 (sheet 0005, q0045, app screen blended into a street photo; sheet 0015, q0130 to q0132, patent drawing over photos of a luggage compartment and cockpit; sheet 0027, q0240, watch screen over a photo of a hand)
- Evidence: wwdc2019_802 (sheet 0008, q0065 and q0070, the list of steps appears over the real photograph of the court, and the orange line skeleton enters over the player's joints)
- Evidence: wwdc2019_803 (sheet 0008, q0064 to q0066, the phrase enters overlaid on the grid of photos it describes, instead of occupying its own slide)
- What this teaches about building interfaces: overlaying instead of juxtaposing keeps cause and effect in the same frame. It is the same logic as an annotation layer that can be turned on and off.

## Green marks what is new
- Evidence: wwdc2019_206 (sheet 0025, green novelty badge in the corner of the code slides, together with the blue highlight that points to the changed line)
- Evidence: wwdc2019_211 (sheet 0021, q0183 to q0189, each stage of the diagram carries a green circular badge in the corner, a device repeated in the technical slides of sheets 0029 to 0033)
- Evidence: wwdc2019_244 (sheet 0005, q0041, and sheet 0006, q0051, fixed green outline around the newly added item on the Settings screens)
- What this teaches about building interfaces: a single, constant mark for novelty saves the reader from comparing versions from memory. It needs to be peripheral enough not to compete with the content.

## Opening and closing follow a sober title card, with credit in small type
- Evidence: wwdc2019_244 (sheet 0001, q0002, dark background, white title left-aligned, small event mark in the corner and name and role in smaller type; sheet 0008, q0067, closing with the white apple centered on black and a small block of legal text)
- Evidence: wwdc2019_520 (sheet 0009, q0075 to q0077, the speaker change is marked by a credit slide with name and role in small text in the corner; sheet 0018, q0154 to q0161, the close chains together a summary, a schedule table and a final title card with the apple)
- Evidence: wwdc2019_104 (sheet 0031, q0275, and sheets 0035 and 0036, footer caption with the app icon and team name, and sheet 0052 closes with the logo in a thin outline)
- Evidence: wwdc2019_803 (sheet 0042, q0376 and q0377, references slide followed by the logo, with no effect at all)
- What this teaches about building interfaces: the credit stays in small type and a fixed position, far from the content. The session's frame is always the same, which makes each opening recognizable without being read.

## Giant typography cut off by the edge serves as background behind the person
- Evidence: wwdc2018_801 (sheet 0006, q0047 and q0049, huge light gray letters cut off at the edge of the screen behind a close-up of the presenter, sometimes with loose words, sometimes with the name of the interviewee who enters next; repeated in sheets 0018 and 0019)
- Evidence: wwdc2019_520 (sheet 0009, q0075 to q0077, the transition is captured in an intermediate frame with the enlarged text fragment behind the new presenter)
- What this teaches about building interfaces: text enlarged beyond the frame works as background texture and gives depth without illustration. Partial legibility is acceptable when the element's role is ambient, not informational.

## Abstract parameter becomes a ruler with examples the audience has already touched
- Evidence: wwdc2019_223 (sheet 0025, q0217 to q0225, the same linear axis starts empty, gains a label at both poles and receives two markers anchored to real examples, the flashlight button near the end and the app switcher closer to the center)
- Evidence: wwdc2019_520 (sheet 0007, q0061 to q0063, and sheet 0008, q0064 to q0067, the same ruler from 0.0 to 1.0 fills in stages, first the poles, then a marker with the flashlight button, then a second with a framed thumbnail of the app switcher)
- What this teaches about building interfaces: a numeric value with no reference does not guide choice. Anchoring the ends and one or two known points turns the scale into a possible judgment.

## Execution flow drawn as a live diagram, with a numbered list on one side and objects changing state on the other
- Evidence: wwdc2019_223 (sheets 0027 and 0028, q0235 to q0244, the list grows on the left while blocks colored by object type change their label in parentheses, with completion marks, up to the seventh step in q0244)
- Evidence: wwdc2019_520 (sheet 0010, q0082 to q0089, the same structure with fixed color per type, arrows linking the objects and a green arrow pointing from the active step to the corresponding object)
- What this teaches about building interfaces: sequence and state are two different pieces of information and fit in the same frame. The list gives the order, the boxes give the consequence, and the arrow ties the two together.

## Single-source findings

- Reparameterization of the same control: the panel swaps mass, stiffness and damping for two sliders, damping as a percentage and response in seconds, and the value-over-time graph changes shape with each pair, rising without overshoot in one setting and creating a peak and oscillation in another (wwdc2018_803, sheet 0025, q0217 to q0220, closing with a dense bundle of overlapping curves in q0223 and q0224).
- Green point of light marking the exact contact, with a gradient trail in the direction of movement and the list of inferred data next to it, position, velocity, speed and force (wwdc2018_803, sheet 0012, q0101 to q0103); the same point stays lit in the corner of the button while the screen changes content, indicating continuous pressure (sheet 0013, q0110 to q0112).
- Anatomy of the scrollable picker: three columns of values with the center row larger and lighter, and the adjacent ones losing contrast as they move away, with opacity and sharpness adjustment suggesting settling after scrolling (wwdc2018_803, sheet 0028, q0244 to q0246).
- In rich notification cards, the buttons are always stacked at full width and never side by side, with the card gaining a circular close control in the corner and the media at full width above the text (wwdc2018_806, sheet 0017, q0148 to q0152).
- The permission request extends the notification card itself downward and places the two buttons inside it, reusing the modal's pair of actions without opening any modal (wwdc2018_806, sheet 0006, q0053 and q0054).
- On the watch, each type of interaction gets its own control inside the notification, over a full-screen black background: a row of five stars plus a payment button, two round minus and plus buttons with the value changing between frames, a circular dial with a number inside a ring, and a list with round checkboxes (wwdc2018_806, sheets 0022 and 0023, q0194 to q0206).
- An optical scan code occupies the entire dial in white, with no other interface element on the screen (wwdc2018_806, sheet 0024, q0214 and q0215).
- The symbol scales arrive as a pre-drawn matrix, a two-dimensional grid with weights in the columns and scales in the rows, the same one in the design app and in the development environment, instead of real-time calculation (wwdc2019_206, sheet 0008, q0068 to q0070, and sheet 0009, q0078 and q0079).
- The baseline is drawn as a visible measurement, with offsets annotated in orange of minus 3.5 and plus 4.5 for two different icons, and an outline rectangle marking the icon's bounds (wwdc2019_206, sheet 0019, q0165 to q0169).
- Horizontal alignment demonstrated with a dotted yellow guide crossing the column of avatars in a comment list, followed by a bidirectional arrow measuring the distance to the text (wwdc2019_206, sheet 0020, q0175 to q0177).
- The code demo is recorded live and not post-produced: autocomplete popups appear over the text being typed, yellow warnings in the margin while the structure is incomplete, and a red error after the cases are filled in (wwdc2019_211, sheet 0022, q0195 to q0198, and sheet 0024, q0212 to q0216).
- Recap as a word cloud hierarchized by font size, with all the section's principles on a single screen (wwdc2019_211, sheet 0012, q0104).
- Two visual themes coexist in the same talk without conflict: the prototype appears in a light theme with a dark gray header over a light background, while the real home screen and the carousel always appear dark (wwdc2019_211, sheet 0014, q0120 to q0123, and sheet 0020, q0177).
- Four color wheels of twelve slices lined up, labeled as normal vision and three types of color blindness, each of the last three with a reference color circle below, showing distinct hues collapsing into similar tones (wwdc2019_244, sheet 0005, q0044).
- Typographic scale diagram in two columns linked by an arrow, the left one with all eleven style names in the same small font size and the right one with each name rendered at its real size and weight (wwdc2019_244, sheet 0002, q0013).
- The three-phase model gains its own graphic form, three orange-ish disks seen in profile, presented together with no emphasis on the first appearance and then with the current phase's disk highlighted in each block (wwdc2018_804, sheet 0005, q0045; sheet 0008, q0071; sheet 0011, q0097).
- Sound comparison made with a column of circles labeled A, B and C next to an app screen that does not change, one circle lit at a time, and then a green circle with a checkmark confirming the choice (wwdc2018_804, sheets 0018 and 0019, q0156 to q0159).
- Pressed state made only by darkening the same color, with no change in shape, border or shadow, with the touch point at the edges of the button (wwdc2018_804, sheet 0010, q0087 to q0090).
- Two actions stacked on the same screen, the top one dimmed and the bottom one vivid, showing the available action and the active action at the same time instead of cutting between screens (wwdc2018_804, sheets 0013, 0014 and 0018, q0126, q0156 and q0159).
- Circular progress ring with the number of repetitions inside, the exercise name in uppercase below, three small icons in a row for previous, current and next, and a linear bar at the top (wwdc2018_802, sheet 0010, q0082 and q0083).
- Three-column grid of circular buttons with a white pictogram on a dark background, a label below each icon and confirmation in the top right corner (wwdc2018_802, sheet 0009, q0079).
- Dictionary-definition slide to anchor a term, with the word in bold, phonetic transcription in italics, part of speech and numbered meanings aligned to the left (wwdc2018_802, sheet 0016, q0141, and sheet 0009, q0077).
- The same weather app layout repeats identically between cities, varying only the background color and the pixel-art scene at the bottom according to weather and time (wwdc2018_802, sheet 0018, q0155 and q0158 to q0160).
- Color becomes the slide's own content: each answer about favorite color occupies the entire screen in that color, with a fixed label in the same size and position, followed by a sample card with a white frame and caption and by a grid of system samples in two rows with a small label under each block (wwdc2018_801, sheets 0034 and 0035, q0299 to q0313).
- Illustrated character in place of a user photo, running through the entire talk and changing roles, including as a row of three named personas with a two-line caption (wwdc2018_811, sheet 0006, q0053, and sheets 0005, 0008 and 0010).
- Narrative structure drawn as a minimalist line diagram, a thin white stroke on a black background, with no color or texture, evolving from a single step into a sequence of steps rising and falling, each with its own label (wwdc2018_811, sheet 0008, q0071 and q0072; the notes record that the speech does not describe the feature).
- Version history represented as an abstract graph, a central blue line with yellow and green branches of connected circles, with not a single text label (wwdc2019_239, sheet 0009, q0078 and q0079).
- The section label enters overlaid on the tool capture itself, in the top left corner, doing away with a separate transition slide (wwdc2019_239, sheet 0018, q0154 to q0155, and sheet 0022, q0193 to q0194).
- The ceremony's progress indicator is built on the stage grid: a row of eight rounded-corner rectangles with a dashed outline, initially empty, that fills in with the icon of each winning app, from five to nine icons over the course of the event (wwdc2019_104, sheet 0007, q0062; sheets 0032, 0036, 0040, 0045 and 0050).
- Spatial data drawn instead of tabulated: a simplified half court with red dots for miss and orange for hit marking the position of each attempt, with the video embedded at the top of the same screen and the statistic next to it (wwdc2019_104, sheet 0047, q0418 to q0419).
- Explicit feedback evolves by reusing the same component: two round buttons appear over the dimmed screen, become items inside the native action menu, and are finally swapped, in the same menu, for options that name the consequence (wwdc2019_803, sheets 0035 and 0036, q0313 to q0324).
- The error is presented as a pair of portraits in a white badge-style frame, first one alone and then next to a similar-looking man, and on the following sheet the same frames darken to receive the highlighted phrase (wwdc2019_803, sheets 0012 and 0013, q0106 to q0110).
- The gesture teaching is drawn as a layer over the game scene itself, with the explanation phrase and the action label accompanied by the circular icon of the corresponding button, instead of a separate panel (wwdc2019_802, sheet 0003, q0027).
- Fixed geometric vocabulary for a sense that cannot be seen: straight bar, rounded drop, pointed triangle and wide block appear loose at first and are then formalized inside a Cartesian plane with both axes labeled from 0.0 to 1.0 (wwdc2019_223, sheets 0003, 0004 and 0013, q0027 to q0031 and q0115 and q0116).
- Contrast communicated by density of elements, not by shape: the slide on one side has few bars in simple pairs and the one on the other accumulates far more bars in the same track (wwdc2019_223, sheet 0016, q0137 to q0141).
- Real photography of the mechanism as a causal argument: gold and silver gears with rubies, in successive camera close-ups, up to the three-dimensional close-up of the serrated crown with a red ring (wwdc2019_223, sheet 0010, q0086 to q0090).
- Layer of the specification that exists only in the diagram: the format's hierarchical tree, in boxes with a stacked-card effect, exposes elements that had not been built in the code of the previous sheets (wwdc2019_223, sheet 0034, q0299 and q0300).
