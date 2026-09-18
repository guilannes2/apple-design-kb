# meet-with-apple

## Design with SwiftUI (id: meet-with-apple_270, 25.2 min)

Basis: transcript and 17 of 17 frame sheets viewed, codes checked. Automatic local transcription done with Whisper, not Apple's official one; proper names and terms may have mishearing errors. Source: https://developer.apple.com/videos/play/meet-with-apple/270/.

Central thesis: A good app starts with structure: first content, sections and navigation are decided, then layout, and only then visual design. SwiftUI's native components already handle a good part of the design decisions (hierarchy, alignment, proximity, color, accessibility), so the designer should let them do the heavy lifting and put personality only in chosen places, without harming usability.

The design process Apple describes:
1. Navigation first. The speaker says she designed the example app (a travel wish list) from scratch and started by thinking about navigation, because deciding content and functions gives a structure to build with clarity and shows how to use the top bar (uncertain term in the automatic transcription) and the toolbar.
2. Brainstorm: list everything the team wanted the app to have and do, with all ideas accepted at this stage.
3. Simplify, keeping only what is essential for this type of app: create trips, add photos, search.
4. Take a step back and group related ideas: trips with activities; progress with the celebration of completed trips.
5. Turn the groups into the app's three main sections, named wish list, goals and search. The exercise works both for a new app and for revising an existing one.
6. Carry the structure to the navigation components: the top bar for the first-level sections and the toolbar to act within a section.
7. Layout: bring the content to the screens and decide how to present it, choosing between lists and collections according to the content and what people need to do with it.
8. Visual design: text styles, semantic colors and consistency, which according to the talk are the three aspects with the greatest impact and the earliest.
9. Final touch: go back and check that all elements are aligned and with consistent spacing. Then the talk moves on to consistent use of components and coherence of images.
10. Only then code: define or evaluate the structure and navigation, use the components with intent, and so start programming knowing exactly what is being built.

Principles stated and why:
1. Do the structuring exercise before building. Why: it organizes thinking and turns loose brainstorm ideas into connected screens, ready to build; in workshops with developers, according to the speaker, it always opens people's eyes.
2. Keep the number of tabs in the top bar (uncertain term in the automatic transcription) low. Why: it stays simple and predictable and reduces decision-making; when opening the app the person knows exactly which options they have. Apps that keep stuffing every new function into the bar become complex, and few people like that.
3. Keep the top bar native. Why: SwiftUI's components bring built-in behaviors, such as animations and accessibility support, that are easily lost when customized. There are many other places in the app to express personality; the top bar is not one of them.
4. Use clear symbols and labels that match what is inside each tab.
5. In the toolbar, minimize the number of actions and use familiar symbols. Why: it stays easy to scan; with too many items, people do not understand what they are expected to do first. Solution given: hide the less common or more advanced actions in the more menu.
6. Use the toolbar's prominent style on at most one action per screen. Why: it adds color and creates an immediate focal point; if everything is important, nothing is.
7. Keep the toolbar native. Why: adding things like a background competes with the content, with the functionality and with the morphing effects.
8. Choose list or collection according to the content and the task. Why: both are flexible, but one serves better than the other depending on what is being shown and what the person needs to do.
9. In collections, choose images that add value and titles of consistent length. Why: most of the content is off screen, so title and image set the expectation and invite scrolling; random images, that do not look curated, take credibility away from the content; titles of different sizes leave the layout clumsy and misaligned, harming the collection and also the vertical scroll below it. Recommendation: define rules for the collections' content.
10. Use the system's text styles, called textiles in the talk (uncertain term in the automatic transcription), choosing the right style for each purpose and applying it consistently. Why: they establish ready-made hierarchy and favor reading across different screen sizes and conditions; consistent use leaves each screen more balanced and polished, and on seeing a familiar style the person knows what that content means.
11. Adopt Dynamic Type. Why: many people use larger styles for comfort or need, and with Dynamic Type the styles keep the same name, just consistently larger.
12. Keep typographic variant choices to a minimum. Why: the interface looks intentional and the app becomes easier to maintain and grow; otherwise too many styles and variants pile up and doubt arises about when to use each one.
13. Use semantic color for state and feedback, and do not use the accent color, nor colors similar to it, as decoration. Why: otherwise people do not know whether that is interactive or whether it has some meaning.
14. Do not overdo customizing the system's colors, especially on buttons and controls. Why: those colors adapt on their own to light and dark mode, to liquid glass and to different screen environments.
15. If using a color outside the system, ensure sufficient contrast, test against different backgrounds and provide a value for increased contrast, and keep testing. Why: keep the app expressive without affecting usability.
16. Align all elements and space them consistently. Why: the design looks polished, balanced and professional, and this supports how people absorb information and decide the next step; components crammed into little space create stress, and an interface that breathes gives room to process.
17. Use the native components the same way on every screen and do not offer several ways of doing the same thing. Why: people already know how the component works, where they saw it and what is expected of them; and it simplifies development, with fewer components to build. The talk notes that offering several ways sometimes happens when someone gets excited creating a new screen and starts from scratch.
18. Give coherence to the images and illustrations. Why: they should look part of the same brand and the same collection.
19. Let SwiftUI, called CPI in the talk (uncertain term in the automatic transcription), do the heavy lifting and then add personality, creativity and humanity. Why: according to the speaker, SwiftUI handles many of the design decisions for her. In the closing, she says she hopes the talk's tips reduce the process's uncertainty a bit and give room to be creative at the start, decide, brainstorm and then go to code.

Concrete interface-building techniques, with exact numbers when spoken:
1. Navigation, top bar (uncertain term in the automatic transcription): shows the first-level sections and stays visible on every screen; it is used to move around the app. The example app has three main sections.
2. Navigation, toolbar: acts within a section and has three elements. First, the title of the current view, which indicates where the person is and gives context and tone to the content. Second, the controls for the screen's most important actions; the primary action, create trip, sits in a control in the top right corner. Third, navigation controls, such as the back button in the trip detail, which goes back one level to the wishlist.
3. Toolbar: less common or advanced actions go into the more menu; the prominent style, which adds color, applies to at most 1 action per screen; no extra background on the bar.
4. Symbols: come from the SF Symbols app, Apple's icon library with more than 7,000 symbols that can be copied and pasted into the design or the code. In the talk, the toolbar calls for familiar symbols, referred to as sub-symbols (uncertain term in the automatic transcription).
5. Resources cited: the Human Interface Guidelines, which the talk abbreviates as The Hague (uncertain term in the automatic transcription), described as the home of design guidance for every Apple platform and the first stop for questions; the link is in the design section of the developer website, which also has the Apple Design Resources, whose native component library the speaker says she uses in almost every app she has designed.
6. Layout with lists: suited to text-based content with many items, because they help scan quickly. Edge-to-edge style used in the trip's activities. Grouped style (group style) when categorizing is needed: the inset and the rounded corners separate the categories. The talk mentions the common confusion between S2S (uncertain term in the automatic transcription; from context, the edge-to-edge style) and inset.
7. Lists, accessories and controls: accessories such as images and subtitles help recognize items without reading line by line; controls such as the selection button allow acting without going to another view. Control types cited: steppers, toggles, sliders, among others.
8. Layout with collections: suited to browsing photos, videos or products. In SwiftUI, according to the talk, collections are basically stack views with a scroll view that lets the content extend past the screen and invites scrolling. In the wishlist tab, whose main purpose is navigation, the layout uses several collection variations with the photos people uploaded.
9. Principles the components already handle: hierarchy, alignment and proximity.
10. Typography: the system's text styles; Title 3 for every section title, such as Summer Glow; support for Dynamic Type; the system's SF Pro font throughout the app; expanded variant for emphasis in titles, aiming for a sporty feel; condensed variant, called condense in the talk, used only sparingly in some overlays.
11. Color: indigo as the accent color, applied to completed activities and the selected tab in the top bar; background and separator colors were not defined, they come from the native components; the only color chosen was the accent color. Neon green, a non-semantic color outside the kit, reserved for emphasis in progress indicators and subtitles, with contrast tested against different backgrounds and its own value for increased contrast.
12. Consistency: progress indicators reuse the same accent color and the same shape, just a bit smaller.
13. Images: place side by side and compare lighting, level of detail and overall mood; adjust until they look like the same brand; if they look like the same collection, trust intuition. In the example, the direction was dynamic skies, with the subject generally smaller or interacting with the space, and the interface more prominent than the photos.

Examples cited:
1. The travel wish list app designed by the speaker with the team and the engineers, with the wish list, goals and search sections; it shows the whole process of brainstorming, simplification and grouping turning into navigation, and that the design had a very close translation into code.
2. An example of a crowded top bar, which makes the app look more complex than it is; it teaches keeping few tabs.
3. The wishlist tab with a rainbow symbol: there is no universal symbol for a wish list, so the rainbow was chosen for being recognizable and conveying hope, the trips one dreams of taking.
4. The ghost tab (uncertain term in the automatic transcript), with a more explicit symbol that matches the label and has the same shape as many of the collectibles inside it.
5. The wishlist screen with the view title and the create trip control in the top right corner, and the trip detail with a back button.
6. A toolbar with too many items, fixed by hiding actions in the more menu; and create trip as the only prominent action, because a trip list app with no trips makes no sense.
7. The trip's activity list in edge-to-edge style, and an example in grouped style that, according to the speech, is not in the app and was shown only to clarify when to use each style.
8. An example of a collection with random images and titles of different sizes, which loses credibility and becomes misaligned, including in the vertical scroll below.
9. The Summer Glow section as a section title in Title 3.
10. Completed activities and the selected tab in indigo; neon green in progress indicators and subtitles; smaller progress indicators reusing color and shape.
11. The example images with dynamic skies, provided in the code so the pattern followed can be seen, although in the real app people upload their own photos.
12. Names cited: Kurt (uncertain term in the automatic transcript), who would speak later about the morphing effects, and Leah (uncertain term in the automatic transcript), to whom the speaker hands the floor back at the end.

