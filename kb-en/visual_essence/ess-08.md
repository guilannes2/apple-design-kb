# ess-08: recurring visual patterns

Batch of 16 videos (WWDC 2020 and 2021), read from the visual syntheses sheet by sheet.

## The session index lives on screen as a persistent column, with the current item lit and the previous ones dimmed in gray
- Evidence: wwdc2020_10175 (sheet 0001, q0007 to q0009; sheet 0021, q0187 to q0189)
- Evidence: wwdc2021_10097 (sheet 0002, q0010 to q0014; returns in sheets 0005, 0007, 0009 and 0014)
- Evidence: wwdc2021_10275 (sheet 0004, q0031; sheet 0017, q0147; sheet 0028, q0248 to q0250)
- Evidence: wwdc2021_10245 (sheet 0001, q0007; sheet 0008, q0068 to q0070; sheet 0015, q0127 to q0129)
- Evidence: wwdc2021_10126 (sheet 0003, q0025 and q0026)
- Evidence: wwdc2021_10184 (sheet 0002, q0016 to q0018; sheet 0005, q0043 and q0044)
- Evidence: wwdc2020_10640 (sheets 0001 and 0013)
- Evidence: wwdc2021_10250 (sheet 0001, q0004 to q0007; sheet 0013, q0117)
- What this teaches about building interfaces: orientation within a long flow does not need a progress bar or numbering, it is enough to keep the whole list visible and vary the weight and opacity of the current item. Several records note that the speech does not mention this feature, meaning it alone carries the function of "where am I".

## Each rule comes accompanied by the right and wrong pair, sealed by a green check circle and a red X in the same frame
- Evidence: wwdc2020_10206 (sheet 0024, q0208 to q0216, with the items revealed one by one next to two devices)
- Evidence: wwdc2020_10640 (sheet 0005; sheet 0017, q0146 to q0150; sheet 0025, q0217 and q0218)
- Evidence: wwdc2021_10250 (sheet 0008, q0064 to q0069; sheet 0017, q0146 to q0148)
- Evidence: wwdc2020_10207 (sheet 0006, q0049 to q0052; sheet 0016, q0141)
- Evidence: wwdc2021_10097 (sheet 0008, q0069 and q0070, "Path" approved against "Stroked path" rejected)
- Evidence: wwdc2021_10126 (sheet 0009, q0077 and q0078)
- Evidence: wwdc2020_10175 (sheet 0009, q0079 to q0081, gray X and green checkmark applied to the code and the result at the same time)
- What this teaches about building interfaces: the norm only becomes clear when the deviation is shown alongside it. The seal is an element foreign to the interface, overlaid from outside, and this is intentional: it separates the judgment from the product. The effective pair isolates one variable, keeping everything else identical between the two sides.

## The measurement is drawn over the element itself, in colored guides and rulers with the value in points alongside
- Evidence: wwdc2020_10640 (diameter "19pt" next to the pointer, sheet 0004, q0033; 12pt padding with bezel against 24pt without bezel, sheet 0018; radii of 21pt, 15pt and 8pt in red, sheet 0019; stroke of 4.5pt against 1pt, sheet 0025)
- Evidence: wwdc2021_10250 (sheet 0003, q0024, blue guide lines labeled "left-margin Regular-M" and "right-margin Regular-M")
- Evidence: wwdc2020_10207 (sheet 0016, q0136 to q0139, numbered aqua green vertical guides, dotted orange boxes and yellow dashed centering guides)
- Evidence: wwdc2021_10029 (sheet 0021, q0183 and q0184, blue rulers of 800px and 400px over the photo)
- Evidence: wwdc2020_10175 (sheet 0002, q0015 and q0016, colored vertical bars marking spacing between letters; sheet 0004, q0029 to q0032, horizontal bars as rulers alongside the glyph)
- Evidence: wwdc2021_10275 (sheet 0023, q0205 to q0207, contrast ratios annotated over the same dialog box in two versions)
- What this teaches about building interfaces: a number loose in a table does not convince, a number anchored to the pixel it governs does. When the measurement appears over the drawing, the decision becomes auditable and replicable by whoever implements it.

## Labeled callout lines name the part of the interface directly over the real capture
- Evidence: wwdc2020_10206 (sheet 0004, q0028 to q0034, "Empty space" pointing to the empty area and then "Fill with content" and "Fast navigation" stacked)
- Evidence: wwdc2020_10205 (sheet 0013, q0112 to q0117, "Currently selected color" and "Saved colors")
- Evidence: wwdc2021_10029 (sheet 0012, q0103 and q0105, "Safe area" and the inset variable pointing to the green strip; sheet 0013, q0111, four labels linked to the four edges)
- Evidence: wwdc2021_10097 (sheet 0013, q0115, "Accent" and "Multicolor" pointing to distinct parts of the same folder; sheet 0008, q0072, "Emphasize" linked to the arrow)
- Evidence: wwdc2021_10275 (sheet 0023, q0199 to q0201, labels linked to two colored dots; sheet 0020, q0173 to q0178, label linked to the new festival section)
- Evidence: wwdc2021_10126 (sheet 0005, q0038 and q0039, gray line linking the three-line icon to its name)
- Evidence: wwdc2021_10184 (sheet 0005, q0037 and q0038, drawn arrow pointing to a small icon that would otherwise go unnoticed)
- Evidence: wwdc2021_10081 (sheet 0002, q0016 to q0018, callout pointing to the controller support badge on the App Store card)
- What this teaches about building interfaces: naming the element in the image is what turns a capture into documentation. It applies both to pointing out the problem and pointing out the solution, and it works best when the label stays outside the element, linked by a thin neutral line, without covering the interface.

