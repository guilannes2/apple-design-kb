# Foundations (part 2)

## Materials (slug: materials)

What it governs: the visual effects of translucency and depth (Liquid Glass and standard materials) that separate foreground elements, like text and controls, from background elements, like content and solid colors.

Why: by letting the background color come through to the foreground, a material establishes visual hierarchy and helps people keep a sense of place within the interface. Apple distinguishes two functions: Liquid Glass unifies the design language across platforms and allows presenting controls and navigation without obscuring the content below; standard materials help with visual differentiation within the content layer itself.

Do and avoid:
- Use Liquid Glass to form a distinct functional layer of controls and navigation (tab bars, sidebars) that floats above the content layer.
- Do not use Liquid Glass in the content layer; use Standard materials for elements like app backgrounds.
- Exception: transient controls in the content layer, like sliders and toggles, can take on a Liquid Glass appearance when the person activates them.
- Use Liquid Glass effects with restraint; applying the effect to too many custom controls distracts from the content.
- Use the clear variant of Liquid Glass only for components over visually rich backgrounds (photos, videos); the regular variant is the one indicated when the background can hurt legibility, as in alerts, sidebars or popovers with a lot of text.
- When using the clear variant over bright content, consider a dark dimming layer with 35% opacity; it is not necessary if the background is already dark enough or if AVKit's standard media playback controls already provide their own dimming.
- Choose standard materials and effects (UIBlurEffect, UIVibrancyEffect, NSVisualEffectView.BlendingMode) by semantic meaning and recommended use, never by the apparent color they produce, since system settings can change that appearance.
- Use system-defined vibrant colors over materials to ensure legibility in any context.
- Thicker materials (more opaque) give better contrast for text and fine elements; thinner materials (more translucent) help the person retain the context of what is behind them.

Exact specifications: no exact number, measurement or default value was provided in this article, except the 35% opacity recommended for the dimming layer behind components with clear Liquid Glass over a bright background.

Platform differences:
- iOS, iPadOS: besides Liquid Glass, they continue to offer four standard materials in the content layer: ultra-thin, thin, regular (default) and thick. They define vibrant colors for labels, fills and separators specific to each material; labels and fills have several vibrancy levels (label, secondaryLabel, tertiaryLabel, quaternaryLabel for labels; fill, secondaryFill, tertiaryFill for fills), separators have a single level. Avoid quaternary over the thin and ultraThin materials, since the contrast becomes too low.
- macOS: provides several standard materials with designated purposes and vibrant versions of all specifications (NSVisualEffectView.Material). It defines two background blending modes: behind window and within window.
- tvOS: Liquid Glass appears in navigation elements and system experiences like Top Shelf and Control Center; elements like image views and buttons adopt Liquid Glass when they gain focus. It also continues to offer standard materials: ultraThin (for full screens that require a light color scheme), thin (overlays that partially obscure the content and require a light scheme), regular (general overlays) and thick (overlays that require a dark scheme).
- visionOS: windows use by default a system material called glass, which lets light, the current Environment, virtual content and physical objects from the surroundings pass through. There is no distinct dark mode; glass automatically adapts to the luminance of what is behind it. Prefer translucency over opaque colors in windows. For visual separation or to indicate interactivity: thin draws attention to interactive elements like buttons and selected items; regular separates sections of the app, like a sidebar or grouped table; thick creates a dark element that stays distinct over a regular background. It defines three vibrancy values: label (standard text), secondaryLabel (descriptive text like footnotes and subtitles) and tertiaryLabel (inactive elements, only when the text does not need high legibility).
- watchOS: use materials to give context in full-screen modal views, common on this platform; avoid removing or replacing the material backgrounds provided by default in modal sheets.

Links to other articles: Color, Accessibility, Dark Mode.

<!-- visual:materials -->
### What the illustrations show
Basis: 7 of 7 illustration sheets viewed (img 0770 to 0789, several in light and dark versions) and 4 of 4 sheets of the video hig-vid_materials__015 viewed (frames q001 to q037), codes checked.
- The opening draws a capsule over a rounded square from an explicit dotted grid, with vertical, horizontal, radial diagonal lines and a guide circle; the edge of the square under the capsule appears slightly curved, suggesting the optical deformation of the glass over what is behind it. In dark mode the background turns olive gold and the outlines become light, inverting the luminosity without changing the yellow hue (img 0770, light and dark).
- Regular Liquid Glass changes tone depending on the background, without changing shape: over a starry sky the circle becomes semitransparent dark gray, over a beach photo it becomes whitish, and in both cases it blurs the content behind it (img 0771, img 0772).
- The clear variant blurs less than the regular one: inside the circle the brick wall pattern remains recognizable, unlike the stronger blur of the two previous images (img 0773 compared to img 0771 and img 0772).
- Contrast over material is taught with a wrong-and-right pair, in both modes: the share symbol in systemGray3 over the material button nearly blends into the background, followed by a badge with an X (img 0774, img 0775); the same button with the symbol in vibrant color stands out clearly, in light and dark, followed by a badge with a green check (img 0776, img 0777).
- The four standard iOS and iPadOS materials are the same icon over the same colored background in a progression of opacity: ultraThin nearly transparent with little blur, thin more opaque and whitish, regular nearly milky white and thick nearly pure white, leaving only a halo of color at the edges (img 0778 to img 0781, light).
- In dark mode the same series goes from a translucent blue that still shows the shapes behind it to an almost uniform dark tone in thick, with the background gradient disappearing at each level (img 0778 to img 0781, dark).
- On tvOS the page uses a real capture from the Destination Video app: tab bar with the active tab in an opaque white pill and, below, a translucent card with title, description, duration and two buttons, in Liquid Glass, letting the colorful background scene show through blurred (img 0782).
- On visionOS the same living room serves as a comparative pair: a solid blue window totally blocks the environment, and the translucent window lets the furniture and the light behind it show through, blurred (img 0783, img 0784).
- A single visionOS window combines three thicknesses annotated with callout lines: "Thick" in an opaque horizontal bar near the top, "Regular" in the large translucent panel and "Thin" in a pill button in the bottom right corner. In dark mode the contrast between the three drops, but the thick bar remains the most solid (img 0785, light and dark).
- On watchOS the material covers the entire screen of a modal with a translucent X button in the top left corner, time, headphone icon, bold title and description; the "Action" pill button with a purple-to-magenta gradient stands out as its own layer over that material, with high-contrast white text (img 0789).
- In the video, the visionOS Music app window rotates on the vertical axis and returns to facing forward; the glass stays translucent the whole time, the distortion and blur of the background become more visible when the window is tilted more, and the internal content does not change relative position (video, sheet 0001, q001 to q009, with greater tilt in q002 to q004).
- Then the background switches to a desk in softer light (sheet 0002, q010 to q018), the room darkens and the window darkens along with it, becoming grayer and more opaque without the list text losing contrast (sheet 0003, q020 to q028), and finally the scene stabilizes with no oscillation of the material (sheet 0004, q029 to q037).
Recorded divergences: the official description of img 0785 speaks of a left sidebar in regular and a content area on the right, with thin on the button and thick on the text field, but the image shows the three materials in the same wide window, with no clearly separated side column; in the visionOS vibrancy images (img 0786 label, img 0787 secondaryLabel, img 0788 tertiaryLabel) the white symbol looks equally sharp at all three levels, and the difference in contrast could not be distinguished with confidence; the official description of the video does not mention that the background framing changes from the room with the sofa to the desk partway through the recording.
<!-- /visual:materials -->

## Motion (slug: motion)

What it governs: how to use movement and animation intentionally to convey status, give feedback and enrich the visual experience of the app or game, including specific comfort considerations on visionOS.

Why: many system components already include movement automatically and adjust it according to accessibility settings or input method, keeping experiences familiar and consistent. Movement added without purpose distracts people and can make them feel disconnected or physically uncomfortable; not everyone can or wants to experience movement, so it should never be the only channel for communicating important information.

Do and avoid:
- Add movement with purpose; do not add movement for the sake of animation itself.
- Make movement optional; complement visual feedback with alternatives like haptics and audio.
- Aim for realistic feedback that follows people's gestures and expectations; movement that does not make sense is disorienting.
- Prefer brief, precise feedback animations, which tend to feel light and discreet and communicate information more effectively than prominent animation.
- In apps, generally avoid adding movement to UI interactions that occur frequently, since the system already provides subtle animations for standard elements.
- Let people cancel movement; do not force them to wait for an animation to finish before acting, especially if they experience it repeatedly.
- Consider using animated symbols when it makes sense (SF Symbols 5 or later).
- In games, make sure movement works well by default on each supported platform; keeping a consistent frame rate of 30 to 60 fps tends to result in a smooth, visually pleasant experience.
- Let people customize the game's visual experience to optimize performance or battery, for example by switching power modes when the system detects an external power source.

