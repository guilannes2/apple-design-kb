# wwdc2025 (part 1)

## Create icons with Icon Composer (id: wwdc2025_361, 14.6 min)

- Basis: transcript and 17 of 17 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/361/.
- Central thesis: Icon Composer is the tool that consolidates, in a single file, the creation of app icons with Liquid Glass for iPhone, iPad, Mac and Watch, eliminating the need to export dozens of sizes and variations manually.

The design process Apple describes:
1. Draw in the software of your choice (one that exports SVG is recommended, for scalability), using one of the icon templates from Apple Design Resources (Figma, Sketch, Photoshop, Illustrator).
2. Organize the art into layers, thinking in terms of Z depth: background at the base, elements stacked above. Separating colors into distinct layers gives more control later.
3. Keep the art "reduced to its graphic essence": flat, opaque, easy to control, because effects like blur, shadow, specular, opacity and translucency are applied later, inside Icon Composer, as Liquid Glass properties, and should not be "baked" into the source art.
4. Export layers as SVG (text needs to become outline, since SVG does not preserve fonts); use PNG only for custom gradients, raster images or whatever cannot be expressed in SVG. Never export the clipping mask (rounded rectangle or circle), since it is applied automatically afterward.
5. Import into Icon Composer, adjust appearance (default, dark, mono, and the derived clear/tinted variants), platforms and glass properties.
6. Export the .icon file and drag it into Xcode.

Principles stated and why:
- One artwork, four platforms: gives the app a consistent identity wherever it appears.
- Groups control how elements stack and receive glass properties; the limit is up to four groups per icon, because Apple concluded that this number already covers the visual complexity appropriate for an icon.
- Some properties (opacity, blend mode, fill) are configurable per appearance (light/dark/mono); others apply to all, for being more consistent across modes.
- Legibility in mono: at least one element of the icon must stay white (usually the most recognizable one), and the remaining colors mapped to shades of gray; the automatic conversion exists, but needs to be adjusted for the best contrast.

Concrete interface-building techniques:
- 1024px canvas for iPhone, iPad and Mac (unified in this update); Watch uses 1088px, which "goes beyond" the rounded rectangle, but follows the same grid, making translation between platforms easier.
- Specular highlight: automatic edge treatment applied even to icons submitted as individual images (without going through Icon Composer).
- Six testable appearances: Default, Dark, Clear light, Clear dark, Tinted light, Tinted dark (renamed this year to default, dark and mono, with clear and tinted derived automatically from the art).
- Neutral shadows (preset) versus chromatic shadows: use chromatic when the color over a white background can "leak" into the background, creating an effect of light and material physicality; it is possible to keep a neutral shadow in dark/mono by creating a variant.
- Optical adjustments when migrating from the rounded rectangle to the Watch circle: elements touching the edge of the canvas need to be scaled to touch the edge again, or the designer can draw with "bleed" (bleed) already in mind.
- Preview panel allows changing the background (to simulate context and test legibility over wallpapers), overlaying icon grids and seeing how light moves.

Examples cited:
- Messages: example of a simple icon, one foreground and one background.
- Home: uses the four available groups, each layer as a single piece of glass.
- Translate: the speech bubbles and the text are separated into distinct layers to allow blur on the overlap, a subtle shadow and, in dark mode, swapping just one fill.
- Calendar (the day number): illustrates the problem of specular becoming "pillowy" (puffed up) in narrow areas; solved by turning off the specular on the group or the glass on the layer.
- Dictionary: without a fill adjustment, the page marker disappears against black in dark mode; the solution is to change the fill.
- Siri: example of a common mistake, exporting the layer with the clipping mask already applied, when it should be left out of the exported file.

Short quotes:
"It's the same tool we used this year to update all our own icons."
"Icon Design is moving from a past of simply static images to a future of expressive, multi-layered artworks."

<!-- visual:wwdc2025_361 -->
### What the images show
Basis: 17 of 17 frame sheets viewed, all codes checked.
- The screen annotates the Watch canvas measurement with a blue label over a vector selection with resize handles, reading "1088 x 1088", on top of a square with a grid of concentric circles and guide lines (sheet 0006, q0046). The same type of construction grid appears open inside two different design applications, one light with a layers panel on the left and Design/Prototype tabs, the other dark with a layers panel on the right and the "App Icon Template" layer highlighted in red (sheet 0005, q0041 and q0042).
- The Icon Composer interface gets an annotated tour with arrows and text labels naming each region: "Sidebar" pointing to the layer list, "Preview panel" pointing to the central icon and "Inspector" pointing to the properties panel (sheet 0009, q0074 to q0076; sheet 0011, q0092). The bottom bar of the canvas is annotated in two sections, "Platforms" on the left and "Appearances" on the right (sheet 0010, q0087 and q0088).
- The anatomy of the inspector appears field by field, with legible numeric values. In one layer's panel are Color, Opacity 100%, Blend Mode Normal and Fill Automatic, plus Composition with Visible, the image "4_House.svg" and Layout in X, Y and scale 100% (sheet 0011, q0091 and q0092). In the group panels, the Liquid Glass section brings Mode Individual, Specular on, Blur 50%, Translucency 60% and Shadow Chromatic 100%, with Composition showing Visible and Layout (sheet 0011, q0099; sheet 0012, q0101; sheet 0014, q0123). Each section carries a scope label next to the title, "Default" or "All", saying whether the property applies to one appearance or to all.
- The difference between two frames shows the change in control granularity: at the layer level Liquid Glass is a single "Effects" toggle, and from q0098 to q0099 the same panel opens into five separate fields at the group level (sheet 0011). A floating context menu next to the Shadow field explicitly offers "Vary for Default" and "Vary for iOS / macOS" (sheet 0012, q0104).
- The Z depth is drawn as an isometric illustration of sheets stacked diagonally, pasted next to the real layer list, and the pair of frames contrasts the two possible organizations: four house layers inside a single group (q0084) against the same four distributed across four separate groups (q0085), with the isometric stack growing along with it (sheet 0010).
- The export naming is shown literally in a row of thumbnails over a checkered transparency background, numbered in layer order from "0_Background.svg" to "4_Glyph.svg", each one showing the art of its layer (sheet 0008, q0066). Next to it, two "A" glyphs with the one on the right selected showing a blue outline and square anchor points on the stems, illustrating the conversion of text into a vector outline (q0067).
- A visual catalog of four types of layer content pairs a generic example with a real app icon for each category: mesh gradient, illustrative, 3D modeled and photographic (sheet 0008, q0069 and q0071).
- Appearance pairs isolate one variable at a time, always with the icon rendered next to the panel and a badge below: Neutral shadow on the Phone icon against Chromatic shadow on the heart icon, then the same chromatic shadow gaining the extra line "Dark: Neutral" with the badge changing from "Default" to "Dark" (sheet 0013, q0109 to q0111).
- The case of fill per appearance appears in three consecutive frames of the same "Aa" icon: light background with a "Default" badge, the same icon over black with a "Dark" badge and the color swatch apparently unchanged, and then the swatch swapped for a visibly more vivid red (sheet 0013, q0113 to q0115). Right after, the Composition panel shows two files associated with the same layer, one default and one "loupe-dark.png" for dark mode only (q0116).
- Color variations of the same Weather icon are arranged in horizontal rows under platform labels, always over a black background: six tones in the "iOS iPadOS" row with an isolated blue icon below (sheet 0002, q0017 and q0018), then a second row of six for "macOS" with an isolated circular icon underneath, this one without a legible label (sheet 0003, q0019), and in a following frame one more row with a circular icon next to the text "watchOS" (q0021).
- The floating appearance panel shows the concrete controls: a Light/Dark toggle and a "Tinted" switch with a colored gradient bar (sheet 0010, q0089) and, in the next frame, "Dark" selected, "Tinted" turned on and two sliders, one rainbow and the other grayscale (q0090), all applied to three instances of the same house icon over a white, black and purple background.
- The same house icon is set against seven different backgrounds in sequence, changing only what is behind it: solid olive green, nebula gradient, ice texture, tulip photo, orange fabric, water with a butterfly and patterned light gray; the icon goes from opaque to translucent and takes on the tone of each background (sheet 0015, q0127 to q0133). Two extreme close-ups that follow reveal the glass's shine and edge and fragments of a grid of house shapes around it (q0134 and q0135).
- A list of four steps overlaid on the presenter's video works as a recurring progress marker, always with the current step in white or black and bold and the others in dim gray: "Deliver" highlighted on sheet 0005 (q0038), "Export layers" on sheet 0007 (q0062), "Icon Composer" on sheet 0008 (q0072) and "Deliver" again at the close (sheet 0016, q0136 and q0137).
- Two examples of glass material are isolated as labeled test cards, "Blur" with a diffuse halo around it and "Shadow" with a defined shadow underneath, in white squares over a black background (sheet 0007, q0060). The layers panel of the Translate example names the elements by convention, "Glyph", "Bubble" and "Background", with the selected item in blue (q0055 and q0056).
- Grids of system icons open and close the video, first in partial crops over a light gray background (sheet 0001, q0004 to q0006) and then as two dense home screens filling the entire frame (sheet 0016, q0139 and q0141). A frame that is almost entirely black isolates a dark icon with very low contrast, nearly invisible against the background (q0138).
Visual proportion: most of the frames are icon, slide or Icon Composer interface; the presenter appears in short cuts between the demonstrations on almost every sheet, and the last sheet (0017, q0145) is just him, with a pink closing tint.
Recorded divergences or limits: the notes flag pairs of frames without a discernible visible difference (sheet 0002, q0017 to q0018; sheet 0003, q0023 to q0024 and q0026 to q0027) and a circular icon whose platform label was not clearly legible (sheet 0003, q0019), plus a frame with a "Mono" badge on an apparently empty page (sheet 0014, q0118).
<!-- /visual:wwdc2025_361 -->

## What's new in SF Symbols 7 (id: wwdc2025_337, 22.9 min)

- Basis: transcript and 16 of 16 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/337/.
- Central thesis: SF Symbols 7 introduces the Draw system, which lets symbols draw themselves along their own vector path (like calligraphy), plus gradients and improvements to Magic Replace, requiring designers to annotate their own custom symbols with guide points to enable these animations.

The design process Apple describes:
- Each symbol is drawn from a single vector point that creates a continuous path; every curve and angle needs to be deliberate, balanced and visually communicative.
- A symbol is not just a visible outline: it is built from shapes with careful contour, allowing precise control of proportions, negative space and visual weight.
- Some shapes use two distinct paths, oriented in opposite directions, which refines the appearance of each path individually and is an important piece of how they can animate.
- To annotate Draw: always start with the "regular" weight (it is the only thickness where guide points can be added/removed); the system automatically interpolates for the other two model weights (ultralight and black); you need to make sure the associated guide points stay in the same order across regular, ultralight and black (guide point numbering helps identify and correct misalignments, marked in orange when overwritten).

Principles stated and why:
- Draw was designed to be flexible: each symbol defines its own drawing direction (for example, "wind" draws from left to right to suggest movement; an Arabic character draws from right to left, following the writing direction).
- There is no single correct way to position guide points: it is trial and error, it is up to the designer to test different placements.
- Symbols support nine weights and three scales, but the designer only needs to annotate three (the system takes care of the rest).