## The argument is the difference between two consecutive frames, with one variable swapped and everything else frozen
- Evidence: wwdc2021_10029 (sheet 0003, q0021 to q0023, the meta tag enters and the browser bar turns from yellow to green; sheet 0009, the newsletter banner disappears and the color goes to filling without interruption)
- Evidence: wwdc2020_10175 (sheet 0015, q0127 to q0129, the same paragraph with tight leading and then loose leading)
- Evidence: wwdc2021_10278 (sheet 0008, q0069 to q0071, the highlight rectangle covers the audio file path and the value changes between one frame and the other)
- Evidence: wwdc2021_10275 (sheet 0006, q0047 to q0053, the list keeps the checkbox and category dots while each item is rewritten; sheet 0007, q0056 to q0060, the two-column grid stays and only the photos and names change)
- Evidence: wwdc2020_10640 (sheet 0016, q0137 and q0138, the button without highlight and then with a bluish halo)
- Evidence: wwdc2021_10126 (sheet 0007, q0055 to q0059, the feature list and the prototype screen change in sync)
- What this teaches about building interfaces: a clean comparison requires freezing the context. When two things change at the same time, the demonstration loses its power of proof, and that is why practically every comparison in the batch reuses the same layout, the same example text and the same frame.

## Code and rendered result sit side by side, with a highlight rectangle jumping from snippet to snippet
- Evidence: wwdc2021_10029 (sheets 0003, 0004, 0007 to 0010 and 0012 to 0016; the order of the sides even inverts between blocks, code on the left in sheet 0003 and on the right in sheets 0008 to 0010)
- Evidence: wwdc2021_10081 (sheet 0010, q0085 to q0088, the same Swift block stays still while the gray highlight moves through the declaration, the condition and the two effect blocks)
- Evidence: wwdc2021_10278 (sheet 0007, q0057 to q0060; sheet 0010, q0085 and q0086; sheet 0012, q0102, with the highlight going from a single isolated line to an entire block)
- Evidence: wwdc2020_10207 (sheet 0008, q0064 to q0067, code progression in three steps with the preview alongside)
- Evidence: wwdc2020_10175 (sheet 0020, q0173 to q0180, the SwiftUI construction progresses from centered text to the stack with side margin)
- What this teaches about building interfaces: the moving highlight solves the problem of saying where to look without cropping the context. It is worth noting the honest limit of the technique, recorded in wwdc2020_10175: in several sequences the rendered result stays identical while the code grows, and in those stretches the image proves nothing.

## Lists enter by addition, one item per frame, and what has already passed stays visible in gray
- Evidence: wwdc2021_10081 (sheet 0001, q0005 to q0007; sheet 0006, q0052 and q0053; sheet 0009, q0077 to q0080)
- Evidence: wwdc2021_10245 (sheet 0013, q0114 to q0116, the slide goes from the title alone to three lines and then four)
- Evidence: wwdc2021_10278 (sheet 0010, q0082 to q0084 and sheet 0013, q0110 to q0112, with subitems appearing dimmed first)
- Evidence: wwdc2020_10640 (sheet 0027, q0235 to q0239, current item in black and previous ones in gray, aligned beside the face)
- Evidence: wwdc2020_10206 (sheet 0024, q0208 to q0216, the next item already visible in gray before lighting up)
- Evidence: wwdc2021_10184 (sheet 0003, q0022 and q0023, the audio section enters below the already existing exceptions)
- What this teaches about building interfaces: progressive disclosure keeps the accumulated context instead of swapping the whole screen. Leaving the next item pre visible in gray anticipates the structure without competing with the current item, a behavior directly applicable to onboarding lists and long forms.

## The interface appears inside a device frame, and the same screen is repeated at several widths side by side
- Evidence: wwdc2020_10206 (sheet 0001, q0006 and q0009, Mail on MacBook with three columns, iPad with two and iPhone with one; sheet 0019, q0171, five devices aligned with different apps and the same sidebar structure)
- Evidence: wwdc2021_10029 (the notes record that every website demonstration appears in a device frame, never as a loose capture; sheet 0012, q0102, three iPhones side by side)
- Evidence: wwdc2020_10205 (sheet 0009, q0079 to q0081, the same list on iPhone, iPad and a Mac window in sequence)
- Evidence: wwdc2021_10275 (sheet 0014, q0119 and q0120, from two to four iPhones lined up at increasing text sizes)
- Evidence: wwdc2020_10175 (sheet 0017, q0149 and q0150, table comparing style by style between iOS at reduced scale and macOS)
- What this teaches about building interfaces: adaptation is not explained, it is shown in parallel. Putting the widths together in the same frame makes the rule for columns, density and text size appear as a single decision, instead of three disconnected screens.

## The anatomy of the component is built in a thin-line wireframe, step by step, with the parts named
- Evidence: wwdc2020_10205 (sheet 0003, q0022, list of four items with the captions "Label" and "Icon", then a second example with a header and hierarchy separator)
- Evidence: wwdc2020_10206 (sheets 0021 to 0025, the sidebar is born from the title and the tabs, gains a collapsible section, a checkbox, an add button and finally an editing state with the item in blue)
- Evidence: wwdc2020_10207 (sheet 0008, q0069 to q0072, the Mac window goes through a gray wireframe, a colored version and a pink and red margin annotation grid)
- What this teaches about building interfaces: removing color and content isolates the structure. The step-by-step wireframe teaches the order of decisions, first the skeleton, then the sections, then the states, and it avoids discussing finish before the hierarchy is settled.