Exact specifications: recommended frame rate in games of 30 to 60 fps. In visionOS, avoid sustained oscillation of objects with a frequency close to 0.2 Hz, to which people are very sensitive.

Platform differences:
- iOS, iPadOS, macOS, tvOS: no additional consideration.
- visionOS: motion can combine with Depth to give essential feedback when people look at interactive elements. Avoid showing motion at the edges of the person's field of view, since this is especially noticeable in peripheral vision and can cause discomfort; if you need to show an object moving in the periphery, keep the brightness similar to the rest of the visible content. When moving large virtual objects, increase translucency or reduce contrast to make the motion less noticeable and help people not feel that they or their surroundings are moving; consider keeping a window's size relatively small. Consider using fades when repositioning an object, if the motion itself doesn't communicate anything useful. In general, avoid letting people rotate an entire virtual world, since this tends to disrupt the sense of stability even when the person controls the rotation; prefer instant directional changes during a quick fade. Consider giving people a stationary reference frame, since it's easier to deal with visual motion contained within an area that doesn't move. Avoid sustained oscillation of objects, especially near 0.2 Hz; if you need to show oscillation, keep the amplitude low and consider making the content translucent.
- watchOS: SwiftUI offers an efficient way to add motion; to animate layout and appearance via WatchKit, or create animated image sequences, use WKInterfaceImage. All layout and appearance based animations automatically include a built-in easing at the start and end of the animation, which cannot be turned off or customized.

Links to other articles: Feedback, Accessibility, Spatial layout, Immersive experiences.

<!-- visual:motion -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed (img 0800, light version), code checked; the page has no video.
- The page opening follows the same construction method as the other HIG section sketches: a shape tinted yellow drawn over a dotted grid with vertical, horizontal, radial diagonal lines and a guide circle (img 0800).
- The motion is suggested by the overlap of repeated diamond shapes offset horizontally: the one on the left in double chevron outline, lighter and hollow, and the one on the right more solid and dark, partially behind the first (img 0800).
- To the left of the shapes, a curved row of small circles of decreasing size works as a trail; together with the overlap of the shapes, it suggests an arc trajectory rather than a purely linear displacement (img 0800).
Recorded divergences: the official description mentions three overlapping diamonds, but in the image only two shapes can be reliably distinguished, and the trail of dots is not mentioned in the description (img 0800).
<!-- /visual:motion -->

## Privacy (slug: privacy)

What it governs: how to request, explain and protect access to people's sensitive data and resources, including permission texts, the location button and stored data protection practices.

Why: people use their devices in a very personal way and expect apps to preserve their privacy; it's natural to distrust a request for personal information or access to a device feature, especially without an obvious need. Transparency about how data is used increases trust, and asking for access only when the feature actually needs it avoids generating distrust.

Do and avoid:
- Request access only to the data the feature actually needs; ask for permissions as specific as possible.
- Be transparent about how the app collects and uses people's data; respect choices made through system features like Hide My Email and Mail Privacy Protection.
- Process data on the device whenever possible, for example using the Apple Neural Engine and custom CreateML models on iOS, avoiding round trips to a remote server.
- Adopt privacy protections defined by the system and follow good security practices, such as using CloudKit for encryption and key management on iOS 15 and later.
- Request permission only when the app clearly needs the access; ideally, wait until the person actually uses the feature that requires the access, for example through the location button.
- Avoid requesting permission at app launch, unless the data or feature is necessary for the app to function.
- Write the purpose string (the justification text) as a brief, complete, direct, specific and easy to understand sentence, in sentence case, without passive voice, ending with a period.
- Correct example of a purpose string: an active sentence that clearly describes how and why the app collects the data. Incorrect examples: a passive sentence with a vague justification, or an imperative sentence with no justification.
- In custom screens or windows that precede the system's standard alert (pre-alert screens), include only one button, making clear that it opens the system alert; use terms like "Continue" or "Next" on the button, never a term like "Allow" that could be confused with the alert's button.
- Don't include additional actions on the custom screen, such as an option to close or cancel without seeing the system alert.
- Never precede the standard tracking alert (app tracking) with a custom screen that confuses or induces the person; offering incentives, displaying a screen that resembles a request, showing an image of the alert or annotating the screen behind the alert are examples of prohibited designs that lead to rejection in App Store review (reference: App Review Guidelines 5.1.1 (iv)).
- Consider using the location button (iOS, iPadOS, watchOS) to give temporary location authorization at the moment the task needs it; the first time the person taps the button, the system shows a standard alert explaining the button's behavior; after that, tapping the button grants one time permission without needing to reconfirm understanding.
- It's possible to customize the location button: system title (for example "Current Location" or "Share My Current Location"), filled or outlined glyph, background color, title and glyph color, and corner radius; it's not possible to customize other visual attributes. It's the developer's responsibility to ensure the text fits without truncating at every accessibility size and translation.
- Avoid relying only on passwords for authentication; prefer passkeys, and if you still use a password, use two factor authentication; use biometric identification (Face ID, Optic ID, Touch ID) to protect access to apps that the person keeps logged in.
- Store sensitive information in a keychain; never store passwords or secure content in plain text files, even with restricted file permissions.
- Avoid inventing custom authentication schemes; prefer system features like passkeys, Sign in with Apple or Password AutoFill.

Exact specifications: no specific number (pt, px, ms, etc.) was provided in this article, besides the reference to clause 5.1.1 (iv) of the App Review Guidelines.

