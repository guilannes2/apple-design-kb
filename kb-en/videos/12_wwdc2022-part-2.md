# wwdc2022 (part 2)

## Design for Arabic · صمّم بالعربي (id: wwdc2022_110441, 19.5 min)

Basis: transcript and 14 of 14 frame sheets viewed, codes checked. Source: https://developer.apple.com/videos/play/wwdc2022/110441/.

Presenter: Mohamed Samir, designer on the Apple Design team.

### Central thesis

Designing well for the Arabic audience requires treating Arabic not as a simple text translation, but as a complete structural change: interface direction (right to left), typography specific to the Arabic script, localized iconography and numeral systems, with much of this already resolved automatically by Apple's native frameworks (such as SwiftUI) when the app uses the system APIs.

### The design process Apple describes

In the talk, the presenter describes the design reasoning in steps:

1. Justify the investment: about 660 million people use the Arabic script today, making it the third most used writing system in the world after Latin and Chinese, with speakers in more than 22 countries.
2. Understand the reading direction: Arabic is written from right to left, and this directionality affects not only the text but the entire layout (titles, paragraphs, columns, images) from top to bottom and from right to left.
3. Think in wireframes: the best way to reason about layout directionality, according to the presenter, is to turn the screens into wireframes and decide which elements swap sides (from left to right) and which keep their position.
4. Map the user's mental flow: when the direction is reversed, navigation between pages also reverses, as if the user were leafing through an Arabic book from right to left.
5. Review component by component where directionality does or doesn't have an impact: content (images, videos, backgrounds) should normally not be mirrored, but interaction, animation, scales, pagination, calendars and charts with a time component generally should follow the right-to-left direction.
6. Check cultural relevance, not just linguistic: the example of the Islamic lunar calendar in the Calendar app is cited as something beyond translation, tied to the audience's culture.
7. Check iconography symbol by symbol: ask whether the symbol represents a physically motivated direction (like the angle of right-hand use on the magnifying glass, kept as is) or a direction tied to text reading (like the lines of the Today icon, reversed).
8. Check the correct numeral system by target country: since there are two Arabic numeral systems in use today, the presenter recommends checking which one predominates in the country the app is targeting, or supporting both.

### Principles stated and the why of each

- Do not reverse photographic or video content when mirroring the UI: the example given is the sun rising in the east in the Weather app, which must remain correct regardless of locale or language; reversing the image would break the physical reality represented.
- Always align paragraphs to the right in Arabic, because it is the natural reading direction of the script.
- Keep the clock hands in the normal physical direction even in Arabic UI, to match the physical representation of a real clock, while the calendar's progress dots change direction because they represent the advance of time read as text.
- Use tracking (letter spacing) equal to zero in Arabic typography when the font is not fully optimized, because the connected nature of Arabic letters can break ligatures (Kashida) or create improper spacing if handled as if it were Latin.
- Prefer the system font (SF Arabic) whenever possible, because it already automatically resolves letter ligatures, optical scale and transparency issues in words.
- Increase the size of the Arabic font relative to Latin when uppercase is used in the Latin text, because Arabic has no uppercase/lowercase distinction and visually looks smaller next to uppercase Latin.
- Plan for extra vertical spacing when there is heavy use of vocalization marks (diacritics), because these marks make Arabic text slightly taller and can be clipped if the vertical space is insufficient.
- Check transparency in Arabic text carefully: opacity applied to individual characters can reveal visible joints between letters; the system font applies opacity to the whole word or phrase to avoid this distortion.
- Prioritize culturally and linguistically relevant symbols, not just automatically mirrored ones, because some icons (like the magnifying glass) carry universal meaning tied to physical use (right hand), while others (like the text lines of the Today icon) carry meaning tied to reading direction and must be adapted.

### Concrete interface-building techniques

Layout and direction:
- Titles, buttons and the navigation bar must swap order and position in Arabic.
- Paragraphs always aligned to the right.
- Carousels and swipeable elements flow from right to left, including the interaction and the animation (example: the "the weather across the day" carousel in the Weather app).
- Temperature scale in the Weather app: in Arabic, the lowest temperature is on the right and the highest on the left; the scale's gradient and the indicator are reversed to reflect this.
- Pagination dots flow from right to left, because the primary page is further to the right and navigation advances to the left.
- In the Calendar app, the progression of dates, months and years runs from right to left, matching how physical calendars work in the Arabic world; red lines under certain dates mark the start of each month of the Islamic lunar calendar.
- In Settings, toggles and segmented controls have mirrored design and interaction in the Arabic layout.
- In charts with a time component, like the battery usage chart, the days of the week progress from right to left in Arabic (the earliest time is on the right, the latest on the left), mirroring the calendar's behavior; other charts depend on the country and must be checked individually before deciding the direction.