Quotes:
1. "if everything is important, nothing is important."

<!-- visual:meet-with-apple_270 -->
### What the images show
Basis: 17 of 17 frame sheets viewed, all codes checked.
- The talk is organized visually by a three-topic agenda (Navigation, Layout, Visual design) in which the current item stays highlighted and the others are in gray, with internal submenus in the same pattern, which gives three levels of structure on the screen; the example app appears right at the opening with the Wishlist icon in a rainbow diamond and three iPhone screens (map with trail, activity list, Goals screen with hexagonal badges), and the closing is a next-steps slide that asks to establish a good foundation before coding (sheet 0001, q0003 to q0009; sheet 0002, q0010 to q0012; sheet 0017, q0146 to q0150).
- The structure exercise is shown with real post-its, in countable stages: 14 loose notes in the brainstorm, 8 after simplifying, the remaining ones stacked into three clusters and, finally, labeled as Wishlist (five notes), Goals (two) and Search (one); the speech describes the process without giving these counts (sheet 0002, q0013 to q0018).
- The slide names the component Tab bar, a term the transcript flagged as uncertain. The sequence of judgment is explicit: a bar with five labeled tabs (Wishlist, Activities, Seasons, Map, Goals) gets a yellow alert icon; a custom bar with two colored pills and a separate search button gets a red X alongside the principle of keeping the native look; the plain native bar, with an icon and label per tab, gets a green check alongside the principle of using clear symbols and labels (sheet 0003, q0024 to q0027; sheet 0004, q0028 to q0034).
- The supporting tools appear as real screenshots: the tab bars page of the Human Interface Guidelines with a category sidebar and a best practices section, the Apple Design Resources page with the UI Kit and App Icon Template templates for iOS 26, and the SF Symbols app with categories on the side, a symbol grid and a weight selector (sheet 0004, q0036; sheet 0005, q0037 to q0041).
- The toolbar is taught with the API name overlaid on the mockup: the .navigationTitle annotation pointing to the title of the Wishlist screen and, next, the ToolbarItem label on an annotation line of the same mockup, which has the blue "+" button in the corner; then a toolbar with six icons (back, plus, pencil, map marker, share, heart) marked with a red X; and finally the "+" alone inside a filled blue circle with the .prominent annotation, against the plain outline icons (sheet 0005, q0045; sheet 0006, q0046 to q0054; sheet 0007, q0055 to q0058).
- For lists, the screen contrasts a continuous activity list, with selection circles on the left and no groups, with the same list in GroupedListStyle, divided into the Landmarks and Sports sections in rounded-corner cards; the name GroupedListStyle appears as an annotation on the slide (sheet 0007, q0063; sheet 0008, q0064 to q0067).
- The anatomy of a list row is drawn with straight lines connecting label and part: Image on the photo thumbnail, Subtitle on the secondary text and Selection button on the blue selection circle, with one item marked and another not; next comes a catalog of controls in rows with Pop-up button, Stepper, Toggle and Slider (sheet 0008, q0068 to q0072; sheet 0009, q0073).
- Collections appear in the Winter Wild section with photo cards with overlaid captions; with the mockup scrolled, more cards appear along with the ScrollView and LazyVGrid annotations over the structure; a later diagram points Section title to the header and Card title to the captions (sheet 0009, q0075, q0076, q0080 and q0081).
- The poorly curated collection is shown before the fix: a red X on the slide next to four cards with generic images that are barely related to each other (palm tree icon, circular photo, almost empty green cards), then with long-sentence captions on the first two; in the corrected version of the Fall Drift section the cards carry real landscape photos filling the frame, under the principle of keeping consistency for scannable collections (sheet 0010, q0083 to q0087).
- The typographic hierarchy is annotated twice on the same Summer Glow screen: first by system style (Title 3 on the section title, Subheadline on the description, Footnote on the card captions), then by family variant (SF Pro Expanded on the title, SF Pro on the subtitle, SF Pro Condensed on the card captions), with the bullets for supporting Dynamic Type and minimizing the number of typefaces; before that, the entry of the Visual design section uses a black full-screen transition slide (sheet 0011, q0095 to q0099; sheet 0012, q0100 to q0108).
- The indigo accent color is annotated in two state uses on the same screen: Completed on the filled checks of completed activities and Selected tab on the active Wishlist tab, under the bullets for describing function and adapting dynamically; another diagram gives the names label for the text, systemIndigo for the selection circles and Separator for the dividing line (sheet 0013, q0112 to q0117; sheet 0014, q0118).
- Non-semantic color appears as lime green restricted to progress bars, in cards such as Spring Explorer "2 of 3" and Explore Cambodia with 50% and the label TRIP ACTIVITIES, under the bullet for using non-semantic color sparingly (sheet 0014, q0120 to q0123).
- Spacing is shown with measurements: blue guides in brackets around a hexagonal icon on the Goals screen and, on the Summer Explorer achievement card, annotations of 40px, 20px and 10px on the margins around the title, the description and the next-milestones section; the speech does not cite values (sheet 0014, q0125 and q0126; sheet 0015, q0127 and q0128).
- Component reuse is proven side by side: three trip detail screens with the same structure (cover photo, progress bar at 33%, activity list with marking) and different photos, under the bullets for reusing components and keeping images coherent; then the view pulls back to six screens in a row that form the app's map (Wishlist, trip detail, Activities, Goals, Search with keyboard) (sheet 0015, q0135; sheet 0016, q0136 to q0143).
- Interaction states that the speech does not detail appear in passing: the Wishlist screen in editing mode, with the system keyboard, X and Edit Trip buttons and confirmation in a blue circle with a check (sheet 0014, q0119); and a transition frame in which the Date, Title and Completed form fields overlap fragments of the list, next to a TRIP ACTIVITIES screen with the add activity button in the footer (sheet 0016, q0144).
Visual proportion: by the notes, 14 of the 152 frames show only the audience, the presenter with no slide or a dark transition frame, and another 2 are close-ups of the presenter with cut-off slide text (q0039, q0050); the rest carry slides, annotated mockups, tool screenshots or logos.
Recorded divergences or limits: the first tab bar has icons that are hard to read, identified only in the zoom of q0027 (sheet 0003); some slide texts appear cut off over the presenter (q0039, q0050, q0104, q0106) and q0042 is a dark frame with no legible text.
<!-- /visual:meet-with-apple_270 -->

## AllTrails: Momentum without a rewrite (id: meet-with-apple_274, 14.2 min)

Basis: transcript and 11 of 11 frame sheets viewed, codes checked. Local automatic transcript made with Whisper, not Apple's official one; proper names and terms may have hearing errors. Source: https://developer.apple.com/videos/play/meet-with-apple/274/.

Central thesis: James Graham, CTO of AllTrails, argues that a large, mature UIKit app can achieve modern speed without rewriting anything, letting SwiftUI in wherever it fits instead of imposing top-down adoption. What supports this is treating interoperability as infrastructure and measuring momentum (smaller PRs, faster reviews, fewer regressions), not how much of the code has already been converted.

The design process Apple describes: The talk is an engineering one and describes AllTrails's adoption path, in this order. 1) Starting point: the product's scale and constraints, which according to him are necessary to understand the technical decisions. 2) When SwiftUI arrived, AllTrails was already a large, mature and successful UIKit app, with weekly release cycles and free and paid experiences; rewriting was not an option. 3) SwiftUI came in quietly, with no mandate and no roadmap item, through a sandbox for low-risk experimentation, prototypes and isolated services, to learn the framework without betting the release candidate on it. 4) The first real decision was not choosing between UIKit and SwiftUI, but how the two thrive together: early investment in interoperability, with a bridging pattern established from the start as a process decision, so the boundaries would be clear. 5) Two parallel tracks formed naturally: UIKit on the heavy lifting, SwiftUI on isolated, new surfaces. 6) The design system came to be built in SwiftUI, in partnership between design and engineering, with all new features using this system. 7) The team noticed that SwiftUI started influencing the architecture (view models and smaller PRs); that was the turning point where it stopped being an experiment and started becoming the default choice, adopted voluntarily by the engineers. 8) Success came to be measured by reduction in lines of code per feature, faster iteration cycles and fewer regressions in the features isolated in SwiftUI. 9) Recognition that interoperability is infrastructure, with investment in hosting wrappers, shared animation bridges and a unified theme. 10) Current state: AllTrails is not migrated to SwiftUI; it is a hybrid system with direction. At the end, he poses three questions for other teams to evaluate adoption in their own context: is interoperability treated as infrastructure; does the new tool reduce cognitive load; do you measure momentum and not conversion.

