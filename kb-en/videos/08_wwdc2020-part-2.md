# wwdc2020 (part 2)

## Design for intelligence: Make friends with "The System" (id: wwdc2020_10087, 19.6 min)

Basis: transcript and 17 of 17 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2020/10087/.

Central thesis: for the system's intelligence (Siri Suggestions, widgets, Shortcuts) to speed up people's tasks, the app needs to speak the same language as the system through three concepts of the Intents framework: define, learn and execute.

The design process Apple describes:
- Define: the developer asks what the important and repeatable actions are that people perform in the app, and represents them as "intents", with the relevant attributes defined as parameters of the intent. Example given in the talk: an "order coffee" intent with drink type and size parameters, configured to represent a "large iced latte".
- Learn: every time someone uses the app and performs a task, the app makes a "donation", a record (snapshot) of the executed intent. These donations feed the on-device intelligence, which detects patterns of time and context (for example, when and where the person usually orders coffee) and generates predictions, such as Siri Suggestions on the lock screen.
- Execute: when a prediction hits and the person interacts with it, the reconstructed intent goes back to the app to execute the action. There are two forms of execution: in the background (without switching apps, possibly showing a confirmation UI within the flow itself) or opening the app directly at the relevant part, such as the order confirmation screen.

Principles stated and the why of each:
- On-device privacy: donations never leave the device; the system learns locally. This allows deep personalization without exposing the person's data.
- Reduce friction: the goal of the intelligent experience is to give time back to the person, so the app must be ready to execute an action even when it is not in the foreground or not even open.
- Real goal that the talk makes explicit: "surprise and delight" without the person noticing the calculation behind it.

Concrete interface-building techniques cited in the talk:
- Shortcuts (explained by Mert): ready-made system intents for general action categories (for example, sending a message) and custom intents defined in Xcode for actions exclusive to the app (for example, "order soup"). The "Add to Siri" flow exposes the intent's parameters for the person to edit at the moment of setup (swapping tomato soup for clam chowder, or leaving the field empty so Siri asks every time). Placement recommendation: offer "Add to Siri" in the flows people already use (for example, on the order confirmation screen), never as a newsletter pop-up type interruption. In the Shortcuts app, intents from different apps can be connected by dragging and dropping, passing the output of one intent as the input of another.
- Widgets (explained by Chad): the new iOS 14 widgets are powered by intents, which allows personalization (for example, the "show weather" intent has location as a parameter). Stacks (widget stacks) use the combination of intents and donations to rotate automatically and put the most relevant widget on top at the right moment.
- Siri Event Suggestions: the app must donate the details of a reservation to the system when the person views it; in iOS 14 and macOS Big Sur, this integration also starts happening via web markup in Mail and Safari.

Examples cited (apps, screens, components) and what each example teaches:
- Soup Chef: example app used to illustrate the "order soup", "check delivery time" and "order history" intents; shows how to turn an app action into a voice command via Siri.
- Charty: charting app cited as a consumer of Soup Chef's "order history" intent within a multi-step shortcut, showing the flexibility of chaining intents between different apps in the Shortcuts app.
- Weather widget: example of a widget that rises to the top of a Smart Stack at the right moment, guided by intents and donations.

Short, literal quotes:
- "What happens on your device stays on your device."
- "It's classic 'surprise and delight.'"

<!-- visual:wwdc2020_10087 -->
# wwdc2020_10087: Design for intelligence: Make friends with "The System"

### What the images show
Basis: 17 of 17 frame sheets viewed, all codes checked.

- The session's three concepts become a fixed graphic system of circular icons, each with its own color and symbol (Define in magenta with a pencil, Learn in green with a book, Execute in orange with gears), and the concept in focus appears larger and more saturated while the other two shrink and fade (sheet 0002, q0014 and q0015, after the toolbox labeled with the framework appears alone in q0013). The trio reappears the same way at several points as a navigation anchor (sheet 0003, q0026; sheet 0005, q0044).
- An intent's parameter is drawn as a circle-plus-label pair, and the screen shows the transition from the empty state to the filled one: first a gray circle with just the name, then two circles labeled "Item" and "Size" under the intent's title, then the same circles in green and gold already with the chosen values overlaid (sheet 0003, q0022 to q0024).
- The order screen used as an example shows the complete anatomy of a purchase confirmation: iPhone frame with simulated status bar at 9:41, light beige background, product photo, item line, tip line, total, solid orange primary button and text-only secondary button (sheet 0003, q0021 to q0024). The button hierarchy, filled for the primary action and plain text for the secondary one, is a visual convention that the talk does not put into words.
- The context triggers appear as a list of eleven short phrases in two columns, and the filtering is done through opacity: in the following frame only three phrases remain in full white and all the others turn gray (sheet 0004, q0031 to q0032). The same list then dissolves in a cross transition with the app screen emerging on the right (q0033).
- The most repeated diagram vocabulary is the context card linked by a thin line to an iPhone screen: orange cards with day, time and place connected to the corresponding order, and the content on both sides changes together between frames, from a coffee order on a Monday to a lemonade on a Tuesday (sheet 0004, q0034 to q0036).
- The system's prediction is shown as a lock screen notification, in a light translucent card with the app icon, a bold title and a secondary line describing the suggestion, over a gradient wallpaper (sheet 0005, q0044 and q0045).
- The two ways of executing the action are shown as two screens compared side by side: one iPhone with the "Ready to order?" confirmation card overlaid on the lock screen, with a photo, order summary and a pair of cancel and confirm buttons, and another iPhone with the app's full screen open (sheet 0006, q0047 to q0049). The difference between background execution and opening the app is recorded in the image as a screen difference, not just as a spoken explanation.
- The setup of a shortcut appears as a two-field labeled form, "When I say" and "Do", with an editable value in blue and a solid blue primary button at the bottom; between frames the field's value changes and a secondary options menu with a cancel button appears, showing the exact moment of the parameter edit (sheet 0009, q0073 to q0076).
- The Shortcuts app appears at two levels: a two-column grid of colored cards, four in the grid and a fifth just below, each with an icon and name; and the editor with action blocks stacked vertically, each block marked by the icon of the source app and with the parameters highlighted in blue within the description sentence, plus a circular blue add button at the end of the stack (sheet 0010, q0086 to q0090).
- The transition from the presenter to the interface is made through a recurring editing device: a translucent iPhone silhouette overlays the person's body in the scene before the cut to the screen (sheet 0010, q0085 and q0089; sheet 0012, q0104).
- The widget setup is shown as a form followed by a standard iOS selection list: a card with the location field and the current value gives way to the full list of available cities (sheet 0013, q0115 to q0116). The same sheet shows different widget sizes on the home screen, from the compact one to the larger one that combines two pieces of content on the same line (q0110, q0117).
- The widget stack's rotation is explained with the same card diagram used for coffee, now with predictions by city and time: some cards fade while the ones relevant to the moment remain in full orange, and the result appears as a weather widget switching cities between frames (sheet 0014, q0121 to q0125).
- The donation of a reservation is drawn as an intent card with three stacked fields for time, place and number of people, linked by a dotted line to the generated calendar screen, followed by two screens compared under the labels native app and browser showing the same event produced by both paths (sheet 0015, q0129 to q0132).
- No screen appears as a raw capture: every interface is a mockup in an iPhone frame with a simulated status bar, isolated over a black background when the point is to explain the component, and shown in the context of the lock screen, dock or home screen only when the point is precisely the integration with the system (observation consolidated in the synthesis of the notes).
- The production alternates between four presenters, each in their own location, from the indoor studio with a dark couch to the outdoors with a road, to the area next to a curved glass building and a glazed corridor, and each change of face and setting visually anticipates the change of subtopic (sheets 0006, 0012 and 0015, in the transitions q0051 to q0052, q0102 to q0103 and q0134 to q0135).

