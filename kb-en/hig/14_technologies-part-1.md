# Technologies (part 1)

## AirPlay (slug: airplay)

### What it governs
How an app should integrate, display and name AirPlay, the feature that streams audio and video content wirelessly from iOS, iPadOS, macOS and tvOS to Apple TV, HomePod and compatible TVs and speakers.

### Why
Apple prioritizes consistency and user trust over customization: the system's media player already handles chapters, subtitles and streaming in a tested, familiar way, so diverging from it costs engineering without perceptible gain. The playback continuity reasoning ("people expect the show to keep going while they check email") governs several rules: the app does not own the moment of consumption, it is only the channel. In naming, the logic is to protect the AirPlay brand as a technical noun and never as a verb or the app's own badge, so that the user's recognition of the icon and the name stays stable across any app that uses it.

### Do and avoid
- Prefer the system-provided media player; consider a custom player only if the system does not meet the app's needs.
- Provide content at the highest resolution possible in the HLS playlist, covering the full range of resolutions.
- Do not stream content that only makes sense within the app's context, such as background loops.
- Support both AirPlay streaming and mirroring.
- Support remote control events (play, pause, fast forward) via the lock screen, Siri or HomePod.
- Do not interrupt playback when the app goes to the background or the device locks.
- Do not interrupt another app's playback, except if the app itself starts playing immersive content.
- Keep the app functional during AirPlay; do not let other videos in the app start playing and interrupt the stream.
- If a custom player is needed, replicate the appearance and behavior of the system buttons, including distinct visual states, and position the AirPlay icon in the bottom right corner (iOS 16 and iPadOS 16 onward).
- Use the black AirPlay icon on white or light backgrounds, when other technology icons also appear in black; use white on dark backgrounds; use a custom color when other icons also use that color.
- Do not use the AirPlay icon or name on custom buttons or interactive elements; use it only in a non-interactive way.
- Pair the icon with the AirPlay name correctly, using the same font as the rest of the layout.
- Give more prominence to the app's name or identity than to AirPlay.
- Capitalize correctly: "AirPlay", capital A and P, the rest lowercase; use the all-caps version only if the layout is entirely in capitals.
- Always use AirPlay as a noun, never as a verb ("Use AirPlay to listen", never "AirPlay to your speaker" or "You can AirPlay with [App Name]").
- Use terms like "works with", "use", "supports", "compatible"; do not say "[App Name] has AirPlay".
- You may combine "Apple" with "AirPlay" ("Compatible with Apple AirPlay").

### Exact specifications
- Position of the AirPlay icon in a custom player: bottom right corner, from iOS 16 / iPadOS 16 onward.

### Platform differences
No additional considerations for iOS, iPadOS, macOS, tvOS or visionOS. Not supported on watchOS.

### Links to other articles
Cites the Apple Trademark List and Guidelines for Using Apple Trademarks and Copyrights (trademark use); references AVFoundation and AVKit (developer documentation).

---

<!-- visual:airplay -->
### What the illustrations show
Basis: 2 illustration sheets viewed (7 images, in light appearance), codes checked; no videos.
- The opening draws the AirPlay icon, a rounded rectangle of a screen with a triangle nested at its base, in dark blue over a blue gradient, with a dotted rectangular and circular grid; it is the same construction as the accessibility and action-button pages, now tinted blue (img 0039).
- The system's default player, paused, overlays translucent controls on the video: at the top close, picture in picture, AirPlay and share; at the center rewind 10 seconds, pause and forward 10 seconds; below, the progress bar with elapsed and remaining time; subtitles and audio in the bottom right corner (img 0040).
- The AirPlay icons appear as a fixed pair: audio on the left, a triangle under three concentric arcs, and video on the right, a triangle under a rounded rectangle of a screen (img 0041).
- The same pair is repeated three times in the same arrangement and only the color changes with the background: black on white, white inside a solid black rectangle and vibrant blue on white, forming a color guide by context (img 0041, img 0042, img 0043).
- In the naming section, right and wrong use isolated badges, a green check in a green circle and a gray X in a gray circle, each in its own cell, not paired in the same image as on other pages (img 0044, img 0045).
<!-- /visual:airplay -->

## Always On (slug: always-on)

### What it governs
How an app should behave when the device enters the Always On state (an always-active, low-power display), present on iPhone 14 Pro / Pro Max and Apple Watch.

### Why
The central principle is "useful information glanceable in a private, low-power way": the system dims the screen and reduces motion to save power and not expose data to casual observers. The rule of "not stopping motion instantly, but transitioning gracefully" exists so the transition does not look like an error to the user. The rule of keeping the layout consistent prevents interface changes from drawing unwanted attention when the phone is lying face up, a situation in which motion on the screen stays visible even without the user looking directly at it.

### Do and avoid
- Hide sensitive information, such as bank balances or health data, including what could appear in a notification.
- Keep other types of personal information glanceable when it makes sense (for example, heart rate during a workout on Apple Watch); the user can turn off Always On if they do not want any information visible.
- Keep important content legible and dim non-essential content (secondary text, images, color fills).
- Keep a consistent layout; avoid distracting interface changes when entering or leaving Always On.
- When entering Always On, prefer transitioning an interactive component to an unavailable appearance instead of simply removing it.
- Within Always On, make infrequent and subtle updates (for example, a sports app pauses play-by-play updates and only updates the score when it changes).
- Gracefully transition motion to a resting state; do not stop it instantly.

### Exact specifications
No number, measurement or default value present in the text.

### Platform differences
No additional considerations for iOS or watchOS. Not supported on iPadOS, macOS, tvOS or visionOS.
- On iPhone 14 Pro and iPhone 14 Pro Max, the system displays Lock Screen items such as Widgets and Live Activities when the device is placed face up and still.
- On Apple Watch, when the wrist is lowered, the system dims the watch face and continues displaying the app's interface, as long as it is in the foreground or running a background session.

### Links to other articles
Cites Notifications (for guidance on hiding personal information in notifications) and Designing for watchOS.

---

<!-- visual:always-on -->
### What the illustrations show
Basis: 1 illustration sheet viewed (1 image, in light appearance), code checked; no videos.
- The opening sketch is a vertical rectangle with rounded corners, a silhouette of a watch or a screen, in dark blue over a blue-to-purple gradient (img 0052).
- The interior of the silhouette is filled with hatching of parallel, uniform diagonal stripes, and not by a sharp figurative pictogram (img 0052).
- A small solid rectangle stands out in the upper left corner of the shape, read as a digital crown or side button (img 0052).
- The overlaid dotted circular and rectangular grid and the monochromatic gradient ink repeat the pattern of the other single-icon pages, changing only the color and the internal shape (img 0052).
Recorded divergences: the official description talks about an Apple Watch with a person running, but no human figure can be made out in the image; what appears is only the uniform diagonal hatching.
<!-- /visual:always-on -->

## App Clips (slug: app-clips)

### What it governs
How to design, distribute and visually flag an App Clip, a lightweight version of an app or game that offers an instant experience without requiring a download of the full app.

### Why
The principle is speed and focus: an App Clip exists to solve a one-off ("in-the-moment") task or demonstrate the full app, preserving people's privacy for a limited time. Apple restricts functionality (no tab bars, no background operations, data erased between launches) because the implicit contract with the user is "this is light and temporary, I am not installing anything permanent". The emphasis on not asking for account creation and on offering Apple Pay/Sign in with Apple comes from the same principle: reduce friction and reduce the surface of personal data collected in a transitory context. The App Clip Code rules (printing, color, size) exist to guarantee a reliable reading experience and to protect the Apple brand, since any distortion of the code reduces the successful scan rate.

### Do and avoid
App Clip design
- Allow a task or demo to be completed entirely within the App Clip, without requiring installation of the full app.
- Focus on essential features; reserve advanced features for the full app.
- Do not use App Clips only for marketing purposes or to display ads.
- Avoid web views; use native components and frameworks.
- Design a linear, easy-to-use and focused interface, without tab bars or complex navigation.
- At launch, show the most relevant part of the App Clip, skipping unnecessary steps.
- Guarantee immediate use: include all necessary assets, omit splash screens, never make the person wait.
- Keep the App Clip small for a fast launch; reduce unnecessary code and assets; avoid downloading additional data.
- Make the App Clip shareable via link, including to specific points within it.
- Make payment easy; consider Apple Pay for express checkout.
- Avoid requiring account creation before delivering value; if it is necessary, limit the information requested (e.g., Sign in with Apple).
- When installing the full app, offer a familiar and focused experience, without requiring a new login.

Privacy
- Limit the amount of data stored; do not rely on previously saved data, since the system may have removed the App Clip and erased its data.
- If you store login data, keep it securely outside the device.
- Consider Sign in with Apple.
- Offer a secure form of payment, such as Apple Pay.

Show the full app
- Do not compromise the experience by abusively asking for the full app to be installed.
- Choose the right moment to recommend the app (when the person completes a task or reaches a natural pause), using SKOverlay.
- Recommend in a non-intrusive and polite way; do not ask repeatedly or interrupt the task; do not use push notifications for this.