Principles stated and why:
Do not rewrite the app. Why: at the scale they operate, a rewrite, whether done through engineering effort or an AI-native workflow, introduces enormous risk; in a mature app it was not viable, either technically or organizationally.
Legacy code is not a problem to fix. Why: UIKit was the foundation that enabled the scale; so it wasn't possible to stop everything, the app had to be maintained and updated while in use (the metaphor used is updating mid-trail).
You can't ship broken code. Why: the diversity of members, from the casual walk to the full-day hike navigating offline with no cell signal, creates rigid constraints on reliability, battery duration and interface performance; and every technical decision affects millions of members on different devices, regions and connectivity levels.
Let SwiftUI adopt the team, don't force adoption. Why: engineers chose SwiftUI for new work because it had less friction and reduced cognitive load; when the choice is writing 40% less code, adoption sustains itself. He sums up that SwiftUI spread because it was the fastest path, not because of an order.
Don't rewrite stable, tested screens just to switch frameworks. Why: in a mature app this doesn't make sense; new investment goes where it delivers clear gains for the user and for speed.
Use SwiftUI where it fits best. Why: self-contained surfaces with dynamic state and interface updates match the declarative model; experimental surfaces can evolve fast without strong coupling to the app's central architecture.
Interoperability is infrastructure. Why: if it is fragile or improvised, adoption stalls the moment real product pressure appears; when the bridge is solid, SwiftUI stops feeling new and starts feeling foundational.
Adoption is not a binary decision. Why: the useful question is not whether to adopt SwiftUI, but under what conditions adoption creates momentum instead of risk; what worked (fewer bugs, faster delivery, better scale across teams) came from a set of deliberate decisions, not an isolated technical choice.
Measure momentum, not conversion. Why: momentum shows up in smaller PRs, faster reviews and fewer regressions, not in the percentage of code converted.
UIKit and SwiftUI can coexist safely. The why given is the experience itself shown in the talk.
Choose SwiftUI for speed, not because it's "cool". Why: in the Apple Watch app the choice allowed faster iteration on a complex surface without touching the legacy navigation logic.

Concrete interface-building techniques, with exact numbers when stated:
What SwiftUI promised and what the team wanted: cleaner state management; views that update themselves when data changes, eliminating the class of bugs where the interface falls out of sync with the model; less code, 40% less than the UIKit equivalents; and live previews, to iterate design changes instantly.
Interoperability bridge: take a feature in SwiftUI, such as the "trail coordinator" (term uncertain in the automatic transcription), wrap it in a hosting view, place it inside a regular UIKit stack view and then add it to the scroll view. According to the talk, some sections of the hosting view on the page contain the SwiftUI subviews.
Division of responsibilities: UIKit handles the app's lifecycle, navigation and complex or deeply integrated surfaces; according to the talk, it remains great for deep interface customization, such as complex collection views and elaborate navigation bars. SwiftUI takes isolated and well-bounded surfaces, rendering-heavy views and new experiments.
Design system in SwiftUI called "Denali" (term uncertain in the automatic transcription): the core components (buttons, segments, controls, badges) are built in SwiftUI and can be seen inside the app in debug mode. What used to take hundreds of lines of boilerplate now takes a fraction of that; adding a new variant or adjusting spacing is a simple change that propagates everywhere, allowing the design system to scale without bloating the code.
Interoperability infrastructure cited: hosting wrappers, shared animation bridges and unified theming.
Effects measured in the architecture: view models got smaller, often by a third, because glue code to keep interface and state synchronized stopped existing; much less explicit plumbing (fewer publishers, fewer operators, far less lifecycle management), because SwiftUI propagates state; since interface, state and behavior stay together, changes touch fewer lines; interface PRs got 30 to 40% smaller and code reviews got visibly faster.
Success metrics used: reduction in lines of code per feature, faster iteration cycles and fewer regressions in features isolated in SwiftUI.
AllTrails context numbers stated in the talk: more than 90 million members in the community, 500,000 trails worldwide, more than 1.9 billion miles logged, 14 languages and weekly release cycles.

Examples cited:
The AllTrails home page over the years, shown as an example that the app constantly evolves with new surfaces and more feature depth.
The photo tour feature, which highlights photos along the trail, cited when introducing the product.
The casual member profile (an easy, relatively flat afternoon walk with a view of a local lake) against the practitioner tackling the full-day "half-dome" (term uncertain in the automatic transcription) trail navigating offline; it teaches where the reliability, battery and performance constraints come from.
The trail page and the community activity view, kept in UIKit for being complex, deeply integrated surfaces.
The trail review flow, in SwiftUI for being a self-contained surface with dynamic state, which matches the declarative model.
The "ask-the-trail-anything" experience (term uncertain in the automatic transcription), built on Apple Intelligence, in SwiftUI for being a new, experimental surface that needs to iterate fast without coupling to the central architecture.
The Denali design system seen in the app in debug mode, as a case where SwiftUI shines: core components with much less code and adjustments that propagate.
The Apple Watch app, with the compass and map surfaces in SwiftUI and the map using MapKit; it shows that critical, performance-sensitive functionality can ship with modern architecture.
The plant identification feature, 100% in SwiftUI, as an example that SwiftUI defines the app's growth.

Quotes: "UIKit wasn't a problem to be fixed. It was the foundation that enabled our scale." and "you don't need a rewrite to make progress. You need direction."

<!-- visual:meet-with-apple_274 -->
### What the images show
Basis: 11 of 11 frame sheets viewed, all codes checked.
- The structure of the talk is guided by a single-column agenda next to the presenter, with an opacity hierarchy: the current section item in full white and the others in dimmed gray, switching as it advances (Safe introduction lights up between q0007 and q0009, Adoption tipping point at q0010); the dark title slide has a large title in white, a smaller subtitle in gray and the green AllTrails logo (sheet 0001, q0002 to q0009; sheet 0002, q0010).
- The app screens appear in four iPhone frames in a row, with a search bar, trail cards with photo, green badges and a rounded green Start button; on zoom you see a topographic map with the trail drawn and a bottom card with name, distance, elevation and the Download and Start buttons (sheet 0002, q0011 to q0014).
- The scale numbers are cards with a translucent dark green background, with a large number in white at the top and a small caption in gray below, revealed one by one from left to right (90M, 500,000, 1.9B, 14) (sheet 0002, q0016 to q0018).
- The app's evolution is shown across six iPhones with a green version label (iOS 12, 14 and 26), going from a simple search screen to an interface with category filter chips in the most recent version; the talk only mentions the home page over the years (sheet 0003, q0023 and q0024).
- The list of SwiftUI benefits is revealed item by item, with the active item in white and the following ones in dark gray, almost invisible, in two columns with the question on the left and the benefit on the right (sheet 0003, q0026 and q0027; sheet 0004, q0029).
- The trail detail screen used as an example has metrics in a two-by-two grid (distance, elevation gain, estimated time, route type), an access notice with an underlined link, a yellow badge for expected weak signal and two buttons at the bottom, a filled green Download and an outlined Map (sheet 0004, q0034 and q0035).
- The bridge pattern is shown in real Swift code with syntax highlighting: a hostingView declaration with HostingView and TrailCoordinator, the creation of a vertical-axis UIStackView and a call to addArrangedSubview; it is the only code snippet in the talk and confirms on screen the name the transcript marked as uncertain (sheet 0004, q0036; sheet 0005, q0037).
- The division between frameworks uses slides with a repeated layout, a large title on the left, a list of three items and two iPhones on the right: UIKit with App lifecycle, Navigation and Legacy Flow; SwiftUI with Isolated surfaces, Rendering-heavy views and Experiments, illustrated by the review flow with stars (4 of 5), selectable chips with a check and a thin progress bar at the bottom indicating the step, and by a community Q&A screen with circular avatars (sheet 0005, q0044 and q0045; sheet 0006, q0046 and q0047).
- The design system appears as a catalog in debug mode across four iPhones labeled Denali Alert, Denali Chip View, Denali Badge, Logo, Logo Co. and Denali Button, each with the component's variations stacked (alerts with a colored icon, rounded chips, badges, filled dark and outlined buttons); the same layout is shown in light mode and then in dark mode, with only the background and surfaces inverted. The screen confirms the name Denali, marked as uncertain in the transcript (sheet 0006, q0049 to q0054).
- The results are statistics slides with the sheet's largest type size: a percentage number in saturated green, a gray arrow pointing down on the left and a white caption below, left-aligned over black; first two in symmetric columns (33% Fewer ViewModel LOC and 50% Less Reactive Plumbing), then one per slide, with 50% Less Reactive Plumbing alone and then 35% Smaller Pull Requests. The screen gives 50% for the reactive plumbing, which the talk does not quantify, and a single 35% where the talk gives the 30 to 40% range (sheet 0007, q0056 to q0060).
- The transition cards always follow the same pattern: a single short sentence, left-aligned, in white over a black background, with no supporting image, such as SwiftUI enters quietly, The codebase didn't flip overnight, Invest in interoperability and Create momentum instead of risk (sheet 0004; sheet 0008, q0066 to q0071; sheet 0009).
- The Apple Watch app appears on two round watch faces: a digital compass with a blue triangular pointer over dark green and elapsed time in the corner, and a miniature trail map with a blue route over a beige and light green background, with the digital crown visible (sheet 0008, q0072; sheet 0009).
- The pair of title on the left and example iPhone on the right repeats three times in a row: UIKit provides stability with an options filter screen with toggles and a bottom action button; SwiftUI defines our growth with the plant identification (a close-up photo of a purple flower, the species name in large type over the image, a descriptive card below); and the AllTrails logo with a photo and trail map. Later, after the question and transition slides, What worked for us shows an iPhone with a push notification in a system card at the top of a screen with a map route (sheet 0009, q0076 to q0081).
- The review questions use a filled green circular seal with the number in white to the left of the text, and the first one is revealed in two opacity phases, from faint gray to full white, in the same position (sheet 0010, q0086 to q0089).
- The brand green repeats as an accent in the highlighted elements: the statistics numbers use the same green as the logo, and the question seals repeat that green; the closing joins the green icon to the AllTrails name in white sans-serif and ends with the translucent apple over the scene fading to gray (sheet 0007; sheet 0010; sheet 0011, q0092 and q0093).
Visual proportion: the 11 sheets carry slides, app screens, design system catalog or code; frames of only the presenter or the audience appear interspersed in at least seven sheets (0001, 0003, 0004, 0007, 0008, 0010 and 0011), and the notes do not allow counting the proportion per frame.
Recorded divergences or limits: only the first two of the three questions appear complete; the sheet ends in a large cut-off text that begins with "Are...", with the third question not legible (sheet 0010, q0090).
<!-- /visual:meet-with-apple_274 -->

