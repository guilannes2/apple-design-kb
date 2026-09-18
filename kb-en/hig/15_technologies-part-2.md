# Technologies (part 2)

## HealthKit (slug: healthkit)

What it governs: how an app requests access to, displays and uses health and fitness data stored in HealthKit, including the use of the Activity ring element and the Apple Health icon.

Why: Apple treats health data as a sensitive category that requires continuous trust. The central reasoning is that permission is not a one-time event (the app needs to ask again every time it needs access, because the person may have revoked it), and that the privacy experience must be predictable and centralized in the system Settings, never duplicated inside the app. In the same way, Activity rings and the Apple Health icon are elements of visual trust: since people already recognize their exact meaning from use in the Activity app and in Health, any visual change (color, shape, scale) breaks that recognition and can even mislead about what is being measured.

Do and avoid:
- Only ask for access to health data if the app actually offers health and fitness functionality.
- Ask for access only when the context makes the need obvious (for example, when the person logs their weight), not right after the app opens.
- Write short sentences explaining why you need the data on the standard permission screen; do not replicate that screen with a customized version.
- Manage health data sharing only through the system's privacy settings; do not create additional screens in the app that affect this flow.
- Provide a privacy policy with a clear URL in the App Store submission process.
- Use Activity rings only to show progress for Move, Exercise and Stand; never for another type of data.
- Use Activity rings only to represent one person's progress at a time; never several people's at the same time, and make clear whose progress it is (label, photo or avatar).
- Do not use Activity rings as ornament or as part of branding or the app's icon.
- Keep the colors and appearance of the Activity ring and its background always the same; never apply filters, change colors or alter opacity. Design the interface around it to fit, for example by wrapping the rings in a circle.
- Keep a minimum outer margin for the Activity ring equal to the distance between the rings; nothing may cut, obstruct or invade that margin.
- To display the Activity ring inside a circle, adjust the corner radius of the view instead of applying a circular mask.
- Visually differentiate other ring-shaped elements from the Activity ring, using padding, lines, labels, color or scale.
- Provide app-specific information in Activity notifications, but never repeat the same information as the system or show an Activity ring inside notifications.
- Use only the Apple Health icon provided by Apple, downloaded from Apple Design Resources; never create your own version.
- Display the name "Apple Health" near the icon.
- Do not use the Apple Health icon smaller than other health app icons when displayed together.
- Do not use the Apple Health icon as a button; it only indicates compatibility.
- Do not alter the icon's appearance (no circular mask, borders, color overlays, gradients, shadows).
- Keep a minimum clear space around the Apple Health icon.
- Do not use the icon within running text or as a substitute for the words Health, Apple Health or HealthKit.
- Do not display images or screenshots of the Health app, since they are protected by copyright.
- Call the app "Apple Health" or "the Apple Health app" in text; never use the term "HealthKit" facing the user (it is a developer term).
- Use the correct capitalization: "Apple Health" with capital A and H, the rest lowercase; an all-caps version only if the layout requires that typographic style.
- Use the translation provided by the system for the term "Health" to avoid confusion.

Exact specifications: the minimum clear space around the Apple Health icon is 1/10 of the icon's height. There are no other numeric values in the text.

Platform differences: no additional considerations for iOS, iPadOS or watchOS. Not supported on macOS, tvOS or visionOS.

Links to other articles: "Works with Apple Health", "Activity rings", "Apple Design Resources", "Protecting user privacy" (HealthKit developer documentation).

<!-- visual:healthkit -->
### What the illustrations show
Basis: 2 illustration sheets viewed (img 0538 to 0542), all codes checked; no video.
- The opening symbol is a faceted diamond in dark blue, with parallel bands stacked like layers and a small heart nestled in the top corner, over a blue gradient and a grid of straight lines and dashed concentric circles (img 0538).
- In the Health app's summary, the data comes in white cards stacked vertically under the favorites header, all with the same hierarchy: a small metric label with a colored icon on top, a large bold numeric value with the small unit beside it, and the record's time in an even smaller and lighter font in the opposite corner (img 0539).
- The activity card carries the move, exercise and stand submetrics with a small colored ring on the right, and the screen closes with a tab bar of three icons, the selected one in blue (img 0539).
- The Health access modal sheet has a title bar with the refusal in text on the left and the permission in blue on the right, a heart icon on a white card, a title, a short paragraph and a text button to turn off all categories (img 0540).
- On the same sheet, write and read are in separate sections with a gray label in uppercase; each category row has a colored icon, a name and a green toggle on the right, and the app's explanation appears just below in small gray text, indented under the label (img 0540).
- The history uses a miniature Activity ring as the calendar unit: in a black-background modal, with cancel on the left and the month centered, each day is a set of three concentric rings, red, green and blue, with incomplete rings on some days and days with no data in faded gray (img 0541).
- On the onboarding screen that integrates with Apple Health, the official icon (a red heart on a rounded white square) sits small and isolated at the top left, separate from the actions; below it come a large bold white title, a smaller and lighter body, page dots, a filled white pill button to sync and, further down, the skip option as plain text with no background, over a green illustrated background with strokes of fruits and vegetables (img 0542).
<!-- /visual:healthkit -->

## HomeKit (slug: homekit)

What it governs: how an iOS, tvOS or watchOS app can integrate with HomeKit (and by extension with the Home app) to set up, name, organize and control connected home accessories, including the correct use of terminology, the setup flow, Siri interactions and HomeKit icons.

Why: HomeKit defines a hierarchical model of objects (home, room, accessory, service, characteristic, scene, automation, zone) and a specific vocabulary so that Siri and the Home app can reliably understand natural-language voice commands in any app. Apple's reasoning is that, by reinforcing this same terminology and hierarchy in third-party apps, the home automation experience becomes predictable and compositional: a person can say "turn off the upstairs lights" and the system understands it regardless of which app set up the accessory. There is also an explicit concern with not duplicating or fragmenting HomeKit's settings: the database of names and organization must have a single source of truth (the one the person set in the Home app), avoiding confusion and rework.

Do and avoid:
- Recognize HomeKit's hierarchical model even if the app does not organize accessories by rooms and zones in its own UI; this helps people use Siri commands correctly.
- Make it easy to find HomeKit details related to an accessory (such as zone or room); do not hide that information in settings screens that are hard to find.
- Recognize that a person may have more than one home, even if the app does not support that concept visually.
- Do not present duplicate home settings; always reflect the choices made in the Home app, never ask to set everything up again.
- Use the setup flow provided by the system, which already covers naming, joining networks, pairing with HomeKit, assigning categories and marking favorites in a few steps.
- Provide a "purpose string" explaining why the app needs to access Home data.
- Do not require account creation or personal data for setup; leave that optional and after HomeKit setup.
- Honor the person's setup choices; do not force the configuration of other platforms during the HomeKit flow.
- Always start with the system's setup flow before offering a customized setup experience, and only offer the customized one after the basic functionality is already available.
- Suggest service names suited to Siri commands; never suggest company names or model numbers as a service name.
- Check that the names people choose follow HomeKit's naming rules: only alphanumeric characters, space and apostrophe; must start and end with an alphabetic or numeric character; no emojis.
- Help avoid service names that duplicate location information (such as "kitchen light" for a light in the kitchen), since this can produce unpredictable results in voice commands.
- Present examples of voice commands during setup, using the chosen service name.
- After setup, teach more complex Siri commands at useful points in the app.
- Offer shortcuts only for accessory-specific functionality that HomeKit does not support; never duplicate functionality that HomeKit already offers through natural language.
- If the app supports HomeKit and shortcuts, make clear the difference between the two types of voice control.
- Recommend creating zones and service groups when it makes sense for the accessory.
- Be clear about what is possible to do in the app versus in the Home app; help the person understand when to open Home to complete a scene.
- Defer to HomeKit when the app's database diverges from HomeKit's database; automatically reflect changes made in the Home app or in other third-party HomeKit apps.
- Ask permission before updating the HomeKit database when the person makes changes in the app; never overwrite HomeKit settings without explicit direction.
- Do not block camera images with other content; it is acceptable to complement them with useful features, but avoid covering parts of the image.
- Show a microphone button only if the camera supports two-way audio.
- Use only the HomeKit and Apple Home icons provided by Apple; never create your own version.
- Choose the HomeKit icon variant (black, white or custom color) according to the background and the style of the other technology icons used.
- Position the HomeKit icon consistently with other technology icons (the same shape treatment, such as circles).
- Use the HomeKit icon in a non-interactive way; do not use it inside customized buttons or combine it with the word "HomeKit" in interactive elements.
- Do not use the HomeKit icon within running text or as a substitute for the word "HomeKit".
- Correctly pair the icon with the HomeKit name (below or beside it), using the same font as the rest of the layout.
- Make references to HomeKit or Apple Home less prominent than the app's own name or main identity.
- Follow Apple's trademark guidelines: use Apple product names only in the singular, with no possessive form; do not translate "Apple", "Apple Home", "HomeKit" or other trademarks; do not use category descriptors (say "iPad", not "tablet"); do not imply Apple sponsorship, partnership or endorsement; attribute correct legal credits where applicable; refer to Apple devices and operating systems only in technical or compatibility specifications.
- Use correct capitalization: "HomeKit" is one word, with capital H and K; "Apple Home" is two words, with capital A and H.
- Do not use "HomeKit" as a descriptive adjective (avoid "HomeKit lightbulbs"); prefer terms such as "works with", "use", "supports" or "compatible".
- Do not suggest that HomeKit is performing an action on its own (avoid "HomeKit unlocked the back door"; prefer "Back door is unlocked with HomeKit").
- You may use "Apple" together with "HomeKit" (for example "Compatible with Apple HomeKit").
- Use the full app name "Apple Home" at the first mention in running text; later mentions can use just "the Home app".

