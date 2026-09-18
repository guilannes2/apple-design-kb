# Visual essence of batch ess-13

Basis: 17 video visual syntheses (WWDC 2025 and 2026), read in full.

## A plain-text side summary marks progress, and only the current item changes weight and color
- Evidence: wwdc2025_359 (sheets 0001, 0002, 0004 to 0007, 0009, 0011 and 0012; four left-aligned words, the current one in heavy black, the rest in light thin gray, with no icon or numbering)
- Evidence: wwdc2026_250 (sheets 0004 to 0014; the list grows from two to seven names and the speech never mentions the feature)
- Evidence: wwdc2026_251 (sheet 0002 q0016 and q0017, sheet 0006 q0046, sheet 0007 q0062, sheet 0009 q0079, sheet 0011 q0095)
- Evidence: wwdc2026_321 (sheets 0007, 0011 and 0013, with the notes themselves recording a divergence about which sheets the slide reappears on)
- What this teaches about building interfaces: navigation hierarchy can be made with only weight and color at the same type size, with no bar, no number and no icon. The current state stays legible because everything around it recedes, not because the active item gets decoration.

## Lists, tables, code and inventories are assembled piece by piece in front of the viewer, in time with the speech
- Evidence: wwdc2025_404 (sheet 0007, q0057 to q0063: the vocabulary table is born with only the three headers, then the accepted term, then the ones to avoid, then the definition, and the next row already starts empty)
- Evidence: wwdc2026_234 (sheet 0008, q0069 to q0072: the reference material cards enter one per frame in a row, always preserving the previous ones in the same position)
- Evidence: wwdc2026_290 (sheet 0005, q0042 to q0045: the post-it columns fill in one at a time)
- Evidence: wwdc2026_269 (sheet 0009, q0073 to q0081: the class starts from an empty shell and gains conformance, a type list, a snapshot method and a writer)
- What this teaches about building interfaces: showing the construction teaches the structure better than showing the finished result, because the order of entry reveals what depends on what. This holds for onboarding, long forms and any screen that needs to justify its own complexity.

## Right and wrong are judged by a colored icon anchored to the element, not by a written word
- Evidence: wwdc2025_323 (sheet 0006, q0049 with a red circle and X on the custom background, q0050 with a green check on the zoom transition; sheet 0015, q0135, a red X over two overlapping sampling regions)
- Evidence: wwdc2025_404 (sheet 0005, q0037 to q0040: the two cards appear stacked, the old one with a red X and the new one with a green check, and this happens only once in the entire video)
- Evidence: wwdc2026_227 (sheet 0004, q0031 to q0033: the list of critiques uses a red X for a layout problem and an orange exclamation point for risk, and the difference in severity by color is never verbalized)
- Evidence: wwdc2026_321 (sheets 0005, 0006, 0007, 0009, 0011, 0012, 0013 and 0014: an orange circle with an exclamation point for the problematic practice and a green circle with a checkmark for the corrected one, reused systematically)
- What this teaches about building interfaces: a small pair of icons with fixed colors carries judgment without taking up a line of text, and sustains a gradation of severity (orange warning is different from red error) that the reader learns on the first occurrence and recognizes in all the others.

## A short label connected by a thin line to the exact point on the screen is the standard way to name anatomy
- Evidence: wwdc2025_323 (sheet 0010 q0085 with "Search Field" over the MacBook and iPad fields, sheet 0009 q0076 and q0078 with the border effect, sheet 0008 q0071 over the numeric indicator of the bell icon)
- Evidence: wwdc2025_361 (sheet 0009, q0074 to q0076: arrows and labels name the sidebar, the preview pane and the Icon Composer inspector; sheet 0010, q0087 and q0088, divide the bottom bar into two sections)
- Evidence: wwdc2026_251 (sheet 0003, q0019 to q0022, and sheets 0004, 0011 and 0013: thin gray text connected by a straight line, from start to finish, without the speech verbalizing the convention)
- Evidence: wwdc2026_292 (sheet 0004 q0034 and q0035, sheet 0005 q0040 and q0041, sheet 0014 q0119: the label points from outside the frame to a specific line of the empty state)
- What this teaches about building interfaces: component vocabulary sticks when the name touches the pixel. The same convention works for internal documentation, handoff and review, as long as the label style is discreet enough not to compete with the annotated interface.

