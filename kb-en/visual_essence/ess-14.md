# ess-14

Video batch. Sources: wwdc2026_322 (13 frame sheets) and wwdc2026_8012 (43 frame sheets).

## The current state is marked by weight and color, and everything that isn't the focus fades

- Evidence: wwdc2026_322 (sheet 0004, q0029, q0030 and q0033; sheet 0009, q0074, q0079 and q0080; sheet 0012, q0107: active list item in bold white and the rest in faded gray, with the highlight advancing from item to item)
- Evidence: wwdc2026_322 (sheet 0010, q0082 to q0083 and q0084: the transcript goes from uniform bold across all lines to only the first in bold black and the others in light gray)
- Evidence: wwdc2026_8012 (sheets 0002 and 0003, q0022 and q0023: selected line in the layer tree with blue highlight and the corresponding element in the canvas with a blue outline; sheet 0021, q0181 and q0186 to q0188: Blend Mode menu with a checkmark on the active item and blue highlight on the item under the cursor)
- What this teaches about building interfaces: selection and focus don't need a label, two variables already available are enough, font weight and saturation, applied consistently. And the highlight always comes together with the demotion of the rest, not alone.

## Parameter and result live in the same frame, and the difference is visible between neighboring frames

- Evidence: wwdc2026_322 (sheet 0004, q0031 to q0032: the gradient cover goes from sharp to blurred when the blur modifier with radius 30 enters the code; sheet 0008, q0067 to q0068 and q0070 to q0072: first wavy blotches when the offset calculation enters, then wider, more contrasted blotches with the second sample shifted; sheet 0011, q0095 to q0096 and q0097: the value in the closure changes from base to top and the label in the isometric diagram changes position)
- Evidence: wwdc2026_8012 (sheet 0005, q0037 to q0042: the cursor moves across the refraction control and the icon's petals go from smooth edges to increasingly wavy edges; sheet 0006, q0046 to q0048: the shadow's Chromatic sub-item is edited while the glow around the edges becomes more visible)
- What this teaches about building interfaces: whoever adjusts a value needs to see the effect without switching screens or waiting. Placing control and result in the same field of view turns an abstract parameter into an observable relationship.

## The label on screen carries vocabulary the speech doesn't say