Exact specifications: the text does not give numeric measurements of pixels, points, durations or proportions for this article.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS (the integration is described as available on iOS, tvOS and watchOS, with the Home app residing on iOS).

Links to other articles: "Resources" (design resources), "Guidelines for Using Apple Trademarks".

<!-- visual:homekit -->
### What the illustrations show
Basis: 4 illustration sheets viewed (img 0544 to 0559), all codes checked; no video.
- The opening symbol is a house in a thick dark blue stroke with three nested levels (outer outline, a smaller house inside and a door at the center) and a chimney on the right, over a blue gradient with the guide grid of dashed lines and circles (img 0544).
- Right and wrong are marked by two minimal, textless badges: a green circle filled with a white check and a gray circle filled with a white X (img 0545, 0546).
- The final HomeKit icon appears clean, in a thin black stroke on white, with no card or grid (img 0547); the Apple Home app icon uses the same three-level house, but filled, in a rounded square with an orange-to-yellow gradient (img 0548).
- The icon variants change only the color according to the background and keep the drawing: a thick black outline on white (img 0549), a white outline on a solid black square with rounded corners that fills the whole frame (img 0550) and a custom-color blue outline on white (img 0551).
- Next to other technologies, the icon gets the same treatment as its neighbors: on a white card with an integration title, three identical light gray circles, each with an icon inside and a label below at the same spacing, the first with the HomeKit house and the others with generic dashed squares (img 0552).
- The wrong examples of interactive use deliberately use a heavy finish: the flat, thin icon inside a chrome circular button, with a metallic gradient and specular highlight at the top (img 0553), and a large rectangular button with a dark metallic gradient and the word HomeKit in bold white, with no icon (img 0554).
- The icon's position within running text is tested on the same white pill card, kept constant: icon at the start of the line, before the sentence (img 0555), in the middle of the sentence between two words (img 0556) and at the end of the line in place of the word HomeKit, which no longer appears written out (img 0557); in img 0555 the drawing carries a padlock inside the house.
- In a settings list on a light gray card, with a title and a divider line, each row has an icon on the left, a title, two gray bars simulating secondary text and a chevron on the right; the HomeKit row uses the icon filled in black with the name written beside it, in the same typographic style as the neighboring rows (img 0558).
- In a two-by-two grid of apps, the colored Apple Home icon sits in a rounded white square with a shadow and the name centered below, with the same typography as the grid's three generic dashed icons (img 0559).
<!-- /visual:homekit -->

## iCloud (slug: icloud)

What it governs: how an app should integrate with iCloud to sync documents, state data and content across devices without requiring the person to sync manually.

Why: the central principle stated in the text is transparency: people do not need to know where the content physically resides, and should always assume they are accessing the most recent version. This leads to a stance of "fewer manual decisions", since most people do not want to manage document storage individually, and the app should automate as much of the file management tasks as possible.

