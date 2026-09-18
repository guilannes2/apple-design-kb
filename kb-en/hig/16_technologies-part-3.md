# Technologies (part 3)

## SharePlay (slug: shareplay)

### What it governs
Governs how an app offers shared, real-time experiences between people on different devices, synchronized by the system and coordinated with FaceTime or Messages, including the spatial behavior of these experiences in visionOS.

### Why
The central intent is presence: making people in different locations feel like they are doing something together, at the same moment. That is why the system synchronizes the activity across devices and keeps communication (voice, video) running in parallel. In visionOS, Apple takes this principle further by creating a "shared spatial context": everyone sees the content in the same relative position, which allows pointing, discussing and interacting as if the object were physically there, reinforcing authentic and intuitive interaction. Spatial template decisions (side by side, surround, conversational) derive from a broader design question: does the activity call for focus on the content (side by side), social interaction around an object (surround), or companionship while the app does something in the background (conversational)?

### Do and avoid
- Use SharePlay for real-time experiences; for asynchronous collaboration, offer a way to share or save after the session ends.
- Design the experience according to the nature of the activity: a single shared view for watching/browsing, or a view adapted to each person's role for games.
- Build experiences that work across different Apple platforms.
- Give a clear, recognizable path to start an activity, such as a button with the SharePlay symbol; also use the system share sheet.
- Let people enter the activity without friction: take them quickly to the shared content, avoid irrelevant screens, and defer non-essential steps (sign-in, download, subscription) to the right moment.
- Offer provisional access to people who are not subscribers, or support Family Sharing, to reduce the barrier to entry.
- Describe activities clearly and concisely in invitations, without truncation.
- Help people understand why the activity changed when one person's action affects everyone (e.g., pausing a movie pauses it for everyone).
- Use the term "SharePlay" correctly: as a noun or verb, never with an adjective (avoid "virtual SharePlay" or "spatial SharePlay") and never inflected (SharePlayed, SharePlays, SharePlaying).
- On iOS, iPadOS and macOS, support Picture in Picture for shared video.
- In visionOS, prefer starting the experience from a window (shareable via the Share button next to the window bar); for an immersive space, custom UI is required.
- Resolve conflicts naturally: if only one person can use an object at a time, do not show UI that lets another person take control; let people negotiate by voice or gesture, with a simple rule such as "the last change wins."
- Reserve unique/personalized views only for moments that truly call for it; in general, keep views and immersion levels synchronized.
- When changing the immersion level, check whether it would interrupt someone's task; if so, let the person choose when to enter, instead of pulling them in automatically.
- Let each participant customize personal settings (volume, captions) without affecting the others.
- Make it easy to leave and return to the activity, with a clear control for re-entering.
- Support people who do not appear as a spatial Persona (those joining from another device, or who turned off Persona), by offering alternatives in the UI when the experience depends on facial expressions or gestures.
- Adopt the spatial template that best fits the activity, or create a custom template if none fits.
- Break a complex activity into stages, each with its own template; prefer mixing system and custom templates over designing a single complex template.
- Tie template transitions to an explicit action by the person (avoid unexpected changes of role or seat).
- Keep transitions smooth: avoid frequent changes or ones that require a lot of movement; use a fade when moving someone to a different seat and give visual reorientation cues.
- For custom templates: account for people who are physically present (seen via passthrough, not as a Persona); offer the ideal seating orientation for the content; support the maximum number of seats (defining all of them in advance); position seats at least one meter apart; define the seat fill order in a balanced way; keep roles (player, spectator, team member) independent of seats, except when a role genuinely requires a specific spot (e.g., the host at the head of the table).

### Exact specifications
- Apple Vision Pro supports up to 5 spatial Personas in one activity.
- Seats must be positioned at least 1 meter apart from each other.
- If a spatial Persona gets too close to another, it is replaced with a contact photo.

### Platform differences
- tvOS: no additional considerations. watchOS: not supported.
- iOS, iPadOS, macOS: support for Picture in Picture for shared video (PiP window on iPhone/iPad; a window that can be brought to the front on Mac).
- visionOS: an extensive, dedicated section, covering the design of shared activities, Personas, spatial templates (side-by-side, surround, conversational) and custom templates, as detailed above.

### Links to other articles
Cites: Immersive experiences (for guidance on immersion transitions); Writing and Inclusion is not cited here, but the article refers to developer documentation (Group Activities, Synchronizing data during a SharePlay activity, Adding spatial Persona support, Configure your visionOS app for sharing with people nearby, Building a guessing game for visionOS, SpatialTemplateSeatElement, isSpatial and isNearbyWithLocalParticipant).

---

<!-- visual:shareplay -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened, all codes checked; the page has no video.
- The opening icon (the outline of a person inside two concentric arcs, in dark blue over a blue gradient) is shown as a construction drawing with a dashed rectangular grid and concentric circles that start exactly at the center of the symbol and extend beyond the arcs, suggesting that the arcs' radius derives from these guides (img 1020).
- The shared video screen on iPhone overlays the paused video with back, pause and skip-forward-10-seconds controls, has a band at the top with a small avatar and an indication of who started the activity, an X button in the top left corner, a progress bar with elapsed and remaining time, and the other person's thumbnail in the bottom right corner (img 1021).
- The screen for the person who started the activity is identical to the participant's, same video, same band and same time, and only the person in the thumbnail changes, which shows that both sides of the session use the same interface (img 1021, 1022).
- The recommended button is a blue rectangle with rounded corners, with the SharePlay symbol on the left and the "Start Activity" label in white on the right, presented as finished, with no grid or measurement (img 1023).
- In the side-by-side template, six silhouettes lined up in a curve all look toward a green rectangular panel, and not at each other; a white silhouette among the gray ones marks the viewer's position (img 1024).
- In the surround template, five silhouettes form a circle facing inward, around a green sphere at the center of the platform (img 1025).
- In the conversational template, five silhouettes are closer together, in a closed half-circle, and the green panel moves to the edge of the group, leaving people facing each other more than the content (img 1026).
- The three templates share the same language: an almost black background, a dark circular platform with a slight glow in perspective, gray silhouettes with no face or detailed clothing, and the color reserved for the content, always saturated green; there is no text, ruler or annotation, and the difference between them is communicated only by the relative position between people and object (img 1024, 1025, 1026).
<!-- /visual:shareplay -->