Notifications
- App Clips can schedule and receive notifications for up to 8 hours after launch.
- Ask permission for an extended period only if truly necessary.
- Keep notifications focused on the task; do not send purely promotional notifications.

App Clips for businesses
- Use consistent branding, prioritizing the business's brand over the platform provider's.
- Handle multiple businesses/locations correctly, verifying the location at launch.

App Clip Card content
- Be informative about what the App Clip offers.
- Prefer photography and graphics over screenshots of the app interface.
- Avoid text in the header image (it is not localizable).
- Use a PNG or JPEG image of 1800x1200 px with no transparency.
- Use concise copy: a title of up to 30 characters and a subtitle of up to 56 characters.
- Choose the action button verb: View (media or educational/informational content), Play (games), Open (other cases).

App Clip Codes
- Always use the designs provided by Apple, following size, placement and printing rules.
- Choose between the badge design (with the App Clip logo) or the no-logo design when space is limited.
- Include the App Clip logo when space allows; use the no-logo design on disposable paper/plastic items or items associated with gambling/drinking (playing cards, poker chips, bar coasters).
- Place the code on a flat or cylindrical surface; on a cylindrical surface, the code's width cannot exceed one sixth of the circumference.
- Avoid deformable materials (paper, plastic, fabric) that bend or wrinkle; if necessary, mount on something rigid like a card.
- Ensure sufficient lighting for reliable scanning and avoid requiring too wide an angle.
- Do not overlay text, logos or images; never animate or darken the code.
- Always display the code in the correct position (not rotated).
- Never create your own variation of the design; do not apply filters, glows, shadows, gradients or reflections; when scaling, do not alter the proportion and scale all attributes (including stroke thickness) proportionally.
- Leave minimum clear space around the code equal to the space between the central glyph and the circular code.

Printing
- Test printed codes before distributing, checking scanning from several angles.
- Use high-quality, non-textured printing materials, matte finish; avoid gloss, reflective or holographic varnish; use matte lamination if laminating; use UV-resistant materials in outdoor settings.
- Work with flexographic printing at a professional service; use an inkjet printer for in-house printing.
- Use high-resolution images; calibrate the printer.
- Convert the SVG (sRGB) to CMYK with relative colorimetric intent (media-relative); use the "Generic CMYK" ICC profile (CMYK printers) or the "Gracol 2013 ICC profile" (CMYKOV printers), with a CIELab Delta E color tolerance of 2.5.
- On a printer that is grayscale only, generate only grayscale codes.
- For a code with integrated NFC, use NFC Type 5 tags.

Printer calibration verification
- Use the calibration test sheets provided by Apple to verify the chosen color pair and the grayscale settings.

### Exact specifications
- App Clip Card image: 1800x1200 px, PNG or JPEG, with no transparency.
- App Clip Card title: maximum 30 characters.
- App Clip Card subtitle: maximum 56 characters.
- Printed App Clip Code: minimum diameter of 3/4 inch (1.9 cm).
- Digital App Clip Code: minimum size of 256x256 px, PNG or SVG file.
- App Clip Code with integrated NFC: NFC tag of at least 35 mm in diameter (or equivalent size); if the embedded NFC tag is 35 mm, the printed code must be at least 1.37 inches (3.48 cm) in diameter.
- Reading distance for code size: a ratio of at most 20:1; recommended ratio of 10:1. Example given: a code read from 40 inches (101 cm) away must have a minimum diameter of 4 inches (10.16 cm).
- Code width on a cylindrical surface: at most one sixth (60 degrees) of the circumference.
- Minimum resolution when rasterizing the SVG: 600 ppi; printing with a minimum resolution of 300 dpi.
- Color tolerance in the CMYK conversion: CIELab Delta E of 2.5.
- App Clip notifications: available for up to 8 hours after launch.

### Platform differences
No additional considerations for iOS or iPadOS. Not supported on macOS, tvOS, visionOS or watchOS.

### Links to other articles
Cites Apple Pay, Sign in with Apple, Guidelines for Using Apple Trademarks, NFC (call-to-action messages with NFC) and Legal requirements (use of Apple trademarks).

---

<!-- visual:app-clips -->
### What the illustrations show
Basis: 6 illustration sheets viewed (24 images, in light appearance), codes checked; no videos.
- The opening draws an app icon in blue with the four corners made of separate short strokes, exposing that the shape is born from corner arcs aligned to a grid of centered horizontal, vertical and diagonal axes (img 0053).
- The App Clip card occupies the bottom half of the lock screen, over the wallpaper, with clear hierarchy: bold title, short two-line description, blue "Open" button on the right and discreet attribution below, with a small app icon and a link to the App Store (img 0054).
- Opened, the App Clip is a complete functional screen, not a preview: a vertical list of items with a circular thumbnail, name, price and quantity controls, closing with a rounded order button that shows the count (img 0055).
- Two cards side by side repeat the same structure of frame, background image, title, description and button, each with its own content, and the button verb changes with the type: Play for the game and Open for the app (img 0056).
- The code has two variants: a rounded badge with dashed concentric rings around a camera icon and the App Clip logo inside, and the loose ring circle, with no frame or text (img 0057, img 0058).
- The anatomy is taught with horizontal callout lines, first by structure (central icon, visual ring code, logo) and then by color (background, color generated in the intermediate tone of the rings, foreground in the icon and the text) (img 0059, img 0076).
- The physical use is told across two planes linked by a blue highlight circle: people at a coffee shop table with a stand and, next to it, the close-up of the phone screen recognizing the code; in the clear-message version, the close-up shows the title above the code and an instruction phrase below, as a single piece (img 0060, img 0071).
- For a cylindrical surface, a circle is divided into six equal slices and the code's arc occupies one of them, with an angular dimension of 60 degrees (img 0061).
- The correct orientation has the central glyph upright; the wrong variants show the glyph lying down and the glyph rotated into a diamond, judged by isolated green check and gray X stamps (img 0062 to 0066).
- The minimum diameter appears as a double arrow with a dimension of 3/4 inch, applied separately to the badge and to the circle with no logo (img 0067, img 0068).
- An App Clip Code and a QR code sit in pink rectangles of the same height, marked by a red line at the top; the clear space is a pink band with the same x dimension repeated on every side of each code (img 0069, img 0070).
- The allowed customization appears in a row of four colors (red and green badge, blue and orange circle) with the same structure, and the errors come one at a time, isolating a single variable: oval proportion, background gradient and drop shadow (img 0072, img 0073, img 0074, img 0075).
Recorded divergences: for img 0064 the official description talks about the code rotated 90 degrees to the left, but in the image only the central glyph changes orientation and the outer rings look the same, so the rotation of the whole code is not visually obvious in the isolated cell.
<!-- /visual:app-clips -->

## Apple Pay (slug: apple-pay)

### What it governs
How to offer, integrate, customize and name Apple Pay in apps and sites, including checkout, the payment sheet, buttons, the Apple Pay mark, subscriptions and donations.

### Why
The dominant principle is trust and simplicity at the point of payment: the payment sheet must reflect exactly what will be charged, from whom, and when, because real money is at stake. The rule of "making Apple Pay the primary option when credentials are available" reflects the logic that Apple Pay resolves the friction of typing card data, and hiding that option is considered a disservice to the user. The rules about the Apple Pay mark versus the button (never use the mark as a button) and about never customizing the buttons' API come from the same commitment to consistent visual recognition that appears in AirPlay: any variation created by third parties breaks the trust that this is really a secure Apple Pay flow. The requirement to clearly communicate pending amounts, subscriptions and future charges (e.g. "Amount Pending") comes from the principle of financial transparency: never let the person authorize an amount without understanding what they are authorizing.

### Do and avoid
Offering Apple Pay
- Offer Apple Pay on all devices and browsers that support it; do not present the option if the device does not support it.
- Make Apple Pay the primary payment option when credentials are available (but not necessarily the only one); do not separate it into a standalone flow.
- Use Apple Pay buttons only to start payment or, when appropriate, the setup process.
- If you use a custom button to start Apple Pay, it cannot display "Apple Pay" or the logo; there must be the Apple Pay mark or a text reference on the same page.
- Use the Apple Pay mark only to communicate that Apple Pay is accepted; never as a payment button.
- Do not hide an Apple Pay button or make it look unavailable; if it cannot be used yet, flag the problem after the tap/click.
- Inform search engines that Apple Pay is accepted, via semantic markup.
- Every site that offers Apple Pay needs a privacy policy and must adhere to the acceptable use rules.

