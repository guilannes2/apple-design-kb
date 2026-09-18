# Components / Selection and input

Basis: Apple's Human Interface Guidelines, texts at /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/. Index group 10 of the "hig" list in groups.json, kb 54.

## Color wells (slug: color-wells)

What it governs: the color well, the control that opens a color picker to adjust the color of text, shapes, guides and other elements on the screen.

Why: Apple recommends the system color picker because it ensures consistency across apps and lets people save a set of colors that's accessible in any app, as well as helping maintain a familiar experience across iOS, iPadOS and macOS.

Do and avoid:
- Consider the system color picker for a familiar experience instead of building a custom one.
- In macOS, clicking a color well gives it a visual highlight confirming it's active, then opens the color picker.
- In macOS, the color well supports drag and drop: colors can be dragged between color wells and from the color picker to a color well.

Exact specifications: no number, measurement or duration is given in the text.

Platform differences: no additional considerations for iOS, iPadOS and visionOS. Not supported on tvOS or watchOS. The highlight behavior, picker opening and drag and drop described are specific to macOS.

Links to other articles: Color (related). Documentation: UIColorWell and UIColorPickerViewController (UIKit), NSColorWell (AppKit), Color Programming Topics.

<!-- visual:color-wells -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked, with the same image in light and dark version; the page has no video.
- The color well is drawn as a square button with rounded corners with a circular chevron pointing down, with a horizontal measurement arrow above and a vertical one on the right marking width and height (img 0253, light).
- A text callout with the RGB value points by a line to the center of the button, treating the current color as specification data for the control (img 0253, light).
- Below the button a popover opens with ten swatches in two rows of five squares, in increasing shades of red and pink, arranged in a regular grid (img 0253, light).
- The popover connects to the button by a continuous drop-shaped form, which visually links the closed control to the open panel and suggests a single origin, rather than two separate elements (img 0253, light).
- The rulers and callout are documentation annotations, not real interface elements, which makes the image a geometry diagram of the component rather than a system capture (img 0253).
- In dark mode, structure, rulers and text position stay identical; the background darkens, the popover container becomes wine brown, the button's white box turns into a light semitransparent outline and the swatches keep the same shades (img 0253, light and dark).
<!-- /visual:color-wells -->

## Combo boxes (slug: combo-boxes)

What it governs: the combo box, which combines a text field with a pull-down button in a single control, allowing a custom value to be typed or one to be chosen from a list of predefined values.

Why: the control exists to balance two needs, the convenience of choosing among the most likely options and the freedom to enter a custom value when no predefined option fits. When the person types a custom value, it is not added to the list of options.

Do and avoid:
- Fill the field with a meaningful default value taken from the list; the field can be empty by default, but it's better when the default value hints at the hidden options; the default value doesn't need to be the first item in the list.
- Use an introductory label to indicate what kinds of items to expect, usually in title-style capitalization and ending in a colon.
- Offer relevant options: people value both being able to type a custom value and the convenience of choosing from the list of the most likely options.
- Make sure the list items aren't wider than the text field, so they aren't truncated and hard to read.

Exact specifications: no number is given in the text.

Platform differences: not supported on iOS, iPadOS, tvOS, visionOS or watchOS. It's a control exclusive to macOS (NSComboBox, AppKit).

Links to other articles: Text fields, Pull-down buttons.

<!-- visual:combo-boxes -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked; only the light version is recorded and the page has no video.
- The combo box joins the editable text field and, to its right, the down-arrow button in a single control, which sits inside a small rounded red rectangle (img 0343).
- The horizontal ruler above covers the width of the entire control, including the arrow button, and the vertical ruler on the right marks the height, treating field and button as one dimensional unit (img 0343).
- The field shows "Cupertino" with the text cursor right after the word, and the open list below brings four other cities, which makes visible that the typed value doesn't need to be among the predefined options (img 0343).
- The dropdown list uses the same typographic hierarchy for the four items, in red text over a lighter gradient background, with no item marked as selected; the current value stays only in the field (img 0343).
Recorded divergences: the official description speaks generically of a combo box displaying a list of cities, and the image adds the detail of free entry, through the cursor after a name that isn't on the list.
<!-- /visual:combo-boxes -->

## Digit entry views (slug: digit-entry-views)

What it governs: the digit entry view, a screen that takes up the entire screen and asks the person to type a series of digits, such as a PIN, using a keyboard specific to digits.

Why: since it's typically used for sensitive data (such as a PIN), Apple recommends hiding the typed value and making the purpose of the screen clear, so the person understands why the entry is being requested.

Do and avoid:
- Use secure digit fields, which display asterisks instead of the typed digit; always use a secure field when the app asks for sensitive data.
- Clearly state the purpose of the digit entry view, with a title and a prompt that explain why someone needs to type digits.
- It's possible to add an optional title and a prompt above the row of digits.

Exact specifications: no number is given in the text.