## ShazamKit (slug: shazamkit)

### What it governs
Governs the use of audio recognition (matching a sound sample against the ShazamKit catalog or a custom catalog) inside apps, with a focus on privacy in microphone use and in storing recognized songs.

### Why
Privacy logic dominates: since the feature depends on the device's microphone, Apple requires an explained permission request and limits recording to the minimum time necessary, so that people do not feel the microphone "stays on" unnecessarily. Likewise, even when both the Music Recognition control and the Shazam app show the app as the source of the recognized song, Apple values giving people explicit control over which apps can record content to the iCloud library, recognizing that visible attribution does not substitute for consent.

### Do and avoid
- Request microphone access only when necessary and explain why you are asking (see Privacy).
- Stop recording as soon as possible: record only for the time needed to get the sample.
- Let people opt in to storing songs recognized by the app in the iCloud library, even though the app's attribution already appears in Music Recognition and in Shazam.

### Exact specifications
No number, measurement or numeric value appears in the text.

### Platform differences
No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

### Links to other articles
Cites Privacy for guidance on permission requests.

---

<!-- visual:shazamkit -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has no video.
- The technology icon (a rounded dark blue diamond with stacked wavy curved layers, like sound waves, and a central shape resembling an S) is presented as a construction drawing over a blue gradient, with a dashed rectangular grid and concentric circles centered on the symbol, in the same treatment as the SharePlay icon; it matches the official description (img 1027).
- The page's only interface screen does not show the audio recognition itself, but rather the request for microphone access: a centered system modal alert, with a title naming the app and the microphone and a short body explaining the reason (img 1028).
- In the alert, the two buttons sit side by side with a color hierarchy: decline ("Not Now") on the left in light gray and allow ("Allow") on the right in highlight blue (img 1028).
- The alert covers the middle of the fictional app's welcome screen (a blue-green gradient with mathematical symbols and the app's name in the background), and the app's "Get Started" button remains visible behind it, at the bottom (img 1028).
<!-- /visual:shazamkit -->

## Sign in with Apple (slug: sign-in-with-apple)

### What it governs
Governs how and when to offer login with Apple ID, what data to collect, and the exact appearance (standard system and customized buttons) of the Sign in with Apple control.

### Why
The central principle is trust combined with convenience: giving people a fast and private way to sign in without remembering multiple passwords, and using this to reduce signup friction. Apple repeatedly reinforces the principle of minimizing data collection and respecting privacy choices (such as the private relay email address), because this is the foundation of the trust that sustains the feature. On the visual side, the strict standardization of the button (colors, proportions, permitted text) exists so that Sign in with Apple is instantly recognizable and is not confused or diluted by brand variations, and that is why it goes through App Review.

### Do and avoid
- Offer Sign in with Apple in every version of the app or website, on every platform, including non-Apple ones.
- Ask for login only in exchange for clear value; briefly explain the benefits of signing in.
- Delay login as much as possible; let the person explore the app before requiring commitment.
- If an account is required, explain why before asking for its creation, and only then offer the login options.
- Consider allowing an existing account to be linked to Sign in with Apple, either before or after logging in to the existing account.
- In commerce apps, wait until after the purchase to ask for account creation; if guest checkout is supported, offer quick account creation after the transaction (and do not ask again for name/email already provided via Apple Pay).
- As soon as Sign in with Apple is completed, welcome the person immediately; do not delay the experience by asking for non-required information.
- Indicate when the person is signed in via Sign in with Apple (e.g.: "Using Sign in with Apple" in settings).
- Minimize requests for additional data; explain why you need it and clearly show the data received.
- Make clear whether additional data is required (legal/contractual) or only recommended.
- Never ask for a password from people who use Sign in with Apple.
- Avoid asking for a personal email when the person has already provided a private relay address; instead, allow the relay address to be seen in the app, direct them to Settings > Apple Account > Password & Security > Apps using Apple Account, or use other identifiers (order number, phone).
- Give the person a chance to use the app before asking for optional data, and never block access to features for declining optional data.
- Be transparent about the data collected, for example, greeting the person by the shared name or email.
- Display the Sign in with Apple button prominently, no smaller than other login buttons, and without requiring scrolling to see it.
- Prefer the buttons provided by the system (ASAuthorizationAppleIDButton, WKInterfaceAuthorizationAppleIDButton, or the web version), which guarantee approved appearance, correct proportions, automatic title translation and a VoiceOver label.
- Use only the approved titles: "Sign in with Apple", "Sign up with Apple", "Continue with Apple" (iOS, macOS, tvOS, web); watchOS uses only "Sign in".
- Choose the style (white, white with outline, or black) according to the contrast of the background; never use white without an outline on a light background, or black on a dark background.
- On watchOS, the black button actually uses a system-defined dark gray (it is not pure black), to contrast with the pure black background of the Apple Watch.
- When creating a custom button, use only the logo artwork downloaded from Apple Design Resources; never create a custom Apple logo; do not use the isolated logo as a button; match the height of the logo file to the height of the button; do not crop the logo file or add vertical padding.
- Do not change: the permitted titles, the general shape (rectangular for logo+text; circular or rectangular for logo only), and the colors of the logo and the title (always black or white, never custom colors).
- What can be adjusted: title font (weight and size), title case (all caps is allowed), background appearance (texture or subtle gradient while keeping black/white), corner radius, bezel and button shadow.
- Use a PNG file only for buttons 44 pt in height (standard on iOS); use SVG/PDF for any height.
- Prefer the system font for the title; keep the same ratio between button height and system font size.
- Preserve the standard capitalization style (first letter capitalized in "Sign"/"Continue" and in "Apple"; remaining letters lowercase) unless the interface uses all caps.
- Vertically align the title to the center of the button, then add the logo with height equal to that of the button.
- For logo-only buttons: do not add horizontal padding (the artwork already includes it); use a mask to change the default square shape (circle, rounded rectangle); never crop Apple's artwork to reduce the built-in padding.