Concrete interface-building techniques:
- Two new animation presets: Draw On (animates the symbol appearing) and Draw Off (animates it leaving), with playback options: By Layer (default, each path draws with a staggered delay), Whole Symbol (all paths start and end together) and Individually (new, draws layer by layer, waiting for the previous one to finish).
- Draw supports compound shapes, such as arrows with two shapes that behave as one, allowing the arrowhead to travel along with the path.
- Variable draw: renders the path at a specific percentage over a reduced-opacity version of the layer, useful for showing progress (download, temperature, yoga session). A symbol can support variable color and variable draw, but only one is chosen at render time (or "default", which uses the system's preferred mode).
- Magic Replace now recognizes matching enclosures between two symbols and preserves them, replacing only the different layers; it combines this with Draw Off (symbol leaving) and Draw On (symbol entering).
- Gradients: generate a smooth linear gradient from a single source color, available in system and custom colors, in all rendering modes; especially recommended for larger instances.
- Guide points: at least two per path (start point, open circle; end point, filled circle); more complex paths may need additional points, including corner points (indicated by a diamond) for curves with sharp bends.
- Attachments: an undrawn element (such as an arrowhead) associated with a guide point, dragged onto the point to "stick" and follow the path as it draws; the arrowhead needs to be a path separate from the base to allow this.
- Adaptive end caps: by default paths draw with a rounded tip; adaptive end caps use the path's actual style during the animation, available only in symbols that draw in a single direction.
- Symbols built from multiple subpaths (e.g., a circle) treat the first guide point as start and end simultaneously (indicated by a capsule at the point's trailing edge); by default they draw clockwise, reversible from the context menu; they only support single-direction animation, not bidirectional.
- Bidirectional drawing: symbols with directionality implied from the center (e.g., wave.3.up) can have the starting point at the center and additional points on each side; the system automatically recognizes the bidirectionality.
- Advanced option: hold the option key and drag one side of the guide point along the path without affecting the associated point, to adjust a default position that is not ideal.

Examples cited:
- line.diagonal: first simple example of annotation with two guide points.
- scribble (variable): has variable width, so it cannot simply have the "stroked" stroke to build the animations; it needs more guide points on closed curves.
- line.3.horizontal: example of multiple paths in the same symbol, each line with its own drawing direction; dragging the starting point onto another guide point reverses the arrow's direction.
- wave.3.up: example of bidirectional drawing from the center.
- Thermometer: example of variable draw enabled on just one layer (the "meter"), so that only that part conveys progress.

Short quotes:
"Every curve and angle must feel deliberate, balanced, and visually communicative."
"There is no one correct way to place guide points."

<!-- visual:wwdc2025_337 -->
### What the images show
Basis: 16 of 16 frame sheets viewed, all codes checked.
- The screen builds a visual notation glossary with a fixed convention: an open point marks the start of the stroke, a filled point marks the end, smaller intermediate points mark guides along curves, and small arrows alongside indicate the drawing direction (sheet 0007, q0058 to q0060). A summary frame brings together six examples in a two-by-three grid, each with its own functional caption: diagonal line, scribble, three horizontal lines, circular arrow, "Same Start & End point" and "Corner points" (q0061).
- A blue technical plate anticipates, well before the spoken explanation, the entire annotation vocabulary for the "scribble.variable" symbol: labels "Guide Points", "Start/Corner/End", "Attachment/Follow Path", a "Variable Width a != b" dimension pointing to two different widths of the same stroke, and thumbnails of two weights in the footer (sheet 0002, q0016).
- The app's anatomy always appears in the same three-column arrangement, category sidebar, central canvas with the symbol and inspector on the right, repeated from the standard catalog for Custom Symbols mode, which adds a layers panel below the animation inspector (sheet 0004, q0028 to q0030; sheet 0007, q0063; sheet 0008, q0064). The inspector stacks fields with a label on the left and a control on the right: Animation and Repeat menus, "Whole Symbol / By Layer" segmented buttons and a Direction field.
- The difference between two frames reveals an interface state rule: the "Reverse" field with a toggle only appears when the selected animation changes from "Draw On" to "Draw Off" (sheet 0004, q0029 to q0030).
- The annotation is shown happening step by step on the canvas, with the symbol in translucent gray and the points overlaid in dark blue: the diagonal line first gets an open point and then the filled point with the direction arrow, and the thumbnail in the layers list updates along with it, working as a progress indicator (sheet 0008, q0064 to q0066).
- A pair of frames makes concrete the density of points a closed curve requires: the same S-shaped stroke appears with few guides and still-loose curves, and then with extra guides filling exactly the tight bends (sheet 0008, q0069 to q0070).
- The layers panel lists each subpath as its own row labeled "Fill", and the blue highlight migrates from row to row as each of the three horizontal lines receives its guides, with the middle one showing an arrow in a different direction from the other two (sheet 0009, q0073 to q0076). In the concentric waves the points concentrate at the central base with arrows going out to both sides, and one of them appears selected with a square drag handle (q0078 to q0081).
- Context menus anchored to a specific point expose the available choices as text: "Default Endcap" and "Adaptive Endcap" over the rounded square (sheet 0010, q0085), and "Automatic / Guide Point / Corner Point / End Point" over the electrocardiogram stroke (sheet 0012, q0106 and q0108).
- A point that marks the start and end at the same time has its own shape on screen: at the top of the circle the marker appears as an elongated capsule, distinct from the round start and end points seen in the other symbols (sheet 0010, q0089 and q0090).
- A color code separates what animates from what does not: blue for "Drawing components" and green for "Non-drawing components", applied to the marker of "list.bullet" and the arrowhead in "arrow.trianglehead.clockwise"; the marker goes from a gray outline to filled green between two frames (sheet 0011, q0093 to q0094). The anchoring of the arrowhead to a point is shown as a translucent shape connected by a thin line to the point (q0095 to q0097), and two final diagrams label the parts as "Path A" and "Path B" to justify the separation (q0098 and q0099).
- Color bands overlaid on the "arrow.trianglehead.pull" symbol visually segment what belongs to each subpath, a green "Path A" band on the straight base, a "Path B" label on the curved tip and a blue "Path A & B" band on the shared extent, with the "Subpath 1" item selected in the app's layers panel (sheet 0012, q0102 and q0103).
- The electrocardiogram's side legend grows between frames from three point types to four, and the new item, "Corner point", gets a diamond marker instead of the circle used by the others (sheet 0012, q0107 to q0108). Complementary diagrams show the corner point as a "Side A" and "Side B" pair on the same side of the stroke (sheet 0013, q0109 and q0110).
- The weight grid is the verification tool shown on screen: columns named from Ultralight to Black with the Regular column in bold as the base, first with three faded drawings, then sharp with a scale bar, then with guide points overlaid, and finally expanded to the nine filled columns (sheet 0013, q0113 to q0116).
- The same grid gets diagnostic markings: small numbers next to each guide point, a red angular fan between two points in the Black column and, in the next frame, orange lines connecting specific points (sheet 0013, q0117; sheet 0014, q0118 to q0120).
- The interface uses dimming highlight to teach where to click: the whole panel is dimmed except one button, with a line and "Enable Variable Draw" label pointing to it, and the target changes from one thermometer layer to the other between two frames (sheet 0014, q0124 to q0125).
- Gradients first appear as an applied system, six icons with the same directional shading, and then inside an iPhone frame on a Face ID screen, with example icons alongside to compare scale (sheet 0006, q0049 and q0050). In the app, the "Gradients" toggle appears switched on both with Rendering Mode set to "Multicolor" and to "Monochrome" (q0051 to q0052).
- The code blocks compare the same function across the three ways of writing it, with header comments per framework, and a light blue highlight that advances from snippet to snippet as the cited API changes, from drawOff to individually, then variableValueMode and colorRenderingMode (sheet 0015, q0128 to q0132).
Visual proportion: most of the frames are technical diagrams, the SF Symbols app screen, symbol charts or code; the presenter appears in short cuts interspersed across almost all the sheets, sometimes with the topic list overlaid, and occupies the final frames of the closing (sheet 0016, q0139 and q0140).
Recorded divergences or limits: the notes flag a pair of frames with no visible change despite the expectation (sheet 0006, q0053 to q0054), identify the concentric waves symbol with a caveat ("wave.3.up or similar", sheet 0009), treat the rainbow and the list with an arrow as likely generic examples rather than the examples cited in the speech (sheet 0003, q0025 and q0026), and note that the last three frames of the final grid turned black because the video ends before completing the sheet (sheet 0016). The notes also contradict each other about frame q0105 of sheet 0012, described at times as the "arrow.trianglehead.pull" arrow, at other times as the electrocardiogram, so it is not cited as proof of either one.
<!-- /visual:wwdc2025_337 -->

## Optimize your custom environments for visionOS (id: wwdc2025_305, 32.8 min)

- Basis: transcript and 28 of 28 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/305/.
- Central thesis: it is possible to bring cinematic-quality immersive environments (pre-rendered, with more than 100 million polygons) to real-time performance on Vision Pro using a procedural workflow in Houdini that specifically exploits the limits of the "Immersive Boundary" (the area the person can physically move through).

This video is primarily technical (3D/graphics pipeline), not a traditional user interface design video, but it deals with decisions that directly affect the spatial experience perceived by the person.

The design/optimization process Apple describes:
1. Pre-rendered image, capturing cinematic lighting, rich detail and high-end materials.
2. Geometry and textures optimized based on what the viewer actually experiences (using the Immersive Boundary as a reference).
3. The pre-rendered image is transferred (baked) onto the optimized environment.
4. Everything is assembled in a real-time editor, such as Reality Composer or Unity.

Principles stated and why:
- Understanding exactly where the person can move and look (the Immersive Boundary) makes it possible not to render everything at maximum quality, only the parts that matter; this is the key to the optimization.
- In full immersion, every pixel is rendered (unlike mixed immersion, where only part of the screen is rendered over the passthrough), making performance more challenging.

Concrete techniques described (with exact numbers when stated):
- Adaptive polygon reduction: based on multiple viewpoints sampled along the Immersive Boundary, preserving detail in silhouettes and reducing where it is not needed.
- Billboards for distant objects: starting at 1 km (Boundary Camera indicates that depth and parallax cues start to flatten between 1 and 3 km), complex 3D geometry is converted into flat geometry oriented toward the Boundary, preserving the original silhouette vertex by vertex (without using transparency).
- Culling: Backface Removal (removes polygons facing away from the Boundary; in the moon's case, almost 60,000 triangles removed) and Occlusion Culling (ray casting of millions of points; 110,000 triangles removed in the example); together, they remove about 50% of the remaining triangles.
- Result in the moon case: from more than 100 million triangles to 350,000 after adaptive reduction and billboards; after culling, 180,000 triangles; in the end, fewer than 200,000 total triangles, with fewer than 100,000 visible on screen at any moment thanks to Frustum Culling.
- UVs: within the first 5 meters of the Boundary, UV mapping based on surface area is used (to keep texel density consistent from any angle); outside the Boundary, mapping based on projection/screen space (spherical projection) is used, because the surface is only seen from limited angles and distances.
- Problem identified with the single spherical projection: UV overlap, incorrect texel scaling when moving, and a single panoramic capture not being able to see everything; solution: project UVs from multiple angles (Mesh Partition HDA divides the mesh into minimal islands; Multi-Projection HDA projects each partition from the point where it appears largest in screen space).
- Final textures: the entire environment fits into two textures (one for inside the Boundary, scaled by surface area; another for the rest, scaled by screen space); the entire moon was compressed to fewer than 250 megabytes of texture memory, starting from tens of gigabytes of high-fidelity PBR maps.
- Frustum Culling via USD hierarchy: inside the Boundary, Boundary Partition HDA is used; outside, Frustum Partition HDA, dividing the mesh into progressively larger blocks.
- Final numbers of the case: fewer than 200 total entities, typically fewer than 100 draw calls per frame.

Examples cited:
- Moon environment: main case study, illustrating each stage of the pipeline.
- Joshua Tree, Mount Hood, Haleakala: other environments cited as examples of scene types (rocky, atmospheric).
- Conference room/theater (hard-surface interior): example of an environment that does not need heavy optimization because it is already modeled by hand efficiently.

Short quotes:
"High-fidelity content doesn't have to be expensive."
"You don't have to reduce the complexity, you just need the right system to take control of it."

<!-- visual:wwdc2025_305 -->
### What the images show
Basis: 28 of 28 frame sheets viewed, all codes checked.

- The presentation script is visible on screen through an opacity hierarchy, not only through the speech: the topics slide shows the current item in black and bold, the ones already covered in light gray and future ones in an even lighter gray, and the transition happens frame by frame (sheet 0004, q0028 with "Optimize geometry" in bold and q0029 adding "UV projection" while the previous one recedes to gray; the same pattern reappears in sheets 0007, 0011, 0013, 0015, 0021 and 0022).
- The same flow-diagram design returns with each new technique: a red source box linked by an arrow to an orange result box in the first two (sheet 0009, q0076, "Source content" to "Adaptive reduce"; sheet 0012, q0106, the same pair for "Vista billboard"), and a chain of several boxes when the subject is the entire sequence (sheet 0014, q0118, four orange boxes up to "Occlusion culling"; sheet 0019, q0171, vertical flowchart with an orange input box and purple steps).
- Right and wrong are marked with a graphic stamp over the image, and the notes record the exact frame where the stamp appears: in sheet 0008, q0066 shows the two wireframes compared without any marking and q0067 brings the same comparison already with a red "X" on one side and a green check on the other, over different mesh images; in sheet 0022, q0191 adds the "Surface projection" photo below the "Spherical projection" one, and only q0192 overlays the red circle with an X on the first and the green circle with a check on the second.
- The same content appears successively in different visualization styles, with the fixed scale symbol running through all of them: translucent green cylinder, red disc or ring on the ground and stylized human figure, yellow in the first sheets and orange in the following ones, appear over an abstract diagram (sheet 0004, q0036), top-down viewport (sheet 0007, q0058), wireframe with red and blue overlay (sheet 0025, q0217), realistic gray texture (q0218), checkered test grid (q0221) and final photograph (q0222).
- The diagram is built through controlled addition of elements, not by cutting straight to the finished version: in sheet 0002 the "Optimization workflow" first appears with only the title (q0011), then with two cards (q0012), then with the four colored ones (q0013), and in a later frame the same four dimmed to gray (q0014); in sheet 0026 the "Memory" slide gains two lines of text between q0228 and q0229 while keeping the same image.
- Exact measurements and numbers are written directly on the 3D scene itself or as a discreet caption next to the image: "1.5m radius of traversable space" (sheet 0004, q0036), the "1km" label over the terrain (sheet 0007, q0060), the "14,400 x 7200" resolution in the panoramic render (sheet 0017, q0146), "2.5m" and "1km" separating the two mosaic groups (sheet 0021, q0181), and "Position 1" and "Position 2" with thin leader lines pointing to points on the crater (sheet 0027, q0236 and q0237).
- Result numbers receive isolated highlighted-text treatment, without a chart and without a frame, between blocks of technical demonstration: a sentence about render cost on a light gray background (sheet 0001, q0008), "Over 100 million polygons!" (sheet 0005) and "350,000 polygons." (sheet 0013). The contrast between source and result already comes in another format, a pair of images of the same rock formation captioned "100,000,000 source" and "180,000 optimized" (sheet 0015, q0129).
- There is a rigid metric-slide template in the conclusion, repeated three times with almost no variation: short title, two or three lines of text always with "<" or "~" before the number, and a proof image on the right taking up about 45% of the width (sheet 0026, "Geometry" in q0226 and q0227, "Memory" in q0228 and q0229, "Draw calls" in q0230 and q0231).
- The production tool appears as a real interface, with legible node names and editable fields, not as a diagram: a three-panel layout with viewport, node network and the "Adaptive Reduce" panel containing Prims To Keep, Sample Points, the "Weights" block and a "Distance Ramp" curve with a control handle (sheet 0010, q0083 onward), plus real names such as adaptive_reduce1, boundary_sample1, filecache_rocks_high and occlusion_culling1 (sheets 0009, 0010 and 0014).
- The heatmap palette switch marks which optimization is on screen, without relying on the text: orange and red in the initial weight adjustment and blue and red after the parameter change on the same mountain (sheet 0010, q0083 versus q0086), yellow density points over gray terrain in the first Houdini captures (sheet 0006, q0049 and q0050) and shades of purple, blue and cyan in the culling stage (sheets 0013 and 0014).
- A black-and-white checkered grid with letters and numbers in the squares is used as a UV diagnostic tool, reappearing at three points far apart from each other (sheet 0018, q0156, with a central figure and green "Projection position" arrows; sheet 0020, q0176, with the projections overlapped; sheet 0025, q0221, applied back to the immersive-boundary scene).
- Color carries judgment, not just distinction: green for inside the immersive boundary and red or pink for outside it or for a problem area, seen in the zone diagram (sheet 0016, q0137 and q0138), in the pink patches that mark UV overlap (sheet 0017, q0153; sheet 0018, q0154 and q0155, with the patches getting fainter from one frame to the next) and in the error and correct stamps of sheet 0022.
- The pipeline's result appears as a data structure on screen, not only as a render: a dark attribute spreadsheet next to a USD hierarchy tree with icons by primitive type, the text "name > USD prim name, groups > USD GeomSubset", fields in monospace font with "name: immersive_boundary" and a "group:partition_N" list, ending on the exported file name visible on screen (sheet 0024, q0209 to q0216).
- The closing builds a grid of examples through gradual reveal, from a thumbnail to pairs and then to a full 3x3 of nine environments with captions, then highlights one of them with a thick black border before the transition (sheet 0027, q0238 to q0243; sheet 0028, q0244), and the final slide switches visual register, using a still-life photograph of a wooden table with decorative objects instead of a screen capture, with a credit footer from another session separated by a thin line (sheet 0028, q0246 and q0247).

Visual proportion: according to the notes, the great majority of frames are slide, render, diagram or real software capture, with the presenter appearing in isolated cutaway frames between blocks, and only at the close in a longer sequence (sheet 0028, q0248 to q0252); the screen switches the presenter's set design in the second half, from the orange and white background to a meeting room with a Mac Studio starting at sheet 0022, q0196.

Recorded divergences or limits: several sheets record incomplete transitions with overlapping titles or ghost text legible underneath (sheet 0016, q0136; sheet 0017, q0145; sheet 0022, q0194, with "High-end visuals. Minimal footprint."; sheet 0026, q0232, with residual "Build robust tools."); some captions appear cut off at the edge of the sheet and were left incomplete in the notes ("Geometry..." at q0101, "UV a..." at q0135, "Frustum Partiti[on]" at q0207); and the notes mark as probable interpretation, not as confirmed reading, the blue overlay of sheet 0015 and the meaning of the red and blue heatmap of sheet 0025, in addition to noting doubt about a duplicate frame at q0209.
<!-- /visual:wwdc2025_305 -->

## Make a big impact with small writing changes (id: wwdc2025_404, 16.0 min)

- Basis: transcript and 11 of 11 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/404/.
- Central thesis: four small writing changes (removing filler words, avoiding repetition, leading with the "why", and creating a word list) have a disproportionately large impact on the clarity of an app's UX writing.

The design process Apple describes:
- Read the writing out loud to identify filler words and repetitions, and know where to tighten the text.
- Pause at every descriptive adverb/adjective found and ask: "does this word add value?"
- Create a word list from the start of development (but it can be done at any time), documenting: the chosen term, terms avoided for the same thing, and a simple definition.

Principles stated and why:
- There is no minimum word quota: unlike a school essay, the app doesn't need to fill every empty space; generally the opposite is true, it's better to remove words.
- Adverbs and adjectives ("simply", "quickly", "fast", "simple") tend to be fillers; when they appear, it's worth pausing to check whether they're necessary. But description can be useful when it clarifies behavior (e.g.: "automatically" explains that the app feeds the pets on a schedule, not only manually).
- Interjections ("uh oh", "oops") and courtesies ("sorry", "please", "thank you") may seem to humanize the app, but when they don't add meaning they should be removed; in error messages, interjections can sound as if the problem isn't being taken seriously, and apologies can sound insincere in an alert.
- Unnecessary punctuation (such as an exclamation point) can function as filler and minimize the seriousness of a situation for someone who is waiting for something important.
- Repetition of language is another form of filler: saying the same thing in different ways should be avoided; economy of language is central to UX writing.
- Leading with the "why": messages are more effective when they say why the next step is useful, interesting or beneficial, before giving the instruction. Mental format: "to do/get one thing, first do another".
- Consistency through the word list helps anyone who works on the app know how it should sound; button labels are a good item to include in the list.

Concrete interface-building techniques (rewrite examples):
- "Simply enter your license plate number to quickly pay for parking." → "Enter your license plate number to pay for parking." (removal of "simply" and "quickly", without loss of clarity).
- Delivery notification: from "Uh oh. We're running late" + "We're sorry, your delivery driver won't make it on time. They'll be there in 10 short minutes! Check the app for your driver's location." to, after removing fillers, "We're running late. Your delivery driver won't make it on time. They'll be there in 10 minutes. Check the app for your driver's location."; then, combining repeated ideas, the headline becomes "Delivery delayed 10 minutes." and the body keeps only "Check the app for your driver's location."
- "Enter your phone number to get reservation updates." → "To get reservation updates, enter your phone number." (moving the benefit to the beginning of the sentence).
- Game app example: choosing "alias" as the official term for the in-game name, avoiding "Handle", "User Name", "Title"; and "health" avoiding "lives", "hearts", "energy", "stamina", each with a simple definition recorded in the list.

Examples cited:
- Parking garage app (the author's personal experience, from a trip): illustrates how a filler ("simply", "quickly") can sound ironic when the real experience is neither simple nor fast.
- Fictional pet food dispenser app: illustrates when keeping a descriptive word ("automatically") is necessary for clarity of behavior.
- Apple News+ Puzzles: the notification "Keep your streak going by solving today's crossword" as an effective example of leading with the why.
- AirPods Pro hearing test setup screen: used as the final example that applies all four techniques together (no fillers in the headline "Test Your Hearing", paragraphs that lead with the why, "Next" button consistent across all screens, no repetition between headline and description).

Short quotes:
"Fortunately, your app doesn't have a minimum word count."
"Read your writing out loud."

<!-- visual:wwdc2025_404 -->
### What the images show
Basis: 11 of 11 frame sheets viewed, all codes checked.

- The list of four topics is built on screen item by item, in a left-aligned column next to the presenter, with the current item in bold black and the ones already covered in light gray, hierarchy made by weight and color rather than size (sheet 0001, q0006 to q0008, with the text disappearing completely at q0009); the same list returns at every topic change (sheets 0004, 0005, 0006 and 0007) and reappears at the close as an accumulated list of principles next to the screens (sheets 0009 and 0010).
- The text editing happens in front of the viewer, with visible editorial markup: the parking app screen appears empty, only with the app label, gains the card with the full sentence, and in a following frame the word "Simply" appears struck through within the sentence itself (sheet 0002, q0016 to q0017 to q0018).
- Before cutting, the screen highlights in bold one passage at a time to direct attention, and only then removes it: in the delivery notification card the bold moves from "Uh oh." to "We're sorry," and then to "10 short minutes!", and only in the following frames does the title lose the interjection and the body lose the apology and the exclamation point (sheet 0004, q0029 to q0035).
- The blue color marks what was added or reordered, against the black of the rest of the text: the word "Automatically" enters in blue at the beginning of the sentence about feeding the pets (sheet 0003, q0022 to q0023) and the benefit passage appears in blue when it's moved to the beginning of the reservation app's sentence (sheet 0006, q0051 to q0052).
- The notification card has a fixed anatomy, reused in sheets 0004, 0005 and 0008: square icon with rounded corners on the left, bold title, body in regular text, "now" label in the top right corner, rounded corners and a subtle shadow. The form card follows another anatomy, with the app label above on the left, a rounded white card with a light shadow, instruction text, a field with placeholder and a solid black "Next" button (sheet 0002), and it returns with a field and button in the game example (sheet 0008, q0067).
- The final rewrite appears as a merge of two sentences into one, and the judgment comes by way of a seal: the card body first highlights in bold the passage to be merged while the rest stays in light gray, then the title becomes the short sentence with the number, and finally the two cards appear stacked, the old one with a red X circle and the new one with a green check circle (sheet 0005, q0037 to q0040). This right and wrong pair appears only once in the video.
- There are two levels of device frame fidelity: the simple smartphone outline, just the rounded silhouette, with no status bar or chrome, appears in the reservation app's conceptual example (sheet 0006, q0050), while the other conceptual text examples stay in cards with no frame at all (sheets 0002 and 0003); the real iPhone frame, with notch, status bar with time, signal, wifi and battery, a dotted progress bar at the top and a rounded blue button at the bottom, is reserved for the real product example at the end (sheet 0009, q0075).
- The vocabulary example lists appear in a single column, left-aligned and with generous spacing: four words in the adverbs and adjectives card (sheet 0002, q0014 and q0015) and the list of interjections and courtesies going from three to six items between one frame and the next, within the same slide (sheet 0003, q0025 to q0026).
- The vocabulary table is built cell by cell in front of the viewer, simulating the act of assembling the document: first only the three column headers, then the accepted term, then the avoided terms, then the definition, and then the next row starts empty (sheet 0007, q0057 to q0063); the format has no vertical borders, a small gray header and rows separated by a thin horizontal line.
- Terminological consistency is demonstrated by going through three components of different nature with the same term, and the video shows them first isolated and then side by side with the word in bold in all three: form card, search field with a magnifying glass icon and departure notification card (sheet 0008, q0067, q0068, q0070 and q0071), with the reference table gaining a fourth row in the middle of this sequence (q0069).
- The final example uses real captures of an onboarding flow and keeps accumulating the principles next to the screens: two iPhones side by side with the adjustment screen and the quiet environment screen, a grayscale ear illustration for physical instruction and a text indicator with a green dot for the noise level, while the side list gains the items one by one until all four are complete (sheet 0009, q0077 to q0081; sheet 0010, q0084 and q0085).
- The close switches visual register: the screen empties to gray, the references title appears over a still photograph of a wooden table with a leash and dog toy, and the list of cited talks uses exactly the same table pattern without vertical borders as the vocabulary list (sheet 0010, q0089 and q0090; sheet 0011, q0091).
- A color filter over the scene of the two presenters at the table marks only the opening and the close: a purple and pink overlay that dissolves at the start (sheet 0001, q0002 to q0003) and a bluish overlay applied in the last frame (sheet 0011, q0092 to q0093).
- A detail recorded in the notes shows the agenda list getting ahead of the script: in the frame where "Lead with the why" is in bold as the current item, "Make a word list" already also appears in bold below the gray items, before it has been mentioned (sheet 0001, q0008).

Visual proportion: per the notes, almost every frame with content carries an interface component, text card, list or table, often in the same frame as the presenter; frames with only the presenter, or the two of them at the table, come in as short cuts between examples and at topic turns, and in a longer sequence at the opening and the closing (sheets 0001, 0010 and 0011).

Recorded divergences or limits: the notes contradict each other on two points, and here what the sheet describes frame by frame governs. On sheet 0005 the frame record says the old card with a red X comes in below the new one, while the notes summary puts the old one on top, so only the stacking is asserted, not the order. On sheets 0002 and 0003 the summary speaks of a smartphone outline, but the sheets describe cards with no device frame, and sheet 0003 says this explicitly. The button in the final example is recorded as "Get Started" on sheet 0009 and as "Next" in the notes summary.
<!-- /visual:wwdc2025_404 -->

## Explore video experiences for visionOS (id: wwdc2025_304, 25.9 min)

- Basis: transcript and 22 of 22 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/304/.
- Central thesis: the Vision Pro, as a spatial computer, lets video be presented in far more forms than a traditional flat screen, from embedded 2D/3D to fully immersive formats like Apple Immersive Video, and visionOS 26 expands that range with new non-rectilinear projection profiles.

This is primarily a technical/engineering video about media formats, not about interface design methodology, but it describes presentation decisions that directly affect the viewer's experience.

The process/framework Apple describes (video profiles and where each one fits):
- 2D and 3D (rectilinear projection): straight lines stay straight, with no lens curvature; that's why they look correct on a flat surface. It can be embedded (inline) in the UI, expanded into a floating window in the shared space, or anchored (docked) in a custom virtual environment.
- Spatial Video: stereo video with additional metadata, capturable by ordinary people (iPhone), not just professional producers; by default it appears in a window with a slight glow at the edges; it can expand to immersive, full-scale presentation, where the frame's edge disappears.
- 180°, 360° and wide FOV: new in visionOS 26, projected onto curved surfaces (half sphere, full sphere, or a curved mesh that recreates the lens profile of an action camera).
- Apple Immersive Video: the most immersive experience, with extremely high-resolution stereo video, calibrated to the exact lens that captured it.

Principles stated and why:
- Rectilinear videos look correct on a flat screen because they have no curvature; non-rectilinear videos (180°/360°/wide FOV) need a curved surface precisely so they don't distort.
- Immersive playback is sensitive to camera movement, because it places the viewer's head exactly where the camera was during capture; that's why the system includes automatic high-motion detection (in QuickLook, AVKit and RealityKit), which automatically reduces immersion in high-motion scenes, with an option to adjust sensitivity in Settings.
- MV-HEVC (MultiView HEVC) is used for stereo video because the left-eye and right-eye images are very similar; compressing only the differences between the two eyes saves file size, especially important for streaming.

Concrete interface-building techniques, with exact numbers when stated:
- 360° video: mapped onto a sphere via equirectangular projection; the rectangular frame used is twice as wide as it is tall, covering 360° in width and 180° in height.
- 180° video: half-equirectangular projection, square frame.
- Wide FOV: action cameras like the GoPro HERO13 and Insta360 Ace Pro 2 capture a horizontal field of view typically between 120° and 180°; it uses "parametric immersive projection", defined by parameters of focal distance, skew and lens distortion.
- Apple Immersive Video (URSA Cine Immersive camera, Blackmagic): stereo capture at 8160 x 7200 pixels per eye, that is, 59 megapixels per eye, at 90 frames per second, totaling more than 10 billion pixels per second; field of view up to 210° horizontally and 180° vertically.
- Apple Immersive Video creation pipeline: 1) capture on the URSA Cine Immersive; 2) editing in DaVinci Resolve Studio; 3) preview and validation in the Apple Immersive Video Utility apps (macOS and visionOS); 4) segmentation in Compressor for distribution via HLS (HTTP Live Streaming).
- Per-shot edge blends: each shot of an Apple Immersive Video can define a custom edge blend curve (a dynamic alpha blend curve, not a fixed mask), which merges the shot's edge with a custom background environment.
- New APMP (Apple Projected Media Profile) file format: a QuickTime profile that natively supports 180°, 360° and wide FOV in visionOS 26; supported for expanded and immersive playback, but not for embedded inline playback.
- Automatic conversion to APMP: 180° stereo videos from the Canon EOS VR system, 360° videos from the GoPro MAX and Insta360 X5, equirectangular videos in Google Spherical Video v1/v2 format, and raw videos from action cameras like the GoPro HERO13 and Insta360 Ace Pro 2.
- Spatial video can be captured on the iPhone 15 Pro, iPhone 16 and iPhone 16 Pro (Camera app or AVCaptureDevice APIs), on the Vision Pro itself, and with Canon R7 and R50 cameras with a Canon dual lens.