Platform differences:
- iOS, iPadOS, tvOS, watchOS: no additional consideration beyond the general ones.
- macOS: sign the app with a valid Developer ID if distributed outside the store; protect people's data with app sandboxing, required for all apps submitted to the Mac App Store; avoid assuming who is logged in, since fast user switching can have several people active on the same system.
- visionOS: by default, ARKit algorithms handle persistence, world mapping, segmentation, matting and environment lighting, always running and benefiting apps in the Shared Space without sending them data; to access ARKit APIs, the app needs to open a Full Space, and features like Plane Estimation, Scene Reconstruction, Image Anchoring and Hand Tracking require explicit permission. User input is private by design: the system automatically shows hover effects when the person looks at interactive components, without exposing where they are looking before tapping. Camera access works differently: the back camera provides blank input (it's just compatibility convenience), and the front camera only provides input after the person's explicit permission.

Links to other articles: Entering data, Onboarding.

<!-- visual:privacy -->
### What the illustrations show
Basis: 4 of 4 illustration sheets viewed (img 0890 to 0905, all in light version), codes checked; the page has no video.
- The opening draws a raised hand in a stop gesture, in golden brown over a yellow gradient, with a grid of rectangular guides and a concentric circle behind, in the same geometric construction method as the other HIG opening illustrations (img 0890).
- The App Store product page organizes privacy into introductory text with the developer's name and a link to the policy, followed by two stacked white cards, "Data Used to Track You" and "Data Linked to You", each with a title, explanatory subtitle and items in a two column grid with an icon to the left of the text (img 0891).
- The correct and incorrect badges have the same composition and the same size, isolated on a white frame, and vary only in color and symbol: green circle with a white check for correct, light gray circle with a dark gray X for incorrect (img 0892, img 0893).
- The location and photos permission alerts, over the "New Post" screen, follow the same structure of title, explanatory text and three stacked buttons; the location one, with a bold title and light gray background buttons, adds a map preview with a "Precise: On" badge and a central blue pin and orders the buttons as allow once, allow while using and don't allow, and the photos one offers select photos, allow access to all and don't allow (img 0894, img 0895).
- The contacts access alert, over the "Friends" tab with avatars, uses only two buttons side by side, with "Allow" highlighted in blue, different from the stacked buttons of the two previous alerts (img 0896).
- The custom screen that precedes the alert, in the accepted format, is a full screen with a light lilac background in a hexagonal pattern, title, three benefits with icon and text, a note that the option can be changed in Settings and a single "Next" button at the base (img 0897).
- The prohibited versions start from the same screen and add an exit: a second "Cancel" button stacked under the "Next" one (img 0898) or a close X in the top left corner, next to the clock (img 0899).
- The prohibited tracking screens use visual persuasion: a large dollar sign in a purple circle with a "Get $100 Credit" button (img 0900) and a chart of growing purple bars from left to right with an "Allow Tracking" button (img 0901).
- Other prohibited screens reproduce the real system alert inside the custom screen and annotate it: the allow while using button hand circled in purple, with a "Continue" button at the base (img 0902), or a purple arrow rising from an instruction to choose allow (img 0903).
- The location button appears as a solid blue pill with a white location arrow icon followed by the "Current Location" label, with no other element (img 0904).
- In context, over a real map with named streets, the standard location alert keeps the map preview with "Precise: On" and the three stacked buttons seen before (img 0905).
<!-- /visual:privacy -->

## Right to left (slug: right-to-left)

What it governs: how to adapt the interface for right-to-left (RTL) reading languages, such as Arabic and Hebrew, including text alignment, numbers, controls, images and icons.

Why: when someone chooses a language for the device (or just for the app), they expect the interface to adapt in several ways. System UI frameworks already support RTL by default and mirror components automatically; the guidance exists for when layout needs adjusting or specific localizations involving currencies, numerals or mathematical symbols need refining.

Do and avoid:
- Adjust text alignment to match the direction of the interface when the system does not do it automatically (for example, text aligned to the left in LTR should become aligned to the right in RTL).
- Align a paragraph (three or more lines) according to its own language, not the current context; blocks of one or two lines keep following the reading direction of the current context.
- Use consistent alignment for all items in a list, including items displayed in a different script.
- Different RTL languages use distinct numeral systems: Hebrew uses Western Arabic numerals; Arabic can use Western Arabic or Eastern Arabic numerals, varying by country, region and even by area within the same region. Identify the appropriate way to display numbers in each locale the app covers for numeric topics; apps without a number focus can rely on the system's standard representations.
- Do not reverse the order of digits within a specific number (such as "541", a phone number or a card number): the internal order always stays the same, regardless of the language.
- Reverse the order of numerals that show progress or counting direction (such as in progress bars, sliders, ratings), but never reverse the numerals themselves; also reverse a sequence of numerals if it communicates a specific order.
- Mirror controls that show progress from one value to another, such as sliders and progress indicators, and also mirror the positions of glyphs or images that represent start and end; mirror fixed-order navigation controls, such as the back button, which needs to point to the right in RTL, and next/previous buttons.
- Preserve the direction of a control that refers to an actual direction or points to an area of the screen; that control keeps its original direction regardless of the context.
- Visually balance adjacent Latin and RTL scripts when necessary: increasing the RTL font size by about 2 points helps balance Arabic or Hebrew text next to Latin text that is all uppercase, since Arabic and Hebrew have no uppercase.
- Avoid mirroring images such as photographs, illustrations and general artwork, since mirroring an image can change its meaning, and mirroring a copyrighted image can be a violation; consider creating a new version of the image when the content is strongly tied to reading direction.
- Mirror the positions of images when their order is meaningful (chronological, alphabetical, favorites and so on), to preserve the meaning of the order in the RTL context.
- When using SF Symbols for interface icons, you gain variants for the RTL context and localized symbols for Arabic and Hebrew, among other languages; if you create custom symbols, you can specify their directionality.
- Mirror interface icons that represent text or reading direction, for example bars aligned to the left that represent text should become aligned to the right in RTL.
- Consider creating a localized version of an interface icon that displays real text, such as the different versions of the signature, rich-text and I-beam cursor symbols that SF Symbols offers for Latin, Hebrew and Arabic.
- Mirror an interface icon that shows forward or backward movement, since the direction perceived as "forward" depends on the reading direction; for example, the icon of a speaker with sound waves needs to mirror the direction of the waves.
- Do not mirror logos or universal signs and marks (such as the checkmark); displaying a mirrored logo confuses people and can have legal repercussions.
- In general, avoid mirroring interface icons that represent real-world objects, unless the object is used to indicate directionality; most people are right-handed, so mirroring an icon that shows a tool used with the right hand is usually not necessary.
- Before simply mirroring a complex custom icon, consider its individual components and the overall visual balance: some components (such as a badge, diagonal bar or magnifying glass) need to keep the same visual language regardless of localization (for example, the same prohibition diagonal bar in the LTR and RTL versions of SF Symbols); in other cases, a component or its position needs to be mirrored to preserve the meaning and visual balance of the icon.
- If the custom icon includes a component that can imply hand dexterity (such as a tool), consider preserving the orientation of the tool while mirroring the base image, if necessary.

Exact specifications: increase the RTL font size by about 2 points to visually balance with uppercase Latin text.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: Layout, Inclusion, SF Symbols.

<!-- visual:right-to-left -->
### What the illustrations show
Basis: 12 of 12 illustration sheets viewed (img 0933 to 0979, all in light version), codes checked; the page has no video.
- Text alignment is demonstrated with the same card in two versions: in LTR a vertical blue bar marks the guide on the left and the text and the inner bar align to it; in RTL the guide and the alignment move to the right, but the central image icon stays in the same place, without mirroring (img 0934, img 0935).
- Paragraphs in Arabic and Latin appear with a vertical red line marking the reading margin of each: Arabic on the right and Latin on the left in one composition (img 0936) and both aligned to the right in the other (img 0938), with an isolated correct checkmark seal (img 0937) and a wrong seal (img 0939) interspersed in the sequence.
- An RTL list is drawn as five gray bars of varying lengths aligned to a single blue guide on the right (img 0940); in the mixed-alignment version, the second bar shifts to the left with its own blue guide (img 0941).
- The numerals appear in large, simple typography: "123" in Western numerals and then in Eastern Arabic numerals, with a more calligraphic stroke (img 0942, img 0943); in sentences, the number appears with the same internal digit order in Latin, Hebrew and Arabic, at the same size and weight as the text, and in Arabic also in the Eastern-numeral variant (img 0944 to img 0947).
- The star rating shows three full stars, one half star and one empty star, with each numeral centered under its star and the count increasing from left to right (img 0948); in the RTL versions the count order reverses, one with Eastern numerals (img 0949) and the other with Western numerals arranged from 5 to 1 (img 0950).
- The volume slider mirrors entirely: in LTR the speaker without waves is on the left, the one with waves is on the right and the blue track fills from the left to the central control; in RTL the icons swap sides and the fill starts from the right (img 0951, img 0952).
- The balance between scripts is measured with two horizontal red lines, ascender and baseline, over three blue buttons with the download label in uppercase Latin, Arabic and Hebrew at the same size: only the Latin touches both lines (img 0953); with the Arabic and Hebrew font slightly larger, the labels reach the guides better and the visual weight balances out (img 0954).
- In the images section, a simplified globe reappears with the landmasses shifted relative to the first version, which is consistent with the horizontal mirroring mentioned in the official description (img 0955, img 0956); and a card with a title, a grid of four areas with the largest selected in a blue outline and a row of five shapes mirrors the title, the largest area and the order of the shapes (img 0957, img 0958).
- Icons that represent text or direction are fully mirrored: a bulleted list, a book with its spine, a text field with a pencil, a window with corner dots and a toggle with a filled circle swap sides (img 0959, img 0960); the document with lines aligned to the left now has the lines on the right (img 0961, img 0962); the speaker with sound waves now emits to the left (img 0966, img 0967); the muted speaker mirrors with the diagonal bar in the opposite direction (img 0973, img 0974).
- Symbols with real text are localized rather than just mirrored: the signature, the document with a letter and the large letter with an I-beam cursor appear in Latin, Hebrew and Arabic; in the Hebrew version the signature ends on the left with the X on the right, and in the Hebrew and Arabic versions the document's letter moves to the top right corner and the large letter sits to the right of the cursor (img 0963 to img 0965).
- Appearing in a single version, with no mirrored counterpart, are the Apple TV logo, the checkmark, an analog clock with no asymmetric element, a pencil with the tip in the bottom left corner and a game controller (img 0968 to img 0972).
- Composite icons show the treatment per component: the mirrored shopping cart keeps the plus badge in the top right corner (img 0976), and the full RTL variant repositions the badge to the top left corner, following the direction of the cart (img 0975, img 0977); the card with a magnifying glass mirrors, moving the magnifying glass to the left and the card's dot to the opposite corner (img 0978, img 0979).
<!-- /visual:right-to-left -->

## SF Symbols (slug: sf-symbols)

What it governs: the use of the SF Symbols library, thousands of configurable symbols that integrate with San Francisco, including rendering modes, gradients, variable color, weights, scales, design variants, animations and the creation of custom symbols.

Why: symbols automatically align with text at every weight and size because they share the San Francisco typographic foundation, allowing precise weight pairing between the symbol and adjacent text and visual consistency throughout the interface. Symbol and feature availability varies according to the targeted system version; features introduced in a given year are not available on earlier operating systems.

Do and avoid:
- It is forbidden to use SF Symbols, or images confusingly similar to them, in app icons, logos or any other trademark use.
- Choose the rendering mode according to the need: monochrome applies one color to all layers; hierarchical applies one color, varying the opacity by the layer's hierarchical level; palette applies two or more colors, one per layer (if you specify only two colors for a symbol with three levels, the secondary and tertiary layers share the same color); multicolor applies intrinsic colors to reinforce meaning (for example, leaf uses green, trash.slash uses red to signal data loss).
- Confirm that the chosen rendering mode works well in every context; you can use the automatic mode to get a symbol's preferred mode, but it is worth checking the results where a different mode could improve legibility.
- Use colors provided by the system so that symbols automatically adapt to accessibility accommodations and appearance modes such as vibrancy and Dark Mode.
- In SF Symbols 7 and later, use gradient rendering to generate a smooth linear gradient from a single source color; it works at any size, but looks better at larger sizes.
- Use variable color to represent a characteristic that changes over time, such as capacity or intensity, applying color to different layers as the value reaches different thresholds between 0% and 100%; some layers of a symbol can opt out of variable color. Use variable color to communicate change, not to communicate depth; for depth, use hierarchical rendering.
- SF Symbols offers nine symbol weights (from ultralight to black), each corresponding to a San Francisco font weight, and three scales: small, medium (default) and large, defined relative to the cap height of San Francisco.
- Specifying a scale lets you adjust the symbol's emphasis relative to adjacent text without changing the weight pairing with text that uses the same point size.
- SF Symbols defines design variants such as fill, slash and enclosed to communicate states and actions with precision while maintaining visual consistency; outline is the most common variant, with no solid areas, similar to text; most symbols also have a fill variant, with solid areas. Outline works well in toolbars, lists and alongside text; symbols with an enclosing shape (circle, square) improve legibility at small sizes; the fill variant gives more visual emphasis and works well in iOS tab bars and swipe actions, and in places that use the accent color to communicate selection.
- SF Symbols offers specific variants for various languages and writing systems (Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari and several Indic numeral systems), which adapt automatically when the device language changes.
- Apply symbol animations with judgment; there is no limit to how many animations a view can receive, but too many animations overload the interface and distract.
- Use symbol animations to communicate information more efficiently and consider the app's tone when adding them, aligning with brand identity.
- When creating a custom symbol, export the template of a similar symbol and modify it with a vector editing tool; follow the template as a guide, keeping consistency of level of detail, optical weight, alignment, position and perspective with the system symbols; the custom symbol should be simple, recognizable, inclusive and directly related to the action or content it represents.
- Symbols that represent Apple products or features are protected by copyright: they can be displayed, but not customized (the SF Symbols app flags these symbols with an information icon); do not create replicas of Apple products.
- Assign negative side margins to the custom symbol if necessary, to help with optical horizontal alignment when the symbol contains a badge or element that increases its width; use the naming pattern that includes the relevant configuration, such as "left-margin-Regular-M".
- Optimize layers to allow per-layer animation in custom symbols, annotating them in the SF Symbols app; test the animations with all presets, since shapes and paths might not appear as expected in motion.
- Avoid creating custom symbols that include common variants, such as enclosures or badges; use the SF Symbols app's component library to maintain design consistency.
- Provide alternative text (accessibility descriptions) for custom symbols, so that VoiceOver describes the visible UI.

Exact specifications: nine symbol weights (ultralight to black); three scales (small, medium default, large), defined relative to the cap height of the San Francisco font.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: SF Symbols, Typography, Icons, Images, Branding, VoiceOver.

<!-- visual:sf-symbols -->
### What the illustrations show
Basis: 5 of 5 illustration sheets viewed (img 1002 to 1019, all in the light version) and 11 videos watched in full (hig-vid_sf-symbols__042 to __052, 24 sheets total), codes checked.
- The SF Symbols app icon appears with the construction grid overlaid: vertical and horizontal dotted lines and two centered dashed concentric circles, serving as a guide and safe area for the glyph inside the square (img 1002).
- A symbol's layers are isolated by contrast on the same cloud.sun.rain.fill silhouette: primary with the cloud in black and the rest in light gray, secondary with the sun in black, tertiary with the drops in black (img 1003 to img 1005); in hierarchical mode the entire symbol turns blue in three opacities, opaque cloud, medium sun and very light drops (img 1006).
- The rendering modes are compared with the same row of eight utility symbols: monochrome all in solid blue and thin stroke (img 1007); hierarchical with strong blue only on the highlighted element, such as the plus sign, the trash stroke and the "abc", and light blue on the rest (img 1008); palette with part of the row all blue and the rest with blue on the highlight and light gray on the other parts (img 1009); multicolor with the trash in red and a red dotted underline under the "abc", keeping blue or gray on the other elements (img 1010).
- Gradient is taught through a minimal pair: the same sun in flat yellow and with a subtle gradient, brighter on the left and a bit darker on the right (img 1011, img 1012); variable color appears as four states of the speaker side by side, with zero, one, two and three waves filled in blue, while the body stays fixed blue (img 1013).
- Weights and scales are tabulated in a matrix of 27 samples of the same folder-with-plus symbol: nine columns from Ultralight to Black and three rows Small, Medium and Large, with labels above and to the left and subtle variation in stroke thickness and size (img 1014).
- Scale relative to text is measured with two red lines, at cap height and at the baseline, over the plus-in-circle symbol next to the word "Add": in small the circle is smaller than the gap between the guides (img 1015), in medium it slightly exceeds both guides (img 1016) and in large it is noticeably bigger, with the plus sign's vertical stroke nearly touching the guides and the symbol touching the word, without the space seen in the previous two (img 1017).
- Design variants appear in a grid of two rows by five columns: the plain heart, with diagonal bar, in a circle, in a square and in a rectangle, in outline on the top row and in fill on the bottom row (img 1018); localization appears in a grid of eight rows by eleven columns of text symbols, where each row repeats the same eleven symbols swapping only the internal character: Latin, Arabic, Hebrew, Devanagari, a second Devanagari character or Indian numeral, CJK ideograph, hiragana and hangul (img 1019).
- All the videos show three different symbols side by side receiving the same effect; in breathe and rotate they appear in black over a white background, with no color, text or interface around them (videos __051 and __052). In appear the symbols enter staggered, first the antenna, then the photo stack and finally the waveform, from an empty frame at q001 to all three at q005 (video __042, sheet 0001); in disappear they vanish in order, folder, light bulbs and balloons, until the empty frame at q004, and return complete at q005 (video __043, sheet 0001).
- In scale each symbol shrinks and returns to size out of step with the others, with the picture in picture smaller from q002 to q006 and the HomePod smaller at q006, q008 and q009, and all three full again at the final frame q019 (video __045, sheets 0001 to 0003). In pulse only one layer of each symbol alternates between light and dark gray, the AirPlay screen, the pause circle and the rectangle behind the person, out of phase with each other, as at q013 (video __046, sheets 0001 to 0003).
- In animated variable color only one part of each symbol appears dark at a time and the highlight travels along the paths: in Wi-Fi the larger arc at q001 and q004, the smaller one at q002 and q005 and the base dot at q003, q006 and q009, with the same rotation in the speaker's waves and the sprinkler's drops (video __047, sheets 0001 to 0003). In breathe the opacity goes from black to light gray and back in cycles of about 2 seconds, one symbol at a time in rotation: sound wave on sheet 0001, translation balloon from q014 to q024 and ring target from q025 to q036 (video __051, sheets 0001 to 0004).
- Replace swaps the entire symbol at each position, in a staggered way: the grid shrinks at q002 and becomes a list at q003, the rain cloud lightens at q004 and becomes a cloud with sun at q005, the circle with X appears clearly at q006 in place of the microphone, and everything returns to the original at q010 (video __048, sheets 0001 and 0002). Magic Replace adds and removes elements over the same shape: card with alert triangle from q001, diagonal bar on the microphone starting at q003, badge swapped from check to X at q006, triangle removed at q007, bar and X reverted at q012 and original state at q013 (video __049, sheets 0001 and 0002).
- In rotate only one part of each symbol spins while the rest stays fixed: the gear's inner spokes inside the toothed outline, the fan blades over the base and frame, and the two orbit dots around the center and the rings, apparently at different speeds; unlike breathe, all three spin at the same time until the last frame q015 (video __052, sheets 0001 and 0002).
Recorded divergences: the multicolor image reuses the row of eight symbols instead of the green leaf and trash-with-bar examples from the official description, and the eighth symbol is cut off at the edge, with no confirmable color (img 1010); in bounce (video __044, q001 to q015) and in wiggle (video __050, q001 to q009) the frames show no difference in scale, position or rotation, so the described movement is neither confirmed nor contradicted; in breathe the official description mentions growing and shrinking along with the opacity, but only the opacity change is perceptible in the frames (video __051); in animated variable color it was not possible to identify the frame where the cycle reverses (video __047).
<!-- /visual:sf-symbols -->

## Spatial layout (slug: spatial-layout)

What it governs: spatial layout techniques for taking advantage of Apple Vision Pro's infinite canvas, covering field of view, depth and content scale.

Why: people perceive depth and orient themselves in space through visual cues such as distance, occlusion and shadow; the goal of spatial layout is to present content in an engaging and comfortable way, avoiding visual discomfort, a sense of confinement or disorientation.

Do and avoid:
- The system doesn't provide information about the person's actual field of view (it varies according to the Light Seal configuration and each person's peripheral acuity).
- Center important content within the field of view; by default visionOS already launches the app directly in front of the person. In immersive experiences, keep important content centered and avoid showing distracting movement or bright, high-contrast objects in the periphery.
- Avoid anchoring content to the person's head (head-anchored); although the app should generally stay within the field of view, statically anchoring content in front of the person can cause a sense of confinement and discomfort, especially if it obscures too much passthrough. Prefer anchoring content in the person's space, allowing them to look freely around.
- Incorporate small amounts of depth throughout the interface, even in standard windows, to feel more natural, since people can see the content from any angle; SwiftUI already adds visual effects that give this sense of depth in 2D windows.
- For additional depth, use RealityKit to create 3D objects, displayed freely or inside a volume (a component that shows 3D content, similar to a window but with no visible frame).
- Provide visual cues that communicate the content's depth accurately; cues that are missing or conflicting with the real-world experience cause visual discomfort.
- Use depth to communicate hierarchy, since an object that stands out in depth becomes more noticeable; people notice changes in depth, such as when a sheet appears over a window and the window recedes on the z axis.
- In general, avoid adding depth to text, since text that appears to float above the background is hard to read, which slows down reading and can cause visual discomfort.
- Make sure depth adds value: use it to visually separate large, important elements (such as a tab bar or toolbar standing out from a window), but avoid it on small objects, such as a button's symbol, since this can reduce legibility and usability; also review how often depth changes occur in the app, since people need to refocus their eyes at every difference in depth, which is tiring if it happens too often.
- visionOS defines two types of scale: dynamic scale (the system increases a window's scale as it moves away from the person and decreases it as it gets closer, keeping the apparent size constant at any distance) and fixed scale (the object keeps the same scale regardless of proximity, looking smaller when far away, like a physical object).
- To support dynamic scale and the appearance of depth, visionOS defines a point as an angle, unlike other platforms, which define a point as a number of pixels that varies according to a 2D screen's resolution.
- Consider using fixed scale when you want a virtual object to look exactly like a physical object (for example, keeping a product's real scale); prefer applying fixed scale sparingly, reserving it for non-interactive objects, since interactive content needs to scale to keep usability as it moves closer or farther away.
- Avoid displaying too many windows; this can obscure the person's surroundings, causing a sense of overload, confinement and discomfort, as well as making it harder to move the app.
- Prioritize standard indirect gestures, which don't require the person to move their hand into the field of view; direct gestures, which require touching the virtual object with a finger, can be tiring, especially if the object is at the line of sight or above it; reserve direct gestures for nearby objects that invite close inspection or manipulation for short periods.
- The Digital Crown recenters windows in the person's field of view without the app needing to do anything.
- Include enough space around interactive components to make it easy to look at them, since visionOS shows a visual hover effect when the person looks at an element; position multiple regular-sized visionOS components with centers at least 60 points apart, leaving 16 points or more of space between them; don't let controls overlap other interactive elements or views.
- Allow people to use the app with minimal or no physical movement, unless some movement is essential to the experience.
- Use the floor to position a large immersive experience, aligning the horizontal plane with the physical floor, helping content blend intuitively with the surroundings.

Exact specifications: minimum spacing of 60 points between the centers of regular-sized visionOS components, with 16 points or more of space between them.

Platform differences: not supported on iOS, iPadOS, macOS, tvOS or watchOS; all the guidance in this article is exclusive to visionOS.

Links to other articles: Eyes, Layout, Immersive experiences.

<!-- visual:spatial-layout -->
### What the illustrations show
Basis: 1 illustration sheet (img 1096 to 1098) and 8 video sheets from 5 videos (054, 055, 056, 057, 058), all opened and with codes checked.
- The page opening uses a solid yellow background with a grid of dashed lines and two concentric circles under an orange pictogram of three arrows coming out of a central point, suggesting the axes of a three-dimensional space with no label at all (img 1096).
- The field of view is drawn as three concentric orange circles, labeled 30°, 60° and 90°, starting from a point outside the frame to the left, implicitly the person's position, over the render of a living room; the app's translucent window sits almost entirely inside the 60° circle, with its side edges coming close to the 90° one (img 1097).
- In a standard 2D window (Notes on visionOS), with rounded corners, depth is suggested only by a slight elevation with a shadow that separates the window from the blurred background, without shifting layers inside it; a list of folders and notes on the left and the open note on the right in the same panel (img 1098).
- In video 054 (sheet 0001, q001 to q006), in line drawing over a dark background, the person sitting upright with a headset appears alone in q001, a vertical blue panel appears in q002 in positions that vary from frame to frame, and the dotted blue line coming out from eye height only appears in q004, grows in q005 and touches the edge of the panel in q006.
- In video 055 (sheet 0001, q001 to q006), with the person reclined in an armchair with a footrest, the panel is already elevated above and in front of them and tilted toward them from the start; the dotted line appears in q004 and in q006 almost reaches the bottom edge. Compared to 054, what changes with posture is the panel's orientation: vertical for someone upright, tilted for someone reclined.
- In video 056 (sheets 0001 and 0002), a 3D satellite floats in a volume inside a photorealistic room; in q001 it is small and has a "Scene" indicator below it with a dotted progress bar, which disappears in q002; the object grows rapidly until it almost touches the side edges with the solar panels (q004), the viewing angle still changes in q005 and q006, and from q007 to q013 it keeps the large size, with variations mostly in rotation and in the light reflection on the solar panels.
- Dynamic scale, in video 057 (sheets 0001 and 0002): in a light gray test scene with a checkered floor, a rounded white window (circular icon in the top right corner, small bar under the base) gains in q004 a hollow yellow outline marking the original position and size, connected to the floor by a diagonal yellow line; from q005 to q012 the real window moves away from that outline and grows larger, in q013 the label "Dynamic Scale" appears, and in q016 the two shapes merge into one, with a yellow border and the line now vertical.
- Fixed scale, in video 058 (sheets 0001 and 0002): same scene and same window; the yellow reference outline appears in q003 larger than the window, which shrinks each frame while the outline keeps its size until q009; in q010 the label "Fixed Scale" appears, in sheet 0002 the whole set seems to recede in the frame, in q013 the line becomes fully vertical and in q014 the window is tiny and centered inside the outline.
- Videos 057 and 058 follow the same didactic construction: a fixed hollow reference against a filled real object, a yellow line that goes from diagonal to vertical at the end (suggesting that the environment rotates to re-present the scene head-on) and a text caption that only enters in the second half, after the effect has already been shown.
Recorded divergences: in img 1098 the open note does not appear as a separate window positioned to the side, as the official description suggests, but rather on the right side of the same panel. In video 054 the frames captured every 0.5 s do not show the window centered in a stable way, and only q006 brings the complete line; in 055 the line does not visibly touch the panel in any of the six frames. In video 056 the manipulation of the satellite's orientation is not distinguishable as a drag gesture in the static frames, looking like automatic or camera rotation instead, and the "Scene" indicator is not in the official description. The labels "Dynamic Scale" (057) and "Fixed Scale" (058) are also not mentioned in the official descriptions.
<!-- /visual:spatial-layout -->

## Writing (slug: writing)

What it governs: the choices of words, voice, tone and language patterns within the app, covering everything from onboarding to error messages and settings labels.

Why: the words used in the app are an essential part of the user experience; a consistent voice and a tone suited to each context help the app feel cohesive, trustworthy and well designed, besides guiding the person clearly through tasks.

Do and avoid:
- Determine the app's voice by thinking about who you are talking to and the kind of vocabulary familiar to the people who use it; create a list of common terms and use it as a reference to keep the language consistent.
- Adjust the tone according to the situational context, considering what the person is doing both in the physical world and within the app (for example, a direct and serious tone for a detected fall versus a light and congratulatory tone for an activity achievement).
- Be clear: choose easily understandable words, review each word to confirm it is necessary, use fewer words when possible, and read the text aloud when in doubt.
- Write for everyone: use simple and direct language, write with accessibility and localization in mind, avoiding jargon and gendered terminology.
- Consider the purpose of each screen, prioritizing the most important information first; if there is more than one idea, consider splitting the text across multiple screens and think about the flow of information between them.
- Be action oriented: use active voice and clear labels on buttons, almost always with a verb (for example "Send" usually works better than "Let's do it!"); avoid "Click here" in links, preferring descriptive phrases like "Learn more about UX Writing", especially important for people who use screen readers.
- Build consistent language patterns throughout the app, which makes familiarity easier and also makes it easier to write for the app in the future.
- Adopt capitalization rules aligned with the app's style and apply them consistently; title case tends to sound more formal, sentence case more casual; choose one style per type of UI element and keep it (for example, title case for all alerts or sentence case for all headlines).
- Give clear guidance and use consistent language in flows with multiple steps: start with something like "Get Started" to indicate the beginning of the flow, use "Continue" or "Next" (consistently) to move forward, and make it clear when the flow ends with something like "Done".
- Use possessive pronouns sparingly (my, your); for example "Favorites" communicates the same as "Your Favorites" more concisely; if you use them, use them consistently and without switching perspective; avoid using "we" altogether, since it can be ambiguous who the "we" refers to, especially in error messages (prefer "Unable to load content" to "We're having trouble loading this content").
- Write with how people use each device in mind: keep the language consistent across devices, but adjust the text as appropriate; describe gestures correctly on each device (don't say "click" on a touch device like iPhone or iPad, where "tap" is correct).
- iPhone and Apple Watch, having small screens, offer opportunities for personalization but require brevity; TVs tend to be in common spaces, viewed by several people at the same time, and larger screens also require brevity because the text needs to be big enough to be read at a distance.
- Provide clear next steps in empty states, which can also show the app's voice, but the content needs to be useful and suited to the context; guide the person with possible actions, with a button or link when possible; remember that empty states tend to be temporary, so don't show crucial information there that will later disappear.
- Write clear error messages: the ideal is to help avoid the error; when the message is necessary, show it as close as possible to the problem, avoid blaming the person, and be clear about what they can do to fix it (for example, "Choose a password with at least 8 characters" is more useful than "That password is too short"); interjections like "oops!" or "uh-oh" tend to be unnecessary and can sound insincere; if language alone cannot resolve an error affecting many people, use that as an opportunity to rethink the interaction.
- Choose the right delivery method (alert, notification, action sheet, etc.) considering urgency, importance, context and how much supporting information the person needs, with a tone appropriate to the situation.
- Keep settings labels clear and simple, as practical as possible; if the label is not enough, add an explanation describing what happens when it is turned on (the person infers the opposite); if you need to direct someone to a setting, provide a direct link or button instead of trying to describe its location.
- Show hints in text fields: label fields clearly and use hint or placeholder text (such as an example "name@example.com" or a description "Your name"); show errors right next to the field and instruct how to fill it in correctly, instead of reprimanding for not following the rules ("Use only letters for your name" is better than "Don't use numbers or symbols"); avoid robotic error messages with no useful information, like "Invalid name".

Exact specifications: no number, measurement or exact value was provided in this article.

Platform differences: no additional consideration for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: Apple Style Guide, Writing inclusively, Inclusion, Accessibility, Color, Notifications, Alerts, Action sheets, Settings, Text fields, VoiceOver, Localization.

<!-- visual:writing -->
### What the illustrations show
Basis: 1 illustration sheet (img 1338 to 1341) viewed, code checked; the page has no video.
- The opening is monochromatic yellow: a clipboard with rounded corners crossed diagonally by a pencil, overlaid on rectangular grid lines and a central guide circle, in the same grid logic as the openings of other pages (img 1338).
- The serious fall message on Apple Watch is built with a dark blue and purple gradient background, time at the top with an X to close, a short, declarative centered sentence, no emoji, and two stacked buttons: "EMERGENCY SOS", with a red circle on the left, above "I'm OK", in a purple and pink gradient; the emergency action comes before the dismiss action (img 1339).
- The light achievement message uses a colorful activity ring in the top left corner, time and "now" at the top, a short title followed by a sentence with a concrete number (35 days) and an exclamation point, over a blurred colorful background in pink, purple and green (img 1340).
- Compared, the two screens show that tone does not come from words alone: background color, temperature and composition change together, dark and cold with an emergency button in the serious situation, vibrant with an achievement ring in the celebration (img 1339 and img 1340).
- The settings label appears as a card on a black background, short title on the left and a green switch turned on, on the right, with a supporting sentence in light gray below that describes only what happens with the feature turned on, without explaining the off state (img 1341).
<!-- /visual:writing -->

## Typography (slug: typography)

What it governs: the system's typographic choices (sizes, hierarchy, the San Francisco and New York font families, text styles, Dynamic Type) that ensure legibility and express the app's brand, including the complete specification tables for size, leading and tracking by platform.

Why: typographic choices help display legible text, convey information hierarchy, communicate important content and express brand or style. People need to read content at different viewing distances and varied conditions; that's why the system defines recommended standard and minimum sizes by platform, for both custom and system fonts. Text styles form a typographic hierarchy that allows text to scale proportionally when people change the system's text size or turn on accessibility adjustments.

Do and avoid:
- Use font sizes that most people can read easily, following the recommended standard and minimum sizes by platform; if using a custom font with a thin weight, aim for sizes larger than recommended to increase legibility.
- Test legibility in different contexts, including in games, on each supported platform; if the text is hard to read, consider a larger size, more contrast between text and background, or typefaces designed for optimized legibility, such as the system fonts.
- In general, avoid light font weights: when using system fonts, prefer the Regular, Medium, Semibold or Bold weights, and avoid Ultralight, Thin and Light, which can be hard to see, especially in small text.
- Adjust font weight, size and color to emphasize important information and help visualize hierarchy, keeping the relative hierarchy and visual distinction of text elements even when people adjust the text size.
- Minimize the number of typefaces used, even in a heavily customized interface; mixing too many typefaces obscures the information hierarchy and hurts legibility, besides leaving the interface looking inconsistent.
- Prioritize important content when responding to text size changes; not all content is equally important (for example, when increasing text size in a window with tabs, tab titles are not expected to increase as well).
- Apple provides two typographic families: San Francisco (SF), sans serif, with the SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew and SF Mono variants, plus rounded variants of several of them; and New York (NY), serif, designed to work well alone or together with the SF fonts. Both are available in variable font format, which combines different styles in a single file and allows interpolation between styles.
- The system fonts support dynamic optical sizes, merging discrete optical sizes (such as Text and Display) and weights into a single continuous design, which removes the need to choose a discrete optical size, except when using a design tool that doesn't support all the features of the variable font format.
- Text styles define a combination of font weight, point size and leading values for each text size (for example, body prioritizes comfortable reading across multiple lines; headline uses a size and weight that distinguish a title from the surrounding content); consider using the native text styles for consistency and for automatic Dynamic Type support.
- It's possible to modify the native text styles using symbolic traits defined by the system APIs, such as the bold trait, which adds weight to the text creating another level of hierarchy, or leading adjustments (loose leading, more space between lines, helps in wide columns or long passages; tight leading, less space, helps fit text in height-constrained areas, such as a list row); avoid tight leading when the text has three or more lines, even in height-limited areas.
- Use the constants defined in Font.Design to access the system fonts; don't embed system fonts in the app or game.
- When producing a faithful interface mockup that uses the system's variable fonts, it may be necessary to adjust the tracking, since in a running app the system adjusts tracking dynamically at each point size.
- When using a custom font, ensure legibility by following the recommended minimum sizes by style and weight; implement the same accessibility behaviors that the system fonts already support automatically (Dynamic Type where available, response to features like Bold Text); in Unity-based games, it's possible to use Apple's plug-ins for Unity to support Dynamic Type, or, if the plug-in isn't appropriate, allow text size adjustment by other means.
- Dynamic Type is a system-level feature (iOS, iPadOS, tvOS, visionOS, watchOS) that lets people adjust the size of the text visible on the device for legibility and comfort.
- Make sure the app's layout adapts to all font sizes; check that the design scales and that text and glyphs remain legible at all sizes, including the larger accessibility sizes (testable at Settings > Accessibility > Display & Text Size > Larger Text).
- Increase the size of meaningful interface icons as the font size increases; when using SF Symbols, the icons already scale automatically with Dynamic Type size changes.
- Keep text truncation to a minimum as the font size increases; in general, aim to display as much useful text at the largest accessibility size as at the largest standard size; avoid truncating text in scrollable regions, unless the person can open a separate view to read the rest.
- Consider adjusting the layout at large font sizes: in horizontally constrained contexts, inline items (such as glyphs and timestamps) and container limits can squeeze the text and cause truncation or overlap; consider a stacked layout, with text above secondary items; multi-column text can also become less legible at large sizes due to horizontal space constraints, so reduce the number of columns as the font size increases.
- Keep a consistent information hierarchy regardless of the current font size, keeping primary elements at the top of the view even with very large fonts.

Exact specifications:

Standard and minimum font sizes by platform: iOS/iPadOS standard 17 pt, minimum 11 pt; macOS standard 13 pt, minimum 10 pt; tvOS standard 29 pt, minimum 23 pt; visionOS standard 17 pt, minimum 12 pt; watchOS standard 16 pt, minimum 12 pt.

Emphasized weights (symbolic traits) can be medium, semibold, bold or heavy depending on the text style.

iOS/iPadOS Dynamic Type tables (style, weight, size in points, leading in points, emphasized weight), by category size:
- xSmall: Large Title 31/38 Bold; Title 1 25/31 Bold; Title 2 19/24 Bold; Title 3 17/22 Semibold; Headline (Semibold) 14/19 Semibold; Body 14/19 Semibold; Callout 13/18 Semibold; Subhead 12/16 Semibold; Footnote 12/16 Semibold; Caption 1 11/13 Semibold; Caption 2 11/13 Semibold.
- Small: Large Title 32/39 Bold; Title 1 26/32 Bold; Title 2 20/25 Bold; Title 3 18/23 Semibold; Headline 15/20 Semibold; Body 15/20 Semibold; Callout 14/19 Semibold; Subhead 13/18 Semibold; Footnote 12/16 Semibold; Caption 1 11/13 Semibold; Caption 2 11/13 Semibold.
- Medium: Large Title 33/40 Bold; Title 1 27/33 Bold; Title 2 21/26 Bold; Title 3 19/24 Semibold; Headline 16/21 Semibold; Body 16/21 Semibold; Callout 15/20 Semibold; Subhead 14/19 Semibold; Footnote 12/16 Semibold; Caption 1 11/13 Semibold; Caption 2 11/13 Semibold.
- Large (default): Large Title 34/41 Bold; Title 1 28/34 Bold; Title 2 22/28 Bold; Title 3 20/25 Semibold; Headline 17/22 Semibold; Body 17/22 Semibold; Callout 16/21 Semibold; Subhead 15/20 Semibold; Footnote 13/18 Semibold; Caption 1 12/16 Semibold; Caption 2 11/13 Semibold.
- xLarge: Large Title 36/43 Bold; Title 1 30/37 Bold; Title 2 24/30 Bold; Title 3 22/28 Semibold; Headline 19/24 Semibold; Body 19/24 Semibold; Callout 18/23 Semibold; Subhead 17/22 Semibold; Footnote 15/20 Semibold; Caption 1 14/19 Semibold; Caption 2 13/18 Semibold.
- xxLarge: Large Title 38/46 Bold; Title 1 32/39 Bold; Title 2 26/32 Bold; Title 3 24/30 Semibold; Headline 21/26 Semibold; Body 21/26 Semibold; Callout 20/25 Semibold; Subhead 19/24 Semibold; Footnote 17/22 Semibold; Caption 1 16/21 Semibold; Caption 2 15/20 Semibold.
- xxxLarge: Large Title 40/48 Bold; Title 1 34/41 Bold; Title 2 28/34 Bold; Title 3 26/32 Semibold; Headline 23/29 Semibold; Body 23/29 Semibold; Callout 22/28 Semibold; Subhead 21/28 Semibold; Footnote 19/24 Semibold; Caption 1 18/23 Semibold; Caption 2 17/22 Semibold.
Point size basis: image resolution of 144 ppi for @2x and 216 ppi for @3x.

Larger accessibility sizes iOS/iPadOS (AX1 to AX5), same format:
- AX1: Large Title 44/52 Bold; Title 1 38/46 Bold; Title 2 34/41 Bold; Title 3 31/38 Semibold; Headline 28/34 Semibold; Body 28/34 Semibold; Callout 26/32 Semibold; Subhead 25/31 Semibold; Footnote 23/29 Semibold; Caption 1 22/28 Semibold; Caption 2 20/25 Semibold.
- AX2: Large Title 48/57 Bold; Title 1 43/51 Bold; Title 2 39/47 Bold; Title 3 37/44 Semibold; Headline 33/40 Semibold; Body 33/40 Semibold; Callout 32/39 Semibold; Subhead 30/37 Semibold; Footnote 27/33 Semibold; Caption 1 26/32 Semibold; Caption 2 24/30 Semibold.
- AX3: Large Title 52/61 Bold; Title 1 48/57 Bold; Title 2 44/52 Bold; Title 3 43/51 Semibold; Headline 40/48 Semibold; Body 40/48 Semibold; Callout 38/46 Semibold; Subhead 36/43 Semibold; Footnote 33/40 Semibold; Caption 1 32/39 Semibold; Caption 2 29/35 Semibold.
- AX4: Large Title 56/66 Bold; Title 1 53/62 Bold; Title 2 50/59 Bold; Title 3 49/58 Semibold; Headline 47/56 Semibold; Body 47/56 Semibold; Callout 44/52 Semibold; Subhead 42/50 Semibold; Footnote 38/46 Semibold; Caption 1 37/44 Semibold; Caption 2 34/41 Semibold.
- AX5: Large Title 60/70 Bold; Title 1 58/68 Bold; Title 2 56/66 Bold; Title 3 55/65 Semibold; Headline 53/62 Semibold; Body 53/62 Semibold; Callout 51/60 Semibold; Subhead 49/58 Semibold; Footnote 44/52 Semibold; Caption 1 43/51 Semibold; Caption 2 40/48 Semibold.

macOS text styles (weight, size in points, line height in points, emphasized weight), base 144 ppi @2x: Large Title Regular 26/32 Bold; Title 1 Regular 22/26 Bold; Title 2 Regular 17/22 Bold; Title 3 Regular 15/20 Semibold; Headline Bold 13/16 Heavy; Body Regular 13/16 Semibold; Callout Regular 12/15 Semibold; Subheadline Regular 11/14 Semibold; Footnote Regular 10/13 Semibold; Caption 1 Regular 10/13 Medium; Caption 2 Medium 10/13 Semibold.

tvOS text styles (weight, size, leading, emphasized), base 72 ppi @1x and 144 ppi @2x: Title 1 Medium 76/96 Bold; Title 2 Medium 57/66 Bold; Title 3 Medium 48/56 Bold; Headline Medium 38/46 Bold; Subtitle 1 Regular 38/46 Medium; Callout Medium 31/38 Bold; Body Medium 29/36 Bold; Caption 1 Medium 25/32 Bold; Caption 2 Medium 23/30 Bold.

Dynamic Type watchOS (weight, size, leading, emphasized), by watch face size:
- xSmall: Large Title 30/32.5 Bold; Title 1 28/30.5 Semibold; Title 2 24/26.5 Semibold; Title 3 17/19.5 Semibold; Headline 14/16.5 Semibold; Body 14/16.5 Semibold; Caption 1 13/15.5 Semibold; Caption 2 12/14.5 Semibold; Footnote 1 11/13.5 Semibold; Footnote 2 10/12.5 Semibold.
- Small (default 38mm): Large Title 32/34.5 Bold; Title 1 30/32.5 Semibold; Title 2 26/28.5 Semibold; Title 3 18/20.5 Semibold; Headline 15/17.5 Semibold; Body 15/17.5 Semibold; Caption 1 14/16.5 Semibold; Caption 2 13/15.5 Semibold; Footnote 1 12/14.5 Semibold; Footnote 2 11/13.5 Semibold.
- Large (default 40mm/41mm/42mm): Large Title 36/38.5 Bold; Title 1 34/36.5 Semibold; Title 2 28/30.5 Semibold; Title 3 19/21.5 Semibold; Headline 16/18.5 Semibold; Body 16/18.5 Semibold; Caption 1 15/17.5 Semibold; Caption 2 14/16.5 Semibold; Footnote 1 13/15.5 Semibold; Footnote 2 12/14.5 Semibold.
- xLarge (default 44mm/45mm/49mm): Large Title 40/42.5 Bold; Title 1 38/40.5 Semibold; Title 2 30/32.5 Semibold; Title 3 20/22.5 Semibold; Headline 17/19.5 Semibold; Body 17/19.5 Semibold; Caption 1 16/18.5 Semibold; Caption 2 15/17.5 Semibold; Footnote 1 14/16.5 Semibold; Footnote 2 13/15.5 Semibold.
- xxLarge: Large Title 41/43.5 Bold; Title 1 39/41.5 Semibold; Title 2 31/33.5 Semibold; Title 3 21/23.5 Semibold; Headline 18/20.5 Semibold; Body 18/20.5 Semibold; Caption 1 17/19.5 Semibold; Caption 2 16/18.5 Semibold; Footnote 1 15/17.5 Semibold; Footnote 2 14/16.5 Semibold.
- xxxLarge: Large Title 42/44.5 Bold; Title 1 40/42.5 Semibold; Title 2 32/34.5 Semibold; Title 3 22/24.5 Semibold; Headline 19/21.5 Semibold; Body 19/21.5 Semibold; Caption 1 18/20.5 Semibold; Caption 2 17/19.5 Semibold; Footnote 1 16/18.5 Semibold; Footnote 2 15/17.5 Semibold.

Larger accessibility sizes watchOS (AX1 to AX3):
- AX1: Large Title 44/46.5 Bold; Title 1 42/44.5 Semibold; Title 2 34/41 Semibold; Title 3 24/26.5 Semibold; Headline 21/23.5 Semibold; Body 21/23.5 Semibold; Caption 1 18/20.5 Semibold; Caption 2 17/19.5 Semibold; Footnote 1 16/18.5 Semibold; Footnote 2 15/17.5 Semibold.
- AX2: Large Title 45/47.5 Bold; Title 1 43/46 Semibold; Title 2 35/37.5 Semibold; Title 3 25/27.5 Semibold; Headline 22/24.5 Semibold; Body 22/24.5 Semibold; Caption 1 19/21.5 Semibold; Caption 2 18/20.5 Semibold; Footnote 1 17/19.5 Semibold; Footnote 2 16/17.5 Semibold.
- AX3: Large Title 46/48.5 Bold; Title 1 44/47 Semibold; Title 2 36/38.5 Semibold; Title 3 26/28.5 Semibold; Headline 23/25.5 Semibold; Body 23/25.5 Semibold; Caption 1 20/22.5 Semibold; Caption 2 19/21.5 Semibold; Footnote 1 18/20.5 Semibold; Footnote 2 17/19.5 Semibold.

Tracking tables (values in 1/1000 em and in points, by point size from 6 to 96 or more) were provided in full in the original text for: SF Pro (iOS, iPadOS, visionOS), SF Pro Rounded, New York (ranging from 6 to 260 pt), macOS (identical to the SF Pro table), tvOS (identical to the SF Pro table), SF Compact (watchOS) and SF Compact Rounded (watchOS). As an example of range: in SF Pro, tracking varies from +41 (1/1000 em, +0.24 pt) at 6 pt to 0 at sizes of 80 pt or more; in New York, tracking reaches -18 (1/1000 em, -4.57 pt) at 260 pt. The complete values, size by size, are in the original source and were not reproduced line by line here because they are extensive technical reference tables; any implementation that needs the exact tracking value for a specific point size should consult the original source or the text file already downloaded.

Platform differences:
- iOS, iPadOS: SF Pro is the system font; apps can also use NY.
- macOS: SF Pro is the system font; NY is available for Mac apps built with Mac Catalyst; macOS does not support Dynamic Type. When needed, use the dynamic system font variants to match the text of standard controls: Control content (controlContentFont(ofSize:)), Label (labelFont(ofSize:)), Menu (menuFont(ofSize:)), Menu bar (menuBarFont(ofSize:)), Message (messageFont(ofSize:)), Palette (paletteFont(ofSize:)), Title (titleBarFont(ofSize:)), Tool tips (toolTipsFont(ofSize:)), Document text/user (userFont(ofSize:)), Monospaced document text/user fixed pitch (userFixedPitchFont(ofSize:)), Bold system font (boldSystemFont(ofSize:)), System font (systemFont(ofSize:)).
- tvOS: SF Pro is the system font; apps can also use NY.
- visionOS: SF Pro is the system font; when using NY, you need to specify the desired type styles. visionOS uses bolder versions of the Dynamic Type body and title styles, and introduces Extra Large Title 1 and Extra Large Title 2 for wide editorial layouts. In general, prefer 2D text: the more visual depth the characters have, the harder it is to read; a bit of 3D text can be fun, but for content that people need to read and understand, prefer text with little or no visual depth. Test text legibility at different scales. Maximize the contrast between text and the container background; by default the system displays text in white, since it usually contrasts well with the default background material. If displaying text with no background, consider making it bold to improve legibility, avoiding shadows to increase contrast, since the current space may not have a visual surface to project a shadow onto accurately. Keep text facing the person whenever possible (billboarding), making the text baseline stay perpendicular to the person's line of sight as they move.
- watchOS: SF Compact is the system font; apps can also use NY; in complications, watchOS uses SF Compact Rounded.

Links to other articles: SF Symbols, Accessibility, Supporting Dynamic Type (internal section referenced as a related article), visionOS, Text input and output.

<!-- visual:typography -->
### What the illustrations show
Basis: 4 illustration sheets (img 1192 to 1204) viewed, codes checked; the page has no video.
- The opening expresses hierarchy through typography: a small lowercase "a" next to a large uppercase "A", in dark brown over mustard yellow that covers the whole image, with a rectangular grid, a large circle centered on the bigger letter and dashed lines marking alignments and proportions between the two (img 1192).
- Legibility at stake is taught by a before-and-after pair with the same scene, angle and palette on iPhone in landscape: first the plant names appear small and with no background over a lilac and pink gradient; then they get bigger, inside capsules with a translucent gray background, and the "Plants Recorded 0/3" card also gets larger text (img 1193 and img 1194).
- The two system families are compared with the same pangram and with two horizontal blue guide lines marking cap height and baseline: SF Pro in black over white (img 1195) and New York, serif (img 1196).
- The weight scale is a pure typographic grid, with no interface: the word "Text" repeated on two lines (Upright and Italics) across nine weight columns, from Ultralight to Black, with the italic right below each weight (img 1197).
- The hierarchy of text styles on a real screen is shown with a screenshot of Mail on iPhone annotated with external labels and straight lines: Large title points to "Inbox", Title to the sender's name, Subtitle to the subject and Body text to the excerpt from the email body (img 1198).
- Dynamic Type appears as the same Mail message at two extremes. At the default size, avatar on the left, name and date on one line, recipient and clip on the line below, subject in bold and body with four lines (img 1199). At the largest accessibility size, the name breaks into two lines, recipient and date go on separate lines, the subject takes up two large lines, the body is cut off right at the start and the footer icons overlap the text (img 1200).
- In visionOS, the right-and-wrong pair uses the same 3D room and the same rounded translucent window, varying only the depth of the word "hello": in flat white serif, read head-on and sharp (img 1201), versus letters with thickness and volume that end up confusing and overlapping each other (img 1203).
- The judgment marks come isolated in their own frames over a white background, without overlapping the examples: white check in a green circle for correct use (img 1202) and white X in a gray circle for incorrect use (img 1204).
<!-- /visual:typography -->

## What this group reveals about the Apple way

1. Apple builds visual and information hierarchy in overlapping layers, never by chance: Liquid Glass separates controls from content (materials), depth and scale communicate importance in visionOS (spatial-layout), and text styles form an explicit typographic staircase of size and weight (typography). The idea of "functional layer" versus "content layer" repeats as a central organizing principle.

2. Every visual decision has to survive the worst-case accessibility scenario before being approved: vibrant color over material so it doesn't depend on system settings (materials), Dynamic Type and AX1 to AX5 covering up to 70 pt of leading (typography), and motion treated as optional, never the sole channel of information (motion).

3. Apple treats "perceptual realism" as a design criterion, not an aesthetic: motion calls for feedback that matches the person's physical gesture; spatial-layout uses depth cues (distance, occlusion, shadow) to avoid visual discomfort; right-to-left flips movement icons (like sound waves) to preserve the sense of "forward".

4. The user's physical and psychological comfort is treated as an engineering requirement, not a footnote: in visionOS, 0.2 Hz oscillation is cited with frequency precision (motion), direct gestures are discouraged because they tire the arm (spatial-layout), and text with depth is discouraged because it slows down reading (spatial-layout, typography).

5. The person's trust is protected against interface manipulation by very specific rules, not just vague principles: privacy explicitly lists prohibited designs on tracking pre-alert screens (incentives, an image of the alert itself, annotations pointing to the button), citing the exact clause of the App Review Guidelines.

6. Where Apple allows customization, it draws the space of freedom with surgical precision: the location button can change title, glyph, background color and corner radius, but nothing beyond that (privacy); custom symbols must follow the system template in level of detail, optical weight and alignment (sf-symbols).

7. Internationalization (RTL, numerals, multi-language typography) is treated as a system of semantic rules, not mechanical mirroring: numbers never invert the internal order of digits even in RTL context, but they do invert when they communicate progress; logos and universal marks are never mirrored; Arabic or Hebrew fonts gain up to 2 points more to visually balance with Latin capitals (right-to-left).

8. The system typography (San Francisco and New York) and the symbols (SF Symbols) are designed as a single shared technical foundation: the nine symbol weights correspond exactly to the SF font weights, allowing "precise weight pairing" between icon and adjacent text (sf-symbols, typography).

9. Writing is treated with the same systematic rigor given to the visual code: capitalization, possessive pronouns and error messages follow explicit, comparable patterns (right/wrong) instead of loose recommendations, which reinforces that "product voice" is part of the design system, not just loose copy.

10. On the more niche platforms (visionOS, watchOS), Apple takes on extra responsibilities for the human body's physical comfort that do not exist on flat-screen platforms: watchOS embeds mandatory, non-customizable easing into every animation (motion); visionOS defines minimum distance between interactive elements in angular points, not in pixels (spatial-layout, typography).

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/materials.md, 123 lines read of 123, yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/motion.md, 61 lines read of 61, yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/privacy.md, 117 lines read of 117, yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/right-to-left.md, 113 lines read of 113, yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sf-symbols.md, 131 lines read of 131, yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/spatial-layout.md, 61 lines read of 61, yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/typography.md, 933 lines read of 933, in three blocks (1-350, 351-700, 701-933), yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/writing.md, 53 lines read of 53, yes

Note on the tracking tables in typography.md: the tracking tables by point size (SF Pro, SF Pro Rounded, New York, macOS, tvOS, SF Compact, SF Compact Rounded) were read in full, line by line, but in the exact specifications section above they were summarized instead of transcribed number by number, because they are very extensive technical reference tables (more than 300 lines of numeric data); all values remain available in the source file already read, with no reading omission.