### Exact specifications
- Logo+text button (iOS, macOS, web): minimum width 140 pt (140 px @1x, 280 px @2x); minimum height 30 pt (30 px @1x, 60 px @2x); minimum margin 1/10 of the button height.
- System font: the title font size is 43% of the button height; equivalently, the button height is 233% of the title font size (rounded to the nearest integer). Examples cited: 44 pt tall button with 19 pt font; 56 pt tall button with 24 pt font.
- Minimum margin between the title and the right edge of the button: at least 8% of the button width.
- Logo-only button: use PNG only for 44x44 pt buttons; ratio always 1:1.
- Minimum margin around the logo-only button: at least 1/10 of the button height.

### Platform differences
No additional considerations specific to iOS, iPadOS, macOS, tvOS, visionOS or watchOS beyond those already described (watchOS has a single title "Sign in" and a dark gray background color instead of pure black).

### Links to other articles
Cites Creating a custom Sign in with Apple button (related guide), Authentication Services, and the "Sign in with Apple button" as a related resource.

---

<!-- visual:sign-in-with-apple -->
### What the illustrations show
Basis: 7 of 7 illustration sheets opened, all codes checked; the page has no video.
- The opening is the construction drawing of the Apple logo in dark blue over a blue gradient, with a dashed rectangular grid and a guide circle centered on the logo, the same treatment as the SharePlay and ShazamKit icons (img 1053).
- The offer after purchase appears on an order-complete screen with an X to close at the top, a green circle with a check, a complete-purchase title and a secondary line about the email confirmation; below, two stacked buttons: "Create Account" in light, neutral gray, and, below it, "Sign up with Apple" in black with the logo (img 1054).
- The three system button titles appear in the same style of black button with logo and white text, changing only the text: sign in, sign up and continue (img 1055, 1056, 1057).
- watchOS has its own button, next to the equivalents from the other platforms: just "Sign in", narrower and in a slightly grayish black (img 1058); over a pure black background, that dark gray is exactly what separates the button from the background (img 1067).
- The white style is taught through a right-and-wrong pair with an identical button and only the background varying: over solid dark gray the contrast is high and it gets a green check (img 1059, 1060); over light gray the button nearly blends into the background and it gets a gray X in a circle (img 1061, 1062); the markers stand alone, with no text inside the image.
- White with outline gets a thin dark stroke that separates it from the light gray background, keeping legibility (img 1063); over a very dark gray background, the same outline nearly disappears and the frame looks continuous with the background (img 1064).
- The black style contrasts well over very light gray (img 1065) and, over dark gray, nearly merges with the background and loses edge definition (img 1066).
- Corner radius is a progression on the same black button: square 90-degree corners at the minimum-radius label (img 1068), moderate rounding at the system default (img 1069), and maximum radius, with the short sides fully rounded into a capsule shape (img 1070).
- Alongside other providers, two iPhone screens show two arrangements: four stacked buttons of the same width and height, Apple's in black with the real logo and the fictitious X, Y and Z in light gray with a filled circle, square and triangle in place of the logo (img 1071, left); or a text field at the top, the label "Sign in with:" and four small square buttons side by side, Apple's in black with the logo and three gray ones with the same shapes (img 1071, right).
- The minimum clear space around the isolated logo is drawn as a thick shaded border around the logo's square, in both polarities: black logo on a white square with a dark gray border (img 1072) and white logo on a black square with a light border (img 1073).
- The proportions of the custom logo-and-text button come with dimensions: a vertical brace of 44 pt in height with a 19 pt font callout (img 1074) and, on the larger button, 56 pt in height with a 24 pt font, in a height-to-font ratio nearly equal to the previous one, close to 2.3 in both cases (img 1075); these are the only images on the page with explicit numeric dimensions.
- The logo-only button is the same black square with a white logo under three masks: rounded rectangle (img 1076), no mask, with square corners (img 1077), and full circle (img 1078).
<!-- /visual:sign-in-with-apple -->

## Siri (slug: siri)

### What it governs
Governs how an app exposes its actions (intents) and content (entities) to Siri and Apple Intelligence, and how to write the responses and dialogs that Siri delivers on behalf of the app.

### Why
The underlying principle is that Siri must understand the app with the least extra work: by default the system does not know what an app does, so the App Intents framework and the App schema domains exist so that common apps (email, music, photos) inherit ready-made logic, with natural conversation and deeper contextual understanding, instead of each app reinventing everything. Apple also insists on consistency of voice and behavior: using terminology familiar to the user (not to the app), avoiding advertising inside Siri's responses, and keeping responses short and without forced humor, because Siri is heard repeatedly and fatigue/irritation set in quickly with wordy responses. There is also a principle of neutrality and inclusion in responses (avoiding unnecessary gendered pronouns) and of device-independence, since a request can start on one device and end on another.

