# Components / Status

## Activity rings (slug: activity-rings)

### What it governs
Governs the use of the Activity ring element, which shows a person's daily progress toward their Move, Exercise and Stand goals.

### Why
The element exists to represent a very specific concept from the Apple ecosystem (the three physical activity metrics) consistently across apps, so that people instantly recognize what they are seeing, on watchOS and on iOS, just as they see it in the Activity app. Apple protects the visual integrity of the symbol (fixed colors, black background, margins) because it functions as a standardized visual language: any change in color, opacity or context breaks that recognition and can confuse the reading of the person's actual progress. The prohibition on decorative use or use as branding comes from the same principle: Activity rings communicate data, not the app's visual identity.

### Do and avoid
- Display Activity rings when they are relevant to the app's purpose, especially in health or fitness apps, particularly those that contribute data to HealthKit.
- Consider showing the element on a workout metrics screen, to track progress during the session, or on a summary screen at the end of the workout.
- Use Activity rings only to show Move, Exercise and Stand information. Never use them for another type of data.
- Never show Move, Exercise and Stand progress in another ring-like element.
- Use Activity rings to show a single person's progress. Never represent data from more than one person in the same element, and make clear whose progress it is (label, photo or avatar).
- Never change the colors of the rings, including through filter or opacity.
- Always display Activity rings on a black background.
- Prefer enclosing the rings and the background inside a circle by adjusting the view's corner radius, instead of applying a circular mask.
- Make sure the black background remains visible around the outermost ring; if necessary, add a thin, black stroke on the outer edge, and avoid gradient, shadow or any other visual effect.
- Scale the rings appropriately, so they don't look disconnected or misplaced.
- When necessary, design the interface around them to match the rings, never the other way around.
- For labels or values associated with a specific ring, use the colors that correspond to it.
- Keep the element's minimum outer margin equal to or greater than the distance between the rings; never let other elements cut, obstruct or invade that margin or the rings themselves.
- Differentiate other ring-shaped elements from Activity rings, using padding, lines, labels, color or scale to visually separate them.
- Don't send notifications that repeat information the Activity app already sends, and don't show the Activity ring element inside your app's notifications; it's acceptable to reference progress in your own way, without replicating what the system already shows.
- Don't use Activity rings as decoration, in labels or in background graphics.
- Don't use Activity rings for branding, app icon or marketing material.

### Exact specifications
RGB colors specified for the labels and values of each ring, according to the image description:
- Move: R 250, G 17, B 79
- Exercise: R 166, G 255, B 0
- Stand: R 0, G 255, B 246

### Platform differences
- watchOS: the element always contains three rings, with the same colors and meanings as the Activity app.
- iOS: contains a single Move ring (an activity approximation based on steps and workouts from other apps) when there is no paired Apple Watch, or the three rings when there is a paired Apple Watch. Available via HKActivityRingView. Since behavior changes based on pairing, an app's activity history can mix the two styles over time.
- iPadOS and watchOS: no additional considerations beyond what's stated.
- Not supported on macOS, tvOS or visionOS.

### Links to other articles
Workouts (related). Developer documentation: HKActivityRingView (HealthKit).

---

<!-- visual:activity-rings -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened, all codes checked; the page has no video.
- The opening is an annotated diagram: three concentric, partially filled rings, with arrows indicating the direction of progress in each one and labels connected by guide lines, Move with percentage and calories on the left, Stand with hours on the right and Exercise with minutes below (img 0029).
- The order of the colors never changes between the images: red or pink on the outer ring, green on the middle one and cyan on the inner one, both in the diagram and in the watch and iPhone screenshots (img 0029, img 0030, img 0034).
- On the Apple Watch workout screen, on a black background, the green running icon appears at the top, the time and a large yellow stopwatch, with the list of Move, Exercise and Stand values on the left and the three rings on the right reflecting those partial values (img 0030).
- The colors of the rings are specified as isolated swatches, each one a rounded square of solid color with the RGB value beside it: reddish pink 250, 17, 79; lime green 166, 255, 0; cyan 0, 255, 246 (img 0031, img 0032, img 0033).
- In the actual screenshots the rings always appear on a black background, and on iPhone they sit inside an "Activity Rings" card with the values listed beside them, not overlaid on the rings (img 0030, img 0034, img 0035).
- The difference between having or not having a paired Apple Watch is isolated by a pair of Summary screens from the Fitness app with the same header, the same date and the same memoji avatar in the corner, changing only the card (img 0034, img 0035).
- With the watch paired, the card shows the three complete rings and the three metrics with the goal reached (img 0034); without it, it shows a single, partially filled pink ring, and the Exercise and Stand metrics give way to steps and distance (img 0035).
- The percentage written beside each ring only appears in the conceptual diagram; in the app screens the values come as pairs of current value and goal, with a unit on iPhone (img 0029 compared with img 0030 and img 0034).
<!-- /visual:activity-rings -->