Examples cited:
- Destination Video (sample code project): shows video transitioning from an expanded window to docked in a custom studio environment made with Reality Composer Pro, with "dynamic light spill" to look like an integral part of the environment.
- Apple TV+ "Wild Life" (elephants at the Sheldrick Wildlife Trust, Kenya): an example of Apple Immersive Video, described as transporting the viewer to a scene that's almost impossible to experience in reality.
- Freeform: an example of inline playback of 2D video inside a board with other content.
- Apple Park (pond and "rainbow"): examples of 180° and 360° capture.

Short quotes:
"They're not just limited to a flat screen in front of the viewer."
"It's like being there."

<!-- visual:wwdc2025_304 -->
### What the images show
Basis: 22 of 22 frame sheets viewed, all codes checked.
- The viewer's orientation is handled by a vertical agenda track in the bottom-left corner, over the presenter's own footage, with no box or border: the current item in bold black, the ones already covered in light gray, growing one item at a time (sheet 0001, q0007 to q0009; it reappears on sheets 0002 q0010, 0004 q0028 to q0030, 0008 q0072, 0017 q0152 and 0020 q0176).
- There's a recurring diagram vocabulary throughout the video: a thin-outline white human silhouette on a perspective grid floor and, in front of it, the surface that receives the video. Only the shape changes according to the format being explained, full sphere, disc or half sphere, curved band, rectangle with a blue grid (sheets 0003 q0026, 0006 q0050, 0009 q0073 to q0078, 0013 q0111 and q0112, 0018 q0162, 0020 q0174). The background isn't always the same: black on sheets 0009 and 0013, light gray in the diagrams on sheet 0006.
- The measurements are drawn as technical-drawing dimension lines on top of the diagram itself: a side line "180°" and a base line "360°" on the equirectangular frame (sheet 0010, q0085 to q0086), pixel dimensions at the top and side of the side-by-side frame (sheet 0011, q0092), and a "170°" field-of-view caption centered below the actual photograph (sheet 0012, q0107 and q0108).
- The anatomy of the descriptive slides is stable: a bold black title and a gray subtitle in the top-left corner, list items one per line, and API names in monospaced font inside a blue-gray chip, for example AVCaptureDevice and PreviewApplication (sheets 0006 q0052 to q0054, 0007 q0055, 0016 q0137). The list marker varies by sheet: a simple dash on sheet 0006, no marker on sheets 0007, 0016 and 0018. New items are marked with a rounded green badge next to the title (sheets 0003 q0026, 0006 q0054, 0007 q0063, 0015 q0127).
- A reference to another session becomes a standardized footer: a thin separator line, the session name on the left in small gray text and the event year on the right, appearing as an extra layer between one frame and the next (sheet 0007, q0058 to q0059 and q0062 to q0063; sheet 0017, q0150 to q0151).
- Almost every text or diagram slide is built up in layers across several frames instead of appearing complete. The camera specifications list grows with each frame at an irregular pace, one item in q0157, two more in q0158 and one more in q0159 (sheet 0018), the pipeline diagram gains the Capture and Edit boxes and only afterward Preview and Segment, connected by dotted arrows (sheet 0019, q0165 to q0167), and the automatic-conversion slide gains one group of icons at a time (sheet 0015, q0130 to q0134).
- The non-rectilinear formats have a fixed shape-and-color coding, repeated every time they reappear: blue dome, round orange shape and green wedge (sheets 0008 q0071, 0014 q0125 and q0126, 0015 q0131 to q0134, 0020 q0179). The rectilinear ones only get their own icon in the recap, as flattened vertical rectangles in gray, red and dark blue, next to a seventh gold icon for Apple's immersive format (sheet 0020, q0178 to q0180).
- An isolated technical concept gets a definition card that differs from the rest: the term in huge, bold, centered typography, with a small caption below and no image, as with the "HEVC" card with the acronym's expansion (sheet 0011, q0097 and q0098).
- The before-and-after comparison is done with a grid overlay instead of right/wrong labels. The same photo appears in color with a blue perspective grid and then desaturated, keeping the blue lines (sheet 0008, q0066 to q0067). On sheet 0013, the corrected image with the blue grid appears alongside a corner thumbnail with the original, distorted capture (q0114).
- The transition between levels of immersion appears as a progressive edge blur, not a hard cut. The video window loses its rectangular frame and the edges dissolve into a blurred vignette on entering immersion (sheet 0005, q0038 to q0039), and the same visual language returns in the automatic immersion reduction, when the scene loses sharpness until the real furniture behind it becomes visible (sheet 0016, q0142 to q0144, with a return to sharpness on sheet 0017, q0148).
- A real visionOS Settings screen shows the panel's anatomy: a side column with icons colored by category, the active category highlighted in light blue, and a main panel with a title, a green toggle switched on, explanatory text, two radio options and a three-position segmented control for motion sensitivity (sheet 0017, q0149).
- The inline app capture shows the construction of a typical window: a white card with rounded corners, a thin title bar at the top with an icon and the document name, a collage of irregularly sized videos with text labels, and a floating capsule toolbar below the card (sheet 0002, q0011).
- The stereo correspondence is illustrated with yellow circular markers connected by thin lines between the left and right panels, adding points with each frame until they form a grid of correspondences between sky, horizon, water and rocks (sheet 0012, q0100 to q0101).
- The immersive format's edge blend curve is drawn as a dotted outline of yellow dots around the circular cutout, visually different from the blurred edge used for spatial video (sheet 0020, q0174).
- Dense tables only appear in the closing: seven columns, one per profile with its icon at the top, and criteria rows on the left, with light-blue background highlights on specific cells and green checkmarks applied only to certain columns (sheet 0021, q0182 to q0183 and q0184).
- The closing repeats the opening's color identity: the last frame gets a saturated magenta layer over the whole scene, echoing the opening "WWDC25" card (sheet 0022, q0191 to q0192, against sheet 0001, q0001).
Visual proportion: per the notes, the presenter alone occupies only a few connecting stretches between blocks, mainly sheets 0001 and 0022 and isolated frames in the middle; most of the frames are slides, diagrams, interface captures or example footage, and at some points he shares the screen with the slide (sheets 0006 q0051 to q0054, 0016 q0136 and q0137, 0019 q0163, q0168 and q0169).
<!-- /visual:wwdc2025_304 -->