## Showcase: Learn how apps are integrating the new design and Liquid Glass (id: meet-with-apple_208, 116.3 min)

Basis: transcript and 81 of 81 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/meet-with-apple/208/.

**Central thesis.** This is the umbrella event: design evangelist Sarah McClanahan opens by explaining the new design and Liquid Glass, four teams (LTK, Slack, CNN, Tide Guide) present their cases (covered in detail in their own cards below), then there is a chat (fireside chat) with Sky Guide, American Airlines and Lowe's moderated by Curt Clifton, and finally a panel with Apple's own design team (Lance Wilson, Caroline Cranfill, Bobby Martin, moderated by a colleague identified as "Mike" in the speech) telling the behind the scenes of how Liquid Glass was designed. This card focuses on the exclusive content of this video: Sarah's introduction, the fireside chat and Apple's internal panel.

**The design process Apple describes.**
- In the opening, Sarah McClanahan explains that the goal of the redesign was to give more emphasis to the app's content, creating a sharper separation between a "functional UI layer" (tab bars, toolbars, controls that should appear when needed and recede when not) and a "content layer" (where brand identity should live).
- In the fireside chat, the three guests describe how they arrived at their own decisions: Chris Laurel (Sky Guide) says the biggest initial concern was performance, because the app's sky view needs smooth animation without dropped frames; they solved it by quickly prototyping (a few days) a Liquid Glass UI inside Sky Guide to verify that performance would be acceptable before moving forward.
- Steve Lindgren (Lowe's) describes how they formed a "small empowered team" of three people (product, UX and engineering) inside a company of 300 thousand associates, with "loose direction" from leadership, and that this team then evangelized the change to the rest of the organization by showing working code instead of static screens.
- Moonhee Kwak (American Airlines) describes how they physically recreated the setup of an Apple Liquid Glass workshop, with developers and designers sitting side by side testing in real time instead of debating abstract ideas.
- In the internal panel, Lance Wilson describes the process as "meticulous iteration", testing the limits of an idea and of what is familiar; for every feature released there are dozens of discarded sketches and prototypes.
- Caroline Cranfill describes the collaboration process between frameworks teams and app teams through "alignment meetings", in which it became explicit what the frameworks would give for free and what each app would need to build on its own; she also describes sessions of physical co-location between designers and engineers looking at the already compiled app, because the Liquid Glass materials were hard to replicate in the design tools themselves.
- The team also describes extensive auditing and testing of components' fundamental metrics (sizes, density) across many contexts before settling on new values, although no final numeric value was cited in the talk (the moderator's question cited "44... 48 or 52 points" only as a hypothetical example, not as an answer).

**Principles stated and the why of each.**
- Native controls "belong to the platform": they were built to support various screen sizes, tap targets, dynamic type, localization and animation "for free", so apps that use SwiftUI and native components since iOS 18 adopt the new design automatically when recompiled against the iOS 26 SDK.
- Unification of the visual language across platforms: motivated by the way users migrate between iPhone, iPad and Mac, and inspired by elements like Dynamic Island and the immersive experience of Vision Pro.
- Reduction of the interface "footprint": hardware evolved (larger screens, thinner bezels), and the old interface layer was taking up more and more of the content's space; Liquid Glass seeks to reverse this.
- Bringing Mac OS window controls to iPad worked, but bringing the colorful iOS toolbar to Mac OS did not work, because of the density of on-screen controls and the Mac's multi-window environment; the team reverted to more monochromatic controls on Mac, and then realized those monochromatic controls worked better back on iOS too.
- Alerts were tested aligned at the bottom of the screen, but went back to being centered, because they are elements that call for the user's pause and attention.
- Search moved from the top to the bottom on iPhone (in apps with and without tabs): the reason cited is reach/ergonomics and the ability for search to animate smoothly into an entry field when tapped; compressing the other tab bar items into a single row avoided the need for a second row of controls.
- Tab bar collapsing on scroll is optional and should be used when the goal is to prioritize content (e.g. reading an article); in other contexts (such as navigation/discovery) it may be preferable to keep the bar more present.
- The San Francisco system font supports more than 150 languages and adapts geometry and spacing according to text size; SF Symbols automatically adapt to reading direction (left to right or the reverse), including symbols with typographic or numeric elements, adapted for around 20 different languages; list components grow in height to accommodate text from taller scripts.

**Concrete interface-building techniques.**
- The content layer should reflect brand identity; Liquid Glass controls "pick up" and visually reflect that content without distracting from functionality. Examples cited by Sarah: the Crumble app shows edge-to-edge brand content; Lucid Motors uses a standard navigation tab bar but with its own visual identity (icons, color and custom interactions) in the content area.
- The Lumy app (daylight tracker) uses a Liquid Glass control to "scrub" (scrub) the time of day and find sunrise and sunset.
- The workout app The Outsiders uses three-tab navigation with standard actions in the top toolbar, but a content layer with data-dense insights.
- App icons: automatic conversion of legacy icons to Liquid Glass on day 1 of launch (even without the developer having updated anything), using smart segmentation logic; Icon Composer allows specifying exactly which layers receive Liquid Glass and configuring translucency, shadows, specular highlights and light source, as well as previewing in "tinted" and "clear" modes. American Airlines used Icon Composer to dissect its logo (abstract eagle) into four groups and test light and shadow, arriving at a subtle reinterpretation of the logo after a first attempt (stretching the lower wing to overlap the beak) was rejected by the brand and legal teams.
- Lowe's kept the brand's characteristic blue bar on each tab's root screens, but completely removed that solid bar on the child navigation screens (product listing and detail), giving screen space back to the content.
- Branding without its own visual "layer": Chris Laurel (Sky Guide) describes that, since there is no other product around the app, "the brand is the app itself", the identity comes from the quality of the experience (smooth animations, responsive controls, attractive imagery, attention to detail), not from brand graphic elements.
- Sky Guide on iPad uses a layout inspired by Apple Maps: an iPhone UI in portrait mode embedded in a sheet on the left side of the screen, with the sky view always visible at the same time, so that configuration adjustments are reflected immediately in the view.
- American Airlines uses a custom segmented control (double, stacked) in the trips tab: a native segment for the specific action of a task, and a custom segment for navigation, inspired by Apple's Photos app (whose API for this pattern was not available), including a notification badge replicated from native behavior.
- Motion/morphing: a button can transform directly into a menu, avoiding the user needing to reposition their hand on the device to complete a related action; the team describes the effect with a biological metaphor of materialization/dematerialization (citing mitosis and meiosis as a study reference).

**Examples cited (apps, screens, components) and what each example teaches.**
- Crumble and Lucid Motors: how brand content and native controls can coexist on the same screen without competing.
- Lumy: how an interactive Liquid Glass control can become a central part of the experience (time scrub).
- The Outsiders: how simple navigation (three tabs, standard toolbar) can coexist with a data-dense content layer.
- American Airlines (icon and header): how to reinterpret a brand logo through Liquid Glass without changing its character, and how to decide to let a logo "scroll out" of the top as the user scrolls the content.
- Lowe's (blue bar): how to remove a highly recognizable brand element from deep navigation screens without losing the familiar "entry point" on the root tabs.
- Sky Guide (layout inspired by Apple Maps): how to make use of a side sheet pattern already validated by Apple itself instead of inventing a new one, even though this pattern is not (yet) a native iPadOS control.

**Up to two short, literal quotes.**
- "Building a plane and flying it at the same time" (Caroline Cranfill, on the collaboration effort).
- "Liquid Glass is beautiful, but it's more than visual craft." (Sarah McClanahan).

<!-- visual:meet-with-apple_208 -->
### What the images show
Basis: 81 of 81 frame sheets opened and viewed, all codes checked.