Checkout
- Offer a cohesive checkout experience, with the app/site brand maintained; avoid opening new pages/windows.
- Assume that people want to use Apple Pay when it is available; consider showing it first, larger, or visually separated.
- Offer Apple Pay buttons on product pages for a quick purchase of an individual item; if the item is already in the cart, remove it from the cart after the purchase.
- Offer express checkout for purchases with multiple items.
- Support coupons and promotional codes directly in the payment sheet, especially in express checkout flows.
- Collect necessary information (color, size) before the Apple Pay button; flag and automatically navigate to the problematic field if data is missing.
- Collect optional information (gift messages, delivery instructions) before checkout or even after the purchase is completed, since there is no way to enter optional data in the payment sheet.
- Gather multiple shipping methods and destinations before showing the payment sheet, since it only allows one method/destination per order.
- For in-store pickup, help choose the location before showing the payment sheet.
- Prefer the checkout information coming from Apple Pay, assuming it is complete and up to date.
- Avoid requiring account creation before the purchase; ask on the order confirmation page, with pre-filled fields.
- Report transaction results in the payment sheet, including error messages.
- Display a confirmation/thank-you page after the purchase; mentioning Apple Pay in the confirmation is optional, but if you mention it, show it after the last four digits of the account or as a separate note (e.g.: "1234 (Apple Pay)" or "Paid with Apple Pay").

Customizing the payment sheet
- Present and ask for only essential information, to avoid confusion or privacy concerns.
- Show the active coupon/code, or allow entry within the sheet itself.
- Let the person choose the shipping method in the sheet, with description, cost and, optionally, estimated delivery/pickup date.
- Use line items to explain additional charges, discounts, pending costs, additional donations, recurring and future payments; do not use line items to list order items.
- Keep line items short, fitting on one line whenever possible.
- Provide the business name after the word "Pay" on the same line as the total (ex.: "Pay [Business_Name]").
- If not the end merchant, identify both businesses (ex.: "Pay [End_Merchant_Business_Name (via Your_Business_Name)]").
- Clearly disclose when additional costs may occur after authorization, using an "Amount Pending" line item when the total is not known at checkout time.
- Handle entry and payment errors clearly, helping resolve them quickly.
- Do not add spinners or additional progress indicators; the payment sheet already handles that.

Site icon
- Sites that support Apple Pay can provide an icon that appears during payment authorization, notably in Handoff.

Handling problems
- Verify data when the sheet appears, on field changes and after authentication; use clear and consistent messages.
- Do not force compliance with your own business logic; ignore irrelevant data and infer missing data when possible (ex.: ignoring extra ZIP code digits instead of requiring a correction).
- Report problems to the system with the correct status code.
- Explain the problem clearly and concisely, referencing the relevant field; use noun phrases with sentence capitalization and no final punctuation; try to keep messages to 128 characters or fewer to avoid truncation.
- When an interruption occurs (cancellation, timeout), cancel any payment in progress; the person can restart by tapping the button again.

Subscriptions
- Clarify the subscription details before showing the payment sheet (billing frequency, terms).
- Include line items reiterating billing frequency, discounts and additional fees; if no payment is required at authorization, disclose when the charge will occur.
- Clearly communicate the trial period terms, including the trial amount (even if $0), the regular amount after the trial and the start date of the regular charge.
- Clarify the current amount being charged at the time of authorization, in the total line.
- Only show the payment sheet when the subscription change results in additional fees; if the cost decreases or stays the same, authorization is not necessary.
- Treat the billing agreement field as a plain-language summary, not a substitute for the formal terms; leave it blank when in doubt.

Donations
- Use a line item to identify the donation (ex.: "Donation $50.00").
- Offer predefined donation amounts and an "Other Amount" option.

Apple Pay buttons
- Always use the API provided by Apple to create buttons; never create custom designs or try to replicate them.
- Choose the button type that best fits the flow's terminology (Buy, Pay, Check Out, Continue, Book, Donate, Subscribe, Reload, Add Money, Top Up, Order, Rent, Support, Contribute, Tip, or the generic Apple Pay).
- Use the "Set Up Apple Pay" button in Settings, a profile or an interstitial page when the device supports it but the person has not set it up yet.

Button style
- Use the automatic style to let the system's appearance decide; or choose manually: black (light backgrounds with sufficient contrast, never on a dark background), white with outline (light backgrounds without sufficient contrast, never on a dark/saturated background), white (dark backgrounds with sufficient contrast, never on a light background).

Button size and position
- Display the Apple Pay button prominently; do not make it smaller than other payment buttons; avoid requiring scrolling to see it.
- In a side-by-side layout, position the Apple Pay button to the right of an "Add to Cart" button; in a stacked layout, position it above.
- You can adjust the corner radius to match the rest of the interface (straight corners or capsule shape).
- Keep the minimum size and margins; the title's translation can vary in size by locale, and if it does not fit, the system replaces it with the plain Apple Pay button (there is no automatic substitution for "Set Up Apple Pay").

Apple Pay mark
- Use only the artwork provided by Apple, with no changes other than height; the height must be equal to or greater than other payment brand marks in the flow.
- Do not adjust width, corner radius or proportion; do not add a registered trademark symbol or other content; do not remove the border; do not add shadows, glows or reflections; do not invert, rotate or animate it.
- Keep the minimum clear space around the mark.

Referring to Apple Pay
- Use "Apple Pay" exactly as it appears in the Apple Trademark List; never in the plural or possessive.
- Capitalize with uppercase A and P, the rest lowercase; all uppercase only if necessary to conform to an existing typographic style.
- Never use the Apple logo to represent the word "Apple" in text.
- In the US, use the registered trademark symbol (®) on the first appearance in body text; do not include the symbol when Apple Pay appears as a selection option at checkout.
- Coordinate the font with the app/site; do not imitate Apple's typography.
- Never translate "Apple Pay" or any Apple trademark.
- In a payment selection context, only use a text-only description of Apple Pay if all the other options are also text-only; otherwise, use the Apple Pay mark.
- When promoting Apple Pay in an app, follow the App Store marketing guidelines.

### Exact specifications
- Site icon: @2x = 60x60 pt (120x120 px); @3x = 60x60 pt (180x180 px).
- "Apple Pay" button (generic): minimum width 100pt (100px @1x, 200px @2x), minimum height 30pt (30px @1x, 60px @2x), minimum margin of 1/10 of the button's height.
- "Book with Apple Pay" button: minimum width 140pt (140px @1x, 280px @2x), minimum height 30pt (30px @1x, 60px @2x), minimum margin of 1/10 of the button's height (the same rule applies to Buy, Check Out, Donate, Set Up, Subscribe with Apple Pay, per the source's table).
- Minimum clear space around the Apple Pay mark: 1/10 of its height.
- Validation error messages: try to keep them to 128 characters or fewer to avoid truncation.

### Platform differences
No additional considerations for iOS, iPadOS, macOS, visionOS or watchOS. Not supported on tvOS.

### Links to other articles
Cites In-app purchase (for selling virtual goods), PKPaymentAuthorizationController, applePayCapabilities, Offering Apple Pay in Your App, Checking for Apple Pay availability, PKDateComponentsRange, paymentSummaryItems, Supporting donations, PKPaymentAuthorizationViewControllerDelegate, PKPaymentError, Apple Pay Status Codes, PKPaymentButtonType, PKPaymentButtonStyle, WKInterfacePaymentButton, App Store marketing guidelines, and the Apple Pay Marketing Guidelines page.

---

<!-- visual:apple-pay -->
### What the illustrations show
Basis: 14 illustration sheets viewed (54 images, in light appearance), codes checked; no videos.
- The payment sheet on iPhone has a block structure: a close X in the top left corner, the centered Apple Pay mark, a title with Pay and the business name, the total amount as the largest text on the screen, a gradient card, the payment method line, summary lines with the amount right-aligned and, in the footer, the indication to confirm with the side button (img 0094).
- With a custom button, the Apple Pay mark sits stacked above the "Order Now" action button, both centered on a gray card, marked with a green check; the wrong version repeats "Apple Pay" in the button text and gets a gray X (img 0095 to 0098).
- The post-purchase confirmation places a green check and a thank-you with the order number at the top, and only below offers account creation, sign up with Apple and login fields with a disabled button (img 0099).
- The line items form their own block separated by a divider above Subtotal, with the label on the left and the amount on the right in a column; on the web the sheet is wider and more spacious, with a name and domain header, the total in bold, Cancel in the top right corner instead of the X and confirmation by a fingerprint symbol (img 0100, img 0101, img 0104, img 0108).
- The validation error is signaled only by red text in the shipping field and in the update address label, with no alert icon and no layout change, in app and web; on the web the error also appears inside the recent addresses selector, item by item (img 0103, img 0104, img 0105).
- Subscriptions get a recurrence block with an orange circular arrows icon, the monthly amount and start and end dates; the variable version swaps the amount for the title "Amount Pending", and the one with no charge at authorization shows $0.00 at the top reinforced by a free trial block with the date the charge begins (img 0106, img 0107, img 0109).
- The system button can display the active card: the Pay logo on the left, a thin vertical bar and the card thumbnail on the right (img 0111).
- All the buttons follow a single template, a black rectangle with rounded corners with centered white text and the Apple symbol in place of the word, varying only the initial verb; there is a minimal version with just the symbol and Pay and the setup version (img 0112 to 0128).
- The three styles are shown in light and dark background pairs: black, white with outline and white; the wrong usage shows up as a loss of contrast, with the button almost disappearing into the background, with no check or X (img 0129 to 0134).
- Size and order always use the same two buttons swapping a single variable: same width and height against a smaller Apple Pay; side by side, touching, with Apple Pay to the right of "Add to Cart"; stacked and left-aligned, with Apple Pay above; the straight, default or capsule corner radius is applied equally to both (img 0135 to 0143).
- The measurement diagrams use a pink outline and dimensions in points: minimum height of 30, minimum width of 100 for the Pay-only button and 140 for the donation button, and minimum margin of 1/10 of the height (img 0144, img 0145).
- The Apple Pay mark, with a white background and a thin gray outline, sits in a row with three other brand marks, all the same size and rounded rectangular shape, and is treated as a payment brand among the others, not as a button (img 0146).
Recorded divergences: the notes point out that the text preceding img 0117 talks about reservations, while the button shown is the donation one, linked to the following paragraph.
<!-- /visual:apple-pay -->