Platform differences: not supported on iOS, iPadOS, macOS, visionOS or watchOS. Exclusive to tvOS (the article's image describes a five-digit PIN screen for Apple TV, according to the image description), with the TVDigitEntryViewController API (TVUIKit).

Links to other articles: Virtual keyboards.

<!-- visual:digit-entry-views -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked; the page has no video.
- The image is a specification diagram, not a screen capture: large title "Enter Passcode" and a one-line prompt centered above five rectangular boxes lined up horizontally, which represent the digit fields (img 0460).
- The vertical order of the screen is title, prompt, row of digits and, below, a row of numbers from 1 to 0 with a delete button, with the "1" highlighted in a white square as the item in focus (img 0460).
- The callouts mark the breathing room around each block: a double vertical arrow above the title to the top edge, horizontal arrows on each side of the row of boxes to the side margins, small vertical marks between the boxes for the spacing between them, and vertical arrows between the boxes and the keyboard and between the keyboard and the bottom edge (img 0460).
- The diagram communicates proportion and spacing through callouts, without presenting numeric values in the recorded reading, and uses large, centered typography (img 0460).
Recorded divergences: the official description identifies the image as a five-digit passcode screen for Apple TV, but the image doesn't show any element that identifies the device or tvOS; compatibility with a screen viewed at a distance is an inference from the notes, not something visible.
<!-- /visual:digit-entry-views -->

## Image wells (slug: image-wells)

What it governs: the image well, an editable version of an image view, where the person can copy and paste the image, delete it, or drag a new image in without needing to select it first.

Why: the control serves to make image manipulation direct and consistent with the system's editing patterns (copy, paste, drag), so that people use the same gestures and shortcuts they already expect from other editing contexts.

Do and avoid:
- Revert to a default image when necessary: if the image well requires an image, go back to showing the default image if the person clears the content.
- If the image well supports copy and paste, make sure the standard copy and paste menu items are available, since people expect to use those menu items or the standard keyboard shortcuts.

Exact specifications: no number is given in the text.

Platform differences: not supported on iOS, iPadOS, tvOS, visionOS or watchOS. Exclusive to macOS (NSImageView, AppKit).

Links to other articles: Image views, Edit menu.

<!-- visual:image-wells -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked, with a single image in the grid; the page has no video.
- The image well is drawn as a rectangle with well-rounded corners in a gradient, with the image glyph contained in a smaller square with a light rounded border, centered (img 0629).
- There's plenty of empty space between the inner square and the larger rectangle, and this inner frame functions as the well where an image would be dropped (img 0629).
- Unlike the image views illustration, which shows the glyph taking up almost all the space with sizing arrows, the image well doesn't bring measurement arrows and presents the glyph smaller and with slack, which suggests a drop area distinct from a display-only area (img 0629, compared to img 0628 from the image views page).
Recorded divergences: the image agrees with the official description of a stylized image well, but adds the visible rounded-border frame around the glyph, absent from the textual description.
<!-- /visual:image-wells -->

## Pickers (slug: pickers)

What it governs: the picker, which displays one or more scrollable lists of distinct values to choose from. Several styles are provided by the system, each with different selectable values and appearance; the exact values shown and their order depend on the device's language (and, for date pickers, the device's region).

Why: the picker exists to make entering single values or multi-part values easier without requiring free typing. Apple advises choosing the component by the size of the list: a picker works well for medium to long lists, since scrolling quickly through many items works well, but it adds too much visual weight to a short list (for that, pull-down buttons are better) and is not ideal for very large sets (for that, lists and tables adjust in height and can have an index, which speeds up locating a section).

Do and avoid:
- Consider a picker for medium to long lists; for short lists, consider a pull-down button; for very large sets, consider lists and tables.
- Use predictable, logically ordered values, such as an alphabetized list of countries, so people can move quickly through the items even with values hidden before interaction.
- Avoid switching screens to show a picker; it works well displayed in context, below or near the field being edited, typically at the bottom of a window or in a popover.
- Consider offering less granularity when specifying minutes in a date picker, increasing the minute interval as long as it divides 60 evenly (for example, fifteen-minute intervals).

Exact specifications:
- By default, a list of minutes includes 60 values (0 to 59).
- Example of an alternative interval: 0, 15, 30 and 45 minutes.
- The countdown timer mode (iOS, iPadOS) displays hours and minutes up to a maximum of 23 hours and 59 minutes, and this mode is not available in the inline or compact styles.

Platform differences:
- No additional considerations for visionOS.
- iOS, iPadOS: date picker with four styles (compact, inline, wheels, automatic) and four modes (date, time, date and time, countdown timer). Compact is recommended when space is restricted: it shows a button in the app's accent color that, when tapped, opens a modal with a familiar calendar editor and time picker, allowing multiple edits before confirming by tapping outside.
- macOS: two date picker styles, textual (for limited space and specific date and time selections) and graphical (for navigating days on a calendar, selecting a date range, or when a clock-like dial is appropriate). See NSDatePicker.
- tvOS: pickers available via SwiftUI (Picker).
- watchOS: pickers display lists navigated with the Digital Crown, in the wheels style, including date and time pickers in that style; it is possible to configure outline, caption and a scroll indicator; for longer lists, a navigation link displays the picker as a button, and the person can also move through the options by turning the Digital Crown without touching the button.

Links to other articles: Pull-down buttons, Lists and tables.

Article change log: June 5, 2023, update to the guidance for using pickers on watchOS.