Visual proportion: of the seventeen sheets, fifteen alternate between presenter and screen material, counting sheet 0001, which adds the opening title card to the presenter; sheet 0016 is entirely the presenter speaking, with no interface element, and sheet 0017 is just the closing title card.

Recorded divergences or limits: the notes mark partial readings at two points, the parameter circles recorded as gray and without a fully visible name (sheet 0003, q0022) and the text of the "Do" field recorded approximately (sheet 0009, q0073). The identification of the glass building as Apple Park style architecture is an inference flagged as such in the notes (sheet 0012, q0103).
<!-- /visual:wwdc2020_10087 -->

## Design for intelligence: Meet people where they are (id: wwdc2020_10200, 5.9 min)

Basis: transcript and 6 of 6 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2020/10200/.

Central thesis: the system's intelligence can help a person even before they install an app, and keeps accelerating them through every subsequent stage, from discovery to advanced use.

The design process Apple describes: the talk uses a journey narrative (a fictional person who starts training at a gym) to link, in sequence, the system intelligence touchpoints:
1. With no gym app installed, Maps suggests driving directions to the gym's address because it recognized the location mentioned in a message in Messages.
2. At the gym's front desk, an NFC tag offers an App Clip that shows the class schedule grid without needing to download the full app; the App Clip also offers a path to download the full app right there.
3. After installing the app, when pulling the screen down to open Search, the app already appears as a suggestion in Siri Suggestions, because Siri learned and predicted which app the person wants to open based on the phone's usage pattern.
4. Already familiar with the app, the person starts using shortcut suggestions in Search to jump straight to the yoga schedule grid, saving steps.
5. After missing a class by not noticing a schedule change, she creates a Smart Stack of widgets on the Home Screen; the stack rotates automatically to show the most relevant widget at the right time (for example, the gym's widget when the class time changes).
6. Finally, she sets up a Shortcuts automation that triggers on arrival at the gym, showing the bus schedule and starting the workout log.

Principles stated and the why of each:
- The system's intelligence must accompany the person through every stage of usage maturity, from "I never installed the app" to "I automated my routine with it", delivering the right touchpoint for each stage.
- The value of intelligence is not just speed: it is solving a problem the person "didn't even know they had", such as discovering the right app from an everyday context.

Concrete interface-building techniques: App Clip triggered by an NFC tag; Smart Stack of widgets with automatic rotation by relevance and time; Shortcuts automation triggered by arrival at a location (geofencing implicit in the talk, without detailing the API).

Examples cited (apps, screens, components) and what each example teaches: the fictional gym app ("Mission Gym", cited later in video id wwdc2020_10087 by the same group of sessions) illustrates the complete journey; Maps, Messages, App Clip, Search/Siri Suggestions and the Smart Stack of widgets appear as successive entry points, showing that each one solves a different stage of the journey, not redundant stages.

Short, literal quotes:
- "Discovering this app helped her solve a problem she didn't even know she had."

<!-- visual:wwdc2020_10200 -->
# wwdc2020_10200: Design for intelligence: Meet people where they are

### What the images show
Basis: 6 of 6 frame sheets viewed, all codes checked.

- The entire structure of the presentation is fixed by its own graphic: a horizontal timeline with four circles connected by a line and a centered label under each circle, from the pre-download stage to the experienced-user stage, in white on a black background (sheet 0001, q0006). It is a visual device that organizes the narrative and that the talk does not describe in detail.
- The earliest entry point of the journey is shown as a pair of screens in sequence: the conversation in Messages with the address and, right after, the map already with the same address filled in as a suggestion (sheet 0001, q0009 and q0010).
- The anatomy of the suggestion in Maps is visible in the card anchored at the bottom of the screen, with the source app's icon to the left of the address and a secondary gray label identifying that it is a Siri suggestion (sheet 0002, q0010). The image shows the source attribution, a composition detail that the talk summarizes only as a suggestion.
- The search screen appears with full hierarchy: search bar at the top, a grid of suggested app icons in three columns and the keyboard occupying the bottom half (sheet 0003, q0022). The gym app appears among the suggested icons in that grid.
- The shortcut suggestion is shown exactly where it fits on the screen: a rectangular green block with white text and an arrow icon inserted between the icon grid and the keyboard, in frames that otherwise keep the same composition (sheet 0003, q0022 to q0026). The comparison between the two frames shows the before and after of the insertion, and the date shown in the grid also changes between them.
- The notification appears as a green card overlaid on the home screen with a three-level hierarchy, class title and time, description paragraph and an action button in darker green (sheet 0004, q0032). The color, the division of the text and the presence of the embedded button are details that only the image records.
- The swap of generic content for app content is shown as a replacement in the same position on the home screen: first a stack of widgets with weather, calendar and notes, paginated by dots, then a dedicated widget from the gym app listing the next two classes, occupying the width of two icons (sheet 0004, q0033 to q0034).
- The automation card in the Shortcuts app shows the composition of more than one app in a single line: two app icons side by side, transportation and exercise, before the trigger and action text, all inside a light card grouped under a personal section (sheet 0005, q0041).
- A small portrait of the presenter stays anchored in the corner next to practically every screen mockup throughout the video (sheets 0001 to 0004), visually tying each demonstration to the journey of a specific person instead of presenting it as an abstract example.
- The opening and closing use the same composition of stickers on the laptop lid, creating an identical visual frame at the beginning and the end (sheets 0001, 0005 and 0006).

Visual proportion: the screen material is concentrated in sheets 0001, 0003, 0004 and 0005, while sheet 0002 is almost entirely the presenter speaking, with a single interface element, and sheet 0006 is only the closing card.
<!-- /visual:wwdc2020_10200 -->

## Make your app visually accessible (id: wwdc2020_10020, 16.1 min)

Basis: transcript and 17 of 17 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2020/10020/.

Central thesis: visual accessibility goes far beyond VoiceOver; since vision loss is a wide spectrum (full vision, partial vision, low vision, no vision, color blindness, light sensitivity, motion sensitivity), the app needs to combine color with shape, take care of text legibility and respect the display preferences the person has already configured on the system.

The design process Apple describes: the presenter (Drew Haas, engineer on the accessibility team) uses as a live case study his own app under construction, Starstruck (a constellations app), together with an example from the App Store (Sneaky Sasquatch), showing the app before and after turning on each accessibility setting on the device. The explicit process recommendation is to think about visual accessibility from the start of the design, while stressing that it is never too late to revise.

Principles stated and the why of each:
- Never use only color to indicate meaning, because for color-blind people or people with low vision the distinction is lost; the recommended solution is to add shape to color.
- Take care of color contrast because it can be the difference between a visible element and one that blends into the background; general rule given in the talk: colors should get darker in Light Mode and lighter in Dark Mode when contrast is increased.
- Do not truncate text when the font size increases; instead, wrap the line and use the full available width, so that no one loses content.
- Respect, and do not override, the display preferences the person has already turned on (Reduce Motion, Reduced Transparency, Smart Invert Colors, Bold Text, Increase Contrast), even when those effects are part of the app's visual identity.

Concrete interface-building techniques, with exact numbers when spoken:
- SF Symbols: more than 1,500 consistent, configurable symbols, that scale with the size and weight of the text.
- Button Shapes: new iOS 14 API to give buttons an alternative shape when that accessibility setting is on; checked via buttonShapesEnabled in UIAccessibility, with a notification for real-time changes.
- Differentiate Without Color (iOS 13 API): apply to status icons, text with distinctive colors and any element that currently depends only on color to convey meaning.
- Increase Contrast: use system colors, which already adapt automatically; for custom colors, an alternative high-contrast appearance must be provided. In Xcode's Accessibility Inspector, the Color Contrast Calculator was used to measure the contrast between the white symbol and Starstruck's custom purple background: 4.5 to 1 (cited as the minimum ratio generally acceptable for most cases) in the default appearance, rising to 7.5 to 1 in the high-contrast appearance, darkening the background.
- Smart Invert Colors: set accessibilityIgnoresInvertColors on views that should not be inverted, such as photos, videos and app icons.
- Bold Text: checked via isBoldTextEnabled in UIAccessibility; works automatically for apps that use the system's font styles.
- Reduce Motion: checked via isReduceMotionEnabled and observing the change notification; the new iOS 14 API for Prefer Cross-Fade Transitions (prefersCrossFadeTransitions) swaps slide transitions for a subtler crossfade; works automatically for apps that use UIKit's standard UINavigationController.
- Reduced Transparency: blur and vibrancy effects turn into a single solid color; checking is available via UIAccessibility for those who do not use the system's visual effects.
- Layout adjustment for accessibility font sizes: in the Starstruck example, the stack view of the symbol and the label changes from the horizontal axis with centered alignment (default size) to the vertical axis with left alignment (accessibility size), and the label's number of lines is always set to zero to allow unlimited wrapping.

Examples cited (apps, screens, components) and what each example teaches:
- Sneaky Sasquatch (App Store): the "start playing" button uses a system color plus a shape around it, showing how to reinforce with shape what is currently signaled only by color.
- Starstruck (the presenter's personal app, under construction): zodiac icons with distinct color and symbol for color-blind people, optional bold text, decorative background blur and a parallax effect between the foreground stars and the background art; it serves as a complete example of how to apply color with shape, contrast, typography and respect for Reduce Motion and Reduced Transparency in the same app.
- iOS Home Screen: cited as an already-familiar example of the parallax effect, to illustrate why this type of effect can cause motion sickness in people sensitive to motion.

Short, literal quotes:
- "Vision loss is best described as a broad continuum."

<!-- visual:wwdc2020_10020 -->
# wwdc2020_10020: Make your app visually accessible

### What the images show
Basis: 17 of 17 frame sheets viewed, all codes checked.

- The thesis of the vision loss spectrum is demonstrated, not asserted: four columns side by side with the same photograph of a beach and cliff treated with progressive filters, from the sharp image to fully dark, each column with its label (sheet 0001, q0009). In the next frame the no-vision column gains a thin white border framing an empty rectangle, a highlight made only with an outline because there is no content to highlight (sheet 0002, q0010).
- The API announcement cards follow a fixed template repeated for each new feature: large bold title, green circular new badge in the top right corner when the API is new for the year, up to three short recommendation sentences and a monospaced code block with color syntax highlighting right below (sheets 0004 q0036, 0005 q0039, 0009, 0010, 0013, 0015 and 0016). The image carries the exact signature of each API, which the speech only describes by behavior.
- The well-resolved button example appears as a real App Store product screen, with a solid blue pill button as the primary call to action and metadata arranged in three columns with a small icon above each label (sheet 0004, q0028 to q0030 and q0034).
- The recommendation to reinforce meaning with a symbol is supported by two distinct materials: a dense grid of black and white symbols organized in rows by theme, all with the same stroke weight and regular alignment, and a typographic test board on a white background with a reference letter on the left and the same symbol repeated in three increasing sizes per row (sheet 0005, q0042 and q0045). The board is a scale verification method that the speech does not describe in this detail.
- The video's central before and after pair is the example app's signs list: first just names in colored text on a black background, with a navigation chevron on the right, then the same list with a colored circular icon added to the left of each name, keeping the color and adding the shape (sheet 0006, q0050 to q0053).
- The developer tools appear as real screenshots, never as illustrations: the Xcode Asset Catalog with sidebar, central preview and attributes panel on the right evolves from a single variant of the symbol to two stacked variants of normal and high contrast in the same slot (sheet 0008, q0070 to q0072), and then to four variants combining luminosity and contrast level, each with its own shade of purple (sheet 0009, q0081).
- The contrast measurement appears with numbers on screen: a macOS-style calculator window with a text swatch and a background swatch, RGB values below each swatch, a text size control and a large result of 4.5 to 1 accompanied by a yellow triangular warning badge stating which sizes and weights that ratio meets (sheet 0009, q0074 and q0075).
- The system preferences are shown on the real iOS adjustment screens, with the default green toggle on and a text size slider with the small letter at one end and the large one at the other (sheet 0011, q0091 to q0092), and then the root Settings list with the colored square icons for each section (sheet 0014 and, already in a person's hand, sheet 0016, q0142).
- The highlighted sentence about legibility uses hierarchy by weight within the sentence itself: the words that matter in white and bold, the rest of the sentence in regular gray (sheet 0011, q0093).
- The code receives partial highlighting as a teaching device, with a light gray rectangle covering only the section under discussion, and the highlight moves between frames from the standard font block to the accessibility size block (sheet 0012, q0100 to q0103). The phone screen changes along with it: the cell stops having the symbol and name side by side, centered, and starts stacking the symbol above the name, left-aligned, with far fewer items visible per screen.
- The app's detail screen shows another reading pattern: label and value pairs in a column, small gray label above the larger white value, with generous spacing between groups and an uppercase section header (sheet 0012, q0108).
- The motion effect is demonstrated physically: the star map screen appears being held and tilted in a person's hand (sheet 0013, q0114 to q0116). Then a settings panel with green toggles is overlaid on the left of the same screen, showing the setting and the affected app in the same frame (sheet 0014, q0119 to q0120).
- The talk's progress is trackable through a recurring index screen always in the same vertical position, with the active topic in white and the rest in gray (sheets 0002, 0003 q0019, 0010 q0090, 0011 and 0013); at the end of the color and shapes section a summary card also appears with a green circular checkmark badge (sheet 0010, q0086).
- One card in the series breaks its own template: the reduced transparency screen first appears with only text, with no code block, unlike the other cards in the series, and only afterward does the version with code appear (sheet 0015, q0132; sheet 0016, q0137).

Visual proportion: most of the sheets alternate the presenter with on-screen material, and there are three distinct types of material (API cards with code, Xcode tool screenshots and iPhone screens from the example app); sheets 0003 and 0007 are almost only the presenter speaking, with variation only in framing, and sheet 0017 is the closing vignette.

Recorded divergences or limits: the notes flag repeated frames with no perceptible change between them (sheet 0009, q0074 and q0075; sheet 0015, q0128 and q0129) and one step of the code highlight where the highlight stays in the same condition instead of advancing (sheet 0012, q0100 to q0101). The identification of the curved facade as Apple Park is recorded as probable, not confirmed (sheet 0002). The example app appears on screen with the name "Constellations", while the notes treat it as the same fictional app cited in the speech under a different name.
<!-- /visual:wwdc2020_10020 -->

## Design for intelligence: Discover new opportunities (id: wwdc2020_10088, 5.2 min)

Basis: transcript and 5 of 5 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2020/10088/.

Central thesis: system intelligence is a collaboration between the operating system and apps, made possible largely by extensibility, and participating in it opens entry points for the app far beyond the home screen.

The design process Apple describes: JP Lacerda defines intelligence as making Apple products seem to "know" the person (their goals, habits, preferences, interests and relationships) for two effects: "achieve more" (speeding the person to a goal they already have in mind) and "discover more" (enriching the person's life with relevant content, people, places and apps delivered at the right moment). From this definition, the talk goes through the system's main entry points where an app can appear: Shortcuts (voice, Siri Suggestions widget, Search, lock screen, Smart Stack), Sharing Suggestions, Siri Event Suggestions (reservations automatically taken to Calendar), Siri Suggestions in Maps, proactive Do Not Disturb suggestion and flight check-in suggestion on the lock screen. At the end, it guides the developer to choose which entry points make sense for the app's own actions and to think about how to measure that impact.

Principles stated and the why of each:
- Privacy as a fundamental human right: usage analytics are only collected with explicit opt-in and do not identify the person, which allows measuring impact without compromising trust.
- Less tedium (fewer taps and clicks) and less distraction (focus on what matters) are the two effects intelligence must produce to justify each new entry point.

Concrete interface-building techniques, with exact numbers when spoken:
- When someone interacts with an app's Sharing Suggestion for the first time, on average they start sharing twice as much as they shared before through that app; this pattern was observed in several apps that adopted Sharing Suggestions.
- Some airlines reported that 82% of check-ins made from a notification came from the Siri Event Suggestion action.
- Third-party apps are viewed, on average, five times a day across the lock screen, Sharing, Search and other system entry points.

Examples cited (apps, screens, components) and what each example teaches:
- Weather widget rising to the top of a Smart Stack at the right moment, showing the mechanics of automatic prioritization by relevance.
- Siri Event Suggestions automatically taking a restaurant reservation to Calendar, and then notifying on the lock screen when it's time to leave based on traffic, illustrating how a single data donation generates multiple moments of value.
- Do Not Disturb suggestion before watching a movie and flight check-in suggestion on the lock screen, showing entry points that anticipate the person's need without them needing to open any app.

Short, literal quotes:
- "The goal of intelligence is to make your Apple products feel like they know you."

<!-- visual:wwdc2020_10088 -->
# wwdc2020_10088: Design for intelligence: Discover new opportunities

### What the images show
Basis: 5 of 5 frame sheets viewed, all codes checked.

- The key concepts appear as short words overlaid on the presenter's video, in white sans serif and right-aligned, one at a time as the speech progresses (sheet 0001, q0009; sheet 0002, q0010 and q0011). The screen works as an emphasis caption, with no separate slide.
- The concept of multiple entry points gets an abstract diagram before any concrete example: a green bar labeled with an app action, next to the app's label, connected by a thin vertical line to a dark blue bar labeled with the system; in the next frame the single green bar unfolds into three bars of distinct actions, all connected to the same system bar (sheet 0002, q0013 to q0014). It is a more abstract layer of explanation than the speech offers.
- The Shortcuts app screen appears with the same grid of four colored cards used in another video from the same track (sheet 0002, q0017 and q0018), visual evidence of material and examples reused between sessions, not just similar discourse.
- The relationship between setting up and reaping the result is shown as a comparison of two screens side by side: one iPhone with the shortcut configuration screen, with the phrase and action fields, and another with the suggestions already appearing in the system (sheet 0003, q0019 to q0020).
- The sharing menu appears with its standard anatomy, circular avatars of suggested contacts in a row above the row of channel icons, and the same component is shown twice in different contexts, anchored to a photos screen on an iPhone and then to a calendar window on a laptop (sheet 0003, q0022 to q0023). The repetition of the same component on two devices is a point that only the image establishes.
- The suggestion notifications on the lock screen appear in a light translucent card with an icon, bold title and secondary text, including the time shown on screen next to the alert (sheet 0003, q0024).
- The variety of suggestion contexts is resolved by a visual device unique to this video: several lock screens overlapping in a fan, like stacked cards, gaining a new notification with each frame, from traffic to interruption suppression and flight check-in (sheet 0003, q0025 to q0027). It shows the accumulation of cases without needing separate screens.
- The impact data becomes fixed-pattern cards: a large number in bold white, much larger than the supporting text, with a short caption centered below, always over the same blurred photograph of a lake and trees; between frames only the number and the caption change (sheet 0004, q0031 to q0033).
- The closing is a list of three recommendations in right-aligned text overlaid on the presenter's video, each line as an independent item with no bullets (sheet 0004, q0036), keeping the same typographic treatment as the keywords at the start.
- Every app or system screen appears inside a simulated iPhone or laptop frame, never as a standalone capture, even when the content shown is just a menu or a notification (observation consolidated in the synthesis of the notes).
- Opening and closing repeat the same standard track card, with the event wordmark, the closed laptop and the stickers in close-up (sheets 0001 and 0005).

Visual proportion: sheet 0003 is entirely screen material, with the presenter never in frame; sheets 0001, 0002 and 0004 alternate the presenter with overlaid text, diagram and data cards; sheet 0005 shows the presenter in two frames and then the closing card.

Recorded divergences or limits: the notes list frame q0013 in both descriptions of sheet 0002, between the presenter frames and between the diagram frames, recording it as partial.
<!-- /visual:wwdc2020_10088 -->

## Adopt the new look of macOS (id: wwdc2020_10104, 28.7 min)

Basis: transcript and 21 of 21 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2020/10104/. Note: the duration of 2.8 min appears in the file header, but the transcript text is extensive; I report the duration exactly as recorded in the source, without correcting it by inference.

Central thesis: the new look of macOS Big Sur, full-height sidebars, redesigned toolbars and SF Symbols on the Mac, arrives automatically for most apps that compile against the new SDK, but an extra layer of intentional adoption allows going beyond what comes for free.

The design process Apple describes: the session is split by two AppKit engineers into three sequential blocks. John Tegtmeyer covers the window structure (sidebar and toolbar); Jeff Nadeau covers the controls and, finally, the iconography with symbol images. In each block, the explanation pattern is the same: first what the framework already delivers with no code change, then what requires manual adoption for extra gains.

Principles stated and the why of each:
- Let the framework do the heavy lifting whenever possible, because this guarantees visual consistency with the rest of the system at no engineering cost.
- Offer incremental adoption points (full-height sidebar, tracking separators, custom accent color) for those who want to express more personality or give more visual context without rewriting the app's structure.

Concrete interface-building techniques, with exact numbers when spoken:
- Full-height sidebar: obtained using NSSplitViewController with the SplitViewItem configured with sidebar behavior, plus the fullSizeContentView window mask; NSView started exposing safe areas for this, including in Interface Builder.
- Sidebar icon color: NSTintConfiguration with four modes, default (uses the accent color), monochrome (colorless appearance, like in Catalina), preferredColor (a specific color that goes back to following the accent color if it is customized, example given: Mail's folders in teal) and fixedColor (a color that never changes, example given: Mail's VIP folder, always a yellow star).
- Toolbar styles via NSWindow.toolbarStyle: unified (new default, larger controls, bold icons, inline title next to the sidebar), unified compact (more compressed layout, regular-size controls, with optional inline title), preference (aimed at the preferences window, applied automatically when using NSTabViewController with toolbar TabStyle), expanded (title above the toolbar, indicated for long titles or a very populated toolbar) and automatic (default value, keeps the layout of already existing apps).
- Large control size: new large size option available for buttons (including pop-up and pull-down), segmented controls, text fields and search fields; it is the size used by default in all items of the new unified toolbar style and in the system alert buttons.
- Subtitle property in NSWindow: secondary text under the title in the unified style (example given: unread message count in Mail) or next to the title in the expanded style.
- NSSearchToolbarItem: search field collapses into a button when the window is compressed and expands back on click; adoption described in two steps, change the item's class to NSSearchToolbarItem and use the searchField property instead of view; keeps backward compatibility on older systems with no manual version check.
- NSTrackingSeparatorToolbarItem: aligns toolbar items to the dividers of a split view, creating full-height sections that follow the resizing; creating each item takes one line of code, associating the item with a split view and the divider it should follow.
- Automatic shadow between the toolbar and scrolling content (scroll shadow), replaceable by an explicit separator or by no separator via titlebarSeparatorStyle, configurable per split view section or for the window as a whole.
- Sliders: new style with the tick marks positioned inside the track; recommendation to align the adjacent label by the slider's baseline, a technique that also works on Catalina.
- NSTableView.style: four options, automatic (default, chooses based on the table's context), fullWidth (edge-to-edge selection, like in Catalina), inset (new style, with extra horizontal padding on cells, extra vertical padding at the top and bottom, taller row height and more spacing in multicolumn tables) and sourceList (aimed at the appearance of sidebars).
- Typography: text styles arrive on macOS, with sizes and weights centered on the default body size of 13 points; accessed via preferredFont(forTextStyle:) or preferredFontDescriptor(forTextStyle:); the speech stresses that this is not the same as dynamic type, there is no slider that adjusts these sizes system-wide.
- SF Symbols on the Mac: more than 2,500 built-in symbols, plus the option to draw custom symbols. Example with exact numbers: the large icons in the unified toolbar are symbol images configured at a size of 13 points, medium weight, using the large symbol scale. Recommended use via NSImageView (it resolves baseline, display scale and other alignment properties automatically); the speech recommends avoiding using NSImage directly in layer contents, because the image loses sensitivity to context and the result tends to come out blurred.
- Custom accent color: any color can become the app's accent color, defined as a named color in the asset catalog and applied when the system preference is set to "multicolor"; the recommendation is to keep designing with the named system colors (not the custom color directly in code) to respect the person's preference when they choose a different system accent color.

Examples cited (apps, screens, components) and what each example teaches:
- Mail: used as a recurring reference, shows the full-height sidebar with colored icons, the folders in teal with preferredColor, the VIP folder in fixed yellow with fixedColor, the unread count as subtitle under the title, and the toolbar's full-height sections aligned to the split view's dividers via NSTrackingSeparatorToolbarItem.

Short, literal quotes:
- "Your native Mac app will look great on macOS Big Sur out of the box."
- "The idea behind large controls is that sometimes you just need a bigger button."

<!-- visual:wwdc2020_10104 -->
### What the images show
Basis: 21 of 21 frame sheets viewed, all codes checked.

- Measurement annotated directly on the component: two toolbars are shown stacked and compared, each with a number on the left indicating its height, 52 for the unified style and 38 for the compact one, with icons and the move button visibly larger in the first one (sheet 0008, q0065 and q0066). The screen gives the exact value that the speech treats only as "larger controls".
- Yellow label with an arrow pointing to a single icon in the Mail toolbar, with the complete specification of that symbol in text, size in points, weight and scale (sheet 0018, q0155 and q0156). The annotation appears between q0154 and q0155, that is, the slide first shows the icon and only afterward labels it.
- Geometric anatomy of a symbol exposed by two boxes overlaid on the same speech bubble icon, one yellow covering the entire area of the image and another smaller blue one inside it, separating the total rectangle from the alignment rectangle (sheet 0020, q0172). The pair of annotations arrives in two stages, the first one alone in q0171.
- Thin yellow line crossing the entire width of the frame at the height of the label next to the slider, working as a baseline alignment guide between text and control (sheet 0015, q0131). In the previous frames the same slider appears without the guide, with the indicator changing shape from a teardrop to a circle and gaining tick marks on the track (q0129 to q0130).
- Typographic scale presented in two columns, with each style name rendered in the very size and weight it represents, and a second step in which yellow labels add the size in points of each line, from the largest at 26 points down to the captions at 10 points (sheet 0017, q0145 to q0146). The hierarchy is demonstrated by the slide's own design before being stated in numbers.
- Technical slide template repeated through almost the entire video: large fixed title at the top, short list of usage conditions, monospaced code block with colored syntax on one side and a screenshot or mockup on the other (sheets 0003, 0004, 0006 to 0009 and 0013 to 0020). The screen fixes the reading order and shows the literal code that the speech only summarizes.
- Incremental construction within the same slide, instead of a change of composition at every sentence: the code block grows from one to two and then four lines while keeping the same screenshot alongside it (sheet 0003, q0019 to q0021), and the previous topic is dimmed and shifted when the next one enters (sheet 0013, q0109 to q0111).
- Marking of a discouraged practice with a circular red X in the corner of the slide, with no correct-example counterpart alongside it: in the slide about the minimum and maximum size properties of the toolbar item (sheet 0008, q0066 to q0069) and in the code block that assigns the image directly to the layer's content, whose comment on the screen itself warns that the symbol tends to come out blurred or distorted (sheet 0020, q0173 to q0175).
- Side-by-side comparisons as a recurring teaching device: three Mail windows with the same layout and increasing text and icon scales across sidebar sizes (sheet 0018, q0157 and q0158), two sliders with and without tick marks (sheet 0015, q0128) and the two toolbar heights already cited.
- Box diagrams translating a code relationship into a drawing: the hierarchy of a window controller connecting to a split view controller and to two view controllers (sheet 0003, q0026 and q0027), and an outer green rectangle with a lighter inner one and double arrows on all four edges, showing that the scroll view needs to fill the entire item (sheet 0011, q0098).
- Three-column decision table mapping context to table style value, with the situation headers on top and the code value below each one, in quick-reference format (sheet 0016, q0140 and q0141). Two lines of caveats appear only in the following frame (q0141).
- Real tools on screen, not just a mockup: Interface Builder with the hierarchy panel, canvas and the size inspector with the safe area checkbox checked (sheet 0003, q0022 to q0027), the object library with draggable search items (sheet 0010, q0082 to q0084) and the Xcode asset catalog with the accent color square and the compiler options window (sheet 0013, q0112 and q0113).
- Color and materials: horizontal row of accent color circles with uniform spacing (sheet 0012, q0107 and q0108), to which a multicolored circle is added in front of the solid tones to represent the free color option (sheet 0013, q0109). In the Mail sidebar captures, one sheet records colored icons per section, with a yellow star on favorites and folders in teal (sheet 0002, q0017), and another records the items on a dark pinkish background with the selected one in blue (sheet 0004, q0033 and q0036).
- Isolated components on a black background, with no text around them, for anatomy reading: pop-up button with blue fill, slider with blue track before the indicator and gray after it, and segmented control with the active segment in white over dark gray (sheet 0012, q0105 and q0106). In the large controls block the compositions are successive, not simultaneous: first an onboarding mockup with a centered red action button (sheet 0014, q0120 to q0122) and then the panel with the six control types stacked with generous spacing (q0123 and q0124).
- Difference between frames showing the state of the same component: the search field appears collapsed as a magnifying glass icon and then expanded into a text box with a blue focus border (sheet 0009, q0075 to q0077); a highlight rectangle outlines a group of toolbar buttons, a reading that the notes record as a suggestion of the click area of a control with no visible border (sheet 0007, q0062 and q0063), and another outlines the divider between sidebar and list, rising to the top of the window (sheet 0010, q0087 and q0088).

Visual proportion: of the 21 sheets, almost all are slides with code, mockup or screen capture, with the presenter entering in short cuts between blocks; the opening and closing are WWDC brand cards, with stickers, logo and MacBook, and in them the presenter appears in a video window in the corner or in a short cut, not alone in the whole frame (sheets 0001 and 0021). The notes do not record any live demonstration, every app appears as a static capture, almost always the same Mail used as the single case study.

Recorded divergences or limits: the notes mark uncertain readings at three points, the comparison of two versions of the search field is described as "probably before and after" (sheet 0009, q0075 to q0076), the catalog panel that darkens is read as a probable exit transition (sheet 0010, q0083 to q0084), and the balloon icon that opens the symbols section is interpreted as a generic example of a messaging app context (sheet 0019, q0164 to q0165). Several pairs of frames are recorded as having no perceptible change in content (sheets 0002, 0004, 0005, 0010, 0011, 0012 and 0017).
<!-- /visual:wwdc2020_10104 -->

## The winners of the 2020 Apple Design Awards (id: wwdc2020_20022, 2.8 min)

Basis: transcript and 8 of 8 frame sheets viewed, codes checked. Local automatic transcript made with Whisper, not Apple's official one; proper names and terms may have mishearing errors. Source: https://developer.apple.com/videos/play/wwdc2020/20022/.

Central thesis: Apple honors developers every year with the Apple Design Award and, in 2020, unable to do it in person, announced the winners personally, in surprise calls. Developers describe their apps, and the closing remarks deal with doing things with a lot of love, with continuing to learn, and with convincing other people of the value of what is made when it is not yet beautiful.

The design process Apple describes: The talk does not describe a structured design process; the transcript brings short, loose excerpts from the announcement calls. What appears about the making, in the order it is spoken:
1. Fine tuning: a loose excerpt says something like a little less here and a little more here, without indicating what it refers to or who is speaking.
2. Continuous learning: a line says that everyone is still learning and is pursuing an ideal that can never be achieved.
3. Effort: everyone works hard just to make beautiful things come into existence.
4. Initial phase: the thing needs to reach the world, but many other people need to be convinced that it will have value, especially at the start, when it is not yet beautiful, but will become so.

Principles stated and why:
1. Tell a story that is anchored and personal. Why: it is the answer given to the question about what makes Where Cards Fall unique.
2. Evoke the luminous side of humanity, with an abstract game that becomes more understandable over time. It is the stated goal of Sky; the talk gives no reason beyond the goal itself.
3. Have an inclusive cast. Why: so that it would seem inviting to more people. The sentence comes right after the talk about Sky, and the transcript does not indicate who says it or which app it is about.
4. Keep the goal simple: make it extremely easy to write musical notation. This app's name is not said in the talk.
5. Make the photographer forget the tool. Why: in Darkroom, the intent is for the person to forget they are in an app editing photos and think only about the stories they want to tell.
6. Aim for an iconic tool. Shaper 3D wants to create a design tool that will define the future of 3D design; the phrase comes out truncated and repeated in the transcript ("for the next", then "for the next two years"), and the part about two years may belong to the following sentence, so the timeframe is not certain.
7. The winners as a foundation for others. Why: according to the talk after the announcement, they become the ones on whose shoulders other developers can lean to build the next generation of apps.
8. Make with a lot of love. Why: the connection between the maker and the thing made lights up again when people experience it.
9. Put your heart into what you make, transcribed as "boil your heart and sow into something" (uncertain term in the automatic transcript). Why: that way the thing will be exceptional, transcribed as "exception" (uncertain term in the automatic transcript).
10. Keep learning. The same line adds, without linking it as a cause, that everyone pursues an ideal that can never be achieved.
11. Convince other people of the value of what is made, especially at the start. Why: the thing needs to reach the world, and at the start it is not yet beautiful, but will become so.

Concrete interface-building techniques, with exact numbers when spoken: The talk does not bring any interface-building technique or values for layout, typography, color, materials, components or interaction. The only excerpt close to an adjustment is the fragment about a little less here and a little more here, with no object or context.

Examples cited:
1. The award itself: given every year at the conference, transcribed as "wwc" (uncertain term in the automatic transcript); in 2020, unable to be in person, it was done personally by calls.
2. The format of the announcement: the call begins as a conversation about the app with "lauren grim" (uncertain term in the automatic transcript), introduced as an Apple design evangelist; in the middle, someone says they received a message and asks to merge another person into the call; "john galenzi" (uncertain term in the automatic transcript) joins, saying he has already met the developer a few times, and the award is announced. "match", "simon" and "sam" (uncertain terms in the automatic transcript) are also greeted.
3. Where Cards Fall: a very anchored and personal story.
4. Sky: an abstract game about the luminous side of humanity, which becomes more understandable over time.
5. "loom" (uncertain term in the automatic transcript): described as a playful approach to an instrument for creating "drone animation" (uncertain term in the automatic transcript).
6. A musical notation app, unnamed in the talk, whose goal was to make writing sheet music extremely easy.
7. Darkroom: photo editing in which the photographer should forget the app and think about the stories.
8. Shaper 3D: a 3D design tool with the ambition to be iconic and define the future of the field.
9. A winner's reaction: asked how he feels, he says it inspired him to do even more.

Quotes:
1. "we're all in pursuit of an ideal that can never be achieved"

<!-- visual:wwdc2020_20022 -->
### What the images show
Basis: 8 of 8 frame sheets viewed, all codes checked.

- Opening treated as a visual identity card, with stickers, the Apple logo, the year text and a cube with the award's name arranged freely over a gradient background, followed by the campus landscape shown on a MacBook screen and internal shots of the building, curved glass, glazed corridors and work spaces (sheet 0001, q0001 to q0006). Between q0001 and q0002 the graphic elements themselves reposition on the screen.
- The interface that structures the whole video is the video call grid, with a caption in white text in the bottom left corner of each participant indicating city and country (sheets 0001 and 0002, q0007 onward). The locations appear only on screen: Los Angeles, Santa Monica, Tel Aviv, Budapest and London.
- Direct cut between person and product, with no gradual transition, tying each app to the moment it is mentioned: from the call to the isometric game scene (sheet 0002, q0015 to q0016), from that to the game's logo on a black screen (q0016 to q0017), and from that to a painted concept art (q0017 to q0018).
- Character creation process documented in two stages on the same sheet, pencil sketches with technical costume notes written next to the figures, and then the finished, colored illustration with stylized outfits (sheet 0003, q0024 to q0025). It is the only design process sequence visible in the video.
- Typographic identity of each product shown in isolation: a logo in hand-drawn lettering, white on black, for one of the games (sheet 0002, q0017), a translucent cursive wordmark over a three-dimensional setting for another (sheet 0003, q0020), and a minimalist opening screen with a single central graphic element and the start word in spaced-out letters (sheet 0003, q0021).
- Palette and material as a scene argument: an interior lit by golden light coming through a doorway against a dark setting, with the silhouette centered in the opening (sheet 0002, q0016), contrasting with the concept art painted in digital watercolor with a cool palette, blue and turquoise, of a rock formation shaped like hands (q0018).
- Anatomy of an adjustment panel in the photo editing app, a vertical list of labels with horizontal sliders, ten named parameters on screen; the previous frame shows the same app on the gallery screen, with a grid of filter thumbnails next to the photo (sheet 0008, q0064 to q0065). These are two screens in sequence, not a single composition, and the exact names of the controls exist only in the image.
- Anatomy of the sheet music app across three distinct screens: a dark grid library of thumbnails with a side context menu of five actions (sheet 0004, q0030), a notation screen with instrument names aligned to the left of the staff (q0031), and a home screen in panel format, with a personalized greeting by name, a grid of recent documents and five navigation tabs at the top (sheet 0008, q0070).
- Anatomy of three-dimensional modeling across two separate screens: a side tool menu with icon plus text in five items and technical information in the footer, count of selected bodies and volume (sheet 0008, q0069); and, on a tablet, a vertical panel of small icons on the left and a bottom menu with tabs, with the object rendered against a white background (sheet 0005, q0038). The notes do not tie the two screens to the same app through the image, the name comes from the talk.
- The opposite of this in the drawing app, interface almost absent, a full aqua-colored screen with a few icons in the corners and no visible control, leaving the whole frame for the gesture with the pen (sheet 0007, q0058 to q0060). In these three frames the drawn figure evolves from two connected ovals into a larger shape added above and then into a defined figure with a head and a body.
- Bridge between digital design and physical piece shown in three consecutive frames, manipulation of the model on the tablet, a laser cutting machine operating with sparks, and hands holding the resulting white pieces (sheet 0005, q0038 to q0040). The talk deals with the tool's ambition, the image shows the piece coming out of it.
- Recurring framing with hands and a physical device inside the frame, instead of a pure screen capture, used in the three creation apps (sheets 0004, 0005 and 0007).
- Emotional reaction filmed in the call grid itself, someone pointing their phone at the screen as if taking a photo, another with a hand on their face laughing, and the frame changing from two participants to one highlighted and back (sheet 0006, q0047 to q0054). That this is the moment of the award announcement is what the notes record based on the talk, not something written on screen.
- Closing assembled as a quick visual recap of the winners, passing through photo editing, a rhythm game with a neon track and on-screen score, three-dimensional modeling, sheet music and an isometric game scene, ending on the icon of one of the apps isolated against a black background, an organic pink shape on turquoise in flat style with rounded corners (sheet 0008, q0064 to q0072).

Visual proportion: the eight sheets alternate a video call grid with presenters and developers and screenshots of the award-winning apps and games, plus the opening and the campus images; no sheet records a technical slide, code block, annotated measurement or layout diagram.

Recorded divergences or limits: the notes flag uncertain attribution in two sheets, the character sketches are linked to a game cited as unnamed in that sheet (sheet 0003), and the topic transition in sheet 0004 is described as probable, without certainty about which app is on screen. The name of the drawing app appears spelled two ways in the notes, with two o's in sheets 0004 and 0007 and with three o's in the icon read in sheet 0008. Sheet 0003 also describes the person on the call as a presenter and, in the same sentence, as a man wearing glasses, an inconsistency recorded in the notes' own text.
<!-- /visual:wwdc2020_20022 -->

## What this group reveals about the Apple way

- The three "Design for intelligence" sessions (ids wwdc2020_10087, wwdc2020_10200, wwdc2020_10088) cover the same framework, the shared define/learn/execute vocabulary of the Intents framework, from three complementary and deliberately sequenced angles: the developer's opportunity view (10088), the journey of a person using it (10200) and the technical mechanics behind it (10087). None of the three repeats the other's content in depth, each one adds a layer.
- On-device privacy appears as a principle repeated in different contexts, not only as a compliance footnote: in 10087, as a guarantee that donations never leave the device; in 10088, as explicit opt-in and anonymization for any analytics.
- Both in proactive intelligence (10087, 10200, 10088) and in the macOS visual redesign (10104) and in accessibility (10020), the argument pattern is the same: first show what the system already delivers for free (automatic predictions, automatic sidebar, system colors that already respect Increase Contrast), then explain the extra point of manual adoption that takes the app beyond the basics.
- The sessions prefer concrete, named examples over abstract explanations: Soup Chef and Charty (10087), the fictional gym from the narrated journey (10200), Sneaky Sasquatch and Starstruck (10020) and Mail (10104) appear repeatedly as a living case study, including "before and after" demonstrations when a setting is turned on.

## No transcript

- wwdc2020_20022: now has its own card in this file, with the basis indicated on the card.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10087.md: 88 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10200.md: 30 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10020.md: 76 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10088.md: 27 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10104.md: 110 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_20022.md: 4 lines read, to the end: yes (file only has a header, no spoken transcript).