## Vector drawing is opened at anchor points and handles, and overlapping outlines show the interpolation
- Evidence: wwdc2020_10175 (sheet 0004, q0035 and q0036, the letter turns into an outline with numbered nodes; sheet 0005, q0044 and q0045, arrows indicate the direction each point moves)
- Evidence: wwdc2021_10097 (sheet 0007, q0061, square anchors and a round control point linking a straight line and a curve; sheet 0008, q0064, three variants overlapped in a cyan outline)
- Evidence: wwdc2021_10250 (sheet 0007, q0057 to q0063, the crown progresses from a silhouette with points to solid black with no points; sheet 0015, q0127 to q0135, red and blue outlines overlapped with lines linking each point to its counterpart)
- What this teaches about building interfaces: the presence or absence of anchor points becomes a state indicator, edit mode versus final result. And showing the point-to-point correspondence explains why two shapes only interpolate if they have the same point count and the same path order.

## The work tools appear from within, with a layers panel on one side and a properties panel on the other
- Evidence: wwdc2020_10207 (sheets 0004 and 0005, q0034 to q0042, layers named item by item and properties with opacity, shadow, font and alignment)
- Evidence: wwdc2021_10250 (sheet 0006, q0054, variants by weight and scale on the left, matrix in the center, fill, borders, shadows and blur on the right; sheet 0011, q0091 to q0099, rendering panel with layers, visibility and opacity)
- Evidence: wwdc2020_10175 (sheet 0006, q0049 to q0054, a dark panel with weight and optical size sliders, and the glyph changing along with the numeric field)
- Evidence: wwdc2021_10278 (sheet 0006, q0047 to q0049, the Xcode file navigator appears next to the instructions slide, in the same frame)
- What this teaches about building interfaces: showing the tool alongside the result connects the design decision to the control that produces it. The three-zone layout, navigation on the left, stage in the center and inspector on the right, repeats tool after tool and serves as a reference for any editor.

## The SF Symbols app and similar ones follow the same three-column skeleton, with categories, grid and inspection panel
- Evidence: wwdc2021_10250 (sheet 0005, q0037 to q0045, with a blue frame on the selected item and a separate "Custom Symbols" section at the bottom of the sidebar)
- Evidence: wwdc2021_10097 (sheet 0014, q0122 to q0123, the right panel switches from availability to active controls for rendering, color and background)
- Evidence: wwdc2020_10207 (sheet 0009, q0078 to q0081, preview, availability by system version and usage restrictions in the details panel)
- What this teaches about building interfaces: the inspector switches content according to the mode, informative when there is nothing to edit and full of controls when there is, without changing position or width. The grid cell carries the glyph plus the technical name underneath, which makes visual search and copying the identifier the same action.

## Variants are organized in a matrix, the same unit repeated across two dimensions
- Evidence: wwdc2021_10097 (sheet 0004, q0033 and q0034, variant columns and fill rows applied to the same heart; sheet 0015, q0129 and q0130, four appearance rows by hue columns; sheet 0016, q0143, four modes by five symbols)
- Evidence: wwdc2021_10250 (sheet 0006, q0054, weights from Ultralight to Black in sizes S, M and L)
- Evidence: wwdc2020_10207 (sheet 0010, q0086 to q0090, export template in three rows by nine columns, one dimension for scale and another for weight)
- Evidence: wwdc2020_10175 (sheet 0018, q0155 to q0159, one column of styles grows to seven columns of size, from xSmall to xxxLarge)
- What this teaches about building interfaces: the matrix proves coverage and exposes gaps. By fixing a sample element and varying only the axes, it becomes visible that the system is combinatorial, and any missing cell becomes an immediate question.

## Diagrams use color as a role code, and this convention is almost never stated in the speech
- Evidence: wwdc2021_10081 (sheet 0002, q0010 to q0012, dark blue boxes for the input classes, green and red for connection and disconnection; sheet 0007, q0056 and q0057, blue for configuration and green for the resulting object; the notes record that the speech does not mention the convention)
- Evidence: wwdc2021_10278 (sheet 0005, q0037 to q0039, engine in dark blue, player in light blue and pattern in green, revealed in three steps)
- Evidence: wwdc2020_10206 (sheet 0020, q0177 to q0180, blue blocks for the main level and gray for the subordinate one, double arrows for alternation and descendants for hierarchy)
- Evidence: wwdc2021_10250 (sheet 0018, q0154 to q0159, blue requirement boxes pointing to green template boxes)
- What this teaches about building interfaces: color carries the taxonomy without a legend, which speeds up reading for those who already know the system and leaves those who do not without support. If color is the sole carrier of the role, the diagram needs a redundant label, the same principle that appears in the batch's accessibility screens.

## Right-to-left support is proven with the same screen mirrored, not just stated
- Evidence: wwdc2020_10175 (sheet 0011, q0097 to q0099, the word in English and in Arabic receive the same measurement arrows and then two iPhones with Settings in Arabic)
- Evidence: wwdc2020_10207 (sheet 0012, q0103 to q0105, a calendar in English and in Arabic with the context menu on the opposite side and the text aligned to the right)
- Evidence: wwdc2021_10097 (sheet 0007, q0057 to q0059, the pair labeled with the two directions on the battery symbol, then applied to two mirrored screens with a green check on the correct one)
- Evidence: wwdc2021_10275 (sheet 0017, q0149, icon grid with navigation and alignment inverted)
- What this teaches about building interfaces: mirroring is a per-element decision, not a global switch. Directional symbols flip, object symbols stay, and the only way to verify this is to assemble the whole screen in both directions and look.