## Gauges (slug: gauges)

### What it governs
Governs the gauge, a component that displays a specific numeric value within a range of values, along a circular or linear path.

### Why
The gauge serves both to show a value's current position and to give context about the entire range (extremes, color gradient), so that the person understands not just "how much" but "where this is" within a range. The recommendation for succinct labels exists because VoiceOver reads the visible labels so that someone who can't see the screen also understands the gauge, that is, accessibility depends directly on the component's textual quality.

### Do and avoid
- Write succinct labels that describe the current value and the two extremes of the range; even though not every gauge style shows all the labels, VoiceOver reads whichever ones are visible.
- Consider filling the path with a gradient to help communicate the gauge's purpose (example given: a temperature gauge can range from red to blue, from hot to cold).

### Exact specifications
The text doesn't give dimension, spacing, duration or proportion numbers for the gauge itself.

### Platform differences
- iOS, iPadOS, visionOS, watchOS: no additional considerations.
- Not supported on tvOS.
- macOS: besides gauges, it also defines the level indicator, with visual styles sometimes similar to those of gauges, configurable for capacity, rating or (rarely) relevance.
  - Capacity style, continuous: a translucent horizontal bar that fills with a solid bar indicating the current value, according to the image description.
  - Capacity style, discrete: a horizontal row of equal, separated rectangular segments; the number of segments corresponds to the total capacity, and each segment fills completely, never partially, to indicate the value.
  - Consider the continuous style for large ranges, since a large range can make the discrete style's segments too small to be useful.
  - Consider changing the fill color to signal significant parts of the range (very low, very high, or just past the middle). The default fill color in both capacity styles is green. It's possible to change the color of the entire indicator or use the tiered state to show a sequence of several colors in a single indicator (example described in the image: one eighth red, three eighths yellow, one quarter green and the rest unfilled).
  - For guidance on the rating style (used to rank something), see the Rating indicators article.
  - The relevance style, although rarely used, communicates relevance through a shaded horizontal bar, for example in a list of search results, when ordering or comparing multiple items.