### Do and avoid
- Identify the app's most popular actions and the contexts (e.g., hands-free, specific device) in which they occur, to prioritize which actions/entities to expose.
- Use terms familiar to people for the app's content and actions (e.g., "track", "song" or "podcast", according to what the audience recognizes).
- Offer content relevant to personal context (recent searches, favorites, wishlist) instead of the entire catalog, except for categories like email/messages, where expanded access makes sense.
- Don't include advertising, marketing or a purchase pitch in the content Siri delivers.
- Only provide a custom response if the standard responses don't meet the app's needs.
- Write clear, descriptive response dialogue; customize follow-up questions for clarity (e.g., "Which soup?" instead of "Which one?").
- Keep responses as concise as possible, using conversation context to remove unnecessary details; avoid superfluous words or attempts at humor.
- Provide responses that Siri can deliver both audibly and visually, making sure the voice response works on its own without depending on visual elements.
- Design inclusive interactions, avoiding specific pronouns when unnecessary (e.g., "Who should I send it to?" instead of "What's his or her name?").
- Ask an open-ended question when the full list of options is too long for Siri to read in time.
- Keep responses device-independent whenever possible, since the request can start on one device and apply on another.
- Omit the app's name from responses; the system already provides verbal and visual attribution.
- Use appropriate language and respect parental controls; don't include offensive language.
- Help people understand errors and failures with descriptions specific to the situation (e.g., "Sorry, we're out of chicken noodle soup" instead of "Sorry, we can't complete your order").
- Refer to Siri by name, never by pronouns (she, he); never personify or reproduce Siri's functionality, nor give a response that seems to come from Apple.
- Don't use reserved phrases like "Call 911" or "Hey Siri".
- In a localized context, translate only the word "Hey" in the phrase "Hey Siri"; "Siri" is never translated (an extensive table of translations by locale is in the article, including pt_BR: "E aí Siri").

### Exact specifications
No pixel, point, time or proportion measurement appears in the text; the content is mostly about behavior and dialogue. The only "numeric table" is of locale translations for the phrase "Hey Siri", with no measurement values.

### Platform differences
The article doesn't have its own "Platform considerations" section separated by system beyond the general introduction; Siri AI is described as available "on supported devices" via Apple Intelligence, with no breakdown by OS in the text read.

### Links to other articles
Cites App Shortcuts, Snippets, Writing and Inclusion, Guidelines for Using Apple Trademarks, and developer documentation (App Intents, App schema domains, Apple Intelligence and Siri AI).

---

<!-- visual:siri -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has a single illustration and no video.
- The symbol is a circular ring in a darker blue with a wavy S-shaped line crossing the interior, over a blue gradient background; it matches the official description of a design tinted blue with a rectangular and circular grid (img 1079).
- Besides the dashed rectangular grid, there's a smaller guide circle, concentric with the ring, that marks the proportion of the inner stroke relative to the outer outline (img 1079).
- It's the only visual material on the page and repeats the construction language of the SharePlay, ShazamKit and Sign in with Apple icons (dashed grid, concentric circular guide, blue over blue gradient); no interface screen or response example is shown (img 1079).
<!-- /visual:siri -->

## Tap to Pay on iPhone (slug: tap-to-pay-on-iphone)

### What it governs
Governs how a payment app on iOS integrates Tap to Pay on iPhone (contactless payment acceptance without external hardware), from the merchant's acceptance of terms through checkout, result display and additional uses such as loyalty cards.

### Why
The central logic is reliability at the moment of checkout: since checkout is a time-sensitive action, Apple advises preparing the feature in advance (setting up the device as soon as the app starts and every time it returns to the foreground) so the merchant never has to wait. There's also a principle of label clarity and error prevention: the text "Tap to Pay on iPhone"/"Tap to Pay" must be reserved exclusively for payment actions, so the merchant never confuses a payment button with one for another purpose (such as reading a loyalty card), and the Apple logo can never appear on the button, so as not to suggest direct Apple endorsement of the commercial transaction.

### Do and avoid
- Help merchants accept the Tap to Pay on iPhone terms and conditions before they start interacting with customers (e.g., within onboarding flows or in-app messages).
- Present the terms and conditions only to an administrator user; if a non-administrator tries to activate it, explain that administrator access is required.
- Make sure the merchant's device is up to date before presenting the terms, if the PSP requires a specific iOS version.
- Offer a tutorial describing the supported payment types and how to use the feature (via Learn More, automatic presentation after accepting the terms, presentation to new users, or a consistent location such as settings/help).
- In your own tutorial, show how to start checkout for each payment type, position a card/digital wallet, and handle PIN entry (including accessibility mode).
- Offer Tap to Pay on iPhone as a checkout option whether or not the feature is enabled; when the button is tapped, present the terms if necessary and show the screen automatically when setup finishes.
- Prepare the feature as soon as the app starts and immediately after each transition to the foreground, to minimize wait time.
- Keep the checkout option available even during background setup, displaying a progress indicator (indeterminate, or determinate if the API indicates continuous progress).
- If the app supports multiple payment methods, make the Tap to Pay button easy to find without scrolling; if it's the only method, open it automatically when checkout starts.
- Make it easy to switch between Tap to Pay on iPhone and supported hardware accessories, without requiring a trip to the app's settings during checkout.
- Use the label "Tap to Pay on iPhone" or, if space is limited, "Tap to Pay"; exception: if it's the only supported method, existing buttons such as "Charge" or "Checkout" can be reused; if using an icon, use the SF Symbols `wave.3.right.circle` or `wave.3.right.circle.fill`; never include the Apple logo on the button.
- Use the label "Tap to Pay on iPhone" only for payment actions, never for actions that aren't payment-related.
- Determine the final amount before starting the Tap to Pay experience (e.g., present tip options beforehand); display the final amount on the Tap to Pay screen.
- Display pre-payment options (such as payment type) before the Tap to Pay screen.
- Start processing the transaction as soon as possible, even before the checkmark animation finishes (API returnReadResultImmediately).
- Display the authorization progress indicator only after the Tap to Pay screen animation finishes, for a smooth visual transition.
- Clearly display the transaction result, approved or declined, and offer digital receipt options (QR code, text message) when possible.
- Help the merchant complete checkout when payment can't be completed via Tap to Pay (a new screen or reuse of the checkout screen, checkout via another method, or relaunching Tap to Pay).
- For SCA (Strong Customer Authentication) in some regions, be prepared to display the PIN entry screen instead of the transaction result.
- If the system returns an error the merchant needs to resolve, display a clear description of the problem and a recommendation (e.g., an alert to update iOS).
- Make it easy for the merchant to get help for problems they can't resolve (help content in the app/site, a contact-support action).
- For card reads with no transaction amount (lookup, verification, refund), use a generic label such as "Look Up", "Store Card", "Verify" or "Refund", never "Tap to Pay on iPhone" or "Tap to Pay".
- If the app supports a loyalty-card transaction independent of payment, use a separate, clearly labeled button, avoiding payment-related terms in the label (e.g., use "Loyalty Card", not "Tap to Pay on iPhone - Loyalty").

