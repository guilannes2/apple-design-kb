# wwdc2019 (part 2)

## Designing Award Winning Apps and Games (id: wwdc2019_802, 46.7 min)

Basis: transcript and 40 of 40 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2019/802/.

Central thesis: the apps and games that win the Apple Design Awards do not have a formula of criteria, but share recurring values (innovation, trust, refinement, beauty, inclusion and attention to detail), and each value appears illustrated by a design process story of a specific app or game.

The design process Apple describes, by value:
- Innovation (Asphalt 9, HomeCourt): questioning the domain's basic assumptions from the start ("why do we do it this way, just because it's always been this way?"), converting problems into ideas, testing and iterating before assuming the solution is final. In HomeCourt's case, the team removed obstacles one at a time (tripod, lighting, manual line drawing) until a friction-free experience remained.
- Trust (Pixelmator Photo): when a feature uses machine learning, visually revealing the cause and effect of the action ("attribution"), so the person understands what is being adjusted and can intervene.
- Refinement (The Gardens Between, Butterfly iQ): exploring directions very distant from the final result before converging; testing real-world metaphors with the target audience and discarding the ones that don't work, even when they seem obvious.
- Beauty (Thumper, ELOH, Ordia): radical simplicity on screen to sustain immersion; hiring dedicated specialists (illustrator, sound designer) when aesthetics are central to the experience; maintaining visual coherence across all screens.
- Inclusion (Pixelmator Photo, Ordia): using native system components to inherit accessibility; simulating disabilities (color blindness) over the design itself and rebalancing colors.
- Attention to detail (Flow by Moleskine): solving the fundamentals of the interaction first (prototypes with plain text buttons, no visual style) before investing in visual design and animation.

Principles stated and why:
- "Question assumptions from the start": Asphalt 9 dropped the traditional racing controls (acceleration, brake, turning) because manual turning was prone to player error; they replaced it with path and item selection via swipe, and this reduced frustration and freed up attention for strategy.
- Simplifying to what the person wants to do, without removing value: HomeCourt automated detection of the hoop, the three-point line, legs and then the full body pose via ML, eliminating the need for a tripod and perfect light, down to running safely propped on the ground.
- Revealing the ML model's intelligence in the interface (attribution): in Pixelmator Photo, the "Magic Wand" button applies a trained model, but the parameters (exposure, skin tone etc.) animate visibly and remain individually editable, which builds trust because the person sees cause and effect.
- Not copying physical-world metaphors without testing: Butterfly iQ tried to directly replicate the physical dials of the traditional ultrasound cart on the iPhone screen; in testing with doctors this took up valuable image space unnecessarily, so the team drew inspiration from the iOS Camera app and moved contrast and depth to gestures (lateral pan = contrast, vertical swipe = depth), without constant visual persistence of the dials.
- Refining is different from getting it right the first time: The Gardens Between's design artifacts showed versions of the game with Snow White and Sleeping Beauty, completely different from the final result, showing broad exploration before converging.
- Aesthetics can have a practical function, not just a decorative one: in ELOH, the illustration and sound reinforce the legibility of the interactive elements (few, but polished) and the difficulty pacing; each time an especially hard level is solved, the next one is simpler, which gives room to notice the aesthetics again.
- Using a native component instead of recreating one: Pixelmator Photo replaced the Mac app's checkboxes with native iOS switches in the iPad version because they communicate state more clearly and already come with accessibility support (labels that can be activated in Settings).
- Simulating the user's limitation on the product itself: Ordia tested the game in full monochrome mode and applied filters that simulate different types of color blindness over screenshots, then rebalanced colors to keep all elements distinguishable.

Concrete interface-building techniques cited:
- Interaction: TouchDrive (Asphalt 9) uses swipe for path/item selection and tap-and-hold for nitro/boost, replacing acceleration, brake and manual turning.
- Machine learning applied to the interface: Pixelmator Photo's model trained with 20 million professional photos, triggered by a single button.
- Gestures mapped to parameters: in Butterfly iQ, "panning left and right changes the contrast and swiping up and down changes the depth"; a ruler appears on the right side during the depth swipe and retracts when not in use.
- Minimalist onboarding (Thumper): title with an epic sequence right at the opening; pause button that turns into a simple diagonal bar and "disappears"; the instruction "Swipe Up to Jump" combined with a 3, 2, 1 countdown before the player even asks when; a subtle arrow reinforcing the gesture; sound signaling when to swipe.
- Vitality state without a HUD (Thumper): vitality is shown on the playable beetle's own wings ("full wings at full health, no wings at half health"), with no numbers or separate bar, to keep the focus on the track.
- App icon derived from the product's own brand (HomeCourt): the letters H and C emerge from the outline of a basketball court; the orange background evokes the color of the ball.
- Consistent design language end to end (Ordia): organic "blobby" theme applied to menus, transitions, levels and characters; color used to communicate whether a creature is friendly, hostile or for navigation; the standard iOS Share icon used to reinforce belonging to the platform.
- Accessibility: native switch instead of a custom checkbox (Pixelmator Photo); colorblind mode with a rebalanced palette and testing in full monochrome (Ordia), citing the figure of "over 300 million people worldwide with some form of colorblindness".
- Color and type (Flow by Moleskine): tool and color selector with "over 1,400 unique color names" in the app; interaction prototypes built first with only plain text buttons, no visual style, to validate the interaction before drawing it visually.
- Animation as communication: in Flow's tool editor, state-transition animation reinforces how to use the interface and draws attention, according to the speech.

Examples cited and what each one teaches:
- Asphalt 9 (TouchDrive): questioning an entire genre's standard controls can open up a new category of gameplay.
- HomeCourt: each setup obstacle removed (tripod, light, manual marking) is one less barrier between the person and the app's value.
- Pixelmator Photo: a result generated by ML only builds trust when the adjustment is visible and editable, not a black box.
- The Gardens Between: the design artifacts reveal that the final result rarely resembles the first drafts.
- Butterfly iQ: physical-world metaphors help create familiarity, but need to be tested with the real audience before becoming an interface standard.
- Thumper: radical simplicity on screen sustains immersion; minimal sound and visual feedback still teaches the mechanic.
- ELOH: a dedicated illustrator and sound designer elevate interactive elements that, on their own, are few and simple.
- Ordia: a consistent visual language ("same environment" throughout the experience) and accessibility testing (color blindness, monochrome) elevate the perception of quality.
- Flow by Moleskine: low-fidelity prototypes (plain text) resolve the interaction before any visual decision.