Do and avoid:
- Make it easy for the app to work with iCloud automatically, since the person turns on iCloud in Settings and expects apps to work with it without extra configuration; if you want to offer a choice, show a simple option on first launch between using iCloud for all data or not using it.
- Avoid asking which documents to keep in iCloud; most people expect all content to be available.
- Keep content up to date when possible, balancing this with the device's storage and bandwidth; for very large documents, consider letting the person control when to download updated content, and indicate when a more recent version is available, with subtle feedback if the download takes longer than a few seconds.
- Respect iCloud storage space, which is a finite, paid resource; use it for content the person creates and understands, avoiding using it for app resources or regenerable content (iCloud backups include the contents of each app's Documents folder, so be selective about what you put there).
- Ensure appropriate behavior when iCloud is unavailable (iCloud manually turned off or Airplane Mode); it is not necessary to show an alert, but it is useful to discreetly warn that changes will not be available on other devices until access is restored.
- Also use iCloud to store app settings and state, such as the last page read in a magazine app, as long as they are adjustments the person wants applied across all devices (not every setting fits, for example settings that are more useful at work than at home).
- Warn about the consequences of deleting a document, since deletion removes the document from iCloud and from all other devices too; show a warning and ask for confirmation before deleting.
- Make conflict resolution quick and easy, trying to detect and resolve version conflicts automatically; when that is not possible, show a discreet notification that makes it easy to tell apart and choose between the conflicting versions, ideally as early as possible.
- Include iCloud content in search results, since people expect their content to be universally available.
- In games, consider saving the player's progress to iCloud, using the GameSave framework, which syncs data across devices and offers native alerts to handle offline sync or conflicts.

Exact specifications: the text does not give numbers, measurements or proportions.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: no cross-reference to another HIG article cited in the text (only CloudKit and GameSave developer documentation).

<!-- visual:icloud -->
### What the illustrations show
Basis: 1 illustration sheet viewed (img 0560), code checked; no video.
- The opening symbol is a cloud in a thick, hollow dark blue outline, with no fill, over a blue gradient background (img 0560).
- The overlaid construction grid combines horizontal, vertical and diagonal lines with a centered dashed circle, tangent to the base of the cloud, which appears to dictate the curvature of the larger lobe on the right (img 0560).
- The page does not illustrate a sync screen, version conflict, offline state or search; the only visual material confirms the sketch of the blue-tinted icon officially described (img 0560).
<!-- /visual:icloud -->

## ID Verifier (slug: id-verifier)

What it governs: how an iPhone app can use ID Verifier to read mobile IDs compliant with ISO 18013-5 in person, with no external hardware, for identity or age verification.

Why: Apple structures ID Verifier around data minimization and trust: the person being verified only presents the minimum data necessary to prove age or identity, without handing over the physical card or showing their own device, and Apple provides the key components for issuing, managing and validating certificates to ensure consistency and reliability across the whole experience. This justifies the split between two types of request (Display Only and Data Transfer): when the app only needs to visually confirm something, the data is not even transmitted to the app, preserving privacy; only when there is a legal requirement for verification is it justified to request (and store) data such as address or date of birth.

Do and avoid:
- Ask only for the data necessary to complete the current verification; for example, to check a minimum age, use an age threshold request instead of asking for the person's exact age or date of birth.
- If the app qualifies for the Apple Business Register, register for ID Verifier, so that the organization's official name and logo appear in the verification UI shown on the customer's device.
- Provide a button that starts the verification process with a clear label such as "Verify Age" (for a simple age check) or "Verify Identity" (for a more detailed identity request); avoid including symbols that suggest a specific type of communication such as NFC or QR code, and never include the Apple logo in the button's label.
- In a Display Only request, help the person using the app give feedback on the visual confirmation they perform, for example with "Matches Person" and "Doesn't Match Person" buttons so the app receives an approved or rejected value as part of the response.

Exact specifications: the text does not give numbers of points, pixels, durations or proportions; the only formal technical reference cited is compliance with the ISO 18013-5 standard.

Platform differences: no additional considerations for iOS. Not supported on iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: "Apple Business Register", "IDs in Wallet", "Identity verification".

<!-- visual:id-verifier -->
### What the illustrations show
Basis: 1 sheet viewed with 3 illustrations (img 0625 to 0627), all codes checked; the sheet's fourth quadrant was empty, with no image or code; no video.
- The opening illustration is a stylized identity card, a rounded rectangle with a generic portrait on the left and horizontal lines of text on the right, from which growing curved waves emerge in the bottom right corner, suggesting contactless reading (img 0625).
- The opening drawing is built on a double grid, straight dotted lines and concentric circles, with a gradient from darker to lighter blue (img 0625).
- The button to start age verification is a rounded-corner rectangle in solid black, with a centered white label, isolated on white and with no icon or additional element (img 0626).
- The version for verifying identity repeats the color, height and corner radius and is only wider to accommodate the larger label, that is, the button's width follows the text while the other measurements stay fixed between the variations (img 0626, 0627).
<!-- /visual:id-verifier -->

## iMessage apps and stickers (slug: imessage-apps-and-stickers)

What it governs: how to create an iMessage app (to share content, collaborate or play within a conversation) and sticker packs (stickers), including exact specifications for icon and sticker size.

Why: Apple's reasoning is that people are in a conversational flow when they open an iMessage app, so the functionality needs to be understood and usable immediately, without requiring a learning curve; hence the recommendation to keep one primary experience per app, rather than accumulating multiple functions that compete for attention in an already fast and informal messaging context.

Do and avoid:
- Prefer offering one primary experience per iMessage app; for multiple types of functionality or distinct content collections, consider creating a separate app for each.
- Consider bringing content from the main iOS/iPadOS app into the iMessage app, such as a shopping list or a trip itinerary, or supporting a simple collaborative task.
- Present the essential functionality in the compact view, which appears below the message transcript; reserve additional content and features for the expanded view.
- In general, allow text editing only in the expanded view, since the compact view occupies approximately the same space as the keyboard; display the keyboard in the expanded view to keep the app's content visible during editing.
- Create stickers that are expressive, inclusive and versatile, legible against a wide variety of backgrounds and when rotated or scaled; use transparency to help visually integrate the sticker with text, photos and other stickers.
- Provide a localized alternative description for each sticker, so VoiceOver can speak it.

Exact specifications:
- iMessage app/sticker pack icon sizes (provided with square corners; the system automatically applies a rounded corner mask):
  - Messages, notifications: 148x110 px at @2x (cited equivalent of 143x100, 120x90 at @2x / 180x135 at @3x, 64x48 at @2x / 96x72 at @3x, 54x40 at @2x / 81x60 at @3x, the table lists multiple usage rows with no clear individual label beyond the first).
  - Settings: 58x58 px at @2x, 87x87 px at @3x.
  - App Store: 1024x1024 px at @2x and at @3x.
- Messages supports three sticker sizes: small, regular and large; do not mix sizes within the same pack.
- Sticker dimensions at @3x (the system generates @2x and @1x by downscaling at runtime):
  - Small: 300x300 px
  - Regular: 408x408 px
  - Large: 618x618 px
- A sticker file must be at most 500 KB.
- Supported formats and their capabilities: PNG (8-bit transparency, no animation), APNG (8-bit transparency, with animation), GIF (single-color transparency, with animation), JPEG (no transparency, no animation).

Platform differences: no additional considerations for iOS or iPadOS. Not supported on macOS, tvOS, visionOS or watchOS.

Links to other articles: "iMessage Apps and Stickers" (related resources link).

<!-- visual:imessage-apps-and-stickers -->
### What the illustrations show
Basis: 1 illustration sheet viewed (img 0634 to 0637), all codes checked; no video.
- The opening illustration is an oval shape in a darker blue with the App Store logo, the letter A drawn as a compass, in the center, over a blue gradient with a grid of dotted lines in an X pattern and concentric circles (img 0634).
- The sticker is shown inside the actual conversation: the iMessage typing bar with a plus button and microphone at the top and, below, the sticker panel with a row of category icons above the grid (img 0635 to 0637).
- At the small size the grid has four stickers per row, with two complete rows and a third cut off at the bottom edge of the screen (img 0635).
- At the regular size the same characters are visibly larger and the grid drops to three per row, with two complete rows visible (img 0636).
- At the large size the grid has only two stickers per row, with one complete row and the start of the next one cut off at the bottom edge (img 0637).
- The three captures keep the iMessage bar, the plus button, the microphone and the category panel identical, and vary the number of columns, from four to three and to two, as the sticker grows, within the same fixed panel width at the bottom of the iPhone screen (img 0635, 0636, 0637).
<!-- /visual:imessage-apps-and-stickers -->

## In-app purchase (slug: in-app-purchase)

What it governs: how to design the in-app purchase experience (in-app purchase) for virtual goods (consumables, non-consumables, auto-renewable subscriptions and non-renewing subscriptions), including support for Family Sharing, the refund flow, subscription sign-up and subscription management.

Why: the central logic is to clearly differentiate in-app purchase from Apple Pay by the type of good sold (virtual versus physical/service), and then ensure that the whole purchase journey is self-contained and visually integrated into the app, without making the person feel like they "left" the app to buy. There is also a strong emphasis on price and terms transparency (always showing the total billing amount, clearly explaining how a free trial period works) and on never making cancellation difficult, reflecting Apple's concern with preventing accidental purchases and the subscriber's long-term trust.

Do and avoid:
- Use in-app purchase for virtual goods (premium content, digital goods, subscriptions); use Apple Pay for physical goods, services (club memberships, hotel reservations, tickets) and donations.
- Let the person try the app before buying; consider supporting limited free access if you offer auto-renewable subscriptions.
- Design a purchase experience that is visually integrated with the style of the rest of the app.
- Use simple, succinct product names and descriptions that do not truncate or wrap.
- Display the total billing price for each in-app purchase, regardless of type.
- Display the store only when the person can actually pay (for example, hide it or explain when there are parental restrictions).
- Use the system's standard confirmation sheet when starting a purchase; do not modify or replicate that sheet.
- Mention Family Sharing prominently where people learn about the content offered, including the term "Family" or "Shareable" in the item name when applicable.
- Help people understand the benefits and how to take part in Family Sharing.
- Customize the app's messages to make sense both for whoever bought it and for family members who receive shared access.
- Offer a custom help screen that people can consult before requesting a refund, with a link to the system's refund flow, answers to frequently asked questions and ways to make contact.
- Use a simple title for the refund action, such as "Refund" or "Request a Refund"; the system flow already makes clear that the request is made to Apple.
- Help the person find the purchase with the problem, showing the image, name, description and purchase date of each recent item.
- Consider offering alternative solutions to a refund (for example immediate fulfillment of the item or a compensation item), always making clear that it is still possible to request a refund.
- Make it easy to request a refund; avoid requiring scrolling or opening another screen before revealing the refund request button.
- Avoid characterizing or giving guidance about Apple's refund policies; do not speculate on whether the customer will receive the requested refund.
- Call attention to the subscription's benefits during onboarding, with a strong call to action and a clear summary of the subscription terms.
- Offer a variety of content options, service levels and durations.
- Consider allowing a free trial of the content before subscribing (freemium app, metered paywall or free trial).
- Prompt for subscription at relevant moments, such as when the person approaches the monthly limit of free content.
- Encourage a new subscription only when the person is not yet a subscriber; if the same service is available in multiple apps or on the website, offer a login option to avoid duplicate billing.
- Offer clear, distinguishable subscription options, with short, self-explanatory names, specifying the price and duration of each option; if there is an introductory price, clearly list the duration of the offer and the standard price after it ends.
- Simplify the initial sign-up by asking only for the necessary information; defer requests for additional information until after sign-up.
- In the tvOS app, help people sign up or authenticate using another device, instead of asking them to type information on Apple TV.
- On the app's sign-up screen, include: the name, duration and content/services of each subscription period; the billing amount correctly localized by territory and currency; and a way for existing subscribers to sign in or restore purchases.
- Clearly describe how the free trial period works, making explicit that at the end a payment will automatically start for the next subscription period.
- Include a subscription opportunity in the app's settings.
- For custom offer codes (custom code), use only ASCII alphanumeric characters; do not use special characters, including Chinese and Arabic characters.
- Explain to users how to redeem a custom code, since it cannot be redeemed directly in the App Store account settings.
- Consider supporting in-app offer redemption using the system-provided redemption screens; the only custom UI needed is the one that starts the system flow.
- Provide an engaging, informative promotional image for the redemption code; if you do not provide one, the screens use the app icon by default.
- Help the person benefit from the unlocked content as soon as they complete the redemption flow, including someone who subscribes even before opening the app for the first time.
- Provide summaries of the person's subscriptions, including the upcoming renewal date, ideally near the subscription management option.
- Consider using the system-provided subscription management UI (StoreKit) for a consistent experience without leaving the app.
- Consider ways to encourage the person to keep the subscription or resubscribe later, such as a personalized offer as an alternative to cancellation or an exit survey.
- Always make it easy to cancel an auto-renewable subscription; if the manage subscription action is hidden or hard to recognize, subscribers may feel they are being discouraged or prevented from canceling.
- Consider creating a contextual branded experience that complements the system's management UI, such as offering a popular premium tier or personalized suggestions.

Exact specifications: the text gives examples of prices in illustrative context, not as normative rules (for example, an example of an annual plan of $29.99/year with a 1 week free trial and 50% savings over the monthly plan of $4.99/month; another example of $14.99/month for "Intrepid Pro"; another of $9.99/month for "Intrepid Pro with Ads"). Family Sharing allows sharing with up to five additional family members. The text does not define any interface measurement value (pt, px, ms) as a mandatory rule.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS or visionOS.
watchOS: the sign-up screen in the watchOS app needs to display the same set of mandatory information about subscription options as the other versions of the app. Make clear the differences between the app versions on different devices, without suggesting that the experience is identical. Consider using a modal sheet to present all the mandatory information in a single view, since it includes a standard close button. Make the subscription options easy to compare on a small screen, for example by displaying each option in a separate button (to start sign-up with a single tap) or a list of options followed by a single button whose title updates to reflect the chosen option.

Links to other articles: "In-app purchase" and "Auto-renewable subscriptions" (marketing and business), "App Review Guidelines", "Onboarding" (for calling attention during onboarding).

<!-- visual:in-app-purchase -->
### What the illustrations show
Basis: 6 illustration sheets viewed (img 0644 to 0666), all codes checked; no video.
- The opening symbol is a square app icon with rounded corners, in blue, with a thick plus sign in the center, over a horizontal, vertical and diagonal dotted grid with a concentric circle marking the center and the axes of symmetry (img 0644).
- The in-game store, on iPad, sits over an olive green background with a drawn map: two thematic rows of circular items with colorful illustration, name below and price in a gray capsule, with very different values coexisting in the same grid (img 0645).
- The help before the refund uses a translucent navy blue palette: a list of five options in a single capsule with thin dividers and chevrons (img 0646); the refund request screen has the back button labeled with the name of the previous screen and lists each purchase with thumbnail, name and date in blue (img 0647).
- The system refund sheet shows icon, name, price and date of the item and the Apple account, a simple list of reasons with only dividers, the chosen one marked with a blue check, a warning about loss of access and the blue button at the bottom (img 0648); the confirmation brings a large centered blue check, title, email response deadline and blue done button (img 0649).
- The subscription onboarding places a benefit card in the lower half over a darkened themed photo, with pagination dots, a button with the detailed price inside it and the sign-in link below (img 0650); the same composition reappears only with the button highlighted by a light blue outline and the rest dimmed (img 0653), and the resubscribe offer repeats the pattern over an illustrated turquoise background, with a white button in two levels of text (img 0662).
- In the plan choice, two stacked cards function as radio options: the annual one selected with a filled red circle and a savings badge, the monthly one with an empty circle; terms repeated in footer text, red free trial button and close in the top right corner (img 0651).
- The free content limit is applied by overlay: the article stays behind with reduced opacity and on top are the limit message, a purple pill button to view options and the link for those who already subscribe (img 0652).
- On the sign-up screen with two plans, the two paid options are green pill buttons with name and monthly price, and code redemption sits below as a plain text link, without button form (img 0654); in the codes section the same screen highlights that link with a solid black capsule and dims the green buttons (img 0656).
- In settings, the subscription block brings together icon, name, plan, price and next billing, and the actions to manage, restore and redeem sit outside the block as stacked blue links with no icon (img 0657); the management screen repeats the block, lists the duration options with a check on the current one, puts cancellation as a centered red link with a renewal warning in gray (img 0660) and confirms the cancellation in a central alert with two buttons side by side, the confirm one in blue (img 0661).
- The code redemption screen appears as a wireframe inside an iPhone frame, in placeholder gray with no brand color: dashed icon area, bold title, empty code field and terms link at the bottom (img 0658); the named offer variant, also in an iPhone frame, swaps the icon for a larger placeholder photo with a small dashed icon in the bottom left corner and adds price in small text and a solid blue redeem button (img 0659).
- On Apple Watch sign-up is a single column: close link at the top, blue title, description, full-width blue button and terms below (img 0655); the pair of texts compares a description with no subscribe button, with the title cut off outside the frame, that does not separate what runs on the watch (img 0663), with the green title rewrite that distinguishes the Watch feature from the maps used on iPhone and other devices (img 0664).
- The price on Watch is resolved in two ways: each option as its own full-width red pill button, with the savings in small text outside the buttons (img 0665), or a list in a single card with a gray uppercase title, the chosen option with a green check and a full-width red button below that shows the selected plan (img 0666).
Recorded divergences: the official caption of img 0654 mentions three images at the top, but the screen shows one forest photo at a time with a three-dot indicator, like a carousel.
<!-- /visual:in-app-purchase -->

## Live Photos (slug: live-photos)

What it governs: how an app should handle, display, edit and share Live Photos, which capture audio content and extra frames before and after the photo.

Why: the guiding principle is consistency: people need to experience Live Photos in the same visual and interaction way across all apps, so the text explicitly forbids taking the Live Photo apart into its components (separate frames, isolated audio) and requires that any edit applied affect the entire content, not just the static frame, preserving the expectation that a "Live Photo" is always a cohesive experience of motion and sound.

Do and avoid:
- Apply adjustments or effects to all frames of the Live Photo; if this is not supported, offer the option to convert to a static photo.
- Keep the Live Photo content intact; do not take the Live Photo apart or present its frames or audio separately.
- Implement a good photo sharing experience: let the person preview the complete content of the Live Photo before deciding to share, and always offer the option to share as a traditional photo.
- Clearly indicate when a Live Photo is being downloaded and when it is ready for playback, with a progress indicator during the download.
- In environments that do not support Live Photos, display the photo as a traditional static photo; do not try to replicate the Live Photos experience.
- Make Live Photos easily distinguishable from static photos, ideally by a subtle motion effect; since there is no built-in motion effect outside the full-screen browser of the Photos app, custom motion effects need to be designed and implemented.
- When motion is not possible, show the badge provided by the system, with or without text; never include a playback button that could be interpreted as a video button.
- Keep the badge placement consistent, typically in a corner of the photo, always in the same location across all photos.

Exact specifications: the text does not give measurement, size, duration or proportion numbers.

Platform differences: no additional considerations for iOS, iPadOS, macOS or tvOS. Not supported on watchOS.
visionOS: on visionOS, people can view a Live Photo, but cannot capture it.

Links to other articles: no explicit cross-reference to another HIG article (only PHLivePhoto and LivePhotosKit JS developer documentation).

<!-- visual:live-photos -->
### What the illustrations show
Basis: 1 illustration sheet viewed (img 0728 to 0730), all codes checked; no video.
- The opening symbol is a double concentric circle, a thick dark blue ring with a hollow center, surrounded by a crown of dots, over a horizontal, vertical and diagonal dashed grid that passes through the center, with a guide rectangle; the design rests on radial symmetry axes (img 0728).
- The badge with text is applied over a real night photo of a lake and mountains: a rounded white badge in the top left corner, with the blue Live Photo icon and the word LIVE in blue next to it, the semi-transparent white background contrasting with the dark scene (img 0729).
- The badge without text uses the same photo and the same corner, now as a small white circle with only the icon; the only difference from the previous image is the absence of the label, with icon, size and position kept (img 0729, 0730).
- The page does not illustrate a motion effect, download progress or sharing screen; the visual material is limited to the icon and the two badge variants (img 0728 to 0730).
<!-- /visual:live-photos -->

## Mac Catalyst (slug: mac-catalyst)

What it governs: how to transform an iPad app into a Mac app using Mac Catalyst, including the choice between the iPad idiom and the Mac idiom, and how to adapt navigation, input, icons, layout and menus for the macOS platform.

Why: the central principle is that a good iPad app is a good foundation, but it is not enough: transforming it into a Mac app requires going beyond simply displaying the iPadOS layout inside a macOS window. iPadOS and macOS define different patterns and conventions, rooted in different ways people use their devices (touch versus keyboard and mouse), so the text guides auditing each dimension of the experience (navigation, input, icons, layout, menus) and adapting it to native Mac conventions instead of porting directly.

Do and avoid:
- Evaluate whether the app is a good candidate for Mac Catalyst by checking whether it already supports key iPad features well: drag and drop, keyboard navigation and shortcuts, multitasking (Split View, Slide Over, Picture in Picture) and multiple windows (multiple scenes on iPad).
- Recognize that apps that depend on features that do not exist on Mac (gyroscope, accelerometer, rear camera, frameworks like HealthKit or ARKit) or whose primary function is something like markup, handwriting or navigation may not be suitable for Mac.
- When building the app with the iPad idiom ("Scale Interface to Match iPad"), know that text and graphics may look less detailed, since iPadOS views and text are scaled down on macOS.
- Consider switching to the Mac idiom when the app is already working well on Mac with the iPad idiom; this renders text and artwork with more detail, gives a more native appearance to some elements and views, and can improve performance and reduce energy consumption in graphics-intensive apps.
- The app that benefits most from the Mac idiom is one that displays a lot of text, detailed artwork or animations; but this choice requires more time updating the layout, text and images of the Mac app.
- When adopting the Mac idiom, fully audit the app layout and plan changes; consider using a separate asset catalog for the Mac app instead of reusing the iPad app's catalog.
- Adjust font sizes as needed; use text styles instead of fixed font sizes when possible, since with the Mac idiom text renders at 100% of the configured size.
- Make sure views and images look good in the Mac version, since with the Mac idiom the iPadOS views render at 100% of size, appearing more detailed.
- Limit appearance customizations to the standard macOS customizations that are the same as or similar to those available on iPadOS; not every iPadOS control customization is available for macOS controls.
- If the iPad app uses a tab bar, consider using a split view with a sidebar or a segmented control on Mac, which are closer to macOS navigation conventions.
- Prefer a split view with a sidebar over a tab bar in general; a segmented control works well if the app uses a flat navigation hierarchy.
- Make sure people keep access to important tab bar items in the Mac version, by listing them in the macOS View menu.
- Offer multiple ways to navigate between pages: Next and Previous buttons in addition to swipe gestures, since Mac users (especially with a pointing device or keyboard only) appreciate this option.
- Know that most iPadOS gestures automatically convert to mouse and trackpad interactions when building the Mac app (tap becomes left or right click; touch and hold becomes click and hold; pan becomes click and drag; pinch and rotate stay on trackpad).
- Create a macOS version of the app icon, that shows the realistic rendering style people expect on macOS while keeping harmony across platforms.
- To take advantage of the Mac's wider screen: split a single column of content and actions into multiple columns; use the regular-width and regular-height size classes, rearranging elements side by side when resizing the window; present inspector UI next to the main content instead of using a popover.
- Consider moving controls from the iPad app's main UI to the Mac app's toolbar, listing the associated commands in the menu bar's menus.
- Adopt a top-down flow (top-down); Mac apps place the most important actions and content near the top of the window.
- Relocate buttons from the side and bottom edges of the screen, since on Mac this ergonomic consideration does not apply as it does on iPad.
- For keyboard shortcuts of menu commands, use UIKeyCommand.
- Know that pop-up or pull-down buttons that reveal a menu in the iPad app automatically take on macOS appearance in the Mac Catalyst app.
- To add and remove custom menus, use UIMenuBuilder and UICommand.
- Know that the system automatically converts the iPad app's context menus into context menus in the macOS app; consider looking for additional places to support context menus, since Mac users tend to expect every object in the app to offer a context menu of relevant actions (on Mac, this menu is sometimes called a "contextual menu").

Exact specifications: iPadOS text that uses the base font size of 17pt is scaled down to 13pt on macOS when using the iPad idiom (scale factor of 77%). In the Mac idiom, text and views render at 100% of the configured size.

Platform differences: no additional considerations for iPadOS or macOS. Not supported on iOS, tvOS, visionOS or watchOS. (This article is entirely about the iPadOS/macOS relationship via Mac Catalyst.)

Links to other articles: "Designing for macOS" (to understand the characteristics that distinguish the Mac experience).

<!-- visual:mac-catalyst -->
### What the illustrations show
Basis: 1 illustration sheet viewed (img 0739 to 0741), all codes checked; no video.
- The opening literally overlaps two device frames instead of a single symbol: behind, the outline of a laptop with a horizontal base and a thick vertical column on the left; in front, a tablet's rounded rectangle with a short stroke at the base, with a guide circle concentric to the tablet and a dashed horizontal, vertical and diagonal grid (img 0739).
- The iPad idiom is represented by the pixelated icon of a building with three arches and columns, in beige and gray, occupying the full width of the frame with no margin, with large, coarse pixel blocks that indicate less detail (img 0740).
- The Mac idiom uses the same icon centered with visible white margin above and below, occupying a smaller area, with proportionally smaller and more numerous pixel blocks and an impression of more sharpness (img 0741).
- The comparison pair carries no grid, numeric annotation or text over the images; the difference between the idioms is shown only by the framing of the same drawing, filling the frame or with a margin, and by the relative size of the pixel blocks (img 0740, 0741).
<!-- /visual:mac-catalyst -->

## Machine learning (slug: machine-learning)

What it governs: how to plan, design and communicate app or game features that use machine learning, including how to classify the role of machine learning in the product, how to collect and use feedback (explicit and implicit), how to conduct calibration, how to handle errors, corrections, multiple options, confidence, attribution and limitations.

Why: the central reasoning is that a machine learning app cannot be designed as fixed reactions to a static set of scenarios, because its behavior depends on the data received; therefore, design consists of teaching the app to interpret data and react, and the UI experience needs to be built around axes that define how much people tolerate error and lack of precision: whether the feature is critical or complementary, whether it handles private or public data, whether it is proactive or reactive, whether it is visible or invisible, whether it improves dynamically or statically. Each axis changes the expectation of reliability and the level of error tolerance people will have, which in turn determines how much to invest in feedback, calibration, corrections and confidence communication.

Do and avoid (planning and the role of machine learning):
- When designing the models, keep the app's intended experience in mind; be prepared to change how you use data and metrics if the app's experience needs to change, since adjusting model behavior can take a long time.
- Define the role of machine learning in the app (critical or complementary) to discover where it can affect the experience.
- The more central the feature is to the app's purpose, the greater the expectation of precise and reliable results; for secondary features, people tend to be more tolerant of inaccuracies.
- The more sensitive the data used, the more serious the consequences of an imprecise or unreliable result; features that handle sensitive data should prioritize precision and reliability, and all apps should protect the user's privacy at all times.
- Proactive features (that deliver a result without the person asking) tend to have less tolerance for low-quality results, because the person didn't ask for that result; it may be necessary to use additional data to reduce the chance of seeming intrusive or irrelevant.
- Visible features let people form an opinion about reliability by choosing among results; invisible features have more difficulty communicating reliability and receiving feedback, because the person may not even know the feature exists.

Do and avoid (explicit feedback):
- Ask for explicit feedback only when necessary, since it requires the person to take an action; prefer using implicit feedback when possible.
- Always make providing explicit feedback a voluntary task, communicating that it helps improve the experience without seeming mandatory.
- Use simple, direct language to describe each explicit feedback option and its consequences; avoid imprecise terms like "dislike", which don't communicate consequence and are hard to translate (prefer something like "Suggest less pop music", "Suggest more thrillers", "Mute politics for a week").
- Add icons to an option's description if it helps understand it; avoid using an icon alone, since it may not communicate granularity or consequence clearly.
- Consider offering multiple options when asking for explicit feedback, giving a sense of control and helping identify unwanted suggestions, progressing from more general to more specific options.
- Act immediately when receiving explicit feedback and persist the resulting change, for example hiding unwanted content throughout the app; this builds confidence that the feedback has value.
- Consider using explicit feedback to help decide when and where to show results, since the person may like a result but not want to see it in certain moments or contexts.

Do and avoid (implicit feedback):
- Always protect people's information, since implicit feedback can collect potentially sensitive data.
- Help the person control their information; explain how the app obtains and shares data, and offer ways to restrict that flow, since people may be startled to see that actions in one app affect experiences in another app, or even suspect improper sharing.
- Don't let implicit feedback reduce the person's opportunities for exploration; it reinforces existing behavior, which can worsen the experience in the long run even while improving it in the short run.
- When possible, use multiple feedback signals to improve suggestions and mitigate errors, since implicit feedback is indirect and it can be difficult to discern the person's real intent (for example, viewing, sharing and saving a photo doesn't necessarily mean positive sentiment about it).
- Consider withholding private or sensitive suggestions when the app receives implicit feedback related to private topics, since people share accounts and devices.
- Prioritize recent feedback, since tastes change frequently; fall back to historical feedback if recent feedback isn't available.
- Use feedback to update predictions at a pace that matches the person's mental model of the feature (typing suggestions should update immediately; continuous and frequent music recommendations can feel rushed or overwhelming).
- Be prepared for changes in implicit feedback when you change the app's UI, since even small changes (like moving a button) can alter the volume and type of feedback received.
- Watch out for confirmation bias: implicit feedback is limited to what the person can see and do in the app and in other apps, rarely revealing new things they might like; avoid relying on it alone.