<!-- visual:pickers -->
### What the illustrations show
Basis: 3 of 3 illustration sheets viewed, all codes checked; the page has no video.
- The opening stylizes an Apple Watch with three stacked bands as a scrollable list: the center one is larger, has a highlighted white outline and the text "Item", marking the selection, and the top and bottom bands appear reduced and partially covered, like out-of-focus items; an arrow appears to the right of the center band (img 0841).
- In the iOS compact layout, the "Date" row shows the value in blue on the right inside a light gray card, and tapping it opens a popover below over the content with a full monthly calendar, month navigation arrows, a weekday header and a day grid, with the chosen day in a blue circle and another day in blue, read in the notes as the current date (img 0842).
- In the inline layout, the card carries the title and an active green toggle on the same row, and the same calendar is embedded within the card itself, with no popover (img 0843).
- In the wheels variation, the "Time" card shows the value in blue on the title row and, below, three vertical wheels for hour, minutes and AM or PM, with the center value in larger black text and the adjacent ones in light gray, suggesting reel-like scroll depth (img 0844).
- On watchOS, the black screen has a blue title at the top and a back button; below, a green label names the field and a three-position wheel highlights the center value with a green outline, with the neighbors cropped and dimmed, and a green confirmation button sits at the bottom (img 0845).
- For date, three wheels side by side each with an outline, the center one highlighted in green, and the bottom button reads "Next", indicating a step-by-step selection (img 0846); for time, three wheels separated by colons, with the center one in green and a confirmation button at the bottom (img 0847).
- For longer lists on watchOS, the closed picker is a dark gray rectangular button with two lines of text, one larger in white and another smaller in gray below, representing the selected option (img 0848); when tapped, it opens a vertical list with rows separated by thin dividers and a green check to the right of the selected item (img 0849).
- On the watchOS screens, green is reserved for focus and selection: wheel outline, field label, action button and check (img 0845, img 0846, img 0847, img 0849); blue appears in the top title (img 0845, img 0849).
- On iOS, blue marks the value on the card row (img 0842, img 0844) and the chosen day in the compact calendar (img 0842), and the same component changes its presentation form between popover, inline and wheels (img 0842, img 0843, img 0844).
<!-- /visual:pickers -->

## Segmented controls (slug: segmented-controls)

What it governs: the segmented control, a linear set of two or more segments, each functioning as a button; in general all segments have equal width. It offers a single choice among a set of options or, on macOS, a single or multiple choice.

Why: the value of the segmented control lies in grouping related functions so that the grouping is preserved regardless of the view's size or where the control appears, which helps people understand at a glance which controls are currently selected. It can also work without a selection state, as a set of buttons that perform actions (for example, Reply, Reply all and Forward in macOS Mail).

Do and avoid:
- Use a segmented control to offer closely related choices that affect an object, state or view.
- Consider a segmented control when it is important to group functions or clearly show its selection state.
- Keep the control types consistent within a single segmented control: do not mix segments that represent actions with segments that represent selection state.
- Limit the number of segments: too many segments are hard to interpret and slow to navigate.
- Keep the segment size consistent; when all have equal width, the control looks balanced; also try to keep icon and title widths consistent.
- Prefer using text or images, not a mix of the two, within the same segmented control, since mixing can create a confusing, disconnected interface.
- Use content of similar size in each segment, since segments usually have equal width.
- Use nouns or noun phrases for segment labels, with title-style capitalization; a segmented control with text labels does not need introductory text.

Exact specifications: aim for no more than about five to seven segments in a wide interface, and no more than about five segments on iPhone.

Platform differences:
- Not supported on watchOS.
- iOS, iPadOS: consider a segmented control to switch between closely related subviews (example: the Calendar new event sheet switches between creating an event and a reminder); to switch between fully separate sections of the app, use tab bars.
- macOS: consider introductory text to clarify the control's purpose; if using symbols or icons, you can add a label below each segment and a tooltip per segment; use a tab view in the main area of the window, instead of a segmented control, for view switching; consider supporting spring loading (on a Mac with a Magic Trackpad, it lets you activate a segment by dragging selected items over it and force clicking, without releasing the items, and continuing to drag afterward).
- tvOS: consider a split view instead of a segmented control on screens that filter content; avoid placing other focusable elements near segmented controls, because segments become selected when focus reaches them, not when they are clicked, which can cause accidental focus on nearby elements.
- visionOS: when the person looks at a segmented control that uses icons, the system shows a tooltip with the descriptive text provided.

Links to other articles: Split views, Buttons, Tab bars, Boxes, Tab views.

Article change log: June 21, 2023, updated to include guidance for visionOS.

<!-- visual:segmented-controls -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened, all codes checked; the page has no video.
- The opening illustration works as a proportion diagram: three segments labeled "Label", the first one selected on a light background, horizontal arrows above marking the total width, a vertical mark on the right indicating the height and a small arrow under the first segment suggesting the tap point (img 0995).
- Single choice and multiple choice appear in pairs with the same control design, changing only the number of filled segments: in the alignment icons, only one segment is solid blue with a white glyph (img 0996); in the B, I, U and S styles, three are blue at the same time and the fourth stays white (img 0997).
- In these two controls, the inactive segments sit on a white background, with a gray glyph in the alignment one, and the selection is indicated by fill, not by border or underline (img 0996, img 0997).
- In the alignment control, a thin vertical dividing line separates the third segment from the fourth, which suggests a slightly different grouping for the last icon within the same control (img 0996).
- On the iOS screens, the selection has a different treatment: the active segment appears in raised white, on a gray background in the Health app's period selector (img 0998), and also in raised white in the Calendar's Event and Reminder pair (img 0999).
- In the Health app, the control with five short-label segments (D, W, M, 6M, Y) sits right below the header and governs the period of the Move and Exercise charts that come below (img 0998).
- In the Calendar's New Event sheet on iPhone, the two-segment control sits right below the header with the close and confirm buttons, and the fields below (all-day, Starts, Ends, Travel Time) are the ones specific to the selected Event mode (img 0999).
- In the Mac Calendar, text callouts separate the two similar-looking components: the segmented control sits in the sidebar filtering invitations, with "New" selected in red, while the tab view with Day, Week, Month and Year sits in the top right corner of the main window, with Month selected (img 1000).
- All the examples use a single type of content per control: only icons (img 0996), only style letters (img 0997) or only text labels (img 0998, img 0999, img 1000), and the real examples always show the control within a full app screen, not in isolation.
<!-- /visual:segmented-controls -->