Typography:
- SF Arabic is Apple's exclusive font for Arabic, designed to have stylistic consistency with the Latin SF family in bilingual contexts, and it offers all weights, from Ultralight to Black.
- Examples of weight usage cited: the Clock app uses Bold in the title, Regular in the cities and Light in the clock numerals; the Health app uses bold, medium and regular in titles and body text; the Weather app uses multiple weights in numerals and body text.
- SF Arabic has optical size: the letterform changes according to the point size used. Large sizes (titles, headings) have a contemporary grotesque style aligned with the rest of the SF family; small sizes (paragraphs, body text) prioritize legibility and functionality, adding angularity to the terminals and adjusting the width and contrast of the font's structure. The system automatically chooses the correct form according to the point size.
- Example cited: in the App Store Editorial sheet, the "display" style is used in the title and "text" in the paragraphs, with Arabic and English working cohesively side by side.
- This year (2022) Apple introduced SF Arabic Rounded, with all weights from Ultralight to Black; example cited: the Reminders app uses SF Arabic Rounded in titles and body text, giving a more "practical, active or soft" look depending on the context.
- Size adjustment: when using uppercase in Latin, it is recommended to increase the size of the Arabic font by 10% to compensate for the difference in optical volume between the two scripts.
- Tracking (letter spacing): use 0 tracking when the Arabic font is not fully optimized for spacing, or use the system font, which adds the correct ligature between letters (called "Kashida", with variable lengths for more organic spacing).
- Transparency: the system font applies opacity to the whole word or phrase, and not to each isolated letter, to avoid visible joints between connected characters.

Iconography:
- More than 300 Arabic and right-to-left symbols are available in the SF Symbols library, including an Arabic signature symbol designed exclusively and other text formatting ones.
- In the SF Symbols app it is possible to check the localization section in each symbol's info panel to see the local variant in Arabic and in other non-Latin scripts.
- Examples of symbol-by-symbol decisions: the Today tab icon (lines aligned to the right, following the reading direction) was changed; the magnifying glass was kept the same because its direction reflects the angle of right-hand use, the behavior of most users in the world, regardless of locale; the writing icon keeps the pen's angularity but mirrors the direction of writing; the speaker icon changes direction but keeps the direction of the slash, consistent across the whole Apple ecosystem; the calendar's progress dots change direction, but the clock hands remain as they are, to match the physical representation of a real clock.
- All right-to-left and local symbols appear automatically in the app if the system APIs are used.

Numerals:
- There are two Arabic numeral systems in use today: Western Arabic (used in Arab countries of western North Africa, such as Morocco, Algeria and Tunisia) and Eastern Arabic (used in some countries of the Levant and the Gulf). Egypt and Saudi Arabia use both versions.
- The choice between the two systems happens automatically based on the user's country, and can also be set manually by the user.
- Examples of apps that reflect this choice: Calculator, Calendar and the Typograph watch face, cited as designed in both numeral forms.
- Recommendation: if the app includes numerals, plan for support of both forms, or check the target country to decide which form is more suitable.

### Examples cited

- App Store: the flow from the story card on the Today tab to an app's product page, used to explain how to turn screens into wireframes when adapting layout direction.
- Weather app: teaches that image content (the sun rising in the east) should not be mirrored, and that carousel, temperature scale and pagination follow the direction of the language.
- Calendar app: teaches the pattern of right-to-left date progression and the cultural relevance of marking the Islamic lunar calendar with red lines.
- Settings (battery): teaches that toggles and segmented controls must be mirrored in interaction and design.
- Battery usage chart: teaches how charts with a time component follow the calendar direction in Arabic.
- Pages app: teaches that the navigation bar and the icons follow the full right-to-left direction.
- Clock, Health and Weather apps: teach the use of different SF Arabic weights in typographic hierarchy.
- App Store Editorial sheet: teaches the combined use of the display and text optical sizes in a bilingual context.
- Reminders app: teaches the use of SF Arabic Rounded to give a more practical and soft tone.
- SF Symbols app: teaches where to check localized icon variants.
- App Store tab bar: teaches the logic of when to mirror an icon (Today) and when not to (magnifying glass).
- Calculator, Calendar and the Typograph watch face: teach the coexistence of the two Arabic numeral systems.