Do and avoid (calibration):
- Use calibration only when the feature can't function without that initial information; if the feature can function without calibration, consider obtaining the information implicitly or explicitly.
- Always protect the information provided during calibration, which can be sensitive.
- Be clear about why you need the person's information, emphasizing what the feature does rather than how it works.
- Collect only the most essential information, making the experience more comfortable and increasing trust.
- Avoid asking the person to take part in calibration more than once; ideally calibration happens early in the experience, and after that use implicit or explicit feedback to evolve the information without asking for calibration again (except when calibration needs to be done with a new object rather than a person).
- Make calibration quick and easy: prioritize obtaining a few important pieces of data and infer the rest from other sources or feedback; avoid asking for information that most people would have to look up; avoid asking for actions that are difficult to perform.
- Make it clear how to complete calibration successfully, giving an explicit goal and showing progress toward it.
- Provide assistance immediately if progress stalls, with actionable recommendations, without implying that something is wrong or that the person is at fault, and without leaving them without a clear next step.
- Confirm calibration's success as soon as it's complete, giving a clear path to using the feature.
- Let the person cancel calibration at any time, without implying judgment about the choice; there's no need to mention the cancellation afterward, since on the next attempt the person will get a new chance.
- Give the person a way to update or remove information provided during calibration, ideally also outside the calibration experience itself.