## Sliders (slug: sliders)

What it governs: the slider, a horizontal track with a control called the thumb that the person adjusts between a minimum and maximum value; as the value changes, the portion of the track between the minimum and the thumb fills with color. It can optionally display icons on the left and right that illustrate the meaning of the minimum and maximum values.

Why: directional consistency exists because people develop a fixed expectation of where the minimum and maximum extremes are, and breaking that expectation disrupts intuitive use. Live feedback and tick marks exist to help locate specific values with more precision, especially when the range of values is wide or non-linear.

Do and avoid:
- Customize the slider's appearance (track color, thumb image and color, side icons) if it adds value and communicates intent.
- Use familiar directions: minimum value on the leading side and maximum on the trailing side in horizontal sliders; minimum at the bottom and maximum at the top in vertical sliders.
- Consider complementing a slider with a corresponding text field and stepper, especially when the slider represents a wide range of values; the stepper offers a convenient way to increment in whole values.
- On macOS, consider giving live feedback as the value changes.
- On macOS, choose the slider style that matches people's expectations: horizontal is ideal for moving between a fixed starting and ending point; circular is suited for values that repeat or continue indefinitely.
- On macOS, consider using a label to introduce a slider, in sentence-style capitalization ending in a colon.
- On macOS, use tick marks to increase clarity and precision, and consider labeling them for even more clarity; it is not necessary to label every mark, unless it is needed to reduce confusion; in many cases, labeling only the minimum and maximum values is enough; when the slider's values are non-linear, periodic labels give context; it is also good practice to show a tooltip with the thumb's value when the person holds the pointer over it.

Exact specifications:
- Range example: horizontal opacity slider between 0 and 100 percent.
- Circular slider example: rotating an object between 0 and 360 degrees.
- Circular slider example for animation: four complete rotations equal four turns, or 1440 degrees of rotation.

Platform differences:
- Not supported on tvOS.
- iOS, iPadOS: do not use a slider to adjust audio volume; for volume control, use a volume view, which is customizable and includes a volume-level slider and a control to switch the active audio output device.
- macOS: sliders can include tick marks; in a linear slider, the thumb has the shape of a narrow diamond; in a circular slider, the thumb appears as a small circle, and the tick marks, when present, appear as equally spaced dots around the circumference.
- visionOS: prefer horizontal sliders, since it is generally easier to gesture from side to side than from top to bottom.
- watchOS: the slider is a horizontal track displayed as a set of discrete steps or as a continuous bar, representing a finite range of values; the person taps buttons on the sides of the slider to increase or decrease the value by a predefined amount; the system displays plus and minus signs by default, but it is possible to create custom glyphs if needed.

Links to other articles: Steppers, Pickers, Text fields, Playing audio.

Article change log: June 21, 2023, updated to include guidance for visionOS.

<!-- visual:sliders -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened, all codes checked; the page has no video.
- The opening illustration names the slider's three reference positions with thin vertical marks labeled "Min", "Mid" and "Max" above the track, aligned to the start, the middle and the end, with the pill-shaped thumb at the exact center (img 1080).
- In the opening, the ends of the track carry a brightness icon and a double arrow pointing outward, which indicate the direction of decreasing and increasing, and the track to the left of the thumb is darker than the one to the right, suggesting the filled part; it is a conceptual piece, not an app capture (img 1080).
- Slider, text field and stepper form a group in a single line: label "Opacity", blue slider with a circular white thumb, rectangular field with the value in percentage, and the stacked-arrow stepper attached to the right of the field; the thumb gives the approximate position and the field gives the exact number (img 1081).
- On macOS, the linear slider without marks is just the track filled in blue from the left to the white thumb, inside a light gray card (img 1082).
- The version with tick marks keeps the same card and adds short gray vertical strokes, equally spaced, about nine of them, covering the entire track and not only the filled part (img 1083).
- The macOS circular slider is a small light ring with a dark gray dot at the 12 o'clock position, without numbering and, in this instance, without tick marks (img 1084).
- In the Energy Saver panel, the tick marks sit under the track and only a few points on the scale get a label ("1 min", "15 min", "1hr", "3 hrs", "Never"), not every mark; the thumb appears right after "15 min" (img 1085).
- On watchOS, the slider is a compact black capsule with a low-volume icon on the left and a high-volume icon on the right, and the fill is green (img 1086, img 1087).
- The difference between discrete and continuous on watchOS lies only in the texture of the central bar, shown side by side on the same sheet: short blocks separated by gaps, with a little less than half filled, against a smooth bar filled to about half (img 1086, img 1087).
<!-- /visual:sliders -->

## Steppers (slug: steppers)

What it governs: the stepper, a two-segment control used to increase or decrease an incremental value; it sits next to a field that displays its current value, because the stepper itself does not display a value.

Why: since the stepper does not show any value on its own, Apple emphasizes making clear which value is being changed; the combination with a text field exists to serve both small changes (well served by taps or clicks on the stepper) and large or highly variable changes (better served by direct typing).

Do and avoid:
- Make it obvious which value the stepper affects.
- Consider pairing a stepper with a text field when large value changes are likely; steppers work well alone for small changes with few taps or clicks, but people appreciate being able to type specific values when the values vary widely (example given: a print screen with a stepper and text field to set the number of copies).
- On macOS, for large ranges of values, consider supporting Shift-click to change the value quickly, by a multiple larger than the default increment.