## The alignment between symbol and text is taught with the labeled typographic lines and the glyph next to a letter
- Evidence: wwdc2020_10207 (sheet 0002, q0013 to q0015, markings for cap height, x-height and baseline, the latter in red, revealing that the symbol sits slightly above the baseline)
- Evidence: wwdc2021_10097 (sheet 0003, q0019 and q0020, "Vertical alignment" with the same guides and "Horizontal alignment" with dotted vertical guides; q0027 places the heart next to a lowercase letter)
- Evidence: wwdc2021_10250 (sheet 0002, q0014 and q0015 and returns on sheets 0003, 0009, 0014 and 0016, matrix with the letter to the left of each row and the symbols aligned by the baseline)
- What this teaches about building interfaces: an icon next to text is a typographic problem, not a graphic one. Aligning by the center of the box produces optical misalignment, and the correct reference is the font's lines, which also sets the scale and stroke weight to match the body text.

## Active state is marked by a check plus a highlight of the entire row, and the list of options repeats this vocabulary
- Evidence: wwdc2020_10205 (sheet 0004, q0030 to q0033, a checkmark on the active item and a color highlight covering the row in focus, two distinct treatments in the same menu; sheet 0007, q0056 and q0057, simultaneous check on two independent axes)
- Evidence: wwdc2021_10097 (sheet 0014, q0125 and sheet 0017, q0147, color picker as a vertical list with a blue check on the active item)
- Evidence: wwdc2021_10250 (sheet 0011, q0094 to q0096, color menu with a square swatch next to the name and a check on the active option; sheet 0005, blue frame on the selected item in the sidebar)
- What this teaches about building interfaces: selection and focus are different things and need different treatments in the same component. And a menu can carry selections from independent axes at the same time without confusion, as long as they are separated by a dividing line.

## The system's limit is shown on the screen, in a yellow alert or an error card, and not hidden
- Evidence: wwdc2020_10175 (sheet 0007, q0055, yellow triangle when the requested value falls outside the available range)
- Evidence: wwdc2020_10207 (sheet 0013, q0109 to q0117, a pink error card overlaid on the window warning that the symbol does not exist before a certain system version)
- Evidence: wwdc2021_10126 (sheet 0006, q0046, isolated yellow alert icon right below the bar with six tabs)
- Evidence: wwdc2021_10250 (sheet 0014, q0118 to q0120, trio of badges with a yellow exclamation circle next to the green dot and the green check)
- Evidence: wwdc2021_10275 (sheet 0025, q0218 to q0221, the field alternates between a red outline with a specific message right below and a neutral outline with no message)
- What this teaches about building interfaces: the warning lives next to the control that generated it and says what is out of range, not just that something failed. Yellow separates the "attention" state from the red of error and the red of destruction, three meanings that should not share the same color.

## Hands and physical devices enter the frame, instead of a pure screen capture
- Evidence: wwdc2020_20022 (sheets 0004, 0005 and 0007, framing with hands and device in the three creation apps; sheet 0005, q0038 to q0040, the model on the tablet, the laser cutting machine and the resulting pieces in hand)
- Evidence: wwdc2020_10640 (sheet 0032, q0284 and q0285, a real photo of a hand on a trackpad overlaid on the corner of the iPad screen)
- Evidence: wwdc2021_10126 (sheet 0012, q0105 to q0107, a real demonstration of striking through text with the pen, with the stroke advancing between frames)
- Evidence: wwdc2021_10278 (the physical iPhone in hand appears in seven sheets, and no frame shows a simulator screen)
- Evidence: wwdc2021_10245 (software screens in real use, held in hand, in nine sheets)
- Evidence: wwdc2020_10207 (sheet 0006, q0046, the grid of symbols on a laptop screen with a hand touching the symbols)
- What this teaches about building interfaces: input interactions only become understandable with the body in the frame. The hand gives scale to the touch target, shows occlusion and proves reach, things that a clean capture erases.

## Conceptual slides are black, with white text and almost no graphics, and the hierarchy comes from weight and opacity
- Evidence: wwdc2021_10081 (sheet 0001, q0005 to q0007, bold white title at the top left and a smaller list below with generous vertical spacing, with no graphics at all)
- Evidence: wwdc2021_10250 (sheet 0002, q0016 to q0018, the margins slide shows only the symbol between axis marks, and the scales one shows only the same symbol in three sizes)
- Evidence: wwdc2021_10278 (sheet 0004, q0028 to q0032, black background, title in the top left corner and a schematic device icon on the right, varying minimally from one principle to the next)
- Evidence: wwdc2020_10640 (the notes record hierarchy by weight and opacity instead of bullet points in the recommendation lists)
- Evidence: wwdc2021_10126 (sheet 0004, q0031 to q0034, ten items in two columns of white text on black, then numbered, then with the first three highlighted)
- What this teaches about building interfaces: when the background is black and the content is text, the only emphasis variable left is typographic. Weight, size and opacity give three levels of hierarchy without introducing color or a box, and the same slide can be reused dozens of times just by changing which line is lit.

