## Design with SwiftUI (id: meet-with-apple_270, 25.2 min)

Basis: transcript (frames not viewed yet). Local automatic transcript made with Whisper, it is not Apple's official one; proper names and terms may carry hearing errors. Source: https://developer.apple.com/videos/play/meet-with-apple/270/.

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