## Build a SwiftUI app with the new design (id: wwdc2025_323, 22.3 min)

- Basis: transcript and 17 of 17 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/323/.
- Central thesis: adopting the new design system and the Liquid Glass material in SwiftUI is, for the most part, automatic when recompiling with the Xcode 26 SDK, but there are new APIs specific to app structure, toolbars, search, controls and custom glass elements that allow the experience to be refined even further.

The design process Apple describes (applied to the Landmarks sample app):
1. Update structural components (NavigationSplitView, TabView, Sheets).
2. Update toolbars (grouping, spacing, badges, monochrome icons).
3. Update the search experience (consistent positioning).
4. Let controls (buttons, sliders, menus) gain Liquid Glass automatically.
5. Adopt glass in custom UI elements when necessary.

Principles stated and why:
- Liquid Glass is an adaptive material: it changes from light to dark automatically according to the content below, when scrolling the screen.
- Controls come alive during interaction (toggles, sliders, segmented pickers turn into liquid glass when touched), creating a "delightful" experience.
- Icons use monochrome rendering in more places (including toolbars) to reduce visual noise and emphasize the app's content; tint should be used to "convey meaning" (a call to action, a next step), not just for visual effect.
- Corner concentricity: buttons and containers must share the same corner center as the container they are in (e.g.: a button at the bottom of a sheet must have corners concentric with the sheet's corners); the "concentric rectangle" shape resolves this automatically across different screens.
- Glass cannot "sample" other glass: nearby elements in different containers produce inconsistent visual behavior; that is why GlassEffectContainer groups elements to share the sampling region, being "essential for visual correctness".

Concrete interface-building techniques:
- backgroundExtensionEffect: allows views to extend beyond the safe area without clipping content; the image is mirrored and blurred outside the safe area, extending the artwork without clipping the visible content.
- tabBarMinimizeBehavior: configures the iPhone's tab bar to float over the content and minimize when scrolling (e.g.: onScrollDown, used by the TV app); re-expands when scrolling in the opposite direction.
- tabViewBottomAccessory: places a view above the tab bar (e.g.: the Music mini player), taking advantage of the extra space from the tab bar's collapse; the environment exposes tabViewBottomAccessoryPlacement to adapt the accessory's content when collapsed.
- Sheets: at partial height in iOS 26, have a Liquid Glass background by default, inset (bottom edges "pulled inward" fitting the display's curves); when transitioning to full height, the glass background gradually becomes opaque.
- Navigation zoom transition: sheets can "morph" out of the button that presents them, marking the toolbar item as the source and the sheet's content as the transition's destination.
- ToolbarSpacer: with fixed spacing, separates toolbar items into distinct visual groups (e.g.: "favorite" and "add to collection" grouped separately from the share link and inspector); with flexible spacing, creates expandable space between items (used by Mail for the filter item on the left and the search/compose group on the right).
- sharedBackgroundVisibility: separates a toolbar item into its own group, with no background (used by the user avatar in the Books app).
- badge modifier: adds an indicator to toolbar items in one line of code.
- scrollEdgeEffectStyle: adjusts the sharpness of the scroll edge effect (scroll edge effect, a subtle blur/fade under toolbars) in dense UIs with many floating elements, as in Calendar.
- Search: in the toolbar, the field sits at the bottom of the screen (easy reach); on iPad/Mac, it appears in the top-right position of the toolbar; searchToolbarBehavior allows explicitly opting into the minimized behavior when search is not central to the app's experience.
- Search as a dedicated tab: set the search role on a TabView tab; when selected, the search field replaces the tab bar (pattern used by the Health app).
- Bordered buttons: capsule shape by default; mini, small and medium controls on macOS keep the rounded rectangle shape (preserving horizontal density); updated control heights on macOS (controls slightly taller, more space around the label, larger click targets); there is support for extra large buttons; new glass and glassProminent styles.
- Sliders: now support tick marks, they appear automatically when initialized with the step parameter, or manually via a ticks closure (example given: marks at 60% and 90%); the neutralValue parameter allows starting the track's fill at a non-initial point (useful for playback speed values that can go up or down from a default).
- glassEffect modifier: applies glass within a capsule shape by default; text inside the glass uses an automatically adaptive vibrant color for legibility; the interactive modifier makes the glass react to interaction (scales, bounces, shines).
- GlassEffectContainer + glassEffectID: group multiple glass elements so they interact and merge with each other; used in the Landmarks sample app to create fluid "morphing" of badges when expanding and collapsing.

Examples cited:
- Landmarks (Apple's sample app): used throughout the video as the application case for each new API.
- TV app: uses tabBarMinimizeBehavior with onScrollDown.
- Music app: uses tabViewBottomAccessory for the mini player.
- Mail app: uses a flexible ToolbarSpacer to separate the filter (leading) from search/compose (trailing).
- Books app: uses sharedBackgroundVisibility to isolate the user avatar with no shared background.
- Maps: example of custom glass controls floating over the map, cited as a good candidate for the floating layer effect.

Short quotes:
"Sometimes, in life, to gain clarity and focus on what's truly important, you may need to re-invent yourself."
"Only use this to convey meaning, like a call to action or next step, but not just for visual effect."

<!-- visual:wwdc2025_323 -->
### What the images show
Basis: 17 of 17 frame sheets viewed, all codes checked.
- The dominant format is the Swift code plus result mockup pair, almost always with the code on the left and the device on the right, and a specific snippet of code highlighted at each change of topic. Only the image shows the exact syntax of the modifiers, parameter names and nesting (sheets 0004 q0031, 0005 q0039, 0011 q0093, 0014 q0125, 0016 q0136). In some of the frames the mockup sits below the code, not beside it (sheet 0010, q0086).
- Recommended and discouraged practice are marked by icons, not words: a red circle with an X next to the custom presentation background code (sheet 0006, q0049) and in the diagram of two overlapping sampling regions (sheet 0015, q0135); a green check next to the zoom transition code (sheet 0006, q0050) and beside the "Sahara Desert" screen in the frame following the one that carried the annotation label (sheet 0009, q0076 to q0077).
- The structure of the video is marked by a recurring visual index: the list of topics appears over the presenter's footage, with the current item in bold and the rest in light gray, reaching up to five items (sheet 0003, q0022 to q0024; repeats in sheets 0007 q0057, 0009 q0079, 0011 q0099, 0014 q0121). In the first four times it is followed by an isolated title card with the topic's name (sheets 0003 q0025, 0007 q0058, 0009 q0080, 0012 q0100); on the fifth, the frame following the highlight is already a map mockup, with no title card.
- The new API receives a green seal pointing to the exact line within the code block itself (sheet 0004, q0031 to q0032, on the background extension modifier).
- Exact measurements appear in a diagram: the button sizes slide shows five heights in points, from 16 to 36, one per named size (sheet 0012, q0105), and the previous slide separates by size range who uses the rounded rectangle and who uses the capsule, with the code box for both modifiers overlaid on the same diagram (q0103 to q0104). According to the notes, the speech addresses the increase in heights without citing these numbers.
- States of the same component are compared in two ways: two devices side by side, one with the full tab bar and the other with it collapsed (sheet 0005, q0040), and the same element across consecutive frames, such as the slider's thumb, which changes position, size and opacity from one frame to the next, suggesting rest and interaction (sheet 0002, q0013 to q0014).
- Annotation labels with a line point to the exact element on the screen: "Search Field" over the search fields on the MacBook and iPad (sheet 0010, q0085), "Edge Effect" over the toolbar area of the "Sahara Desert" screen and "Hard edge effect" over the top of the Calendar app's screen (sheet 0009, q0076 and q0078), and "Badge" over the red numeric indicator on the bell icon (sheet 0008, q0071).
- The toolbar's anatomy is shown by the evolution of the highlight in the code over the same result screen: the highlight moves from the fixed spacer to the inspector item without the mockup changing (sheet 0007, q0062 to q0063), and the isolated avatar gains a light circular background when the modifier that hides the shared background is highlighted (sheet 0008, q0065 to q0066).
- The material's effect appears through a change in color and shape of the same element across consecutive frames: the badge goes from a rounded rectangle to a green capsule when it receives tinting (sheet 0015, q0127 to q0128), then goes from green to golden yellow (q0129 to q0130) and from golden to pinkish orange (q0130 to q0131), following the interactive glass code block.
- The concept of glass sampling is explained through an abstract diagram: a pill labeled as a view with a glass effect surrounded by its sampling region, and then two of these regions overlapping, marked with a red X (sheet 0015, q0133 to q0135).
- The grouping animation is shown by the count of elements across frames: the stacked circular badges on the right side of the screen increase from two to several and then go back to two, while the code block with the container and the identifiers stays on the left (sheet 0016, q0136 to q0139).
- Almost every result screen is framed within the device's physical outline, sometimes with the same app on MacBook, iPad and iPhone at the same time (sheets 0003 q0019 and q0020, 0007 q0059 and q0060, 0008 q0072), sometimes on just two devices, MacBook and iPad (sheet 0010, q0083 and q0084), which visually reinforces the idea of family across platforms.
- A semitransparent, blurred layer effect around the screen appears as a presentation device on two occasions, on the iPad and then on the three devices together (sheet 0004, q0028 to q0029; sheet 0007, q0060 to q0061).
- System controls are presented on their own as a design reference before any code: zoom, plain button, tinted button, toggle, list picker and segmented control, first over a central iPhone and then without it (sheet 0002, q0011 to q0012).
- The slider appears with symbolic icons at the ends instead of text, magnifying glasses in one case and a turtle and rabbit in the other. The fill already starts from an internal point of the track in the turtle and rabbit frame, before the code changes, and shifts further to the right when the neutral value parameter enters the code (sheet 0013, q0110 to q0113).
Visual proportion: according to the notes, the presenter alone occupies short transitional segments between topics and the entire final sheet (sheet 0017), while from sheet 0004 to sheet 0016 most of the frames are code, diagram or device mockup.
Recorded divergences or limits: the notes flag frame q0114 (sheet 0013), a system context menu with undo, redo, copy and duplicate items, as having no apparent connection to the surrounding slider content, possibly a transition instant captured between cuts.
<!-- /visual:wwdc2025_323 -->

## Elevate the design of your iPad app (id: wwdc2025_208, 15.3 min)

- Basis: transcript and 17 of 17 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/208/.
- Central thesis: iPadOS 26 introduces new building blocks (fluid navigation, freely resizable windows, a new pointer, a full menu bar) that, together, make it possible to elevate an iPad app far beyond what was possible before; the basis of everything is simplicity.

The design process Apple describes:
1. Choose the navigation pattern (sidebar or tab bar).
2. Make the navigation adapt to smaller sizes.
3. Extend the content around the navigation.
4. Adjust the app to the new windowing system (multitasking).
5. Consider the new pointer and the hover effect.
6. Build the app's menu bar.

Principles stated and why:
- Sidebar is ideal for apps with many subviews or deeply nested content (e.g. Mail); tab bar is more compact and flexible, allowing more content to be shown and a more immersive feel. It is recommended to start with tab bar if in doubt, since it can "morph" into sidebar as the app scales.
- When adapting the navigation to size changes, the layout change must be non-destructive: resizing the app must not permanently alter its layout; you should be "opportunistic" and revert to the initial state whenever possible.
- Content is the reason people use the app, so as much of the display as possible should be used for the most immersive experience (via the scroll edge effect, extending content below the toolbar and the sidebar).
- On multitasking: each document should open in its own window (additive behavior), instead of the old "Open in Place" that cleared the previous context; this requires naming each window descriptively (e.g. the document's title), because otherwise the new window list in the app's menu does not help find the right window.
- The new pointer tracks input directly 1 to 1, without snapping or "rubber band" to any target; it is more precise because, under the hood, the pointer has always been capable of more precision than the finger approximates.
- Menu items should always stay in the same place, even when inactive (they appear dimmed); hiding them is disorienting, because it forces the person to rescan the entire menu every time it opens, without being able to rely on spatial memory. The same applies to entire menus: never hide them completely, even when nothing inside them is actionable at the moment.

Concrete interface-building techniques:
- Sidebar can fluidly morph into tab bar (and vice versa) via a button on the sidebar itself (example: Music app).
- Toolbar wrap around the window controls: for apps updated to iPadOS 26, the window controls should sit inline at the leading edge (leading) of the app's toolbar, avoiding reserving a permanent safe area above the toolbar (which is the compatibility behavior for apps that have not been updated); this frees up space for more content without increasing the window size.
- A handle in the bottom right corner of each window allows dragging to resize; the window controls, in the top left corner, grow on touch revealing functionality, and if pressed and held expand to show window layout shortcuts.
- Pointer: new shape (no longer circular, approximating the finger) to a more precise and responsive shape; the new highlight effect is a "platform" (platter) of Liquid Glass that materializes over the buttons as the pointer passes, bending and refracting the elements below to indicate the selected button.
- Menu bar: revealed by moving the pointer to the top edge, or by swiping down with a finger; it contains the app menu, standard menus provided by the system, and custom menus from the app.
- Organization of a custom menu (example: Mail's "Message" menu): populate it with every action related to the menu's name; order by frequency of use, not alphabetically; group related actions into their own sections; move secondary actions to submenus when the menu gets long; assign a symbol to each item (ideally the same one used in the app); assign keyboard shortcuts to the most common actions.
- Populate the "View" menu (provided by the system) with the app's tabs (if organized by tabs) and a navigation toggle (show/hide sidebar).

Examples cited:
- Mail: sidebar lists mailboxes and multiple accounts, exposing the content hierarchy at the top level; navigation is faster because the sidebar "flattens" the navigation.
- Music: sidebar with library and playlists; has a button that morphs the sidebar into tab bar.
- TV app: uses tabBarMinimizeBehavior with onScrollDown for multitasking.

Short quotes:
"At its core, iPad is about simplicity."
"Hiding menu items is not recommended because people will find this disorienting."

<!-- visual:wwdc2025_208 -->
### What the images show
Basis: 17 of 17 frame sheets viewed, all codes checked.
- A fixed right-and-wrong marking as a teaching method: a green check in the top right corner signs off the approved composition and a red X signs off the rejected one. The complete pair appears across two themes, the document opened in its own window against the window that replaces content (sheet 0009, X at q0079 and check at q0083) and the menu with all items against the reduced menu (sheet 0015, q0132 to q0135). In sheet 0008 only the negative marking appears, over the band above the toolbar (q0070).
- Error annotation via red dashed line: sheet 0008 draws a horizontal dashed line above the Mail toolbar, next to the red X (q0070 and q0072), and before that shows the three window control circles in close-up with a measurement ruler above indicating distance (q0069). What the screen marks is that band above the toolbar; the explanation of the safe area reserved for apps that have not been updated comes from the speech, not the frame.
- Text labels overlaid on the real interface to name the structure: gray words such as "Mailboxes", "Accounts", "Tabs", "Library", "Playlists" sit next to the sidebars of Mail and Music, as a teaching layer that the final interface does not have (sheet 0003, q0023 to q0026).
- Comparison of the two navigation patterns over the same content screen: the vertical bar gets the label "Sidebar" and the horizontal bar gets "Tab bar", and the following sequence shows the same Music screen going from one format to the other and back (sheet 0004, q0028 to q0036).
- Adaptation by width is demonstrated across three states of the same app: full screen inside an iPad frame, the same interface rotated in perspective and a smaller floating window over a blurred physical environment (sheet 0005, q0039 to q0045), and then windows of varying sizes with the iPad Dock appearing underneath (sheet 0006, q0046 to q0054).
- Anatomy of the window controls: a translucent whitish capsule with a shadow gathering three colored circles in the red, yellow, green pattern, plus a sidebar icon beside it, in the top left corner of the window, isolated in close-up across three nearly identical frames that suggest a slow highlight animation (sheet 0007, q0061 to q0063).
- Window accumulation shown through overlap with diagonal offset and shadow: two Photos windows ("Recents" and "Timelapse") in sheet 0009 and three Notes windows ("Roadtrip To Do's", "Presentation Notes", "Bird Spotting") appearing one by one in sheet 0010 (q0085 to q0087).
- The before and after of window naming appears inside the menu itself: the "Open Windows" menu first lists "Notes 1, Notes 2, Notes 3" with a check on the active window (sheet 0010, q0088 and q0090) and then lists the documents' real titles, already with a green approval check in the corner of the frame (sheet 0011, q0091 to q0093).
- Anatomy of the pointer highlight: three toolbar icons inside a single translucent white capsule receive a gray highlight circle that moves from the center icon to the one on the right between frames, with a green "NEW" badge and an arrow cursor pointing at the target in the middle frame (sheet 0012, q0101 to q0104).
- The desktop menu bar appears fully reproduced on the iPad, with plain text items (Mail, File, Edit, View, Mailbox, Message, Format, Window, Help) and the open item highlighted in blue. Mail's "File" menu carries keyboard shortcuts aligned to the right, command N and command O among them (sheet 0002, q0012), while the "Message" menu isolated in close-up lists the items with submenu arrows and no visible shortcuts (sheet 0013, q0116 and q0117).
- Populating the View menu is shown with two apps, but with different contents: in Clock the tabs themselves become menu items, with numbered shortcuts, command 1 on "World Clock" and command 4 on "Timers" (sheet 0014, q0121 to q0126); in Music the View menu lists actions to show and hide panels (Show Sidebar, Show Now Playing, Show Lyrics), each with its own shortcut (sheet 0015, q0127 to q0129).
- The slides work as a typographic progress bar: the same list of four themes reappears with every section change, with the current item in strong black and the rest in light gray (sheets 0002, 0007, 0011 and 0012), and in sheet 0016 all four appear equally highlighted, signaling the end of the path. The recommendation slides follow a single pattern, a large bold title and items in regular weight, built up incrementally, first the title alone and then the lines (sheet 0007, q0055 to q0056; sheet 0016, q0139 to q0140).
- The screen shows the black iPad frame with rounded corners when the intent is to situate the app on the device, and removes the frame when the focus is an isolated component, toolbar, menu or cursor over an empty gray background (sheets 0004, 0011, 0012 and 0013).
Visual proportion: of the 17 sheets, only the last one is presenter only, and the presenter frames in the others are isolated; the volume is in captures of real apps (Mail, Music, Photos, Notes, Clock), almost always inside an iPad frame, plus about a dozen title and summary text slides.
Recorded divergences or limits: the notes record that the green and red marking system is not mentioned in the speech, nor are the teaching labels overlaid on the interface; that the visual indication of how much has been scrolled, mentioned in the speech, does not appear explicitly in the frames of sheet 0006; that in sheet 0003 the button that turns sidebar into tab bar is described in the speech but does not appear in the frames; and that the list of themes changes name throughout the video, with "Layout" in place of "Navigation" already by sheet 0007, "Arrow Pointer" in place of "Pointer" from sheet 0012 onward, and "Windowing" and "Menu Bar" in the final list of sheet 0016.
<!-- /visual:wwdc2025_208 -->

## Build a UIKit app with the new design (id: wwdc2025_284, 25.9 min)

- Basis: transcript and 19 of 19 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/284/.
- Central thesis: just like in SwiftUI, UIKit apps get most of the new design system (Liquid Glass) automatically when recompiled with the new SDK, but there are new APIs specific to tab views, split views, bars, presentations, search, controls and custom glass elements.

The design process Apple describes (UIKit equivalent to the SwiftUI video):
1. Tab views and split views adopt the new design and float above the content.
2. Navigation bars and toolbars become transparent, with Liquid Glass buttons, giving more space to the content.
3. Presentations (sheets, alerts, action sheets) get an updated zoom transition.
4. Updated search experience with more placement options.
5. Controls (buttons, switches, sliders) get a new look.
6. Custom UI elements can adopt Liquid Glass via their own API.

Principles stated and why:
- Liquid Glass is distinct from other visual effects such as UIBlurEffect: it is designed to be an "interactive layer" that floats above the content, just below the fingertips, providing the main controls that the person touches; for that reason it should be limited to the app's most important elements, preferring system views and controls where possible.
- The bars' background is transparent by default; background customizations (UIBarAppearance, backgroundColor) interfere with the glass appearance and should be removed.
- Groups of items in separate glass should be used to distinguish related actions from actions with distinct behavior (e.g., image buttons share a background with each other; text buttons, the system's "Done"/"Close", and the prominent style have their own backgrounds).
- Glass cannot sample other glass: keeping glass elements close together in different containers produces inconsistent behavior (the same principle as the SwiftUI video); UIGlassContainerEffect resolves this by sharing the sampling region and reinforcing a uniform adaptation.

Concrete interface-building techniques:
- UITabBarController: tabBarMinimizeBehavior (e.g., the TV app with .onScrollDown); bottomAccessory via UITabAccessory (e.g., the Music mini player), with the tabAccessoryEnvironment trait to adapt the accessory view when collapsed inline.
- UIBackgroundExtensionView: covers the full width, including the sidebar's leading safe area inset; the input is a content view (e.g., an image view) positioned in the hierarchy and extended to fill the empty space; by default it fills the safe area on all edges with a positive inset; automaticallyPlacesContentView can be turned off to position manually with AutoLayout (e.g., extension only on the leading edge for the sidebar, but not on top, if the navigation bar has little content that could cover the artwork).
- Navigation bars/toolbars: items are automatically grouped into visual sets with a shared glass background; use fixedSpace to separate items into distinct groups; bar buttons use labelColor by default (legibility); a custom tintColor conveys action meaning (e.g., systemOrange on the "Flag" button); the prominent style tints the button's own background.
- flexibleSpace: by default it separates the background between items; use hidesSharedBackground = false to distribute items evenly while keeping a single shared background.
- UINavigationItem: a new subtitle rendered below the title (example: Mail shows the number of unread emails); largeSubtitleView allows showing a button (e.g., an active filter) below the large title.
- Large titles now sit at the top of the scroll view and scroll along with the content; the scroll view needs to be extended fully under the navigation bar to keep the large title visible.
- Edge effect: automatic visual treatment (blur/fade) applied to scroll views under navigation/toolbars, ensuring legibility of overlapping content; it can be applied to custom containers via ScrollEdgeElementContainerInteraction; the .hard style is available for dense UIs with many floating elements (an appearance similar to iOS 18 bar backgrounds).
- Interruptible zoom transition: the default navigation transition (slide) is now always interactive and interruptible, as it already was in iOS 18 for the zoom transition; it allows swipe back at any moment during the transition, including in non-leading content areas (content backswipe gesture), automatically checking for concurrent interactions (e.g., swipe actions take priority over the content backswipe).
- Presentations: menus and popovers originating from a glass button make the button "morph" into the overlay, keeping visual continuity; sheets can adopt this by setting preferredTransition to .zoom and returning the origin barButtonItem; action sheets on iPhone now anchor to the origin view (sourceItem/sourceView on the popoverPresentationController), the same as on iPad; without a source, the action sheet appears centered with a cancel button.
- Search: on iPhone, the search bar automatically moves to the toolbar via searchBarPlacementBarButtonItem; on iPad, it follows the macOS toolbar pattern on the navigation bar's trailing edge (searchBarPlacementAllowsExternalIntegration = true), ideal for split views; UITabBarController can have a distinct search tab on the right, which expands when tapped (automaticallyActivateSearch = true activates the field automatically); integratedCentered centers the search bar on iPad.
- Controls: UISwitch with updated sizes; switch and segmentedControl thumbs gain a Liquid Glass appearance automatically during interaction; UIButtonConfiguration gains .glass() and .prominentGlass(); sliders preserve momentum and "stretch" when moved, support tick marks via TrackConfiguration (example: a speed slider limited to 5 values with allowsTickValuesOnly), neutralValue to anchor the fill at any point on the track, and a "thumbless" style (looks like a progress bar) for media playback.
- API for custom glass: UIVisualEffectView with UIGlassEffect; capsule shape by default, customizable via cornerConfiguration (.containerRelative adapts automatically to keep concentricity); glass adapts its appearance according to size (larger = more opaque; smaller = more "clear" and it alternates between light/dark to increase contrast); isInteractive = true for a scale/bounce reaction on touch; always prefer animating the "effect" property (not the alpha) to materialize/dematerialize correctly.

Examples cited:
- TV app: sidebar with vibrant content underneath (poster with UIBackgroundExtensionView), tabBarMinimizeBehavior.
- Music app: mini player as the tab bar's bottom accessory.
- Mail: subtitle showing the count of unread emails; current filter in largeSubtitleView; grouping of bar buttons with fixedSpace.
- Notes: used to demonstrate the interruptible navigation transition (swipe back at any moment).
- Maps: custom glass buttons floating over the map; when the sheet expands, the buttons are removed to avoid overlapping glass on glass.

Short quotes:
"Liquid Glass is designed to be an interactive layer."
"For that reason, limit Liquid Glass to the most important elements of your app."

<!-- visual:wwdc2025_284 -->
### What the images show
Basis: 19 of 19 frame sheets viewed, all codes checked.
- The dominant format is Swift code next to the screenshot of the affected app, and the difference between frames shows the new line and its effect on the screen at the same time: in sheet 0007, the fixed spacing line enters the code and the screenshot gains a noticeable gap between the navigation bar icons (q0055 to q0056), and right after, the accent color line enters and the flag icon changes from black to orange (q0058 to q0059).
- Anatomy of the button grouping in the navigation bar of the flowers app: an isolated text button on the left, a block of three image icons in the middle (share, folder, flag) and a single confirmation button on the right (sheet 0006, q0051). What names the rule is the slide next to it, which first lists who shares the glass background and in the next frame adds who gets their own background (q0052 to q0053).
- Label annotations with a thin line pointing to regions of the screenshot name the parts of the background extension mechanism, always on the same iPad screen of the TV app: "UIBackgroundExtensionView" at the bottom of the screen (sheet 0004, q0034 and q0035), "Content view" pointing to the center of the image (q0035) and, in the next sheet, "Content view" and "Extension" together, the latter in the band between the sidebar and the artwork (sheet 0005, q0041 to q0043).
- The edge effect appears in both styles and with a label pointing to the exact band: the gradual darkening of the content that scrolls under the bar on the email screen (sheet 0009, q0075 to q0076), the same effect applied to a custom container behind two buttons in the footer of a confirmation screen, with the "Edge Effect" label (q0077 to q0079), and the solid, opaque style on the calendar's top bar (q0080 and q0081).
- Anatomy of the title area: large title "Inbox" with a smaller gray subtitle below it, and then a pill-shaped filter button occupying the line under the large title, shown on iPhone and iPad in the same composition (sheet 0008, q0068 to q0071). The slide that opens the section builds the list of what's new one item per frame (q0064 to q0067).
- Difference between frames that shows the transition of search as a tab: the health app's screen goes from "Summary" to "Search" with a list of categories (sheet 0013, q0114 to q0115) and in the next frame the system keyboard rises, making the automatic activation of the field visible (q0116 to q0117). The same pair repeats in another app, from "Library" to "Search" with recent thumbnails and the keyboard (sheet 0014, q0118 to q0119).
- Three search placements are shown on different screens: a capsule field on the iPhone's bottom bar next to the add button (sheet 0012, q0108), a field to the right of the iPad's navigation bar in a two-column layout (sheet 0013, q0112 and q0113) and a field centered horizontally at the top over a grid of colored category cards (sheet 0014, q0121 to q0123).
- A showcase of isolated controls, one component per slide, centered over a neutral background with the code snippet in small monospaced font below: a green switch turned on, a plain glass button next to the prominent blue glass button, and a blue slider between turtle and rabbit icons (sheet 0015, q0127 to q0129).
- The slider's anatomy is demonstrated by moving the thumb between frames: with tick marks, the thumb appears in two distinct positions, always aligned to a mark (q0130 to q0131); with a neutral value, the thumb changes sides but the blue fill still originates from the same internal point on the track, not from the end (q0132 to q0133); and the thumbless style appears as a smooth bar (q0134). Where the fill starts only becomes clear in the image.
- The adoption of glass in a custom view is staged as layers accumulated on the same object, always over the same photo of a green leaf with a yellow flower: fixed corners become corners relative to the container, the frame's origin shifts, the size changes between two values, a "WWDC25" label enters inside the glass, the text and background get an accent blue, and then the text disappears via alpha before the effect is removed (sheets 0017 and 0018, q0145 to q0158).
- Two glass capsules inside the same container show the proximity behavior: they appear separated by a spacing defined in code and then merge into a single larger shape (sheets 0018 and 0019, q0162 to q0164).
- The continuity between button and presentation is shown by growth from the origin: a popover grows from the origin button on iPad across successive frames (sheet 0011, q0094 and q0095). Right after, Mail's folder-choice sheet appears next to the zoom transition code, in a card with rounded corners, centered title, close button and a list of folders with a colored icon and count (q0097); the origin of this sheet in the folder button is in the code and in the speech, not in a visible movement between frames.
- A visual metaphor stages the glass as a physical layer: a message card tilted at an isometric angle, with a pronounced shadow, rotates and moves closer until it flattens against the iPhone screen, with a second semi-transparent layer behind it (sheet 0016, q0137 to q0140).
- A warning slide with a yellow-orange alert icon lists the two bar background customizations to avoid, adding the lines between frames (sheet 0009, q0073 to q0074), and the topic slides use a hierarchy by opacity, with the current item in strong black and the rest in light gray, repeated across almost the entire presentation.
Visual proportion: none of the 19 sheets is just the presenter; it appears in isolated transition frames, and the bulk is in screenshots of real apps (TV, Music, Mail, Notes, Contacts, Health, Maps, Calendar, Weather and a place-details app) almost always paired with Swift code snippets, plus title and list slides that build up by addition.
Recorded divergences or limits: the notes point out that in sheet 0011 the popover content changes between q0095 and q0096, which indicates two different examples and not the same element in transition; and they record several sequences of consecutive frames with no perceptible difference on the screen, some with the code next to it advancing (sheets 0012, 0013 and 0014) and others with no change on either side (sheets 0004, 0010 and 0016).
<!-- /visual:wwdc2025_284 -->

## Meet SwiftUI spatial layout (id: wwdc2025_273, 20.4 min)

- Basis: transcript and 15 of 15 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/273/.
- Central thesis: in visionOS 26, SwiftUI's layout system (with its already familiar 2D concepts and tools) now works natively in three dimensions, making it possible to build declarative spatial experiences without needing RealityKit for everything.

This video is mostly technical (3D layout APIs in SwiftUI), with direct application to spatial interface construction.

The design process Apple describes (using the BOT-anist example app):
- Views in visionOS calculate width, height, depth and Z position (not just X and Y).
- Views with a fixed frame (e.g. Model3D) versus flexible (e.g. RealityView, GeometryReader3D, which occupy the full proposed depth by default).
- A window proposes a fixed depth to its content; a volume proposes a depth that is also resizable.
- Stacks (ZStack, HStack, VStack) are already 3D in visionOS, with sensible default behaviors for depth; ZStack composes depth the way VStack composes height.

Principles stated and why:
- Using SwiftUI's layout system (instead of manual positioning) gives built-in support for animations, resizing and state management automatically: when a robot is removed from the carousel, SwiftUI animates the positions and sizes of the rest to accommodate the new space.
- Visual effects (rotation3DEffect, scaleEffect, offset) do not impact layout: an HStack does not "know" about a view's rotated geometry, which is good for animating something without affecting its neighbors, but bad when you want the layout to react to the rotation, which is why rotation3DLayout exists, modifying the rotated view's frame within the layout system.
- The default depth alignment in Stacks is "back"; it can be customized with depthAlignment (.front, .center, .back) or with a fully custom depth alignment, implementing the DepthAlignmentID protocol.

Concrete interface-building techniques:
- scaledToFit3D: used together with resizable() to keep a Model3D's aspect ratio (avoiding "stretching" the model) while still scaling to fit the available width, height and depth.
- Model3DAsset: allows the 3D model to be preloaded in a reusable way.
- Depth Podium (custom example): three robots aligned in a staggered arrangement in depth, the first aligns its back with the second one's center, and the second one's center aligns with the front of the third, implemented with a struct that conforms to the DepthAlignmentID protocol and a default value (.front).
- rotation3DLayout: applied to an HStack with a rocket model and a description card, rotating 90° on the X axis (or 45° in another example) and correctly adjusting the HStack's size/positioning to make room for the rotated object, preventing it from "bumping into" the card or leaving the volume.
- debugBorder3D (custom modifier, taught at the end of the video): uses spatialOverlay to render the border in the same 3D space as the view; internally it uses two ZStacks and a rotation3DLayout to place borders on the leading, trailing, back and front faces.
- SpatialContainer: positions multiple views in the same 3D space "like Russian dolls" (nesting dolls), applying a shared 3D alignment (e.g. bottomFront, topTrailingBack).
- spatialOverlay: similar to SpatialContainer but for overlaying a single view onto another in the same 3D space, with support for 3D alignments (used, for example, to overlay a selection ring around the selected robot, aligned by the bottom).
- MyRadialLayout (custom layout reused from the video "Compose custom layouts with SwiftUI"): positions views in a circle; combined with rotation3DLayout (90° on the X axis) and an opposite rotation3DEffect of -90° on each robot individually, to orient the carousel horizontally while keeping the robots "standing".

Examples cited:
- BOT-anist: example app used to demonstrate robot customization, a collection of robots in a 3D radial carousel, a robot profile card (RobotProfile) with name/description aligned to the front for legibility, and a selection ring via spatialOverlay.
- Rocket model + description card: example used to contrast rotation3DEffect (does not affect layout, causes overlap) versus rotation3DLayout (adjusts the layout correctly).

Short quotes:
"SwiftUI is a great tool for building 3D apps, but there are many use cases where you'll still want to reach for RealityKit."
"I love how I can compose these existing 2D SwiftUI modifiers with new 3D APIs to make something completely new."

<!-- visual:wwdc2025_273 -->
### What the images show
Basis: 15 of 15 frame sheets viewed, all codes checked.

- The video's dominant format is a two-panel slide: on the left a gray comment followed by syntax-colored Swift code, next to it the result, which is an iPhone thumbnail in the 2D examples and a rendered 3D scene of the robot gallery in the visionOS examples. This pairing appears from sheet 0003 to sheet 0014, and is what makes visible which line of code corresponds to which change on screen.
- There is an explicit measurement annotation on the layout diagram: in sheet 0003, frame q0022 shows arrows and point values for a Y position of 40, an X position of 35, a height of 50 and a width of 100, next to the code for the robot head image and the iPhone thumbnail with the corresponding red frame.
- The color convention for the debug outlines is fixed and carries meaning throughout the video: solid red for the individual view's frame or for the visual geometry, yellow for the composite container's frame, and dashed blue for the frame the layout system sees. Yellow appears surrounding a VStack in sheet 0003, a ZStack in sheet 0005 and an HStack in sheets 0006 and 0007, and the red plus dashed blue pair appears in sheets 0010 and 0011.
- The clearest right-versus-wrong pair is in sheet 0007: in q0060 the robot's name card is hidden and cut off behind the model, with the default depth alignment by the back, and in q0061 and q0062, after applying the depth alignment by the front, the same card appears whole and legible in front of the robot. The sheet first shows the same concept in 2D, with center alignment in q0057 and bottom alignment in q0058, using the iPhone thumbnail as an analogy.
- The visual proof of the difference between visual effect and layout is in sheet 0010: in q0083 and q0084 the rotated rocket collides with the details card, with the red outline and the dashed blue one visibly misaligned, in q0085 the side camera shows the rocket leaving the frame toward the wall, and in q0090 the two outlines coincide and the rocket positions itself next to the card without overlap. The conclusion appears written over the scene itself in q0086, as a short intertitle.
- Sheet 0011 repeats the same check from another angle: in q0092 and q0093 the rocket rotates 45 degrees and in q0094 the two debug outlines appear exactly overlapping, confirming that the rotated geometry and the layout frame have become the same.
- Abstract diagrams serve as a bridge before the realistic scene. In sheet 0008, frames q0068 and q0069 show three colored blocks first in isometric view and then in top view, with a dotted line indicating which one is further forward. In sheet 0009, q0073 through q0076 evolve this top-down diagram step by step, one square changing depth at a time as each alignment guide line enters the code, and only in q0077 does the actual gallery scene show the three staggered robots.
- To explain views that occupy the same three-dimensional space, sheet 0013 uses nested boxes in Russian-doll style: q0112 shows three nested boxes, q0113 and q0114 show the same composition repositioned in opposite corners as the alignment parameter changes, and q0115 reduces to two boxes, visually marking the difference between the container for multiple views and the overlay of two.
- New APIs receive a green badge that reads "NEW" placed right over the exact word in the code, not over the whole slide. This appears in sheet 0005 on the modifier that adjusts the model's scale, in sheet 0006 on the 3D model's resource type, in sheets 0007 through 0011 on the custom depth alignments and on the rotation modifier that affects layout, and in sheet 0013 on the spatial container and the spatial overlay.
- The code is built incrementally, with the new line highlighted in a light blue background over the already existing snippet, which makes the before and after of each addition visible frame by frame. This is the case for the robot profile between sheets 0006 and 0007, the podium alignment between sheets 0008 and 0009, the carousel between sheets 0011 and 0012, and the debug border modifier in sheet 0014.
- Sheet 0012 shows the carousel assembly step by step within the scene: in q0102 the camera pulls back and reveals the circular arrangement, in q0103 and q0104 the robots appear lying down after the 90-degree rotation on the X axis seen from above, in q0105 and q0106 they stand back up after the individual counter-rotation, and in q0107 the whole set descends to the base of the room with the use of a spacer.
- Sheet 0014 assembles the debug tool itself on screen: in q0121 the robot appears inside a simple outline, in q0124 the edges turn into two crossed vertical faces after the 90-degree rotation on the Y axis, and in q0125 a second stacking adds front and back, closing the edge box on all faces.
- The session's topic list works as a progress bar made only of typography: the active item in bold black and the rest in light gray on a beige background, reappearing in sheets 0003, 0006, 0009 and 0012, each time with a single item changing weight. In sheet 0003 it also gains a fourth item between q0019 and q0020.
- Caption cards with a bold name and a short description below float next to the 3D objects in sheets 0001, 0006, 0007, 0008 and 0009, with no window frame and no buttons, closer to a museum label than to an app interface. The actual app UI appears in two other formats: the customization app's panel in sheet 0001, with tabs and color palettes in circles arranged in a grid, and the compact game panel in sheet 0002, with a short title and two buttons side by side.
- The selection state of a 3D object is communicated by two combined elements, seen in sheets 0013 and 0014: a white ring under the robot's feet and a small floating panel above it with the item's name and two circular action icons, one for editing shaped like a pencil and a red one noted in the notes as for deleting or stopping.
- The closing, in sheet 0015, reveals the list of next steps one item per frame, from q0127 to q0130, adding at the end a divider line and a footer with the name of the recommended session on the left and the event identification on the right, in the same typography as the topic lists used throughout the video.

Visual proportion: about four fifths of the recorded frames show a code slide, diagram or rendered three-dimensional scene, and the presenter alone appears in short interspersed blocks, concentrated in the opening, the topic changes and the close.

Recorded divergences or limits: four frames had the code text overlapped and illegible or partially illegible due to double exposure from a slide transition, in q0032 and q0034 of sheet 0004, q0059 of sheet 0007 and q0116 of sheet 0013. The notes also record excerpts captured with the code still incomplete, such as the empty angle in q0091 on sheet 0011, and a shift in the presenter's shirt tone between q0002 and q0003 on sheet 0001, noted as a possible camera cut.
<!-- /visual:wwdc2025_273 -->

## Design foundations from idea to interface (id: wwdc2025_359, 19.1 min)

- Basis: transcript and 15 of 15 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/359/.
- Central thesis: a well-designed app answers three questions clearly on every screen ("where am I", "what can I do", "where can I go"), and getting there is an iterative process that goes through structure, navigation, content and visual design, in that order.

The design process Apple describes (demonstrated throughout a fictional vinyl record collection app):
1. Structure: write down everything the app does (features, flows, "nice-to-haves") without judging or cutting anything yet; then imagine how and when people would use the app, what helps and what gets in the way; only then clean up, removing what isn't essential, renaming what isn't clear, and grouping what belongs together. This process is called information architecture (organizing and prioritizing information so people find what they need, without friction).
2. Navigation: use what was learned from information architecture to decide what becomes a tab in the tab bar (asking "what is really essential? what deserves a tab?"); name and choose icons (SF Symbols) that help understand the purpose of each tab without needing to interact; use the toolbar to resolve "where am I" (screen title, not menu or branding) and "what can I do" (screen-specific actions).
3. Content: separate mixed content types; apply progressive disclosure (show only what's necessary at first, revealing more as people interact); choose the clearest layout (list versus grid) according to the type of content; group content by themes (time, seasonality, progress, patterns) to reduce choice overload.
4. Visual design: review how typography, color and imagery work together; build visual hierarchy (what should be seen first); use system text styles for flexible hierarchy under different screen conditions; choose a color palette and simple rules to apply it; use semantic colors (not hardcoded) for any dynamic element.

Principles stated and why:
- The three central clarity questions: "where am I", "what can I do", "where can I go from here", when an app answers these questions easily, it feels inviting and fluid, a sign of a solid foundation.
- Menus (hamburger) at the top of the screen are vague and unpredictable, because what the person needs first is context, not a hidden list.
- Each extra tab in the tab bar is one more decision the person needs to make, and can present the app as more complex than it really is; that's why simplifying the tab bar matters.
- Tabs are for navigation, not for taking action (direct reference to the Human Interface Guidelines), that's why a primary action button (like "Add") should stay inside a section, not in the tab bar.
- Progressive disclosure: showing only what's necessary right away, revealing more as the person interacts, avoids overloading with choices.
- Grouping content by time, seasonality, progress or patterns reduces choice overload and makes the app feel "one step ahead", understanding what the person will need next.
- Semantic colors (named by purpose, like "label" or "secondarySystemBackground", not by appearance like "black" or "purple") are dynamic: they change automatically according to contrast, screen environment and light/dark modes; use accent color with care so as not to disrupt these dynamic changes, overall readability, or people's comfort.
- Design elements shouldn't be treated as isolated projects: the real impact comes from how they work together, contributing to the overall meaning of the interface.
- Design is never really finished, and there's no single right answer.

Concrete interface-building techniques:
- Toolbar replacing menu/branding: includes the screen title (sets expectations about the content, helps maintain orientation when navigating and scrolling) and screen-specific actions using SF Symbols (only the essential, since space is limited).
- Disclosure control next to a section title, to reveal more groups on demand (progressive disclosure applied to a list of "crates"/groups).
- List (instead of grid) recommended when the grid takes up too much space for few items and doesn't handle longer text well; list is described as flexible, highly usable, familiar, makes quick scanning easier, and takes up less vertical space than images (more items fit on the screen); the list template comes from Apple Design Resources.
- Collection (for large volumes of images: photos, videos, products that scroll in/out of the screen): consistent spacing between items, avoid too much text over them.
- Four content-grouping themes cited: by time (e.g.: recent files, "continue watching"), by seasonality/current events, by progress (e.g.: email drafts, a class in progress), by patterns (relationships between items, e.g.: related products).
- Visual hierarchy: making the most important element larger or with more contrast so it catches the eye first; using system text styles instead of "eyeballed" sizes or custom styles, because they support Dynamic Type and stay legible under different conditions (longer text, different languages, larger text sizes).
- Subtle background (gradient or blur) behind text overlaid on an image, to improve readability without disrupting the design.
- A closed color palette (four colors in the example) plus a few retro shapes, applied with simple mix-and-match rules, to establish a cohesive aesthetic; a bolder, expanded typeface for group titles, distinguishing them from list text.

Examples cited:
- Fictional vinyl record collection app (created by the author for the demonstration): used from start to finish to illustrate each stage, from the initial confusing version (menu at the top, title as branding, "Records" revealed only at the end in the tab bar) to the final version (tab bar with three clear sections: Records with Add built in, Swaps, Saves).
- Video streaming ("continue watching"), email drafts, a class in progress: examples cited of grouping by progress.

Short quotes:
"Menus can be vague and unpredictable."
"Design is never really finished, and there's no single right answer."

<!-- visual:wwdc2025_359 -->
### What the images show
Basis: 15 of 15 frame sheets viewed, all codes checked.

- The agenda marker is made only of typography: a column of four words left-aligned, with the current topic in black and bolder and the rest in thin light gray, with no icon, numbering or progress bar, surrounded by plenty of empty space. It reappears on sheets 0001, 0002, 0004, 0005, 0006, 0007, 0009, 0011 and 0012, and some frames add a second level of subtitle, as on sheet 0006, where the tab bar item already appears in gray and the toolbar item in black.
- The questions guiding the session appear in two different formats. First as a white screen with a single centered sentence in bold on sheet 0002, in q0017 and q0018, one about what the person can do and another about where they can go. Then as an annotation applied over the real interface on sheet 0007, where q0059 points to a third question, about where the person is, simultaneously at the title at the top and at the tab bar at the bottom, and q0060 swaps the label for the question of where to go, pointing only to the tab bar.
- The diagnosis of the app's initial version is shown on the screen itself, not described in a slide: on sheet 0003, frames q0022 to q0025 show a hamburger menu button inside a translucent white circle overlaid on the album cover in the upper left corner, and q0026 and q0027 reveal the tab bar with five labeled items and the central add button raised in a colored circle above the line of the others.
- The simplification of navigation is recorded in stages, not in a single cut: on sheet 0005 the bar goes from five items in q0038 and q0042 to four in q0044 and to three in q0045. Frame q0042 still shows a curved arrow leaving an isolated plus sign and landing on the first tab, illustrating where the action was moved to, and q0043 shows the actual Human Interface Guidelines page on Apple's website, with a side menu and example illustration, appearing as a reference next to this change.
- The critique of ambiguous labels and icons gets a literal representation on sheet 0005: in q0039 the same tab bar keeps the text and positions, but four of the five symbols are swapped for generic smiley faces, one of them with a confused expression.
- The renaming appears as a controlled variable swap: on sheet 0006, q0047 and q0048 show the same three tab slots changing only label and icon, and q0050 and q0051 place the two screens side by side over the same content grid, labeled in full as previous version and new version, with the only difference being the tab bar.
- The anatomy of the toolbar is dissected with a thin line and short label on sheet 0007: q0056 points to the title in the upper left corner and q0057 and q0058 point to the group of three action icons in the upper right corner, which includes add, sync and an ellipsis menu.
- The separation of mixed content appears as a pair of states on sheet 0008: q0064 annotates two categories coexisting in the same grid, and q0065 shows the screen already reorganized with its own section header. Next, q0068 shows the section reduced to two thumbnails with a reveal arrow next to it, and q0069 and q0070 show the resulting full screen, with an item count at the top, while q0071 annotates the back control on the left and the actions on the right of the new bar.
- The choice between grid and list is resolved with a direct comparison on sheet 0009: q0074 and q0075 show the section in a grid of square thumbnails, q0076 shows the same section converted into a text list with a navigation arrow per row, and q0077 places the two versions side by side with before and after labels. Frame q0078 shows a screenshot of a component library in dark theme, with list templates, a permission dialog and toggle controls, indicating the origin of the component used.
- The content-grouping themes get their own pictograms on sheet 0010, presented one per frame and only afterward brought together in one row: a calendar for time in q0083 and q0084, a circular gauge for progress in q0085, a grid of four squares for patterns in q0086, and the three together in solid black on white in q0087. Right after, the app screen shows a collection section with two large cards in a colorful gradient in q0089 and q0090, with the collection label pointing to them, and on sheet 0011, in q0092, a count indicator in the corner of one of these cards is annotated as a progress reading.
- The visual hierarchy problem is demonstrated through exaggeration before the solution: on sheet 0012, q0100 and q0101 show the screen with a lime green background and the album title in huge letters crossing the entire width, repeated decoratively in the background.
- The system's typographic table appears in full in q0104 on sheet 0012, with each line rendered in the style it names and the point size stated: Large Title at 34, the three title levels at 28, 22 and 20, Headline at 17 semibold, Body at 17, Callout at 16, Subheadline at 15, Footnote at 13 and the two captions at 12 and 11. Next, q0105 applies these styles as an annotation over a full-screen cover, linking each style label to its corresponding text.
- The readability limit is also shown, not just stated: on sheet 0012, q0107 and q0108 show the same screen with title and subtitle over a colorful illustration of a butterfly and flowers, with one of the frames annotating the background layer and the text visibly competing for contrast with the artwork.
- The search for visual coherence appears as a process on sheet 0013: q0109 and q0110 show the group list gaining one thumbnail per row, q0112 and q0113 show a dense grid of dozens of thumbnails in mutually incompatible styles, mixing face photos, geometric shapes and retro illustrations, and q0114 shows the final screen with a reduced palette and consistent shapes.
- The system colors are taught by function name linked with a thin line or annotation point to a concrete area of the screen, in two complementary diagrams: q0115 on sheet 0013 and q0118 on sheet 0014 cover six roles, among them text, screen background, list row background, separator and the color of the selected tab item. On sheet 0014, q0119 and q0120 show a mockup in dark theme where a single blue accent color runs through buttons, selection and controls, and q0121 closes with the reference chart that brings together the four label levels, about a dozen system color swatches and three background levels, each block duplicated in light mode and dark mode.
- The closing, on sheet 0015, shows in q0127 and q0128 a dense mosaic of thumbnails of the same app screen in dozens of distinct visual identities, with different palettes, backgrounds and typefaces, in a regular grid and without caption, and no thumbnail repeats between the two frames.

Visual proportion: most of the recorded frames show app screens in an iPhone frame, topic slides, annotated diagrams or reference cards, and the presenter alone appears in short intervals between the blocks, including in the last two frames of sheet 0015.

Recorded divergences or limits: several sequences were noted as repeated framing with no perceptible change, including q0011 to q0014 in sheet 0002, q0053 and q0054 in sheet 0006, q0057 and q0058 in sheet 0007, q0093 and q0094 in sheet 0011, and q0119 and q0120 in sheet 0014. The notes also record transition frames with no content, such as q0016 in sheet 0002, and zoom transition frames with an overlaid iPhone silhouette, such as q0113 in sheet 0013.
<!-- /visual:wwdc2025_359 -->

## Explore prompt design & safety for on-device foundation models (id: wwdc2025_248, 22.2 min)

- Basis: transcript and 17 of 17 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/248/.
- Central thesis: designing good experiences with Apple's on-device language model (Foundation Models framework) requires understanding the specific limitations of a small model (about 3 billion parameters) and applying a layered safety approach, since no single layer is sufficient.

This video is about engineering/prompt design for generative AI, with direct implications for product design and safety UX, not about traditional visual interface construction.

The design process Apple describes:
1. Understand the on-device model's limitations before designing the feature (tasks that require complex reasoning should be broken into simple steps; avoid using it as a calculator or code generator; be careful with limited world knowledge and the training cutoff date).
2. Write prompts as clear commands, give few examples (fewer than five) directly in the prompt when necessary, use uppercase commands like "DO NOT" to reinforce restrictions.
3. Use "instructions" (a special prompt that defines how the model should behave for all subsequent prompts) separately from prompts coming from people using the app.
4. Safety layer: prompt design is the first tool; then come the framework's native guardrails (applied to both the model's input and output); then safety instructions written by the developer; then control over how the person's input is included in prompts; finally, use-case-specific mitigations.
5. Evaluation and testing: curate quality and safety datasets, covering the app's main use cases and also prompts that could create safety issues; automate end-to-end execution; manually inspect small datasets or use another LLM to evaluate at scale; also test the "unhappy path" of safety errors.

Principles stated and why:
- The on-device model is optimized and compressed to fit in a pocket (about 3 billion parameters), much smaller than server models with hundreds of billions of parameters; that is why it does not do everything a large LLM does.
- The model has limited world knowledge and can hallucinate (completely invent answers) for what it does not know; in places where facts are critical (such as instructions), one should not risk hallucinations that could mislead people. To generate facts, provide verified information written directly in the prompt, and carefully check the outputs for any new prompt.
- The level of imprecise knowledge may be acceptable in some contexts (e.g.: character dialogue in a bakery game) but not in others (a bagel encyclopedia).
- The model obeys instructions with precedence over prompts; that is why instructions are a great place to improve the safety of responses, but instructions should only come from the developer, never from untrusted content or user input; user input should go in prompts, not in instructions.
- Safety layers work like slices of Swiss cheese: each layer has holes, but a problem only gets through if the holes in all the layers line up at the same time.
- For a proactive feature (not initiated by a user action), a safety error can simply be ignored without interrupting the UI; for a feature initiated by the user, appropriate UI feedback must be given explaining that the app cannot process the request, possibly with alternative actions.

Concrete interface-building techniques (with prompt examples):
- Control the size of the output ("in three sentences", "in a few words" to shorten; "in detail" to lengthen).
- Control style and voice by specifying a role in the prompt (example: "a fox who speaks Shakespearean English").
- Guided generation: gives control over what the model should generate (strings, numbers, arrays, or a custom data structure), improving reliability.
- Xcode Playgrounds (#Playground): the recommended way to experiment with prompts, with the response appearing immediately in the canvas.
- Three patterns for including user input in a prompt, from riskiest to safest: (1) use the user's input directly as the prompt (most flexible, most risk, requires careful instructions to handle a wide variety of inputs); (2) combine the app's own prompt with the user's input; (3) offer a list of predefined prompts for the person to choose from (less flexible, but full control over the prompt, allowing you to curate what actually works well with the model).
- Use-case mitigation: for the bagel flavors app example, alert about allergens in the UI, or add dietary restriction settings to filter recipes; for the trivia app example, add extra instructions or a list of forbidden keywords, or train a classifier for a more robust solution.

Examples cited:
- Diary app: instructions define the model as an assistant that helps write diary entries by asking questions; it demonstrates both the use of instructions and the safety risk when the person's input becomes the prompt directly.
- Bagel flavor generator: illustrates both the limitation of world knowledge (incorrect description of a plain bagel) and allergy risk mitigation.
- Image Playground: cited as an example of UI that offers to "undo" the prompt that caused a safety error.
- Trivia app (fictional): illustrates mitigation of controversial topics or topics unsuitable for the audience.

Short quotes:
"Prompts impact safety."
"You can imagine the layers as a stack of Swiss cheese slices."

<!-- visual:wwdc2025_248 -->
### What the images show
Basis: 17 of 17 frame sheets viewed, all codes checked.

- Almost all the content slides repeat a single template, from sheet 0001 to 0017: bold black title aligned left at the top, secondary subtitle in light gray right below it, and list items appearing one per frame in a single column, without numbering, over a light gray background. The subtitle is what changes between neighboring slides, keeping the title fixed, as happens in sheet 0004, where the same header switches topic and resets the list to empty in q0032.
- Many statement blocks carry a status badge in the top right corner, functioning as a traffic light: an orange circle with an exclamation mark for risk and a green circle with a check for approved use. It appears in sheets 0004, 0005, 0006, 0007, 0011, 0013 and 0016, and is absent in others, such as sheets 0010 and 0014. The lighting up is visible frame by frame in sheet 0004, where the icon goes from off in q0028 to orange and lit in q0029, together with the first list item.
- The model flow diagram is the same drawing reused and expanded throughout the session: an input text box, a colored arrow, a square icon of connected nodes representing the model, and an output box. In sheet 0002 it first appears with the output empty and a blinking cursor in q0013, then filled in in q0015, and in q0016 the same drawing serves another use case, with input and output for tone rewriting.
- This same diagram grows to explain the difference between instruction and prompt in sheet 0008: q0068 shows only the instruction box connected to the model, q0070 adds a second row below with the prompt box and its output, and q0071 stacks three rows, the instruction and two different prompts, each row with its own model icon and its own response.
- The scale difference between models is shown as an area visualization in sheet 0003: in q0025 and q0026 two proportional circles appear side by side, the large one in light purple labeled as the server model with over one hundred billion parameters and the small one in dark purple labeled as the on-device model with three billion, each with a small color indicator dot.
- The source of the input is marked graphically: starting in sheet 0009, the prompt that comes from a person using the app gains a black, minimalist human silhouette beside it, seen in q0076, a feature that did not exist in the earlier diagrams where the prompt came from the developer. The same icon comes back in sheet 0012, in q0104, linking the user's request to the model's empathetic response.
- The risk progression in the code is taught through three consecutive blocks with the same status badge, in sheet 0013: q0110 shows the user's input becoming the prompt directly, with an orange alert, q0111 shows the input interpolated inside a fixed prompt, still with an alert, and q0112 shows an enumeration with named cases feeding the prompt, now with a green check.
- Editing instructions is shown as a difference between two frames in sheet 0012: q0103 brings the original instruction box and q0104 brings the same box with an extra line added, highlighted with a light blue background inside the code block, followed by its effect on the generated response.
- The protection diagram uses its own color code and grows across sheets: in sheet 0010, q0090 shows a red speech bubble with swear-word symbols, an arrow to an orange lock, and an arrow to a light pink violation card, in a linear sequence. In sheet 0011, q0091 repositions the model at the center and places one lock before it and another after it, making visible that the check happens on both input and output.
- The only real tool capture is in sheet 0007, in q0060 to q0062: Xcode with the code panel on the left and the results canvas on the right, the canvas divided into collapsible blocks for session, response, prompt and content, an eye icon next to the content field to expand the string, the generated response inside a light card in a serif font, and a run duration marker. Frame q0061 shows two windows side by side and q0062 the same windows slightly repositioned.
- The only real app capture is in sheet 0011, in q0096: an iPhone in dark theme with a status bar, a close button, the centered error message suggesting describing something else, an undo button and a row of suggestions with colored circular avatars below. This is error handling shown in a real layout, not in a diagram.
- Error handling also appears as a classification on a slide, in sheet 0011: q0093 brings only the proactive feature category and q0095 adds the user-initiated category, building the pair across two frames.
- A single moment in the session abandons the flat style of the slides: sheet 0005 brings a pixel art illustration of a character in front of a bakery counter in q0038 and, in q0039, adds the pixel art speech bubble and the green check, visually signaling that this is the error-tolerant scenario.
- The safety summary becomes a composite card in sheet 0015, in q0127: a block with a gears icon gathering the app's responsibility mitigations into two gray chip-shaped buttons, and below it another block with the model icon and a solid orange button for the native protections, with the color difference separating what belongs to the developer from what comes built in.
- The closing has two visual marks of its own: in sheet 0016 the final list grows from one item in q0141 to five items in q0143, gathering points already seen in earlier slides into one place, and in sheet 0017 the resources slide swaps the flat gray background for a real photograph of a wooden counter with a physical iPhone and slices of Swiss cheese, with the resource list in plain text over the photo, closing in q0149 with a translucent purple overlay over the live scene.

Visual proportion: most of the frames show text slides, schematic diagrams and Swift code blocks, with only two real capture sequences, that of the development environment on sheet 0007 and that of the app on sheet 0011, and the presenters appearing in short shots interspersed between the blocks.

Recorded divergences or limits: the notes point out that the Swiss cheese layers metaphor mentioned in the speech does not appear illustrated in any frame, and that the cheese slices in the final slide of sheet 0017 are a decorative photography element, possibly a late reference, without the layer diagram described verbally. There are also several nearly identical frame repetitions noted, at q0025 and q0026 on sheet 0003, q0065 and q0066 on sheet 0008, q0074 and q0075 on sheet 0009, and q0112 and q0113 on sheet 0013.
<!-- /visual:wwdc2025_248 -->

## What's new in Xcode 26 (id: wwdc2025_247, 36.9 min)

- Basis: transcript and 29 of 29 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2025/247/.
- Central thesis: Xcode 26 brings performance and download size gains, in addition to new productivity tools (inline Playgrounds, integrated Icon Composer, code assistant with LLMs) and debugging/performance/testing tools that, together, speed up the development cycle.

This video is a development tool summary (Xcode), not an interface design methodology video; it is included here because it is part of the indicated group, and brings two sections with direct relevance to interface design: Icon Composer and the AI-assisted code framework (use of images/sketches to generate UI).

The process/flow that Apple describes in the parts relevant to design:
- Icon Composer (mentioned in passing, with full detail in the dedicated video id wwdc2025_361): an app bundled with Xcode 26 to create multi-layer icons with material effects in a single file, covering light, dark and tinted modes, plus the new watchOS look.
- Code assistant with LLMs: can receive images (UI sketches) as an attachment to the query, since many LLMs can generate code from an interface sketch.

Concrete interface-building techniques cited:
- String Catalogs: automatic generation of context comments for translators, using the on-device model to analyze where and how a localized string is used in the project.
- Voice Control in "Swift mode": allows writing Swift code by speaking naturally, with the system understanding Swift syntax (spacing, operators, camelCase); demonstrated by adding a field to the "landmark" inspector for "continent".
- Playground (#Playground macro): allows iterating on any code (not just UI) with results appearing in the canvas; used in the video to debug a wrong-coordinates bug on a map, revealing that a regex was not correctly capturing the minus sign (negative longitude), placing the Grand Canyon in the wrong place.
- Code assistant (integration with ChatGPT, Claude 4 Opus and Sonnet, or local models via Ollama/LM Studio): can reference symbols with "@", attach files and images to the query, apply changes automatically or ask for review first, and maintain conversation context across successive messages (used to add a star-rating feature to "landmark collections", including adjusting the UI to display the stars).
- UI automation recording: records real interactions in the simulator and automatically generates test code; Automation Explorer in the test report allows inspecting attributes of each identifiable element after a test failure (example: an expected TextField that actually became a TextView because it supports multiple lines).

Honesty note: since this video is mostly about development tools (build performance, debugger, Instruments, tests), most of the content does not deal with "interface design" in the sense of this group's brief; the card above covers only the excerpts with direct relevance to UI construction or AI-assisted design flow. Performance numbers (e.g.: "24% smaller", "40% faster to load a workspace", "up to 50%" of typing latency, "up to 16 times faster" in Lists) appear in the text but concern tool performance, not interface techniques, so they were not detailed here.

Examples cited:
- App Landmarks (sample project): used throughout the video to demonstrate Playgrounds, Voice Control, and the code assistant adding star ratings.

Short quotes:
"With Icon Composer, you can create beautifully designed, sophisticated, multi-layered icons that work across multiple platforms and software versions."
"Images are especially useful, since many large language models can generate code from just a sketch of a user interface."

<!-- visual:wwdc2025_247 -->
### What the images show
Basis: 29 of 29 frame sheets viewed, all codes checked.

- The session's side topic list works as a progress bar for the entire talk and uses hierarchy only by font weight and color: active item in bold black, the rest in light gray. It already appears at the opening and switches items between neighboring frames (sheet 0001, q0005 to q0006), gains a second level with subitems when the topic subdivides (sheet 0002, q0012 to q0013) and reappears at every subject change (sheet 0021, q0188; sheet 0023, q0204), including right after the presenter switch, when the second presenter enters with the next topic already highlighted (sheet 0014, q0118 to q0119).
- Numbers become full screen: an empty frame precedes the data, which enters alone in large typography with no other element. The preceding frame is white at the opening, with "Xcode is 24% smaller." (sheet 0001, q0008 to q0009), and light gray before the data about workspace loading (sheet 0002, q0010 to q0011). The same isolated treatment is given to a feature name, "String Catalogs" (sheet 0008, q0066).
- The dominant composition of the captures is three fixed zones: file browser or chat panel on the left, code editor in the center, iPhone preview or result panel on the right. It repeats in almost all sheets from 0002 to 0015, and the synthesis of the notes records that the speech never names this structure, speaking only of editor and preview (sheet 0010, q0082; sheet 0011, q0099).
- Icon Composer appears with the anatomy of a three-column design app: layers panel on the left, central icon preview and properties panel on the right with named material controls and percentage values, among them blur, translucency, specular and shadow (sheet 0007, q0056). The same screen then gives way to a comparison grid with platforms in the rows and appearance modes in the columns, showing that the same icon generates up to six variations and that watchOS has only one (sheet 0007, q0058 to q0060).
- Before-and-after pairs appear in the live editing itself: the iPhone preview does not have the continent field and gets it after the conditional block is completed in the code (sheet 0004, q0031 to q0032); and the row of stars in the preview increases when the loop range changes in the code, with the accessibility label following the count (sheet 0011, q0095 to q0096).
- Background highlighting over text is the recurring way of saying "this matters here", with different colors by purpose: yellow for search terms within the code (sheet 0003, q0022) and blue for the selection made by voice (sheet 0004, q0029). In the regular expression result the marking changes shape, it is not a colored background in the code but rather a match badge next to the extracted numeric value, inside the canvas (sheet 0006, q0049 to q0051).
- Blue marks what is selected or active in completely different contexts: timeline track (sheet 0019, q0164), dropdown menu option (sheet 0017, q0150), API call snippet within the code (sheet 0027, q0239 to q0240) and chosen option in a settings menu, there accompanied by a checkmark (sheet 0028, q0247). The tone varies according to context, solid in the timeline track and light in the code snippet.
- The playground canvas shows the result as an expandable property tree next to the code, and special-type values bring embedded visualization instead of text: the coordinate property opens a miniature map with a pin, and a second line of code brings up a second, wider map below the first (sheet 0005, q0043 to q0045; sheet 0006, q0047).
- Error correction follows the same three-step choreography on sheets 0012, 0013 and 0015, visible in the comparison between frames: error underlined in red or in a popup over the line itself, then an action button named for that specific error, then the already-corrected state. It appears with "Generate Fix for Issue" (sheet 0012, q0106 to q0107), whose corrected result is only seen on the following sheet, in the file with the adjusted enum (sheet 0013, q0110), and with "Add NSCameraUsageDescription", which leads to the capabilities editor, where an empty required field gets a yellow warning, is filled in and loses the warning, and the typed text reappears literally in the system permission popup in the iPhone preview (sheet 0015, q0127 to q0134).
- The assistant panel has its own anatomy: conversation history in a vertical list, quick-actions popup anchored to the text field with four options (sheet 0009, q0074 to q0075), structured responses in numbered steps by file with a footer counting the scope of the change, "4 Changes in 3 Files" (sheet 0010, q0090), cancel and restore buttons to move through the code's version history (sheet 0012, q0100 to q0101) and the possibility of collapsing the panel to a narrow strip to give space back to the editor and preview (sheet 0011, q0096 to q0099).
- There is a standardized fact-sheet slide: large bold title, smaller gray subtitle when present, list of short phrases in normal weight and, in the footer separated by a thin line, the name of the reference session on the left and the event year on the right. It appears this way on sheets 0020 (q0175), 0022 (q0193) and 0027 (q0236 to q0238). The same title-plus-short-list design appears without a reference footer on the Processor Trace slide (sheet 0017).
- These slides are built in layers, not all at once: the title enters alone, the items appear afterward and the reference footer enters last (sheet 0027, q0236 to q0237 to q0238). On the closing slide the title also enters alone, but the items and the links footer arrive together in the following frame (sheet 0028, q0250 to q0251).
- In almost every new topic, before the real capture of the tool, a simple icon or schematic diagram with a label appears: magnifying glass over a chip for "Processor Trace" (sheet 0016, q0141), three square build-stage icons in a row (sheet 0022, q0191), three icons connected by straight lines for CPU optimization (sheet 0018, q0160) and double gears in black stroke for security (sheet 0023). Only afterward does the real window appear.
- Instruments windows share a fixed composition, timeline colored by track at the top and data table below, repeated in four different instruments (sheet 0016, q0143; sheet 0017, q0152 to q0153; sheet 0019, q0163; sheet 0019, q0170), while the configuration panels use the same form block with the name on the left, the control on the right and explanatory text in smaller gray below, also in editors of very distinct function (sheets 0017, 0023 and 0028).
- Diagnostic data comes packaged in a card: white popover with rounded corners and shadow, short text and an embedded miniature bar chart (sheet 0021, q0181), and a bar chart by app version with the current bar in dark blue plus a two-level recommendation tooltip, highlighted value and origin in smaller gray (sheet 0021, q0184 to q0187).
- Interface test recording is shown as a synchronized pair: simulator on the right, editor on the left, and each interaction on the screen gives rise to a new line of code, step by step (sheet 0024, q0211 to q0216). The editor's status bar is the state indicator that changes text throughout the process, something that only reading the frames in sequence reveals (sheet 0025, q0220 to q0224).
- The test failure is examined in an explorer with an event list on the left, the failure line in light red background with the detailed error, and a popover that opens over the simulator video bringing the real type of the element and the suggested code snippet (sheet 0026, q0232 to q0233).

Visual proportion: of the 29 sheets, only the last one is presenter-only; the body of the video alternates text slides, icons and diagrams with real captures of Xcode, Instruments, Organizer and Simulator, and the presenter appears mostly at topic turns, sometimes reduced to a rounded video cutout in the corner of the code screen (sheet 0004, q0028).

Recorded divergences or limits: the notes mark frames that are practically identical, with no perceptible change, at several points (sheet 0017, q0150 to q0151; sheet 0019, q0170 to q0171; sheet 0022, q0191 to q0192; sheet 0021, q0184 to q0186); a frame with an icon overlaid on the code is described as partially legible (sheet 0010, q0087); and the full-screen fade used between transitions is attributed to video editing, not to the product's interface (sheets 0016 to 0021 and sheet 0026).
<!-- /visual:wwdc2025_247 -->

## What this group reveals about the Apple way

- Liquid Glass, the new adaptive material introduced in 2025, permeates practically the whole group (ids wwdc2025_361, wwdc2025_337, wwdc2025_323, wwdc2025_284, wwdc2025_208) as the common thread of this cycle's interface redesign: icons, symbols, SwiftUI and UIKit controls, and even the iPad pointer receive the same translucent, dynamic material language, which reacts to interaction and to the light of the content below.
- There is a recurring discipline of separating "what is drawn" from "what is computed later": icons must be exported flat and opaque, with glass effects applied in Icon Composer (id wwdc2025_361); symbols are drawn as outlined shapes, not just strokes, to allow fine animation control later (id wwdc2025_337). The system consistently separates the source art from the dynamic behavior layer.
- Convergence between SwiftUI and UIKit is explicit and parallel: the videos id wwdc2025_323 and id wwdc2025_284 cover essentially the same concepts (floating tab bars, toolbars with glass, adaptive sheets, GlassEffectContainer/UIGlassContainerEffect) with its own API for each framework, signaling that Apple treats the two frameworks as first-class peers in this redesign.
- A recurring rule of "don't hide it, dim it": both in the iPad menu bar (id wwdc2025_208) and implicitly in the UI writing philosophy (id wwdc2025_404) and in the clarity thesis (id wwdc2025_359), Apple prioritizes spatial and cognitive predictability over space economy: inactive items remain visible and dimmed, screens always answer "where am I / what can I do / where am I going".
- The group mixes traditional interface design sessions with more technical engineering sessions (visionOS/Houdini id wwdc2025_305, video formats id wwdc2025_304, 3D layout in SwiftUI id wwdc2025_273, Foundation Models id wwdc2025_248, Xcode id wwdc2025_247) but all share the same stance: optimizing radically according to how the person will actually experience the product (the Immersive Boundary in id wwdc2025_305, the attention to camera movement in id wwdc2025_304, the on-device model's knowledge limitation in id wwdc2025_248).
- The spatial theme (visionOS) appears in three distinct videos with complementary approaches: geometry/texture optimization (id wwdc2025_305), video formats and presentation (id wwdc2025_304), and declarative 3D layout in SwiftUI (id wwdc2025_273), together they form a relatively complete coverage of how Apple thinks about depth and space as a design dimension, not just a graphics engineering one.
- Writing and content clarity receive treatment equivalent to the visual: the UX writing video (id wwdc2025_404) and the design fundamentals one (id wwdc2025_359) treat text, hierarchy and information structure as part of the same design process, not as a separate or secondary step.

## No transcript

None of the 12 files in this group was left without a transcript; all contained title, source, duration, description and the full spoken transcript.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_361.md, 60 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_337.md, 99 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_305.md, 108 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_404.md, 64 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_304.md, 80 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_323.md, 85 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_208.md, 78 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_284.md, 94 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_273.md, 69 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_359.md, 81 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_248.md, 88 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_247.md, 120 lines read, yes, to the end.

No file was truncated by the Read tool; all fit entirely in a single read (the largest had 120 lines, well below the default limit of 2000 lines).