## The teaching happens in the difference between two consecutive frames, with one variable changing at a time
- Evidence: wwdc2025_337 (sheet 0004, q0029 to q0030: the reverse field only appears when the animation changes from drawing to erasing, revealing an interface state rule)
- Evidence: wwdc2025_361 (sheet 0013, q0109 to q0111: neutral shadow against chromatic shadow, then the same shadow gaining the extra dark mode line, isolating one property per pair)
- Evidence: wwdc2026_290 (sheet 0002 q0018 and sheet 0003 q0019 to q0024: the Apple Cash card keeps an identical layout and only the label text changes between frames)
- Evidence: wwdc2026_250 (sheet 0013, q0111 to q0112: the pill-shaped button swaps the text for a spinner; sheet 0012, q0104 to q0105: the circular pause button becomes a pill with play and a progress bar)
- What this teaches about building interfaces: comparing states is only honest when everything else stays frozen. Keeping the position, size and color of the surroundings is what turns the change into proof, and it is exactly the discipline missing from most portfolio before-and-afters.

## Code and result share the frame, with the relevant snippet highlighted and the highlight moving along with the speech
- Evidence: wwdc2025_323 (sheets 0004 q0031, 0005 q0039, 0011 q0093, 0014 q0125 and 0016 q0136: code on the left, device on the right, the snippet highlighted on every change of subject; sheet 0007, q0062 to q0063, the highlight migrates from the spacer to the inspector item without the mockup changing)
- Evidence: wwdc2026_314 (sheet 0003 q0027 and sheets 0004 to 0006: monospaced CSS on the left with the relevant line on a light blue background and a block diagram on the right reacting, an identical template for seven concepts in a row)
- Evidence: wwdc2026_315 (sheets 0003, 0004 and 0005: each new CSS block appears alongside the control already with the effect applied)
- Evidence: wwdc2026_269 (sheets 0003, 0012, 0013 and 0016: the code enters overlaid at partial transparency over the running app, leaving the result visible in the background)
- What this teaches about building interfaces: cause and effect need to fit in the same frame. When a line's highlight changes without the result changing, it is proven that line is not the one responsible, and that is information no text delivers as fast.

## The content advances by adding one property at a time, always keeping what was already there
- Evidence: wwdc2026_314 (sheet 0004, q0028 to q0031: first the display mode, then the column template, then the spacing, with the diagram redrawing itself with each addition)
- Evidence: wwdc2026_315 (sheet 0003, q0019 to q0023: native appearance, rectangular border with inherited font, rounded button with a custom arrow, solid button in the open state)
- Evidence: wwdc2025_337 (sheet 0015, q0128 to q0132: the light blue highlight advances from snippet to snippet as the cited API changes, within the same blocks comparing three frameworks)
- What this teaches about building interfaces: a style system is learned in cumulative layers, and erasing the previous step forces the reader to reconstruct the context. The rule holds for design token documentation as much as for a tutorial.

## A circular badge in the corner marks what is new or which version a behavior belongs to
- Evidence: wwdc2026_269 (sheets 0008 to 0019: a green circular badge fixed in the top right corner of the code blocks, across dozens of frames, without the narration mentioning it every time; sheet 0017, q0145 to q0149, the same code snippet appears identical with a gray badge for one version and then green for the next)
- Evidence: wwdc2025_323 (sheet 0004, q0031 to q0032: a green badge pointing to the exact line of the new modifier inside the block)
- Evidence: wwdc2026_315 (sheet 0001, q0007 to q0008: a green circular version watermark overlaid on the corner of the site screenshot)
- What this teaches about building interfaces: availability is visual metadata, not a sentence. A persistent badge, always in the same position, lets the reader filter what they can use today without interrupting the reading of the content.

## Almost every result screen is framed in a device frame, and the device chosen carries an argument
- Evidence: wwdc2025_323 (sheet 0003, q0019 and q0020; sheet 0007, q0059 and q0060; sheet 0008, q0072: the same app on MacBook, iPad and iPhone at the same time, reinforcing the idea of a family)
- Evidence: wwdc2026_269 (iPad for the store and the library, iPhone for the toolbar and swipe actions, MacBook for reordering between list and grid)
- Evidence: wwdc2026_290 (sheets 0002 and 0003: all screens in a full iPhone frame with notch and status bar, and the frame is only abandoned when the camera moves in on an isolated card to focus on the text)
- Evidence: wwdc2025_404 (sheet 0006 q0050 brings only the rounded silhouette in the conceptual example, while sheet 0009 q0075 reserves the realistic frame with notch, status bar and progress bar for the real product example)
- What this teaches about building interfaces: the frame declares the degree of commitment. An empty silhouette signals concept, a realistic frame signals product, and switching devices in the middle of an argument is the cheapest way to prove adaptation across platforms.

