# Components / Content

## Charts (slug: charts)

### What it governs
How to organize data in a chart to communicate information with clarity and visual appeal, covering anatomy, mark types, axes, descriptive content, color and accessibility.

### Why
Apple starts from the idea that an effective chart highlights a few key pieces of information from a data set to help people gain insights and make decisions, not to display all the possible data. The central reasoning is attention hierarchy: the data itself must be the most prominent element, while descriptions and axes give context without competing with it. Another throughline is that accessibility is not an extra: like any infographic, a chart needs to be fully accessible regardless of how the person perceives the content, and that is why VoiceOver, Audio Graphs and keyboard/Switch Control navigation get extensive treatment. Finally, there is a concern with the perceptual honesty of the data (for example, choosing the lower bound of the Y axis) so as not to distort the reading of the differences between values.

### Do and avoid
- Choose the mark type (bar, line, point) according to the information you want to communicate.
- Use bar marks to compare categories or see proportions of a whole, especially when each value represents a sum.
- Use line marks to show change over time and reveal trends through the slope of the line.
- Use point marks to show the relationship between two properties and identify outliers and clusters.
- Consider combining mark types when that brings clarity, such as points over a line to highlight individual values.
- Use a fixed range on the axis when specific minimum and maximum limits are meaningful for all possible values (for example, battery charge from 0 to 100%).
- Use a dynamic range when the possible values vary widely and you want the marks to fill the plot area.
- Set the value of the axis lower bound according to the mark type and the chart's use; zero works well in bar charts to allow visual comparison of heights, but can obscure relevant differences in other types, such as heart rate.
- Prefer familiar value sequences in tick and grid-line labels (for example, 0, 5, 10) instead of unusual sequences (1, 6, 11).
- Adjust the density and visual weight of grid lines and labels to the chart's context of use: too many grid lines overload it visually, too few make it hard to estimate values.
- Write descriptions (titles, subtitles) that explain the chart's purpose before the person examines the details, especially for VoiceOver users and people with certain cognitive disabilities.
- Summarize the chart's main message with simple, direct language.
- In compact environments, maximize the width of the plot area; keep vertical axis labels as short as possible without losing clarity, and consider describing units elsewhere (such as in the title).
- Make every chart accessible: provide accessibility labels for the components and consider using Audio Graphs.
- Allow interaction with the data when it makes sense, but never require interaction to reveal critical information.
- Enlarge the hit target when the marks are too small to reach with a finger or pointer, allowing "scrubbing" across the entire plot area.
- Make an interactive chart navigable by keyboard (including full keyboard access) and Switch Control, whether by following the standard linear sequence, by defining a custom logical path via accessibility APIs, or by allowing focus to move between subsets of values in very large datasets.
- Help people notice important changes in the chart, including through animation, but complement it with other signals for VoiceOver users or those who have disabled animations.
- Align the chart with neighboring interface elements, for example by aligning the chart's leading edge with that of other views; consider placing the label of each vertical grid line on the trailing side and shifting the Y axis to the trailing side so it doesn't cross the leading edge.
- Don't rely on color alone to differentiate data or communicate essential information; complement it with different shapes or patterns.
- Add visual separation between contiguous color areas, such as in stacked bar charts with colored segments.
- When writing accessibility labels: prioritize clarity and comprehensiveness, including context (date, location) and not just the raw value.
- Avoid subjective terms like "quickly", "gradually", "almost" in descriptions; use real values.
- Avoid ambiguous formats and abbreviations in data descriptions (prefer "June 6" over "6/6", "60 minutes" over "60m").
- Describe what the chart's details represent, not their appearance (for example, don't describe colors used to differentiate series).
- Be consistent throughout the app when referring to a specific axis (for example, always mention the X axis first).
- Hide visible text labels of axes and ticks from assistive technologies, since VoiceOver users get that information through accessibility labels and Audio Graphs.

### Exact specifications
The text does not give pt, px, ms numbers, proportions or standard sizes specific to charts; the numeric references present are examples of data values (0%, 50%, 100% battery charge; sequence 0, 5, 10; alternative sequence 1, 6, 11), not design specifications.