Do and avoid (mistakes, corrections, multiple options, confidence, attribution, limitations):
- Anticipate errors, help people deal with them, and learn from them when it improves the app (in some cases, learning from an error can have unwanted effects, like causing unpredictability in the experience).
- Understand the severity of an error's consequence (a wrong keyboard suggestion is annoying; suggesting a route that causes a missed flight is serious) and provide corrective actions or tools proportional to the severity.
- Make it easy to correct frequent or predictable errors; without this, people may lose confidence in the app.
- Continuously update the feature to reflect evolving interests and preferences, and update it with domain-specific information (like current trends).
- When possible, resolve errors without complicating the UI; balance the effect of a UI pattern with its potential to worsen the error (a wrong attribution, for example, amplifies the effect of the original error).
- Be especially careful to avoid errors in proactive features, since people have less patience for errors in something they didn't ask for, and may feel they have less control.
- When reducing errors in one area, always consider the effect on other areas and on overall precision (optimizing dog recognition can worsen cat recognition).
- Give familiar, easy ways to make corrections, showing the steps the app took in the automated task, so the person can use the same controls to refine or undo the result.
- Provide immediate value when the person makes a correction, displaying the corrected content instantly and persisting the update.
- Let the person correct their own corrections, responding immediately and persisting the update.
- Always balance a feature's benefit against the effort required to correct it; if correcting feels more work than doing it manually, people stop using the feature.
- Never rely on corrections to make up for low-quality results, since this can erode trust and reduce the feature's value.
- Learn from corrections when it makes sense, first verifying that the correction will in fact lead to higher-quality results.
- When possible, use guided corrections (which suggest specific alternatives, requiring less effort) instead of freeform corrections; an app can support a combination of both.
- Prefer diverse options when presenting multiple results, balancing precision with the diversity of options.
- In general, avoid offering too many options, since more options increase cognitive load; when possible, list options on a single screen without requiring scrolling.
- List the most likely option first when confidence values correlate with the quality of results; consider using contextual information (time of day, location) to determine the most likely option, and select the first option by default if it makes sense.
- Make options easy to distinguish and choose, with brief descriptions that highlight the differences; group options into categories when there are too many to display in a single view.
- Learn from selections when it makes sense, using the implicit feedback of choice to refine the options offered and increase the chance of presenting the most likely option first; continuing to offer incorrect results tends to reduce people's confidence.
- Verify that confidence values actually correspond to the quality of results before deciding how to present them (for example, reviewing multiple confidence thresholds or comparing across app versions); if you're not sure of the correlation, it's not a good idea to convey confidence to people.
- Translate confidence values into concepts people already understand, instead of simply displaying a number (for example, an attribution like "Because you listen to pop music" is more actionable than "97% match").
- In situations where attributions don't help, consider ordering results in a way that implies confidence level; if you need to display confidence directly, consider semantic categories (like "high chance", "low chance") instead of raw numbers.
- In scenarios where people expect statistical or numerical information (weather forecasts, sports statistics, election polls), display confidence values that help interpret the results, like a range or percentage.
- Whenever possible, help people decide by conveying confidence in terms of actionable suggestions (for example "This is a good time to buy" instead of displaying a percentage).
- Consider changing how results are presented according to different confidence thresholds, adapting the presentation when the confidence level has a significant impact on the experience (for example, Photos directly shows a person's photos when confidence is high, but asks for confirmation when confidence is lower).
- When confidence values actually correspond to the quality of the result, generally avoid showing results when confidence is low; for proactive features, set a confidence threshold below which you do not offer results.
- Consider using attributions (attribution) to explain the basis or the reasoning behind a result, without explaining exactly how the model works; use it to encourage behavior change, minimize the impact of errors, help build a mental model of the feature, or promote trust over time.
- Avoid being too specific or too generic in an attribution; attributions that are too specific make the person feel like they are being watched too closely, and attributions that are too generic feel unpersonalized.
- Keep attributions factual and based on objective analysis; do not imply understanding or judgment of the person's emotions, preferences or beliefs (prefer "Because you've read nonfiction" over "Because you love nonfiction").
- In general, avoid technical or statistical jargon in attributions, except when the result itself is statistical or technical in nature (weather, sports, elections, scientific data).
- Identify the scenarios where the feature's limitations impact the experience and design ways to handle them: set expectations before use, show how to get the best results during use, and explain the reason when the result is inferior.
- Help set realistic expectations, describing the limitation in marketing material or in the feature's own context when the effect can be serious but rare.
- Demonstrate how to get the best results, for example with placeholder text that suggests the type of input, real-time feedback as the person interacts, or a suggestion of alternative ways to reach the goal.
- Explain how limitations can cause unsatisfactory results, so the person adjusts their expectations (for example, Memoji warns that it does not work well in the dark).
- Consider notifying when limitations are resolved, so the person adjusts their mental model of the feature and goes back to using interactions they previously avoided.

Exact specifications: there are no measurement, size or duration numbers in the text; the only numeric value cited is the illustrative example of "97% match" used to explain why displaying the raw percentage is not effective communication.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

Links to other articles: "Generative AI" (for guidance related to using machine learning models in intelligent experiences), "Privacy", "Create ML" and "Core ML" (developer documentation), "Onboarding" not cited here but relevant to the group's general context.

<!-- visual:machine-learning -->
### What the illustrations show
Basis: 3 of 3 illustration sheets opened, all codes checked; the page has no video.
- The opening uses three four-pointed stars (sparkles) in different sizes over a blue gradient, with a horizontal, vertical and diagonal dashed grid and a central guide circle; the points cross the circle, which works as a scale reference and not as the outline of each shape (img 0742).
- Explicit feedback appears inside a floating, standard white context menu, over a gray iPhone with no app color: four generic gray lines at the top and, below a divider, two options with text and icon ("Love" with a heart, "Suggest Less Like This" with a thumbs down), that is, alongside the other actions and not in a separate control (img 0743).
- Implicit feedback becomes a notification on Apple Watch over a black background, with the phrase "It looks like you're working out." and two large buttons below the text: the most likely option in vivid lime green and the alternative in dark gray (img 0744).
- Calibration is a full-screen flow on a black background: a schematic face inside a dotted circle, a title with instructions to position and turn the head, and a single blue "Get Started" button at the bottom (img 0745).
- Correction is shown as a manual tool over an automatic result: crop and straighten mode with handles on the four edges of the photo, a tilt wheel at the bottom with the indicator slightly off center, rotate, mirror and grid icons above it, and "AUTO" highlighted in yellow in the top bar (img 0746).
- Multiple options appear at the same time in two views: three blue routes on the map, each with a time label, and an "Options" side panel listing time and distance, with the first route selected in blue as the fastest (img 0747).
- Confidence is communicated in natural language and not in a number: a flights app with a light purple header shows "Keep waiting." in purple, the current lowest price and the estimated savings, followed by a button hierarchy with "Track" filled in purple, "View Flights" outlined and "Find New Dates" below (img 0748).
- The attribution is a subtitle line right below the "For You" section title (with a navigation arrow), above a row of cards with a video camera icon, where the third one is cut off at the right edge of the frame (img 0749).
- The limitation is flagged by a small gray "Low light" pill overlaid on the bottom of the dotted yellow facial-tracking outline, in the capture frame itself, with no modal alert; below is the Memoji and Animoji grid with the current item outlined and the "+" option to create another (img 0750).
Recorded divergences: in img 0745 the official alt text talks about a face, but the drawing is a schematic smiling face, not a photo. In img 0750 the "Low light" label is more subtle than the description suggests, a small pill and not large centered text.
<!-- /visual:machine-learning -->

## Maps (slug: maps)

What it governs: how to incorporate an interactive map (outdoor or indoor) into the app or site, including visual style, custom information about the map (annotations, overlays), place cards and indoor maps.

Why: the central principle is functional familiarity: a map in a third-party app must support the same basic interactions that people already expect from the system's Maps app (zoom, pan, rotation), so that non-interactive elements that obscure the map do not frustrate that expectation. There is also a legal and brand concern with the visibility of the Apple logo and the legal link, which must remain visible and fixed relative to the map, and a legibility concern in scenarios with high information density, addressed by clustering points of interest and by progressive levels of detail as you zoom.

Do and avoid:
- In general, make the map interactive; non-interactive elements that obscure the map can interfere with people's expectations.
- Choose an emphasis style suited to the app's needs: the default style (default), with fully saturated colors, is good for most standard map apps without many custom elements, and keeps visual alignment with the Maps app; the muted style (desaturated) is great when there is a lot of information-rich content that needs to stand out against the map.
- Help people find places on the map, considering a search feature combined with filtering locations by category.
- Clearly identify selected elements, using a distinct style such as outline and color variation.
- Group (cluster) overlapping points of interest to improve map legibility; a cluster uses a single pin to represent multiple nearby points of interest, which progressively expand as you zoom in.
- Help keep the Apple logo and the legal link visible: do not cover them the whole time (covering them temporarily is acceptable); use adequate padding to separate them from the map's edges and from custom controls; avoid having the logo and the link move along with the interface (ideally they should appear fixed to the map); if the custom interface can move relative to the map, use the lowest position of the custom element to determine the placement of the logo and the link.
- Use annotations that match the app's visual style to identify custom points of interest; you can change the color (tint) of the default marker (which has a red hue and a white pin icon) and swap the icon for a string or image, such as a logo; an icon string can contain any character, including Unicode, but should have two to three characters for legibility.
- If you want to display custom information related to standard map features, consider making them independently selectable, since the system treats features provided by Apple (points of interest, territories, physical features) independently from other added annotations.
- Use overlays to define map areas with a specific relationship to the content: the "above roads" level (default) places the overlay above streets but below buildings, trees and other features, useful when you want people to have a sense of what is below the overlay; the "above labels" level places the overlay above streets and labels, hiding everything below, useful for content that is fully abstracted from the map's features or for hiding irrelevant areas.
- Ensure sufficient contrast between custom controls and the map, using a thin stroke or light shadow to make the control stand out, or applying blend modes to the map area.
- Use place cards to display structured, up-to-date information about places, such as hours of operation, phone number and address.
- When displaying place cards directly on the map, choose among the available styles: automatic (the system decides based on the size of the map view), callout (popover style next to the selected place, with a full variant for a large, detailed version and compact for a concise, space-saving version; if not specified, the default is the automatic callout), caption (displays only an "Open in Apple Maps" link) and sheet (displays the place card in a sheet).
- Note that the full callout style place card appears differently depending on the device: in a popover on iPadOS and macOS, and as a sheet on iOS.
- Consider the map's presentation when choosing a place card style; choose a style that fits the context (for example, a small map with many annotations benefits from the compact callout style).
- Make sure the place card looks good on different devices and window sizes; for the full callout style, you can set a minimum width to prevent text from overflowing on smaller devices.
- Avoid duplicating information already displayed elsewhere in the app or site when choosing a place card style.
- Keep the location on the map visible while displaying a place card, helping maintain a sense of where the location is; you can set an offset distance for the place card pointing to the selected location.
- When displaying place cards outside a map (for example in a list of search results), if you do not display the place card directly inside a map view, it is mandatory to include a map inside the place card itself.
- Use location-related cues in the surrounding content to communicate that a place card can be opened, such as displaying the place's name and address next to a more-details button, or including a map pin icon alongside the place's name.
- For indoor maps linked to specific locations such as malls and stadiums, adjust the map's level of detail according to the zoom level, showing large areas such as rooms and buildings at all zoom levels and progressively adding more detail and labels as you zoom in.
- Use a distinct visual style (color and icons) to differentiate the map's features and help people quickly find what they are looking for.
- Offer a floor picker if the location has multiple levels, keeping the floor numbers concise (generally a list of floor numbers instead of names is enough).
- Include surrounding areas to provide context, such as adjacent streets, playgrounds and other nearby locations; if these areas are non-interactive, use dimming and a distinct color so they appear supplementary.
- Consider supporting navigation between the location and nearby transit points (bus, train, parking), also offering the option to quickly switch to the Maps app for more navigation options.
- Limit scrolling outside the location, to help people avoid getting lost when swiping too hard; when possible, keep at least part of the indoor map visible on screen at all times, adjusting the amount of scrolling allowed according to the zoom level.
- Design an indoor map that feels like a natural extension of the app; do not try to replicate the appearance of the Apple Maps app, instead combine area overlays, icons and text with the app's own visual style.

Exact specifications:
- Recommended padding around the Apple logo and the legal link relative to the map edges and custom controls: 7 points on the sides and 10 points above and below the elements.
- When the custom interface can move relative to the map (for example a card that rises from the bottom), position the logo and the link 10 points above the card's lowest resting position.
- The Apple logo and the legal link are not displayed on maps smaller than 200x100 pixels.
- Annotation icon strings should be two to three characters long for legibility.
- On watchOS, you can add up to five annotations to a map.

Platform differences: no additional considerations for iOS, iPadOS, macOS, tvOS or visionOS.
watchOS: on Apple Watch, maps are static snapshots of geographic locations; position a map in the interface at design time and show the appropriate region at runtime. The displayed region is not interactive; tapping it opens the Maps app on Apple Watch. You can add up to five annotations to highlight points of interest or relevant information. Fit the map element to the screen size, so the entire element is visible without requiring scrolling. Show the smallest region that covers the points of interest, since the map element's content does not scroll, so all key content needs to be visible in the displayed region.

Links to other articles: there is no explicit cross-reference to another HIG article cited in the text (only MapKit, MapKit JS and Indoor Mapping Data Format developer documentation).

<!-- visual:maps -->
### What the illustrations show
Basis: 5 of 5 illustration sheets opened, all codes checked; the page has no video.
- The opening draws the map folded into three panels only in a thick dark blue outline, hollow, over a blue gradient with the dashed grid and the construction guide circle (img 0753).
- Standard style and muted style are compared in the same 3D framing of the Coit Tower, with the same buildings, trees, roundabout and photo stamp: only the saturation changes, from vivid green and reddish roof to grayish green and beige; in this comparison, as in the page's other style and platform comparisons, there is no grid or annotation (img 0754, 0755).
- Clustering is a before and after of zooming: a single circular orange pin with a white "3" centered replaces the nearby points (img 0756) and, zooming in, becomes three orange teardrop pins, each with a white cup and a label below (img 0757).
- The place card styles appear over the same map and the same pin, varying only in density: the full callout stacks a header image, a brown circular icon, name, category and rating, an hours block, a website block, phone and address, and ends in the "Open in Apple Maps" button (img 0758); the compact stays anchored just above the pin with name, category and address, rating and the blue link (img 0759); the caption reduces everything to the label under the pin and the blue link alone (img 0760).
- On iPad, the same full callout also appears as a sheet centered over the map, with an X close button in the top right corner of the card (img 0761).
- On iPhone, the full callout is a sheet that rises from the bottom edge and gains its own structure: a row of action buttons with icon (drive time, call, website, order, more), a row of metrics (hours, rating, cost, distance), a details section and the final button to open in Maps; the address appears abbreviated and in blue, while on iPad it came complete in black (img 0762).
- The indoor map starts at the wide city view with the airport marked by a blue square airplane icon and a bottom card with actions and metrics (img 0763); zooming in, the terminal label appears, the blue "Look Inside" link above the icon and the gate numbers in yellow capsules along the corridor, with new map controls on the right (map, location, 3D, compass) (img 0764).
- At the room level, the L-shaped terminal is filled in light pink and labels internal functions with orange markers (cross for first aid, circle for security), while stairs and elevators are in lilac outside the outline, with search at the bottom (img 0765); in an equivalent view, with the map almost all white and fewer elements, a single point appears selected, the elevator, with a blue square icon at the center of the building and a detail card below with the text truncated (img 0766).
- The view returns to outside the terminal: labeled roads, numbered markers in yellow capsules along the road's edge and blue parking in a small gray area, with the streets slightly faded and in a neutral color, contrasting with the vivid green of the grass alongside (img 0767).
- The indoor map of a custom app adopts the app's identity: light green background, buildings in darker green, red circular markers, numbered markers in green capsules, blue current-location pin, search field, bottom list with time to each destination and the app's own green tab bar, keeping the logic of numbered pins and round markers from the standard map (img 0768).
- On Apple Watch, the map is a dark-theme snapshot of Apple Park in 3D, with a white uppercase label, blue location pin and only two floating circular buttons in the bottom right corner (blue with navigation arrow, black with three dots), with no search or list (img 0769).
<!-- /visual:maps -->

## NFC (slug: nfc)

What it governs: how an iOS app can read NFC (near-field communication) tags from physical objects, both actively within the app (in-app tag reading) and in the background (background tag reading), including the correct language to use when instructing the person to scan.

Why: the central principle is language accessibility: since NFC can be technically unfamiliar to many people, the text advises avoiding developer-oriented technical terms (NFC, Core NFC, tag) and using friendly conversational language. There is also a correction of physical expectation: since scanning requires only proximity and not actual physical contact with the tag, the text instructs using verbs like "scan" and "hold near" instead of "tap" and "touch", so as not to lead the person to try to physically touch the object.

Do and avoid:
- Don't encourage people to make physical contact with objects; the device only needs to be near the tag, not touch it. Use terms like "scan" and "hold near" instead of "tap" and "touch".
- Use accessible terminology, avoiding developer-oriented technical terms like NFC, Core NFC, "near-field communication" and "tag"; use friendly, conversational terms that most people understand (for example "Scan the [object name]" instead of "Scan the NFC tag"; "Hold your iPhone near the [object name] to learn more about it" instead of "To use NFC scanning, tap your phone to the [object]").
- Provide concise instructional text for the scanning sheet: a complete sentence, in sentence case, with final punctuation, identifying the object to be scanned, revising the text appropriately for subsequent scans, and keeping the text short to avoid truncation (for example, first scan: "Hold your iPhone near the [object name] to learn more about it."; subsequent scans: "Now hold your iPhone near another [object name].").
- Support both background reading and in-app reading; the app should always provide a way to scan tags within the app, for people with devices that don't support background reading.

Exact specifications: the text doesn't bring measurement, size, duration or proportion numbers. Factual note: background reading is not available when an NFC scanning sheet is visible, when Wallet or Apple Pay are in use, when cameras are in use, when the device is in Airplane Mode, and when the device is locked after a restart.

Platform differences: no additional considerations for iOS or iPadOS. Not supported on macOS, tvOS, visionOS or watchOS.

Links to other articles: there is no explicit cross-reference to another HIG article (only Core NFC developer documentation).

<!-- visual:nfc -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has no video.
- The opening, tinted blue over the geometric grid and the guide circle, shows three concentric arcs growing to the right, symmetrical and occupying a good part of the frame, which matches the official description of increasingly larger curved lines; it's the same wave motif from the nearby-interactions page (img 0806), here without the person or sensor circle (img 0807).
- The in-app reading is a sheet with the title "Ready to Scan", a blue circular icon with a stylized smartphone (with a slight reflection on the left edge, suggesting glass), an instruction sentence, "Hold your device near the NFC tag.", and a light gray "Cancel" button spanning the full width at the bottom (img 0808).
- Background reading doesn't show any app screen: the first contact is a standard notification banner at the top of the Home Screen, with a black wave icon on the left, title "Item Detected", an action to open in the app and the time, overlapping and covering part of the first row of icons (img 0809).
<!-- /visual:nfc -->

## Photo editing (slug: photo-editing)

What it governs: how to create photo-editing extensions that let people modify photos and videos within the Photos app, applying filters or other changes.

Why: the guiding principle is preservation and clarity of context: edits are always saved as new files in the Photos app, safely preserving the original version, and the extension loads within a modal view that already includes a toolbar from the Photos app itself, so duplicating that toolbar or asking for cancellation confirmation without need only confuses and wastes the person's space and time.

Do and avoid:
- Confirm the cancellation of edits, since editing a photo or video can take time; ask for confirmation that the person really wants to cancel and inform them that the edits will be lost; it's not necessary to show this confirmation if no edits have been made yet.
- Don't provide a custom top toolbar; the extension loads within a modal view that already includes a toolbar, and a second toolbar is confusing and takes space away from the content being edited.
- Let the person preview the edits before approving; it's difficult to approve an edit without seeing the result of the work before closing the extension and returning to the Photos app.
- Use the app's own icon as the photo-editing extension's icon, to convey confidence that the extension is in fact provided by the app.

Exact specifications: the text does not give numbers for measurement, size, duration or proportion.

Platform differences: no additional considerations for iOS, iPadOS or macOS. Not supported on tvOS, visionOS or watchOS.

Links to other articles: there is no explicit cross-reference to another HIG article (only developer documentation "App extensions" and "PhotoKit").

<!-- visual:photo-editing -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has a single illustration and no video.
- The page's symbol is formed by crop marks in dark blue, two opposite L-shaped corners (upper left and lower right), in a thick colored stroke (img 0840).
- Two curved arrows surround the marks, one at the top pointing left and another at the bottom pointing right, drawing an incomplete circular motion that adds the idea of rotation to that of cropping; the image matches the official description (img 0840).
- The construction follows the system of the other opening illustrations, like those for onboarding and offering-help: a rounded-corner rectangle with a gradient in the theme color, here blue, crossed by a rectangular dotted grid and a central guide circle (img 0840).
<!-- /visual:photo-editing -->

## ResearchKit (slug: researchkit)

What it governs: how to use the ResearchKit framework to design a medical research app, including the correct onboarding sequence (introduction, eligibility, informed consent, permission to access data), conducting research via surveys and active tasks, and managing participants' personal information and engagement.

Why: the central principle is clarity on screens that will not be revisited: since a research app's onboarding screens are usually only seen once, clarity is essential, and the fixed order (Introduction, Eligibility, Informed consent, Permission to access data) exists to guarantee that no one advances to consent without first knowing whether they are eligible, and that informed consent always precedes any actual collection of sensitive data. There is also an explicit note that the guidelines are informational only and do not constitute legal advice, reflecting that consent in medical research involves legal and ethical requirements (institutional review board / ethics review board) that go beyond interface design.

Do and avoid:
- Always display the onboarding screens in the correct order: Introduction, then Eligibility, then Informed consent, then Permission to access data.
- In the introduction, clearly describe the subject and purpose of the study, and let existing participants log in quickly to continue a study already in progress.
- Determine eligibility as early as possible, presenting only the eligibility requirements necessary for the study, with simple and direct language, and making it easy to enter information; people do not need to advance to the consent section if they are not eligible.
- Before obtaining consent, make sure participants understand the study; break a long consent form into digestible sections (one for each aspect, such as data collection, data use, potential benefits, possible risks, time required, how to withdraw), using simple language for an overview and, if necessary, a "Learn More" button for a more detailed explanation; participants need to be able to view the entire consent form before agreeing to participate.
- If it makes sense, provide a quiz that tests the participant's understanding, for questions that would otherwise be asked when obtaining consent in person.
- Obtain the participant's consent and, if appropriate, some contact information; after agreeing to participate, participants receive a confirmation dialog, followed by screens for signature and contact details; most research apps email a PDF version of the consent form for the participant's records.
- Obtain permission to access the participant's device or data and to send notifications; clearly explain why the research app needs access to location, Health or other data, and do not request access to data that is not critical to the study; if necessary, also request permission to send notifications.
- Create surveys that keep participants engaged, using ResearchKit's customizable screens to present questions of different answer types (true or false, multiple choice, date and time, sliding scale, free text), following these guidelines: state how many questions there are and the survey's approximate duration; use one screen per question; show the participant's progress in the survey; keep the survey as short as possible (several short surveys usually work better than one long one); use the standard font for the question and a slightly smaller font for additional explanatory text; let the participant know when the survey is complete.
- Make active tasks easy to understand; an active task requires the participant to engage in an activity (speaking into the microphone, tapping fingers on the screen, walking, taking a memory test); describe how to perform the task with clear and simple language; explain any requirements, such as whether the task must be performed at a specific time or under specific circumstances; make sure participants know when the task is complete.
- Use a profile to help participants manage personal data related to the study, allowing them to edit data that may change over the course of the study (such as weight or sleep habits), remember upcoming activities, and provide an easy way to leave the study and view important information such as the consent document and the privacy policy.
- Use a dashboard to show progress and motivate participants to continue, if appropriate to the study, providing encouraging feedback such as daily progress, weekly assessments, results of specific activities, and even aggregated comparisons with other participants in the study.
- Ideally, both the profile and the progress dashboard remain accessible at all times in the app.

Exact specifications: the text does not give numbers for measurement, size, duration or proportion.

Platform differences: no additional considerations for iOS or iPadOS. Not supported on macOS, tvOS, visionOS or watchOS.

Links to other articles: "Research & Care > ResearchKit" and "Research & Care > Developers" (developer documentation), "Protecting user privacy, HealthKit", "ResearchKit GitHub project".

<!-- visual:researchkit -->
### What the illustrations show
Basis: 3 of 3 illustration sheets opened, all codes checked; the page has no video.
- The opening draws a layered diamond shape in blue, like stacked pages seen in perspective, with small hearts on the top face, over a rectangular grid and a concentric construction circle (img 0922).
- The onboarding order is a flat diagram of four light purple boxes of uniform color, in a row, connected by arrows from left to right and labeled only with plain text, with no icons (img 0923).
- The sample app's introduction uses a dark purple background, a central illustration of an elderly person surrounded by icons, a welcome title with a subtitle that names the study, and a white "Next" button at the bottom (img 0924).
- Eligibility is a form written as running sentences with embedded fields (an age field, country and phone type in menus), under a purple bar with back, title and help; at the bottom, "Back" and "Submit" side by side and "Step 3 of 3" with an almost full progress bar (img 0925).
- The quiz shows the first question, about the purpose of the study, in bold, with three radio options (the first one selected), a centered gold "Next" button, and "Step 1 of 5" with the progress bar at the start (img 0926).
- The signature screen is the densest: each consent item has a colored icon on the left and a green check on the right, followed by the legal paragraph and the typed name; the final decision is an asymmetric pair, "Disagree" as plain text and "Accept" as a solid yellow button (img 0927).
- Scrolling the same screen, the data-sharing option becomes two radio buttons (share with other researchers or only with this study, the latter selected) and a single yellow "Accept" remains (img 0928).
- The same primary button appears in two states: solid yellow when an action is possible (Next, Submit, Accept, Get started) and pale yellow when nothing has been selected, as in the multi-select symptom survey, which has a bold question, a subtitle asking to check all that apply, and a white grouped list under a category label (img 0929).
- The active task combines a dark purple top with an illustration of a person walking, a title, explanatory text and a section on what will be needed with three labeled colored circular icons, closing with a yellow "Get started" (img 0930).
- Survey and active task use a white close "x" in the upper left corner (img 0929, 0930), while eligibility, quiz and signature carry a back arrow on the purple bar (img 0925, 0926, 0927).
- The profile is a list of label-and-value pairs with a navigation arrow on the right, a gear icon on the purple bar and a tab bar with three items, the active one highlighted in purple (img 0931); the history groups records by date with time, a colored icon by task type and name, repeating the task icon vocabulary and the same tab bar (img 0932).
<!-- /visual:researchkit -->

## What this group reveals about the Apple way

1. Permission is never a single, definitive event: in healthkit, homekit, id-verifier and researchkit, the text treats requesting access as contextual and revocable, repeated whenever necessary, never assumed as granted forever.

2. Data minimization as a structural rule, not just an ethical one: healthkit ("request access to health data only when you need it"), id-verifier ("ask only for the data you need", with Display Only requests that do not even transmit data to the app) and machine-learning (calibration: "collect only the most essential information") show the same principle applied in completely different domains.

3. Visual trust elements of the system (icons, badges, rings) are treated as protected intellectual property with a fixed meaning: healthkit (Activity ring, Apple Health icon), homekit (HomeKit icon), live-photos (Live Photo badge) and maps (Apple logo) share the same logic of "never change color, shape, scale or position", because the meaning of the element depends on visual consistency across apps.

4. Developer-facing terminology must never leak into the person-facing interface: healthkit forbids the term "HealthKit" in user-facing text, homekit carefully distinguishes "action set" (API) from "scene" (UI), and nfc forbids terms like "NFC", "Core NFC" and "tag" in favor of conversational language.

5. Never duplicate or fragment a single source of truth: icloud avoids asking which documents to keep (the cloud is the single source), homekit requires always deferring to the HomeKit database and never presenting duplicated settings, and in-app-purchase uses the system's confirmation sheet and refund flow instead of replicating them.

6. Canceling, exiting and reverting must always be easy and never hidden: in-app-purchase insists that canceling a subscription must never seem difficult or discouraged, machine-learning requires that calibration can be canceled at any time without judgment, and photo-editing asks for confirmation before discarding edits, but never blocks exiting.

7. Feedback and error correction always trigger an immediate, persistent action: machine-learning is explicit in at least three sections (explicit feedback, implicit feedback, corrections) that any response from the person must be reflected instantly and retained, never lost or ignored.

8. Sequential, non-revisitable onboarding demands doubled clarity: researchkit defines a fixed order of four onboarding steps precisely because these screens are normally seen only once, and in-app-purchase recommends showing the value of the subscription right at onboarding before asking for financial commitment.

9. Adaptation between platforms is never just resizing: mac-catalyst is the most explicit example, with an entire section dedicated to why simply scaling up the iPad interface is not enough, requiring rethinking navigation, input, menus and layout for the Mac's native conventions.

10. Data sensitivity determines the rigor of UI treatment, not just backend security: healthkit, id-verifier, homekit and the private/public data section of machine-learning treat the interface (the permission text, the calibration UI, the prompts) as part of the privacy protection mechanism, not as a decorative layer over a backend policy.

11. Transparency about limitations and confidence is preferred over faking perfect accuracy: machine-learning dedicates entire sections to "Limitations", "Confidence" and "Attribution" instructing to communicate openly when a feature may fail or when confidence is low, instead of simply hiding the imperfection.

12. Correct brand and trademark naming is treated with the same rigor in very different technical contexts: homekit dedicates an entire section to correct capitalization and use of "HomeKit" and "Apple Home", and healthkit does the same for "Apple Health", both forbidding translation of the brand name and requiring correct legal credits.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/healthkit.md, 67 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/homekit.md, 209 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/icloud.md, 32 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/id-verifier.md, 42 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/imessage-apps-and-stickers.md, 66 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/in-app-purchase.md, 132 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/live-photos.md, 34 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/mac-catalyst.md, 111 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/machine-learning.md, 196 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/maps.md, 106 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/nfc.md, 32 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/photo-editing.md, 26 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/researchkit.md, 76 lines read, to the end: yes

All 13 articles in this group have their own text; none is merely a collection index.