Exact specifications: example given of Shift-click changing the value by 10 times the default increment.

Platform differences: no additional considerations for iOS, iPadOS or visionOS. Not supported on watchOS or tvOS. Shift-click with a larger multiple is specific to macOS.

Links to other articles: Pickers, Text fields.

<!-- visual:steppers -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened, all codes checked; the page has only the opening illustration and no video.
- The stepper is drawn as a vertical pill divided in half by a thin horizontal line, with an up arrow in the top half and a down arrow in the bottom half, leaving each segment with a single function (img 1107).
- The illustration carries construction measurements: a horizontal bracket at the top indicating the control's width and a vertical bracket on the right indicating the total height (img 1107).
- The behavior is annotated in pseudocode, with "i++" linked by a line to the top half and "i--" linked to the bottom half, mapping each segment to the increment and the decrement; it is the only point in the material that expresses the control's logic as code notation (img 1107).
- The control appears isolated, with no field or number next to it, in an orange-to-red gradient, as a conceptual piece and not an app capture; the image does not show the pairing with a text field (img 1107).
<!-- /visual:steppers -->

## Text fields (slug: text-fields)

What it governs: the text field, a rectangular area where the person enters or edits small, specific pieces of text, such as a name or email address; for larger volumes of text, text views are used instead.

Why: the guidelines revolve around reducing effort and ambiguity in text entry: showing the field's purpose before typing (placeholder and label), protecting sensitive data, adjusting size and spacing to the expected content, keeping a logical tab sequence between fields, and validating at the right moment to avoid unnecessarily interrupting the typing flow.

Do and avoid:
- Use a text field to ask for a small amount of information; for larger text, use text views.
- Show a hint (placeholder text) in the field, such as "Email" or "Password", to communicate its purpose; since the placeholder disappears when typing, it can also be useful to include a separate label.
- Use secure text fields to hide private data, whenever the app asks for sensitive data such as a password.
- Match the field's size to the amount of text expected, to help the person visually judge how much text to provide.
- Space multiple text fields evenly, stacking them vertically when possible and using consistent widths to create an organized layout.
- Make sure that tabbing between multiple fields follows a logical sequence; the system tries to do this automatically.
- Validate fields when it makes sense, choosing the right moment based on context (for example, validating email when switching fields; validating username or password before switching fields).
- Use a number formatter for numeric data, which configures the field to accept only numeric values and can display the value in a specific way (a certain number of decimal places, percentage, currency); do not assume the exact presentation, since formatting varies by locale.
- Adjust line breaks according to the field's needs: by default the system clips text that exceeds the field's limits; alternatively it is possible to break the line by character or word, or truncate with an ellipsis at the beginning, middle or end.
- Consider an expansion tooltip to show the full version of clipped or truncated text, appearing when the person positions the pointer over the field.
- On iOS, iPadOS, tvOS and visionOS, show the keyboard type appropriate to the expected content type.
- Minimize text entry in tvOS and watchOS apps, preferring more efficient ways to collect information, such as buttons.

Exact specifications: no fixed specification number is given in the text (the image examples mention a number with four decimal places and a currency value, but these are image descriptions, not a numeric rule).

Platform differences:
- No additional considerations for tvOS or visionOS.
- iOS, iPadOS: display a Clear button at the trailing edge of the field to erase the entry with one tap, without needing to hold down the Delete key; use images and buttons at both ends of the field, generally the leading edge to indicate the field's purpose and the trailing edge for additional features, such as a Bookmarks button.
- macOS: consider a combo box if you need to combine text entry with a list of options.
- watchOS: present a text field only when necessary, preferring whenever possible to display a list of options instead of requiring typing.

Links to other articles: Text views, Combo boxes, Entering data, Virtual keyboards.

Article change log: June 5, 2023, update reflecting changes in watchOS 10.

<!-- visual:text-fields -->
### What the illustrations show
Basis: 2 of 2 illustration sheets opened, all codes checked; the page has no video.
- The opening illustration defines the parts of the field: placeholder "Value" with cursor, circular clear button with an X at the right edge, and overlapping ruler arrows marking the width above and the height on the right (img 1138).
- The opening is the only conceptual piece, in an orange and red gradient; all the other images on the page are clean captures of the field on a neutral background, without a device frame (img 1138 to img 1142).
- For numeric data, the fields appear stacked vertically in a light gray card, with the label outside the box, on the left and ending in a colon, and the value aligned to the right inside the field (img 1139).
- The same number appears in two presentations: "100000.00" as a plain number and "$100,000.00" with a thousands separator and currency symbol (img 1139).
- The three long-text behaviors use the same test phrase for direct comparison: in a single-line field, the text is cut exactly at the right edge, without ellipsis (img 1140).
- In word wrapping, the field becomes taller, with two lines, and the phrase appears complete, split between "jumps" and "over" (img 1141).
- In truncation, the field goes back to one line and the rest of the text is replaced by an ellipsis at the end (img 1142).
<!-- /visual:text-fields -->

## Toggles (slug: toggles)

What it governs: the toggle, which lets the person choose between a pair of opposite states, such as on and off, using a different appearance to indicate each state; it can have styles such as switch and checkbox, which vary by platform. Besides toggles, all platforms also support buttons that behave like a toggle, changing appearance according to the state.

Why: the toggle always manages the state of something (not a list of options, for which another component such as pop-up button is used); Apple insists on making the visual differences between states obvious and on not relying only on color to communicate the state, because not everyone perceives color differences.