## Intermediate transition states are captured, with translucent layers before settling
- Evidence: wwdc2020_10205 (sheet 0004, q0029 to q0032, the menu appears first translucent over the screen and then opaque; sheet 0011, q0097 to q0099, the calendar card appears semitransparent before becoming solid)
- Evidence: wwdc2020_10206 (sheet 0019, q0163 to q0165, the third Mail column appears overlaid with transparency before settling; sheet 0017, q0147 to q0153, the sidebar goes through expanded, collapsed to a thin strip, overlaid as a semitransparent layer, and hidden)
- Evidence: wwdc2021_10029 (sheet 0013, q0112 and q0113, the rotation happens across intermediate frames with motion blur, instead of a hard cut)
- Evidence: wwdc2021_10126 (sheet 0010, q0089 and q0090, the shutter button goes from translucent to solid white as recognition progresses)
- What this teaches about building interfaces: the midpoint is part of the component. Opacity and overlap communicate that the element is not yet committed, and showing the full cycle of a panel's states, instead of just open and closed, is what actually defines the behavior.

## Menus and popovers are born anchored to the control that originated them, with an arrow pointing to the exact element
- Evidence: wwdc2020_10205 (sheet 0005, q0041 to q0045, menus appearing under the add button, above the annotation bar, and next to the video editing controls)
- Evidence: wwdc2020_10206 (sheet 0007, q0057 to q0061, the event popover with an arrow to the grid block, the calendars one with an arrow only to the footer button, and the same list turning into a fixed column with no arrow or overlap)
- Evidence: wwdc2020_10200 (sheet 0002, q0010, card anchored to the base of the screen with the source app icon to the left of the address and a secondary label identifying the origin)
- What this teaches about building interfaces: the anchor is what tells where the interface came from and what it acts on. When the same content gains permanent space on the screen, the arrow disappears along with the overlap, a sign that it stopped being a response to a touch and became structure.

## Real system apps serve as proof of each abstract concept
- Evidence: wwdc2020_10175 (sheets 0012 to 0015, Calendar, Mail, Fitness, Maps, Book Store, Reminders, and the music app header identified as the large title style)
- Evidence: wwdc2020_10205 (most of the frames are real screens from Reminders, Photos, Music, Podcasts, Files, Messages, Mail, and Safari)
- Evidence: wwdc2020_10640 (sheets 0029 to 0033, spreadsheet, text document, calendar, Maps, and Control Center as case studies in the second half)
- Evidence: wwdc2021_10097 (sheet 0004, q0035 and q0036, the variants table fades over a real Mail screen with a swipe action revealed)
- What this teaches about building interfaces: the generic example proves that the rule is implementable, the real app proves that it was implemented. The transition from abstract table to real capture, done by fading within the same framing, is the gesture that ties the two layers together.

## The video is framed by identical opening and closing, and closes with a recap plus related sessions
- Evidence: wwdc2020_10200 (sheets 0001, 0005, and 0006, the same sticker composition on the laptop lid at the beginning and the end)
- Evidence: wwdc2020_10640 (sheet 0035, q0307 and q0308, the same MacBook with stickers from the opening, in two framings)
- Evidence: wwdc2020_10205 (sheet 0001, q0006 and sheet 0014, q0121, the same showcase of the three components, only changing which one is in focus)
- Evidence: wwdc2021_10081 (sheet 0012, q0100 and q0103, slide with title, call to action, and session list with the event tag to the right, then the black card)
- Evidence: wwdc2021_10184 (sheet 0007, q0055 to q0057, recap with all four items complete and then the final card)
- Evidence: wwdc2021_10278 (sheet 0013, q0110 to q0112, side panel on the left half, list growing up to the resources section, and a footer separating the session name from the event code)
- Evidence: wwdc2021_10245 (sheet 0017, q0145 to q0151, the opening presenter returns to the initial set to close, followed by the slide with two cross references)
- What this teaches about building interfaces: the close repeats the frame of the opening and gives the reader back the entire structure already covered, plus the adjacent paths. It is an exit pattern applicable to any long flow, and it uses the same list component as the persistent index, now with every item lit up.