## Augmented reality (slug: augmented-reality)

### What it governs
How to design augmented reality experiences on iOS and iPadOS with ARKit: coaching, object placement, interaction, multiuser experiences, recognizing real objects, communicating with the user, and handling interruptions.

### Why
The central principle is the "convincing illusion": everything, from the scale and lighting of virtual objects to the scene's update rate, exists so the object seems to really inhabit the physical world. The rule of updating the scene 60 times per second, for example, follows directly from this: below that rate, the object "jumps or flickers" and the illusion breaks. The safety and comfort rules (introducing movement gradually, avoiding fatigue, avoiding dangerous movements) reflect that AR draws attention away from the real physical environment, creating real risk of accident. The communication rules avoiding technical terms like "ARKit" or "tracking" reflect the accessibility principle: AR is an advanced concept that can intimidate, so the language should be friendly and action oriented (what to do), not technical diagnosis.

### Do and avoid
- Offer AR features only on capable devices; if the app depends primarily on AR, restrict it to devices that support ARKit; if optional, don't show an error, just omit the feature.
- Use as much of the screen as possible for the physical world and virtual objects; avoid cluttering it with controls and information.
- Aim for convincing illusions: realistic textures, correct scale and placement on detected surfaces, reflecting lighting conditions and simulating camera grain, soft top down shadows, updating the scene 60 times per second.
- Prefer small or rough reflective surfaces, since ARKit's reflections are approximations.
- Use audio and haptics to reinforce immersion (confirming contact between a virtual object and a surface).
- Minimize text in the environment; show only the information that's necessary.
- Consider displaying additional information/controls in screen space (fixed screen space, not attached to the AR environment).
- Consider indirect controls (2D in screen space) for persistent controls; use translucency so as not to block the scene.
- Clearly communicate the app's requirements and expectations for different real environments.
- Be attentive to people's comfort; position objects at a distance that reduces the need to bring the device closer; in games, keep levels short with pauses.
- Introduce movement gradually if the app encourages physical movement.
- Be attentive to safety; avoid encouraging fast, broad or sudden movements.

Coaching
- Use the integrated coaching view to show what to do and give feedback during initialization; it can also help with relocalization after an interruption.
- Hide unnecessary app UI while the coaching view is present.
- Offer custom coaching only if necessary, using the system view as a reference.

Object placement
- Show when it's possible to locate a surface and place an object, aligning the visual indicator to the detected plane.
- Integrate the object into the AR environment immediately when it's placed; subtly refine the position afterward if necessary (e.g., "pushing" it back inside the detected surface).
- Consider guiding toward virtual objects that are off screen with visual or audio cues.
- Avoid aligning objects precisely to the edges of detected surfaces, since they are approximations.
- Incorporate plane classification (e.g., only allow furniture on a "floor" plane, a game board on a "table" plane).