Do and avoid:
- Use a toggle to choose between two opposite values that affect the state of content or a view.
- Clearly identify the setting, view or content that the toggle affects; generally the surrounding context is already enough, but it is possible to provide a label, common in macOS apps; if using a button that behaves like a toggle, use an interface icon that communicates its purpose and update its appearance (typically changing the background) according to the current state.
- Make the visual state differences obvious (adding/removing color fill, showing/hiding the background shape, changing internal details such as a checkmark or dot); avoid relying only on different colors.

Exact specifications:
- Radio buttons are typically displayed in groups of two to five.
- If it is necessary to present more than about five options, consider a component such as pop-up buttons instead of a long list of radio buttons.

Platform differences:
- No additional considerations for tvOS, visionOS or watchOS.
- iOS, iPadOS: use the switch style only inside a list row, without needing a label because the row's content already gives the context; change the switch's default color (green) only if necessary, preferring the app's accent color when it makes sense, ensuring sufficient contrast with the colorless appearance; outside a list, use a button that behaves like a toggle, not a switch (example given: the filter button in the Phone app uses a blue highlight when active and removes the highlight when inactive); avoid providing a label that explains the button's purpose, since the interface icon combined with the alternate background appearance already communicate this.
- macOS: besides the switch style, it supports the checkbox style and also defines radio buttons; use switches, checkboxes and radio buttons in the body of the window, not in the window frame (avoid in toolbar or status bar).
  - Switches: prefer a switch for settings you want to emphasize, since it has more visual weight than a checkbox, being suitable when it controls more functionality than a checkbox typically controls (for example, turning a group of settings on or off); inside a grouped form, consider a mini switch to control the setting on a single line, whose height is similar to that of buttons and other controls, resulting in rows of consistent height; when presenting a hierarchy of settings in a grouped form, it is possible to use a regular switch for the primary setting and mini switches for the subordinate ones; in general, do not replace a checkbox already in use with a switch.
  - Checkboxes: a checkbox is a small square button, empty when off, with a checkmark when on, and it can contain a dash when the state is mixed; it typically includes a title at the trailing edge; in an editable checklist, it can appear without a title or additional content; use a checkbox instead of a switch if you need to present a hierarchy of settings, using alignment (generally along the leading edge) and indentation to show dependencies; consider radio buttons if you need to present a set of more than two mutually exclusive options; consider a label to introduce a group of checkboxes if the relationship between them is not clear, aligning the label's baseline with the group's first checkbox; accurately reflect the checkbox's state (on, off or mixed) in its appearance, showing the mixed state when the subordinate checkboxes have different states.
  - Radio buttons: a radio button is a small circular button followed by a label, typically displayed in groups of two to five, presenting a set of mutually exclusive choices; the state is selected (filled circle) or deselected (empty circle); although a radio button can also display a mixed state (indicated by a dash), this state is rarely useful because multiple states can be communicated with additional radio buttons, and for a mixed state it is better to use a checkbox; prefer a set of radio buttons for mutually exclusive options, and checkboxes if the person can choose multiple options; avoid listing too many radio buttons (more than about five options suggests considering a component such as pop-up buttons); for a single on/off setting, prefer a checkbox, since the presence or absence of the checkmark makes the state easier to understand quickly (in rare cases where a checkbox does not clearly communicate opposite states, it is possible to use a pair of radio buttons, each labeled with the state it controls); use consistent spacing when displaying radio buttons horizontally, measuring the space needed for the longest label and using that measurement consistently.

Links to other articles: Pop-up buttons, Layout.

Article change log: March 29, 2024, improved guidance for using switches in macOS apps, clarification about when a checkbox has a title, and new art for radio buttons; September 12, 2023, updated art.

<!-- visual:toggles -->
### What the illustrations show
Basis: 4 of 4 illustration sheets opened, all codes checked; the page has no video.
- The opening illustration shows the switch's pair of states with the dotted label "Label": on in dark red with the white knob on the right and ruler arrows measuring width and height, and off in white with a thin red outline and a small empty circle on the right (img 1147).
- On iOS, the switch appears inside list rows in a card, with the label "Title" on the left and a thin divider line between rows; off is a light gray track with the knob on the left, on is standard green with the white knob on the right (img 1148).
- The change of the default color is shown by repeating exactly the same card structure and changing only the color of the on state to a custom purple, in a separate image (img 1149 compared with img 1148).
- The button that behaves like a toggle is shown in two frames of the Phone app: with the segmented control on "Missed", the circular filter button to the right of the bar is solid blue and the list shows only missed calls in red (img 1150); with "All" selected, the button loses the fill, is left with only a light gray outline, and the list shows all calls (img 1151).
- In these Phone frames, the filter button's state is communicated by a background fill behind the symbol, without a switch track (img 1150, img 1151).
- The checkbox's three states appear isolated, each in its own captioned image: on is a rounded-corner square in blue with a white checkmark (img 1153), off is just a very subtle light gray outline (img 1154), and mixed is the blue square with a white horizontal dash in place of the checkmark (img 1155).
- In a list of seven checkboxes in a light gray card, the first item is in the mixed state and the following ones vary between empty and checked, showing the states side by side in a flat list (img 1152).
- The group of radio buttons has five rows in a card, and only the third circle is filled in blue with a central white dot, while the others are light gray empty circles (img 1156).
- The radio button states repeat the isolated pattern with a caption: selected is a blue circle with a central white dot and deselected is an empty circle with a very subtle gray outline (img 1157, img 1158).
- Checkbox and radio button share the same vocabulary: blue fill with a distinct internal white mark (checkmark, dash or dot) to indicate state, instead of just changing color (img 1153, img 1155, img 1157).
- In radio buttons arranged horizontally, the three blocks occupy the same width even with labels of different sizes ("A long text label", "Short label"), with the middle option selected (img 1159).
Recorded divergences: in the checkbox list (img 1152) there is no visible hierarchical indentation, although the article's text addresses hierarchy expressed through alignment and indentation.
<!-- /visual:toggles -->