### Exact specifications
No numeric measurement (pt, px, ms, proportion) appears in the text; the content is entirely behavioral and flow-related.

### Platform differences
No additional considerations for iOS. Not supported on iPadOS, macOS, tvOS, visionOS or watchOS.

### Links to other articles
Cites Progress indicators, Alerts, Additional interactions (within the article itself), and Tap to Pay on iPhone marketing guidelines, as well as developer documentation (ProximityReader, ProximityReaderDiscovery API, PaymentCardReaderSession.ReadError, prepare(using:), PaymentCardReader.Event.updateProgress(_:), PaymentCardReader.Event.readyForTap).

---

<!-- visual:tap-to-pay-on-iphone -->
### What the illustrations show
Basis: 5 of 5 illustration sheets opened, all codes checked; the page has no video.
- The opening is conceptual, with no interface: a dark central circle with the contactless payment waves symbol, over a blue gradient with a dotted rectangular and circular grid (img 1121).
- The activation screens follow the same hierarchy within the iPhone frame: title, short body, primary action in a solid block blue button and secondary action in a text link right below, with a gray image placeholder in the footer; on the first, enable and learn more (img 1122); on the second, make a test transaction or leave it for later (img 1123).
- The tutorial is accessible in a standard Settings list cell, on the "Tutorials" screen, with a bold title, gray subtitle and a disclosure arrow on the right (img 1124).
- The tutorial appears in a modal sheet with a gray circular X in the top right corner, a small uppercase label above the bold title, a dark iPhone illustration asking to bring the card close with an orange card showing the merchant name and amount, and numbered steps below (img 1125).
- During checkout preparation, a thin blue progress bar sits right below the navigation bar (back and the title "Checkout"), above the preparation text and the centered amount in a large typographic highlight (img 1126); the next screen keeps everything the same with the bar full, which the official description treats as an indeterminate indicator (img 1127).
- During authorization, the bar disappears and a gray spinner appears next to the label "Authorizing", over the same large amount (img 1132).
- The payment button is a full-width blue shape with the waves symbol on the left and centered text, marked as correct with a green badge (img 1128, 1129); the same button with the Apple logo in place of the waves is marked as wrong with a gray X badge (img 1130, 1131); the badges sit isolated, outside the button.
- The result uses a large circular badge centered above the amount, with "Done" in the right corner of the bar, the prompt to choose the receipt and three empty gray blocks stacked as options (img 1133); on decline, the layout is identical and only the badge changes, from a green check to a red X (img 1134).
- When the payment doesn't complete, the back button reappears in the bar, the red badge comes with the text for the incomplete payment and a list of four stacked methods where the contactless one is first, in solid blue, with the rest in gray (img 1135).
- The loyalty buttons keep the same blue shape, but with only text and no waves symbol: one labeled "Loyalty Card" (img 1136) and a variant whose label joins the feature name to the word "Loyalty" (img 1137).
<!-- /visual:tap-to-pay-on-iphone -->

## VoiceOver (slug: voiceover)

### What it governs
Governs how an app provides descriptions, labels and reading order so that the VoiceOver screen reader makes the interface and content accessible to people who are blind or have low vision.