## What has no image becomes an abstract diagram of blocks and geometric shapes, with no text inside
- Evidence: wwdc2025_356 (sheet 0004, q0028 and q0029: the corner radius calculation drawn on a dark background with a corner line, a dotted circle at the vertex and guides to the shared center)
- Evidence: wwdc2026_314 (sheet 0002, q0012 to q0016: uneven horizontal bands, a dotted mesh and a line mesh with empty cells compare three layout modes before any code)
- Evidence: wwdc2026_321 (sheet 0002, q0015 to q0018: gray bars of varying widths inside a vertical rectangle represent the stack, with an orange outline on the visible region and a vertical ruler for the estimated height)
- Evidence: wwdc2026_269 (sheet 0018, q0159 to q0161, and sheet 0019, q0163 to q0167: the tree of boxes grows layer by layer, turns into rows of pyramids and collapses into a single chain)
- What this teaches about building interfaces: when the subject is behavior and not appearance, drawing the mechanics in neutral blocks keeps the reader from confusing the example with an aesthetic recommendation. The diagram also allows exaggerating scale and quantity, something a real screenshot does not allow.

## Categorical color separates roles within the same diagram, and the legend stays implicit in the repetition
- Evidence: wwdc2026_269 (sheet 0010 q0090 and sheet 0011 q0091: green cards for the write side and blue for the read side, with the same code returning in the stacked cards diagram)
- Evidence: wwdc2025_337 (sheet 0011, q0093 to q0094: blue for components that draw and green for those that do not draw, with the marker going from a gray outline to filled green)
- Evidence: wwdc2026_314 (sheet 0005, q0040 to q0045, orange outline rectangle for the item under edit among blue blocks; sheet 0006, q0050 to q0054, empty green outlines for possible positions and an orange line for the threshold)
- Evidence: wwdc2026_290 (sheet 0005, q0042 to q0045: blue post-its for what the person thinks, peach for what they feel and green for what they do)
- What this teaches about building interfaces: two or three colors with fixed meaning are enough to eliminate a written legend, as long as the meaning never switches within the same piece. The common mistake is recycling the color for another dimension on the next slide.

## An exhaustive grid of samples is the verification instrument shown on screen
- Evidence: wwdc2025_337 (sheet 0013, q0113 to q0116: weight columns from lightest to heaviest with the reference column in bold, first dimmed, then sharp with a scale bar, then with guide points overlaid and finally all nine columns filled in)
- Evidence: wwdc2026_251 (sheet 0011 q0092 compares the system fonts by distinct markers of height, width and per-character grid; sheet 0012 q0100 shows the same share icon in three rows by platform with eight variations each)
- Evidence: wwdc2025_361 (sheet 0002 q0017 and q0018, sheet 0003 q0019 and q0021: color variations of the same icon arranged in horizontal rows under platform labels, always on a black background)
- What this teaches about building interfaces: consistency is proven in a matrix, not in a single example. Fixing one column or row as the reference and varying only one axis at a time is what makes the deviation visible to the naked eye.