## Virtual keyboards (slug: virtual-keyboards)

What it governs: on devices without a physical keyboard, the system offers several types of virtual keyboard for data entry; a virtual keyboard can provide a specific set of keys optimized for the current task (for example, a keyboard for typing email can include "@", a period or even ".com") and does not support keyboard shortcuts. When it makes sense, the app can replace the system keyboard with a custom, app-specific data entry view; on iOS, iPadOS and tvOS it is also possible to create an app extension that offers a custom, installable keyboard as a replacement for the default keyboard.

Why: choosing the right keyboard for the type of content reduces typing effort and errors, and by specifying the semantic meaning of a text entry area the system can automatically offer a compatible keyboard, including refining the corrections it proposes. Custom keyboards and input views exist for app-specific data entry tasks that the default keyboard does not handle well, but Apple asks that this replacement make sense in context, otherwise the person may find it strange not being able to go back to the system keyboard.

Do and avoid:
- Choose a keyboard that matches the type of content being edited (for example, the numbers and punctuation keyboard for numeric data).
- Consider customizing the type of the Return key if it clarifies the text entry experience (for example, a search-type Return when the app starts a search).
- When creating a custom input view, make sure it makes sense in the context of the app, since besides making data entry simple and intuitive, people need to understand why they cannot use the system keyboard there.
- Play the default keyboard sound while the person types in a custom input view, to keep the familiar feedback people expect from the system keyboard (this sound can be turned off globally in Settings > Sounds).
- Custom keyboards (via app extension) make sense when you want to expose a unique keyboard feature system-wide, such as a new way to type text or support for a language the system does not support; if the goal is a keyboard only within the app itself, prefer a custom input view.
- Once chosen in Settings, a custom keyboard can be used for text entry in any app, except when editing secure text fields and phone number fields; the person can choose multiple custom keyboards and switch between them at any time.
- Provide an obvious and easy way to switch keyboards: the Globe key on the default keyboard (which replaces the dedicated Emoji key when multiple keyboards are available) quickly switches between keyboards, and people expect an equally intuitive experience on the custom keyboard.
- Avoid duplicating system keyboard features: on some devices, the Emoji/Globe and Dictation keys appear automatically below the keyboard even with custom keyboards in use, and the app cannot affect these keys.
- Consider providing a keyboard tutorial inside the app, rather than displaying help content inside the keyboard itself.

Exact specifications: no number, measurement or duration is given in the text.

Platform differences:
- Not supported on macOS.
- iOS, iPadOS: use the keyboard layout guide so the keyboard looks like an integrated part of the interface and to keep important parts of the interface visible while the virtual keyboard is on screen; position custom controls above the keyboard (input accessory view) with care, making sure they are relevant to the current task; if other views in the app use Liquid Glass, or if the custom view looks out of place above the keyboard, apply Liquid Glass to the view that contains the controls to maintain consistency (a standard toolbar adopts Liquid Glass automatically); use the keyboard layout guide and the default padding to ensure the expected positioning of the controls.
- tvOS: displays a linear virtual keyboard when the person selects a text field using the Siri Remote; a grid keyboard screen appears when other devices are used, with the content layout adapting automatically to the keyboard; when activating a digit entry view, tvOS shows a keyboard specific to digits.
- visionOS: the system's virtual keyboard supports direct and indirect gestures and appears in a separate window that the person can move wherever they want; there is no need to consider the keyboard's location in layouts.
- watchOS: on an Apple Watch, a text field can show a keyboard if the device's screen is large enough; otherwise, the system allows dictation or Scribble for information entry; it is not possible to change the keyboard type on watchOS, but it is possible to set the content type of the text field, which the system uses to make entry easier (such as offering suggestions); the person can also use a nearby paired iPhone to type text on the Apple Watch.

Links to other articles: Entering data, Keyboards, Layout, Digit entry views, App extensions.

Article change log: June 9, 2025, guidance added about custom controls above the keyboard and update on virtual keyboard availability on watchOS; February 2, 2024, clarification about support for direct and indirect gestures on visionOS; December 5, 2023, art added for visionOS; June 21, 2023, article title changed from "Onscreen keyboards" and updated to include guidance for visionOS.