### Why
The guiding principle is that visual information needs a faithful and proportional audible equivalent: not everything needs to be described (purely decorative images should be excluded, out of respect for the person's time and to reduce cognitive load), but everything that is functionally relevant (meaningful images, charts, spatial relationships between elements, layout changes) needs to be explicitly communicated to VoiceOver, because relationships that sighted people perceive through proximity and visual alignment are invisible to someone who cannot see the screen. Grouping elements (such as image and caption in a single frame) exists so that the reading order matches the logical sense of the content, not the raw arrangement on the screen.

### Do and avoid
- Provide descriptive alternative labels for all key interface elements, in addition to the system controls' default generic labels; keep the descriptions up to date as the interface changes.
- Describe meaningful images; describe only the information the image itself conveys (not the surrounding context, such as nearby captions).
- Make charts and infographics fully accessible: provide a concise description of what each infographic conveys, and make equivalent interactions available for people using VoiceOver, if the visual version allows interaction.
- Exclude purely decorative images from VoiceOver.
- Use titles and headings to help navigate the information hierarchy; offer unique, succinct titles, and precise section headings.
- Specify how elements are grouped, ordered or linked, since proximity and visual alignment (visual-only cues) do not reach VoiceOver by default.
- Remember that VoiceOver reads elements in the reading order of the active language/locale (in US English: top to bottom, left to right); group an image and its corresponding caption in a single VoiceOver frame.
- Inform VoiceOver when visible content or layout changes occur, so the person can update their understanding.
- Support the VoiceOver rotor when possible, identifying headings, links and other content types; the rotor can also trigger the braille keyboard.

### Exact specifications
No number, measurement or value appears in the text.

### Platform differences
No additional considerations for iOS, iPadOS, macOS, tvOS or watchOS.
visionOS: custom gestures are not accessible by default when VoiceOver is on; apps and games that define custom gestures do not receive hand input by default, to ensure the person can explore the interface by voice without the app simultaneously reacting to hand gestures. A person can opt into Direct Gesture mode, which disables VoiceOver's default gestures and lets the app process hand input directly.

### Links to other articles
Cites Accessibility, Inclusion and Charts.

---

<!-- visual:voiceover -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened, all codes checked; the page has no video.
- The opener combines the accessibility figure inside an open navy blue circle with a speaker with sound waves to the left, in dark blue over a lighter blue gradient in the upper left corner, with a dashed grid and a guide circle concentric to the human symbol (img 1224).
- The wrong grouping example is an iPhone screen with back and more options at the top, a placeholder paragraph of text, two side-by-side photos (mangoes and artichokes), each with a caption below, and another paragraph; a thin black rectangle surrounds both photos and both captions as a single group, accompanied by a white X in a gray circle (img 1225, 1226).
- The right example repeats exactly the same screen and the same content, but the rectangle surrounds only the mango photo with its caption, while the artichoke photo and its caption sit outside any border; accompanied by a white check in a green circle (img 1227, 1228).
- The pair isolates a single variable, where the grouping border is drawn, and the right and wrong markers appear alone in their own frames, right after each example, never drawn over the screenshot (img 1225 to 1228).
<!-- /visual:voiceover -->

## Wallet (slug: wallet)

### What it governs
Governs how an app creates, adds, displays and updates digital passes (cards, tickets, loyalty cards, etc.) and trackable orders in Apple Wallet, including exact image specifications and identity verification via Wallet.

### Why
The throughline is that Wallet maintains a consistent visual style to build familiarity and trust, so the design of a pass should not just replicate the look of the physical version, but feel native to Wallet. The hierarchy of fields (what stays visible when the pass is collapsed versus expanded) reflects the principle of showing the essential information first (event date, account balance) and reserving the rest for when the person actually needs it. For orders (order tracking), Apple prioritizes immediate confirmation (the person needs to know the order was received even if fulfillment details do not exist yet) and continuous status updates, because this reduces the anxiety of waiting. In identity verification, the dominant principle is minimization and the right moment: ask only for the data that is strictly necessary (minimum age instead of date of birth), only at the instant it is needed, and be transparent about how long the data will be retained, because this sustains the trust that makes Verify with Wallet viable.

### Do and avoid
- Offer to add new passes to Wallet with one tap when an action generates a pass (ticket purchase, rewards program signup); for predictable and frequent actions, you can add it in the background after a one-time authorization.
- Help add a pass created outside the app (via a website or another device); if the person declines, do not ask again.
- Add related passes as a group (e.g.: boarding passes for a connecting flight) all at once.
- Display an "Add to Apple Wallet" button to allow adding an existing pass that is not yet in Wallet.
- Allow jumping from the app directly to the pass in Wallet, with a link of the "View in Wallet" type.
- Inform the system when passes expire (expiration date, relevant date, the "voided" property), so Wallet correctly hides expired passes.
- Always ask permission before deleting passes from Wallet.
- Help the system suggest a pass at the relevant moment (e.g.: appearing on the Lock Screen when the person arrives at the gym); for certain types, the system can start a Live Activity.
- Keep passes up to date, reflecting changes (e.g.: flight delay, gate change).
- Use change messages only for time-critical information updates; never for marketing.
- Use semantic tags (required for poster event and semantic boarding passes) to enable automatic layout; also include pass fields in these cases for compatibility with older iOS versions.
- Use Pass Designer to design and preview passes.
- Design a pass that works well on all devices (Apple Watch shows less information and fewer images; do not put essential information in elements that might be absent; avoid padding on images, since watchOS crops blank space).
- Keep the front of the pass clean: show essential information in the header (visible when collapsed); reserve rarely used details for the additional information page.
- Make the pass instantly identifiable, using brand colors and visual elements (images, icons, full-art backgrounds).
- Ensure sufficient contrast between background and text color.
- Use language that works on any device (avoid device-specific phrases, such as "Slide to view", which does not apply to Apple Watch).
- Reserve pass images for visual content only; use text fields and semantic tags for textual information (text embedded in an image is not accessible); use Pass Designer or APIs for barcodes, do not embed them in an image.
- Keep image file size small for fast downloads.
- Provide a pass icon (you can reuse the app icon or design a separate one).
- Avoid inner drop shadows on the logo art, since they reduce legibility.
- For order tracking: make it easy to add an order to Wallet (e.g.: with PKPaymentOrderDetails/ApplePayPaymentOrderDetails, or the "Track with Apple Wallet" button via AddOrderToWalletButton); make order information available immediately after purchase, even if incomplete (with a status such as "Check back later for full order details"); provide fulfillment information as soon as it is available and keep the status updated; provide a high-resolution logo with a non-transparent background; provide distinct, high-resolution product images with a non-transparent background and a direct representation (avoid "lifestyle" context or cluttered background); keep the text brief; use clear, localized language, making sure the displayed price matches the confirmed final price.
- For fulfillment details: provide a link to the order management area (ideally a universal link); clearly describe each item; list a priority of installed apps for the system to link to; avoid duplicate notifications; make it easy to contact the merchant by offering multiple methods (at minimum, a link to the merchant's website); help track the order with a direct carrier link, a pickup barcode, and clear instructions; keep the fulfillment screen focused on tracking, prioritizing that information over other promotional content; choose shipping status values consistent with the available data (carrier name if known, or a generic "shipped" status if intermediate details are not accessible); be direct and complete when describing "Issue" or "Canceled" status.
- For identity verification: present the verification option via Wallet only when the device supports it, with a fallback in case it does not; ask for identity information only at the exact moment it is needed, never before; describe clearly and succinctly why you are asking for the information (purpose string in a complete, direct, specific sentence, sentence case, no passive voice, ending in a period); ask only for the data that is actually necessary (e.g.: a minimum age threshold instead of exact age/date of birth); clearly indicate whether the data will be retained and for how long; choose the system verification button suited to the use case ("Verify Age", "Verify Identity", "Continue", or the generic "Verify", each with a multiline variant for constrained space); the verification button always uses white letters on a black background, with an optional light outline for contrast on dark backgrounds; you can adjust the corner radius to match other buttons.

### Exact specifications
- Logo: minimum width 50 pt, maximum width 160 pt, height 50 pt. File: logo.png.
- Primary logo: minimum width 30 pt, maximum width 126 pt, height 30 pt. File: primaryLogo.png.
- Secondary logo: minimum width 12 pt, maximum width 135 pt, height 12 pt. File: secondaryLogo.png.
- Icon: width 38 pt, height 38 pt (square; rounded corners applied automatically by the system). File: icon.png.
- Strip image: width 375 pt, height 144 pt. File: strip.png (supported in coupon and store card).
- Thumbnail: minimum width 60 pt, maximum width 90 pt, height 90 pt. File: thumbnail.png (event ticket and generic pass).
- Background (non-poster, event tickets): width 343 pt, height 503 pt. File: background.png.
- Background (poster, event tickets and poster generic passes): width 358 pt, height 448 pt. File: artwork.png.
- Footer (airline boarding passes only): width 268 pt, height 15 pt. File: footer.png.
- Logo and product images for order tracking: 300x300 pixels, PNG or JPEG format, non-transparent background.
- Pass images in general: PNG format, in @2x and @3x.

### Platform differences
No additional consideration for iOS, iPadOS, macOS or visionOS. Not supported on tvOS.
watchOS: Wallet displays passes in a scrollable carousel of cards; the person can add the pass to Apple Watch even without a specific watch app; tapping a pass reveals a scrollable details screen. Each pass style defines the fields and images that fit into the three basic layout areas (top row with logo and essential field; second row with primary field; third row with secondary and auxiliary fields); information that does not fit appears on the scrollable details screen. In every style, watchOS crops the strip image to fit the card's proportion and can crop whitespace from other images. The article details the watchOS-specific layout for boarding pass, coupon, store card, event ticket and generic pass (each with three rows of specific content).

### Links to other articles
Cites Apple Pay, ID Verifier, Add to Apple Wallet guidelines, and extensive developer documentation (Wallet, PKPassLibrary.Capability.backgroundAddPasses, PKAddPassesViewController, PKAddPassButton, Pass, Wallet Passes, Wallet Orders, Order, LineItem, Merchant, ShippingFulfillment, VerifyIdentityWithWalletButton, PKIdentityIntentToStore, PKIdentityButton.Label, PKIdentityButton.Style.blackOutline, FinanceKitUI, FinanceKit, PassKit).

---

<!-- visual:wallet -->
### What the illustrations show
Basis: 14 of 14 illustration sheets opened (img 1229 to 1283), all codes checked; the page has no video in the notes.
- The Wallet icon is drawn over a grid of symmetrical dotted guides, with concentric circles and rectangles aligned to the center of the icon, and the entire image appears tinted blue (img 1229).
- All pass styles repeat the same skeleton: header with logo on the left and a short piece of data on the right, body with the primary field or a featured image, footer with the person's identification and the barcode or QR code; between passes the background color changes, not the field structure (img 1230, 1242 to 1249). On the boarding pass the hierarchy descends from the route in large letters, with the airplane icon between the two airports, to the name and rounded status badges, then a grid of operational columns, and ends in a large centered QR code (img 1242).
- Each style treats the image its own way. The coupon uses a narrow illustrated band at the top with the discount value in large typography, and a diagram with dashed rectangles shows that the primary field sits overlapping the band itself, not beside it (img 1243, 1258). The poster ticket has a dominant illustration and a rounded notch at the top of the card (img 1244). The same ticket appears with a blurred background photo plus a thumbnail and then only with a thumbnail over solid blue, keeping fields and the round thumbnail in the same positions and the code at the bottom (img 1245, 1246). The generic pass dispenses with a background image and uses solid purple (img 1249).
- Contrast is taught in pairs separated by markers, a green check for right and a gray X for wrong, never within the same image: the purple pass with white text is legible, the same pass with pink text nearly blends into the background (img 1236 to 1239); over a colorful, blurred background image, white text in a bold weight stays sharp (img 1240).
- Annotated callouts fix the position of each brand element: logo in the top left corner, before the name in text (img 1250); square primary logo accompanied by brand text, or a purely typographic, rectangular logo occupying the same space (img 1253, 1254); secondary logo as a circular emblem in the bottom right corner, next to the venue name (img 1255); square thumbnail with rounded corners in the top right corner (img 1259). The paper bag pair shows the same flat silhouette and then with an inner shadow band that gives it a sunken look, the latter as the example to avoid (img 1251, 1252). The pass icon appears in two places: to the left of the text in the lock screen banner, with rounded corners, and overlapping the bottom left corner of the QR code inside the open card (img 1256, 1257).
- For the full-screen background artwork, the same illustration is shown finished and then covered by solid blue blocks that mark the reserved zones: at the top, bars for the header (two on the skull artwork, one on the waterfall one), and below a larger block for the code and footer, T-shaped on the pass with a QR code; the notes read that the reserved area changes size depending on whether the code is QR or rectangular barcode (img 1261 to 1264).
- The pass fits into system surfaces with visible rules: the black Add to Wallet button sits right below the pass, narrower than the screen and within the page's scroll flow (img 1231); the lock screen banner shows a reduced thumbnail of the pass to the right of the text, above the flashlight and camera shortcuts (img 1232); the Live Activity condenses the ticket into three columns of large, centered numbers, over a black card (img 1233); the featured actions sit outside the card, in side-by-side blocks with a colored icon, bold title and gray subtitle (img 1234, 1257).
- The Pass Designer on the Mac organizes editing in a side tree by field type (header, primary, footer, back) and shows the pass preview on the right with a minimum iOS version label above it (img 1235).
- The order screen is a single template that changes by state: with the order placed there is a partially filled green progress bar; delivered, the bar disappears, a green check appears next to the status and a blue tracking link shows up (img 1265, 1266). A numbered diagram points to each field, from logo and merchant name to status, description, tracking link and items with image, title, quantity and price (img 1268). Delivery and pickup share the same template, swapping the address for time, location and a black barcode button (img 1271).
- In the orders panel, the active ones have status in green and thumbnails, while the month's history stays compact, in gray and without thumbnails (img 1267). Contact methods appear as a list of actions in blue text with a cancel button, not as icons (img 1270). The product image is specified with 300 px rulers on both edges, over a solid background (img 1269).
- The four identity verification buttons use a single design: rounded black background, colored Wallet icon on the left and two lines of white text, the action line smaller and the brand line larger, changing only the first line (img 1272 to 1275).
- On Apple Watch the passes form a vertical stack with the next card peeking out below, and opening a pass sends the QR code to its own white background area below the colored card (img 1276, 1277). A three-row diagram defines the skeleton (logo and essential data, then primary, then secondary and auxiliary) and is repeated per style: the coupon uses an image band in the middle row and leaves the third unused; the store card leaves the top right unused; the ticket puts the event text in the middle; the generic one uses a band in the middle with name and number below; the number of rows never changes (img 1278 to 1283).
Recorded divergences: img 1241, presented as the example of insufficient contrast for the show ticket, shows no perceptible difference from img 1240 in this copy; sheet 0014 has only three images, the last one on the page is img 1283.
<!-- /visual:wallet -->

## What this group reveals about the Apple way

1. Presence over the screen: in SharePlay, the stated goal is not to "synchronize data" but to make people feel like they are together, and this shapes everything from the technical mechanics (shared spatial context) to rules of social etiquette in the design (resolve conflicts "naturally", let the person opt into changes in immersion rather than pulling them along). See shareplay.
2. Data minimization as a recurring principle, not an isolated one: it appears in sign-in-with-apple (ask only for what's necessary, use minimum age instead of date of birth), in wallet (ask for age instead of birthday, retain only for as long as necessary) and in shazamkit (record the minimum amount of audio possible). It is a cross-cutting value, not a rule of a single technology. See sign-in-with-apple, wallet, shazamkit.
3. Brand terminology treated as a legal and recognition asset, not as style: Siri is never translated and never takes a pronoun; SharePlay never takes an adjective or inflection; Sign in with Apple has button titles closed to three options; Tap to Pay on iPhone is reserved only for payment actions. Apple protects these terms with almost legal rules within the design guide itself. See siri, shareplay, sign-in-with-apple, tap-to-pay-on-iphone.
4. Extremely detailed numeric specification when it involves producing visual assets (Wallet and the Sign in with Apple button carry exact pt/px tables), but nearly absent when the article is about conversational or flow behavior (Siri, Tap to Pay, VoiceOver, ShazamKit have no measurements at all). This suggests that Apple documents with numeric precision what will be produced as a graphic asset, and with precision of language/behavior what will be conversation or app logic.
5. Timing as an explicit design variable: "ask for login as late as possible" (sign-in-with-apple), "ask for identity only at the exact moment" (wallet), "stop recording as soon as possible" (shazamkit), "prepare Tap to Pay as soon as the app opens" (tap-to-pay-on-iphone). The moment when an action or request happens is treated as just as important as the content of the request.
6. Fallback and graceful degradation are required, never optional: Wallet requires an alternative path when the device does not support verification; Tap to Pay requires an alternative when payment fails; SharePlay requires an alternative for those without a spatial Persona; VoiceOver requires an alternative (Direct Gesture) for custom gestures. See wallet, tap-to-pay-on-iphone, shareplay, voiceover.
7. Active respect for attention and repetition: Siri warns against long responses because "people may hear the same response multiple times"; SharePlay warns against frequent template transitions; Wallet reserves change messages only for what's critical. Apple treats the repetition of an interaction as a reason to cut, not to enrich. See siri, shareplay, wallet.
8. User trust as a recurring, explicit justification for a design rule, not just for privacy: Sign in with Apple talks about "build on the trust that people have"; Wallet talks about "to help people trust your app"; Tap to Pay talks about preventing label confusion so as not to compromise trust in the transaction. Trust appears as a product concept, not just a compliance one. See sign-in-with-apple, wallet, tap-to-pay-on-iphone.
9. System label consistency versus the app's visual freedom: in almost every article there is a rigid line (button text, feature name, mandatory symbol) surrounded by an explicit zone of freedom for color, shape, font and shadow, as long as the Apple brand and the function remain immediately recognizable. This appears in sign-in-with-apple, tap-to-pay-on-iphone and wallet (Verify with Wallet buttons).
10. Multi-platform as a first-class concern, not an afterthought: SharePlay and Wallet dedicate entire sections to how the same experience behaves differently yet still coherently on iPhone, Apple Watch and visionOS (image crops on watchOS, spatial templates on visionOS), recognizing that the same pass or activity can be experienced by people on completely different devices at the same time. See shareplay, wallet.

## Reading evidence
| File | Lines read | Read to the end |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/shareplay.md | 81 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/shazamkit.md | 28 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sign-in-with-apple.md | 150 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/siri.md | 89 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/tap-to-pay-on-iphone.md | 104 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/voiceover.md | 50 | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/wallet.md | 291 | yes |

All 7 articles in the group were read in full in a single Read call each, with no truncation reported by the tool.