- Evidence: wwdc2026_322 (sheet 0003, q0019 to q0024: the pipeline boxes carry step names like "Shader effects" and "Timeline input", technical captions absent from the narration in that section)
- Evidence: wwdc2026_8012 (sheets 0002 to 0007: the images show the exact names and fixed order of the inspector fields, which the speech treats in general terms; sheet 0007, q0055 and q0056: floating appearance panel with a light and dark toggle, a tint switch and a gradient bar, a component the narration doesn't describe)
- What this teaches about building interfaces: visible naming is the product's real documentation. If the field name is wrong or vague, no verbal explanation around it fixes it, because the label is what the person will repeat later.

## The same artifact is shown inside several frames, side by side or in sequence

- Evidence: wwdc2026_322 (sheet 0012, q0104: the final screen with transcript, timestamp and controls appears replicated on iPad next to the iPhone)
- Evidence: wwdc2026_8012 (sheet 0006, q0049 to q0054: the same icon in a rounded square frame, circular frame, back to square, a colored version on a dark background and a monochrome version on a light background; sheet 0040, q0356 to q0359: the maps app icon as a square with a circular cut guide, then as a full circle with the marker recentered, then back to the square)
- What this teaches about building interfaces: a component is only ready when it survives more than one crop. Testing the same piece in different frames reveals early what depends on the framing and what needs to be recentered.

## Effect and property belong to a level of the hierarchy, and the difference in level is taught graphically

- Evidence: wwdc2026_322 (sheet 0005, q0043 to q0045, against sheet 0006, q0049 and q0050: the per-pixel effect connects an input point to an output point, while the layer effect bounds a larger square of sampled region connected by an arrow to an output pixel; sheet 0010, q0087 to q0089: two orange rectangles labeled view container and subview gain a shared central dotted line)
- Evidence: wwdc2026_8012 (sheet 0003, q0022 to q0027: with the group selected the inspector shows the glass section with mode, specular, blur, refraction, translucency and shadow; with the layer selected it shows opacity, blend, fill, the switch that decides whether that layer receives the effect, the source image and the layout)
- What this teaches about building interfaces: deciding what level each property lives at is an architecture decision, not a panel decision. Material and effect at the group level, color and participation at the layer level, and the interface should make that boundary obvious by changing what it displays according to the selection.

## The annotation is overlaid on the object itself, not placed as a caption beside it

- Evidence: wwdc2026_322 (sheet 0005, q0041 to q0045: yellow label boxes and arrows connecting the input pixel to the output pixel directly over the blue pixel grid; sheet 0010, q0088 and q0089: dotted alignment line drawn over the two rectangles; sheet 0011, q0093: orange top and base labels touching the subview in perspective)
- Evidence: wwdc2026_8012 (sheet 0040, q0356: dashed circular guide drawn over the square icon to indicate the crop area; sheets 0002 to 0006: blue selection outline drawn around the element in the canvas)
- What this teaches about building interfaces: measurement, boundary and crop area should be drawn on top of the element, at its own scale. A separate caption forces the eye to go back and forth and loses the exact correspondence.

## The framing closes in on the detail to inspect material and finish

- Evidence: wwdc2026_322 (sheet 0003, q0026 to q0027: a dark circular vignette frames the result preview and closes in further between one frame and the next; sheets 0002 and 0003: circular lenses attached to the pipe show a thumbnail of the content at that exact point in the flow)
- Evidence: wwdc2026_8012 (sheet 0004, q0031, and sheet 0006, q0046 to q0048: the canvas zoom goes well above natural size to check the selection outline and shadow glow on the edges of the petals)
- What this teaches about building interfaces: magnification here is a checking instrument, not a navigation one. Edge, glow and shadow detail need their own inspection scale, larger than the scale of use.

## Translucency and blur only appear over genuinely colored content

- Evidence: wwdc2026_8012 (sheet 0007, q0057 to q0058: the canvas background switches from solid gray to a colored gradient image filling the whole area, and the icon starts showing the background's refraction through the material, with the toolbar gaining extra preview controls; back to gray at q0061)
- Evidence: wwdc2026_322 (sheet 0012, q0100 to q0102: the translucent playback controls sit over a colored gradient background with the transcript overlaid; sheet 0004, q0032: the blur is demonstrated over the gradient cover image, not over a flat surface)
- What this teaches about building interfaces: translucent material is invisible against a neutral background. The valid test is against the real, varied content that will pass underneath, and it's worth having that background available in the tool itself.

## The context switch is signaled by an explicit transition, fade or neutral screen

- Evidence: wwdc2026_322 (sheet 0001, q0004; sheet 0002, q0011; sheet 0004, q0034; sheet 0012, q0108: empty white screens separate blocks)
- Evidence: wwdc2026_8012 (sheets 0002, 0007, 0021 and 0022: in the first block's four screen entries and exits the presenters appear partially transparent behind the enlarged icon; sheet 0028, q0244 to q0247, and sheet 0030, q0264 to q0267: the question card enters and exits by gradual fade, visible frame by frame; sheet 0040, q0359: exit by simple fade)
- What this teaches about building interfaces: a context change deserves its own frame. A short intermediate state, neutral or semi-transparent, avoids the hard cut that makes the person lose track of where they came from.

## Each part gets its own name, and the naming is the visible structure

- Evidence: wwdc2026_322 (sheet 0002, q0016 to q0018: the input pipe labeled as original interface opens into three outputs with its own preview; sheet 0003, q0019 to q0024: each pipeline box names the transformation it applies)
- Evidence: wwdc2026_8012 (sheets 0002, 0003, 0004 and 0006: layers named one by one inside nested groups, with indentation marking the level; sheet 0040: the maps app file's layers are named by function and destination, with suffixes indicating the watch variant)
- What this teaches about building interfaces: readable hierarchy comes from specific names plus indentation, not from icons. A name that states function and destination lets you understand the file without opening each layer.

## The same structure repeats without variation from start to finish, and that's what makes reading cheap

- Evidence: wwdc2026_322 (sheets 0002 and 0003: notation stable throughout the whole video, circular lens equals data state, rectangular box equals transformation, Y fork equals branch, X crossing equals merge; sheets 0004, 0006 to 0010: always a code block on one side and an iPhone mockup on the other)
- Evidence: wwdc2026_8012 (sheets 0002 to 0007, 0021, 0022 and 0040: always the same three-panel layout, layer tree on the left, canvas in the center, inspector on the right, in every sheet where the app appears)
- What this teaches about building interfaces: fixing the template and changing only the content makes the reading cost drop with each repetition. The graphic vocabulary works like an API, it changes in value but never in form.

## The explanation is built by addition, one element entering at a time

- Evidence: wwdc2026_322 (sheet 0010, q0087 without the alignment line, q0088 and q0089 with it; q0085 to q0086: dark gray timestamp boxes appear above each text block; sheet 0011, q0093: the orange top and base labels only appear there; sheet 0004: the topic list grows from three to five items over the course of the video; sheet 0005, q0041 to q0042, and sheet 0006, q0047 to q0048: the light blue syntax highlight moves across the three shader signatures one at a time)
- Evidence: wwdc2026_8012 (sheet 0005, q0043 to q0045: the translucency value box enters edit mode while the icon stays stable; sheet 0007, q0058: the toolbar gains extra preview controls along with the test background; sheet 0003, q0021, and sheet 0004, q0030: the dropdown menus reveal the closed set of options only when opened)
- What this teaches about building interfaces: never show the complete diagram at once. One layer of information per step, with the rest of the frame held still, gives time to connect each new element to what was already there.

## Single-source findings

- Syntax highlight palette used in all code blocks: comment in gray, string in red or orange, parameter and types in purple, function name in green (wwdc2026_322, sheets 0004 and 0006 to 0010).
- Paired, labeled code, one side SwiftUI and the other Metal, showing the same feature in both languages in the same frame (wwdc2026_322, sheets 0006 and 0007). On sheet 0008 the pair disappears and only the Metal block remains, and on sheets 0009 and 0010 it goes back to being only SwiftUI.
- Pixel grid in shades of blue labeled as input and output, with arrows connecting one side to the other, used to distinguish shader types: in one pair what is annotated is position at the input and color at the output, in another there are two different positions connected by crossed arrows (wwdc2026_322, sheet 0005, q0041 to q0045).
- Noise texture opened into three channel thumbnails labeled R, G and B, each with a white dot marking the sampling position and a scale bar from zero to one below it; between two frames the dot changes position in all three channels at the same time (wwdc2026_322, sheet 0008, q0064, q0065 and q0067).
- Metaphor explained as a physical object rather than a diagram: 3D metal piping with joints, a glass and chrome flow meter labeled "BYTES" and a red valve at the opening, and a real pipe wrench next to an iPhone on wood at the close (wwdc2026_322, sheet 0001, q0007 and q0008; sheet 0013, q0109 to q0114).
- Alignment explained in two phases, first in two flat rectangles and then the same relationship in isometric perspective with colored anchor points (wwdc2026_322, sheet 0010, q0090, and sheet 0011, q0091 to q0093).
- Two-dimensional refraction control, a two-dimensional field with two percentage values alongside it, instead of two separate sliders (wwdc2026_8012, sheet 0005, q0037 to q0042).
- Deliberately short, closed option sets: fill with automatic, solid, gradient, system light and system dark (wwdc2026_8012, sheet 0003, q0021); specular with off, automatic, internal and outline (sheet 0004, q0030); blend with ten modes in a vertical list (sheet 0021, q0181).
- Floating appearance panel over the canvas bringing together the light and dark toggle, a tint switch and a horizontal rainbow gradient bar with a cursor to pick the color (wwdc2026_8012, sheet 0007, q0055 and q0056).
- Standardized audience question card: rounded-corner rectangle, semitransparent dark background, white text left-aligned in the bottom third, author name in bold and vote count in green alongside it (wwdc2026_8012, sheets 0008, 0010, 0012, 0017, 0020, 0024, 0025, 0027, 0029, 0030, 0033 to 0035, 0039 and 0041).
- Conversation set instead of a stage: curved light wood table, a panel of vertical slats in the background with an illuminated sign, table microphones and open laptops in front of each participant, with the camera alternating between a wide shot of the five and shots of two or of one (wwdc2026_8012, sheet 0001 onward).
- Closing with a logo watermark and a copyright notice in small centered text over the panel image (wwdc2026_8012, sheet 0043, q0380 to q0381).
- Very low demonstration ratio in the panel format: out of 43 sheets, only nine show the app interface, and the notes record long stretches in which the speech covers visual topics like blend modes, contrast and layers with nothing corresponding on screen (wwdc2026_8012, sheets 0023, 0026, 0031, 0032, 0036 to 0038 and 0042).
- In the technical session format there is no live tool demonstration at any point, only static code next to the already rendered result (wwdc2026_322, visual proportion observation).