### Platform differences
- iOS, iPadOS, macOS, tvOS, visionOS: no additional considerations beyond the general ones.
- watchOS: in general, avoid requiring complex interactions with the chart; prioritize information visible at a glance and simple interactions when they add value. If the app also exists on another platform, consider using that version to show more detail (example cited: the Heart Rate app on watchOS shows the current day's chart, while Health on iPhone shows heart rate data across several periods and allows examining individual marks).

### Links to other articles
Charting data, Creating a chart using Swift Charts, Marks, Inclusive color, Enhancing the accessibility of a chart, Vision (for VoiceOver), Accessibility, UIAccessibility.Notification (UIKit), NSAccessibility.Notification (AppKit), Swift Charts.

---

<!-- visual:charts -->
### What the illustrations show
Basis: 3 of 3 illustration sheets opened (img 0234 to 0245), codes checked; no video.
- The cover is already a chart with labeled data: a bell-curve histogram with dark red bars over a reddish-orange gradient, Y axis marked 0, 50 and 100 on the right, times on the X axis, red measurement arrows for the total height and the width of the X axis, and a dashed grid on top (img 0234).
- The anatomy diagram reuses the same histogram, now in blue on white, with callouts naming each part: grid line on a vertical dotted background line, plot area on the inner area of the bars, mark on the tallest central bar, axis on the vertical ruler from 0 to 100 on the right side, tick on a mark on the X axis and axis value label on a time label (img 0235, in sequence with 0234).
- The three mark types appear in distinct data: blue bars of steps per day over a month, Y axis from 0 to 15,000 and an isolated peak above 10,000 near day 26 (img 0236); blue line with a gradient area below, price from 2018 to 2022 with Y axis from 71 to 182 and an upward trend (img 0237); line with a small circle at each data point, from April to September, Y axis from 50 to 80 and a peak in July (img 0238).
- Fixed axis on battery level: rounded card with Y axis always from 0% to 100%, green bars near the top, intermediate bars in light gray decreasing, two smaller green bars at the end and lightning bolt and pause icons over the top strip of some bars (img 0239).
- Dynamic axis on the steps chart: the same card with a period selector D, W, M, 6M and Y and a summary of average and dates in text above; in W, orange bars per day of the week and Y axis ending at 6,000; in M, narrower bars per day and Y axis ending at 10,000 (img 0240 and 0241).
- In the descriptive content, a dark card shows first the title of the heavy rain alert and a subtitle in plain language, and only then the chart of many very thin light blue bars, with the X axis in minutes from now to 50 minutes (img 0242).
- Color never works alone in blood pressure: systolic in red dots on top and diastolic in black and white diamonds on the bottom, in the same plot area with Y axis from 50 to 150, and the header repeats the shape marker next to each range of values (img 0243).
- The storage bar is a single horizontal bar divided into nine segments of distinct colors, from red to light gray, each separated from its neighbor by a thin white gap, with a colored dot legend and text below (img 0244).
- In accessibility, a black elevation line chart, with total ascent and descent in the header, X axis in miles and Y axis in feet, receives a black outline rectangle covering only about the final fifth of the route, the section with the steepest climb, plus a small circular dot at the start of the route; the notes read the rectangle as a focus indicator, probably from VoiceOver (img 0245).
<!-- /visual:charts -->

## Image views (slug: image-views)

### What it governs
How to use an image view, which displays a single image (or, in some cases, an animated sequence of images) over a transparent or opaque background, including when to use it instead of symbols, icons or image buttons.

### Why
The central intent is to use each component for its specific purpose: an image view is for displaying an image, not for receiving interaction, and Apple prefers that interactivity be left to components already built for that, such as a system button configured to display an image. Likewise, for icons the guidance is to prefer SF Symbols or interface icons over image views, because symbols and icons are vector-based, colorable and can adopt the accent colors chosen by the person, which an ordinary bitmap image doesn't readily offer. There is also a concern about legibility when text is overlaid on images, and about performance/consistency when the image view displays animated sequences.

### Do and avoid
- Use an image view when the view's main purpose is simply to display an image.
- In rare cases where the image needs to be interactive, configure a system-provided button to display it, instead of adding button behavior to the image view.
- To display an icon, prefer a symbol (SF Symbols) or interface icon over an image view.
- Take care when overlaying text on images: this can reduce both the clarity of the image and the legibility of the text; ensure contrast between text and image and consider features such as text shadow or a background layer.
- In animated sequences, use a consistent size for all images; pre-scaling the images to fit the view avoids the need for the system to scale them, and when the system does need to scale them, performance tends to be better if all the images have the same size and format.

### Exact specifications
There are no specific numbers, measurements, durations or proportions in the text.

### Platform differences
- iOS, iPadOS: no additional considerations.
- macOS: for an editable image view, use an image well (supports copying, pasting, dragging and using Delete to clear the content); to make an image clickable, use an image button instead of an image view.
- tvOS: many images on tvOS combine multiple layers with transparency to create a sense of depth (see Layered images).
- visionOS: app and game windows in visionOS can use image views to display 2D images, stereoscopic images and spatial photos; apps that use RealityKit can also display images of any type outside image views, alongside 3D content, or generate a spatial scene from an existing 2D image.
- watchOS: use SwiftUI to create animations when possible; alternatively, WatchKit can animate a sequence of images inside an image element, if necessary (API cited: WKImageAnimatable).

### Links to other articles
Images, Image wells, Image buttons, SF Symbols, Layered images, visionOS.

---

<!-- visual:image-views -->
### What the illustrations show
Basis: 1 of 1 illustration sheet open, with a single image (img 0628) and the other three quadrants of the grid empty, code checked; no video.
- The frame is a rectangle with well rounded corners with a gradient from orange on the left to reddish pink on the right, with the classic image glyph at the center: a translucent white rounded frame with a circle and a silhouette of mountains (img 0628).
- Measurement arrows turn the cover into a sizing diagram: a horizontal double arrow above marks the width and a vertical double arrow on the right marks the height of the glyph inside the frame (img 0628).
- The combination of the placeholder with width and height dimensions treats the image view as a container with its own dimensions, which can differ from those of the image it carries (img 0628).
Recorded divergences: the official caption speaks only of a stylized photo tinted red and does not mention the measurement arrows that the image shows (img 0628).
<!-- /visual:image-views -->

## Text views (slug: text-views)

### What it governs
How to use a text view, which displays multiline, styled text content, optionally editable, in contrast to labels and text fields.

### Why
The logic behind the component choice is the amount and nature of the text: text views exist for long, editable or specially formatted text, offering more display and text entry options than labels or text fields. For little text, Apple prefers the simplicity of a label (or of a text field, if editable). Behind the legibility recommendations is the principle that freedom of styling (multiple fonts, colors, alignments) cannot compromise the readability of the content, hence the recommendation to adopt Dynamic Type and test with accessibility options turned on. The recommendation to make useful text selectable reflects the idea that information such as error messages or serial numbers has practical value when it can be copied.

### Do and avoid
- Use a text view for long, editable or specially formatted text; for little text, use a label or, if editable, a text field.
- Keep the text legible even when using multiple fonts, colors and alignments.
- Adopt Dynamic Type so the text continues to look good when the person changes the text size on the device.
- Test the content with accessibility options turned on, such as bold text.
- Make useful text selectable, such as an error message, serial number or IP address, to allow copying and pasting elsewhere.

### Exact specifications
There are no specific numbers, measurements or durations in the text.

### Platform differences
- macOS, visionOS, watchOS: no additional considerations.
- iOS, iPadOS: display the appropriate keyboard type; there are several keyboard types available, each designed to make a different type of input easier, and the keyboard displayed when editing a text view needs to be suited to the type of content.
- tvOS: it is possible to display text using a text view; since text entry on tvOS is minimal by design, tvOS uses text fields for editable text instead of text views.
- General behavior note: in iOS, iPadOS and visionOS, if a text view is editable, a keyboard appears when the person selects the view. By default, the content is aligned to the leading edge and uses the system label color.

### Links to other articles
Labels, Text fields, Combo boxes, Accessibility, Typography, Virtual keyboards.

---

<!-- visual:text-views -->
### What the illustrations show
Basis: 1 of 1 illustration sheet open (img 1143), code checked; no video.
- Over an orange and red gradient, a light pink rectangle contains a paragraph of text with several lines, representing the multiline text area (img 1143).
- Ruler arrows dimension the block: a horizontal one at the top for the width and a vertical one on the right for the height (img 1143).
- The construction is the same as the text-fields opening cited in the notes, and what changes is the example content, a whole paragraph instead of a single word, which visually separates text view from text field before any reading (img 1143).
<!-- /visual:text-views -->

## Web views (slug: web-views)

### What it governs
How to use a web view, which loads and displays rich web content, such as embedded HTML and websites, directly inside the app.

### Why
The guiding principle is scope of use: a web view serves to show occasional web content without taking the person out of the app's context (the example given is Mail displaying HTML content from messages), but it should not become a substitute for a browser. The stated reason is that Safari is the primary way people browse the web, so replicating a browser's functionality inside another app is considered unnecessary and discouraged. The recommendation to support forward and back navigation reflects the expectation that, if the person is likely to visit multiple pages within the web view, they need the same basic navigation controls they would have in a browser.

### Do and avoid
- Support forward and back navigation when appropriate; this behavior exists in the web view but does not come turned on by default, so you need to provide the corresponding controls if people are going to visit multiple pages.
- Avoid using a web view to build a browser. Using a web view to allow brief access to a website without leaving the app's context is appropriate, but trying to replicate Safari's functionality is unnecessary and discouraged.

### Exact specifications
There are no specific numbers, measurements or durations in the text.

### Platform differences
- iOS, iPadOS, macOS, visionOS: no additional considerations.
- tvOS and watchOS: web views are not supported.

### Links to other articles
Webkit.org (external link cited as related).

---

<!-- visual:web-views -->
### What the illustrations show
Basis: 1 of 1 illustration sheet open (img 1285), code checked; no video.
- Over a gradient from orange to pinkish red, a very light pink horizontal rectangle sits centered and frames a compass icon in simple outline, a circle with a triangular pointer pointing inward (img 1285).
- Double-headed arrows dimension the rectangle, a horizontal one above for the width and a vertical one on the right for the height, as in the sizing of a window or viewport of web content (img 1285).
- The themed icon stops being just a symbol and becomes a sizing diagram; per the notes, the watch-faces cover does not use this device, and the wallet one only uses it in the internal technical diagrams, not in the opening (img 1285).
Recorded divergences: the official caption describes only a stylized compass icon tinted red, without mentioning the rectangle that frames it or the width and height arrows that the image shows.
<!-- /visual:web-views -->

## What this group reveals about the Apple way

1. The right component for the right purpose, without overloading a component with a function that already exists in another: an image view should not become a button (use a system button instead), an icon should not be an image view (use SF Symbols), short text should not be a text view (use a label or text field), and a web view should not become a browser (use Safari). Supported by: image-views, text-views, web-views.
2. Explicit refusal to replicate system app functionality inside third-party apps, even when technically possible: the guidance not to build a browser inside a web view is the most direct example of this. Supported by: web-views.
3. Accessibility treated as a structural requirement, not finishing: the charts article dedicates a whole section and detailed rules on accessibility label, Audio Graphs, VoiceOver and keyboard/Switch Control navigation, treating this as part of the definition of a "well made chart", not as an addendum. Supported by: charts.
4. Systematic preference for real data and content over subjective or decorative representations: in charts, the guidance to avoid subjective terms ("quickly", "almost") and to use real values in the descriptions, and to not describe appearance (color) but rather what the data represents. Supported by: charts.
5. Visual hierarchy as a recurring principle: in charts, the data should be the most prominent element and descriptions/axes should not compete with them; in image-views, the same logic appears in the warning that text over an image can harm both the image and the text if there is no care with contrast. Supported by: charts, image-views.
6. Adaptation of complexity by platform, reducing interaction in small screen or limited input contexts: watchOS should avoid complex interactions in charts and prefer at-a-glance information; tvOS uses a text field instead of a text view because text entry there is minimal by design; web views do not even exist on tvOS and watchOS. Supported by: charts, text-views, web-views.
7. Consistency across platforms as a value: the four articles explicitly organize a "Platform considerations" section that states, platform by platform, where the default behavior changes and where it does not ("no additional considerations for..."), making clear that the base rule applies unless stated otherwise. Supported by: charts, image-views, text-views, web-views.
8. Symbols and vector icons (SF Symbols) are treated as the preferred way for small, colorable graphic elements, aligned to the accent colors chosen by the person, instead of static bitmaps. Supported by: image-views.
9. Active precaution against making the person depend only on the visual perception of color: both in charts (not relying only on color to differentiate data, using complementary shapes or patterns) and in the general logic of VoiceOver and Audio Graphs, Apple builds redundancy of information channels. Supported by: charts.
10. Strong editorial weight on "not requiring interaction for critical information": charts makes it explicit that interaction can enrich the experience but can never be the only way to reveal essential information, which echoes the concern for accessibility and for robustness across different forms of use (keyboard, Switch Control, VoiceOver). Supported by: charts.

## Reading evidence
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/charts.md, 99 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/image-views.md, 53 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/text-views.md, 37 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/web-views.md, 25 lines read, to the end: yes.