### Links to other articles
Ratings and reviews (related). Rating indicators (cited for the rating style of macOS's level indicator). Developer documentation: Gauge (SwiftUI), NSLevelIndicator (AppKit). Also refers to the macOS article for general guidance on level indicators.

---

<!-- visual:gauges -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has no video.
- The opening works as an anatomy diagram of the two formats, stacked in a card with an orange-to-red gradient, without the dashed grid used in other openings: a numeric circular gauge on top and a linear percentage one below (img 0523).
- The circular gauge has an incomplete arc in dark red around the large number "67", a small dot marking the tip of the filled section and the labels "0" and "100" below the number indicating the extremes, with measurement arrows above and below dimensioning the height (img 0523).
- The linear gauge has its left half filled in dark red and the right half in a lighter tone, with "0%" and "100%" at the ends and measurement arrows indicating the width and the side margins (img 0523).
- macOS's continuous capacity indicator is a single bar with rounded corners, with a light gray track and solid green fill covering about two thirds, with no internal divisions (img 0524).
- The discrete one uses the same bar divided into 8 rectangular segments separated by small gaps, with 6 filled in green and 2 in light gray, adding up to three quarters (img 0525).
- In the tiered state, the continuous bar receives several colors in sequence from left to right: a narrow red stretch, a much wider yellow one, a green one and the rest unfilled in gray (img 0526).
- The three macOS variations isolate one decision at a time: continuous versus discrete swaps the smooth bar for separate segments (img 0524 compared with img 0525, with observed fills of about two thirds and three quarters), and single color versus color by range changes the color coding of the same continuous bar (img 0524 compared with img 0526).
<!-- /visual:gauges -->

## Progress indicators (slug: progress-indicators)

### What it governs
Governs progress indicators, transitory elements that signal the app has not frozen while it loads content or runs long-running operations.

### Why
The central function of the progress indicator is to manage the person's expectation and trust during a wait: it exists so that no one mistakes a process in progress for a frozen app. That is why Apple distinguishes determinate from indeterminate depending on whether the task's duration is known or not, and prefers the determinate style whenever possible, because it gives the person a real basis for deciding whether to wait, do something else, restart the task later or give up on it. The requirement to keep the indicator always moving and to have a uniform pace of advance (not jumping from 90% in 5 seconds to the last 10% in 5 minutes) comes from the same principle: an indicator that is stalled or has an inconsistent pace reads as a failure, even when the process is still active, and can even seem misleading. Allowing cancellation or pausing, and warning when canceling has a negative consequence, is an extension of the same logic of giving the person control and honest information during the wait.

### Do and avoid
- Use a determinate indicator whenever possible; the indeterminate one shows that something is happening, but does not help estimate how much time is left.
- Be as precise as possible when reporting progress in a determinate indicator. Consider leveling the pace of advance to convey confidence about the time needed; showing 90% in 5 seconds and the last 10% in 5 minutes can make it seem like the app froze, or even seem misleading.
- Keep progress indicators always moving, so people know something is still happening; a stalled indicator is usually associated with a stuck process or a frozen app. If a process really does freeze, give feedback that helps the person understand the problem and what to do.
- When possible, switch a progress bar from indeterminate to determinate as soon as the duration can be calculated; people generally prefer the determinate indicator, because it helps them understand what is happening and how long it will take.
- Do not switch between the circular style and the bar style: activity indicators (spinners) and progress bars have different shapes and sizes, and the transition between them can disrupt the interface and confuse people.
- If it is useful, show a description with additional context about the task. Be precise and concise; avoid vague terms like "loading" or "authenticating", which rarely add value.
- Show the progress indicator in a consistent location, so the person can reliably find the operation's status across platforms, within the app or between apps.
- When feasible, allow interrupting the processing: if the person can interrupt without a negative side effect, include a Cancel button; if interrupting can cause a negative effect (such as losing the part of a file already downloaded), it can be useful to offer a Pause button in addition to Cancel.
- Warn when interrupting a process has a negative consequence: when canceling results in loss of progress, it is useful to show an alert with the option to confirm the cancellation or resume the process.

### Exact specifications
The text does not give numbers for duration, size or spacing for the indicators. There are no exact numeric values beyond the qualitative pace example (90% in 5 seconds, last 10% in 5 minutes), which is an illustrative example of bad practice, not a specification.

### Platform differences
- tvOS and visionOS: no additional considerations.
- iOS, iPadOS: beyond the standard, there is the refresh control, a specialized type of activity indicator hidden by default, which appears when the person pulls down the view they want to reload (example given: the Inbox message list in Mail). Recommendations: perform automatic content updates periodically, without relying only on the person's manual action; include a short title in the refresh control only if it adds value, and in that case use it to convey something relevant about the content (for example, when the last update happened), never to explain how to use the control. Developer documentation: UIRefreshControl.
- macOS: the indeterminate style can look like a bar or a circle, both with an animated image. Prefer the activity indicator (spinner) to communicate the status of a background operation or when space is limited, since it is small and discreet, useful for asynchronous tasks (such as fetching messages from a server) or for communicating progress in a small area, such as inside a text field or next to a specific control. Avoid labeling a spinning indicator, since it usually appears when the person themselves starts the process, which generally makes the label unnecessary.
- watchOS: by default the system displays the indicators in white over the scene's background color; it is possible to change the indicator's color by adjusting its tint color.

### Links to other articles
Developer documentation: ProgressView (SwiftUI), UIProgressView (UIKit), UIActivityIndicatorView (UIKit), UIRefreshControl (UIKit), NSProgressIndicator (AppKit).

---

<!-- visual:progress-indicators -->
### What the illustrations show
Basis: 3 of 3 illustration sheets opened, all codes checked; the page has no video.
- The opening brings both types together in a single composition with red measurement guides: a short-ray spinner centered at the top and, below it, a dark bar filled to about 60%, with arrows marking width and height (img 0906).
- On macOS, the determinate bar sits inside a rounded light gray rectangle, with solid blue fill up to just before the halfway point and the rest in light gray (img 0907).
- The determinate circular indicator is a thin ring filled in blue clockwise from the top, almost complete, with a remaining light gray segment near the 8 o'clock position (img 0908).
- The macOS indeterminate circular indicator is a small icon of short rays around an empty center, in gray on a white background (img 0909).
- The macOS indeterminate bar appears fully filled, but with a gradient from stronger blue in the center to almost transparent at the ends, which suggests a wave of shine traveling along the bar rather than a fill advancing (img 0912).
- On watchOS, the bar and the ring sit inside a rounded black rectangle that imitates the watch face, with solid white fill and the rest in dark gray, instead of macOS's blue: the bar at about 65% and the ring a little past the halfway point, clockwise from the top (img 0913, img 0914).
- The spinner associated with watchOS uses dots arranged in a circle inside a rounded black square, with opacity varying from white at the top to dark gray at the bottom (img 0910).
- The refresh control appears in a real Mail screen on iPhone: the gray spinner is centered just below the status bar, accompanied by the text "Updated Just Now", and the mailbox list remains visible below it (img 0911).
- In both determinate circular indicators, the fill starts at the top and advances clockwise, blue over light gray in one and white over dark gray inside watchOS's black frame in the other (img 0908, img 0914).
Recorded divergences: img 0910 has no visible caption in context, and its connection to watchOS was inferred from its position in the caption list.
<!-- /visual:progress-indicators -->

## Rating indicators (slug: rating-indicators)

### What it governs
Governs the rating indicator, a series of graphic symbols arranged horizontally (by default, stars) that communicate a ranking level.

### Why
The component exists to communicate a rating quickly and visually, and that is why Apple keeps strict legibility rules: symbols always the same distance apart, without expanding or shrinking to fit the component's width, and rounding to complete symbols instead of partial ones. This ensures the rating is read consistently and unambiguously, regardless of the space available. The recommendation to keep the star, or to make the purpose of a substitute symbol clear, follows the same reasoning: the star is already a widely recognized ranking symbol, and any substitution without clarity risks not being understood as a rating scale.

### Do and avoid
- Make it easy to change the ranking: when presenting a list of ranked items, allow adjusting the rank of individual items right there, without navigating to a separate editing screen.
- If you replace the star with a custom symbol, make sure its purpose is clear, since other symbols may not be associated with a rating scale the same way the star is.
- The component never displays partial symbols; it rounds the value to show only complete symbols.
- Within the rating indicator, the symbols are always the same distance apart, and do not expand or shrink to fit the component's width.

### Exact specifications
The text does not give numbers for size, spacing or duration for the rating indicator.

### Platform differences
- macOS: no additional considerations.
- Not supported on iOS, iPadOS, tvOS, visionOS or watchOS.

### Links to other articles
Ratings and reviews (related). Developer documentation: NSLevelIndicator.Style.rating (AppKit). Also cited from the Gauges article, as a reference for the rating style of the level indicator on macOS.

---

<!-- visual:rating-indicators -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has only the opening illustration and no video.
- The component is drawn as a horizontal row of five stars, with a rating of three out of five expressed through whole stars, three filled and two empty, with no fractional star (img 0918).
- Filled star and empty star are distinguished only by the shade of the same color: solid dark red in the filled ones and lighter, translucent red in the empty ones, with no separate outline (img 0918).
- The measurement arrows mark two different dimensions: the total width of the row and the height of an individual star (img 0918).
- It is a conceptual piece over an orange-to-red gradient, in the same specification-diagram style as the other opening illustrations, and confirms the official description of a three-out-of-five-star ranking (img 0918).
<!-- /visual:rating-indicators -->

## What this group reveals about the Apple way

1. Components that carry system data (Move, Exercise, Stand in Activity rings) are treated as protected vocabulary: color, shape and context stay locked to preserve instant recognition across apps, unlike generic components such as gauges or rating indicators, which the app can adapt (activity-rings vs. gauges, rating-indicators).
2. The choice between determinate and indeterminate style, or between a simple gauge and a level indicator with a gradient, is always subordinate to giving the person the maximum honest information about "where am I" and "how much is left", never just aesthetics (progress-indicators, gauges).
3. Consistency of form is treated as a usability rule, not a matter of taste: not switching between spinner and progress bar, not letting the rating indicator's symbols change their spacing, is always meant to avoid confusing the reading of a state (progress-indicators, rating-indicators).
4. Accessibility appears built into the component itself, not as a separate layer: VoiceOver reads the gauge's labels, which forces the text to be concise and correct from the design stage (gauges).
5. There is a clear hierarchy between system feedback and app feedback: the app can reference data such as Activity progress in its own way, but must never replicate or duplicate what the system (watchOS/Activity app) already communicates, so as not to create confusing redundancy (activity-rings).
6. Apple carefully distinguishes "real data" from "decoration": Activity rings and rating indicators carry an explicit ban on decorative or branding use, because they communicate real information, not visual identity (activity-rings, rating-indicators).
7. macOS receives separate treatment in this group, with its own component (level indicator) that overlaps the functions of gauge, rating and relevance, showing that Apple concentrates on a single platform style variations that other platforms do not even support (gauges, rating-indicators, progress-indicators).
8. Giving the person control during a wait (canceling, pausing, warning about loss of progress) is treated as part of the progress component's own design, not as an optional extra feature (progress-indicators).
9. All four components in this group point to "Ratings and reviews" or to each other (gauges cites rating-indicators, rating-indicators cites gauges), showing that Apple thinks of these status components as an interrelated family, not isolated units (gauges, rating-indicators).

## Reading evidence
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/activity-rings.md: 55 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/gauges.md: 45 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/progress-indicators.md: 67 lines read, to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/rating-indicators.md: 25 lines read, to the end: yes
