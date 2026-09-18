# Foundations (part 1)

## Accessibility (slug: accessibility)

**What it governs:** the principles and standards for making an interface accessible to people with visual, hearing, motor, speech and cognitive disabilities, including minimum sizes, contrast and the behavior of system assistive features.

**Why:** Apple defines an accessible interface as intuitive (familiar and consistent interactions), perceptible (does not depend on a single sensory channel) and adaptable (responds both to the system's accessibility features and to personal configuration preferences). The underlying reasoning is that designing for accessibility broadens the audience and makes the experience more inclusive for everyone, not just for those who use assistive features.

**Do and avoid:**
- Support larger text sizes; ideally allow scaling up by at least 200% (or 140% in watchOS apps), via Dynamic Type or custom UI.
- Follow the recommended default and minimum sizes per platform for custom type styles.
- Consider that thin-weight fonts need sizes larger than recommended to maintain legibility.
- Aim to meet the minimum color contrast standards (WCAG Level AA is used by the Accessibility Inspector).
- If the app does not meet the minimum contrast by default, offer at least a higher-contrast scheme when the system's Increase Contrast setting is active; check contrast in both light and dark mode.
- Prefer system-defined colors, which already have accessible variants that automatically adapt to color preferences.
- Convey information through more than one channel besides color (shapes, icons), because people with color blindness have difficulty with pairs like red-green and blue-orange.
- Describe the app's interface and content for VoiceOver.
- Offer text-based ways to take advantage of audio and video: captions, subtitles, audio description and transcripts, each with a distinct purpose.
- Use haptics in addition to audio cues (e.g.: Music Haptics and Audio graphs on iOS/iPadOS) for those who cannot perceive audio.
- Reinforce audio cues with visual cues, especially in games and spatial apps where important content can be off-screen.
- Offer controls with sufficient size and adequate spacing between them to reduce mistaken taps.
- Support simple gestures for common interactions; avoid custom gestures with multiple fingers or multiple hands.
- Offer alternatives to gestures: make sure the main functionality is accessible through more than one type of physical interaction (e.g.: a button in addition to a swipe to dismiss a view).
- Label interface elements appropriately to allow the use of Voice Control.
- Integrate with Siri and Shortcuts to allow tasks to be performed by voice alone.
- Support assistive technologies related to mobility: VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control and Switch Control.
- Keep actions simple and intuitive; prefer gestures and behaviors already familiar from the system over custom gestures.
- Minimize interface elements with a timer that dismiss themselves; prefer dismissing views with an explicit action.
- Consider offering difficulty accommodations in games (adjusting success criteria, reaction time, control assistance).
- Let people control audio and video playback; avoid autoplay without available and discoverable start/stop controls.
- Allow people to opt out of seeing flashing lights in videos (Dim Flashing Lights setting).
- Be cautious with fast, flashing animations; when Reduce Motion is active, reduce automatic and repetitive animations, including zoom, scale and peripheral motion.
- Additional good practices for reducing motion: tighten animation springs to reduce bounce effects, track animations directly with people's gestures, avoid animating depth changes on the z axis, replace transitions on the x, y and z axes with fades, and avoid animating in and out of blurs.
- Optimize the interface for Assistive Access (iOS/iPadOS): identify the core functionality, remove non-essential flows and elements, split flows into multiple steps across separate screens focused on a single interaction, and always ask for confirmation twice for actions that are hard to reverse, like deleting a file.

**Exact specifications:**

Default and minimum type sizes per platform:
| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Minimum contrast (WCAG Level AA, used by the Accessibility Inspector):
| Text size | Text weight | Minimum contrast ratio |
|---|---|---|
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

Default and minimum control size per platform:
| Platform | Default control size | Minimum control size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Spacing between controls: about 12 points of padding around elements with a bezel; about 24 points of padding around elements without a bezel.

Recommended text scaling: at least 200% (140% on watchOS).

**Platform differences:** the text explicitly states that there are no additional considerations for iOS, iPadOS, macOS, tvOS or watchOS beyond what is already covered. On visionOS, there are specific comfort considerations because of its immersive nature: keeping interface elements within the person's field of view, preferring horizontal layouts over vertical ones (which can cause neck tension), avoiding requiring attention in different locations in rapid succession, reducing the speed and intensity of animated objects (especially in peripheral vision), being careful with camera and video movement, avoiding anchoring content to the person's head (this can prevent the use of Pointer Control) and minimizing the need for large, repetitive gestures. visionOS offers head and hand Pointer Control, and a Zoom feature.

**Links to other articles:** Inclusion, Typography, VoiceOver.

<!-- visual:accessibility -->
### What the illustrations show
Basis: 6 illustration sheets and 4 video sheets (2 videos, 2 sheets each) viewed, all codes checked.
- The opening draws the accessibility symbol in a dark brown silhouette over a yellow gradient, with a dotted rectangular and circular grid and diagonals marking the center and proportions (img 0000); each subtopic (Vision, Hearing, Mobility, Speech, Cognitive) gets the same module, a rounded yellow band with exactly five brown pictograms in equally spaced compartments, changing only the icons (img 0001, 0012, 0014, 0019, 0020).
- Font weight and size are compared using the same word on the same type of light gray card: small and bold on a smaller card, large and thin-weight, with slender strokes, on a larger card (img 0002, 0003).
- Button contrast comes as a right-and-wrong pair with the same pill shape: light blue with a darker blue title that nearly disappears, marked with a gray X (img 0004, 0005), against royal blue with a white title, marked with a green check (img 0006, 0007).
- Adaptive color is demonstrated on a card split in half with the labels "Light" and "Dark": the default systemRed stays practically the same over both backgrounds (img 0008), while the accessible variant darkens and saturates on the light side and lightens, pulling toward pink, on the dark side (img 0009).
- To avoid depending only on color, two green and red circles that differ only in hue (img 0010) gain shape and symbol: a white check on the green one and an octagon with a white X on the red one (img 0011).
- Under hearing, an iPhone in black outline with vibration lines on the sides and a dark bubble with a music note above it shows music accompanied by vibration (img 0013).
- Spacing between controls appears in two states of the same row of three round blue buttons (back, play, forward): with generous room (img 0015) and with dashed red outlines over the tap areas, touching each other with no space between them (img 0016).
- The gesture alternative is shown in the same list: in edit mode, each row has an always-visible red minus button (img 0017); with a swipe, a row slides and the "Delete" button covers part of the title and subtitle (img 0018).
- Assistive Access simplifies the Camera on a black background: the first screen has only three large targets, two squares side by side (yellow for photo, green for video) and a black back button at the bottom (img 0021); the next screen swaps the two options for a large preview, a yellow button to take a photo and the back button (img 0022).
- Zoom on visionOS is a circular lens with a gray outline over a floating window in a real home environment, magnifying only the region beneath it, unlike the flat illustrations in the rest of the page (img 0023).
- In the hand Pointer Control video, a straight white line with a dot at the tip goes from the hand to a yellow star over the engine photo in the "Rockets" window; the hand is open and nearly still (q001 to q003), brings thumb and index finger together (q004 to q006), opens again (q007 to q009), continues in a light pinch (q010 to q012) and at q013 gets closer to the bottom right corner of the window; the origin and angle of the line change, and the star never moves from its spot (video 000, sheets 0001 and 0002, q001 to q013).
- In the head Pointer Control video, no hand appears: the star stays still a little to the left of the center of the screen while the window and the environment rotate to one side (q001 to q003), stabilize with the window larger and centered (q004 to q006), rotate in the opposite direction (q007 to q009), keep rotating and reveal more armchairs on the right (q010 to q012), smoothly reverse again (q013 to q015) and at q016 return close to the initial framing; the content moves under a fixed target, instead of a cursor moving over still content (video 001, sheets 0001 and 0002, q001 to q016).
Recorded divergences: in video 000, the official description speaks of a line whose pointer changes position as the hand moves, but in the 13 frames sampled every 0.5 s the destination (the star) always stays at the same point and only the origin and angle of the line vary. In video 001 the description checks out, but it does not mention the back-and-forth oscillation of the rotation or the return close to the initial framing.
<!-- /visual:accessibility -->

## App icons (slug: app-icons)

**What it governs:** how to design the app icon, including layered structure, shape, visual effects, appearances (light/dark/tinted/light translucent) and technical specifications per platform.

**Why:** the icon is a crucial element of the brand and the user experience because it appears in multiple places across the system (Home Screen, search, notifications, settings, sharing). Layers give more control over how the design is represented, allowing the system to apply visual effects that respond to the environment and to people's interactions, creating a sense of depth and vitality. Simplicity is valued because icons with too many fine details become "busy" when the system applies shadows and highlights, and details become hard to perceive at small sizes.

**Do and avoid:**
- Prefer clearly defined edges on foreground layers; avoid soft, faded edges so that highlights and shadows drawn by the system look good.
- Vary the opacity of the foreground layers to increase the sense of depth and vividness.
- Design a background that stands out while also emphasizing the foreground content; if using a gradient, make sure it responds well to the system's lighting effects.
- Prefer vector graphics (SVG or PDF) when bringing layers into Icon Composer; for mesh gradients and rasterized artwork, prefer PNG.
- Produce layers without a mask, in the appropriate shape (square for iOS/iPadOS/macOS/visionOS/watchOS, rectangular for tvOS), letting the system apply the final masking.
- Keep the main content centered to avoid clipping when the system adjusts corners or applies a mask.
- Embrace simplicity: find a concept or element that captures the essence of the app, with a minimal number of shapes.
- Prefer a simple background (solid color or gradient) that emphasizes the main design.
- Provide a visually consistent icon design across all supported platforms.
- Consider basing the design on overlapping solid shapes, especially combined with transparency and blur, to give a sense of depth.
- Include text only when essential; text does not support accessibility or localization, tends to be too small to read, and can make the icon look busy. Avoid nonessential words like "Watch", "Play", "New" or "For visionOS".
- Prefer illustrations over photos, and avoid replicating UI components or screenshots of the app itself.
- Don't use replicas of Apple hardware products (protected by copyright).
- Let the system take care of blur and other visual effects; there is no need to include specular highlights, shadows between layers, beveled edges, blurs or glows.
- Create layer groups to apply effects to multiple layers at once, when it makes sense for the design.
- Keep the icon's visual assets consistent across appearances (default, dark, light translucent, tinted); avoid swapping elements between variants.
- Use the light icon as the basis for the dark icon, choosing complementary colors and avoiding excessively bright images.
- Consider offering alternate icons on iOS, iPadOS, tvOS and compatible apps running on visionOS; each alternate icon needs to remain related to the app's content and experience, and alternate icons on iOS/iPadOS require their own dark, light translucent and tinted variants.

**Exact specifications:**

Layout, final shape, size, style and appearances by platform:
| Platform | Layout shape | Icon shape after masking | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, light translucent, dark translucent, light tinted, dark tinted |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

Supported color spaces: sRGB (color), Gray Gamma 2.2 (grayscale), Display P3 (wide-gamut color on iOS, iPadOS, macOS, tvOS and watchOS only).

Layers on tvOS: between two and five layers.
Layers on visionOS: one background layer plus one or two overlapping layers.
Layers on iOS, iPadOS, macOS and watchOS: one background layer and one or more foreground layers.

**Platform differences:** iOS, iPadOS and macOS use square icons masked to rounded corners that match the curvature of other elements and the device's own bezel. tvOS uses rectangular icons, also with concentric edges; it requires a safe zone because the system can crop content at the edges during focus and the parallax effect, and it is recommended to avoid black in the icon background according to the text about watchOS (to avoid the icon blending into the display background, applicable to watchOS). On visionOS and watchOS, the mask is circular; on visionOS, avoid shapes that look like a hole or concave area in the background, since the system's shadow and specular highlights would make the shape stand out instead of recede.

**Links to other articles:** Apple Design Resources, Icon Composer, Icons, Images, Dark Mode.

<!-- visual:app-icons -->
### What the illustrations show
Basis: 6 illustration sheets and 2 video sheets (1 video) viewed, all codes checked; some of the illustrations have a light and dark version.
- The opening is the sketch of the App Store "A" over yellow, with a dashed rectangular, circular and diagonal grid, an inscribed circle and diagonals crossing the corners; in the light version there is a second rounded square offset behind the main one, which disappears in the dark version, where the background turns a darker gold and the icon light yellow, inverting the contrast (img 0077).
- The same Photos flower only swaps its frame by platform, with identical inner content: rounded square for iOS, iPadOS and macOS, elongated rounded rectangle for tvOS and circle for visionOS and watchOS; in the dark version only the page background turns black and the icons stay light (img 0078).
- Icon Composer appears as a real tool: named layers in nested groups on the left, the assembled flower in the center and, on the right, the properties of the selected layer, with 100% opacity, normal blend mode, solid fill, "Liquid Glass Effects" on, SVG image, x and y position at 0 pt and 100% scale; in dark mode the interface darkens and the artwork keeps its colors (img 0079).
- The Settings gear is built over a double checkered grid (thin modules and a coarser mesh on top), a large inscribed circle touching the inner edges, a smaller concentric circle and diagonals in an X from corner to corner (img 0080); the same grid is reapplied to the tvOS rectangle, with the checkered pattern and diagonals stretched and the circles still centered (img 0081), and to the circle, with the grid inscribed in an imaginary square (img 0082).
- In the dark versions of these grids, the gear and the position of each guide don't change; background and lines switch to black and white, and the fine checkered pattern disappears in the tvOS rectangle and becomes subtle near the edges of the circle, leaving the reference circle and diagonals (img 0080, 0081, 0082).
- Economy of shapes is shown in system icons: Podcasts, in purple, with concentric circles that taper to a light center from which an elongated drop descends (img 0083), and Home, in white, with an orange house in nested layers down to a beige door, plus a side chimney (img 0084).
- Depth through overlap is taught with a correct version and an incorrect version over a checkered transparency background, using the same pair of concentric blue circles: the first version gets the gray X badge (img 0085, 0086); in the approved one, the outer circle has no outline and has a semitransparent fill that lets the checkerboard show through, and the solid circle looks like it's resting on top of it, with a green check badge (img 0087, 0088).
- The appearances form a 3 by 2 grid with the Photos flower and a label under each cell: on top, colored default, light translucent (translucent gray background, flower in gray and white) and light tinted (purple background, flower in light purple); on the bottom, dark (black background, colored flower), dark translucent (translucent black background, gray flower) and dark tinted (purplish black, flower in dark purple). In the dark version of the sheet only the page background changes (img 0089).
- The tvOS safe zone is a white dashed rectangle inside the grayish blue icon, pointed to by the "Safe zone" callout; the gear fits entirely inside it, with visible margin to the outer edge, and in dark mode only the surrounding page changes (img 0090).
- In the video, the visionOS home screen shows circular icons over the blurred real environment in two rows: the front one sharp (Safari, Photos, Notes) and the back one blurred and cropped at the top, which suggests a focus hierarchy by sharpness and blur, not by scale (video 004, sheet 0001, q001 to q009).
- In the Photos icon, q001 shows petals with less shine and, from q004 to q009, the white background seems to move forward slightly and the petals gain definition, which suggests a small change in depth between the layers, with no perceptible lateral shift of the icon on the screen (video 004, sheet 0001, q001 to q009).
- In the second sheet, Freeform enters to the left of Safari and Notes exits to the right, with the rest of the composition stable from q010 to q015, which shows the row of icons scrolling horizontally (video 004, sheet 0002, q010 to q015).
Recorded divergences: the official video description talks about movement to show parallax in the Photos icon, but the frames show only a subtle variation in sharpness and depth between the layers, with no perceptible lateral shift; the swap of icons in the row (Freeform enters, Notes exits) is not mentioned in the description.
<!-- /visual:app-icons -->

## Branding (slug: branding)

**What it governs:** how to express an app's or game's brand identity in a recognizable way, without compromising the platform's familiarity and consistent experience.

**Why:** the central logic is that the brand should reinforce, not compete with, the platform experience and the app's content. Using patterns and components that are already familiar makes the experience feel trustworthy from the start, allowing people to focus on what makes the app unique. Screen space used only to display a brand asset is space taken away from the content people actually want.

**Do and avoid:**
- Use the brand's exclusive voice and tone in all written communication.
- Apply the brand's accent color with judgment; using it too broadly can overload the interface and dilute its impact. Minimize its use in controls and reserve it for primary actions or status indicators (such as unread content badges, or the icon of the selected tab in a tab bar). To express the brand through color, consider moving the color to the content layer, where it scrolls under controls in Liquid Glass and is dynamically picked up.
- Consider using a custom font, as long as it's legible at all sizes and compatible with accessibility features like bold text and Dynamic Type; it can work well to use the custom font for titles and subtitles while using system fonts for body text and captions.
- Express the brand using familiar components; when customizing a component's appearance, make sure size, positioning and behavior continue to preserve an experience that is familiar and appropriate for the platform.
- Make sure the brand always yields space to the content; incorporate the brand in a refined and discreet way.
- Help people feel comfortable by using consistent patterns: position the UI in expected places, use standard symbols for common actions, rely on established navigation and modality conventions.
- Resist the temptation to display the logo repeatedly throughout the app, unless it's essential to provide context.
- Avoid using a launch screen as a branding opportunity, since it disappears too quickly to convey information; consider instead a welcome or onboarding screen that incorporates brand content at the start of the experience.
- Follow Apple's trademark guidelines; Apple trademarks can't appear in the app's name or images.

**Exact specifications:** the text does not include numbers, measurements or specific values on this page.

**Platform differences:** the text explicitly states that there are no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

**Links to other articles:** App Store Marketing Guidelines, Show more with app previews, Color.

<!-- visual:branding -->
### What the illustrations show
Basis: 2 illustration sheets viewed (2 of 2), all codes checked; no video listed for the page.
- The opening is a megaphone in dark brown outline over a yellow gradient, with a rectangular dashed grid and a centered circle serving as a construction guide; according to the official description, the megaphone suggests communication and yellow is one of the six colors of the Apple logo (img 0184).
- The example to avoid is Maps on iPhone with the map in near-monochromatic light gray, points of interest in bright red, a location pin in a tone between purple and blue and the blue accent color spread across the controls: search bar and circular navigation button (img 0185).
- The recommended example repeats the same composition of the airport map, but moves the blue to the content layer, with the map in light and medium blue tones and buildings in blue, without applying the color to the controls; the points of interest remain red to maintain contrast (img 0187).
- The two examples are near-identical variations of the same map, with the layout reused for the before and after; what sets them apart is where the brand color is applied, on the controls or on the content (img 0185, img 0187).
- The judgment comes from a fixed pair of seals, always isolated and centered on a white background, with no interface element: gray X in a light gray circle for wrong (img 0186) and green check in a green circle for right (img 0188).
- The two sheets contain only light versions of the images (img 0184 to 0188).
<!-- /visual:branding -->

## Color (slug: color)

**What it governs:** the use of color in apps and games, including system colors, custom colors, color in Liquid Glass, color space management, and the platform-specific definitions of dynamic colors.

**Why:** judicious use of color improves communication, evokes the brand, provides visual continuity, communicates status and feedback, and helps people understand information. System colors are already defined to work well across different backgrounds and appearance modes, and can automatically adapt to vibrancy and accessibility settings, which makes the experience feel "at home" on the device.

**Do and avoid:**
- Avoid using the same color to mean different things; use color consistently, especially when it communicates status or interactivity.
- Make sure all the app's colors work well in light, dark and increased contrast contexts; when possible, use system colors, which already define variants for these contexts. If you define a custom color, provide light and dark variants, and an increased contrast option for each variant. Even if the app has only one appearance mode, provide light and dark colors to support Liquid Glass adaptivity.
- Test the app's color scheme under different lighting conditions (strong light makes colors darker and duller; dark environments make colors brighter and more saturated); in visionOS, colors can look different as the colors of the surrounding physical environment reflect light.
- Test the app on different devices, including True Tone displays and different color profiles.
- Consider how artwork and translucency affect nearby colors.
- If the app allows people to choose colors, prefer the color controls provided by the system.
- Avoid relying only on color to differentiate objects, indicate interactivity or communicate essential information; offer the same information in an alternative way (text labels, glyph shapes).
- Avoid colors that make content harder to perceive; insufficient contrast makes icons and text blend into the background.
- Consider how the colors used may be perceived in other countries and cultures (e.g.: red communicates danger in some cultures, but has a positive connotation in others).
- Avoid encoding system color values directly in the code (hard-code); the actual values can fluctuate between versions. Use APIs such as Color to apply system colors.
- Avoid redefining the semantic meaning of dynamic system colors (e.g.: do not use the separator color as a text color).
- In Liquid Glass, apply color with restraint to the material and to symbols or text over the material; reserve color for elements that truly benefit from emphasis, such as status indicators or primary actions. To emphasize primary actions, apply color to the background, not to symbols or text. Avoid adding color to the background of multiple controls at the same time.
- Avoid using similar colors in control labels if the app has a colored background; prefer a monochromatic appearance for toolbars and tab bars in apps with visually rich backgrounds, or choose an accent color with enough visual differentiation.
- Pay attention to the position of color in the content layer, avoiding overlap of similar colors between the content layer and the controls.
- Apply color profiles to images to ensure colors appear as intended on different displays.
- Use wide color to improve the visual experience on compatible displays; when appropriate, use the Display P3 color profile at 16 bits per pixel (per channel) and export images in PNG.
- Provide image and color variations specific to the color space, if necessary, to avoid clipped gradient problems on sRGB displays.

**Exact specifications:**

Minimum contrast between colors (Dark Mode, Color article): contrast ratio no lower than 4.5:1; for custom foreground and background colors, aim for a 7:1 ratio, especially in small text (this specification appears in the Dark Mode article, referenced from Color).

System colors (RGB values, default light and dark appearance, and increased contrast light and dark): Red, Orange, Yellow, Green, Mint, Teal, Cyan, Blue, Indigo, Purple, Pink, Brown, each with four RGB value variants documented in the page's specifications table (Default light, Default dark, Increased contrast light, Increased contrast dark). visionOS uses the default dark color values for the system colors.

System gray colors on iOS/iPadOS: systemGray, systemGray2, systemGray3, systemGray4, systemGray5, systemGray6, each with RGB value variants for default light, default dark, increased contrast light and increased contrast dark.

Wide color profile: Display P3 at 16 bits per pixel (per channel), PNG export format.

**Platform differences:**
- iOS, iPadOS: defines two sets of dynamic background colors (system and grouped), each with primary, secondary and tertiary variants; defines dynamic foreground colors such as label, secondaryLabel, tertiaryLabel, quaternaryLabel, placeholderText, separator, opaqueSeparator and link.
- macOS: defines an extensive list of dynamic system colors (e.g.: controlAccentColor, controlBackgroundColor, labelColor, linkColor, separatorColor, windowBackgroundColor, among others), also accessible in the standard color panel. Starting with macOS 11, it is possible to specify an app accent color to customize buttons, selection highlight and sidebar icons; if the person sets their system accent color to something other than "multicolor", the system replaces the app's color with the chosen one, except for sidebar icons with a fixed color.
- tvOS: consider a limited color palette that matches the app's logo; avoid using only color to indicate focus (subtle scale and responsive animation are the primary means).
- visionOS: use color with restraint, especially over glass, since the default Material lets light and objects from the physical environment show through the glass, affecting legibility; prefer color on bold text and large areas; in a fully immersive experience, maintain balanced brightness levels for visual comfort, avoiding very bright objects over very dark backgrounds.
- watchOS: use background color to support existing content or provide additional information (e.g.: each infographic view in Activity has a background that matches the ring color); avoid full-screen background color in views that stay visible for long periods, such as workout or audio playback; recognize that graphic complications may prefer tinted mode (a single color based on the color selected by the person) instead of full color.

**Links to other articles:** Dark Mode, Accessibility, Materials, Apple Design Resources.

<!-- visual:color -->
### What the illustrations show
Basis: 42 illustration sheets viewed (hig-img_color), all opened and with codes checked; the page has no video.
- The opening illustration draws a painter's palette with a dotted construction grid overlaid, with vertical lines, horizontal lines and a concentric circle. In the dark version the luminosity relationship reverses: the palette, previously darker than the yellow background, becomes cream over a mustard background (img 0254).
- The same Notes screen appears in four versions with identical composition: default light, increased contrast light, default dark and increased contrast dark. The confirmation button in the top right corner keeps the yellow background in Liquid Glass in all four; what changes is the symbol, white in the default versions and black in the increased contrast ones. The text selection uses a light yellow highlight behind the word, with the text editing menu visible (img 0255, 0256, 0257, 0258).
- Cultural inclusion of color is shown with the same Stocks chart, the same values and the same curve: in English the rise is a green line with a green gradient that dissolves into transparent below it; in Chinese the same rise is red, with the period tabs translated and the one-month period selected in both (img 0259, 0260).
- Color in Liquid Glass is taught with isolated crops of the control, with no device frame. The blue circular button with a white check does not change tone over a white background and over a black background; only the surrounding background inverts (img 0261).
- In the capsule tab bar, with well-rounded corners and a light shadow, the selected item carries blue on the icon and the label and gains a slightly grayed background behind the icon. The unselected item never receives the accent color: black icon in light, white in dark, gray label; in dark the bar becomes translucent and dark (img 0262).
- The glass absorbs the color of the content behind it: a share button over a photo of flowers and a mountain appears visibly tinted pink and blue (img 0263).
- The pair of excessive use and restrained use reuses the same toolbar above a bold title, with an X on the left, a pair of buttons in the center and a check on the right. In one version the three controls have a blue background; in the other only the check has a blue one and the rest stay in neutral gray, light in light mode and dark in dark mode. In the version with all three blue, between the modes only the screen background and the title change, which turns white in dark (img 0264, 0266). The isolated example markers appear as a gray circle with a white X and a green circle with a white check, with no text (img 0265, 0267).
- Color space management is explained with the tongue-shaped chromaticity diagram and two black-outline triangles: the larger one labeled Display P3 contains the smaller one labeled sRGB. In the dark version only the surrounding background changes (img 0268).
- The macOS accent color appears as an actual settings panel: the color row has nine circles in fixed order (multicolor, blue, purple, pink, red, orange, yellow, green, gray), multicolor selected with a blue ring, and below it the text highlight color selector with a gradient circle. The dark version keeps the order and selection (img 0269).
- The system colors are documented as minimal cards: a square with rounded corners with the three RGB values written next to it, with no color name or usage context. Each card is shown over a white background and over a black background with an identical value, so that only the background changes. The cards come in blocks of four per hue, and the third of each block is always the darkest; in red, for example, 255, 56, 60, then 255, 66, 69, then 233, 21, 45 and finally 255, 97, 101 (img 0270 to 0317). Inference: the count of four per hue matches the four variants the text documents, but the images do not label which card is which variant.
- The iOS and iPadOS grayscale uses the same card format across 24 images, out of luminosity order, with values between 28, 28, 30 at the darkest and 242, 242, 247 at the lightest. Some values repeat in different positions (142, 142, 147 in img 0318, 0319 and 0324; 174, 174, 178 in img 0321, 0322 and 0328). At the extremes the contrast with the background drops a lot: the lightest gray has very subtle contrast over white, and the darkest becomes nearly indistinguishable over black (img 0318 to 0341).

Recorded divergences: the official caption treats img 0265 as a mark of incorrect use, but the image shows only a neutral gray button with a white X, with no visual sign of error.
<!-- /visual:color -->

## Dark Mode (slug: dark-mode)

**What it governs:** the systemwide dark appearance setting, including the color palette, the use of icons and images, and the treatment of text in dark appearance.

**Why:** Dark Mode provides a comfortable viewing experience adapted to low-light environments. People expect apps to respect this systemwide preference; having an app-specific appearance setting creates extra work for people, who would have to adjust more than one setting, and can give the impression that the app is broken for not responding to the systemwide choice.

**Do and avoid:**
- Avoid offering an app-specific appearance setting.
- Make sure the app looks good in both appearance modes, including the Auto setting, which switches between light and dark as conditions change throughout the day, potentially while the app is running.
- Test content to ensure comfortable readability in both modes, including with Increase Contrast and Reduce Transparency turned on (separately and together); pay special attention to dark text on a dark background in Dark Mode.
- In rare cases, consider using only a dark appearance in the interface, for example in an app that supports immersive media viewing, so the UI recedes and helps focus on the content.
- Embrace colors that adapt to the current appearance: semantic colors (such as labelColor and controlColor on macOS, or separator on iOS/iPadOS) adapt automatically. For a custom color, add a Color Set asset in the Xcode asset catalog, specifying the light and dark variants. Avoid fixed color values that do not adapt.
- Soften the color of white backgrounds: if displaying a content image with a white background, consider slightly darkening the image to avoid the background "glowing" in the context of Dark Mode.
- Use SF Symbols whenever possible, since they adapt automatically to Dark Mode.
- Design separate interface icons for light and dark appearances, if necessary (e.g., a full moon icon might need a subtle dark outline on a light background, but none on a dark background).
- Make sure colored images and icons look good in both appearances; use the same asset if it works in both, or create separate assets via the asset catalog.
- Use the label colors provided by the system, which adapt automatically.
- Use system views to draw fields and text views, so the text looks good on all backgrounds, automatically adjusting to the presence or absence of vibrancy.

**Exact specifications:**
- Minimum contrast ratio between colors: 4.5:1.
- For custom foreground and background colors, aim for a contrast ratio of 7:1, especially in small text.

**Platform differences:** the text states that there are no additional considerations for tvOS, and that Dark Mode is not supported on visionOS or watchOS.
- iOS, iPadOS: uses two sets of background colors in Dark Mode, called base and elevated, to reinforce the perception of depth when one dark interface is layered over another. The base colors are darker (making background interfaces appear to recede) and the elevated colors are lighter (making foreground interfaces appear to advance). The system automatically switches from base to elevated when an interface is in the foreground, such as a popover or modal sheet, and also uses the elevated color to give visual separation between apps in multitasking and between windows.
- macOS: when the person chooses the "graphite" accent color in General settings, macOS makes window backgrounds pick up color from the current desktop wallpaper (called desktop tinting). It is recommended to include some transparency in custom component backgrounds when appropriate, so they pick up color from the window background when desktop tinting is active, but only in components with a visible background or bezel, and only in a neutral state (with no use of color).

**Links to other articles:** Color, Materials, Typography, Accessibility.

<!-- visual:dark-mode -->
### What the illustrations show
Basis: 4 illustration sheets viewed (hig-img_dark-mode), all opened and with codes checked; the page has no video.
- The opening illustration shows three concentric rings, each with half filled in brown and half empty, alternating the side between rings, with a dotted construction grid of rectangular and diagonal lines overlaid. In the dark version the background becomes golden and the previously brown halves become near-white yellow: figure and background swap roles, keeping the same yellow hue, instead of a simple swap of black for white (img 0411).
- A real screenshot of Stocks on iPhone in dark mode shows the entire construction on a black background: header with S&P 500 and AAPL, black card with the stock detail, green line chart of the last month and data table below, with text in white and green (img 0412).
- The system colors are presented as a 2 by 2 grid of swatches (blue, green, purple, magenta) inside a rounded square. In the pair, the square goes from light gray to near black and the four swatches shift only slightly in saturation, without losing their identity (img 0413, 0414).
- For a simple icon, the solution is an outline: the solid black drop does not need an outline on a white background, and on a black background the same black shape gains a thin white outline that keeps it visible (img 0415, 0416).
- For a complex illustration, the solution is to redo the internal values, not to add an outline. The line-drawn scene of two people at a round table, legible on white, loses its outlines when placed on black, because dark hair, clothing and chairs blend into the background; in the corrected version clothing and chairs become white or light gray and the hair lightens, and the scene reads again (img 0417, 0418, 0419).
- The text pair shows the label word in black on white, loose and without a button shape, and then in white inside a centered black rectangle with rounded corners, where the button shape appears drawn (img 0420, 0421).
- The label hierarchy is a scale of four stacked lines with decreasing contrast: label at maximum contrast, secondaryLabel in light gray, tertiaryLabel in medium gray and quaternaryLabel in dark gray, nearly invisible. The same scale repeats, in the same order, on black (base), on dark gray slightly lighter than black (elevated) and on white, where label becomes black (img 0422, 0423, 0424).

Recorded divergences: the official description of img 0420 refers to an illustration of a button in the light appearance, but the image shows only the loose word, with no rectangle, outline or button fill.
<!-- /visual:dark-mode -->

## Icons (slug: icons)

**What it governs:** the design of interface icons (glyphs), distinct from app icons: their simplicity, visual consistency, optical alignment, file format, and the standard SF Symbols catalog for common actions. It also covers document icons on macOS.

**Why:** unlike an app icon, which can use rich visual detail, an interface icon needs to communicate a single idea instantly and universally. Too much detail makes the icon confusing or illegible; familiar visual shapes directly related to the action or content make recognition faster.

**Do and avoid:**
- Create a recognizable, highly simplified design, using familiar visual metaphors.
- Maintain visual consistency across all of the app's interface icons: consistent size, level of detail, stroke weight and perspective, whether custom or system icons.
- Match the weight of interface icons to the weight of adjacent text, unless you want to emphasize one or the other.
- If necessary, add padding to a custom icon to achieve optical alignment (not just geometric), especially for asymmetrical icons.
- Provide a selected-state version of an interface icon only if necessary; standard system components (toolbars, tab bars, buttons) already update the selected-state appearance automatically.
- Use inclusive imagery: prefer gender-neutral human figures and avoid images that are hard to recognize across different cultures or languages.
- Include text in the design only when essential to the meaning; if you need to show individual characters, localize them; if you need to suggest a stretch of text, draw an abstract representation and include a mirrored version for right-to-left contexts.
- If you create a custom interface icon, use a vector format such as PDF or SVG, which scales automatically for high-resolution displays; alternatively, create a custom SF Symbol.
- Provide alternative text labels (accessibility descriptions) for custom interface icons, so VoiceOver can describe them.
- Avoid using replicas of Apple hardware products; use only images available in Apple Design Resources or the SF Symbols that represent Apple products.

**Exact specifications:** the page includes an extensive table of "standard icons" mapping common actions (Cut, Copy, Paste, Done, Cancel, Delete, Undo, Redo, Compose, Duplicate, Rename, Move to, Attach, Add, More, Select, Deselect, Superscript, Subscript, Bold, Italic, Underline, Align Left, Center, Justified, Align Right, Search, Find, Filter, Share, Print, Account, Dislike, Like, Bring to Front, Send to Back, Bring Forward, Send Backward, Alarm, Archive, Calendar) to the exact names of the corresponding SF Symbols (e.g., `scissors`, `document.on.document`, `checkmark`, `xmark`, `trash`, `arrow.uturn.backward`, `square.and.pencil`, `folder`, `paperclip`, `plus`, `ellipsis`, `checkmark.circle`, `textformat.superscript`, `bold`, `italic`, `underline`, `text.alignleft`, `magnifyingglass`, `square.and.arrow.up`, `printer`, `person.crop.circle`, `hand.thumbsdown`, `hand.thumbsup`, `square.3.layers.3d.top.filled`, `square.3.layers.3d.bottom.filled`, `alarm`, `archivebox`, `calendar`, among others listed).

Document icons on macOS, background image sizes (background fill):
- 512x512 px @1x, 1024x1024 px @2x
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

Center image sizes (center image), measuring half the canvas of the document icon:
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

Margin for the center image: about 10% of the image canvas; the image should occupy about 80% of the canvas (e.g., on a 256x256 px canvas, most of the center image would fit in an area of 205x205 px).

Smallest display size of a document icon: 16x16 px.

**Platform differences:** the text states that there are no additional considerations for iOS, iPadOS, tvOS, visionOS, or watchOS.
- macOS: covers document icons in detail, traditionally with a paper appearance with the top right corner folded down; if the app does not provide a document icon for a supported file type, macOS automatically creates one by composing the app icon with the file extension. It is possible to provide a background fill, center image, and text; important content should be avoided in the top right corner of the background, since the system draws the white fold there. The system displays the file extension at the base of the icon by default, but it is possible to provide a more descriptive term (e.g., "scene" instead of "scn"); the system automatically capitalizes each letter of the text.

**Links to other articles:** App icons, SF Symbols.

<!-- visual:icons -->
### What the illustrations show
Basis: 29 illustration sheets viewed (hig-img_icons), all opened and with checked codes; the page has no video.
- The opening illustration shows the Command key symbol with construction guides on top, made of straight lines and a dashed circle. In the dark version the stroke becomes cream on a darker, opaque gold background, and the grid remains visible, more subtle (img 0561).
- Size consistency is taught with a strip of four solid glyphs (camera, heart, envelope, alarm clock) between two dashed lines that mark the common height limit, with a solid red line in the middle marking the optical center. Only the alarm clock's bells go a little past the top line, and only in the fine details, not in the body. In a second version the internal details (camera lens, envelope lines) appear in blue as a didactic marking. In the dark the strip turns burgundy, the glyphs turn cream, and the guides stay in the same place (img 0562, 0563).
- Optical centering comes in three steps over the same download glyph inside a disc. First, pink bars of equal height at the top and bottom mark the geometric center. Then the glyph moves up a few pixels relative to those bars, leaving more space at the bottom, and a translucent pink rectangle over the glyph shows the padding that already incorporates the offset. Finally, the two discs appear side by side with no marking at all, and the difference is only a slight vertical offset. In the dark versions the discs and glyph invert color, but markings and measurements do not move (img 0564, 0565, 0566).
- The selected state appears in a toolbar capsule with two buttons on a shared background: the active one, larger, has the whole circle filled with blue with the filter glyph in white; the inactive one shows only the ellipsis in a neutral color over the capsule's light gray. In the dark the selected blue does not change, and the ellipsis goes from black to white (img 0567).
- Glyph localization is shown in the SF Symbols app panel itself: a large frame with the symbol, the technical name in bold underneath, and a localization list with one line per language, each with the thumbnail of the localized character on the left and the name on the right. For the text page symbol, the list has two lines, left to right and right to left, each thumbnail showing the text lines in the corresponding orientation (img 0568, 0569).
- Standard action icons are presented as a single glyph, isolated and centered, without grid or card, black on white and white on black with identical shape (img 0570 to 0610). Inverse actions are the horizontal mirroring of the same curved arrow, as in undo and redo (img 0576, 0577). The same pencil changes meaning through composition: alone for rename, overlapping the corner of a square to compose (img 0578, 0580). Select is a check inside an outline-only circle; deselect is a loose X, with no frame (img 0585, 0586).
- Formatting icons use the letter itself as the body and apply to it the variation that the action represents: A with a small 1 above or below, B in much heavier weight, I in italic, U with a stroke of the same thickness right below (img 0587 to 0591). The four alignment icons are always four stacked lines, and only the alignment varies: edges on the left, center axis, edges on the right mirroring the first, and all widths equal in justified (img 0592 to 0595).
- Composite glyphs and hierarchy by fill: locate overlaps a small magnifying glass on the bottom right corner of a document with lines (img 0597); the user account is an outline circle with abstract head and shoulders, no face, the shoulders cut off by the edge (img 0601); like and dislike use the same hand only in outline, with the thumb pointing up or down (img 0602, 0603). In layer ordering, isometric diamonds stacked diagonally, three for front and back and two for moving a layer forward and backward, indicate the layer in focus only through solid fill against outline, without changing shape (img 0604 to 0607).
- macOS document icons share the same sheet silhouette with the top right corner folded down and vary only in background, center image, and label in capitals at the base (JPG in gray; AR OBJECT, SWIFT, and SCENE). The project one fills the entire body in blue, with the label in a horizontal band at the base, and the TextEdit one fills the body with a page of running text, with no center symbol or visible label (img 0611, 0612, 0613, 0614, 0619, 0624).
- The layered composition appears disassembled before the result: first the background fill alone, a pink grid that lightens toward the bottom, cut by a white electrocardiogram line and with no page outline; then the isolated red heart; then the label word in gray, which in the dark becomes light gray and not pure white; and finally the three layers composited in the document icon (img 0615, 0616, 0617, 0618).
- The same art simplifies as it shrinks: in the first reduction, pixelated, the grid has fewer lines, the electrocardiogram thickens and the text still appears; in the next one the grid disappears, the text becomes illegible and the heart remains recognizable; at the minimum only the blurred heart remains in a very light pink square (img 0618, 0620, 0621, 0622).
- The icon's margin is the only numeric measurement annotated on the page: an outer pink square with a white square centered inside, the heart occupying almost all of the white, and a bracket at the top with the 10% mark for the margin width. In the dark the margin turns burgundy and the inner square turns black, with the mark in the same place (img 0623).

Recorded divergences: in img 0623 the margin appears in pink, while the official alt text says blue. In img 0564 the alt text talks about bars in both images, but the marking appears only in the figure on the right.
<!-- /visual:icons -->

## Images (slug: images)

**What it governs:** how to deliver art with resolution, format, and scale appropriate for each device and platform, including scale factor, recommended file formats, layered images with parallax effect (tvOS), photos and spatial scenes (visionOS), and self-scaling PDFs (watchOS).

**Why:** different devices display images at different resolutions; a point is an abstract unit of measure that keeps visual content consistent regardless of how it is displayed. Providing high-resolution assets for each scale factor ensures the art does not become pixelated, stretched, or compressed at different pixel densities.

**Do and avoid:**
- Provide high-resolution assets for all of the app's bitmap images, for each supported device, identifying the scale factor with "@1x", "@2x", or "@3x" in the file name.
- In general, design images at the lowest resolution and scale up to create the high-resolution assets; when using resizable vector shapes, position control points at integer values for clean alignment at 1x (which stays aligned at 2x and 3x, multiples of 1x).
- Include a color profile in each image.
- Always test images on a variety of real devices.
- In tvOS, use standard interface elements to display layered images, so that they receive the parallax treatment automatically when they come into focus.
- In tvOS, identify logical foreground, middle, and background layers: foreground for prominent elements (game character, text on album cover or poster), middle for secondary content and effects such as shadows, background as an opaque backdrop.
- In tvOS, keep text in the foreground, unless you want to obscure it.
- In tvOS, keep the background layer opaque (required; generates an error if it is not opaque).
- In tvOS, keep the layer simple and subtle (the parallax is designed to be nearly imperceptible).
- In tvOS, leave a safe zone around the foreground layers, since content can be cut off when the layered image scales and moves when focused.
- In tvOS, always preview layered images throughout the design process, and finally on a real TV.
- In visionOS, prefer vector art for 2D images, avoiding bitmap content that may not scale well.
- In visionOS, if you need to use rasterized images, balance quality and performance when choosing the resolution; resolutions above @6x can impact runtime performance.
- In visionOS, for spatial photos, use the stereo HEIC format; prefer the feathered glass background effect to display text over spatial photos.
- In visionOS, display photos and spatial scenes in isolated views (not embedded together with other content), to avoid visual discomfort.
- In watchOS, in general avoid transparency to keep image files small, except in complication images, menu icons, and other interface icons that serve as template images, where the system uses transparency to determine where to apply color.
- In watchOS, use self-scaling PDFs to provide a single asset for all screen sizes, designing for the 40mm and 42mm screens at 2x.

**Exact specifications:**

Recommended scale factors by platform:
| Platform | Scale factors |
|---|---|
| iPadOS, watchOS | @2x |
| iOS | @2x and @3x |
| visionOS | @2x or higher |
| macOS, tvOS | @1x and @2x |

Recommended formats by image type:
| Image type | Format |
|---|---|
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that do not require 24-bit full color | 8-bit palette |
| Photos | JPEG files (optimized) or HEIC |
| Stereo or spatial photos | Stereo HEIC |
| Flat icons and other flat art that need scaling at high resolution | PDF or SVG |

Image scale for self-scaling PDF in watchOS, by screen size:
| Screen size | Image scale |
|---|---|
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

Layers in layered images (tvOS): between two and five distinct layers.

**Platform differences:** the text states that there are no additional considerations for iOS, iPadOS or macOS.
- tvOS: covers the parallax effect and layered images in detail; layered images are required for the tvOS app icon, and strongly recommended (but optional) for other focusable images, including Top Shelf images. It is possible to embed layered images in the app or obtain them from a content server at runtime, using the `.lcr` format generated from LSR or Photoshop files via the `layerutil` command line tool.
- visionOS: people can view images across a much wider range of sizes than on any other platform, and the system dynamically scales the image resolution to the current size; app icons are composed of two to three layers that move at subtly different rates when coming into focus. Covers spatial photos (stereo photos with spatial metadata, captured on iPhone 15 Pro or later, Apple Vision Pro or a compatible camera) and spatial scenes (3D image generated from a 2D image, with a parallax effect responsive to head movement).
- watchOS: covers self-scaling PDFs and the recommendation to avoid transparency for file size, with exceptions for template images.

**Links to other articles:** Apple Design Resources; App icons (for the visionOS icon Layer design); Color management.

<!-- visual:images -->
### What the illustrations show
Basis: 1 illustration sheet (hig-img_images) and 4 video sheets (hig-vid_images__012, frames q001 to q037) viewed, all opened and with checked codes.
- The opening illustration places the image glyph, with a rounded frame, circle and mountain silhouette, in a rounded-corner rectangle in a yellow gradient, with the glyph in a darker, semitransparent yellow. On top come construction guides: horizontal, vertical and diagonal X dotted lines, plus a grid of concentric circles aligned to the glyph (img 0630).
- The scale factor is shown with the same shape, a black circle, drawn over visible square pixel grids of increasing size: 10 by 10 cells, then about 20 by 20, then about 30 by 30. In the smallest, the edge is jagged and uses intermediate gray pixels to smooth it; in the largest, the pixels are almost imperceptible. The shape does not change, only the pixel count per side (img 0631, 0632, 0633).
- The tvOS app icon video separates layers by speed of movement: the rounded red card and the white ring stay practically fixed, while the red panda face, in the foreground, moves from the left to almost the center and then to the right, repeating this triad throughout the entire sample (video, sheet 0001, q001 to q009; sheets 0002 to 0004, up to q037).
- The background does not stay completely still: a light diagonal glow appears in the upper left corner of the card in the frames where the face is almost centered and disappears at the extreme positions, when the light goes flat (video, sheet 0001, q002 and q005).
- The intensity of this glow changes from one cycle to the next, with the same amplitude as the face's displacement: in q012 it becomes stronger and wider, covering almost a quarter of the card, in q027 it appears wider and lighter than in the neighboring central frames, and in q014 and q017 it is more subtle (video, sheets 0002 and 0003).
- There is a sign of scaling along with the translation: in q036 the card appears narrower on the sides, as if the composition were zooming in, with the face almost centered, and in q037 it returns to a width close to that of the previous frames (video, sheet 0004, q035 to q037).

Recorded divergences: the official video description only says that the icon moves to show the parallax; the frames add the cyclical lateral movement and the variation in background glow, which the description does not mention. No frame shows the icon still or a different final state, and the 37-frame sample seems to cover only one continuous repetition of the same cycle, with no distinct start or end.
<!-- /visual:images -->

## Immersive experiences (slug: immersive-experiences)

**What it governs:** the design of immersive experiences in visionOS: immersion styles (mixed, progressive, full), transitions between them, use of passthrough, display of virtual hands and creation of custom environments.

**Why:** in visionOS, apps can run in the Shared Space (together with other experiences, like on the Mac) or in a Full Space (alone, hiding other experiences). The central reasoning is the person's comfort and control: not every task benefits from immersion, and even when it does, people often want to remain anchored to their physical surroundings and keep the ability to use other apps and system features at the same time.

**Do and avoid:**
- Offer multiple ways to use the app, including support for the accessibility features that people use to customize the interaction.
- Prefer launching the app in the Shared Space or using the `mixed` immersion style, giving people more control to choose when to increase immersion.
- Reserve immersion for significant moments and content; not every task needs to be fully immersive.
- Help people engage with key moments using cues such as dimming, tinting, motion and scale, starting with subtle cues and reinforcing them only when there is good reason.
- Prefer subtle tint colors for passthrough (available starting with visionOS 2), avoiding bright or dramatic tones that distract and reduce the sense of immersion.
- Be careful with visual comfort: prefer positioning 3D content within people's field of view, and display movement in comfortable ways while the app runs in a Full Space.
- Choose an immersion style that supports the movements people might make during use; avoid the `progressive` or `full` styles, or fall back to `mixed`, if people might need to move beyond the 1.5 meter limit.
- Avoid encouraging movement during a progressive or fully immersive experience; design ways to interact with the content without moving (e.g.: bringing a virtual object close to the person instead of waiting for them to approach it).
- If using the `mixed` style, avoid obscuring the passthrough too much.
- Adopt ARKit if you want to combine custom content with the person's surroundings; request permission when you need sensitive data such as hand position.
- Design smooth and predictable transitions when changing immersion level, avoiding sudden, disorienting transitions.
- Let people choose when to enter or exit a more immersive experience, providing a clear entry/exit action; avoid requiring system controls to reduce immersion.
- Indicate the purpose of an exit control (whether it returns to a less immersive context or ends the experience entirely).
- When displaying virtual hands, prefer that they match familiar characteristics (the person's hand positions and gestures); use caution with virtual hands larger than the person's real hands, since they can obstruct vision and look disproportionate; if there is an interruption in the hand tracking data, fade out the virtual hands and reveal the person's real hands, without leaving them frozen.
- When creating a custom environment, minimize distracting content, help distinguish interactive objects (by proximity), keep animation subtle, create an expansive environment (avoiding a sense of claustrophobia), use Spatial Audio to create atmosphere while avoiding excessive repetition, avoid using an isolated flat 360 degree image (prefer object meshes with lighting and shaders), help people feel anchored by providing a ground plane (ground plane mesh), and minimize asset redundancy.

**Exact specifications:**
- The system defines a limit (boundary) that extends about 1.5 meters from the person's initial head position in the `progressive` and `full` styles. When the head approaches this limit, the experience begins to fade and the passthrough increases; once the limit is crossed, the immersive visuals are replaced in space by the app icon.
- Default immersion range in the `progressive` style: from 120 to 360 degrees (it is possible to define a custom range).
- The `full` style displays a custom 360 degree environment that completely replaces the passthrough.

**Platform differences:** this article is specific to visionOS; the text explicitly states that it is not supported on iOS, iPadOS, macOS, tvOS or watchOS.

**Links to other articles:** Spatial layout, Motion, Accessibility, Privacy.

<!-- visual:immersive-experiences -->
### What the illustrations show
Basis: 2 illustration sheets (hig-img_immersive-experiences) and 3 video sheets (hig-vid_immersive-experiences__013, frames q001 to q020) viewed, all opened and with checked codes.
- The opening illustration uses an abstract concave shape, similar to a horizontal hourglass with straight sides and top and bottom edges curved inward, in darker semitransparent yellow over a rounded-corner rectangle in a yellow gradient, with a straight X grid and a grid of concentric circles on top. The shape recalls the frame of a headset, but it is not a literal drawing of the device (img 0638).
- The passthrough fade is shown with the same living room and the same large panel of frosted, blurred glass in the center, with no legible content. In the first version, the surroundings are sharp and with normal light; in the second, it becomes visibly darker, with deeper shadows, while the panel keeps roughly the same brightness, which increases the difference in tone between window and surroundings (img 0639, 0640).
- In the mixed style, app objects enter the real space and coexist with the room's furniture: a folding director's chair, a tripod with an old film camera and a wooden desk of a different design from the rest. In the background, a staircase and a glazed door appear that were not in the two previous images (img 0641).
- In the progressive style, the same foreground objects and the panel stay the same, but the surroundings change: narrower walls, a staircase on the left, darker and more yellowish overall light, a more angular stool and chair on the right, mixing real-looking elements with a dark, uniform setting (img 0642).
- In the full style, the foreground stays the same and the surroundings turn into an enclosed gallery with terracotta walls, with colorful framed abstract paintings on both sides, with no trace of the room left (img 0643).
- The series isolates a single variable: the frosted glass panel stays in the same position and proportion in all the captures (img 0639 to 0643), and the app objects stay fixed from img 0641 to 0643, so that only how much of the real environment is replaced changes.
- The video opens with an outdoor landscape (lake, ochre rocks, trees, hill, blue sky) and a smaller rectangular cutout, slightly rotated, in the upper left corner, with another scene of water and vegetation. The framing opens up with each frame, the strip of ochre rocks gains area and more trees enter from the right, while the cutout stays in practically the same place and size. In this section there is no border, text or control (video, sheet 0001, q001 to q009).
- In q010, a small translucent gray circular control appears, with a mountain icon, to the right of the cutout, and it stays practically in the same place from then on while the background changes behind it (video, sheet 0002, q010 to q018; sheet 0003, q019 and q020).
- The environment swap is a gradual blend, not a cut: starting at q015, an interior scene with a wooden shelf and an articulated lamp enters from the right in transparency over the landscape, grows frame by frame and pushes the exterior to the left, with a diagonal transition line clearly visible in q016, q017 and q018 (video, sheet 0002, q014 to q018).
- In the end, the interior room (gray sofa, dark blue cushion, plant, shelf, coffee table, rug, picture on the wall) takes up almost the entire frame, leaving only a fraction of the landscape and the original cutout in the upper left corner; the circular control now appears over the light-colored wall. Between q019 and q020, almost nothing changes (video, sheet 0003, q019 and q020).

Recorded divergences: the official description of the video mentions an adjustment via the Digital Crown that reveals more of the physical environment, but the frames show no hand and no Digital Crown, only the result of the transition. Inference, not recorded in the notes as a divergence: the notes treat the outside landscape as passthrough and the inside room as a customized environment, a reading opposite to the official description, which speaks of revealing more of the physical environment.
<!-- /visual:immersive-experiences -->

## Inclusion (slug: inclusion)

**What it governs:** the principles of inclusive design: welcoming language, gender identity, representation of people and environments, how to avoid stereotypes, accessibility and language/localization considerations.

**Why:** inclusive apps and games put people first, prioritizing respectful communication and presenting content and functionality in ways everyone can access and understand. Apple's reasoning is that a "non-offensive" app is not necessarily an inclusive app; the focus should be on creating a welcoming experience for everyone, which requires empathy to understand how people with different perspectives might respond to the content and experiences created. Inclusive design is described as an iterative process that requires time and a willingness to examine one's own assumptions.

**Do and avoid:**
- Consider the tone of the copy from different perspectives; be clear, direct and respectful.
- Pay attention to how you refer to people: it generally works well to use "you" and "your"; referring indirectly to "the user" or "the player" can make the experience feel distant; reserve "we" and "our" to represent the software or the company.
- Avoid technical or specialized terms without defining them.
- Replace colloquial expressions with plain language, since colloquial expressions tend to be culture-specific and hard to translate, and some have exclusionary origins (the text cites "peanut gallery" and "grandfathered in" as examples of phrases with oppressive origins).
- Consider carefully before including humor, which is highly subjective and hard to translate across cultures.
- Present a clear, direct interface, and build ways to learn how to use the app, such as an onboarding flow.
- Avoid unnecessary references to specific genders; prefer gender-neutral language (the text gives an example of rewriting a sentence to remove unnecessary gendered pronouns).
- Avoid referencing a specific gender in an avatar, emoji, glyph or game character; prefer giving people tools to customize these items as they wish.
- If you need to depict a generic person, use a non-gendered human image; SF Symbols offers many non-gendered glyphs.
- If you need gender information (for health or legal reasons), consider inclusive options such as non-binary, self-identification and "prefer not to say", and consider allowing people to specify the pronouns they use.
- When depicting people, show a variety of human characteristics and activities; avoid stereotypical representations (e.g., showing only male doctors or female nurses).
- Review the environments and objects shown; prefer showing places, homes, activities and items that are familiar and recognizable to most people.
- Be aware of unconscious biases and generalizations that can influence design decisions; avoid basing decisions on stereotypical definitions (the text gives the example of a family access management app that assumes a stereotypical definition of family).
- Avoid security questions based on experiences specific to a culture or ability (the text gives examples of problematic questions and more universal alternatives).
- Support Apple's accessibility features (VoiceOver, Display Accommodations, closed captions, Switch Control, Speak Screen); avoid assuming that a disability would prevent someone from wanting to enjoy the experience.
- Recognize that every disability is a spectrum, and that everyone can experience disabilities, including temporary and situational ones.
- Avoid images and language that exclude people with disabilities; use people-first language when writing about people with disabilities, and find out how the person or community self-identifies.
- Prioritize simplicity and perceptibility.
- Prepare the software to handle languages and regions other than your own (internationalization) before providing translated text and resources for specific locales; using SF Symbols can help simplify localization, including language-specific glyphs and glyphs for left-to-right and right-to-left contexts.
- Be mindful of how you use color when localizing, since colors have strongly culture-specific meanings (the text cites white associated with death or mourning in some places, and with purity or peace in others).

**Exact specifications:** the text brings no numbers, measurements or specific values on this page; it is an entirely qualitative page of principles and guidelines.

**Platform differences:** the text explicitly states that there are no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

**Links to other articles:** Writing inclusively, Accessibility, Localization, Right to left.

<!-- visual:inclusion -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_inclusion), opened and with codes checked; the page has no video.
- The opening illustration sketches two generic human figures side by side, each with a circular head and a half-ellipse body, inside a rounded-corner rectangle tinted yellow. Above them there is a dotted grid of horizontal and vertical lines and a large circle that frames both heads, marking the geometric alignment of the figures in the frame (img 0667).
- The person-in-circle symbol is a solid black silhouette of a head and shoulders inside a circle that is only outlined, with no trace indicating gender (img 0668).
- The group symbol shows three identical, filled silhouettes of head and shoulders, side by side with slight lateral overlap, all the same apparent size and on the same plane (img 0669).
- The waving figure symbol is a solid black full-body silhouette, standing, with one arm raised well above the head, with no outline or gender detail (img 0670).
- In the three symbols in the gender identity section, the neutrality comes from the absence of face, hair and clothing in a solid black silhouette, not from a different abstract symbol (img 0668, 0669, 0670).

Recorded divergences: the official caption of img 0669 describes depth, with the figure on the left in the foreground and the other two in the background, but the image shows all three at the same apparent size and with no visible difference in plane or opacity, only slight horizontal overlap.
<!-- /visual:inclusion -->

## Layout (slug: layout)

**What it governs:** the principles of visual hierarchy, adaptability to different screen sizes and multitasking configurations, size classes, layout guides and safe areas, and grid and margin specifications by platform.

**Why:** layout provides the structure for people to understand content from the moment they open the app. Familiar relationships between controls and content allow immediate use and discovery, and make the design feel "at home" on each platform. People expect the experience to stay familiar when they rotate the device, resize a window, add another display or switch devices.

**Do and avoid:**
- Order content by relative importance; since people tend to read from top to bottom and from the leading edge to the trailing edge, place the most important items near the top and the leading edge of the window or display. For right-to-left languages, prefer standard system components that adapt automatically.
- Align elements to make scan reading easier, and use indentation to convey hierarchy; aligned items are perceived as related, and indented items are perceived as subordinate.
- Group related items using negative space, container shapes or separator lines.
- Use progressive disclosure to make layouts cleaner and easier to interact with: disclosure triangles, menus, nested views, or scrollable sections.
- Differentiate controls from content: take advantage of Liquid Glass material on platforms that support it to give controls a distinct appearance; use a scroll edge effect to visually elevate controls above content, instead of applying a solid or semi-opaque background color under them. For full-screen background content, extend it under sidebars, toolbars and tab bars.
- If scaling a background image to the edge of the window covers components such as sidebars or inspectors, use a background extension effect to mirror and blur the image under the adjacent components.
- Design a layout that adapts elegantly and consistently; respect safe areas, margins and guides defined by the system, and specify layout modifiers to adjust the positioning of views.
- Even if the app is locked to one orientation (e.g., a landscape-only game), make sure the interface resizes well across different devices and window sizes.
- Prepare for text size changes (Dynamic Type), adjusting the layout to accommodate text at larger sizes (e.g., horizontally adjacent views may need to stack vertically; table rows may need to grow in height).
- Preview the app on multiple devices, size classes, localizations and text sizes; test the largest and smallest layouts first.
- When necessary, scale background art in response to display changes, without altering the art's proportion (avoiding cropping, letterbox or pillarbox).
- Determine layout based on size classes, not on device type or orientation, since size classes describe the actual space available.
- Consider every possible combination of size classes.
- Keep functionality the same as size classes change (you can change the amount of functionality visible on screen, but not the functionality itself); consider taking advantage of larger spaces to switch from tab bars to sidebars or to expose functionality that would otherwise sit in an overflow menu.
- Keep the layout recognizable and familiar to the platform even when resizing, since the device idiom stays the same even when size classes change.

**Exact specifications:**

tvOS, safe area: inset the main content 60 points from the top and bottom of the screen, and 80 points from the sides.

tvOS, focus grids (unfocused content width, horizontal spacing, minimum vertical spacing):
| Grid | Unfocused content width | Horizontal spacing | Minimum vertical spacing |
|---|---|---|---|
| Two columns | 860 pt | 40 pt | 100 pt |
| Three columns | 560 pt | 40 pt | 100 pt |
| Four columns | 410 pt | 40 pt | 100 pt |
| Five columns | 320 pt | 40 pt | 100 pt |
| Six columns | 260 pt | 40 pt | 100 pt |
| Seven columns | 217 pt | 40 pt | 100 pt |
| Eight columns | 184 pt | 40 pt | 100 pt |
| Nine columns | 160 pt | 40 pt | 100 pt |

visionOS: minimum space around controls so that their centers are at least 60 points apart from each other.

watchOS: at most three buttons with glyphs, or two buttons with text, side by side on one line.

**Platform differences:** the text states that there are no additional considerations for iOS or iPadOS beyond what has already been covered.
- macOS: avoid placing controls or critical information at the bottom of the window (people often move windows so that the bottom edge ends up below the screen); avoid displaying content behind the camera housing at the top edge of the window.
- tvOS: safe area and grid requirements detailed above; include adequate padding between focusable elements, since an element grows in size when it enters focus; keep spacing consistent so the content looks like a grid; make partially hidden content symmetric (same width on each side of the screen).
- visionOS: layout inside a window, a bounded 3D volume or an immersive space; support resizing by default, keeping the content horizontally centered at very large sizes; it is possible to set a minimum and maximum size for windows, volumes and ornaments, but not as a way to prevent resizing; use 3D content sparingly inside windows, reserving it for meaningful moments; show supplemental content in an adjacent window, not in an ornament.
- watchOS: at most two or three controls side by side; support auto-rotation in views that people might want to show to others (for example, a QR code).

**Links to other articles:** Right to left, Spatial layout, Layout and organization.

<!-- visual:layout -->
### What the illustrations show
Basis: 5 of 5 illustration sheets viewed (img 0680 to 0696, all in light version), codes checked; the page has no video.
- The section opener draws the position of an element inside the window as a smaller solid rectangle fitted into the upper left quadrant of a larger rectangle, with a grid of rectangular guides and a central alignment circle overlaid, the same construction scheme as the other HIG openers (img 0680).
- The visual hierarchy appears in a real iPad app composition: a sidebar on the left with items and icons, a photo of Mount Fuji occupying the upper half of the content area and three paragraphs of text below it; it is the only complete app example on the page, the rest are abstract diagrams (img 0681).
- The background extension effect is visible in the same screenshot: where the photo meets the sidebar, the image continues underneath it mirrored and blurred, and near the top the photo gets a slight blur under the toolbar items grouped on the right (img 0681).
- The size classes are drawn as an empty light blue window over the same abstract beige and gold background, varying only the proportion: narrow and short in compact width and compact height (img 0682), taller in compact width and regular height (img 0683), wide and low in regular width and compact height (img 0684) and large in both dimensions in regular width and regular height (img 0685). Width and height grow independently.
- The tvOS safe area is annotated as a pink band between the TV frame and the content area, with the measurements in red: 60 at the top and bottom, 80 on the sides (img 0686).
- The spacing between tvOS focusable items shows three cards side by side in which the center one appears larger and with a shadow, indicating focus, and vertical pink bands fill the padding between it and its neighbors (img 0687).
- The tvOS grids are a sequence of screens with the same frame: from two to eight full columns, each row ends with an extra column cut off at the right edge, and the first grid also cuts off a row at the bottom, suggesting content beyond the visible area (img 0688 to 0694).
- In each grid a single item appears highlighted, white and with "Title" below it; in the two-column grid it sits in the first row, next to a light gray item, and in the following ones it sits in the second row, in the middle column of the three-column grid, the second of the four-column one, the third of the five-column one, the fourth of the six and seven-column ones, and the fifth of the eight and nine-column ones, which in the nine-column grid is the center position (img 0688 to 0695).
- The nine-column grid is the only one with no column cut off: the nine columns fit entirely within the frame, in three complete rows (img 0695).
- In the tvOS diagrams red functions as the annotation color for measurements and pink marks the margin and padding zones (img 0686, img 0687).
- On watchOS the illustration shows a single pill-shaped text button at the bottom of the screen, with a semitransparent background and white text, over a gradient from navy blue to magenta, with the time in the upper right corner (img 0696).
Recorded divergences: the four size class images do not draw an iPad frame, even though the official description mentions an iPad in landscape (img 0682 to 0685); starting from the "Two-column grid" section, each image shows the column count that follows the one in the heading under which it appears, matching the image's own caption and not the section title (img 0689 to 0695); the watchOS image shows only one button and no line of text, while the official description mentions two buttons side by side under three lines of text (img 0696).
<!-- /visual:layout -->

## What this group reveals about the Apple way

1. The system, not the developer, owns the final visual effects. In app-icons, icons and color, the recurring guidance is "let the system apply it" (masking, specular highlights, shadows, Liquid Glass effects) instead of embedding these effects manually; this appears in almost identical form in app-icons (Visual effects section) and icons (SF Symbols, icons with no pre-applied mask).

2. Simplicity is not aesthetic, it is function. accessibility, app-icons, icons and branding converge on the same argument: less detail is more recognizable and more robust across varied contexts (small sizes, different appearances, cultural translation), not just "prettier".

3. Color has a semantic function before a decorative one. color, dark-mode, accessibility and branding share the rule of not using color alone to communicate information, and of reserving accent color for a few high-importance elements (primary actions, status), never applied broadly.

4. Every visual choice needs to survive alternative system states, not just the default state. accessibility, color and dark-mode require testing contrast under Increase Contrast, Reduce Transparency, Reduce Motion and Dark Mode simultaneously, treating these settings as part of the design, not as an exception.

5. The brand must defer to the platform and to the content, never compete with them. branding is explicit ("ensure branding always defers to content"), and the same principle reappears in layout (differentiate controls from content, not decorate) and in color (apply accent color sparingly).

6. Consistency across variants is treated as a recognition requirement, not a matter of taste. app-icons requires that the icon's core characteristics stay the same across appearances (default, dark, tinted); icons requires consistency of weight, size and perspective across all of an app's interface icons.

7. There is a declared hierarchy of sources of truth about "how much space do I have": layout explicitly instructs using size classes, not device type or orientation, as the basis for layout decisions, because size classes describe the actual available space.

8. Text embedded in graphic elements is treated as a problem, not a feature, consistently across app-icons, icons and inclusion: text does not localize well, does not provide accessibility and tends to become illegible at small sizes.

9. The safety default in immersive or multi-screen environments always favors giving the person explicit control over transitions, instead of automatic or abrupt decisions: immersive-experiences (entering/exiting immersion through an explicit action) and layout (free resizing, not blocked via min/max size) repeat this pattern.

10. Localization and inclusion are treated as part of the core design, not as a layer added afterward: inclusion, color (cultural connotations of color), icons (character localization and text direction) and layout (right-to-left languages) show the same concern applied across different articles.

11. Apple explicitly distinguishes two types of icon with different rules: app icons (an app's icon, rich in layers and effects, representing personality) versus interface icons (glyphs, simple and functional); treating one by the other's rules is flagged as a mistake (for example, not replicating the app icon as an interface icon).

12. The person's physical and psychological comfort is elevated to a formal design criterion, not just a usability one: immersive-experiences dedicates an entire section to "Promoting comfort" with measurable distance limits (1.5 meters), and accessibility treats Reduce Motion with a concrete list of animation techniques to avoid.

## Reading evidence

| File | Lines read | Read to the end |
|---|---|---|
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/accessibility.md | 147 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/app-icons.md | 107 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/branding.md | 39 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/color.md | 184 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/dark-mode.md | 68 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/icons.md | 170 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/images.md | 103 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/immersive-experiences.md | 89 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/inclusion.md | 99 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/layout.md | 170 | yes |

All 10 files in the group were read in full in a single Read call each, with no need for offset/limit (no file exceeded the default read limit), and each read ended at the last visible line (the "Change log" or "Resources" section, depending on the article).
