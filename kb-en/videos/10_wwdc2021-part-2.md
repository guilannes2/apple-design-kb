# wwdc2021 (part 2)

## Explore the SF Symbols 3 app (id: wwdc2021_10288, 12.8 min)

- Basis: transcript and 11 of 11 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2021/10288/.
- Central thesis: the SF Symbols app follows the entire design and development cycle, from finding and organizing symbols to customizing and exporting them for comps and code, covering platform compatibility, localization and the new rendering modes.

- The design process Apple describes: in the talk, the presenter builds, live, a fictional card game app to illustrate the complete flow.
  - Creates a collection ("+" button) to gather the project's symbols and find them later.
  - Searches for symbols by category in the sidebar (e.g.: "Human" category for an "add player" symbol) and by keyword in the toolbar (searches cited: "suit", "stack", "book").
  - Drags and drops the symbols found into the collection.
  - Before using a symbol, checks platform compatibility in the information inspector: the symbol's name, the SF Symbols version it appeared in, the corresponding iOS, and whether an old (deprecated) name exists to support older OS versions.
  - Checks localization in the same inspector: how the symbol changes by language (character in the user's native script) and by reading direction (the book opens from one side or the other depending on LTR or RTL). Recommends not hardcoding a localization suffix (such as .ar or .zh) in Xcode and letting the system choose the right representation.
  - Uses the rendering inspector to compare the rendering modes before deciding which one to use.
  - To create a custom symbol, duplicates an existing symbol as a starting point (File > Duplicate as Custom Symbol), renames it, exports a template SVG, edits that SVG in a vector editor and drags the edited file back to update the symbol in the app.
  - To annotate the custom symbol for the new rendering modes, selects parts of the drawing and drags each part to a layer (Multicolor: sets the color of each layer; Hierarchical: sets layers as Primary and Secondary).
  - At the end, decides how to export the symbol depending on the destination: design comp (SF fonts, pasting as text) or custom drawing with advanced rendering (Copy Image).

- Principles stated and why:
  - Letting the system choose the right localization and compatibility, instead of hardcoding it manually, because this removes repeated work from the developer for every new supported language or OS.
  - Using SF fonts (copy as text) whenever the symbol is a system one and monochrome, because this way it stays automatically aligned and with the same weight as the text next to it, with no manual adjustment.
  - Reserving the Copy Image feature for design comps, and using the symbol's name (not the image) when working in code, to keep each tool in its proper role within the design-to-development flow.
  - To place a custom symbol in an Xcode asset catalog, using Export Symbol instead of Copy Image, so as not to lose resources that only the complete custom symbol carries.

- Concrete interface-building techniques:
  - System catalog: more than 3000 SF Symbols available across Apple platforms.
  - Versioning example cited: the name person.fill.badge.plus has been available in monochrome since SF Symbols version 2.0, corresponding to iOS 14; the equivalent deprecated name, person.badge.plus.fill, has been available since version 1.0, corresponding to iOS 13.
  - Rendering modes available in the rendering inspector: Monochrome (one color, system or custom), Multicolor (colors intrinsic to the symbol's meaning; in the example, heart and diamond turn red, spade and club turn black, with automatic adjustment for Dark Mode testable via the Background picker), Hierarchical (new this year: one color with opacity variations to give depth) and Palette (new this year: two or three colors specifiable by the user).
  - Copying for design: Edit > Copy Symbol (Command-C shortcut) pastes the symbol as text using the SF fonts. Edit > Copy Image (Option-Command-C shortcut) or Copy Image As... copies an image in PNG or SVG, with configurable point size and pixel scale; these settings remain until changed again. Copied images can gain extra vertical padding so that the vertical center of several symbols aligns on a horizontal line.
  - For code: copy the symbol's name (not the image); for asset catalog, use Export Symbol.

- Examples cited (apps, screens, components) and what each one teaches:
  - Fictional card game app: teaches the end-to-end flow, from searching for symbols to exporting them for comp and code.
  - "Add player" symbol (person.fill.badge.plus / person.badge.plus.fill): teaches how to check OS version compatibility and use deprecated names when necessary.
  - Book symbol for "game rules": teaches automatic symbol localization (native script and reading direction) with no extra effort from the developer.
  - Custom "queen of hearts" symbol (created from crown.fill, renamed to queen.heart.fill): teaches the flow of duplicating, editing in vector, reimporting and annotating a custom symbol for the new rendering modes.
  - Button with book symbol + the word "Rules": teaches the use of Copy Symbol/paste as text to keep symbol and text aligned and with equal weight, using the SF fonts.

- Quotes:
  - "There are now over 3000 SF Symbols built into Apple platforms."
  - "Remember that Copy Image is intended to be used when you're making design comps."

<!-- visual:wwdc2021_10288 -->
### What the images show
Basis: 11 of 11 frame sheets viewed, all codes checked.

- The SF Symbols app always appears in the same three-column layout: sidebar with fixed categories and, below a dividing line, the "Library" section with the user's collections; central grid of symbols with a caption under each icon and an "N Symbols" counter in the header; inspector on the right that switches between "No Selection" in centered gray and the detail of the selected item (sheet 0001, q0009; sheet 0002). The spatial division is not narrated in the talk, it only appears on screen.
- The availability inspector shows two stacked entries for the same design: the current name with one line per rendering mode and the version number aligned to the right, and below it the obsolete name marked with a small warning triangle (sheet 0003, q0019). The visual structure of two entries with a warning icon is an addition by the image over what the talk explains.
- The "Rendering" panel changes content according to the mode: in Monochrome there is a color picker with a square swatch and a percentage value next to it, in Hierarchical a single color picker, and in Palette the "Colors" list appears with named rows and their own percentages (100, 40, 100); all of them have a "Background" section at the end, and the dropdown menu lists the four options stacked with a selection mark on the active one (sheet 0004, q0035 and q0036; sheet 0005, q0038 to q0040).
- The switch from Monochrome to Multicolor is visible frame by frame: the suits take on their own color, heart and diamond in red, club and spade in black, while the other symbols in the same collection remain monochrome (sheet 0004, q0035 to q0036).
- The layer annotation of a custom symbol appears as a vertical "Layers" list, one row per layer with a thumbnail and color name (sheet 0006, q0054). When splitting the drawing in Hierarchical, the list goes from a single "Primary" row to two rows, "Primary" and "Secondary", with the active row in a blue outline (sheet 0007, q0059 to q0060).
- Active selection is always a square blue outline around the icon, and multiple selection switches the inspector to the "Multiple Selected" label (sheet 0002, q0015).
- The external editing flow is shown as an alternation between two environments: a vector editor with rulers, blue and red guides crossing the icon and a panel for position, size, opacity and shadow; a Finder window with two SVG files; and a modal template replacement dialog with an icon at the top, bold text, an explanation in gray and the "Cancel" and "Replace" buttons, the latter blue as the default action (sheet 0006, q0047 to q0051).
- The difference between pasting as text and pasting as an image is recorded in two distinct frames: the book symbol and the word "Rules" on the same baseline, the same blue color and similar weight, as if they were characters (sheet 0008, q0066); and the custom crown inside a selection box with handles in a design app, with numeric fields for position, size and opacity (sheet 0009, q0080).
- The highlight cards follow a fixed pattern: black background, short white title aligned to the left and up to two supporting sentences in smaller body text, with no bullets (sheet 0003, q0025; sheet 0008, q0072). One card breaks this pattern, with a green circular badge reading "NEW" next to the title and two items marked with a dot (sheet 0010, q0082). At the end of thematic blocks a credit footer appears with the name of another session on the left and the event year on the right, in the last case separated by a thin line (sheet 0008, q0072; sheet 0010, q0089).
- The transition from the demo to the concept is made by a dissolve, not a hard cut: the app capture darkens in steps, the card title appears overlaid and semitransparent over the still-visible screen, reaches full black with the complete text and then the app screen reappears behind the text (sheet 0003, q0019 to q0027).
- The "When to use Copy Image" card arranges four colored icons in a horizontal row with equal spacing, with short captions centered below, with the last two icons sharing a single caption (sheet 0010, q0086). In the previous frame the same card existed with only the title, without the icons.
- The presentation overlays topic text onto the presenter's video: at the start there are two white lines aligned to the left, with no box or solid background (sheet 0001, q0006); further along there are three lines stacked to the right of the face, the ones already covered in light gray and the current one in white and bold (sheet 0005, q0041 and q0042).
- A symbol's localization is exposed in the inspector as a list of writing systems, with one line per item (Latin, Arabic, Hebrew, Hindi, Japanese, Korean, Thai, Chinese), a structure the talk does not describe item by item (sheet 0002, q0018).
- The close is a purely iconic summary: a row of isolated icons on a black background, grouped by theme and with no caption, changing group between frames, until the final screen with the apple and "WWDC21" centered (sheet 0011, q0091 to q0095).

Visual proportion: based on the notes, most of the frames are captures of the SF Symbols app, black text card or external editor, with the presenter entering in short cuts between blocks, plus context shots of the physical laptop on the desk (sheet 0001, q0008; sheet 0006, q0053; sheet 0009, q0077).

Recorded divergences or limits: the notes record that, on sheet 0009, the icons on a black background appear without caption text in that segment (q0074 and q0075), and that the shot of the laptop seen from behind has no legible detail on the screen (sheet 0006, q0053).
<!-- /visual:wwdc2021_10288 -->

## The process of inclusive design (id: wwdc2021_10304, 36.6 min)

- Basis: transcript and 26 of 26 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2021/10304/.
- Central thesis: inclusion needs to be considered from the start and throughout the entire design and development process, guided by axes of diversity and by actively listening to perspectives different from the team's own, and not treated as a last-minute addition.

- The design process Apple describes, phase by phase:
  - Ideation: each person on the team should be able to answer why they are making that app or game, what human good it serves, and how people will be better off. Ask who the product is made for, thinking through the axes of diversity and not only current users. Challenge your own assumptions and actively listen to experiences different from the team's.
  - Design: think about the extremes of use, not just the average person. Consider the emotional, social and physical impact on whoever uses the app, asking whether some group tends to have more negative experiences and whether that group is already vulnerable or disadvantaged. Consider the impact of context and location (culture, type of housing, noisy or quiet environment, connectivity).
  - Development: ensure inclusive representation and expertise throughout development, explicitly including a diverse group in discussions about prototypes and decisions. Plan accessibility and internationalization from the start, understanding the accessibility and localization APIs in advance. Standard UIKit, AppKit or SwiftUI controls already implement the UIAccessibility methods and are accessible by default; custom controls or views require extra planning time to become accessible.
  - Test: seek out a diverse group of people to give real usage feedback. Test with assistive technologies and accommodations (VoiceOver, text size at maximum, keyboard navigation) to identify problems before they affect customers. Listen to, review and prioritize the feedback received, including advocating for inclusive testing goals as KPIs (key performance indicators) within the company.
  - Launch: when there is a fixed deadline, hard choices need to be made, cutting the launch of a feature in order to do fewer things well for everyone. When it is not possible to deliver the best experience for an axis or intersection of diversity, it is necessary to understand why, how and when this will be resolved, with a plan and a target date. Launch is not an end point: continually reassess and evolve based on real feedback after launch.

- Principles stated and the why of each:
  - Axes of diversity as a reference for thinking beyond one's own experience: class, culture, ethnicity, language, education, political, philosophical and religious beliefs, race, gender, sexual orientation, age, abilities, disabilities, being left handed or right handed, body measurements such as height, and environmental conditions such as location, internet connectivity and access to devices.
  - "Inclusion is a journey", not a single obstacle: change is an iterative process that requires planning, persistence and patience, because the benefit (improving people's quality of life) outweighs the effort.
  - Inclusive design stimulates creativity instead of limiting it: constraints help focus energy on the first decisions within a narrower problem space, instead of forcing everyone to accept the "common denominator" experience.
  - A diverse team is not the same as an empowered team: having a diverse team does not guarantee an inclusive product; what guarantees it is a diverse team whose perspectives actually enter into decisions. Hence the recommendation to hire thinking in terms of "culture add" (what is missing) instead of "culture fit" (what already exists).
  - Inclusion cannot be treated at the end of the process, the same way as security or privacy: leaving it for the end is reactive and usually there is no time left to fix it.
  - Intersectionality (a concept attributed to legal scholar Kimberlé Crenshaw): recognizes that people with multiple systemically disadvantaged identities have unique needs and experiences, which only appear when looking at the intersection of the axes, not at each axis in isolation.

- Concrete interface, writing and process building techniques (with exact numbers when stated):
  - Cited data point: people with disabilities are 15% of the world's population, a number that grows with population aging and chronic health conditions.
  - Example of accessibility through recognition: an Apple feature for recognizing physical objects and text (signage, business cards, envelopes) emerged with the team restricting the scope to a few objects and text, then expanding to action buttons (call, send message, add to contacts, copy recognized number).
  - People Detection in the Magnifier app: uses LiDAR technology (pulsed laser that generates a 3D model of the surrounding environment) to report the distance between the person and other nearby people; it began as a convenience prototype and became a practical necessity during the COVID-19 pandemic to support social distancing for people who are blind or have low vision.
  - In iOS 15, the Description feature in Markup lets you write image descriptions manually, which are sent along when the photo is shared.
  - VoiceOver Recognition image descriptions: a machine learning model trained to generate image descriptions automatically at scale. The team found that ML models tend to represent only two genders (female and male) and decided to make these automatic descriptions gender neutral (example of a generated description: person with curly black hair, red and white striped shirt, in front of a building), reserving the mention of gender for descriptions written manually by someone who knows the person in the photo.
  - Memories (Photos, iOS 15): the team analyzed new memory themes along the axes of rural versus urban life, teenagers versus grandparents, regional versus global, answering for each theme who is being included, who is being excluded and how people will feel. They began representing more hobbies (martial arts, skateboarding, soccer) and expanded the international catalog of holidays (Christmas, Diwali, Lunar New Year, Eid al-Fitr, Hanukkah, among others).
  - Still in Memories, based on feedback about running into photos of an ex partner, the team created the "Feature Less" action (feature this person less), available from a featured photo, from the People albums, and from an individual photo; in a second iteration, it let the person choose between "feature less" or "never feature again". They also swapped the "thumbs down" icon for a more neutral glyph, since it could read as "not liking the person" in situations such as grief.

- Examples cited (apps, screens, components) and what each example teaches:
  - Object and text recognition for people who are blind or have low vision: teaches how an initial scope restriction can open the way to a high-impact solution.
  - People Detection (Magnifier, LiDAR): teaches collaboration between accessibility and engineering teams, and how a real context (pandemic) turned a convenience feature into a necessity.
  - VoiceOver Recognition image descriptions: teaches how to investigate machine learning representation by axis of diversity and how partnerships with external organizations (blind/low vision and LGBTQ+) helped decide on gender neutral descriptions.
  - Memories (photos and videos): teaches concrete inclusive research techniques (multicultural brainstorming in small groups and across different time zones, analysis by axes of diversity, individual interviews for sensitive topics) and design iteration based on real user feedback.

- Quotes:
  - "Inclusive design and development stimulates new creative solutions."
  - "Diverse representation does not guarantee inclusivity will come naturally."

<!-- visual:wwdc2021_10304 -->
### What the images show
Basis: 26 of 26 frame sheets viewed, all codes checked.

- The list of axes of diversity is presented as a grid of twenty white icons on black, four rows of five, each cell with a simple line symbol and a short caption centered below, the same horizontal and vertical spacing, with no borders or boxes separating the items (sheet 0002, q0010). The grid forms item by item before becoming complete (sheet 0001, q0009) and returns later in the same arrangement of five columns by four rows (sheet 0019, q0167 to q0169).
- There is a recurring device of pulling one or two icons out of the grid, enlarging them and leaving them alone with a larger caption, exactly at the moment the speech addresses that axis (sheet 0002, q0011 to q0012). The same device returns to represent intersection, and there the two icons come close together and start sharing a single three-line caption adding the two conditions together with a plus sign in the middle (sheet 0013, q0109, then q0112 and q0113).
- The same icons from the grid are recycled as a contextual caption over a real filmed scene: over the image of a family at the table, small white icons with short context captions appear, semi-transparent, in the lower band (sheet 0008, q0070). The speech mentions culture, environment, location and connectivity; it is the image that shows the same vocabulary of grid icons serving as an annotation on real life.
- The black text card alternates left and right alignment depending on which side the presenter enters the frame on next, and the supporting sentences accumulate one per frame without erasing the previous ones (sheet 0003, q0021; sheet 0004, q0029; sheet 0005, q0043 to q0045; sheet 0006, q0048). In a block of research questions the contrast grows with each frame, the first two questions in light gray and the third in bold white (sheet 0021, q0184 to q0186).
- From the "Ideate" stage on, the format changes: instead of a full-screen black card followed by a cut to the presenter, the same frame starts to contain both things, text on the left growing line by line and the presenter on video occupying about a third on the right, with no frame or dividing line, with the stage name in bold at the top (sheet 0007, q0060 to q0063). The format repeats identically in Design and Develop (sheet 0008, q0065 to q0068; sheet 0009, q0075 to q0077).
- The process diagram changes shape within the narrative: first a thin horizontal line with five words in colored cursive font, one color per stage and a colored dot marking the position of each one, then the same set redrawn in a circle, following the curvature of the path, with no line or marker dots (sheet 0007, q0055 to q0057).
- A small white triangular arrow at the top of the circle works as a current position marker, and the ring actually rotates between frames: in one passage "Test" is at the top and in the next frame "Release" takes that place, with "Test" moving down to the left (sheet 0008, q0064; sheet 0016, q0141 to q0142).
- List items enter by fading in: the new marker first appears at very low opacity, almost illegible, and only in the next frame does it become fully white (sheet 0014, q0123 to q0124; sheet 0015, q0127 to q0131; sheet 0025, q0222 to q0224). The exact order in which each item enters is information that only the image delivers.
- System interface captures always appear isolated, centered on a black background or inside a device frame drawn with a notch and status bar, never with a hand holding the phone (sheets 0003, 0010, 0011, 0014, 0018, 0019, 0022, 0023). Filmed scenes of people, by contrast, occupy the entire frame with no black background around them (sheets 0004, 0008, 0009).
- Text recognition is shown in two consecutive states: the Camera viewfinder with the photographed license plate and small yellow rectangles marking each recognized segment, and in the next frame a vertical context menu over the phone number, with six stacked actions, each with an icon on the right (sheet 0003, q0026 to q0027).
- The distance measurement is composed through overlay: over the real scene of a line of people, the semi-transparent frame of an iPhone appears, thin white outline and rounded corners, containing a vertical dotted line that runs up to the head of the person ahead, a large numeric label next to the base of that line, the word "End" in the top left corner and a thin progress bar at the bottom. In the next frame the background scene disappears and only that screen remains, enlarged and centered (sheet 0004, q0034 to q0035).
- The image description flow appears chained across three screens: the photo in the Photos app with a thumbnail strip and a bottom bar for share, favorite, information and delete; the same photo in Markup with a vertical menu listing Description, Text, Signature and Magnifier over a drawing bar; and the photo attached in a Messages conversation, with the description written by a human in a separate bubble, outside the phone's screen (sheet 0011, q0091 to q0096).
- The Memory card is the repeated component of the final block, always with the same anatomy: background photo, heart and ellipsis icons in the top corner, bold title and smaller subtitle at the base (sheets 0018, 0019 and 0020). In one passage the four cards move from a fanned out arrangement, overlapping and with reduced opacity behind, to an aligned, evenly spaced row, all opaque (sheet 0020, q0172 to q0173).
- The action to reduce a person's presence appears at different entry points in the app, always as a list item inside a light, rounded-corner floating card, divided into blocks; in the Memory card menu the destructive delete action appears highlighted in red, and in a pair of side-by-side screens the equivalent option appears with a highlight box around it in one of them and with no highlight in the other (sheet 0022, q0195 to q0198). The next iteration replaces the menu with a full-screen modal with a circular photo at the top, two list-format options with a bold title, smaller explanatory text, a circular selection indicator on the right and a full-width blue button (sheet 0023, q0203 to q0205).
- An icon swap is shown as a side-by-side pair, with no text label: the thumbs-down glyph next to a circle of a person with a minus sign, both in white on black and in the same thin line style as the axis icons (sheet 0024).

Visual proportion: per the notes, the initial sheets alternate a full-screen black card and a cut to the presenter; from the "Ideate" stage onward the split layout predominates, with the slide on the left and the presenter on the right in the same frame (sheets 0007 to 0009, 0014 to 0017 and 0024 to 0026). Short blocks of real system interface also appear (sheets 0003, 0010, 0011, 0012, 0014, 0018, 0019, 0022 and 0023), some filmed scenes of people (sheets 0004, 0008, 0009) and one sheet in which the presenter occupies almost all the frames (sheet 0026).

Recorded divergences or limits: the notes point to content cut off by the frame edge at two points, the word "Develop" appearing truncated in the diagram (sheet 0006, q0053 and q0054) and the start of a third line of text cut off at the bottom (sheet 0008, q0066 to q0068). They also record that the change of presenter on screen happens before the person is named in the speech (sheet 0015) and that, in sheet 0022, the additional menus were noted generically, without item-by-item transcription.
<!-- /visual:wwdc2021_10304 -->

## Practice audio haptic design (id: wwdc2021_10278, 16.0 min)

- Basis: transcript and 13 of 13 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2021/10278/.
- Central thesis: to create multimodal experiences that feel magical, Apple uses three principles (causality, harmony, utility) together with the Core Haptics API, demonstrated in practice by adjusting the HapticRicochet sample project in Xcode.

- The design process Apple describes: in the speech, the presenter works directly in Xcode on the HapticRicochet project (derived from an earlier project called HapticBounce), a ball that rolls and collides with the edges of the iPhone, grows when touched, gains a shield when touched again, and whose shield wears down with each collision until the ball implodes; there is also a background texture that can be activated by touching the background.
  - First reviews the three principles of audio and haptic design used internally at Apple.
  - Then presents the four fundamental elements of Core Haptics: engine (the connection to the device's physical actuator), player (playback control: start, stop, pause), pattern (a collection of events over time) and event (the building blocks of the experience; the most common types cited are transient and continuous). Shows an .ahap file (Apple Haptic Audio Pattern, in JSON) open in the QuickLook Visualizer on macOS 12.
  - For the shield moment, applies the harmony principle: dissecting the visual animation, the haptic feedback and the sound feedback separately before bringing the three together.
    - Compares two ready-made assets: ShieldTransient (haptics made of three transient events, together with a continuous, progressive audio) and ShieldContinuous (continuous, progressive haptics, together with a "wobbly" audio that decays). In neither of the two do the haptics and the audio match each other.
    - Decides to recombine: uses the continuous haptics from ShieldContinuous with the audio from ShieldTransient, editing the .ahap file in a text editor and swapping the audio file reference from ShieldB.wav to ShieldA.wav in the AudioCustom event type (whose volume can be adjusted by a ParameterValue). Then changes, in the code, the player initialization to load this revised ShieldContinuous file.
  - For the rolling texture, solves two problems:
    - A technical problem: the texture stopped playing after a few seconds because the texture's .ahap file only had 2 seconds of haptic content. The fix was to change the player type to CHHapticAdvancedPatternPlayer (the advanced variant of the pattern player, which has extra features such as pause, resume and callbacks) and enable looping, keeping the rest of the code the same.
    - A design problem: the texture's haptic pattern was dense (almost 100 events in 2 seconds), but the visual background texture was coarse (few dots). The fix was to swap the background visual asset for a "Fine" version, with denser dots, to match the density of the haptics.

- Principles stated and the why of each:
  - Causality: it needs to be obvious what caused the feedback. Example given: the ball's collision with the wall of the phone generates sound and haptics together; the rolling texture haptics only appears when the background visual (the grid of dots) is visible, so that the cause is clear.
  - Harmony: the senses work better when they are coherent, consistent and work together; the experience should feel like what you see, what you hear and what you feel at the same time. Example given: a small ball should sound and feel small; a big ball should sound and feel heavier, as if it had more real mass.
  - Utility: the feedback needs to have clear value for the experience; don't add haptics or sound just because it is possible, because that quickly becomes overloaded and unpleasant. Reserve haptics and audio for meaningful moments in the app, such as the ball's growth.

- Concrete interface-building techniques (with exact numbers when spoken):
  - The visual animation of the moment of gaining the shield lasts 500 milliseconds.
  - The .ahap format (Apple Haptic Audio Pattern) uses JSON syntax.
  - The rolling texture's .ahap file had only 2 seconds of haptic content, with almost 100 events (entries) in those 2 seconds, which motivated both the looping fix and the density of the visual.
  - To feel the haptics, a physical iPhone model 8 or newer is required; the simulator does not reproduce haptics.

- Examples cited (apps, screens, components) and what each one teaches:
  - iOS Flashlight button: cited as a reference for a unified, clear, precise and concise multimodal experience (visual animation, sound and haptics), the result of an iterative and creative process of design and engineering together.
  - HapticRicochet (ball, collisions, shield, rolling texture): teaches, in practice, how to compare and recombine ready-made audio and haptic components to achieve harmony between the senses, and how to resolve a mismatch between haptic density and visual density.
  - ShieldTransient and ShieldContinuous assets: teach that not every ready-made pair of audio and haptics matches, and that sometimes the solution is to recombine parts of different assets (the haptics of one with the audio of the other), not discard either of the two.
  - CHHapticAdvancedPatternPlayer with looping: teaches the difference between the basic and advanced player of Core Haptics for solving a specific technical problem (a pattern that "ends" before the interaction finishes).

- Quotes:
  - "It should feel the way it looks, and the way it sounds."
  - "Don't add feedback just because you can."

<!-- visual:wwdc2021_10278 -->
### What the images show
Basis: 13 of 13 frame sheets viewed, all codes checked.

- The principle slides use a fixed visual vocabulary: black background, white title in the upper left corner and a schematic smartphone icon on the right with a red dot representing the feedback. Each principle gets a minimal variation of the same icon: a grid of dots filling the screen with a point of origin at the edge for causality, a single dot with the "HapticIntensity = 0.3" annotation next to it for harmony, and a lone central dot, without annotation, for utility (sheet 0004, q0028, q0030 and q0032). The numeric value annotated on the slide is not said in the speech.
- The Core Haptics architecture appears as a hierarchical diagram, color coded and built in three steps: first the title alone, then the engine box in dark blue and player box in light blue, and finally the pattern box in green with three smaller event circles connected below by vertical arrows (sheet 0005, q0037 to q0039; the same diagram reappears in sheet 0006, q0046).
- The Finder's QuickLook is shown as a real tool for inspecting the .ahap file, with two overlaid graphs, an orange intensity curve and thin blue vertical bars, plus the window header counting the file's events, and callout lines pointing to points on the graph with the labels "Transient" and "Continuous" (sheet 0005, q0040 to q0044).
- The difference between the two event types is recorded as a difference in shape in the graph: three discrete vertical marks in the haptics block over a continuous waveform in the audio block in one asset (sheet 0007, q0062 and q0063) against an ascending ramp of solid orange fill, without discrete bars, in the alternative asset (sheet 0008, q0064 to q0066).
- The design specification is organized by sensory channel in three parallel rows, Visual, Haptic and Audio, each with a colored badge naming the corresponding asset file, gray for the animation, green for the .ahap and yellow for the .wav, next to a large circle representing the ball with shield. The rows are revealed in stages, first the Visual one and then the Haptic and Audio ones together (sheet 0006, q0052 to q0054); further on the Haptic and Audio rows start displaying two badges each, to compare the alternative assets, with the highlight alternating between them (sheet 0007, q0055 and q0056).
- The editing of a file is shown as an exact before and after inside the code itself: a gray highlight rectangle covers the value of the audio file's path field, and between one frame and another this value changes from one file name to another (sheet 0008, q0069 to q0071). The speech describes the swap; the image documents the earlier and later state.
- The Swift editor appears in a dark theme with syntax highlighting by type, and a gray highlight moves through the code following the speech, changing from an isolated line to an entire block of lines depending on the subject (sheet 0007, q0057 to q0060; sheet 0010, q0085 and q0086; sheet 0011, q0094 and q0095; sheet 0012, q0102). This precisely locates which passage is being explained at each moment.
- The choice between two player classes is presented as a comparison table, with feature columns and two player rows, support marked by a green circle with a check and absence indicated by an empty cell. In the table, the basic class only has a mark in the first column (sheet 0011, q0091 to q0093).
- The haptic density gets visual proof: the texture file's graph shows dozens of thin blue vertical bars very close together, with a transient count in the window header (sheet 0010, q0090), in direct contrast with the three sparse transients of the asset seen before (sheet 0007, q0062 and q0063).
- The background texture states are always compared side by side, two smartphone icons with a two-level caption naming the state and the asset file: first smooth background against background with a dot pattern (sheet 0010, q0082 to q0084), then two different densities of dots labeled dense and coarse (sheet 0011, q0098 and q0099). The actual asset swap appears between frames, with the right icon going from an empty outline to filled with the dense pattern (sheet 0012, q0100 to q0101).
- The work environment is shown together with the slide, not in a separate cut: the Xcode file browser appears to the right of the instructions slide with icons colored by file type, and the slide gains two more lines of instruction while the file panel grows, with a list item selected in blue (sheet 0006, q0047 to q0049).
- The slide lists enter through progressive reveal, with sub-items first appearing faded and only later legible, both in the slide of problems to solve (sheet 0010, q0082 to q0084) and in the closing (sheet 0013, q0110 to q0112).
- The agenda slide uses typographic hierarchy to mark progress, with the previous topics in light gray above and the current topic in black and bold, in a larger size (sheet 0002, q0018).
- The closing is a side panel that occupies the left half of the screen, with the presenter visible on the right half, a list of topics growing until it includes an additional resources section, and a footer with a thin dividing line separating the name of the cited session, on the left, from the event code on the right (sheet 0013, q0110 to q0112).

Visual proportion: by the notes, most of the frames are slide or tool capture, Xcode, QuickLook and code editor, with the presenter entering in short cuts between blocks; the physical iPhone in hand appears in seven sheets (0001, 0002, 0006, 0009, 0010, 0011 and 0012) and in no frame is there a simulator screen.

Recorded divergences or limits: in sheet 0011 the notes name the same line of code in two different ways, as "texturePlayer?.loopEnabled = true" in the screen description and as another variable in the description of the change between frames (q0094 and q0095). They also record a frame that is entirely black, with no visible element, different from all the others in the sheet (sheet 0012, q0105), and stretches with no perceptible change between consecutive frames (sheet 0009, q0073 to q0074).
<!-- /visual:wwdc2021_10278 -->

## What this group reveals about the Apple way

- Apple treats both a design tool (SF Symbols app, id: wwdc2021_10288) and a technical API (Core Haptics, id: wwdc2021_10278) with the same process care: instead of showing the finished result, the speech documents each decision in real time, including comparisons between alternatives before choosing one.
- The value of saving repeated work for whoever builds the app appears frequently: automatic localization of symbols with no extra effort from the developer (id: wwdc2021_10288), automatic accessibility of the standard UIKit, AppKit and SwiftUI controls (id: wwdc2021_10304), and automatic sensory consistency between visual, sound and haptics when well designed (id: wwdc2021_10278).
- The three videos use short, named principles as a working tool, not as loose slogans: causality, harmony and utility in id wwdc2021_10278; the axes of diversity and intersectionality in id wwdc2021_10304; symbol name versus deprecated name in id wwdc2021_10288. In every case, the named principle becomes a checklist that repeats throughout the demonstration.
- The process described is always iterative and comparative, never "right the first time": two versions of a shield asset tested side by side (id: wwdc2021_10278), two iterations of the "feature less" action in Memories (id: wwdc2021_10304), and comparison between the current name and the deprecated name of a symbol (id: wwdc2021_10288).
- There is a recurring emphasis on taking into account the real context of whoever uses the product: language and reading direction in the case of the symbols (id: wwdc2021_10288), the axes of diversity and intersectionality in the case of inclusive design (id: wwdc2021_10304), and the requirement of a physical iPhone (not a simulator) to validate the haptic experience (id: wwdc2021_10278).

## No transcript

No file in this group was left without a transcript; the three videos (wwdc2021_10288, wwdc2021_10304, wwdc2021_10278) had a complete transcript of the speech.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2021_10288.md, 120 lines read (complete file, no truncation notice), read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2021_10304.md, 289 lines read (complete file, no truncation notice), read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2021_10278.md, 30 lines read (complete file, no truncation notice), read to the end: yes.