Short quotes: "When we first launched, the experience was actually not magical." (HomeCourt founder, about the app's initial version which required a tripod and perfect light).

<!-- visual:wwdc2019_802 -->
### What the images show
Basis: 40 of 40 frame sheets viewed, all codes checked.

- The talk uses a real game design board as evidence of a product's visual vocabulary: palettes labeled "PRIMARY COLORS" and "SECONDARY COLORS" in square blocks, a component state table with the labels NORMAL, PRESSED, TOGGLE and DISABLED, cyan triangular arrows numbered 1 to 3, "CLAIM" and "BUY" buttons, typographic specification with "RAJDHANI Medium" and "RAJDHANI Semibold" and the full alphabet in uppercase, lowercase and numbers, plus hand-annotated pencil concept art (sheet 0002, q0011 to q0013).
- The presentation's throughline is a fixed list of six words (Innovation, Trust, Refinement, Aesthetics, Inclusion, Attention to detail) that reappears at every topic change, with the active item in full white and bold and the rest in dimmed gray, that is, hierarchy through opacity (sheets 0002, 0005, 0010, 0014, 0015, 0019, 0033, 0035, 0036, 0038 and 0039). On sheet 0023 the same list appears next to three app icons, with no notes recording which item was highlighted.
- Two different apps appear with the same settings screen pattern: option cards of equal size, each with an icon-diagram, short label and selection state marked by a colored outline. In Asphalt 9 there are three cards, "TOUCHDRIVE" selected with a yellow outline, "TAP TO STEER" and "TILT TO STEER", with a "SWIPE SENSITIVITY" slider below (sheet 0004, q0034); in HomeCourt there are two cards under "DEVICE SETUP", with "GROUND" selected in a red outline and short one-line captions on each option (sheet 0008, q0069).
- The game's onboarding is designed as a layer over the scene itself, not as a separate panel: over the racing image the explanation phrase and the "HOLD TO DRIFT" label appear, accompanied by the circular icon of the corresponding button (sheet 0003, q0027). In the earlier gameplay frames of the same sheet there is only racing HUD, with position, the speedometer climbing from 85 to 110 and then 146, and the "TOUCHDRIVE ON" badge appearing between q0021 and q0022.
- The elimination of manual steps is staged in two phases. On sheet 0007 the numbered list of seven steps appears as plain text, with no phone frame, and shortly after with items 1 to 5 dimmed and items 6 and 7 in full white (q0058 and q0059). On sheet 0008 the same list reappears overlaid on a real photograph of a court, now with items 4 and 5 struck through by a line, while the detection appears as a red rectangle over the backboard and, in the following frames, as an orange line skeleton on the player's joints, which changes posture between q0070 and q0071 (q0065, q0066, q0070 and q0071).
- The anatomy of HomeCourt's feed card becomes visible through the difference between two consecutive frames: the same user header, the same workout title, the same stars and the same two statistic numbers (12 and 20), changing only the lower media, which goes from a video thumbnail to a "U"-shaped chart with percentages by court zone, among them 71% and 67% (sheet 0006, q0047 and q0048).
- Pixelmator Photo's adjustments inspector appears in a three-zone layout, central image with a histogram in the corner, right panel with parameter name plus switch plus slider control, and a bottom bar of presets as colored thumbnails. The sequence of frames shows the state actually changing: a dark, desaturated photo with switches lighting up in blue, then a bright photo, then sliders going from zero to filled-in percentages (sheet 0011, q0095 to q0099).
- The same app's advanced panel shows direct color control beyond the linear sliders: Exposure, Highlights with a negative value, Shadows, Brightness, Contrast and Black Point, and below a "Color Balance" section with a circular color wheel labeled "Master" plus the "3-Way Color" option, and a "Selective Color" section with a hue-range chart, in an order that goes from global to granular (sheet 0013, q0112 to q0117).
- The native iOS component is dissected on screen: the switch appears enlarged and isolated in both states, on with a blue background and the circle to the right, off with a gray background and the circle to the left, and also small inside the app's real panel next to the "White Balance" label, with a translucent circular highlight zooming in on the same control (sheet 0034, q0299 to q0304).
- The Butterfly iQ case is built through direct comparison of versions and references: on sheet 0021 the 2016 demo shows fixed values in the bottom bar, "11cm" for Depth and "38%" for Gain, next to two square icons, with the "Freeze" and "Record" buttons below (q0181 to q0183); on sheet 0022 a second iPhone alongside shows the iOS Camera app, with icons at the top, mode labels at the bottom and a white circular shutter, and the gesture-based version displays a central "Gain/TGC" popup with a percentage and a numbered vertical ruler on the right edge of the image (q0191 to q0195). Sheet 0022 also shows the measurement over the image, two blue dots connected by a dashed yellow line with the value fixed at the bottom.
- The process artifacts shown are technical documents, not generic illustrations: a board with an uppercase title over a level excerpt, a central drawing and red annotation lines for path, water flow and material, which gains blocks of written notes between q0158 and q0159; and a second board over a farewell scene, with line drawing, a diamond diagram with circles at the vertices and a column of sketch thumbnails on the left (sheet 0018, q0158 to q0161).
- The fidelity progression appears staged on real screens. In Flow by Moleskine, the low-fidelity prototype is just gray rectangular boxes with text, no color and no icon, with a red scribble in the center; then comes an intermediate version with a gradient bar labeled "Marker" and a triangular slider; then the final editor in a cross layout, with the color name, the "SIZE 5" value and a confirmation icon (sheet 0037, q0325 to q0329). In ELOH, the same character goes from a black line on white to a colored version in a purple and turquoise gradient, and only then receives the evaluation word next to it (sheet 0028, q0247 to q0249).
- The same component is shown in two screen sizes at the same time, iPad and iPhone side by side displaying the color editor in a cross at the same layout proportion, next to the large number "1,400" with the caption of color names (sheet 0038, q0335 to q0338).
- In the games, the screen has almost no interface: The Gardens Between shows only a pause icon in the upper-left corner throughout the sequence (sheet 0015, q0129 to q0131), and Thumper keeps only the level indicator in the upper-left corner, "LEVEL 2-1" at q0215 and "LEVEL 1-5" on sheet 0025, with a pause button or a numbered circular icon in the upper-right corner, no health bar or other HUD elements, and with iOS's own gesture indicator strip at the bottom (sheets 0024 and 0025, q0215 to q0224).
- Ordia's visual language cohesion is demonstrated by going all the way to the least glamorous screen: translucent achievement card at the top, map with a "10/10" counter and the "SETTINGS" screen with native switches aligned to the right of the labels, including colorblind mode and sync, plus a reset progress button; and a comparison of two map screens where the share icon appears next to the play button between q0283 and q0285, highlighted by a light blue outline in one of the two compared frames (sheet 0032, q0281 to q0285).
- Production tool on screen: a screenshot of animation software on a MacBook Pro, with canvas on the left, layers panel on the right, horizontal timeline with keyframe markers and a preview thumbnail in the corner; between consecutive frames, the character's facial expression changes subtly, evidencing the keyframe adjustment (sheet 0029, q0254 to q0256).

Visual proportion: according to the notes, typographic slides and captures of app, game, design board and photography predominate; presenter-only frames appear in a good part of the sheets, always a minority within each one, and the notes do not record any live demonstration, only captures, photographs and mockups in device frames.

Recorded divergences or limits: the notes make an exception for q0072, handled outside the frame-by-frame description because the crop of sheet 0008 brings three distinct iPhone screens on the bottom row; on sheet 0040 part of the handwritten annotations is declared illegible at the frame's distance; and on sheet 0035 the same trio of screens appears twice in a row with no visible change between q0307 and q0310.
<!-- /visual:wwdc2019_802 -->

## Designing Great ML Experiences (id: wwdc2019_803, 57.8 min)

Basis: transcript and 42 of 42 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2019/803/.

Central thesis: designing a good machine learning experience requires designing both the model (the data used to teach it and the metrics used to evaluate it) and the interface (how the model's results are presented as output and how people give input back to the model); ML design goes beyond the screen.

The design process Apple describes:
- Define the desired experience before collecting data: understand what you want to build and then intentionally decide which data to collect, instead of just sampling existing customers or using ready-made academic datasets, because this can reinforce systemic biases instead of reflecting the desired world.
- Choose metrics aligned with values, not just numbers that are easy to measure: metrics are proxies for abstract concepts that are hard to measure (good experience, satisfied customer, strong brand); if the experience seems bad but the metric says it's good, the metric is the one that's wrong.
- Group failure cases by category and scenario, decide whether each type of error is better solved with design (non-ML) or with a better model, and deliberately design for the failure scenario (not just the happy path) when sketching the experience.
- After defining data and metrics, design the interface on two fronts: outputs (how the model's result is presented) and inputs (how the person interacts with and feeds back into the model).

Principles stated and why:
- "You shouldn't optimize for the customers you have. You should optimize for the customers you want" and "you should reflect a better world, that world that you want it to be": biased data collection (for example, facial recognition that historically didn't work well for people of color) requires intentional collection across races, cultures and scenarios, not passive sampling.
- Metrics don't tell the whole story: on Face ID, the metric "a one in a million chance of a stranger unlocking the phone by chance" was communicated publicly, but Apple also needed to communicate the limitation with twins or similar-looking siblings, because every failure is a real person and a real scenario.
- Prefer outputs with multiple options when the model can't know everything about the person's preference: in Maps, instead of a single "optimal" route, three distinct routes (one for the northern bay region, two for the east) give the person real control, because the ideal route depends on preferences the model doesn't capture (scenic route, no tolls, no highway).
- Use attribution to explain decisions with objective facts, not assumptions about taste or emotion: the App Store explains recommendations by saying "because you downloaded app X" instead of claiming to understand the person's taste, because profiling emotions and preferences leaves people feeling misunderstood or "boxed in".
- Translate confidence into understandable language: instead of saying "85% match", the App Store uses "recommendations based on apps you've downloaded"; the weather app, in turn, uses percentage directly (30% chance of rain) because people have already learned to interpret that number over time; the flight app Hopper avoids percentages (it doesn't say "65% chance of the price dropping") and instead recommends the direct action (wait or buy now), because the difference between 65% and 70% is not actionable for most people.
- Prefer ranges to point numbers when exact precision is false: the ride-hailing app Lyft shows an arrival time range instead of a single time, because traffic and extra stops make any exact number misleading.
- Ask for confirmation when confidence is low instead of acting alone: Photos asks for confirmation of a person's identity before automatically labeling future photos of them.
- Communicate limitations and offer alternatives: when Memoji can't recognize the face (camera covered, dark environment, face out of frame), Apple uses inline coaching hints; when Siri can't create a timer on the Mac, it suggests a reminder instead of simply saying it can't, because it understands that the goal (being alerted at a certain time) is the same.
- Prioritize negative feedback over positive in explicit feedback: positive feedback can be implicitly inferred (reading, saving, sharing an article), so asking to "love" every item overburdens the person; for negative feedback, use language with a clear consequence ("suggest less", "hide the suggestion") instead of ambiguous labels like "Dislike".
- Corrections as the preferred pattern: letting the person correct the model's result using controls they already know (rewriting a word on the keyboard, dragging the Photos rotation/crop slider) instead of creating a new interface; this works as implicit feedback to improve the model with no extra perceived effort.

Concrete interface-building techniques, with numbers when spoken:
- Example metric of model accuracy: "the model gave the correct prediction 75% of the time".
- Face ID security: "one-in-a-million chance that a random person could unlock your phone using Face ID".
- Translated versus raw confidence: rejected example of "85% match" swapped for explanatory text; weather uses "30% chance" directly; Hopper avoids figures like "65%" vs "70%" because they're not actionable; example of bad practice cited: "I'm 72% confident you'll get there at 1:30".
- Siri watch face: up to 19 customizable data sources ("customize up to 19 different data sources").
- Minimal calibration: Face ID asks you to scan your face twice ("It asks you to scan your face twice") and then never recalibrates again, even with a change of glasses, hairstyle or age; HomeCourt calibrates automatically by pointing the front camera at the rim, with no manual lines to draw and no multiple angles.
- Implicit feedback on the keyboard: the size of each key's touch area increases or decreases according to the likely word, without changing the keyboard's visual appearance.
- Output patterns described: multiple options, attribution, confidence, limitations.
- Input patterns described: calibration, implicit feedback, explicit feedback, corrections.

Examples cited and what each one teaches:
- Photos (search "dog"): the value of an ML feature is not only in the search interface, but in the recognized categories and the quality level of each category, design decisions just as much as the screen itself.
- Maps: several distinct routes beat a single "best" route when the person's preferences are unknown to the model.
- Siri watch face: selecting a small, relevant subset from many possible sources (19) avoids overloading a small screen.
- App Store: factual attribution ("downloaded X") avoids claiming to understand taste; editorial content complements recommendations purely driven by time-spent metrics, so as not to trap the person in a niche (the example given is games).
- Weather / Hopper / Lyft: the same variable (confidence/uncertainty) translated in three different ways depending on how accustomed the person already is to the number (percentage), or needs a direct action (buy now), or a range (estimated time).
- Memoji / Siri (timer on the Mac): communicating the limitation at the right moment and suggesting an alternative maintains trust in the feature instead of simply failing.
- Photos (face recognition), Safari (Siri suggestions), keyboard (autocorrection of "Angie"/"angle"): examples of calibration, explicit feedback and corrections respectively.

Short quotes: no literal quote in quotation marks was used by the presenters in this video; the content is mostly direct exposition from Apple's design team (Kayur, Rubii, Cas), with no third-party statements quoted in quotation marks.

<!-- visual:wwdc2019_803 -->
### What the images show
Basis: 42 of 42 frame sheets viewed, all codes checked.

- The conceptual diagram is built up incrementally, sheet after sheet: first just the green "Interface" box and a person icon connected by two arrows (sheet 0004, q0036), then the blue "Model" layer above it (sheet 0006, q0052 to q0054), then each layer splits into two sub-boxes, Data and Metrics inside Model, Outputs and Inputs inside Interface (sheet 0007, q0055 to q0058), and finally the Interface sub-boxes display four items each (sheet 0016, q0144). Near the end the block reappears alone, only with Interface, Outputs and Inputs (sheet 0039, q0349 to q0351), and the complete set, with the blue Model on top and the person icon below, returns one last time (sheet 0040, q0353, q0355 and q0356).
- The difference between traditional code and a model is shown by the same horizontal chain with the middle piece swapped: animal photo, Swift logo, output box with the dog label, and a hyena receiving that same label in subsequent frames (sheet 0005, q0039 to q0043). Then the Swift logo exits and a vertical blue "Model" bar enters, first with three animal photos going in and three labels coming out (sheet 0006, q0048) and then as three stacked flows of different inputs, microphone, photo and text being typed (q0049 and q0050).
- The data gets its own screen: a uniform grid of photos with a category caption under each image (sheet 0007, q0062 and q0063), which returns filling almost the whole screen and receives the overlaid phrase that data determines the model's behavior (sheet 0008, q0064 to q0066, with the phrase entering at q0065). Next comes a mosaic of faces of different ethnicities, ages and genders (sheet 0008, q0069 and q0070), which gets the caption about intentional collection at q0071.
- The practical recommendation slides follow a progressive checklist template: fixed title at the top left, items stacked with no marker, each one entering as the speech progresses and remaining on screen. "Data Needs to Be Designed" starts with just one item (sheet 0009, q0080 and q0081) and reaches four (sheet 0010, q0082 to q0086, q0089 and q0090), and "Metrics Reflect Values" repeats the same mechanic (sheet 0015, q0128 to q0131 and q0135).
- An isolated metric gets its own card, with a huge number and a small label underneath, used twice in the same composition: "75%" over "Accuracy" (sheet 0011, q0094 and q0096) and "1 in 1,000,000" over "Face ID" (sheet 0012, q0102, q0103 and q0105).
- The error is presented as a pair of images: the presenter's portrait in a white badge-style frame appears alone (sheet 0012, q0106) and gains the portrait of a similar-looking man next to it (q0107 and q0108); on the next sheet the same frames darken to receive the highlighted phrase about errors not all being equal (sheet 0013, q0109 and q0110).
- Green index card with an active item: the four outputs appear on the same card, one item in full white and the rest grayed out, gone through one by one before the definition slide (sheet 0017, q0145 to q0150) and picked up again with the confidence item highlighted (sheet 0022, q0197 and q0198); on sheet 0021 that card appears faded behind the definition slide (q0183 and q0184). The same card repeats for the four inputs, swapping the bold item on each frame (sheet 0029, q0254 to q0256).
- The examples never appear as a loose sketch: they enter within the device frame with the native interface reproduced. Maps on the MacBook with a side panel listing three routes of 1 hr 3 min, 1 hr 5 min and 1 hr 13 min (sheet 0018, q0160 and q0161); App Store on the iPhone whose attribution caption changes from a generic phrase about downloaded apps to the citation of a specific app (sheet 0021, q0184 to q0189); and, further on, the same App Store with the "85% Match" badge (sheet 0023, q0199 and q0200).
- Three different treatments of uncertainty appear on neighboring sheets: the flight app with a large price, a primary blue button and a forecast card with an orange arrow for drop and red for rise (sheet 0024, q0208 to q0213); the ride app with a purple route and a list of options with the price aligned to the right (sheet 0025, q0219 to q0221); the weather app with the temperature in large type and a time range (sheet 0023, q0203 to q0205).
- Calibration is shown as a complete flow, not as a concept: the basketball app with an orange icon and, next, the iPad screen with the court video and the instruction to frame player and rim (sheet 0029, q0260 and q0261), then the request for a shot and the green confirmation screen (sheet 0030, q0262 to q0265); Face ID with a progress ring around the face, "Cancel" and accessibility options at the edges (sheet 0002, q0013 and q0014), the ring completing in stages (sheet 0031, q0276 to q0278), the completion screen with a full-width blue button (sheet 0031, q0272) and the Settings screen with green switches and a destructive action in red (sheet 0031, q0274 and q0275).
- The invisible keyboard adjustment is made visible through a didactic overlay: the same keyboard screen appears normal in a series of frames and, in the middle ones, with blue smudges covering an area larger than the drawn key, returning to normal afterward (sheet 0034, q0298 to q0303).
- The evolution of explicit feedback reuses the same component instead of creating another: two round heart buttons appear over the dimmed Safari screen (sheet 0035, q0313 to q0315), become items inside the native action menu (sheet 0036, q0317 and q0318) and in the end are swapped, in the same menu, for options that name the consequence, suggest less from a given source and hide the suggestion (sheet 0036, q0322 to q0324).
- Correction also uses an already familiar control: in Messages, the typed word appears underlined being replaced by the suggestion and then opens the menu with the two options not to correct (sheet 0037, q0331 to q0333); then comes editing in the Photos app with a bottom toolbar, rotation icons and slider, and the same photo in portrait mode (sheet 0038, q0341 and q0342; sheet 0039, q0343 to q0345).
- The closing switches visual language already by the end of sheet 0040: slide and screen capture give way to video scenes with an overlaid word, pulse with Apple Watch and running (sheet 0040, q0359 and q0360), wheelchair and objects being identified with the iPhone in hand (sheet 0041, q0361 to q0369), electrocardiogram on the watch and drawing with a pen (sheet 0042, q0371 to q0373), ending on the references slide and the logo (sheet 0042, q0376 and q0377).
- The presenter change is staged on stage, not just announced: a silhouette enters through a hatch in the floor next to a miniature of the diagram (sheet 0016, q0140) and, in the second change, the new presenter appears first on stage next to the reduced diagram (sheet 0028, q0249) and then walking alone on a black background with no audience (q0252).

Visual proportion: almost all 42 sheets record a slide, diagram or product screen, with presenter-only frames functioning as short intervals between these blocks (sheets 0003, 0011 and 0032, for example), and only sheets 0041 and part of 0042 are left with no interface on screen.
Recorded divergences or limits: in sheet 0041 the notes record that the iPhone appears being held and pointed at objects, but without the screen becoming legible enough to describe the interface; in sheets 0025 and 0026 the face confirmation screen is recorded as an app called "Rubii", without the notes determining which app it is.
<!-- /visual:wwdc2019_803 -->

## Designing Great Shortcuts (id: wwdc2019_806, 20.7 min)

Basis: transcript and 16 of 16 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2019/806/.

Central thesis: a good shortcut needs to be chosen with judgment (not every app action deserves to become a shortcut), needs to be discovered discreetly inside the app, and, when it involves voice, needs to be designed as a real conversation with Siri, with dialogue treated with the same care given to the pixels of the visual interface.

The design process Apple describes:
1. List everything the app does and consider which ones make sense to repeat by voice.
2. Evaluate each candidate by three criteria: is it valuable or interesting to repeat; is it feasible by voice without depending on visuals or touch; is it invocable in many contexts (not just within a short window of time).
3. Make the shortcut discoverable inside the app in a discreet way (not on every list item), preferably right after the person repeats an action that has already indicated interest.
4. For shortcuts with interactive Siri, design the conversation as a script first, covering all possible paths, and then consolidate it into a flow diagram with all states and transitions.
5. Write and test the dialogue repeatedly: "When in doubt, test it. Listen to Siri speak your dialog." and evaluate how the text sounds the third and the tenth time it is heard.

Principles stated and why, with the example of the fictional app SoupChef:
- Not every action becomes a shortcut: browsing the menu (very visual, requires scrolling and touch, doesn't change from invocation to invocation) is not a good candidate; checking order status only works within a short window of time; viewing past orders is not something people check often; placing the order itself, however, is valuable and repeatable, so it is a good candidate.
- The Add to Siri button should be used with restraint: putting the button on every item of a main menu "looks ugly" and is not relevant, because the person is probably trying to place the first order, and suggesting to repeat something never ordered before doesn't make sense; better to show it right after the person has already placed an order, when there is a clear signal that they might want to repeat it.
- Invocation phrases should be short: around three words or fewer, limited to a proper noun or verb plus object, to reduce the chance of the person swapping the word order or forgetting terms while trying to remember the phrase.
- Minimize disambiguation prompts by presenting a list of options right away when there is a closed set of options, instead of an open prompt.
- When reading options out loud (AirPods, HomePod, "Hey Siri"), specify pronunciation hints separately from the visual text, and read out loud only what differentiates the options from each other (for example "Beef or Veggie?" instead of repeating "Noodle Soup" for each option).
- Anticipate synonyms for each option, because the person might respond with a natural variation of the question asked (if the question uses a more casual tone, the expected response should also recognize that tone).
- Use the parameter confirmation prompt sparingly, only for cases of real consequence, because it slows down the interaction.
- Use the whole-action confirmation prompt mainly when the action has high consequence; for the "ordering" category in the App Store, the system requires mandatory confirmation from the person.
- Voice dialogue should not include a question that Siri already formulates automatically by category (categories determine the question and the default response status that Siri generates; the customized dialogue is appended at the end).
- Provide clear error messages for automatic reprompting of invalid values, and never present as an option something already known to be invalid at the time of execution.
- When presenting shortcut UI, the entire tappable area opens the app (don't design elements that look individually interactive, because they aren't), and the app should open already filled in with the information provided up to that point.

Rules for writing dialogue (voice as interface):
- Don't be excessively polite or inject too much personality, because the person will hear the same text repeatedly and it becomes irritating.
- Don't include the app's name in the dialogue (the app is already attributed visually by the icon in the confirmation/response UI).
- Don't include the person's name in the dialogue, because Siri might already say their name on the HomePod for identity verification, which sounds repetitive.
- Avoid first-person pronouns ("I"/"we") because Siri is not the one performing the action, the app is; using "I" can make the person think Siri understands the app better than it actually does, leading to follow-up action attempts that don't work. Prefer neutral terms such as "here" or "there are a few options".

Concrete interface-building techniques cited:
- Standard Add to Siri button with customizable corner radius and appearance that changes automatically according to light/dark mode.
- Tapping the Add to Siri button reveals a standard edit/delete sheet for the shortcut, showing the configured phrase.
- The shortcut category selected in Xcode determines Siri's default confirmation question and the default response status.
- Conversation patterns: open prompt, disambiguation prompt, parameter confirmation prompt, final confirmation prompt.

Examples cited and what each one teaches:
- SoupChef (fictional soup-ordering app): illustrates the complete funnel, from prioritizing which action becomes a shortcut to the ordering conversation script (soup type, delivery or pickup, on-site or counter).
- "Hey Siri, bus schedule" via HomePod: shows the hands-free and eyes-free use case, with a spoken response.
- Chained nighttime routine (order soup, play music, show route): example of a multi-step shortcut combining actions from several apps.

Short quotes: no literal quote in quotation marks from a third party appears in the text; the video is the presenter's direct speech (Jay, a designer on the Siri and Shortcuts team) describing guidelines, with no excerpts quoted from another person.

<!-- visual:wwdc2019_806 -->
### What the images show
Basis: 16 of 16 frame sheets viewed, all codes checked.

- The triage of which feature becomes a shortcut is done on screen like an evaluation card: a slide with the feature name in italics and bullets that accumulate next to the corresponding screenshot, with a red X appearing over the device when the feature is discarded (sheet 0003, q0021, q0023 and q0024, with the X entering at q0024), an orange alert icon when the feature only serves a specific context (sheet 0003, q0026) and a positive stamp when the feature is approved (sheet 0004, q0029), closing with the three-criteria slide (sheet 0004, q0030).
- The mistake of putting the button on every item is shown as a pair: the soup list with an "Add to Siri" button repeated on every row, marked with a red X (sheet 0004, q0033, q0034 and q0036; sheet 0005, q0037), against the order status screen with a single button in the footer and a green checkmark stamp (sheet 0005, q0038 and q0041).
- The button has its anatomy shown piece by piece: a dark pill with Siri's colored icon next to the text (sheet 0004, q0032), then four corner-radius variations side by side on a light-background slide (sheet 0005, q0042 and q0044) and, in the next frame, one of those buttons converted to the already-added shortcut state, with the configured phrase and a check icon (sheet 0005, q0045).
- The configuration flow appears in full, screen by screen: a dark modal sheet listing the order items with quantity, name and a blue plus sign (sheet 0006, q0047 and q0049), which gains the suggested phrase in quotation marks below the title at q0049, and then the system form with the phrase field filled in, the action section with the app icon on one line and a full-width blue button in the footer (sheet 0006, q0054; sheet 0007, q0056 and q0060).
- The action editor is shown as a running sentence, with the editable values highlighted in blue within the text (sheet 0008, q0065 and q0067); next to it a second iPhone enters with the disambiguation question (q0066), which evolves into the closed list of four soups (q0068) and then into the confirmation screen with a summary and two buttons (q0070 and q0071).
- The conversation script appears as a physical artifact, not as slide text: a typed sheet of paper with labeled lines alternating between system and person, which turns into two and then three overlapping sheets as more paths are considered (sheet 0009, q0074 to q0076), with the unavailable-option path line highlighted in light blue (sheet 0009, q0078 and q0079).
- Each conversation pattern gets its own label on a slide with a screenshot next to it: disambiguation prompt (sheet 0010, q0083), prompt with options list (q0085 and q0087) and options list without a display (q0088 to q0090). The example card repeats the same structure, app name in small body text at the top, question in bold and the options listed, one of them with a gradient background indicating focus.
- Reading aloud is staged with two devices on the same screen: HomePod with a speech bubble carrying the spoken text, with the option names in different colors inside the bubble, next to the iPhone showing the visual version of the same question (sheet 0010, q0089 and q0090); the same pairing returns on the pronunciation-hint slide, with different text in the bubble (sheet 0011, q0091 and q0092).
- Synonyms appear as layers that grow over the same card: each option gains a second line in italics with the accepted variations, and that line gets longer from one frame to the next (sheet 0011, q0093 to q0095). Then comes the parameter confirmation with a numeric value in large body text and two response buttons (sheet 0011, q0096) and the variation that proposes the usual order (q0097).
- The action confirmation is shown in both registers: the screen with the app header, item line, total and two buttons in the footer (sheet 0012, q0100, q0102 and q0104) and the same moment with the HomePod bubble saying delivery time and price out loud, information that in the visual version only appears implicitly in the summary (sheet 0012, q0105, q0106 and q0108).
- The authorship of the text is marked right on the image: labels pointing to which part of the sentence is written by the developer and which is determined by the category (sheet 0013, q0116) and, in the next frame, the same contrast made through opacity, the system part faded and the customized part in solid white (q0117); before that comes the list of categories with grouped verbs and the ordering option marked with a check (q0114 and q0115).
- Error and context get question screens with the exact text instead of a description (sheet 0014, q0119 and q0120), and the tappable area receives a spec annotation, an arrow with a label pointing to the whole card to say it is a single button, with the camera zooming in until the annotation fills the screen (sheet 0014, q0122, q0123 and q0125).
- The dialogue-writing rules are demonstrated in isolated sentences with a stamp: excessive greeting marked with an X and then repeated in faded copies around it to simulate the effect of hearing that many times (sheet 0015, q0127 and q0128), brand name in the text with an X (q0130), person's name with a label indicating that Siri already adds that on its own (q0132), and the swap of first person for a neutral phrasing going from X to a green check (q0133 to q0135).
- The closing follows the same accumulating-list pattern, with two main bullets in white and a complementary note in gray below, before the cut to the closing screen (sheet 0016, q0136, q0137 and q0139).

Visual proportion: practically every sheet carries a slide, a screen capture or a device mockup, and the frames with only the presenter work as a breather between examples, present in sheets 0001, 0002, 0003, 0005, 0007, 0009 and 0016.
Recorded divergences or limits: the notes observe that the speech mentions the transition from the set of scripts to a flow diagram, but the frames record only the stage of scripts stacked on paper, without that diagram ever appearing.
<!-- /visual:wwdc2019_806 -->

## Building Great Shortcuts (id: wwdc2019_805, 11.9 min)

Basis: transcript and 10 of 10 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2019/805/.

Central thesis: this is primarily an engineering video (Shortcuts API, INIntent, Donation, input/output) presented by an engineer from the Shortcuts team; even so, several implementation decisions carry direct consequences for text design and discoverability that are worth recording.

Process described (from the standpoint of building the feature, with implications for design):
1. Define the action's parameters in the Intent definition file; each parameter has a display name shown until the person fills in a value.
2. Write the "parameter summary", a sentence that describes what the shortcut will do when run.
3. Choose, among the parameters, which one is the "key parameter" (the most identifiable to the person) so that it appears in the system's suggestions.
4. Do "Donation" (INInteraction + Donate) every time the person performs the action in the app, to feed suggestions in the Gallery, Lock Screen and Spotlight Search.
5. Define input and output for each action to allow chaining several actions in a multi-step shortcut.

Principles stated and why:
- The parameter summary should read as a sentence and start with a verb, without repeating the app's name (which already appears at the top of the action, next to the app's icon), so as not to duplicate information already visible.
- Keep the summary short and include only the parameters required for the action to work; the rest stay collapsed under "Show More", editable but not exposed by default, so as not to overload the initial reading.
- Each parameter's display name should always be initial capitalized ("always capitalized"), because it is sometimes displayed as a title in a configuration UI.
- The suggested invocation phrase (suggestedInvocationPhrase) should be short, descriptive of the action and easy to say and remember, because it will be spoken aloud by the person.
- The app should fill the intent with as much information as possible at the moment of donation, so that the shortcut can repeat the action without unnecessary follow-up questions.
- The key parameter should be the most identifiable to the person, not necessarily the technically most relevant one: SoupChef chose the type of soup as the key parameter instead of quantity or side dishes, because that is what the person most associates with the order.
- Include an image for the key parameter when donating; without an image, the app's icon is used instead, which is less specific.
- Actions should produce output (a custom type, with properties) so that other actions can use the result as input automatically, reducing manual selection steps in multi-step shortcuts.

Concrete interface and text-building techniques, with numbers when spoken:
- Add to Siri button: starting with iOS 13, the person can type or dictate the phrase instead of only speaking it, with the app pre-filling suggestedInvocationPhrase.
- The "Do" section of Add to Siri shows a preview of what the shortcut will do; if the intent is configurable, the person can tap to customize values before confirming.
- The Gallery in the Shortcuts app, in the rightmost tab, gained in iOS 13 a section of suggested shortcuts based on the most used apps on the device.
- The shortcuts editor shows categories of built-in actions (media, reminders, scripting such as Loops and If) and a list of suggested actions based on device usage, including third-party apps.
- StickyNote example: a "Find StickyNote" action produces an output type with identifier, name, content and modification date; the next action ("Add Text to Note") declares that type as an input parameter, filling it automatically when chained.

Examples cited and what each one teaches:
- SoupChef (soup order): illustrates the parameter summary varying between "pickup" and "delivery" according to the values filled in by the person, and the choice of key parameter.
- StickyNote (fictional notes app): illustrates how input/output between actions eliminates repeated manual selection when chaining a multi-step shortcut.

Short quotes: no literal third-party quote in quotation marks appears in the text; the speech is entirely the presenter's (Ian, an engineer on the Shortcuts team) describing the API and usage recommendations.

<!-- visual:wwdc2019_805 -->
### What the images show
Basis: 10 of 10 frame sheets viewed, all codes checked.
- The action card in the Shortcuts editor is the visual unit that repeats through almost the whole video, always with the same anatomy: header with the app icon and name in small caps, summary sentence with the parameters underlined in blue and a "Show More" link with an arrow for what is collapsed (sheet 0002, q0013 to q0018).
- A parameter not yet filled in has its own visual treatment, a light gray background with a dotted border around the text, which marks the field as editable and empty without needing an extra label (sheet 0002, close-up from q0013 to q0014).
- The same card template appears in two different fictional apps, Soup Chef and StickyNote, with no variation in structure, meaning the app's identity comes in only through the icon and the name, not through the card's design (sheets 0002 and 0008).
- The link between API and pixel is made through a code caption in a dark monospaced box attached to the element that property produces, first in the "When I say" field and then in the "Do" field of the modal (sheet 0004, q0029 and q0032).
- The green circular "NEW" badge marks points of API novelty over the mockup, both in the modal and in the Gallery's detailed view (sheet 0004, q0029; sheet 0005, q0038).
- Two different code routes appear annotated over the same type of suggestion card in successive frames, INVoiceShortcutCenter.setShortcutSuggestions and then ININteraction with donate, which shows in the image that the same screen element can come from different paths (sheet 0005, from q0041 to q0043).
- The code block grows in layers next to a card that does not change, first just the creation of the intent and the donation, then the INImage lines, and the effect shows which code addition produces the actual photo of the dish inside the suggestion circle (sheet 0007, q0058 to q0060).
- The system suggestion uses an actual photo of the dish in a circular crop, not a generic icon, inside the "Suggestions" card with a gray subtitle about iPhone usage and a "+" button at the end of the row (sheet 0007).
- Emphasis between sibling items is done through opacity: of the three StickyNote cards, the one in focus keeps full color and the other two darken, with no change in size, position or frame (sheet 0008, from q0066 to q0067).
- The concept of the action's output is drawn as a solid blue block labeled "Sticky" with four properties stacked in white, connected to the source card by a simple vertical arrow (sheet 0008, from q0067 to q0068).
- Chaining between actions appears as a state transformation of the parameter: the field goes from a generic placeholder to a blue variable chip with the name "Note", while Xcode alongside shows the "Input Parameter: note" field with a green frame and help text (sheet 0009, from q0079 to q0081 and q0080).
- An interface element that appears only in this sheet, with no equivalent in the previous ones, is the blue "Select a Magic Variable" dropdown overlaid on the action card, listing the available variables (sheet 0009, q0076).
- The slides use a solid black background and hierarchy only through weight and color: the current agenda item in bold white, the other two in light gray, with no icon or position marker (sheet 0001, q0003 to q0009).
- The agenda slide's entrance is animated in perspective, the title appears tilted and then straightens to its final horizontal position, keeping the active item already in bold (sheet 0001, from q0006 to q0007 and from q0007 to q0009).
- The Intent editor in Xcode follows a single palette and structure across every screen shown, dark theme, active item in solid blue in the side list and a form in sections with small caps titles (sheets 0003, 0007, 0008 and 0009); in one of these screens the form itself embeds a preview of the final card (sheet 0003).
- The category grid in the Shortcuts editor differentiates the groups by the icon's shape and color, translucent gray circle for "Apps", orange diamond for "Favorites", black octagon for "Scripting", red diamond for "Media", in two rows of four with a small label below (sheet 0006, from q0052 to q0053).
- At the close, the "Summary" slide reuses exactly the layout of the initial agenda, but leaves "Discoverability" in bold and the other two items in gray, with no visual state indicating the three topics covered (sheet 0010, from q0083 to q0084).
Visual proportion: practically all the sheets show interface, an iPhone mockup, an Xcode window or an annotated slide, and the presenter appears alone only at the opening and in short passages, almost always in a small overlay or next to the enlarged screen.
<!-- /visual:wwdc2019_805 -->

## Great Developer Habits (id: wwdc2019_239, 34.6 min)

Basis: transcript and 26 of 26 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2019/239/.

Scope note: this video does not deal with interface design (layout, typography, color, materials, motion, sound, haptics). It is a talk about engineering habits and the development process (Xcode project organization, version control, comments and documentation, testing, performance analysis, code review, packages and dependencies), presented by a technology evangelist who is also an amateur woodworker and uses woodworking as a recurring analogy. It is included in the group because it is part of the listed ids, but the interface technique sections below are empty or minimal because they do not apply to the video's actual content.

Central thesis: craft in app development means turning careful practices (organization, version control, comments, testing, analysis, code review, modularization, diligence with dependencies) into automatic habits, the same way any practical skill is automated through repetition.

The process/habits Apple describes (this is not a visual design process, it is an engineering process):
- Xcode project organization: use groups that mirror the folder structure on disk (starting with Xcode 9, creating a group also creates a real folder); split large storyboards into multiple files linked by storyboard references, instead of a single giant storyboard; keep the project format updated when Xcode offers the update; use Xcode's new build system, the default since Xcode 10.
- Version control: always enable Git when creating the project (even as a solo developer); small, frequent, localized commits; useful commit messages, written as a note to your "future self"; use branches for bugs and features, then squash back into the main branch.
- Comments and documentation: a good comment explains the "why", not the "what" (well-written code is already self-explanatory about the algorithm); use descriptive variable names instead of single-letter abbreviations; generate a documentation stub in Xcode with Option-Command-Slash (option+command+/) by positioning the cursor on the function's signature.
- Testing: write unit tests as part of regular practice, even for pieces of code that seem too simple to break, and run them before every commit; tests are part of continuous integration.
- Analysis and debugging: use the Network Link Conditioner to simulate typical or poor cellular network conditions; enable Address Sanitizer (memory corruption, buffer overflow), Thread Sanitizer (data races), Undefined Behavior Sanitizer (division by zero, overflow, misaligned pointers) and Main Thread Checker (invalid UIKit/AppKit use outside the main thread); use Debug Gauges (CPU, memory, disk, network) and the Time Profiler in Instruments to find costly pieces of code.
- Code review: understand every line changed, actually compile and run the project (do not assume the person who made the commit already tested it), run the tests, read comments and documentation, check for spelling errors including in variable names; at Apple, no code goes into a project without code review.
- Packages and frameworks: extract shared code (including between the main app and extensions) into frameworks, which reduces the binary's size and allows reuse across apps; thoroughly document any shared package or framework.
- External dependencies: before adding a dependency, understand what it does with user data, whether it collects unnecessary metrics, whether it sends data outside the device, what other dependencies it brings along, and have a plan for the case it breaks, stops being maintained or disappears.

Principles stated and why:
- "Craft is defined as skill in planning, making, and executing": care in the code (not only in the visual) is craft as much as interface design, even though the end customer never directly sees these choices, because they affect performance, reliability and stability.
- Engineering details are rarely seen directly by the customer, but are felt indirectly through performance, reliability and stability.
- Code commented out "just in case" should be removed, not kept, because it already exists in the version control history in case it needs to be recovered.
- Zero-warning practice: never commit code with warnings, treating warnings as errors while writing, because projects that accumulate thousands of warnings stop noticing new, relevant warnings.
- A simple unit test can catch a future regression even when, at the time of writing, there seems to be no risk of breakage (the presenter's personal example with a Struct-to-dictionary serialization round-trip).

Concrete interface-building techniques: not applicable to this video (the content is about engineering process, not about layout, typography, color, materials, motion, sound, haptics, interaction or interface writing). The only mention close to "writing" is about code comments and documentation, not text aimed at the end user.

Examples cited and what each one teaches:
- Carpentry analogy (organized bench vs. messy bench): a disorganized workspace in Xcode costs time the same way a messy workbench costs physical time.
- Struct/dictionary serialization bug in the "DubDub" app: a simple unit test, suggested by a colleague (Marshall), caught a regression introduced weeks later, which would only have shown up later in the UI if it hadn't been caught earlier.
- Code review as a team practice at Apple: no code goes in without review, which standardizes style and increases the whole team's familiarity with the codebase.

Short quotes: no literal third-party quote in quotation marks appears in the text; the speech is entirely the presenter's (Josh, from the Technology Evangelism team), including a reconstructed dialogue with colleague Marshall that is not marked as a direct quote in quotation marks in the transcript text.

<!-- visual:wwdc2019_239 -->
### What the images show
Basis: 26 of 26 frame sheets viewed, all codes checked.
- The screen does not show end-user app interface at any point: the visual material is conceptual slide, metaphor photo, system dialogue and development tool capture, and the only product mockup is an App Store review card at the close (sheet 0026, q0230 and q0231).
- A vertical list of eight words works as a navigation map for the entire talk, with the current item in bold white and the rest in light gray, without numbering or graphic marker (sheet 0003, q0022 to q0025; reappears on sheets 0008, 0010, 0015, 0021, 0023 and 0025).
- At the close, this same list moves item by item, frame by frame, following the recap, without anything else in the composition changing position (sheet 0025, from q0218 to q0225).
- Section summary slides are constructed by build, with lines appearing one per frame instead of appearing together (sheet 0008, from q0064 to q0065; sheet 0013, from q0111 to q0112; sheet 0018, q0157 to q0159; sheet 0022, from q0196 to q0197; sheet 0024, q0212 to q0214).
- The mirroring between project and disk is shown by two symmetrical columns with the same three-file tree, distinguished only by the color of the folder icon, yellow for the Xcode group and blue for the Finder folder (sheet 0004, q0034 to q0036).
- The idea of splitting storyboards is conveyed only through shape and position: vertical rectangles in an app screen format go from a disordered cloud to a regular grid and then to blocks connected by a line, with white cards marking what is active and gray ones the rest (sheet 0005, q0037 to q0042).
- The version history becomes an abstract graph, a central blue line with yellow and green branches of connected circles, without a single text label (sheet 0009, q0078 and q0079).
- The code snippet evolves through three successive states on the same line, weak comment, two-line explanatory comment, and finally the variable renamed from "id" to "cmsApplicationIdentifier", keeping the same string value (sheet 0011, q0095 to q0099).
- A test passing and then failing is narrated by three state icons in sequence, spinner, green diamond with a checkmark and red diamond with an X, without any real test screen (sheet 0014, q0122 to q0126).
- The captures of the Xcode scheme panel show the checkboxes being checked one at a time, in the same order spoken, Address Sanitizer, Thread Sanitizer, Undefined Behavior Sanitizer and then Main Thread Checker in another section (sheet 0016, q0140 to q0143; sheet 0017, from q0145 to q0146).
- The network profile menu appears as a plain text list on a white background, with the chosen item in blue and a selection mark, and the quality scale communicated only by the profile name, without icon or gauge (sheet 0016, q0136 to q0138).
- The diagnostic screens follow high density and their own pattern: the Disk Report opens with numeric cards at the top, red charts and a monospaced table; Instruments uses a sidebar of instruments and a hierarchical table with percentage bars inside the cells (sheet 0017, q0149, q0150 and q0153).
- The section label enters overlaid on the tool capture itself, in the upper left corner, instead of requiring a separate transition slide (sheet 0018, from q0154 to q0155; sheet 0022, from q0193 to q0194).
- Code review steps become three single-sentence slides in the same composition grid, text left-aligned in the middle of the screen, small presenter below on the right and the audience as a dark strip at the bottom (sheet 0020, q0176 to q0180).
- The emphasis before closing a block is done through typographic zoom, the phrase "Have a plan." in three increasing sizes until it fills the screen without the presenter, followed by the section title entering at low opacity (sheet 0024, q0208 to q0211).
- Subject transition is marked by flat color and an isolated symbol, a solid blue screen with no element and then a white speech bubble over the same blue to open the comments topic (sheet 0010, q0088 to q0090; sheet 0011, q0093 and q0094).
Visual proportion: most of the frames are the presenter on stage with a conceptual slide or metaphor photo alongside, with real tool captures concentrated on sheets 0006, 0008, 0012, 0016 to 0018 and 0022, and several stretches where only the presenter appears, with nothing on the screen.
Recorded divergences or limits: the notes mark unreadable text in three places, the extra line at low opacity on the "Track" card (sheet 0009, q0081), the small text below the illustration of the new scenario (sheet 0013) and the text of the review card cut off at the edge of the screen (sheet 0026); the notes also record that, from sheets 0014 to 0026, no side-by-side right-and-wrong comparison, device frame, hand sketch or measurement annotation appears.
<!-- /visual:wwdc2019_239 -->

## What this group reveals about the Apple way

- Machine learning is never treated as a neutral magic resource: in wwdc2019_802 (Pixelmator Photo, HomeCourt) and throughout wwdc2019_803, the recurring argument is that trust only exists when the model's result is visible, editable and explainable (attribution), never a black box.
- Radical simplicity in the interface appears as a value both in pure entertainment games (Thumper, ELOH in wwdc2019_802) and in utility tools (HomeCourt, Butterfly iQ, also in 802), suggesting that "removing obstacles until only the essential remains" is a judgment pattern that crosses very different product categories.
- Voice is treated as a design surface with the same rigor requirements as the visual: both wwdc2019_806 and wwdc2019_803 (confidence and attribution standards) repeat the instruction to never use raw percentages or technical terms with the end user, and wwdc2019_806 details specific rules for writing dialogue (no app name, no first person, test by listening repeatedly).
- Testing design decisions directly with the target audience, and being willing to discard ideas that "seemed right", appears both in a fully human context (Butterfly iQ testing with real doctors in wwdc2019_802) and in an accessibility context (Ordia simulating color blindness on the game itself, also in 802).
- The two Shortcuts videos (wwdc2019_806, design; wwdc2019_805, engineering) show the same idea seen from two angles: not every app feature should become a shortcut, and the decision of which parameter is "most identifiable to the person" (the key parameter, in 805) is, in practice, a design decision applied inside the code.
- wwdc2019_239 is the only video in the group whose declared "care" (craft) is entirely on the inside of the code and the engineering process, not the visible interface; this shows that, for Apple, the notion of craft and attention to detail (a theme also cited in wwdc2019_802, Flow by Moleskine section) explicitly extends from the pixel to the source code.

## No transcript

None of the five files in the group was without a transcript; all of them contained title, source, duration, description and the complete spoken transcript.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_802.md, 194 lines read (file has 193 lines according to wc -l, no final line break; full content, from the header to "[ Applause ]"), read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_803.md, 203 lines read (file has 202 lines according to wc -l, no final line break; full content, from the header to "[ Applause ]"), read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_806.md, 60 lines read (file has 59 lines according to wc -l, no final line break; full content, from the header to "[ Applause ]"), read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_805.md, 66 lines read (file has 65 lines according to wc -l, no final line break; full content, from the header to "[ Applause ]"), read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_239.md, 147 lines read (file has 146 lines according to wc -l, no final line break; full content, from the header to "[ Applause ]"), read to the end: yes.

All five files were read in a single Read call each, with no truncation warning; none needed to be read in parts with offset/limit.