- In the opening, the example controls appear translucent over colorful content: a player with three circular buttons, the center one larger than the side ones (sheet 0002, q0017); a segmented VIDEO/PHOTO control and a pill-shaped "Select" button over a photo (sheet 0003, q0020 and q0021); a bottom bar with five translucent circular icons over a photo and pill-shaped filter chips with one item selected in blue and a circular search on the right (sheet 0004, q0032 and q0033). On the same sheet a dark menu appears with icons to the left of the items and toggles on the right (sheet 0004, q0035).
- The same introduction catalogs the native components in four translucent white cards labeled Tab bar, Sheet, Controls and Context menu (sheet 0006, q0047) and uses a single control panel (toggle, "+" button, blue slider, gradient slider, One/Two/Three caption) first isolated on the big screen and then inside an iPhone frame (sheet 0001, q0004; sheet 0006, q0053). iOS 7 appears as an old reference: an "iOS 7" icon followed by four old iPhone frames with screens from that system, with flat icons and solid colors (sheet 0001, q0007 and q0008), and then a larger frame with a dial pad (sheet 0001, q0009).
- Third-party apps appear in a fixed format: a large squircle icon on one side and an iPhone frame with the app's screen on the other. In Crumbl the screen moves from the "National Flavors" cover to a product one, showing navigation within the same app (sheet 0005, q0040 and q0041); the format repeats with a bear icon next to a dark automotive app screen (sheet 0005, q0042) and with a sun ray icon next to a dark weather screen (sheet 0006, q0049 and q0050).
- In the LTK case, the screen shows a mockup with the "RUNWAY" logo, Posts, Products and Creators tabs, a percentage indicator and a swatch palette (sheet 0011, q0092); a tree information architecture diagram, with boxes colored by category and yellow at the top level (sheet 0011, q0094 to q0099); SwiftUI code next to the mockup with ".buttonStyle(.glass)" highlighted (sheet 0012, q0103 and q0104); and the "with Runway" and "without Runway" pair, with a "Code complete" stamp over the mockups (sheet 0012, q0105 to q0107).
- In Slack, the difference between frames records the state of a gesture: the message cell slides and turns blue with "Keep Unread", above the fixed Keep Unread (outline) and Mark as Read (filled in green) buttons (sheet 0017, q0149 to q0150); right after, a quick reactions bar appears with translucent circular icons over the keyboard (sheet 0017, q0151 and q0152).
- Still in Slack, the same channel list is repeated across three iPhones to compare three prototyped headers (concentric, capsule and gradient), with constant list anatomy: icon on the left, unread counter on the right, VIP, Mentions and Project Space sections with an expand triangle, and a Home, DMs, Activity and More tab bar with search (sheet 0021, q0183 to q0187). In another trio only the color theme changes (light, dark, orange), keeping the grid and hierarchy (sheet 0022, q0190 to q0192). The iOS 18 and iOS 26 pair shows the solid tab bar turning into a translucent tab bar and header over the same structure (sheet 0020, q0176 to q0178).
- Screen decomposition through leader lines (a label linked by a straight line to a part of the interface) is the most recurring anatomy device: on Slack's iPad, "Improved Menus" and "Windowing" (sheet 0023, q0204); on the iPhones, Conversation Headers, Composer, Create Menu and Tab Bar (sheet 0023, q0206); on the canvas, Viewer Chrome and Canvas Controls (sheet 0024, q0210); in the CNN article, Title, Byline, Image and Paragraph, then Top navigation and Tab bar (sheet 0027, q0235 to q0238). In Slack the labels come in over the screen already shown clean (sheet 0023, q0203 to q0204 and q0205 to q0206; sheet 0024, q0209 to q0210), and the screens come in slides with the month name in large text, from September to December (sheets 0023 and 0024).
- In CNN there is a right-and-wrong pair about where to apply the glass: two iPhones labeled "Nested glass" and "No nested glass" (sheet 0028, q0252), preceded by a Swift code slide with a custom ViewModifier and an "#available" conditional (sheet 0028, q0250 and q0251). The list of learnings grows one topic at a time, swapping the image on the right: a "Liquid Glass padding offset" menu over a red screen (sheet 0029, q0254) and a player annotated with glass in the search and player controls and no glass in the bottom navigation (sheet 0029, q0256).
- In Tide Guide, the anatomy of the floating card over the map appears complete: + and X buttons in the top right corner, a tide curve with high and low points and times, a grid of four metrics with icon and value, and a five-item tab bar with the active one filled in blue (sheet 0034, q0300 and q0301). On the same sheet, a closed tide card gives way to a wind panel with a blue pill day selector, a large numeric value and a mini bar chart, a state change within the app (sheet 0034, q0303 to q0304).
- In the "Identity effects" slides, the same type of wave graph appears in different contexts, inside a mini player and inside a simple card, and another slide with the same title brings a wind graph with bars and a line (sheet 0035; mini player in q0308 and q0309). In a forecast-by-date list, each daily block has a bold date header, a blue-gradient filled curve, a weather icon with a short label and a grid of four times, under a period selector at the top (sheet 0035, q0311).
- The evolution of the same pattern appears in three stages of real Tide Guide screens: context menu in list form with a timeline and size submenu (sheet 0036, q0321 to q0323; sheet 0037, q0325); glass popover with pill-shaped segmented controls, selected item in solid color, blue toggle and item with chevron (sheet 0037, q0326 and q0327, q0329 and q0330); and full screen "Customize Charts" with reorderable list, red remove buttons and drag handles (sheet 0037, q0328).
- Layout over time and across devices: four iPhones labeled iOS 12, 14, 16 and 26 side by side, from the more textual versions to the more visual one, with wave curve and colors (sheet 0032, q0283 and q0284); the same tide graph adapted to laptop, iPhone and watch (sheet 0032); on iPad, a fixed sidebar and a two-column card grid, which the iPhone next to it reduces to a single column (sheet 0036, q0320).
- Alignment and spacing: three screens side by side with a common left edge, the location one with a red "Remove" button at the bottom, the support one with a filled blue Email Support button and actions with an icon on the left, and the settings one with a colored icon on the left and a chevron on the right on each item (sheet 0038, q0335); followed by the system keyboard with search and location suggestions (sheet 0038, q0337) and the slide "Redesign not required." (sheet 0038, q0342).
- The slides themselves use pure typographic hierarchy: agendas where the active item is in full white and the rest in translucent gray, without color or icon (sheet 0008, q0066 to q0072; sheet 0019, q0170; sheet 0033, q0296); statistics in large serif type with ">>" between old and new value and a small sans-serif caption (sheet 0015, q0129 to q0132).
- In sheets 0043 to 0080, the only design artifact that was actually designed is the pair of American Airlines icons labeled iOS 18 and iOS 26, with the same eagle moving from flat graphic treatment to a translucent appearance in layers of light (sheet 0050, q0443 to q0450); other than that, only the staging of two translucent circles that approach and overlap each other (sheet 0052, q0460 to q0463). Shortly before, at the opening of the fireside chat, the identification cards follow the pattern of logo, name and iPhone with the app screen (sheet 0041, q0361 to q0365).

Visual proportion: sheets 0001 to 0038 (the first 52 minutes, with the opening and the LTK, Slack, CNN and Tide Guide cases) are dense with slides, screenshots and mockups, while from sheets 0039 to 0080 (fireside chat and the Apple design team panel, about an hour) almost everything is just stage, panelists and audience, except for the cards in sheets 0040 and 0041 and the icon slide in sheet 0050; sheet 0081 is the final copyright card.

Recorded divergences or limits: in sheets 0064 to 0080 the speech describes a colored toolbar brought to the Mac and alerts aligned at the bottom (0064), a button that turns into a menu (0069 and 0070), component size metrics (0070 and 0071), San Francisco and SF Symbols (0072 and 0073) and the Icon Composer (0079), but no corresponding image appears, and in sheets 0043 to 0063 there is no visible sketch, prototype or measurement annotation; the Swift code in sheet 0028 is small and not fully legible; the Slack laptop mockup in sheet 0018 has low legibility; the tablets in the panelists' hands are always off or out of view; sheet 0081 has only 2 of 9 frames filled in.
<!-- /visual:meet-with-apple_208 -->

## Liquid Glass showcase: Tide Guide (id: meet-with-apple_257, 10.9 min)

Basis: transcript and 9 of 9 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/meet-with-apple/257/.

**Central thesis.** Tucker MacDonald, founder of Condor Digital and solo developer of the tide app Tide Guide since 2018, shows how he adopted Liquid Glass to make the interaction more tactile and fluid without "weighing down" the interface, arguing that adopting updated system components already brings most of the gain, and that a complete redesign is not a prerequisite.

**The design process that Apple/the presenter describes.**
- He sought to apply Liquid Glass where interaction was already central: buttons, the main tide graph, the tide table cards and the hourly graph container.
- He identified "paper cuts" (small frictions) in a context menu pattern with submenus that he already used: each selection quickly rebuilt the entire menu, requiring many taps to configure preferences (timeline, order, graph height). He tried removing the hierarchy and putting everything into a single list, but found that hard to read at first glance.
- He solved this by adopting a glass popover, reusing the same components from the original menu, which keeps the options visible and allows tapping to open a full sheet of reorderable controls; when finished, everything collapses back into the ellipsis menu.
- Conclusion of the process: "my process was more adopt and then redesign" (paraphrase), much of the gains came simply from using the most recent version of the system components, without waiting for a complete redesign.

**Principles stated and the why of each.**
- Interfaces should feel alive without becoming "heavy": expressive and functional effects, not just decorative, literal quote below.
- Concentricity (soft corners consistent with the shape of the hardware) makes screens feel more "welcoming" and "at home", regardless of the device or the screen space available.
- Consistent left (leading) alignment and spacing reduce cognitive load, because they allow quickly scanning the starting edge of each line and recognizing action/content by color and iconography.
- The new positioning of the keyboard and search bar avoids unexpected behavior while typing, which he considers important because text entry is a sensitive point of frustration when something deviates from what is expected.