## The presenter's set marks the role and the block, and shares the frame with the material instead of alternating by cut
- Evidence: wwdc2021_10029 (two fixed sets separate concept from demonstration, the presenter at the light desk in sheets 0001 to 0007, and the second presenter in the dark set in sheets 0008 to 0010)
- Evidence: wwdc2021_10245 (each switch between the five presenters comes with a full cut of desk, decoration, and computer in the background, never a gradual transition)
- Evidence: wwdc2021_10081 (the same desk with a row of controls reappears in almost every sheet, only the control in hand changing as the topic advances)
- Evidence: wwdc2020_10200 (a small portrait of the presenter stays anchored next to practically every mockup in sheets 0001 to 0004)
- Evidence: wwdc2021_10275 (sheet 0004, q0031, the list of six practices stacked next to the presenter's face)
- What this teaches about building interfaces: the coexistence of person and material in the same frame keeps the continuity of the explanation, and the change of set works as a chapter separator without needing a card. The text contrast has to follow the set's background, as recorded in wwdc2021_10275, where the active item is black over a light background in some sheets and white in others.

## Novelty is signaled by a green badge inside the slide itself, next to the item it refers to
- Evidence: wwdc2020_10175 (sheet 0017, q0145 to q0148, circular green "NEW" badge in the corner of the card, with the text revealed line by line; it reappears in sheets 0010 and 0016)
- Evidence: wwdc2020_10207 (sheet 0008, q0064 to q0067 and sheet 0017, q0146, green badge in the corner of the code frames and of the new item in the sidebar)
- Evidence: wwdc2021_10184 (sheet 0006, q0046 to q0049, "NEW" label in a green box next to the list item)
- What this teaches about building interfaces: the novelty marker stays attached to the item, never on the block's title, which allows mixing new and old items in the same list without ambiguity. Saturated green in a small field is enough and does not compete with the content.

## The limitation is stated within the material itself, instead of being omitted
- Evidence: wwdc2020_10175 (sheet 0017, q0145 to q0148, the macOS card adds the sentence about the lack of support for Dynamic Type)
- Evidence: wwdc2021_10278 (sheet 0011, q0091 to q0093, in the comparative table the lack of support is an empty cell, and the basic class only has a mark in the first column)
- Evidence: wwdc2020_10207 (sheet 0013, q0109 to q0117, comparison of old and new names with a red caption under the deprecated forms, and a section dedicated to deprecated names in the details panel)
- Evidence: wwdc2021_10126 (sheet 0002, q0013 to q0018, the carousel onboarding is built screen by screen precisely to be discarded right after)
- What this teaches about building interfaces: showing what does not work, what has been deprecated, and what does not exist in a given version is part of the component's documentation. An empty cell in a table communicates absence better than an X, because it does not compete with the disapproval vocabulary used in the right-and-wrong pairs.

## The physical past is used as an anchor for the digital concept
- Evidence: wwdc2020_10175 (sheet 0003, q0022 to q0027, hands leafing through an 18th century copy with small-caps captions, then the pair of letters in two point sizes and the same letters over a pixel grid; sheet 0011, q0091 to q0094, photographic background of rusted metal type on the card about leading)
- Evidence: wwdc2021_10245 (sheets 0001 to 0003, beige computer with two drives, integrated keyboard, phosphor green screen with a blinking cursor, the original Macintosh with a four-label menu bar, and the original iPhone with the slide to unlock strip)
- Evidence: wwdc2020_20022 (sheet 0003, q0024 and q0025, pencil sketches with technical costume notes next to the character figures, followed by the finished illustration)
- What this teaches about building interfaces: terms inherited from print, like leading and point size, become clear when the source object appears. The same logic applies to justifying why an old convention still holds, by showing the entire line instead of just the current state.

## Large isolated numbers over a plain background work as a pause and emphasis between blocks
- Evidence: wwdc2020_10206 (sheet 0006, q0047, the increase figure enters as an isolated typographic element with a smoke effect, outside any interface)
- Evidence: wwdc2021_10097 (sheet 0006, q0050, the symbol count in large typography over the same dotted background as the previous grids)
- What this teaches about building interfaces: a piece of data that supports an entire argument deserves to occupy the whole screen alone. Reusing the previous block's background keeps the visual continuity while completely changing the density.

## A chart with labeled axes is used to justify a design decision, not just to report data
- Evidence: wwdc2020_10175 (sheet 0008, q0071 and q0072 and sheet 0009, q0073 to q0075, tracking curve with size and spacing axes, background areas by zone, and the evolution from two labels with a single cutoff to one continuous label with two marked limits)
- Evidence: wwdc2021_10278 (sheet 0005, q0040 to q0044, the QuickLook of the haptic file with an orange intensity curve and blue vertical bars, plus callouts labeling the two event types; sheet 0010, q0090, dozens of bars very close together contrasting with the three sparse events of the other asset)
- What this teaches about building interfaces: when the system's curve appears, the specific value stops looking arbitrary. And using the same visualization for two different files turns density into an immediate comparison, without needing a number.

## A hidden control is replaced by a named control, and the primary action never enters the secondary menu
- Evidence: wwdc2020_10205 (sheet 0007, q0059 to q0062, the compose icon stays isolated in the top right corner, outside the menu, while select, pin, and edit stay grouped inside the secondary menu)
- Evidence: wwdc2021_10126 (sheet 0023, q0204 to q0207 and sheet 0024, q0209 to q0213, the ellipsis icon in the corner of the card gives way to an inline green text button, and the menu it opens goes on to list complete phrases with icons of different weight)
- What this teaches about building interfaces: visibility is the decision, not the icon's aesthetics. What the person does all the time stays exposed and labeled, the rest gets grouped, and within the grouping the complete text matters more than the icon when the consequence of the action is not obvious.

## Findings from a single source

- Hit target drawn as a dashed frame larger than the visible icon, with the frames showing the outline first offset and then coinciding with the drawing, and two neighboring icons coming to share one continuous dashed band with no gap between them. Reference: wwdc2020_10640 (sheet 0010, q0082 to q0085; sheet 0018, q0160 and q0161).
- The pointer's magnetism algorithm gets its only graphic representation as a spiral of dashed turquoise dots in concentric circles over the home screen, which disappears in the next frame with the pointer already fixed on the icon. Reference: wwdc2020_10640 (sheet 0013, q0109 to q0111).
- Anatomy of the pointer's lift effect as an exploded diagram in three dimensions, with the layers named and revealed progressively, first specular reflection and element, then radiosity and shadow. Reference: wwdc2020_10640 (sheet 0015, q0130 and q0131).
- Anchor point of the pointer's shape marked by a yellow dot, placed on the lower tip of the eyedropper, outside the geometric center, and then in the exact center of a circle, comparing the two choices in consecutive frames. Reference: wwdc2020_10640 (sheet 0026, q0232 and q0233).
- Black-to-white gradient bar used as a contrast scale to choose the pointer's material, with a circular marker that changes position between frames next to the same button with and without background. Reference: wwdc2020_10640 (sheet 0022, q0191 and q0192).
- Optical alignment documented with negative margin: the progressive zoom on the folder icon shows the right guideline entering inside the drawing, and the badge exceeding the outline on the icon stack. Reference: wwdc2020_10207 (sheet 0010 up to q0084; sheet 0011, q0091 to q0093).
- Destructive button positioned above the neutral button on the confirmation sheet, never beside it, shown in two apps in the same two-step sequence. Reference: wwdc2020_10205 (sheet 0008, q0068 to q0072; sheet 0009, q0076 and q0077).
- Direct numeric entry replacing the spinning wheel: keyboard of large square keys below the time field, and the month and year picker turning into a scrollable two-column list with the center item larger and bold. Reference: wwdc2020_10205 (sheet 0011, q0091 and q0094).
- Confirmation by tapping outside the field shown as a pair of frames with no intermediate step: the blue outline box around the value disappears and the date turns into plain text. Reference: wwdc2020_10205 (sheet 0012, q0102 and q0103).
- Idle space measured in proportion: the toolbar with a few small icons and a lot of negative space around it, followed by the recommendation card and the same screen with the buttons repositioned closer to the content. Reference: wwdc2020_10206 (sheet 0026, q0226 to q0230).
- Density progression shown in three steps on the same home screen, from a spaced grid to a full grid and then with widgets in place of part of the icons, and the file manager going from large icons to much smaller icons with many more items visible. Reference: wwdc2020_10206 (sheet 0005, q0038 to q0043).
- Inline renaming inside the file grid itself contrasted with the classic modal centered over darkened content, with a thumbnail, a focused field and the keyboard occupying the bottom band. Reference: wwdc2020_10206 (sheet 0006, q0054; sheet 0007, q0055 and q0056).
- The thesis that the browser's frame should disappear is staged literally: the window from the 1990s, with menus and a URL field, keeps losing content and contrast until only an almost empty gray rectangle with a narrow bar on top remains. Reference: wwdc2021_10029 (sheet 0002, q0010 to q0012).
- The variation of a system measurement is converted into a visual gradation, three identical devices with the same screen covered by a green layer of increasing opacity, a resource that the speech expresses only in words. Reference: wwdc2021_10029 (sheet 0012, q0102).
- Fixed proportion explained in three registers within the same block: measurement rulers over the photo, a card that turns into a square and then grows in height to fit the content appearing at four widths, and geometric diagrams with lists of equivalent declarations. Reference: wwdc2021_10029 (sheet 0021, q0183 and q0184; sheet 0022, q0194 to q0199; sheet 0023, q0202 to q0207).
- Spacing between flexible items demonstrated by three states of the same navigation bar, items stuck together, items breaking into two lines, and items evenly spaced once the declaration enters the code. Reference: wwdc2021_10029 (sheet 0024, q0214 to q0216).
- Comparative grid of white cards labeled one by one to display the entire set of redesigned native controls at once. Reference: wwdc2021_10029 (sheet 0025, q0224 and q0225).
- Localization treated as a parametric system and not as translation: the same structure of cell, book, speech bubble, letter with a superscript and letter in a frame, repeated with the Latin letter and with the Thai one, and then in a dense grid covering seven scripts. Reference: wwdc2021_10097 (sheet 0006, q0053 and q0054; sheet 0007, q0055).
- Layer opacity annotated in number over the symbol itself, with a labeled pair bringing the percentages above each icon, contrasted with the monochrome version. Reference: wwdc2021_10097 (sheet 0014, q0119 and q0120).
- Comparison of close hues made with two large circles and the name below, to separate colors that get confused with each other in the catalog. Reference: wwdc2021_10097 (sheet 0015, q0131 and q0132).
- Choice between static and variable configuration translated into visible quantity: the dot diagram goes from nine dots per line to three, with the vertical guides repositioned. Reference: wwdc2021_10250 (sheet 0006, q0049 to q0051).
- Interaction between layers explained with a diagram of three overlapping circles comparing the behavior that blends at the intersection with the one that clears what is behind, overlaid on the icon itself before being isolated in full screen. Reference: wwdc2021_10250 (sheet 0012, q0106 to q0108).
- Path order problem demonstrated by coloring each path a different color and numbering the points, with the internal outlines revealing that the two drawings do not coincide. Reference: wwdc2021_10250 (sheet 0009, q0073 to q0078).
- Distribution decision flowchart with columns of minimum system version pointing to the compatible template boxes, one column pointing to both and two pointing only to the newest one. Reference: wwdc2021_10250 (sheet 0018, q0154 to q0159).
- The app's camera drawn as a target and not as an instruction: dark overlay, dashed outline in the shape of the object being searched for, short centered text and a shutter that goes from translucent to solid as recognition progresses, with the text switching from searching to framing instruction. Reference: wwdc2021_10126 (sheet 0010, q0089 and q0090; sheet 0011, q0094 and q0095).
- Confirmed feedback at a scale larger than the control itself: the small heart in the corner of the photo gives way to a large filled heart in the center of the image, with a short caption of consequence. Reference: wwdc2021_10126 (sheet 0013, q0109 and q0110).
- Gesture hint given by partially visible content, with cropped thumbnails appearing at the left and right edges of the main photo and changing content between frames. Reference: wwdc2021_10126 (sheet 0014, q0120 to q0123).
- Search field with concrete examples of ingredient and place in place of generic text, presented with the red marker only on the discarded version. Reference: wwdc2021_10126 (sheet 0010, q0085).
- Visual glossary of standard gestures in a three-by-two grid, with abstract blue symbols on black and a text label below each one. Reference: wwdc2021_10126 (sheet 0012, q0102).
- Row of three pillar icons used as a focus device: the icons at the ends fade and the one in the center is replaced by a real screenshot, marking the passage from abstract concept to concrete example. Reference: wwdc2021_10184 (sheet 0003, q0019 and q0020).
- Distance zones annotated as luminous concentric rings around the speaker, with numbered markers over the line between the two devices and a zoom revealing the list of parameters that vary by zone, among them banner position and scale, background blur, haptic strength, device light and audio. Reference: wwdc2021_10245 (sheet 0009, q0078 to q0081).
- The same interface space changes function according to distance without changing position: the directions button with distance and time turns into the find button when the target is close, keeping the pair of buttons in the same place on the card. Reference: wwdc2021_10245 (sheet 0006, q0048 to q0052).
- Background color as the sole carrier of state on a minimalist screen: the same structure of a central arrow and distance line alternates between neutral dark background and solid green to mark alignment with the right direction. Reference: wwdc2021_10245 (sheet 0012, q0101 and q0102; sheet 0016, q0138 and q0139).
- Illustrative graphic overlay that is not a screenshot: the cone of green light coming out of the top of the phone toward the sofa, created to communicate the idea of the screen lighting up. Reference: wwdc2021_10245 (sheet 0007, q0060).
- Negative example shown as a list in which all audio destinations have the same visual weight, regardless of being near or far, with the current device marked only by a selection icon. Reference: wwdc2021_10245 (sheet 0014, q0120).
- White balloons with a triangular tip overlaid on the real screenshot bringing in quotation marks what the screen reader would announce for that specific element. Reference: wwdc2021_10275 (sheet 0015, q0132 and q0135).
- Form structure revised from fixed role fields to repeatable fields with a role selector next to the name and an add member button. Reference: wwdc2021_10275 (sheet 0011, q0092 to q0098).
- Content adaptation by region and not just translation: the recipe cards go from translated Western dishes to local dishes and a festival section appears that did not exist before. Reference: wwdc2021_10275 (sheet 0020, q0173 to q0178).
- Translucent material stacked over translucent material in Control Center, with the text size panel over the accessibility shortcuts panel and the finger trace visible. Reference: wwdc2021_10275 (sheet 0016, q0138 to q0140).
- A single panel frame reused for completely different categories in character creation, colored header, grid of square blocks, highlight outline on the chosen option and back button, serving the same way for skin tone, hairstyle and voice language. Reference: wwdc2021_10275 (sheet 0027, q0241 to q0243).
- Gender treated first through typography, with a list of terms in large type each in a color from the green-to-magenta gradient, and only afterward as a component, comparing three fixed options with a free text field with a clear button and a privacy toggle. Reference: wwdc2021_10275 (sheet 0008, q0068 and q0069; sheet 0026, q0231 to q0233).
- Specification organized by sensory channel in three parallel lines, visual, haptic and audio, each with a colored badge naming the corresponding file, revealed in stages and then duplicated to compare alternative assets. Reference: wwdc2021_10278 (sheet 0006, q0052 to q0054; sheet 0007, q0055 and q0056).
- On-screen virtual controller as a translucent panel over the game, with a gray left stick, a larger orange right stick, action buttons as small translucent circles with the letter centered and a thin progress bar at the base, running through variations of position, size and shape between frames. Reference: wwdc2021_10081 (sheet 0006, q0047 to q0051).
- The same instruction written twice on the slide changing only the button symbol embedded in the middle of the sentence, to prove that the glyph needs to match the real control. Reference: wwdc2021_10081 (sheet 0004, q0035).
- Video call grid with a city and country caption at the bottom corner of each participant serving as the structure for the entire video, with the frame alternating between several participants and one highlighted at the moment of reaction. Reference: wwdc2020_20022 (sheets 0001, 0002 and 0006, q0007 onward and q0047 to q0054).
- Bridge between digital design and physical piece in three consecutive frames, manipulating the model on the tablet, cutting machine in operation and hands holding the resulting pieces. Reference: wwdc2020_20022 (sheet 0005, q0038 to q0040).
- Nearly absent interface as a deliberate choice in the drawing app, a screen full of color with a few icons in the corners and no visible controls, leaving the entire frame for the gesture with the pen. Reference: wwdc2020_20022 (sheet 0007, q0058 to q0060).
- Suggestion entry point captured at both origin and destination as a pair of screens in sequence, the conversation with the address and the map already with the same address filled in. Reference: wwdc2020_10200 (sheet 0001, q0009 and q0010).
- Substitution in the same position on the home screen: the stack of generic widgets paginated by dots gives way to a dedicated widget listing the next two classes, taking up the width of two icons. Reference: wwdc2020_10200 (sheet 0004, q0033 and q0034).
- Automation involving more than one app represented in a single card line, with two app icons side by side before the trigger and action text. Reference: wwdc2020_10200 (sheet 0005, q0041).
- Two-column typographic table with the same sample sentence repeated from 12 to 26 points and the row of the active size highlighted in white while the others stay gray, with the highlighted row moving up between frames. Reference: wwdc2020_10175 (sheet 0002, q0013 and q0014).
- Preserved ligature and disassembled ligature shown on the same word under the failed and passed stamps, proving the side effect of changing letter spacing in code. Reference: wwdc2020_10175 (sheet 0010, q0082).
- Line-height adjustment table in points with columns for standard, tight and loose values and one row per platform, next to the screenshot of the development environment panel with the option to optimize the interface highlighted in blue. Reference: wwdc2020_10175 (sheet 0014, q0125 and q0126; sheet 0017, q0151 to q0153).