## The exact measurements exist only in the image, the speech never states them
- Evidence: wwdc2025_323 (sheet 0012, q0105: five button heights in points, from 16 to 36, one per named size, while the speech deals only with the heights increasing)
- Evidence: wwdc2025_359 (sheet 0012, q0104: the system's typographic table with each line rendered in its own style and the size in points stated beside it)
- Evidence: wwdc2025_361 (sheet 0011, q0099: the material panel shows blur at 50 percent, translucency at 60 percent and chromatic shadow at 100 percent)
- Evidence: wwdc2026_227 (sheet 0015, q0130 to q0131: the damping sliders show numeric values on the right and change position between frames, recording the live adjustment)
- What this teaches about building interfaces: whoever only listens to the presentation leaves without the number that allows the result to be reproduced. When documenting a design decision, the value needs to be written in the visual artifact, not entrusted to the narration or to memory.

## The real tool appears on screen, almost always with the same three-column anatomy
- Evidence: wwdc2025_337 (sheet 0004, q0028 to q0030: category sidebar, central canvas with the symbol and inspector on the right, with the custom mode adding a layers panel below)
- Evidence: wwdc2025_361 (sheet 0009, q0074 to q0076, and sheet 0011, q0091 and q0092: layer list, central preview and inspector with fields and values legible one by one)
- Evidence: wwdc2026_252 (sheet 0003, q0025, and sheets 0005, 0009 and 0012: hierarchy on the left, viewport or graph in the center, inspector on the right, varying only the central panel, with the selected item marked by a solid bar)
- Evidence: wwdc2026_314 (sheet 0007, q0061: capture of the browser inspector with a colored overlay on the grid, column size labels and a side panel of checkboxes controlling the overlay)
- What this teaches about building interfaces: the three-column pattern with the work area in the middle is so stable across different tools that it has become an expectation. Changing only the central panel between modes preserves the orientation of the person using it.

## The component appears isolated on a neutral background before entering context
- Evidence: wwdc2025_323 (sheet 0002, q0011 to q0012: zoom, plain button, tinted button, toggle, list picker and segmented control, first over a central iPhone and then loose, before any code)
- Evidence: wwdc2026_292 (sheet 0002, q0016 to q0018: the anatomy of the search field in three successive states on a textured gray background, and only afterward does the pattern reappear inside each app)
- Evidence: wwdc2026_290 (sheet 0001, q0005 and q0006: generic context menu, tab bar and card, already with red reserved for the destructive action, before any real app enters)
- Evidence: wwdc2026_252 (sheet 0015, q0129 to q0131: the game's speech bubble is then shown isolated as a gray component with no border or shadow)
- What this teaches about building interfaces: separating the piece from the setting is what allows discussing anatomy and states without the example content stealing attention. Context afterward, never before.

## Dimming and opacity direct focus and mark hierarchy, including erasing what is not under discussion
- Evidence: wwdc2025_337 (sheet 0014, q0124 to q0125: the whole panel is dimmed except for one button, with a line and label pointing to it, and the target changes from one layer to another between the two frames)
- Evidence: wwdc2026_250 (sheet 0005, q0040 and q0041, with the first two questions in black and the third in light gray; sheet 0009, q0079, with an opaque laptop next to a semitransparent phone)
- Evidence: wwdc2026_321 (sheet 0006, q0053 and q0054: the screen of one of the two iPhones darkens under a semitransparent overlay while the label and the arrow remain visible)
- Evidence: wwdc2025_404 (sheet 0005, q0037 to q0040: the passage to be merged is set in bold while the rest of the card body drops to light gray)
- What this teaches about building interfaces: reducing the surroundings costs less than highlighting the target and introduces no new element on screen. It is the same mechanism that underlies a modal, a coach mark and a disabled state.

## Fidelity grows in steps: empty outline, wireframe, generic mock, real capture
- Evidence: wwdc2026_292 (sheet 0003, q0025 and q0026: three devices in wireframe evolving from a blank screen to a screen with a tab bar and then with a large title and search field; sheet 0006, q0047 to q0048, the pair of search tabs first appears in wireframe and only afterward in real apps)
- Evidence: wwdc2025_356 (sheet 0012, q0107 and q0108: two completely empty device outlines, one narrow vertical and one horizontal split down the middle, set up the format comparison with no content inside)
- Evidence: wwdc2026_250 (sheet 0004, q0033 to q0036: a grid of unbranded icons turns into an icon with a pizza slice and then a complete delivery screen with a photo, map and action bar)
- Evidence: wwdc2026_234 (sheet 0001, q0004 and q0005: the same mountain scene in a realistic photo and then as a white wireframe mesh over a reference grid)
- What this teaches about building interfaces: choosing the fidelity is choosing which question is open. A wireframe invites discussing position and presence, a colored mock invites discussing style, and mixing the two in the same frame scrambles the conversation.

## Before and after appear in the same frame, labeled or split by a line, not in separate slides
- Evidence: wwdc2025_359 (sheet 0006, q0050 and q0051: the two screens side by side on the same content grid, labeled in full as previous version and new version, with the tab bar as the only difference; sheet 0009, q0077, repeats the technique for grid versus list)
- Evidence: wwdc2026_234 (sheet 0010, q0087: a single frame split vertically by a thin line, with both sides in slightly different tones, working as a comparison curtain)
- Evidence: wwdc2025_323 (sheet 0005, q0040: two devices side by side, one with the tab bar full and the other with it collapsed)
- What this teaches about building interfaces: comparison in sequential frames depends on the viewer's memory, comparison in the same frame does not. When the difference is subtle, the vertical curtain is more convincing than any pair of captures.

## The placeholder is replaced by real content and by the worst case, and that is what reveals the problems
- Evidence: wwdc2026_227 (sheet 0007 q0055 shows the book cover in solid purple color with no image, and sheet 0008 q0067 replaces it with real covers, people's names, comments with relative time and a new comment field; sheet 0009 names the edge cases right in the previews list, including long content, empty club and full club)
- Evidence: wwdc2026_290 (sheet 0003, q0019 to q0020: the card's value is zeroed out while keeping the same label, in a frame dedicated to testing the tone of the name in the worst case)
- Evidence: wwdc2026_292 (sheet 0014, q0119: the empty state is shown in full, with a large central magnifying glass, the term in quotes including a deliberate typo and an instructive subtitle)
- What this teaches about building interfaces: only true content exposes truncation, absence and label ambiguity. Designing the empty state and the extreme together with the happy state is what prevents a late fix.

## Each block closes on a single-sentence card, in large typography over a plain background
- Evidence: wwdc2026_250 (sheet 0003 q0021 in green left-aligned, sheet 0010 q0085 in pink left-aligned and sheet 0014 in centered blue, the same template changing alignment between occurrences)
- Evidence: wwdc2026_251 (sheet 0005 q0044, sheet 0009 q0073, sheet 0011 q0094 and sheet 0013 q0112, repeated in q0113 already centered and with the screen grid sharper around it)
- Evidence: wwdc2025_359 (sheet 0002, q0017 and q0018: white screen with a single centered sentence in bold, one per question that guides the session)
- What this teaches about building interfaces: a screen with one sentence and nothing else works as a breather and as a memory anchor. The price is writing discipline, because the sentence needs to survive alone without the support of an example.

## Each video invents its own notation at the start and recycles it through the end
- Evidence: wwdc2025_337 (sheet 0007, q0058 to q0061: hollow dot for the start of the stroke, filled dot for the end, smaller dots for guides and small arrows for direction, with a summary frame gathering six examples in a two-by-three grid)
- Evidence: wwdc2026_227 (sheet 0010 q0088 to q0090, sheet 0011 q0092 to q0099 and sheet 0012 q0103: black linear icons accumulated from left to right, one per animation concept)
- Evidence: wwdc2026_321 (sheet 0002, q0015 to q0018, with the stack notation reused through sheet 0013 and gaining measurement annotations along the way, including a second orange outline for the off-screen target in q0114)
- Evidence: wwdc2025_359 (sheet 0010, q0083 to q0087: a calendar for time, a circular gauge for progress and a grid of squares for pattern, presented one per frame and only afterward gathered in a row)
- What this teaches about building interfaces: a short graphic vocabulary, presented before being used and never changed afterward, allows condensing the explanation without turning into a secret code. The cost is presenting each symbol in isolation before the first application.

## Photograph of a physical object on a wooden table grounds the abstract concept and closes the video
- Evidence: wwdc2026_227 (sheet 0011 q0094 and q0097 and sheet 0012 q0100 ground perceived weight, response to movement and tactile response on a physical iPhone in hand on a wooden table, never in an isolated capture; sheet 0016 brings the final slide about table photography)
- Evidence: wwdc2026_314 (sheet 0008, q0064 to q0066: wooden table with a green toolbox, blue iPhone and notebook, with the list of next steps growing with each frame)
- Evidence: wwdc2026_321 (sheet 0015, q0127 and q0128: wooden table with a green swan origami and the list of recommendations growing from two to three items)
- Evidence: wwdc2026_269 (sheet 0020, q0176 and q0177: colored physical objects on a wooden table as background, with the text revealed line by line in a column on the left)
- What this teaches about building interfaces: the last frame is where the brand speaks, not the content. A calm photograph with the text in a side column delivers the same message as a list slide, with a completely different temperature.

## A color filter over the scene marks the opening and the closing, and only those
- Evidence: wwdc2025_404 (sheet 0001, q0002 to q0003, with a purple and pink overlay that dissolves at the start; sheet 0011, q0092 to q0093, with a bluish overlay in the last frame)
- Evidence: wwdc2025_361 (sheet 0017, q0145: the presenter's final frame carries a pink closing tint)
- Evidence: wwdc2026_315 (sheet 0007, q0060 to q0061: orange and sepia filter applied over the presenter's scene at the end, with the version badge marking the other end of the video)
- What this teaches about building interfaces: color treatment reserved for the ends works as punctuation, signaling start and end without a title card or text. Using the same device in the middle would destroy the function.

## A dense mosaic of dozens of screens with no caption opens or closes the piece
- Evidence: wwdc2025_359 (sheet 0015, q0127 and q0128: the same app screen in dozens of distinct visual identities, in a regular grid and with no caption, with no thumbnail repeating between the two frames)
- Evidence: wwdc2026_251 (sheet 0013, q0114: uniform mosaic gathering dozens of screens from the cited apps, with no captions)
- Evidence: wwdc2025_361 (sheet 0001, q0004 to q0006, in partial crops of icon grids, and sheet 0016, q0139 and q0141, with two dense initial screens occupying the entire frame)
- What this teaches about building interfaces: quantity is an argument. A wall of examples proves reach and variety in a single frame, and it works precisely because no item asks for individual reading.

## Visible editorial markup over the text shows the writing decision happening
- Evidence: wwdc2025_404 (sheet 0002, q0016 to q0018, with a word struck through inside the sentence itself; sheet 0003, q0022 to q0023, and sheet 0006, q0051 to q0052, with blue marking what was added or reordered against the black of the rest; sheet 0004, q0029 to q0035, with bold running through one stretch at a time before each cut)
- Evidence: wwdc2026_290 (sheet 0006, q0050 to q0051: nine names in orange blocks and, in the next frame, six crossed out by a diagonal line, leaving three; sheet 0008 q0069 to q0072 and sheet 0009 q0073 repeat the elimination one by one next to the very control where the name will live)
- What this teaches about building interfaces: interface text review becomes more convincing when the discard stays visible. Seeing what was cut justifies what remained, and testing the candidate inside the destination component avoids a name that only works in a list.

## Single-source findings

- System typographic table with the size in points declared line by line, from the large title at 34 down to the captions at 12 and 11, and each line rendered in the very style it names; the next frame applies the same styles as annotation over a full-screen cover (wwdc2025_359, sheet 0012, q0104 and q0105).
- Color reference chart gathering four label levels, about twelve system color swatches and three background levels, with each block duplicated in light mode and dark mode in the same frame (wwdc2025_359, sheet 0014, q0121).
- Button heights declared in points, from 16 to 36, and the shape rule separated by size range, with a rounded rectangle at the smaller sizes and a capsule at the larger ones, all in the same diagram with the code box overlaid (wwdc2025_323, sheet 0012, q0103 to q0105).
- Two glass material sampling regions overlapping, marked with a red X, preceded by the diagram of the pill surrounded by its own sampling region (wwdc2025_323, sheet 0015, q0133 to q0135).
- Icon canvas annotated with a dimension label over a vector selection with resize handles, on top of a grid of concentric circles and guide lines (wwdc2025_361, sheet 0006, q0046).
- Layer export convention shown literally, thumbnails over a checkered transparency background numbered in layer order, from the background to the glyph, each one displaying the artwork of its own layer (wwdc2025_361, sheet 0008, q0066).
- The same icon placed against seven different backgrounds in sequence, changing only what is behind it, with the icon shifting from opaque to translucent and taking on the tone of each background (wwdc2025_361, sheet 0015, q0127 to q0133).
- A point that marks start and end at the same time gets its own elongated capsule shape, distinct from the round points used in the other cases (wwdc2025_337, sheet 0010, q0089 and q0090).
- The legend grows from three to four point types and the new item enters with a diamond marker, while the rest keep the circle (wwdc2025_337, sheet 0012, q0107 to q0108).
- Tab bar with the group inside a capsule and the circular search button separate beside it, composition repeated in three different apps, one of them adding a mini player in a row above (wwdc2025_356, sheet 0009, q0074 to q0076).
- Margin next to the edge studied in isolation, with a small unlabeled capsule changing its distance from the rounded corner between two frames, and the corner then enlarged with it already gone (wwdc2025_356, sheet 0005, q0042, q0043 and q0045).
- Highlight tab taken out of the bar and turned into an isolated circular button in the bottom right corner, with the other four grouped on the left (wwdc2026_269, sheet 0004, q0033 and q0034).
- Items moving out of the ellipsis menu into the toolbar between two frames, arriving highlighted in blue (wwdc2026_269, sheet 0005, q0042 to q0043).
- Compiler error drawn as a light red band with an icon, anchored at the exact line where it occurs (wwdc2026_269, sheet 0017 q0153 and sheet 0018 q0157 and q0158).
- Predictive suggestion inside the same line uses two shades, the part already typed in darker black and the part predicted by the system in lighter gray (wwdc2026_292, sheet 0011, q0095 and q0096).
- Colored token distinct from free text inside the search field, with two coexisting in the same field, and a labeled generic avatar preceding the application to show the base component (wwdc2026_292, sheet 0013, q0109 to q0114).
- Searched term highlighted on a yellow background inside the results preview, a recurring feature the speech never describes (wwdc2026_292, sheet 0005 q0037 and sheet 0012 q0103).
- Exception state signaled only by type weight, with the label turning bold in the inspector when the value was adjusted on that component, while the neighbors stay at normal weight (wwdc2026_252, sheet 0008, q0065 to q0067).
- Encapsulation shown as a visible replacement, several loose read and logic nodes giving way to a single node with a custom name and a grouping icon (wwdc2026_252, sheet 0011, q0096 to q0099).
- Adjustment panel shown first in the bad state, as a dark layer that occupies the lower half and obstructs the interface in a narrow window, and then reorganized side by side with the preview, with a label pointing to the resize button that solves it (wwdc2026_227, sheets 0014 and 0015, q0124 to q0129).
- Proximity communicated by area of color, with the radar of scattered points turning into a solid green circle that fills almost the entire screen (wwdc2026_227, sheet 0012, q0100 to q0101).
- Larger interface text demonstrated on the same product card, with the vertical layout preserved and nothing truncated, preceded by the adjustment screen with the toggle active and the slider at the base (wwdc2026_251, sheet 0010, q0084 to q0087).
- Color concentrated only where it communicates, with the colored top bar annotated at three points and then neutral with the annotation that the color scrolls off the screen (wwdc2026_251, sheet 0008, q0070 to q0072).
- Pure structural guide before any content, with the columns drawn as thin orange vertical bars over a light gray background that change position and spacing between frames (wwdc2026_314, sheet 0003, q0019 to q0020).
- Fill order of a grid proven with boxes numbered 1 to 15 in four columns of unequal heights, inside a browser window (wwdc2026_314, sheet 0003, q0022).
- Dropdown menu stopping being a vertical list and turning into a grid of cards with explicit rows, columns and spacing, shown next to the code that produces the change (wwdc2026_315, sheet 0005, q0040 to q0041).
- Rich content inside a list option rendered as a square card with an icon above and a label below (wwdc2026_315, sheet 0004, q0035 to q0036).
- Rendering cost explained as a horizontal timeline with regular frame-deadline markers, and a block that was dark gray turning red when it goes past the deadline (wwdc2026_321, sheet 0010, q0087 to q0090).
- Spectrum of literalness of a metaphor drawn as a slider control between two named extremes, reappearing with the indicator in a different position next to two alternative icons for the same function (wwdc2026_250, sheet 0007, q0057 to q0058).
- Only real product capture in an entire video, a documentation page with a side filter, a grid of four principle cards and an index on the right, inserted for a single frame (wwdc2026_250, sheet 0015, q0132).
- Gray human silhouette used as a scale reference tool inside the three-dimensional scene, changing position between frames while the scene gains annotations (wwdc2026_234, sheet 0003 q0026 and sheet 0005 q0039 and q0040).
- Elements to remove marked directly over the panorama with simple geometric shapes, a large translucent oval and white outline circles, creating a vocabulary of circling to point out a problem (wwdc2026_234, sheets 0009 and 0010, q0080, q0081, q0084 and q0085).
- Pipeline of an asset broken down into four stages stacked vertically, from motion data in colored lines to mesh, then gradient texture and finally the rendered element with fine fibers (wwdc2026_234, sheet 0014, q0125).
- Prompt bubble with translucent background and a three-color gradient border as the most recurring graphic element of an entire video, always displaying the request text in full (wwdc2026_227, sheets 0004, 0005, 0006, 0008 and 0014).
- Live process recording given away by an overlaid elapsed-time stopwatch in the captures of the development environment (wwdc2026_227, sheet 0002, q0014 to q0016).