**Concrete interface-building techniques.**
- Liquid Glass button style: expands and "morphs" under the finger on touch, giving immediate feedback even before releasing; especially useful on small buttons, normally covered by the finger itself when touched, where before it was not obvious that the touch had registered until lifting the finger.
- Day-of-week buttons in the hourly graph sheet: expand and "morph" within the container; the effect is described as "snappy" and, combined with haptic feedback, creates a "moment" of interaction.
- The "identity" variant of glass: does not change appearance until there is interaction. Applied to the main tide wave (when dragging, a subtle, soft highlight appears under the wave) and to the tide graph cards (replacing a scale animation he used before, making the cards more cohesive with the rest of the app and the platform).
- Same "identity" effect applied to the background of the hourly graph containers: when dragging/scrubbing through the hourly conditions, the container "scales" in a tactile way.
- Custom use of the glass material to highlight small details: the selected water level on the tide graph when dragging a finger along the wave, and in the rings of the radar animation on the empty stations screen (when a new user sets up the app for the first time), creating a refraction effect.
- Glass popover for graph settings (timeline, order, height), with the option to open a full sheet and reorder items, and an equivalent custom component for the presets in the tide tables.
- Padding and hierarchy changes applied more broadly, not restricted only to the newest version of the operating system.

**Examples cited (apps, screens, components) and what each example teaches.**
- Tide Guide itself across multiple platforms: "super simple and glanceable" on Apple Watch, and with "more information-dense layouts" on iPad and Mac, teaches that the same brand can have very different information densities by platform, while staying "purpose built" for each one (paraphrase).
- Context menu with submenu (previous version) versus glass popover (new version): teaches that a technically correct pattern (context menu) can generate real usage friction (rebuilding the menu on every selection) that only appears with continued use.

**Up to two short, literal quotes.**
- "without being overweight, expressive and functional without being distracting"
- "my process was more adopt and then redesign"

<!-- visual:meet-with-apple_257 -->
### What the images show
Basis: 9 of 9 frame sheets viewed, all codes checked.
- Direct comparison between generations of the same app: the slide "Design evolution since 2018" lines up four iPhones labeled iOS 12, iOS 14, iOS 18 and iOS 26, each with a real screenshot framed in a device bezel, allowing a side-by-side view of the change in palette, card and graph style (sheet 0001, q0007 and q0008).
- Same interface reorganized by platform: the slides "Meet Tide Guide" and "Designed to be Multi-platform" show iPhone, iPad, Mac and Apple Watch with the same wave graph elements, and the Watch face reduces everything to a single large numeric value with a menu icon in the corner (sheet 0001, q0005 and q0009; sheet 0002, q0011).
- Pair of old and new patterns for the same setting: the traditional context menu appears as a vertical list that opens a submenu with period and size options, and then the same set turns into a glass popover with selection chips and a toggle, without closing the panel on each choice (sheet 0006, q0046, q0048, q0050 and q0052).
- Third step of the same flow: tapping "Customize Charts" opens a full screen with a reorderable list, a drag handle on the right of each row, a red circular remove button on the left and a confirmation mark in the top right corner (sheet 0006, q0053).
- Difference between frames that exposes the interaction state: the same tide graph card appears flat and frontal in one frame and tilted in perspective in another, making visible the effect that only appears during touch (sheet 0004, q0033 and q0035).
- Anatomy of the wind popover: floating card with a circular close button in the top right corner, day-of-week chips with the active day on a solid dark background, a row of sun and moon icons per time of day and a side numeric scale (sheet 0004, q0029).
- Anatomy of the map screen: bottom navigation bar with five labeled items and the active item marked by a blue pill, plus a location popup as a floating card with rounded corners, shadow and two action buttons at the top (sheet 0003, q0026).
- Left alignment repeated across three different screens: station detail, "Support" and "Settings" use the same row, colored icon in a rounded square, label and action on the right, whether chevron, button or toggle (sheet 0007, q0060; sheet 0005, q0041).
- Concentricity shown at the component level: in the slide "Increased Concentricity" the corners of the inner cards follow the curvature of the device's own corners, something the speech only addresses in the abstract (sheet 0007, q0058).
- Search and keyboard anchored at the bottom: the list of location suggestions sits directly above the system keyboard, with no gap between the two, with a microphone icon in the field (sheet 0007, q0062).
- Different density by screen size: on iPad, a fixed sidebar with search, "Today", "Overview", "Charts", "Tables" and a recents section, plus a grid of graph cards on the right; on iPhone, the same cards stacked vertically (sheet 0005, q0045).
- Summary with hierarchy by opacity, active item lighter and the rest in gray, with the third item named "Custom menus" at one point and "Custom Components" at another (sheet 0003, q0021 and q0022; sheet 0005, q0038 and q0039).
- Closing in two pieces: a text-only slide, "Redesign not required.", and a collage that brings together the screens already shown on iPad, iPhones and Apple Watch as a summary of the set (sheet 0008, q0067, q0065 and q0066).
Visual proportion: almost all the sheets bring a slide or app mockup on screen, with frames of the presenter alone interspersed mainly in sheets 0002, 0003, 0005 and 0008, and sheet 0009 in its entirety is just audience, with no interface.
<!-- /visual:meet-with-apple_257 -->

## Liquid Glass showcase: Slack (id: meet-with-apple_255, 12.5 min)

Basis: transcript and 10 of 10 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/meet-with-apple/255/.

**Central thesis.** Jaime DeLanghe (product lead for the Slack experience at Salesforce) and Akshay Bakshi (mobile product director) describe why adopting Liquid Glass was, according to them, a "no-brainer" aligned with Slack's product principles, and how they used the opportunity to also solve a limited search problem, moving it to the tab bar.

**The design process Apple/the presenters describe.**
- Jaime presents four Slack product principles that guide every build decision (detailed below).
- When iOS 26 was announced at WWDC 2025, the mobile team was already following along live in a dedicated channel, gauging "how far and deep" to go with the redesign; they decided on a broad redesign because Slack's mobile design language was already evolving in the same direction ("morphing" animations in creation menus and channel headers).
- For the app header, they prototyped and tested three different versions on the device, in hand, before deciding (detailed in "concrete techniques").
- Rollout phased by risk and frequency of use: at the day 1 launch (October) they prioritized the elements used most daily (create menu, tab bar, conversation headers, composer) and the riskiest "muscle memory reconnection" changes (glass header, search in the tab bar); next they updated navigation and huddle controls; they planned to update the media player chrome and canvas controls in November, and landscape support (landscape) in December. On iPad, they scoped September to just the essentials (using iPadOS 26 windowing and improving the menu bar), postponing custom sidebar controls that, in an earlier version of the redesign, had delayed engineering.

**Principles stated and the why of each.**
- "Take bigger, bolder bets": not limiting themselves to thinking small, but also looking for ways to get there safely.
- "Seek the steepest part of the utility curve": a metaphor attributed to founder Stewart Butterfield, each unit of investment brings increasing return up to a certain point, and that is the ideal point to stop (compared to a carpenter shaving wood with a hand plane until finding the beauty of the piece).
- "Prototype the path": daily builds of the app itself tested in the team's hands, with a willingness to discard what doesn't work; a strong culture of "using what you're building".
- "Be a great host": anticipating the user's needs and putting things where they wouldn't even think to look (a metaphor for towels left on the bed for guests, also attributed to Stewart Butterfield).
- "Don't make me think": since the entire operating system is migrating to Liquid Glass, Slack shouldn't be "extra Slack", the work of teaching the user how to use the software shouldn't be necessary; the less the user needs to think, the better.
- Native controls "future-proof" the app as the platform evolves: for example, the iOS 26 tab bar uses less space, which already improves landscape mode, and new future orientations will be supported automatically.

**Concrete interface-building techniques.**
- Search moved from its previous position (limited, required leaving a thread, going back to home, tapping search, finding the DM/channel/canvas and going back) to the tab bar, available globally on any screen.
- Header prototyped in three versions: a "concentric" version that fit well with the shape of the device but whose bottom edge "didn't work well"; a "capsule" version that shrank next to the front camera and looked good, but when switching between mostly light or dark conversations sometimes looked like a primary button; and a "gradient" version similar to Apple's own apps, which didn't work well with the variability of content in Slack's scroll views. They opted for something closer to the previous header, but highlighting the Liquid Glass containers.
- The new header also needs to accommodate workspace theming (personal versus professional themes), which in Slack isn't just aesthetic, but helps the user quickly tell contexts apart when switching workspaces.
- Slack's brand identity maintained not through the aesthetics of the chrome, but through the voice and tone of the copy, user customization and theming, and the expressiveness of emojis.

**Examples cited (apps, screens, components) and what each example teaches.**
- Slack's "catch up" (ketchup) feature, cited as an example of turning a task nobody wants to do (reading unread messages) into a "delightful" experience, teaches that the product principles apply beyond visual aesthetics.
- Create menu and channel header menus, already with "morphing" animations before iOS 26, teaches that having your own interaction language can lay the groundwork for quickly adopting a new design system.

**Up to two short, literal quotes.**
- "seek the steepest part of the utility curve"
- "Our job is to help people get their job done"

