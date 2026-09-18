# Visual essence of batch ess-10

Basis: 17 visual syntheses read in full, all from video (WWDC 2022 and 2023).

## A fixed list of topics serves as the navigation bar for the entire video, with the active item in dark bold and the others in light gray, without changing size or position
- Evidence: wwdc2022_110340 (sheet 0003, q0022 and q0023; sheet 0007; sheet 0010, q0085; sheet 0019, q0165 to q0167)
- Evidence: wwdc2023_10072 (sheets 0006, 0009, 0014 and 0019, q0050, q0075, q0124, q0167)
- Evidence: wwdc2023_10138 (sheet 0001, q0007 to q0009; sheet 0004, q0035; sheet 0009, q0078; sheet 0012, q0102)
- Evidence: wwdc2023_10115 (sheet 0002, q0013 and q0014; sheet 0005, q0041; sheet 0008, q0064; sheet 0010, q0082)
- Evidence: wwdc2023_10078 (sheet 0001, q0005 to q0007, translucent overlaid list in the right corner of the presenter's shot)
- Evidence: wwdc2022_110441 (sheet 0003, q0019 to q0021; sheet 0010, q0090; sheet 0012, q0105, the same list in Arabic on the right side)
- What this teaches about building interfaces: selection state can be communicated by weight and tone alone, with no box, background, marker or offset, and the element stays at the same pixel between sections so it costs the reader no reorientation. A persistent summary is cheaper than a repeated index screen.

## Slides and components are built by accumulation, items entering one by one while the previous ones remain visible, instead of switching screens
- Evidence: wwdc2022_110340 (sheet 0002, q0014 to q0017, icon grid assembled in two stages, three first and three more after; sheet 0014, q0118 and q0119, two icons and then four more)
- Evidence: wwdc2022_110381 (sheet 0009, q0074 to q0078, recap with a green checkmark icon entering item by item)
- Evidence: wwdc2023_10073 (sheet 0010, q0082 and q0083, from three to five recommendations; sheet 0011, q0094 to q0096, from two to four items; sheet 0014, q0124 to q0126, from the title alone to four items)
- Evidence: wwdc2023_10078 (sheet 0010, q0086 to q0088, title with no items, then three, then a fourth)
- Evidence: wwdc2023_10193 (sheet 0004, q0031 to q0033, first line alone and the second adding on in the next frame)
- Evidence: wwdc2022_103 (sheets 0039 and 0040, q0346 to q0356, each award category gets one column at a time within the same template)
- What this teaches about building interfaces: revealing content by addition inside a stable container keeps the reader from rebuilding context at every step, and it serves onboarding as well as long forms and result summaries.

## The pairing of right and wrong is the dominant didactic convention, with a checkmark badge and an X badge always positioned in the same place under each variation
- Evidence: wwdc2023_10076 (sheets 0004, 0007, 0008, 0011 and 0015, applied to book cards, FaceTime notifications, settings lists and toolbars)
- Evidence: wwdc2023_10073 (sheet 0005, q0038 to q0041, a rounded pill approved against a rectangle with near-right-angle corners, and a centered heart approved against two overlapping hearts)
- Evidence: wwdc2023_10197 (sheet 0012, q0103 and q0104, two identical bears labeled with and without erase layers, the second getting an X in the next frame)
- Evidence: wwdc2023_10194 (sheet 0002, q0017 and q0018; sheet 0004, q0030; sheet 0006, q0047, here with X and check in neutral gray, not colored)
- Evidence: wwdc2023_10193 (sheet 0005, q0039 and q0040, red X overlaid on the version whose title repeats the app's name)
- Evidence: wwdc2023_10078 (sheet 0009, q0078 to q0080, comparisons split down the middle by a vertical line with fixed badges at the top of each half)
- What this teaches about building interfaces: the rule reads clearly when the two versions differ in only one attribute and stay in the same frame, which holds for documenting a design system as well as for teaching in a talk.

## Measurements in points are annotated in yellow over the actual component, breaking down the target area into visible artwork plus empty space
- Evidence: wwdc2023_10076 (sheet 0009, q0077 to q0081, a 60pt rectangle around the heart, then 8pt on the four inner margins, then spacing marks between buttons and 16pt written on the music grid)
- Evidence: wwdc2023_10073 (sheet 0005, q0043 and q0044, 8pt on each side of the glyph and 44pt marking the width of the target, with the text slide coming only afterward)
- Evidence: wwdc2023_10076 (sheet 0010, q0082 to q0086, 28pt on the disclosure and a dashed rectangle encompassing image plus text as a single target; sheet 0011, q0094, 4pt between list items; sheet 0015, q0134, 20pt of ornament overlap at the edge)
- Evidence: wwdc2022_110381 (sheet 0002, q0016 and q0017, stacked blocks marked 96, 70 and 45 pts; sheet 0006, q0049 and q0050, bodies from 42pt to 20pt to match the final width)
- What this teaches about building interfaces: the tappable area is not the icon's artwork, and showing the padding as an explicit rectangle keeps it from being treated as leftover space. Annotating the measurement on the actual component avoids a specification nobody can apply.

## The reference grid appears drawn over the finished interface, exposing the mesh that the text only describes in words
- Evidence: wwdc2023_10026 (sheet 0004, q0028, lines overlaid on the Activity rings watch face)
- Evidence: wwdc2023_10138 (sheet 0009, q0081; sheet 0010, q0082 and q0090; sheet 0011, q0091, the cross mesh and concentric circles over the watch face and then isolated as green lines with no content at all)
- Evidence: wwdc2023_10194 (sheet 0002, q0016, green vertical guides at the edges of the lock screen's card stack, proving that Live Activities and notifications align on the same margin)
- What this teaches about building interfaces: coherence between components from different layouts comes from sharing the same margin, and drawing that margin once over the product is worth more than repeating the rule in prose.

## The label connected by a leader line to the exact point on the screen names a color, property, API or component part without altering the image
- Evidence: wwdc2023_10026 (sheet 0005, q0039, "System Green" pointing to the primary button of an alert in dark mode)
- Evidence: wwdc2023_10138 (sheet 0011, q0095, ".topBarTrailing" linked to the icon in the top right corner; sheet 0013, q0117, and sheet 0014, q0118, the background modifier and the secondary style modifier pointing to distinct targets on the same screen)
- Evidence: wwdc2022_110342 (sheet 0009, q0076 to q0078, the Activity capture stays still while thin lines point first to the rings and then to the supporting charts)
- Evidence: wwdc2022_110381 (sheet 0007, q0058, the title label linked to the Memory card's text; sheet 0008, q0064 to q0066, marking which part of the headline uses each width)
- Evidence: wwdc2023_10078 (sheet 0009, q0074 to q0077, the vanishing point label enters with an arrow, then leaves and the point remains, then the point is shifted off center)
- What this teaches about building interfaces: annotation makes it possible to teach the anatomy without cutting the component out of its context, and it keeps the same image as a reference while the subject shifts layers.

## Color comes in last, after the structure already holds up in black and white or in a single color
- Evidence: wwdc2022_110340 (sheet 0017, q0145 and q0146, both series appear only in white, distinguishable only by circle and square, and only then does the colored legend appear; sheet 0004, the study charts are white on black while the concept icons are blue)
- Evidence: wwdc2022_110342 (sheets 0009 and 0010, q0079 to q0085, two identical platters that first diverge in period and scale, then in color, then in bar style)
- Evidence: wwdc2023_10197 (sheet 0002, q0010 to q0016, the symbol grid starts out black on light gray, then a single symbol lights up blue, then more light up)
- What this teaches about building interfaces: if the layout only works with color, it does not work. Separating shape from color in the construction itself makes coding redundancy visible before it becomes an accessibility problem.

## The palette is validated by repeating the same composition over different backgrounds and modes, in a grid or in sequence
- Evidence: wwdc2022_110340 (sheet 0018, q0160 to q0162, the same chart duplicated in dark mode and light mode thumbnails with the color swatches alongside; sheet 0019, a grid of four crossing both modes with and without increased contrast)
- Evidence: wwdc2023_10076 (sheets 0006 and 0007, q0050 to q0059, the translucent panel stays fixed in the same position while the background video switches between ocean, elephant, aquatic creature, green field, dinosaurs and foliage)
- Evidence: wwdc2022_110381 (sheet 0008, q0064 to q0066, the same headline repeated over light beige, white and dark gray keeping the annotations)
- Evidence: wwdc2023_10075 (sheet 0010, q0086 to q0090, the per-person volume control repeated over four backgrounds; sheet 0013, q0112 to q0114, the identical invitation card over three blurred backgrounds)
- What this teaches about building interfaces: translucent material and contrast color need to be tested against the worst possible background, not against the background chosen for the mockup, and the grid crossing mode and contrast is the minimum test before locking in the palette.

## The effect is proven by the difference between two frames of the same scene, with a single attribute changing and everything else frozen
- Evidence: wwdc2023_10026 (sheet 0007, q0059 to q0062, World Clock switches location while preserving the layout and map, changing only the time and the indicator's position)
- Evidence: wwdc2023_10194 (sheet 0004, q0028 and q0029, the same flight card with the same text and the same layout in blue and then in yellow; sheet 0008, q0067 and q0068, the tide card going from grayish blue to dark red in night mode without moving anything)
- Evidence: wwdc2022_103 (sheet 0023, q0203 to q0205, the mountain landscape switches from magenta and purple to petrol blue and green keeping the composition identical)
- Evidence: wwdc2023_10138 (sheet 0011, q0097 and q0098, with the control size modifier highlighted in the code, the pause button appears larger than in the previous frame)
- What this teaches about building interfaces: variation in theme, brand or state should fit into a token swap over the same structure, and that is the cheapest way to check whether the structure truly holds up under variation.

## The side-by-side comparison in identical frames is the standard device for proving parity across languages, platforms and screen sizes
- Evidence: wwdc2022_110441 (sheet 0004, q0028 to q0036, iPhone pairs with English on the left and Arabic on the right, each pair labeled by the subject under test, image, temperature scale, day order, calendar and chart over time)
- Evidence: wwdc2022_110381 (sheet 0010, q0082 to q0089, the same system screen in Spanish, English and Chinese with identical component structure and only the text changing)
- Evidence: wwdc2023_10138 (sheet 0005, q0040 to q0043, the same weather app on iPad landscape, then compared simultaneously across three sizes down to the watch)
- Evidence: wwdc2023_10076 (sheet 0005, q0040 to q0042, columns labeled by platform with body and title samples, the spatial device's line getting visibly thicker)
- What this teaches about building interfaces: the internationalization and responsiveness test is visual and comparative, not descriptive, and the identical frame on both sides is what makes the difference attributable to the content.

## Human anatomy and posture enter as thin-line diagrams, defining the comfortable reach before any layout decision
- Evidence: wwdc2023_10072 (sheet 0007, q0060 to q0063, reclined person with feet supported and person sitting upright, dotted circle around the head and a vertical board beside it representing the content)
- Evidence: wwdc2023_10073 (sheet 0003, q0023 to q0025, the rendered room gains a ring of light around the sofa and then turns into a diagram of concentric rings marked 30, 60 and 90 degrees)
- Evidence: wwdc2023_10078 (sheet 0002, q0010 to q0012, head profile with brain, then two frontal circles with dotted lines converging on a target; sheet 0007, q0057 to q0060, the same profile receiving the cochlea icon)
- Evidence: wwdc2023_10075 (sheets 0003 and 0004, q0026 to q0029, black disk on the floor, white faceless silhouettes and green shapes representing content, with contact shadow)
- What this teaches about building interfaces: the limit of physical comfort comes before the grid, and an abstract, reusable graphic vocabulary, silhouette, disk, plane, allows positioning to be discussed without the product's appearance getting in the way.

## The chromatic vocabulary of the diagrams is fixed within each piece, with one color reserved only for annotation and others for semantic roles
- Evidence: wwdc2023_10075 (sheet 0012, q0100 to q0102, green with a shared badge for the common context and navy blue with a not-shared badge for the personal window, ending in the composition with a green screen in the background and three blue panels)
- Evidence: wwdc2023_10073 (sheet 0006, q0050 and q0051, and sheet 0007, q0055 and q0056, yellow appears only as an outline, diagonal line and divider of the scale comparison)
- Evidence: wwdc2023_10076 (sheet 0009 to sheet 0015, yellow is used exclusively for measurement and spacing, never as the component's color)
- Evidence: wwdc2023_10078 (sheet 0002 and sheet 0007, green marks line of sight and comfort cones, and sheet 0006, q0050, adds a third signal, orange alert, for the intermediate case)
- What this teaches about building interfaces: reserving one color for the meta level, that is, for annotation and measurement, keeps the reader from confusing instruction with product, and the same discipline applies to debug overlays inside the app.

## Real screens from system apps enter as a reference repertoire before the principle is applied to the example under construction
- Evidence: wwdc2022_110340 (sheets 0001, 0009, 0013, 0015 and 0016, translucent card with hourly timeline, trend card with a highlight point, metric cards, concentric rings and route card with elevation profile, each preserving its own language)
- Evidence: wwdc2022_110342 (sheet 0001, q0007 to q0009, dark platters with rounded corners with a small title, large number and smaller caption; sheet 0006, q0052 and q0053, watch face complications, mini lines beside assets and a tiny chart inside a card)
- Evidence: wwdc2023_10138 (sheet 0010, q0083 to q0089, the three fundamental layouts labeled over real apps and then pairs of watches swapping content through a translucent transition)
- What this teaches about building interfaces: before proposing a pattern, it is worth assembling the wall of examples already existing in the system, because it fixes the acceptable range of variation and avoids reinventing a component that already has a canonical form.

## Interaction is filmed with a real hand and device, showing the finger entering, pressing and leaving across successive frames
- Evidence: wwdc2022_110340 (sheet 0006, q0046 to q0051, and sheet 0012, q0101 to q0103, the hand holds the iPhone, the finger approaches, presses the bar and is withdrawn, with a dark badge appearing under the touch point)
- Evidence: wwdc2023_10073 (sheet 0014, q0119 to q0121, close-up of the virtual keyboard with a brighter glow on the keys neighboring the contact point, a glow that moves along with the finger)
- Evidence: wwdc2023_10115 (sheet 0006, q0049 and q0050, the finger turns the Digital Crown and the map changes city)
- Evidence: wwdc2023_10138 (sheet 0015, q0127, the same World Clock screen first in a product still and then in a real wrist photo)
- What this teaches about building interfaces: touch feedback needs to be designed for the instant the finger covers the target, and only filming with a real hand reveals how much of the component stays hidden at the moment of contact.

## Hand sketch and final product appear in the same frame, with arrows labeling each area of the screen before it exists
- Evidence: wwdc2022_103 (sheet 0014, q0123 and q0124, left half with a hand-drawn wireframe and arrows naming sender, captions, exit and participants, right half with the real capture of the iPhone in use)
- Evidence: wwdc2022_113 (sheet 0013, q0115 and q0116, the handwritten wireframe and, in the following frame, that same wireframe placed beside the already implemented mockup; sheet 0002, q0013, hand-drawn rectangles on paper covering the interviewee's face)
- Evidence: wwdc2022_110441 (sheet 0003, q0022 to q0025, three screens with real content, then reduced to gray blocks with no content, then the already mirrored wireframe with the Arabic content put back)
- What this teaches about building interfaces: reducing the screen to gray blocks is the step that exposes the structure independently of the content, and keeping the draft beside the result documents which decision came from intent and which came from implementation.

## Components are shown first empty and then filled, with the container defined before the data
- Evidence: wwdc2022_110342 (sheet 0011, q0091 to q0096, the horizontal bar appears first with no value and then with name and length, and the day columns emerge only with dotted marking before receiving gray and yellow bars)
- Evidence: wwdc2023_10078 (sheet 0010, q0086 to q0088, the list title appears with no item before any row enters)
- Evidence: wwdc2023_10194 (sheet 0009, q0074 to q0080, the Dynamic Island pill starts empty and moves through incoming call, near-square shape, elongated bar with waveform and back to empty)
- Evidence: wwdc2023_10138 (sheet 0012, q0107 and q0108, three watches with only solid gradient backgrounds, no icon or text, and in the following frame two of them receive content)
- What this teaches about building interfaces: the empty state is part of the component and not an exception, and designing the container before the content is what guarantees the screen does not collapse when the data is missing.

## Typography is presented as a table or matrix of labeled samples, with the same text repeated across all variations
- Evidence: wwdc2022_110381 (sheet 0004, q0028 to q0033, matrix with width rows, Compressed to Expanded, and weight columns, Ultralight to Black, lighting up one row at a time; sheet 0005, q0041 to q0044, the same pangram in four rows, one per width; sheet 0007, q0061, three by three grid with nine combinations of the same title)
- Evidence: wwdc2022_110441 (sheet 0006, q0052 and q0053, double-column table with the Latin family from thinnest to heaviest on the left and the Arabic family at the same weights on the right; sheet 0007, q0058 to q0061, columns labeled by optical size with the same word at different scales)
- Evidence: wwdc2023_10138 (sheet 0013, q0112 to q0114, pills labeled primary, secondary and tertiary in decreasing opacity, beside the same blocks of text in decreasing sizes)
- What this teaches about building interfaces: the type scale can only be evaluated with the same content in every cell, because the difference that matters is how much space each variation consumes to say the same thing.

## The code sits beside the result and the highlighted snippet changes in the same frame the screen changes
- Evidence: wwdc2023_10138 (sheet 0006, q0053; sheet 0007, q0060 to q0062; sheet 0008, q0066 to q0069, the blue highlight moves from a source condition to its inverse and the Activity ring switches position along with it)
- Evidence: wwdc2023_10115 (sheet 0003, q0026 and q0027, file tree on the left, Swift editor in the center and canvas with an iPhone frame on the right; sheet 0004, q0028, the blue text on the canvas corresponds to the font, weight and color modifiers in the code)
- What this teaches about building interfaces: when the demonstration ties a line of code and a pixel to the same instant, the property stops being abstract, and that is the argument for design tools that render live instead of exporting static screens.

## Authoring tools are filmed in use, with panels, layers and sliders visible, revealing the density of control behind the simple result
- Evidence: wwdc2023_10197 (sheet 0011, q0095 to q0099, the SF Symbols app in three columns, categories on the left, large preview in the center, rendering, color, background and layers panel on the right, with the layer list gaining a row and the mode moving from monochrome to multicolor)
- Evidence: wwdc2023_10115 (sheet 0012, q0100 to q0103, a parameterized tool on an iPad with numeric sliders for size, gap, thickness, opacity and shadow, thumbnail grid on the right and a color picker opening over the panel)
- Evidence: wwdc2022_103 (sheet 0023, q0202 to q0205, bar of named gradients, color wheel, modal cropping panel and per-channel sliders; sheet 0025, q0221 to q0224, stacked tools on the left and named layer cards on the right)
- Evidence: wwdc2022_113 (sheet 0021, q0185 to q0187, cropping window, color wheel and per-channel rulers, and a second tool in which only the background image changes between two frames while the gradients panel stays)
- What this teaches about building interfaces: a persistent side panel with the result in the center is the recurring arrangement for creative tools, and showing the real panel is what makes clear how many parameters are implicit in a decision presented as simple.

## Monochrome linear icons in a regular grid serve as a vocabulary for abstract concepts, and later reappear as a marker for the topic in focus
- Evidence: wwdc2022_110340 (sheet 0002, q0014 to q0017, grid of three columns by two rows of squares with linear icons and a small caption below, and the same icons come back anchored beside the charts in sheets 0004, 0009 and 0010)
- Evidence: wwdc2022_110342 (sheet 0003, q0020 and q0021, monochrome blue thumbnails in a two by two grid under a concept label, one grid for change and another for proportion)
- Evidence: wwdc2023_10115 (sheet 0004, q0033, grid of green square icons with rounded corners, each with a symbol and the modifier's name below)
- Evidence: wwdc2023_10073 (sheet 0010, q0090, six named gestures with direction arrows in a two-row grid)
- Evidence: wwdc2023_10193 (sheet 0004, q0035, a bolt inside an outline for action and a three-dimensional box for entity, side by side with a label)
- What this teaches about building interfaces: a concept gains recognition when it receives its own form and reappears anchored to the content it illustrates, and the uniform grid communicates that the items are peers, not a hierarchy.

## The closing condenses the whole piece into a mosaic of thumbnails, unlabeled, resting on a photographic still or a card of related sessions
- Evidence: wwdc2022_103 (sheet 0041, q0364, mosaic of twelve icons in a four by three grid, without names)
- Evidence: wwdc2022_113 (sheet 0035, q0308 and q0309, grid of four columns by three rows of icons under a small centered title, followed by a plain light frame)
- Evidence: wwdc2022_110441 (sheet 0014, q0119 to q0122, irregular grid gathering almost all of the session's examples, from clocks to wireframes, spacing slides, icons and app screens)
- Evidence: wwdc2023_10138 (sheet 0015, q0127 and q0128, closing block over a still life of a wooden table with three related sessions)
- Evidence: wwdc2023_10078 (sheet 0010, q0086 to q0088, list revealed item by item over a photograph of a wooden table, with the event code right aligned on each line)
- Evidence: wwdc2023_10026 (sheet 0008, q0071 and q0072, leather strap watch on a wooden table receiving the list of four sessions right aligned)
- What this teaches about building interfaces: a thumbnail summary works because it recovers accumulated visual recognition, and the real photographic surface breaks the slide's monotony without introducing new information.

## Translucent glass panel is the default material, always demonstrated with the surroundings visible through it and contrasted with the opaque equivalent
- Evidence: wwdc2023_10076 (sheets 0003 and 0004, q0022 to q0032, the translucent window at several angles, part empty and part with the app inside, first in bright light and then in a dark setting, against the frame of solid blue gray panels that instructs avoiding opaque windows)
- Evidence: wwdc2023_10073 (sheet 0004, q0028 and q0032 to q0034, a large blurred panel in the background and another smaller, sharp one in front, with a secondary dark rectangle that appears and disappears)
- Evidence: wwdc2023_10072 (sheet 0003, q0019 to q0027, the glass music window inside a room, with transparency varying to the point where the window nearly disappears against the light wall)
- Evidence: wwdc2023_10075 (sheet 0004, q0030 and q0031, dark glass card with cover art, icons, title, artist, thin progress bar and three transport buttons)
- What this teaches about building interfaces: transparency is a legibility risk that needs to be exercised in the worst case, a light wall or a high contrast scene, and the opaque counter-example only convinces when shown in the same framing.

## Hierarchy is built through opacity and depth, with the secondary element receding instead of shrinking
- Evidence: wwdc2023_10075 (sheet 0004, q0034 and q0035, the library window appears behind the now playing card, more faded, with the close button floating above the group)
- Evidence: wwdc2023_10072 (sheet 0012, q0102 to q0104, small, semi-opaque playback panel placed in front of and to the left of a large cinema screen; sheet 0002, q0015, three overlapping words separated only by opacity contrast)
- Evidence: wwdc2022_110342 (sheet 0004 and sheet 0008, the agenda slide keeps the three topics visible and fades the ones not currently underway)
- Evidence: wwdc2023_10138 (sheet 0013, q0112 to q0114, three levels of text distinguished only by decreasing opacity over a dark background)
- What this teaches about building interfaces: demoting through opacity preserves the element's position and shape, which keeps the screen's map stable and costs the user less than removing or resizing.

## The transformation of one component into another is shown frame by frame, with the anchor points staying in place
- Evidence: wwdc2023_10026 (sheet 0006, q0049 and q0050, the stopwatch goes from an analog dial to a digital readout while keeping the same buttons in the same positions, with the annotation naming the pattern right on the screen)
- Evidence: wwdc2023_10194 (sheet 0017, q0151 to q0153, a black circle stretches sideways until it becomes two ends linked by a thin band and then splits into two independent circles; sheet 0011, q0094 and q0095, the full screen workout condenses into the pill, keeping only the icon and distance)
- Evidence: wwdc2022_110342 (sheet 0010, q0089 and q0090, a vertical bar segmented into colored blocks becomes a horizontal bar chart in the same colors, ordered by length)
- Evidence: wwdc2023_10197 (sheet 0009, q0074 to q0079, the origin symbol stays to the side while the shape inside the plane grows and resolves, also turning into a check and a cloud with sun turning into a cloud with rain)
- What this teaches about building interfaces: continuity of identity depends on keeping something fixed during the transition, a button, icon, color or position, and that is what separates a legible transformation from a disguised screen swap.

## The presenter shares the frame with the material instead of alternating with it, and the interface usually appears overlaid on the person's shot
- Evidence: wwdc2023_10078 (sheet 0001, q0005 to q0007, the list of topics stays translucent in the right corner of the presenter's shot, over a blurred background)
- Evidence: wwdc2022_110340 (sheet 0003, q0022 and q0023, the list of five words in a split screen beside the presenter)
- Evidence: wwdc2023_10073 (sheet 0011, q0094 to q0096, growing list in a split screen layout with the presenter on the right)
- Evidence: wwdc2023_10026 (sheet 0003, q0023 and q0024, bold title template, simple list and light gray background in a split composition with the presenter)
- Evidence: wwdc2022_103 (sheets 0005, 0010, 0022, 0023, 0025 and 0026, the dominant composition places the interviewee and the interface in the same frame, half face and half screen, instead of showing the interface in isolation)
- What this teaches about building interfaces: keeping reference and commentary simultaneously on screen avoids the viewer having to choose between looking at the person or the artifact, and the same reasoning applies to help panels that do not cover the content they explain.

## Single source findings

- Tap target drawn as a thick white outline much larger than the chart's bar, making it explicit that the tappable area extends well beyond the drawing of the mark, with the accessibility label quoted right below (wwdc2022_110340, sheet 0014, q0121 to q0123).
- Anatomy of the chart tooltip: dark rectangle with the date in gray above and the value in larger bold below, anchored by a thin vertical line that descends to the top of the corresponding bar, tested on three bars in a row (wwdc2022_110340, sheet 0013, q0112 to q0114).
- The same chart description rewritten in four steps within the same dark card, from the period label to the label with the number highlighted, then a full sentence below the chart, then the sentence plus the percentage change with an arrow (wwdc2022_110342, sheet 0004, q0031 to q0036).
- Three data reading scales labeled on screen, with the intermediate level demonstrated twice, one with bars highlighted in red against gray and another in yellow against gray, before the arrow annotations anchored on specific bars (wwdc2022_110342, sheet 0005, q0041 to q0044).
- Link between list and chart demonstrated frame by frame: the statistic row gets a solid green background and the corresponding bar above turns green, and the highlight migrates when the selected row changes (wwdc2022_110342, sheet 0006, q0046 to q0049).
- Point size compensation between typographic widths: all lines first at 20 pts with different final widths, then adjusted by style, from 42 pts on the narrowest to 20 pts on the widest, to fit the same horizontal measure (wwdc2022_110381, sheet 0006, q0049 and q0050).
- Explicit risk signaling with a yellow warning triangle, which appears first over the most compressed paragraph column and then also over the next one, marking the long text that loses legibility (wwdc2022_110381, sheet 0006, q0052 to q0054).
- Anatomy of the isolated letter in four stages, the word with no annotation, then with a dotted line measuring the width of each style, then with color bands covering the inner curves, and finally reduced to abstract teardrop shapes with no text at all (wwdc2022_110381, sheet 0005, q0037 to q0040).
- In the mirrored layout, the sun icon and the weather icon stay in the same physical corner in both versions while the city name and the texts swap sides (wwdc2022_110441, sheet 0003, q0026 and q0027).
- Icon by icon comparison across two row slides labeled by language, one symbol per frame, showing that the document with text lines flips and the search icon keeps its handle pointing to the same side in both versions (wwdc2022_110441, sheet 0011, q0094 to q0099).
- The letter spacing annotated as a percentage below the sentence stays the same across three frames and increases from the fourth on, stretching and breaking the connections of the cursive script until the letters separate artificially (wwdc2022_110441, sheet 0009, q0076 to q0080).
- Game HUD with fixed positions by function, abilities grouped in the bottom right corner, translucent circular minimap in the top left corner and mission box in the top right corner, and the damage numbers going from an isolated value to a stacked pile (wwdc2022_103, sheet 0029, q0258 to q0261; sheet 0030, q0265 and q0266).
- Internal testing tool overlaid on the final art, with a monospaced text box listing speed, drawing mode and coordinates over the scene, present in one frame and absent in the previous one, meaning a development interface and not the screen delivered to the player (wwdc2022_103, sheet 0029, q0255).
- Storyboard of the body tracking prototype with nine numbered sketches in a grid, red markers and yellow stars at the capture points and the last one labeled as ready, followed by the person performing the same movements (wwdc2022_103, sheet 0019, q0163 to q0166).
- Instructions modal in a three by three grid, each cell with a figure in a numbered pose and a red contact point marker, ending in a readiness notice, and in the next frame the person performs the movement in the same environment (wwdc2022_113, sheet 0017, q0150 and q0151).
- Grid of exactly nine circular avatars as the fixed page of conversations, repeated in two box finishes, matching the limit of nine pinned conversations (wwdc2023_10026, sheet 0006, q0053 and q0054).
- Hardware diagram justifying the layout system, columns labeled by generation with proportional rectangles and measurements from 38MM to 49MM under each one, with a physical watch overlaid at the center (wwdc2023_10138, sheet 0009, q0079 and q0080).
- Immersion spectrum drawn as three stages side by side with the same silhouette, small distant screen, partial curved screen over a circle on the floor, and gradient sphere surrounding the person (wwdc2023_10072, sheet 0015, q0127).
- The exit immersion button sits in a dark translucent pill with a diagonal arrow in the top left corner and stays in the same corner when the scene expands, remaining alone when the thumbnail bar disappears (wwdc2023_10072, sheet 0019, q0165 and q0166; sheet 0021, q0181 and q0182).
- The light emitted by the content is rendered as a colored reflection on the tabletop under the window, more evident up close, and as a halo on the edge of a photo card that grows (wwdc2023_10072, sheet 0013, q0111 and q0112; sheet 0016, q0136 and q0137).
- Tap area defined for the entire composite cell, image plus text, circled by a dashed rectangle, and not for the visible arrow beside it (wwdc2023_10076, sheet 0010, q0084 to q0086).
- Concentric corner rule converted into a diagram over a real component, with a rounded outline, a circle marking the radius and the label adding inner radius and padding over the same cell (wwdc2023_10076, sheet 0011, q0097 and q0098).
- The hover shape follows the complete card, cover plus text, as a single element: the frames show first the cells with no outline and then each one fully outlined (wwdc2023_10076, sheet 0011, q0095 and q0096).
- Label reveal through gaze focus, with the icon sidebar expanding the share label and, in the next frame, a search field with a microphone icon occupying the same spot (wwdc2023_10073, sheet 0009, q0073 to q0075).
- Eye effort scale in three levels with two kinds of signal, looking down and sideways approved with a green check and looking up and diagonally marked with an orange warning, a third state that is neither right nor wrong (wwdc2023_10078, sheet 0006, q0049 and q0050).
- Repetitive pattern demonstrated as a convergence failure: first both eyes converge on the same hexagon of the mesh, in the next frame each eye gets a different color and converges on a different hexagon of the same mesh (wwdc2023_10078, sheet 0004, q0029 and q0030).
- In StandBy the card background extends until it fills the device's entire screen at the base, revealing a black pill shaped cutout reserved for the sensor region, which the content does not invade (wwdc2023_10194, sheet 0007, q0058 to q0063).
- Layout collapse by relevance across successive states: the scoreboard loses the play text line, becomes dimmed and replaces the clock with the interval name, reducing height and information without swapping components (wwdc2023_10194, sheet 0005, q0038 to q0040).
- The empty gap inside the compact view becomes visible as considerable space between the icon on the left and the value on the right of the same pill, for example a heart with a number on one side and a silhouette on the other (wwdc2023_10194, sheet 0015, q0129 and q0131).
- Progression of detail across sizes in three states of the same content: icon with time, then card with the line name and station, then full layout with a time badge and a progress bar with the named stops (wwdc2023_10194, sheet 0016, q0137 to q0139).
- Translucent bubble with an edge glow used as a symbol of the shared context boundary, with a variable number of people inside, ending in two separate bubbles with one person in each (wwdc2023_10075, sheet 0007, q0063; sheet 0008, q0064 and q0072; sheet 0012, q0108).
- Sharing state communicated by a pill badge fixed above each window, green when shared and gray when not, with two windows in different states coexisting in the same scene (wwdc2023_10075, sheet 0004, q0033 to q0035; sheet 0005, q0040 and q0043).
- Waiting placeholder drawn as a centered frosted glass card, with a two silhouette icon, title, a smaller instruction line and an action button, which disappears when content returns to occupy the same screen (wwdc2023_10075, sheet 0006, q0046 to q0050).
- Ease versus power illustrated by a microwave and a professional espresso machine side by side, separated by a thin vertical line (wwdc2023_10115, sheet 0003, q0023).
- Slide listing, in running text separated by slashes, the states a dynamic design needs to resolve, from loading, dark mode, screen reader, Dynamic Type, pressed, empty and error states, to right-to-left layout, localization, per-device scale, reduced motion and material rendering (wwdc2023_10115, sheet 0005, q0044 and q0045).
- The app icon taken apart into a diagram of three labeled layers, the two foreground ones shown over a checkerboard background to indicate transparency, before the finished circular icon appears with shine and shadow (wwdc2023_10076, sheet 0002, q0013 to q0017).
- The drawing for animation shown in vector stages in black line, loose points, a closed outline of the head and body, dashed circles of the paws overlaid and finally the paws isolated without the body (wwdc2023_10197, sheet 0011, q0091 to q0094).
- Library size communicated by large numbers over a texture of hundreds of small icons, one value emerging discreetly and the larger value appearing sharp before lightening (wwdc2023_10197, sheet 0013, q0109 to q0116).
- The system's search result card has a constant structure throughout the video, a small label at the top, a translucent card with one to four action icons and a short caption under each one, a suggestions section in a list below and a search field with a keyboard at the bottom (wwdc2023_10193, sheets 0001, 0002, 0005, 0006, 0007 and 0008).
- The entity icons repeat the shape the concept has inside the app, circle for contacts and lists, square for albums, carrying details along with them, such as the heart in the corner of the favorites album (wwdc2023_10193, sheets 0005 and 0006).
- Color guidance delivered as a pure, unlabeled sample, a grid of twelve colored diamonds with rounded corners in three rows of four (wwdc2023_10193, sheet 0006, q0049).
- Slides of related sessions with their own pattern, a thin horizontal line above each item, the session name on the left and the event code aligned to the right (wwdc2023_10193, sheet 0007, q0057 and q0060).