Interactions with objects
- Prefer direct manipulation (touching the object directly) when possible; indirect controls work better when the person is moving.
- Use standard, familiar gestures (dragging with one finger to move, turning with two fingers to rotate).
- Keep interactions simple, since touch gestures are two dimensional but AR is three dimensional.
- Respond to gestures within reasonable proximity of interactive objects, since precision is difficult with small, thin or distant objects.
- Allow object scaling when it makes sense in the app (e.g., an imaginary world yes; a real furniture app no, since scaling doesn't help visualize the real size).
- Never use scale as a way to adjust an object's perceived distance.
- Be careful with potentially conflicting gestures (two finger pinch versus two finger rotation); test for the correct interpretation.
- Aim for object movement consistent with the physics of the AR environment; avoid objects that jump, disappear and reappear.
- Explore interaction methods beyond gestures, such as movement and proximity.

Multiuser experience
- Each participant maps the environment independently and ARKit merges the maps automatically.
- Consider allowing occlusion: people captured by the camera can occlude virtual objects placed behind them.
- When possible, allow new participants to join an AR experience already in progress (implicit map merging).

Reacting to real world objects
- Use 2D/3D reference images and objects so ARKit detects when and where they appear in the current environment.
- When a detected image disappears, consider delaying the removal of attached virtual objects by up to one second before fading out or removing them, to avoid flickering.
- Limit the number of reference images active at the same time; detection works best with 100 or fewer distinct images. If you need more, switch the active set based on context (e.g., using location to know which part of the museum the person is in).
- Limit the number of reference images that require a precise position, since updating the position consumes more resources; use tracked image when the image can move or when the attached animation/object is small compared to the image size.

Communicating with people
- If you need to display instructional text, use accessible terminology; avoid technical terms like "ARKit", "world detection" and "tracking".
- Prefer 3D hints in a three dimensional context (e.g., a 3D rotation indicator around the object) over 2D text, unless the person doesn't respond to contextual hints.
- Make important text legible: use screen space for critical labels and instructions; if you need to display text in 3D space, make sure it faces the person and stays the same type size regardless of distance.
- If necessary, provide a way to get more information, with an appropriate visual indicator.

Handling interruptions
- ARKit can't track position/orientation during an interruption (e.g., app switching, a call); after the interruption, previously placed objects likely appear in the wrong position.
- Use relocalization to restore objects to their original position using new observations.
- Consider using the coaching view to help with relocalization, guiding the person back to their previous position/orientation.
- Consider hiding previously placed virtual objects during relocalization, to avoid flickering, and showing them again in the new position.
- Minimize interruptions if the app supports both AR and non AR experiences, embedding the non AR experience within the AR one when possible.
- Allow canceling relocalization, since it can continue indefinitely without success; offer a reset button or another way to restart.
- Indicate when the front camera can't track a face for more than about half a second, with a visual indicator; if you need text, keep it minimal.

Suggesting troubleshooting
- Allow restarting the experience if it doesn't meet expectations, without forcing a wait for better conditions.
- Suggest possible fixes for surface detection problems (insufficient light, a too reflective surface, a surface without enough detail, excessive camera movement).

Icons and badges
- Apps can display the AR icon on controls that start ARKit based experiences.
- Use the AR glyph only to start an ARKit based experience; never alter it (except size and color), don't use it for other purposes, and don't use it together with AR experiences not built with ARKit.
- Maintain minimum clear space around the AR glyph.
- Apps with product collections can use badges to identify items viewable in AR.
- Use the AR badges (collapsed or expanded) only to identify objects viewable in AR via ARKit; never alter them or change their color.
- Prefer the full AR badge over the glyph only badge; use the glyph only badge in restricted spaces.
- Use badging only when the app mixes objects viewable in AR with objects that aren't; if all objects are viewable in AR, badging is redundant.
- Keep badge placement consistent (same corner), legible and not so large that it occludes important detail in the photo.
- Maintain minimum clear space around the AR badge.

### Exact specifications
- AR scene update rate: 60 times per second.
- Minimum clear space around the AR glyph: 10% of the glyph's height.
- Minimum clear space around the AR badge: 10% of the badge's height.
- Delay before hiding the object of a disappeared image: up to one second before fade out/removal.
- Recommended limit of reference images active at the same time: 100 or fewer.
- Indication of lost face tracking: about half a second without tracking.

### Platform differences
No additional considerations for iOS or iPadOS. Not supported on macOS, tvOS or watchOS.
- visionOS: ARKit can be used to detect surfaces in the person's environment, use hand and finger positions to inform custom gestures, and support interactions that incorporate nearby physical objects in immersive experiences.

### Links to other articles
Cites Playing haptics, Playing audio, Gestures, Occluding virtual content with people, Detecting Images in an AR Experience, Managing Session Life Cycle and Tracking Quality, Designing custom gestures in visionOS, Immersive experiences, and the ARKit developer documentation.

---

<!-- visual:augmented-reality -->
### What the illustrations show
Basis: 6 illustration sheets (23 images, in light appearance) and 1 video sheet (8 frames) viewed, codes checked.
- The opening shows six dark blue arrows radiating from a common center as three dimensional axes, over a blue gradient with a grid and circle; the AR glyph reuses the same stroke, isolated in black on white, with no gradient or grid (img 0160, img 0175).
- In Measure, the measurement is a translucent white circle with a dotted line and a value label near the tip, while the persistent 2D controls sit in the bottom bar (undo, a large central add button, capture) and in the tabs at the base, over the real camera scene (img 0161).
- Coaching and relocalization reuse the same translucent, dotted surface indicator, and the text changes: at the start, a trapezoid plane on the floor with an illustrated iPhone and a request to move the iPhone; after an interruption, on a dark gray screen, the request to return to the previous area, plus a "Start Over" button in a dark capsule (img 0162, img 0172).
- The app's own placement indicator combines a light blue oval with a thick filled arc at the base, an outer dashed circle, a central point crossed by a horizontal line, and four targeting brackets at the corners of the dark card (img 0163).
- Direct manipulation and indirect control use the same gray cube: in the first, the finger touches the corner with a dotted line and a curved drag arrow; in the second, two black square rotation buttons, clockwise and counterclockwise, sit below the object (img 0164, img 0165).
- The movement constraints use a light gray sphere: over an isometric grid, two dotted axes, red and blue, with arrows in the four directions of the plane; for rotation on a single axis, a dotted vertical line and a blue arrow band wrapping around the sphere (img 0166, img 0167).
- The 3D hint highlights the front left face of the cube in blue and surrounds it with a full curved arrow; the 2D alternative swaps this for a "Rotate" label in a dark capsule over the grid, just below the cube (img 0168, img 0169).
- Black labels with text and an arrow are connected by thin lines to the table and chair in the camera view, with a circular back button in the top left corner; the following detail screen is full and split into two columns, the object on the left and name, price, dimensions and a black purchase button on the right, with an X in the top right corner (img 0170, img 0171).
- Sufficient and insufficient lighting are the same table and chair scene, at the same angle, just in a light tone and a dark tone, with no marker for right or wrong (img 0173, img 0174).
- The glyph appears in composition on a blue "View in AR" button, white to the left of the text, and as a small badge in the top left corner of each item in a grid of collectibles (img 0176, img 0178).
- The expanded badge, with glyph and AR text, and the glyph only badge sit in a rounded light gray rectangle over a checkered transparency background; the minimum clear space of the glyph and of each badge is marked by a translucent pink frame, with no numeric measurements (img 0179, img 0180, img 0177, img 0181, img 0182).
- In the video, a textured 3D meteor spins at a constant pace and direction above a real table, with the "meteor" label anchored just below it and still during the rotation; a dark translucent sidebar on the left lists files with thumbnail, name, date and size, with Select and Search buttons, and stays fixed across all frames while the room remains static (video 005, sheet 0001, q001 to q008).
Recorded divergences: for img 0163 the official description talks about right angle shapes framing a square and a 3D perspective indicator with the longer edge at the bottom, but the drawing viewed is essentially frontal, with the base only suggested by the thicker arc; the official description of the video doesn't mention the file sidebar or the anchored label, visible in all frames.
<!-- /visual:augmented-reality -->

## CareKit (slug: carekit)

### What it governs
How to design CareKit apps, used to manage care plans related to chronic illnesses, injury/surgery recovery, or health and wellness goals, including data privacy, HealthKit/ResearchKit integration, and task, chart, and contact views.

### Why
The dominant, explicit principle is protecting extremely sensitive data: "nothing is more important than protecting people's privacy and safeguarding the extremely sensitive data your CareKit app collects and stores." This explains why permission to access health data must be requested in the exact context of use (not at app launch), and why managing health data sharing must go exclusively through the system's privacy settings, never through the app's own screens: Apple wants a single point of control and trust for the user. On the content side, the logic behind the five task view variations (simple, instructions, log, checklist, grid) is to give precision without verbosity: describe the task with the minimum words necessary, because the person is already in a treatment context and clarity reduces error. The rule for refined, non-intrusive branding follows the same reasoning as "it's not advertising, it's care": distracting from a health plan with branding is seen as harmful to the app's purpose.

### Do and avoid
Data and privacy
- Provide a clear privacy policy with an accessible URL on the App Store.
- Ask for permission before accessing data via iOS features and capabilities, protecting both manually entered data and data obtained from the device/system.

HealthKit integration
- Ask for access to health data only when needed in context (e.g., weight, at the moment of logging weight, not at app launch).
- Clarify the app's intent with descriptive messages on the standard permission screen; avoid custom screens that replicate the standard screen's behavior.
- Manage health data sharing only via the system's Settings > Privacy; do not build additional screens in the app for this.

Motion data
- With permission, obtain motion data from the device (stationary, walking, running, cycling, driving) and, when walking/running, step count, pace, and flights of stairs.
- Motion data can include custom physical therapy data (e.g., ResearchKit tasks testing flexibility, range of motion, ambulatory capacity).

Photos
- With permission, access the camera and photos to share treatment progress images with the care team.

ResearchKit integration
- Incorporate ResearchKit features to display related surveys, tasks, and charts, if appropriate; use the informed consent module to ask permission for data collection/sharing.

CareKit views
- Use each view type (tasks, charts, contacts) for its intended purpose, maintaining consistency.
- Tasks present prescribed actions (taking medication, eating specific foods, exercising, reporting symptoms); charts display progress data/trends; contacts display contact information with support for phone, message, email, and map.

Tasks
- Use the simple style for a single-step task.
- Use the instructions style when you need to add informative text to a simple task.
- Use the log style to help log events, with an automatic timestamp on each entry.
- Use the checklist style to list actions/steps of a multi-step task.
- Use the grid style to display a grid of buttons in a multi-step task in a more compact way; it is the only style with access to the underlying collection view, allowing custom UI elements.
- Consider using color to reinforce the meaning of task items (e.g., one color for medications, another for physical activities), but never as the sole means of conveying information.
- Combine precision with simplicity when describing a task and its steps (e.g., the medication's brand name instead of a chemical description); minimize words when the context already clarifies the meaning.
- Consider complementing complex or multi-step tasks with videos or images.

Charts
- Consider highlighting narratives and trends to illustrate progress.
- Label chart elements clearly and concisely, avoiding repeating the same information (e.g., use "BPM" in the axis label instead of on every data point).
- Use distinct colors; avoid different shades of the same color for different meanings; ensure sufficient contrast.
- Consider providing a legend when colors are not immediately clear.
- Clearly denote units of time (seconds, minutes, hours, days, weeks, months, years).
- Consolidate large data sets for greater legibility.
- If necessary, offset data to keep charts proportional when there is a significant difference between points.

Contact views
- Consider using color to categorize care team members.

Notifications
- Minimize notifications, since care plans vary from patient to patient; consider consolidating multiple items into a single notification.
- Consider providing a notification detail view to allow immediate action without opening the app.

Symbols and branding
- Most view styles work best with the symbols provided by CareKit; the exception is the grid-style task view, which is highly customizable.
- In grid view, consider SF Symbols for symbols relevant to the app's content.
- Design a relevant care symbol, related to the app or to the general concept of health/wellness; avoid a purely decorative symbol or corporate logo.
- Incorporate refined, discreet branding; people don't want to see advertising in a CareKit app.

### Exact specifications
No number, measurement, duration, or default value present in the text (the view structure is described qualitatively, without dimensions).

### Platform differences
No additional considerations for iOS or iPadOS. Not supported on macOS, tvOS, visionOS, or watchOS. Apple Watch can display notifications from the CareKit app (references Notifications).

### Links to other articles
Cites Color, Accessibility, HealthKit, ResearchKit, Notifications, and the CareKit, Core Motion, UIImagePickerController developer documentation, requestAuthorization(toShare:read:completion:), and Protecting user privacy.

---

<!-- visual:carekit -->
### What the illustrations show
Basis: 4 illustration sheets viewed (img 0216 to 0229), all codes checked; no video.
- The CareKit symbol is drawn over a dashed grid with a construction guide circle: a heart with an electrocardiogram trace inside a blue shape in three stacked layers, like overlapping cards, in dark blue outline over a blue gradient (img 0216).
- The typical screen is a vertical stack: a row of seven day circles at the top (complete days with a filled red check, the selected day with a thicker outline), the date and, below, stacked task and chart cards, including a red and gray bar chart with a color legend (img 0217).
- The card's anatomy is annotated with callout lines: header with title and disclosure indicator in the top right corner, horizontal separator, and content subview below (img 0219); header with disclosure indicator and separator reappear without markup in the instructions, log, and checklist styles (img 0221 to 0223), and the detailed contact also opens with a header and separator (img 0229).
- The task styles reuse the same white, rounded-corner card and swap out only the subview: simple with a large red circle and a white check, no instruction (img 0220); instructions with instruction text and a light gray rectangular "Completed" button in red text (img 0221); log with a solid red "Log" button and a log timestamp with a clock icon below (img 0222); checklist with three rows separated by a thin line, each with its own check circle, and instruction at the bottom (img 0223).
- The example associated with the compact grid style repeats the schedule card: three circles, two with a filled red check and one with only an empty outline, alongside the instruction text (img 0219, 0224).
- Completion states are coded by fill: a full red circle with a check for done, an outline-only circle for pending, and the header summarizes what's left, such as "1 remaining" (img 0219, 0223, 0224).
- The three chart styles use the same card, title, Y axis with dashed gridlines at 2.0 and 4.0, X axis with the initials of the seven days, and a color legend with a red square; only the data mark changes, bar (img 0225), dot (img 0226), or continuous line (img 0227), and the peak day appears highlighted in a filled red circle on the axis (img 0225, 0226).
- The contact comes in two levels of the same header (gray circular avatar, bold name, specialty below): simple is a single row with a disclosure indicator (img 0228); detailed adds a separator, descriptive text, a row of three square buttons with red icon and label for call, message, and email, and a light gray address block with a navigation arrow on the right (img 0229).
- The contacts screen repeats two cards with the detailed structure: generic profile photo, descriptive text, three small buttons side by side with red icon and text for call, message, and email, and an address row with a navigation icon on the right (img 0218).
- A single accent color, red, runs through checks, the day selector, bars, the log button, and contact actions, while backgrounds and secondary buttons stay white and light gray (img 0217 to 0229).
<!-- /visual:carekit -->

## CarPlay (slug: carplay)

### What it governs
How to design CarPlay apps using the system-defined templates (audio, communication, navigation, fueling), covering interactions with iPhone, audio, layout, color, icons/images, and error handling.

### Why
The central principle, explicitly stated, is that "CarPlay is designed for drivers to use while driving": every rule follows from the premise that the person has limited attention and cannot and should not handle the iPhone. This explains why interactions on the iPhone must be eliminated when CarPlay is active, why the app can never lock access to CarPlay by requiring input on the iPhone (which might be in the car's trunk), and why errors must be reported in CarPlay and never redirect the person to pick up the iPhone. The audio rule (don't start playback automatically, don't change the overall volume) reflects that the app coexists with other audio sources in the car, like the radio, and the driver, not the app, should control the final volume. The rule to test colors under real in-car lighting conditions reflects that the usage environment is unpredictable (day, night, reflections), unlike testing on a computer screen.

### Do and avoid
iPhone interactions
- Eliminate app interactions on the iPhone while CarPlay is active; any setup must happen before the vehicle is in motion.
- Never block CarPlay because the connected iPhone requires input; the app needs to work even with the iPhone inaccessible (in a bag, in the trunk).
- Make sure the app works without requiring the iPhone to be unlocked, since most people use CarPlay with the iPhone locked.

Audio
- Let the person choose when to start playback; avoid automatic start unless the app's purpose is to play a single audio source or it is resuming interrupted audio.
- Avoid starting an audio session before being ready to play, since this silences other sources (the car radio).
- Start playback as soon as the audio has loaded enough; the system keeps the selection highlighted and shows an activity indicator until the app signals it is ready.
- Display the Now Playing screen when the audio is ready; do not delay playback waiting for descriptive information to finish loading, show it when available.
- Resume playback after an interruption only when appropriate (e.g.: after a phone call); permanent interruptions (such as a playlist started by Siri) are not resumable.
- Automatically adjust audio levels when necessary, but do not change the overall volume; the person controls the final output volume.

Layout
- Provide useful, high-value information in a clean layout, easy to scan from the driver's seat; do not clutter it with nonessential details.
- Keep the overall appearance consistent; elements with similar functions should look similar.
- Make sure the primary content stands out and looks actionable; large items look more important and are easier to tap; in general, place the most important content and controls in the top half of the screen.

Color
- Prefer a limited color palette, coordinated with the app's logo.
- Avoid using the same color for interactive and noninteractive elements.
- Test the color scheme under various lighting conditions in a real car, considering brightness at night and washout under direct sunlight.
- Make sure it looks good in light and dark environments, since CarPlay supports both appearances and can adjust automatically according to lighting.
- Choose colors that communicate effectively with everyone, considering differences in color perception.

Icons and images
- Provide high-resolution images with @2x and @3x scale factors for all the app's art in CarPlay.
- Mirror the iPhone app icon; a good icon works well in both without needing a second design.
- Do not use black for the icon background; lighten a black background or add a border so it does not blend with the screen background.

Error handling
- Report errors in CarPlay, not on the connected iPhone; never direct the person to pick up the iPhone to read or resolve an error.

### Exact specifications
- Common screen sizes cited: 800x480 px (5:3), 960x540 px (16:9), 1280x720 px (16:9), 1920x720 px (8:3).
- CarPlay app icon: @2x = 120x120 px; @3x = 180x180 px.

### Platform differences
No additional considerations for iOS. Not supported on iPadOS, macOS, tvOS, visionOS or watchOS.

### Links to other articles
Cites Inclusive color and the CarPlay App Programming Guide developer documentation.

---

<!-- visual:carplay -->
### What the illustrations show
Basis: 1 illustration sheet viewed (img 0230), code checked; no video.
- The only drawing on the page is the opening symbol: a "C" in a thick dark blue outline with a play triangle centered inside it (img 0230).
- The symbol sits on a gradient background from purplish blue to light blue, with a grid of dashed lines and a construction guide circle, the same thematic icon drawing system used on other HIG pages (img 0230).
- No CarPlay screen, template, layout, applied palette or app icon is illustrated; the visual material only confirms the officially described icon sketch, and the page's screen and icon measurements have no support in image (img 0230).
<!-- /visual:carplay -->

## Game Center (slug: game-center)

### What it governs
How to integrate Game Center (Apple's social gaming network) into a game: access point, Game Overlay/dashboard, achievements, leaderboards, challenges and multiplayer activities.

### Why
The stated principle is to broaden the game's discovery and social connection through the system (App Store, notifications, the Games app), so the integration must be "seamless" and not visually compete with the game itself. This explains rules such as "avoid displaying the access point during active gameplay, splash screens or tutorials": Game Center should appear at natural pause moments (menu, settings), not interrupt immersion. The correct terminology rule (use "Game Center", "Achievements", "Leaderboards" and not synonyms like "Trophies" or "Rankings") seeks a uniform language across games so the player recognizes the system in any app. In challenges, the rule of tracking the most recent score instead of overall progress or personal best exists explicitly to keep regular and new players on equal footing ("level playing field"), avoiding unfair advantage to veteran players.

### Do and avoid
Accessing Game Center
- Determine whether the player is signed in to the system Game Center account when launching the game; if not, initialize the player at that point, for a smoother experience and to maximize discovery opportunities (e.g.: Top Played chart, social recommendations).

Access point
- Display the access point on menu screens; consider adding it to the main menu or settings area.
- Avoid displaying the access point during active gameplay, temporary splash screens, cinematic flows or tutorials that precede the main menu.
- Avoid positioning controls near the access point, since it has a collapsed and an expanded version; check for overlap with important UI.
- Consider pausing the game while the Game Overlay or dashboard is present.

Custom UI
- Use the art that Game Center provides in custom links, preserving the appearance without adjusting dimensions or visual effects.
- Use the correct terminology in custom links: "Game Center" (not GameKit, GameCenter, game center), "Game Center Profile" (not Profile, Account, Player Info), "Achievements" (not Awards, Trophies, Medals), "Leaderboards" (not Rankings, Scores, Leaders), "Challenges" (not Competitions), "Add Friends" (not Add, Add Profiles, Include Friends).

Achievements
- Align with the four Game Center achievement states: locked, in-progress, hidden, completed; the system groups by completion status.
- Determine the display order at upload time, since that is the final order (e.g.: following the most common path through the game).
- Be concise when describing achievements: title and description limited to two lines each, with truncation beyond that; use title-style capitalization in the title and sentence-style in the description.
- Give a sense of progress by using progressive achievements, which display automatic motivational progress messages.
- Design rich, high-quality images; avoid reusing the same asset for more than one achievement; with no asset provided, the card shows a placeholder image.
- Keep the content centered, since the system applies a circular mask to the achievement image.

Leaderboards
- Choose the leaderboard type: classic (tracks the best score of all time, always active, no end) or recurring (resets at a defined interval, such as weekly or daily).
- Use leaderboard sets to organize multiple leaderboards, grouping by themes or game experiences (difficulty modes, activity types, genres/themes).
- Add leaderboard images to reinforce the game's visual aesthetic; create a unique image for each leaderboard that reflects the gameplay involved.
- On iOS, iPadOS and macOS, use a single image; on tvOS, provide a set of images that animates when in focus.
- Be mindful of how cropping can affect the art: on iOS/iPadOS/macOS the system crops art for leaderboards that are part of a set; on tvOS the focus effect can crop layers at the edges; keep the primary content comfortably visible.

Challenges
- Create engaging challenges: short, skill-based activities, with a clear way to measure achievement; create challenges of 1 to 5 minutes of gameplay that the player completes individually.
- Avoid creating challenges that track overall progress or personal best scores, since they give an unfair advantage to regular players; instead, track the most recent score of each attempt, to keep all players on equal footing.
- Make it easy to access the challenge: always deep-link to the exact mode/level where the challenge begins; help first-time players complete initial onboarding before starting.
- Create high-quality art that encourages engagement; avoid positioning the primary content where the challenge's title/description might cover it; provide localized versions of the text in the image via App Store Connect or Xcode.

Multiplayer activities
- Use party codes to invite players to real-time multiplayer activities.
- Allow players to join late, leave early and return later; provide a way to view the group's current code in the game; allow manual entry of the code.
- Support multiplayer activities via in-game UI, taking advantage of the Game Overlay and the Game Center dashboard, which help find players without leaving the game.
- Provide engaging activity art, since the preview image appears at several points in the system.

### Exact specifications
- Game Center party codes: typically eight alphanumeric characters (example given: "2MP4-9CMF").
- Recommended duration of a challenge: 1 to 5 minutes of gameplay.
- Achievement title and description: limited to two lines each, with truncation beyond that.

Achievement image (iOS, iPadOS, macOS, visionOS):
| Attribute | Value |
| Format | PNG, TIF or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |

Achievement image (tvOS):
| Attribute | Value |
| Format | PNG, TIF or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 320x320 pt (640x640 px @2x) |
| Mask diameter | 200 pt (400 px @2x) |

Leaderboard image (iOS, iPadOS, macOS):
| Attribute | Value |
| Format | JPEG, JPG or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x312 pt (1024x624 px @2x) |

Leaderboard image (tvOS):
| Attribute | Value |
| Format | PNG, TIF or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 659x371 pt (1318x742 px @2x) |
| Size in focus | 618x348 pt (1236x696 px @2x) |
| Size out of focus | 548x309 pt (1096x618 px @2x) |

Challenge image:
| Attribute | Value |
| Format | JPEG, JPG or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |

Multiplayer activity image: same dimensions as the challenge image (1920x1080 pt / 3840x2160 px @2x, cropped area 1465x767 pt / 2930x1534 px @2x).

tvOS dashboard image:
| Attribute | Value |
| Image size | 600x180 pt (1200x360 px @2x) |
| Format | PNG, TIF or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |

### Platform differences
No additional considerations for iOS, iPadOS, macOS or visionOS.
- On iOS, iPadOS and macOS, the access point leads to the Game Overlay, a system overlay.
- On visionOS and tvOS, the access point leads to the in-game dashboard, a full-screen view over the game; on visionOS, the access point's location varies depending on the type of game (immersive or volume-based).
- tvOS: an optional image can be shown at the top of the dashboard (do not use the app icon for this).
- watchOS: GameKit features and API are available, but there is no invokable Game Center UI on watchOS; the content appears on the connected iPhone.

### Links to other articles
Cites Designing for games, Game controls, Apple Design Resources, Focus and selection, and the GameKit developer documentation, Creating activities for your game, Creating engaging challenges from leaderboards, Create games for Apple platforms, Game Porting Toolkit, Adding an access point to your game, Rewarding players with achievements, Finding multiple players for a game.

---

<!-- visual:game-center -->
### What the illustrations show
Basis: 6 illustration sheets viewed (img 0490 to 0512), all codes checked; no video.
- The opening symbol is three interlocking dark blue rings, unfilled, over a blue card with a rectangular and circular construction grid (img 0490); all example screens use the same fictional maritime-themed game, with a constant dark blue palette in the Game Overlay (img 0491 to 0509).
- The access point is a translucent circular button with a rocket symbol on the diagonal, alone in the upper left corner of the title screen, with no other control grouped near it and with the game art free around it (img 0491).
- The Game Overlay changes presentation depending on the device without changing the content: on iPhone it covers the entire screen, with a darkened background and a translucent card at the top over the list of shortcuts; on iPad the same list becomes a narrow vertical strip at the trailing edge and the art remains visible over most of the screen (img 0492).
- In the achievements overview, a large counter of completed achievements with friends' avatars opens the screen; earned achievements are circles with a colored image, a date arcing around them and legible text, and locked ones are uniform gray circles with a lock, with no visible title (img 0493). The detail adds the list of players with relative time and the global percentage of who has earned it (img 0494).
- The anatomy of the achievement card is annotated with callouts: circular image centered at the top, large two-line title, smaller description below and players' avatars at the base (img 0495).
- The circular mask is drawn over the square of the image: on iOS, iPadOS, macOS and visionOS the 512 pt circle touches the four edges of the 512x512 pt square (img 0496); on tvOS the 200 pt circle is centered in a 320x320 pt square, leaving a wide square margin outside the mask (img 0497).
- The asset diagrams follow a common language: a square or rectangle in gray, lilac or pink for the image size, a second shape in pink, purple or dashed marking the mask, the crop or the focus sizes, and values in pt annotated (img 0496, 0497, 0500, 0501, 0505, 0511).
- The leaderboard art is a 512x512 pt square from which only a central horizontal strip of 512x312 pt is kept, with excess above and below (img 0500); on tvOS three concentric, centered rectangles show the 659x371 pt image, the 618x348 pt size in focus and the 548x309 pt size out of focus, the last two dashed (img 0501).
- Leaderboards follow the overview-plus-detail pattern: a leaderboard counter with friends' avatars and sections for rankings and friends' activity, with map cards that show a numeric fraction and avatars (img 0498); in the detail, play and challenge buttons side by side, friends and global tabs, numbered ranking with score and, at the end, an invitation to more friends (img 0499).
- Challenges and multiplayer activities share the same annotated card: background art, title, number of players and a dark gradient provided by the system at the base to give the text legibility over the art (img 0504, 0510); the challenge screens show invitations with an accept button, a position highlighted as "3RD" and remaining time with play and add players buttons (img 0502, 0503).
- The challenge art and the multiplayer activity art use the same diagram: a 1920 by 1080 pt rectangle with a central crop area labeled 1465x1080 pt, which preserves the full height and discards narrow lilac margins on the sides (img 0505, 0511); the optional image at the top of the tvOS dashboard is just a 600x180 pt lilac rectangle with the label in the center, with no crop area (img 0512).
- In multiplayer, the overview lists level cards with map, title and player range (img 0506); the detail brings group code, link sharing, contact search with status and a selection checkbox on the right, closing with the join button (img 0507); the game's own UI opens a modal with create code, an eight-digit field in two groups of four and a join button, over the same level screen that appears in full, with random match and invite friends, when the modal exits (img 0508, 0509).
Recorded divergences: in img 0507 the notes point out that the official description "in-game UI starting a multiplayer activity" corresponds better to img 0509, though the content of 0507 is consistent with the invitation section.
<!-- /visual:game-center -->

## Generative AI (slug: generative-ai)

### What it governs
Design principles for incorporating generative artificial intelligence into apps and games: responsibility, transparency, privacy, model/dataset choice, handling of inputs and outputs, and continuous improvement.

### Why
The key principle, defined right at the start, is "Responsible AI": intentional design and development that considers the direct and indirect impacts on people, systems and society, because generative AI is unpredictable by nature (small changes to the input, or even the same input repeated, produce very different results, unlike classic programming). This justifies almost all the rules that follow: keeping people in control (allowing them to discard, undo, redo) follows from the idea that AI manipulates and creates content, but decision-making agency remains human. The insistence on transparency (never deceiving someone into thinking they are interacting with a human) and on privacy (processing locally when possible, asking permission before using personal data) reflects that sensitive data frequently feeds or is processed by these models. The rule about bias and inclusion comes from the fact that models learn from data and tend to favor the most common information, which can reproduce harmful stereotypes if there is no deliberate correction. The rules about hallucination (communicating that content may contain errors, avoiding asking for factual information without confidence that the model has access to verified data) derive from the recognition that generative models "know" how to produce plausible content, but not necessarily true content.

### Do and avoid
General best practices
- Design the experience responsibly, considering direct and indirect impacts on people, systems and society.
- Keep people in control: honor requests within scope, handle sensitive content with care, allow discarding unwanted content, undoing or redoing transformations; clearly identify when and where AI is used.
- Ensure an inclusive experience: ask people to provide the necessary information instead of inferring personal or cultural characteristics; seek clarity before assuming anything that could lead to common stereotypes (gender identity, types of relationship); test with a diverse set of people.
- Offer generative features only when they bring clear, specific value (time savings, better communication, enhanced creativity), not in every situation.
- Ensure a good experience even when the generative feature is not available or the person chooses not to use it; consider offering a non-AI-based fallback.

Transparency
- Communicate where the app uses AI, so the person consciously chooses to use the feature; never deceive someone into thinking they are interacting with or seeing content authored by a human when it is actually AI; align disclosure with local regulations.
- Set clear expectations about what the feature can and cannot do, for example with a brief tutorial or curated suggestions in open-ended features such as search or prompt-based generation; if there are known limitations, warn in advance and explain why inferior results occur.

Privacy
- Choose the appropriate model type: on-device models keep information on the device, respond quickly and work offline; server-based models are worthwhile when the feature requires more processing power or greater context; always weigh privacy together with capability and performance.
- In server-based processing, process as much as possible locally, minimize what is shared, be transparent about what is sent and how it may be stored or used for training.
- Ask permission before using personal information and usage data; use the minimum necessary; offer a clear way to opt out; ask for explicit permission if sensitive data is used for model improvement or storage; apps for children have stricter rules and laws.
- Clearly disclose how the app and its model use and store personal information; explain benefits concisely, specifically and in an easy-to-understand way; clarify whether the model uses personal information for training.

Models and datasets
- Carefully assess the model's capabilities, since some have general knowledge and others are trained for specific tasks; get hands-on experience with models and data as early as possible; consider that some model types may be unavailable depending on device compatibility, network access and battery level.
- Be intentional when choosing or creating a dataset: choose data that includes diverse representation; understand the origin and the way the data was collected; ensure relevant licenses for data that is not your own; offer appropriate choices when using people's data; set aside time for testing and evaluation, since real-world datasets tend to be imperfect and can propagate bias and misinformation.

Inputs
- Guide people on how to use the generative feature, for example by offering diverse, predefined input examples.
- Increase awareness of hallucinations and minimize their chance: hallucinations occur when the model produces plausible but invented content; clearly communicate that AI-generated content can contain errors; avoid asking for factual information unless there is confidence that the model has access to verified and up-to-date data; avoid using AI-generated content in situations where a possible hallucination could misinform and cause harm.
- Consider consequences and ask permission before performing irreversible or potentially problematic tasks; avoid automating destructive actions (like deleting photos) or actions that are hard to reverse (like making a purchase on the person's behalf); generally ask for confirmation before significant actions; review and follow model-specific usage policies and each locality's regulatory policies.

Outputs
- Make it easy to refine or revert generated results, acknowledging when corrections take effect, for example with controls like Edit, Undo, Retry or Adjust near the generated content.
- Help people improve requests when blocked or with undesired results, minimizing blocked or limited output by teaching how to succeed more on the next attempt (example cited: Image Playground responds "Unable to use that description" for harmful content).
- Reduce unexpected and harmful results with careful design and thorough testing, considering scenarios of accidental and intentional misuse, poorly formed, vague or ambiguous requests, and personal, sensitive or controversial topics.
- Avoid replicating copyrighted content; reduce the chance by building on models that already protect against this and carefully curating inputs; consider letting the person choose among pre-approved prompts or explicitly instructing the model to avoid imitating certain content or style.
- Consider processing time (latency) in the design; generative models tend to take longer than non-generative models (like body position tracking in ARKit and the Vision framework); design a loading experience or generate in the background while the person uses another part of the app.
- Consider giving specific and reassuring feedback during generation, describing what is actually happening (for example, "Finding substitutions for ingredients" instead of "Processing…"); if something goes wrong, describe it in plain language and offer a clear next step.
- Consider offering alternative versions of results, giving the person a greater sense of control (example cited: Image Playground generates multiple images representing a person, allowing the preferred one to be chosen).

Continuous improvement
- Consider ways to improve the model over time, adapting it to people's behavior, responding to feedback and incorporating new data; some improvements (like updating the blocked words list) can be made frequently and independently of the app's development cycle; plan fine-tuning, retesting and prompt engineering when updating to a more capable base model; if training your own model, retrain it with additional data.
- Allow people to share feedback about results, which helps identify unexpected problems; always make feedback voluntary; position the feedback mechanism in a clear location that does not interrupt the experience; consider a quick way to give positive/negative feedback (like thumbs up/down) and also a way to share detailed feedback.
- Design flexible and adaptable features, since generative AI is a rapidly evolving technology; consider separating the model from the user experience so you can swap models over time while keeping the same experience.

### Exact specifications
No number, measurement, duration or default value is present in the text (the article is entirely qualitative/strategic, with no specifications of dimension, contrast or duration).

### Platform differences
No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

### Links to other articles
Cites Inclusion and Accessibility, Requesting permission, Loading, Multiple options, Explicit feedback, Implicit feedback, and the developer documentation Apple Intelligence and machine learning, Foundation Models, Core AI, plus the reference "Acceptable Use Requirements for the Foundation Models Framework".

---

<!-- visual:generative-ai -->
### What the illustrations show
Basis: 1 illustration sheet viewed (img 0527), code checked; no video.
- The opening symbol is a diagonal pencil in solid dark blue, surrounded by three four-pointed stars of different sizes, distributed asymmetrically around the tip and the body (img 0527).
- The card has a gradient from violet blue on the left to sky blue on the right, with an overlaid rectangular and circular construction grid, the same pattern as the opening illustrations of pages like Feedback, File management and Focus and selection (img 0527).
- The sparkle linked to generative AI appears repeated at three scales, not as a single fixed icon; outside of this sketch, the page does not illustrate a screen, control, loading state or generation flow (img 0527).
<!-- /visual:generative-ai -->

## What this group reveals about the Apple way

1. Brand recognition is treated as a pixel-level protected asset: AirPlay, Apple Pay and App Clip Codes share the same rule structure ("never alter the provided artwork", "don't rotate, don't add glow, don't change proportion", "maintain minimum clear space") because any third-party variation dilutes the trust the user places in the symbol (slugs: airplay, apple-pay, app-clips).

2. Apple systematically prefers to provide the ready-made component (media player, payment button, coaching view, achievement card) and treats customization as an exception to be justified, never as a starting point (slugs: airplay, apple-pay, augmented-reality, game-center).

3. Terminology is standardized with near-legal rigor: each technology has an explicit list of correct and incorrect terms (AirPlay as a noun never a verb, "Game Center" never "GameKit", "Achievements" never "Trophies"), revealing that Apple understands inconsistent language as a risk to the unified experience across apps (slugs: airplay, apple-pay, game-center).

4. Privacy functions as an architectural constraint, not as an additional legal notice: App Clips erase data between launches, CareKit centralizes everything in system settings, Generative AI requires local processing when possible and explicit permission before using sensitive data (slugs: app-clips, carekit, generative-ai).

5. Contexts of divided attention (driving, augmented reality) generate the group's most protective rules for physical and cognitive safety: CarPlay prohibits any dependency on an unlocked or accessible iPhone, and Augmented Reality calls for a gradual introduction of movement and attention to the person's comfort and safety (slugs: carplay, augmented-reality).

6. The illusion or credibility of an experience has exact technical parameters when Apple defines them: 60 scene updates per second in AR, a 20:1 reading ratio (ideal 10:1) in App Clip Codes, a CIELab color delta of 2.5 in printing. When the ruler exists, it is given as a number, not an adjective (slugs: augmented-reality, app-clips).

7. Where the technology handles money or health (Apple Pay, CareKit), the documentation is the group's longest and most prescriptive, with tables of error messages, required states and detailed exception flows, reflecting that the cost of a design error in these domains is higher than in, for example, AirPlay or CarPlay (slugs: apple-pay, carekit).

8. Apple repeatedly asks for a "fallback" or plan B when the technology in question might fail or be unavailable: App Clip with the full app, Generative AI with a non-AI path, AR with subtly readjusted positioning, Game Center with the game working even without a connected account (slugs: app-clips, generative-ai, augmented-reality, game-center).

9. All seven platform-specific technologies (airplay, always-on, app-clips, apple-pay, carplay, carekit, game-center) have a standardized "Platform considerations" section that explicitly states where the feature is not supported, revealing an editorial discipline in the HIG of never leaving a technology's coverage across iOS, iPadOS, macOS, tvOS, visionOS and watchOS implicit.

10. In recent and still unstable domains of the ecosystem (generative-ai is the newest in the group, with a "New page" dated June 2025), Apple writes principles and ethical stances instead of numerical specifications, unlike mature technologies like Game Center and Apple Pay, which already accumulate tables of exact dimensions (slugs: generative-ai, game-center, apple-pay).

## Reading evidence

| File | Lines read | Read to the end |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/airplay.md | 77 (file with 77 nominal lines, last content line is 78 in Read) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/always-on.md | 35 (last content line is 36 in Read) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/app-clips.md | 202 (last content line is 203 in Read) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/apple-pay.md | 242 (last content line is 243 in Read) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/augmented-reality.md | 134 (file ends at line 135 in Read, with no change log section) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/carekit.md | 127 (last content line is 128 in Read) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/carplay.md | 73 (last content line is 74 in Read) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/game-center.md | 177 (last content line is 178 in Read) | yes |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/generative-ai.md | 71 (last content line is 72 in Read) | yes |

All 9 files in the group were read in full in a single Read call each, with no truncation reported by the tool (no limit-reached warning appeared in any of the returns). No article in the group is merely a collection index; all have their own complete text.