<!-- visual:meet-with-apple_255 -->
### What the images show
Basis: 10 of 10 frame sheets viewed, all codes checked.
- List of principles built one by one on screen: each principle gets a line-drawing stick-figure illustration with its own metaphor (balancing on a ball, using a pole, climbing a ladder, holding a cup, pointing) and the name in small text below, the row growing from one to five items as the speech progresses (sheets 0003 and 0004, q0019 to q0032).
- Launch timeline documented feature by feature: a fixed month marker in the left margin and callouts with a connecting line pointing to the exact element, "Improved Menus" and "Windowing" on iPad in September, "Conversation Headers", "Create Menu" and "Composer" on iPhones the same month, "Glass Header" and "Search in the Tab bar" in October (sheet 0008, q0068, q0070 and q0072).
- The same callout pattern continues in the following months: "Viewer Chrome" and "Canvas Controls" over a media player and a notes screen in November, and December reduced to a single phone with a document screen (sheet 0009, q0074, q0077).
- Before-and-after pair by system version: two phones in the same composition, channel list on the left and conversation on the right, labeled "iOS 18" and then "iOS 26" (sheet 0005, q0040 and q0042).
- Theming proven by repetition, not by assertion: the same fictional workspace screen repeats in five variations with identical structure, changing only the header and accent color, and further on in three color schemes with additional tabs at the top (sheet 0006, q0047 to q0051, q0053 and q0054).
- Anatomy of the workspace home screen: header with name and avatar, horizontal summary cards, huddles section with an indicator for an ongoing call, lists grouped by category with a numeric counter to the right of each item, and a bottom icon navigation bar (sheet 0006).
- Two-button decision component: conversation card with reactions and a counter, an outlined button on one side and a filled green button on the other, plus an intermediate state with a blue background, centered text and an arrow icon that signals the gesture, a mechanical detail that the speech doesn't describe (sheet 0002, q0013 and q0014).
- The turn from problem to solution done in large text, "Search felt limited" next to the home screen with no dedicated search icon in the bar, then "Search available globally" next to a list of conversations, zoomed in until the text bleeds off the screen (sheet 0007, q0059 to q0064).
- The team's own internal messages become slide material: bubbles with a circular avatar, bold name, timestamp, body and reactions, stacked in a cascade, listing targets such as "Tab bar (tabless)", "Create menu" and "Composer" (sheet 0005, q0038 and q0039).
- Identity slide in a horizontal row with five words, "Voice", "Tone", "User Customization", "Theming" and "Expressivity", immediately before the theme screens (sheet 0006).
- Brand color applied to the event itself: a section slide in a purple and magenta gradient with the app icon on the right, and the stage backdrop in the same color family for much of the video, even though sheet 0001 records a dark stage (sheet 0001, q0006 to q0008; sheet 0008).
- Standardized credits and closing: the title slide carries the names and titles of the two presenters, the final slide gathers a row of circular team face photos, and the last frame is the apple icon used as a generic cut between videos in the series (sheet 0001; sheet 0009, q0081; sheet 0010).
Visual proportion: practically all the sheets alternate between a slide or app capture and frames of the presenter alone on stage, and there is also an audience-only frame on sheet 0004 and a final frame with no presenter on sheet 0010.
Recorded divergences or limits: in the "Search available globally" frame, the notes record that the conversation list shows no obvious navigation change, meaning the screen doesn't visually prove the tab bar search in that frame (sheet 0007, q0062); on sheet 0009 the first pair of phones appears with no visible month label; and on sheet 0001 the notes point out a remnant of the previous video on the big screen, with another company's logo still visible in the background.
<!-- /visual:meet-with-apple_255 -->

## Liquid Glass showcase: LTK (id: meet-with-apple_254, 9.6 min)

Basis: transcript and 8 of 8 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/meet-with-apple/254/.

**Central thesis.** Jeseka Hahn, VP of product design at LTK (a social community for creator recommendations), tells how the company rebuilt the app from scratch in SwiftUI with a new internal design system called Runway, around three lessons (start small; work smarter, not harder; build trust), which laid the groundwork for adopting Liquid Glass quickly when it arrived.