### Quotes

"Regardless the location or the language" (about keeping the sun rising in the east in the Weather app, without inverting the content).

"As if they are navigating through an Arabic book from right to left" (about the mental model of navigation in Arabic).

<!-- visual:wwdc2022_110441 -->
### What the images show
Basis: 14 of 14 frame sheets viewed, all codes checked.
- Article on iPad as the first demonstration of the inverted layout: the title appears first alone on a light background slide (sheet 0002, q0012) and then inside the app's full layout, with a large title and paragraphs aligned to the right, a supporting image to the left of the text block and the top toolbar mirrored, with the navigation controls on the right side (q0013 to q0016). Over this screen a display options dropdown menu opens aligned to the right, with list items and a toggle turned on in green (q0014).
- Wireframe shown in three stages in the same sequence: the three iPhone screens with real content, then the same screens reduced to gray blocks with no content, then the already mirrored wireframe with the Arabic content put back in, with the bottom bar and the cards switching sides (sheet 0003, q0022 to q0025). The notes record that, in this section, the speech describes titles, buttons and navigation bar switching position in Arabic.
- A pair of screens side by side in two identical iPhone frames, English on the left and Arabic on the right, is the session's central technique, with an Arabic label next to each pair naming the subject under test (image, temperature scale, order of the days, Islamic calendar, chart over time) (sheet 0004, q0028 to q0036). In the weather app pair the city name and the texts switch sides while the sun illustration and the weather icon stay in exactly the same physical corner in both versions (sheet 0003, q0026 and q0027); in sheet 0004 the same principle appears as an identical blue sky on both sides, labeled image (q0028).
- Anatomy of the temperature scale card in the comparison pair: gradient bar with a number at each end, "18°" on the left and "32°" on the right in the English version, and the same bar with the order switched in the Arabic version (sheet 0004, q0030).
- Components with a time axis compared in the same format: annual calendar in a 12-month grid in 4 rows of 3, with the order of the months mirrored in the Arabic version; a warning box overlaid on the calendar appears only in the following frame, with the text "1444 AH, First Day of Islamic Month" in the English version and some day numbers in red in the Arabic one; and the battery usage bar chart with the bars and the hour labels inverted between the two versions (sheet 0004, q0032 to q0036).
- Typography slides on an absolute black background with a single element in white and a small caption below, a pattern that repeats across several sheets: the example word gains a callout line and the connected script caption in a frame the previous one did not have; the letter appears in the four positional forms labeled isolated, initial, medial and final; and a dense grid of small glyphs fills the whole screen (sheet 0005, q0039 to q0043).
- Volume comparison between the two scripts made with two solid color rectangles, one per word, each underlined by a thin line, with the little space caption entering only in the second frame (sheet 0005, q0044 and q0045). Next the same Arabic word receives the vocalization marks and becomes visibly taller than the previous version, in the same framing (sheet 0006, q0046 and q0047).
- Weight table in double column: the Latin family name repeated from thinnest to thickest on the left and the Arabic family in the same weights on the right, with weight labels at the ends; the isolated pair of font names in the previous frame expands into this full table (sheet 0006, q0052 and q0053). The same table format reappears for the rounded variant, with softer letter endings (sheet 0008, q0068), followed by the real screen that uses it (q0069 and q0070).
- Optical size demonstrated as two columns labeled "Display" and "Text" with the same word at different scales, each block with a circular marker above and a side label in Arabic, and then the text variant enlarged alone to expose the angularity of the endings (sheet 0007, q0058 to q0061).
- Measurement annotated inside the slide: the letter spacing value appears as a percentage below the example sentence, stays the same for the first three frames and grows from the fourth on, while the connections between the letters stretch and break and the letters separate artificially (sheet 0009, q0076 to q0080). In the following frame the sentence loses opacity and the word for the next topic enters as a watermark on top, announcing the subject before the speech does, which continues with the slide at 50 percent transparency (q0081; sheet 0010, q0082).
- Size adjustment between scripts shown with arrows: a downward arrow next to the Latin sentence in lowercase and an upward one next to the same sentence in uppercase, with the Arabic sentence next to it on both lines (sheet 0010, q0084 and q0085). Right after comes the real editorial card from the store in both versions, and the following frame zooms in on the footer showing the active tab highlighted in blue on the side opposite to the English version (q0086 and q0087).
- Icon by icon comparison in two-line slides labeled English and Arabic, going through a different symbol per frame: some invert orientation, like the document with lines of text, and the search icon appears with the handle pointing to exactly the same side in both lines, with no inversion (sheet 0011, q0094 to q0099). Before them, a close crop of the App Store's tab bar shows the same icons mirrored in the Arabic version (q0093). The same two-line format returns in a single slide that compares signature, numbered list, letter, numeral and a text formatting icon; the notes point out completely different shapes between the two scripts in the signature, the letter and the numeral, and the same structure in the formatting icon (sheet 0012, q0100).
- Tools and documentation shown on the screen itself: the symbols app open on a MacBook with a category sidebar on the left, a central icon grid and a detail panel on the right with the location information for the selected symbol (sheet 0012, q0103); and the right-to-left layout guidance page from the Apple guidelines site in full screen on a MacBook, with a side menu, a large title and iPhone mockups (sheet 0013, q0117; sheet 0014, q0118).
- Numerals treated first as form and then as a product decision: dark rounded key-shaped blocks, with the whole "123" that splits into three blocks and then becomes a numeric keypad grid (sheet 0012, q0106 to q0108); then the two systems side by side with a label for each, and the places where the choice appears, the settings list with a blue selection mark, the annual calendar with the same month grid changing only the days' numeral system, and two Apple Watch faces, one orange and one green, with the hands overlaid on the large numbers (sheet 0013, q0109 to q0114).
- List of topics in Arabic on the presenter's right side that accumulates item by item and highlights the current one through opacity and size, reappearing before each topic change and signaling the section before the speech announces it (sheet 0003, q0019 to q0021; sheet 0010, q0090; sheet 0012, q0105).
- Closing by mosaic: a dense grid of thumbnails of native app screens in Arabic already appears at the end of the typography block (sheet 0008, q0072) and the final recap gathers thumbnails of almost every example in the session in an irregular grid, from watches to wireframes, spacing slides, icons and app screens (sheet 0014, q0119 to q0122); the final card is covered by a dark band that advances from right to left over the text "WWDC22" (q0125 and q0126).
Visual proportion: only sheet 0001 is dominated by the presenter; in the rest he appears in short connecting segments (for example q0037, q0048 to q0050, q0064 to q0067, q0083, q0115 and q0116) and most of the frames are typography slides on a black background or interface captures in a device frame, with sheets 0004 and 0011 entirely without the presenter. The frames vary according to the type of content: iPad in the long article, iPhone in most of the apps, Apple Watch in the watch faces and MacBook in the tools and the documentation.
Recorded divergences or limits: in sheet 0010 the notes note that, in the uppercase slide, the Arabic text appears at the same visual size in both lines, and that the difference in treatment is indicated by the arrows and the caption, not by the size actually shown. The notes also record frames with no visible change between them, q0059 and q0060 in sheet 0007, q0084 and q0085 in sheet 0010 and q0091 and q0092 in sheet 0011, which limits what can be stated about the animation in these sections, and describe the change of the keyboard icon with a clock (sheet 0011) in vague terms, without detailing what changes. In sheet 0002 the notes themselves diverge about the display options menu: the screen description places it in q0014 and q0015, and the change between frames line says it disappears from q0014 to q0015.
<!-- /visual:wwdc2022_110441 -->

## What this group reveals about the Apple way

- Localization, for Apple, is not text translation: it is a structural redesign of the layout, the navigation direction, the typography, the icons and the numeral systems, with case by case decisions about what to mirror and what not to mirror (id: wwdc2022_110441).
- Apple distinguishes direction motivated by the physics of the real world (sun, clock hands, hand angle) from direction motivated by reading text, and uses that criterion to decide what to invert in right-to-left (id: wwdc2022_110441).
- The company invests in its own typography optimized by script (SF Arabic, SF Arabic Rounded, automatic optical scaling) to take away from the developer the manual responsibility for getting letter connection, spacing and transparency right (id: wwdc2022_110441).
- Most of the adaptation work for right-to-left is resolved automatically by the native frameworks (SwiftUI and system APIs), which Apple uses as an argument to encourage the use of these frameworks instead of custom solutions (id: wwdc2022_110441).

## No transcript

No file in this group was left without a transcript.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2022_110441.md, 24 lines read, to the end: yes.