<!-- visual:virtual-keyboards -->
### What the illustrations show
Basis: 5 of 5 illustration sheets and 2 of 2 sheets of the visionOS video opened, all codes checked.
- The opening is a stylized numeric keyboard, with mnemonic letters under each number, in a diagonal gradient from red to pink and with no construction grid overlaid (img 1206).
- Each keyboard type is shown in the same standardized composition, with the type name in gray at the top, a field with a placeholder right below and the complete keyboard aligned to the base, with no device frame, which allows comparing the variations key by key (img 1207 to img 1218).
- The numeric keyboards change by minimal details: asciiCapableNumberPad and numberPad have a 3 by 3 grid with 0 and delete on the last row, with no mnemonic letters, suggestions, emoji or microphone (img 1208, img 1213); decimalPad adds the decimal point to the left of the 0 (img 1209); phonePad has the letters under the numbers and the "+*#" key in the bottom left corner, with the 0 centered (img 1215).
- The default letter keyboard has suggestions above the keys, Shift, delete, "123", space and return, with emoji in the bottom left corner and microphone on the right (img 1210); asciiCapable keeps the layout but shows only the microphone, with no emoji (img 1207).
- Context keys occupy part of the space bar without changing the base QWERTY: "@" and "." on emailAddress (img 1211), "@" and "#" on twitter (img 1216) and ".", "/" and ".com" before the return on URL (img 1217).
- webSearch swaps the gray return for a blue key with an arrow, signaling the search action through the color and the key's icon (img 1218).
- namePhonePad differs from the default only by the letter case: they appear in lowercase and the Shift key has an empty outline instead of a filled one, which shows the Shift state through the glyph's fill (img 1212 compared with img 1210 and img 1207).
- numbersAndPunctuation reorganizes the rows into numbers from 0 to 9, then punctuation and currency, then more punctuation with delete, and offers the "ABC" key to go back to letters, with microphone and no emoji (img 1214).
- The correct use of the keyboard layout guide is shown on an iPhone Account screen: stacked Email and Password fields and a black Sign In button, all visible above the keyboard that occupies the bottom half, with the white check mark in a green circle in a separate image (img 1219, img 1220).
- The errors use the same screen at other scroll positions: in the first, the Password is reduced to a thin gray bar and the Sign In disappears behind the keyboard, marked with a white X in a gray circle (img 1221, img 1222); in the second, the fields are free, but the Sign In appears cut in half by the suggestions bar (img 1223).
- In the visionOS video, the dark keyboard is a single panel with no frame, with a "Text preview" bar, a row of three suggestions and keys, floating over a real room; the panel's position and size stay fixed while only the text and the key under the finger change, and the touch appears as a white highlight on the key (video, sheet 0001, q001 to q009, highlight at q005, q006 and q008).
- The sequence goes from the empty panel with no hands (q001), to the hands entering and typing with several fingers in the air (q002 to q009), to a complete "Hello" with a cursor and three variations of the word in small capsules, already with no hands; between q010 and q011 the window gets a bit closer and further to the right, which suggests it can be repositioned (video, sheets 0001 and 0002).
Recorded divergences: the official description of the video says only that a person types on a virtual keyboard on visionOS, and the frames also show the real scene in the background, the text and suggestions appearing progressively and the window shifting; the words of the suggestions and the intermediate text fragments were only read approximately; in img 1217 the microphone is not visible in the capture; img 1219 is a concrete login screen, more specific than the official, generic description of two fields and a button.
<!-- /visual:virtual-keyboards -->

## What this group reveals about the Apple way

1. The choice of component is always guided by the volume and format of the data, not by aesthetic preference: pickers versus pull-down buttons versus lists and tables (pickers), the limit of five to seven segments in a segmented control (segmented-controls), the limit of about five options before switching radio buttons for pop-up buttons (toggles).
2. State components always require redundant visual clarity, never dependent only on color: toggles require an obvious visual difference beyond color (toggles), checkboxes use fill and a selection mark beyond the blue color (toggles), sliders fill the track with color but also have a thumb and, on watchOS, plus/minus glyphs (sliders).
3. macOS systematically receives more styles and more manual control than the other platforms: combo boxes and image wells only exist on macOS (combo-boxes, image-wells), sliders gain tick marks and a circular style only on macOS (sliders), toggles gain checkbox, radio button and mini switch only on macOS (toggles).
4. Several controls in this group are deliberately "mute" on their own and depend on a partner to show the value: the stepper does not display a value and needs a field next to it (steppers), the slider is frequently complemented by a text field and a stepper (sliders), the combo box joins free text with a list (combo-boxes).
5. Sensitive data security appears as a recurring pattern, not as an exception: secure text fields for passwords (text-fields), secure digit fields for PIN (digit-entry-views), and custom keyboards are blocked precisely in secure text fields and phone number fields (virtual-keyboards).
6. Apple prefers to keep people in place rather than switching screens: pickers should appear in context, below or near the field, avoiding a view change (pickers); keyboards should respect the keyboard layout guide so as not to cover important content (virtual-keyboards).
7. Platforms without a physical keyboard and with more limited interaction (tvOS, watchOS) receive explicit instruction to minimize text entry and prefer lists, buttons, dictation or Scribble instead of typing (text-fields, virtual-keyboards, pickers).
8. Where the system can infer the type of content, Apple asks that this inference be used instead of reinventing it: number formatter for numeric fields (text-fields) and keyboardType/textContentType to automatically choose the right keyboard (virtual-keyboards).
9. Liquid Glass appears as the most recent layer of visual consistency applied even to auxiliary controls, such as the custom controls above the keyboard on iOS and iPadOS (virtual-keyboards), showing that updates to the system's visual language propagate to supporting components, not only to main screens.
10. Groups of mutually exclusive options have a recurring informal ceiling around five items before Apple recommends a more compact component: radio buttons (toggles), segments on an iPhone (segmented-controls).

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/color-wells.md, 28 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/combo-boxes.md, 26 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/digit-entry-views.md, 22 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/image-wells.md, 23 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pickers.md, 69 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/segmented-controls.md, 58 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sliders.md, 57 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/steppers.md, 27 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/text-fields.md, 54 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/toggles.md, 74 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/virtual-keyboards.md, 81 lines read, yes, to the end.

All 11 articles in the group were read to the end in a single Read per file, with no truncation reported by the tool. No article in the group is merely a collection index page, with no text of its own.