**The design process Apple/the presenter describes.**
- Starting point of the rebuild: in 2024, constant changes to social platforms, algorithms and noise multiplied by AI were threatening the visibility of creators who depend on LTK for their livelihood; years of layers on top of an aging framework had left the app heavy, slow and expensive to evolve.
- They decided to rebuild on a four-month timeline, with a real design system (which didn't exist before) built on Apple's native OS for faster iteration and scalability.
- They literally started with a single button, which grew into patterns, screens and a shared language until it became the Runway design system.
- They audited the information architecture, questioning every flow and pattern; they found they were solving the same problem in multiple redundant ways, even in something as simple as the product card; they practiced what they internally call "brutal prioritization" to cut redundancies, with debates described as "lively" and prioritization as "brutal".
- To convince founders and leadership to pause the current work and support the rewrite, a principal engineer built a side-by-side demo showing how long it took to build a page with the design system in SwiftUI versus without it; the demo (without the design system, the process "kept going and going") ended the debate.

**Principles stated and the why of each.**
- "Brutal prioritization": saying no to more options helps focus on what really matters; simplifying gives speed and reduces teams' insecurity about decisions already made.
- Cascading trust: first trust in the system (design system), then trust between teams, and finally trust from the users themselves.
- Brand identity should not compete with creator content, it should complement it, literal quote below.

**Concrete interface-building techniques.**
- Complete rewrite of the app in SwiftUI, with native Apple components as the base of the Runway design system.
- With Liquid Glass, the controls integrated with the content so that the creator's content stood out; before iOS 26, the team spent weeks manually adjusting the layout to achieve this same goal.
- After the solid base in SwiftUI, backlogged features (dark mode, widgets) and new features with each new iOS version could be delivered more easily.
- New dedicated search tab and adoption of "visual intelligence": the user takes a photo and instantly finds related creator content within LTK.

**Examples cited (apps, screens, components) and what each example teaches.**
- The product card, cited as a concrete example of the same problem solved in several redundant ways before the audit, teaches that pattern redundancy accumulates silently in apps that evolve through continuous addition.
- The lead engineer's side-by-side demo (with and without the design system), teaches that quantitative arguments about development speed can convince leadership where design arguments alone would not be enough.

**Exact numbers cited.**
- Revenue from creator recommendations: US$ 6 billion per year (company business context, cited in the opening).
- Timeline for the app's full rebuild: 4 months.
- Build time cut: almost 70%.
- App size reduction: almost by half.
- Time spent in the app since the February relaunch: up 138%.
- Search usage since the iOS 26 launch: doubled overnight ("doubled overnight").

**Up to two short, literal quotes.**
- "Simplifying gave us the speed to move faster."
- "Our identity should not compete with creator content."

<!-- visual:meet-with-apple_254 -->
### What the images show
Basis: 8 of 8 frame sheets viewed, all codes checked.
- Proof of simplicity in two side-by-side editor panels, "with Runway" versus "without Runway", the panel without the design system visibly longer in number of lines, with the "Code complete" label appearing only over the left panel (sheet 0004, q0032 to q0034).
- An isolated, enlarged line of code as an example of an adopted native API, shown alone on screen before the comparison (sheet 0004).
- Concrete tool from the information architecture audit: tree diagram with rectangular nodes colored by category, organized in hierarchical columns, with yellow nodes highlighted at the top and flow labels such as create profile, follow creator and product poll (sheet 0003, q0021 to q0026).
- Metrics in large typography with a short caption below: build time and app size in a before-and-after format linked by a double arrow, and search usage reduced to a single multiplier, with no pair of values (sheet 0007, q0059 to q0061).
- Translucent controls positioned over the photo, small circles with a central icon marking points of interest on the product image, and a translucent side navigation bar anchored to the left without covering the photographic content (sheet 0006, q0046, q0048 and q0049).
- State transition between frames: from the photo with zoom markers to the visual search results screen, with a back-and-close header and a grid of thumbnails with variable proportions, some spanning two columns (sheet 0006, q0046 to q0047).
- Vertical action bar on the right edge of the full-screen content, stacked translucent icons with a numeric counter below each one, a pattern that reappears on several screens of the app (sheets 0001, 0005 and 0006, q0004 and q0041).
- Anatomy of the post screen: header with avatar and name, dominant image, action column to the right of the photo, horizontal carousel of related products in square thumbnails and a caption block in the footer (sheet 0005, q0041).
- Brand identity expressed within system components: circular design system badge with a percentage indicator and a palette of square swatches next to a screen with a three-item tab bar (sheet 0003, q0019).
- Bullets of the three lessons appearing progressively in the opening and returning later with the third item highlighted, marking the point in the talk (sheet 0001, q0007 to q0009; sheet 0005).
- Large text with no interface as a pacing device: three stacked words describing the old app, the rebuild timeline in large text, two stacked gains and a closing sentence about rebuilding the right way (sheets 0002, 0003 and 0004).
- Volume shown through device repetition: six phones side by side on stage at one point, around ten at another, each with a different screen of the app (sheet 0006, q0051; sheet 0007).
- Difference between frames suggesting animation: the same phone appears tilted in perspective and then straight-on, indicating device rotation on screen (sheet 0006, q0052 to q0053).
- Incremental composition of the context slide: between two consecutive frames the set of news clippings grows from three to four cards, with the new image inserted among the existing ones (sheet 0002, q0010 to q0011).
Visual proportion: slides and app screenshots predominate, with the presenter in close-up interspersed, and sheet 0006 is almost entirely made up of full-screen app screens with no visible stage.
Recorded divergences or limits: in the information architecture diagram the notes record illegible text labels at the distance of the first framing (sheet 0003), and in sheet 0005 the text of the notification cards appears partially covered by the presenter.
<!-- /visual:meet-with-apple_254 -->

## Liquid Glass showcase: CNN (id: meet-with-apple_256, 9.4 min)

Basis: transcript and 7 of 7 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/meet-with-apple/256/.

**Central thesis.** Kevin Long, CNN's director of apps, explains how the prior adoption of SwiftUI (motivated three years ago by a CMS switch) left CNN well positioned to adopt Liquid Glass quickly, and shares specific technical integration lessons (modifier nesting, padding and performance).

**The design process Apple/the presenter describes.**
- Three years ago, CNN began a transition to a modern content management system, which required rewriting the client code; the team used this window to modernize the iOS client architecture and adopt SwiftUI.
- CNN works with cross-functional squads per platform (engineers, product managers, designers and QA), each platform with dedicated competencies, sharing learnings between teams but with solutions adapted to each platform, keeping the design principles unified.
- They recompiled the app in Xcode 26 to see how it would look; components such as the tab bar and navigation bar migrated automatically and already "looked great" with no extra work, serving as a baseline for designing the rest.
- A designer from the team took part in a three-day workshop with Apple in July, to understand what already comes ready with Liquid Glass and what needs to be custom built; the team focused first on getting the basics right, especially the top-level navigation.

**Principles stated and the why of each.**
- Avoid nested glass modifiers (applied to both a parent view and a child view): this creates visual redundancy, double translucency, layered blur and unpredictable rendering; the solution was to apply the modifier only at the highest level necessary and create internal guidelines to prevent accidental nesting. Literal quote below.
- Watch out for padding: the glass effect did not always respect the expected padding, sometimes stretching or cutting off content; the solution was to wrap the effect in background or overlay methods and adjust the padding outside the scope of the modifier.
- Watch out for performance: the effect is GPU-intensive, especially in scrollable views or ones updated frequently; the team limited its use in high-frequency areas (such as lists and animations) and reserved the effect for static or top-level components, such as tab bar and toolbars.
- Use a custom view modifier that applies the glass effect conditionally, only on iOS 26, to give control over where the effect is applied (for example, on the video player's button overlays) without affecting the app's broader layout.

**Concrete interface-building techniques.**
- Before the migration, the codebase was a mix of Objective-C, Swift, UIKit and React Native; SwiftUI brought a unified, modern approach to building views, simplified the layout and improved state management.
- Example of article rendering: each element (title, byline, image, paragraph) used to be represented by a separate view, each with its own nib, logic and ViewModel; with SwiftUI, they consolidated everything into a single file per element, significantly reducing the number of files and making code navigation and maintenance easier.
- Iteration speed gain: upon receiving internal feedback about spacing and contrast in the article layout, the team was able to make and preview the changes in minutes using SwiftUI, instead of hours of manual testing and layout adjustment.
- Future plans: migrate the tvOS app to share the iOS codebase, and create a team (squad) dedicated to platform-specific innovation, to speed up the adoption of new features.

**Examples cited (apps, screens, components) and what each example teaches.**
- Article rendering (title, byline, image, paragraph): teaches how consolidating several legacy views into a single file per element reduces maintenance complexity.
- Button overlays in the video player: teaches a selective and conditional use of the glass effect, applied only where necessary, without affecting the broader layout.

**Up to two short, literal quotes.**
- "Avoid nested glass effect modifiers."
- "The glass modifier is well designed."

<!-- visual:meet-with-apple_256 -->
### What the images show
Basis: 7 of 7 frame sheets viewed, all codes checked.
- Right-and-wrong pair for a technical problem: two nearly identical phones labeled "Nested glass" and "No nested glass", each with an image inside a card over the screen, making visible the double translucency that the talk only describes in words (sheet 0004, q0034 and q0035).
- Real code as proof of implementation: a block of Swift in a dark editor with colored syntax, labeled as a custom view modifier, shown in two consecutive frames with a framing shift (sheet 0004, q0032).
- List of learnings built item by item, always with a different example image alongside: first the item about glass on glass, then the one about padding and layout behavior, then the one about performance (sheets 0004 and 0005, q0034 to q0038).
- Callouts marking where the effect was and was not applied on the same screen: three labels connected by a line point to the search field at the top, the player controls and the bottom navigation bar, the latter named as the area without the effect (sheet 0005, q0038).
- Annotation arrow indicating the padding shift caused by the material, over a phone showing the logo inside a translucent glass outline (sheet 0005, q0037).
- Decomposition of a screen into components: an article thumbnail receives callouts with a connecting line for title, byline, image and paragraph, materializing the view consolidation that the talk treats in the abstract (sheet 0002, q0017 and q0018).
- Navigation callouts on two phones side by side, pointing to the top and bottom of the screen, with a dotted vertical ruler between them that changes position between consecutive frames (sheet 0003, q0019 and q0020).
- The same product image supporting three different messages: the composition of two app thumbnails stays fixed while only the slide text changes across three frames, one per motivator cited (sheet 0001, q0006 to q0008).
- Media app layout seen on a real screen: scrollable horizontal sections with a title on the left and program covers with overlaid text, plus a bottom bar with four labeled items (sheet 0003, q0021).
- Full-screen vertical format for short video, with a caption overlaid on the upper part of the image, location and date information, controls and progress bar at the bottom and an audio icon in the corner (sheet 0003, q0023).
- Different convention for TV: horizontal menu at the top with five items, a featured image taking up most of the screen and text with an action button anchored at the bottom (sheet 0006, q0047).
- Two nearly identical variations of the same article screen shown side by side, with the headline and body legible only in the zoomed-in frame (sheet 0004, q0031).
- Presentation system shared by the series: the title slide and the closing frame with the Apple logo follow the same template as the other videos in the group (sheets 0001 and 0007, q0059).
Visual proportion: all the content sheets feature a slide, app screenshot or code, interspersed with frames of the presenter alone, and only sheet 0007 is mostly presenter and closing.
Recorded divergences or limits: in sheet 0001 the notes hesitate about who is on screen, recording "the presenter, feminine (the presenter, masculine)"; in sheet 0002 the fourth icon in the row of papers appears with no clearly visible caption; and in sheet 0006 the notes mark as an assumption that a cut-off text would be part of an acknowledgment.
<!-- /visual:meet-with-apple_256 -->

## What this group reveals about the Apple way

- The Liquid Glass redesign is treated by Apple as a coordinated platform event with in-person follow-up for external teams (multi-day workshops, group labs), not just as a visual update announced and left to developers on their own (ids: meet-with-apple_208, meet-with-apple_256).
- The separation between "functional UI layer" (native controls) and "content layer" (where the brand should live) is the most repeated principle across all the accounts, appearing both in Apple's institutional speech and in the concrete decisions of each partner company: Lowe's removes its blue brand bar on detail screens, American Airlines lets its logo scroll out of the top, Slack keeps the brand in the voice and tone of the copy instead of the chrome's aesthetics, LTK explicitly states that identity should not compete with the creator's content, Tide Guide values the concentricity and spacing that make the UI "step back", and CNN describes its goal as "edge to edge layouts, minimal chrome" (ids: meet-with-apple_208, meet-with-apple_254, meet-with-apple_255, meet-with-apple_256, meet-with-apple_257).
- Adopting SwiftUI and native components before Liquid Glass arrived is cited repeatedly as the factor that allowed fast adoption of the new design: CNN had already been migrating for three years because of a CMS switch, LTK had just rewritten the app from scratch, and American Airlines had already migrated to native components before Liquid Glass arrived (ids: meet-with-apple_256, meet-with-apple_254, meet-with-apple_208).
- Fast "hands on" prototyping, on a real device, appears as a recurring validation method before convincing leadership or closing a design decision: Slack tested three header versions on the device, Sky Guide prototyped in a few days to validate performance, LTK used a side by side demo of development time to convince founders, CNN cut layout adjustment cycles from hours to minutes, and Apple's own design team describes co-location sessions with engineers watching the real build, because the Liquid Glass materials were hard to replicate in design tools (ids: meet-with-apple_208, meet-with-apple_255, meet-with-apple_254, meet-with-apple_256).
- Moving search from its traditional position to the bottom of the screen (tab bar) is a specific structural change, cited independently by multiple teams as a significant UX decision, justified both by ergonomics (thumb reach) and by the whole operating system's convention changing at the same time (ids: meet-with-apple_208, meet-with-apple_255).
- GPU performance of the glass effect is a recurring technical concern among those who actually built with the material: CNN limits its use to static components and avoids high-frequency lists/animations, and Sky Guide specifically feared resource competition with the continuous animation of the sky view, resolving the doubt through fast prototyping (ids: meet-with-apple_256, meet-with-apple_208).

## No transcript

- meet-with-apple_270: now has its own card in this file, with the basis noted on the card.
- meet-with-apple_274: now has its own card in this file, with the basis noted on the card.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_270.md, 4 lines read, read to the end: yes (file with no transcript, header only).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_274.md, 4 lines read, read to the end: yes (file with no transcript, header only).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_208.md, 320 lines read, in two parts (1 to 226, then 227 to 320, due to the size limit of the first read), read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_257.md, 40 lines read, read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_255.md, 45 lines read, read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_254.md, 39 lines read, read to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_256.md, 38 lines read, read to the end: yes.
