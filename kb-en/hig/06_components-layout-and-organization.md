# Components / Layout and organization

## Boxes (slug: boxes)

What it governs: how to visually group related information and components within a distinct border or background, with an optional title.

Why: a box communicates that its content belongs to the same logical group. This only works as long as the box stays small relative to the container that surrounds it; if it approaches the size of the window or the entire screen, it loses the power to separate content and starts to clutter the rest of the interface. A box's border is already, by itself, a strong visual element, so nesting boxes inside boxes to mark subgroups makes the interface feel crowded; prefer padding and alignment to communicate internal subdivisions.

Do and avoid:
Prefer to keep the box small relative to the view that contains it.
Use padding and alignment to express subgroupings instead of nested boxes.
Provide a short title if it helps clarify the box's content, since appearance alone is sometimes not enough, and the title also helps VoiceOver users anticipate what they will find.
If you use a title, write a brief phrase with sentence-style capitalization and avoid final punctuation, except in a settings panel, where a colon is added to the title.

Exact specifications: the text does not include any number, measurement or default value.

Platform differences: no additional considerations for visionOS. Not supported on tvOS or watchOS. On iOS and iPadOS, the box uses the secondary and tertiary background colors by default. On macOS, the box's title appears above it by default.

Links to other articles: Layout.

<!-- visual:boxes -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0183), code checked; no video.
- The box is drawn as a rectangle with rounded corners in an orange to pinkish red gradient, with a dashed inner rectangle marking the content area (img 0183).
- The inner content simulates a list of properties: dark gray horizontal bars of varying length in two columns, the left one narrow like a label and the right one wide like a value (img 0183).
- Red double arrows measure four distances, above and below the inner block to the top and bottom edges and to the left and right to the outer edge, showing symmetric padding and a constant margin on all four sides (img 0183).
- No number is printed: the constant margin works as a visual unit of measurement, with no numeric grid or written measurement (img 0183).
<!-- /visual:boxes -->

## Collections (slug: collections)

What it governs: how to present an ordered set of content, typically image-based, in a customizable and highly visual layout.

Why: collections exist to display visual content efficiently, and it is important to keep the default layout (horizontal row or grid) because that is what people already expect; a customized layout can confuse or draw undue attention to itself instead of the content. The ease of choosing an item is also central: if an item is hard to reach, the person gets frustrated and loses interest before reaching what they wanted.

Do and avoid:
Use the default row or grid layout whenever possible; avoid a customized layout that confuses.
Consider using a table instead of a collection for text, since textual information is simpler and more efficient to digest in a scrollable list.
Make it easy to choose an item, with adequate padding around the images so that focus or hover effects stay visible and the content does not overlap.
Add customized interactions when needed; by default people tap to select, tap and hold to edit, and swipe to scroll.
Consider using animations to give feedback when inserting, deleting or reordering items; collections support default animations for these actions, in addition to allowing customized animations.

Exact specifications: the text does not include any number, measurement or default value.

Platform differences: no additional considerations for macOS, tvOS or visionOS. Not supported on watchOS. On iOS and iPadOS, use caution when making dynamic layout changes: avoid changing the layout while people are viewing and interacting with it, unless it is in response to an explicit action.

Links to other articles: Lists and tables, Image views, Layout.

<!-- visual:collections -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0252), code checked; no video.
- Eight identical image icons, a rounded frame with a sun circle and a stylized mountain in light pink over red, form a regular grid of two rows by four columns over an orange to pinkish red gradient, as the official description states (img 0252).
- Red measurement arrows mark the outer margin: above and below the icon block to the container edge, and to the left and right of the block to the edge (img 0252).
- Two smaller marks inside the grid measure the spacing between cells, one horizontal between the third and fourth image of the top row and one vertical between the third image on top and the one below (img 0252).
- The measurement vocabulary is the same one the notes point out in boxes and buttons, bidirectional arrows with no numbers, applied here to show the collection as a grid with consistent spacing between items (img 0252).
<!-- /visual:collections -->

## Column views (slug: column-views)

What it governs: a column view (also called a browser) allows navigating a data hierarchy using a series of vertical columns, where each column represents a level of the hierarchy.

Why: this format works well when the hierarchy is deep and people tend to navigate back and forth frequently between levels, without needing the sorting features a table offers. Always showing the root of the hierarchy in the first column gives people a consistent starting point to restart navigation.

Do and avoid:
Consider using a column view when the hierarchy is deep, navigation between levels is frequent, and there is no need for sorting as in a table.
Show the root level of the data hierarchy in the first column.
Consider showing information about the selected item when there are no nested items to display, as the Finder does with a preview and data such as creation date, modification date, type and size.
Let people resize the columns, especially important when long item names do not fit the default width.

Within a column, a parent item that contains children is marked with a triangle icon; when the parent is selected, the next column shows its children, and navigation continues until an item with no children.

Exact specifications: the text does not include any number, measurement or default value.

Platform differences: not supported on iOS, iPadOS, tvOS, visionOS or watchOS (column view is exclusive to macOS). A note in the article recommends that, to present hierarchical content on iPadOS or visionOS, Split views be considered instead of column view.

Links to other articles: Lists and tables, Outline views, Split views.

<!-- visual:column-views -->
### What the illustrations show
Basis: 1 of 1 illustration sheet opened (img 0342), code checked; no video and no dark version recorded.
- The column view is drawn as three columns side by side separated by thin vertical lines, tinted in red and pink over a reddish orange gradient background (img 0342).
- The first column lists three folders, each with a folder icon on the left and a chevron on the right indicating that it opens the next column; folder A appears selected with a background only slightly lighter (img 0342).
- The second column lists five images with a thumbnail on the left; image B appears with a solid red background, a much stronger contrast than the first column's highlight (img 0342).
- The selection uses two levels of highlight at the same time: weak for the column whose selection has already advanced to the next one and solid for the item with active focus, which makes the cascading column-to-column navigation visible (img 0342).
- The width of the columns grows from left to right, and the last one, the widest, is not a list, but a details panel for the selected item (img 0342).
- The details panel stacks the information by importance: large thumbnail, file name in bold and larger than the item names in regular weight, a short line of format and size, and then an Information section with label and value pairs aligned in columns, creation and modification, separated by a thin divider (img 0342).
Recorded divergences: the official description speaks only generically of three columns with folders, images and file information, without the two levels of highlight or the cascade that the image shows.
<!-- /visual:column-views -->

## Disclosure controls (slug: disclosure-controls)

What it governs: controls that reveal and hide information and functionality associated with specific controls or views, in the disclosure triangle and disclosure button variants.

Why: hiding details until they are relevant avoids overwhelming people with too many detailed options at once. The recommendation to position the most used controls at the top of the disclosure hierarchy, with more advanced functionality hidden by default, exists so that essential information can be found quickly without requiring the person to open everything first.

Do and avoid (disclosure triangles):
Use a disclosure triangle to show and hide information and functionality associated with a view or list of items.
The triangle points inward, from the leading edge, when the content is hidden, and downward when it is visible; clicking or tapping toggles between the two states and the view expands or collapses accordingly.
Provide a descriptive label when using a disclosure triangle, indicating what is being revealed or hidden, such as "Advanced Options".

Do and avoid (disclosure buttons):
Use a disclosure button to show and hide functionality associated with a specific control, as in macOS's Save sheet, which expands the dialog for advanced navigation options.
The button points downward when the content is hidden and upward when it is visible; clicking or tapping toggles the state and the view expands or collapses.
Position a disclosure button near the content it shows and hides, establishing a clear relationship between the control and the expanded options.
Use at most one disclosure button in a single view; multiple disclosure buttons add complexity and can confuse.

Exact specifications: the text does not include any number, measurement or default value.

Platform differences: no additional considerations for macOS. Not supported on tvOS or watchOS. On iOS, iPadOS and visionOS, disclosure controls are available via the SwiftUI view DisclosureGroup.

Links to other articles: Outline views, Lists and tables, Buttons. There is also a related video cited ("Stacks, Grids, and Outlines in SwiftUI").

<!-- visual:disclosure-controls -->
### What the illustrations show
Basis: 2 of 2 illustration sheets open (img 0464 to 0468), codes checked; no video.
- Pair of disclosure button states: two white square buttons side by side, labeled Collapsed and Expanded, with a chevron pointing down on the first and up on the second; only under the expanded one does a larger empty red rectangle appear, representing the revealed content panel (img 0464).
- Finder-style list, fully collapsed: three folder rows with a blue icon and, to the left of the icon, a triangle pointing right, over alternating light, light gray and light backgrounds (img 0465).
- The same list with the middle folder expanded: its triangle now points down and below it three indented rows appear, with smaller folder icons and their own triangles pointing right, while the neighboring folders remain collapsed (img 0466, in sequence with 0465).
- The macOS save dialog in the collapsed state is compact: name field, empty tags field, a Where row with a folder selector and the disclosure button with a chevron pointing down right next to that selector, plus Cancel and Save, with no file browser (img 0467).
- After the click, the same window grows vertically and gains a sidebar with Shared, Favorites and Locations, a column browser with the selected folder, back and forward arrows, view selectors, a search field and a New Folder button at the bottom, without changing the name field at the top (img 0468, in sequence with 0467).
- Both controls are demonstrated through pairs of states, side by side or in sequence: the triangle changes direction and the revealed content enters indented within the list itself, while the button flips the chevron and, in the save dialog, makes the same window grow until it shows a full file browser (img 0464 to 0468).
<!-- /visual:disclosure-controls -->

## Labels (slug: labels)

What it governs: a label is static text that people can read and often copy, but not edit; it appears in buttons, menu items and views to help understand the current context and what can be done next.

Why: the choice between label, text field and text view depends on the volume of text and the need for editing, which guides the person to use the right component for the amount and editability of the content. The four system label colors exist to consistently communicate relative levels of visual importance of the text across the platform.

Do and avoid:
Use a label to display a small amount of text that does not need to be edited; use a text field if you need to edit a little text, and a text view if you need to display (and optionally edit) a large amount of text.
Prefer system fonts; a label can display plain or styled text and supports Dynamic Type by default (where available); when adjusting the style or using custom fonts, make sure the text remains legible.
Use the label colors provided by the system to communicate relative importance.
Make the text of a label selectable when it contains useful information, such as an error message, a location or an IP address, so the person can copy and paste it elsewhere.

Exact specifications: the article defines four system label colors and their API names by platform.
| System color | Example use | iOS, iPadOS, tvOS, visionOS | macOS |
| Label | Primary information | label | labelColor |
| Secondary label | A subtitle or supplementary text | secondaryLabel | secondaryLabelColor |
| Tertiary label | Text that describes an unavailable item or behavior | tertiaryLabel | tertiaryLabelColor |
| Quaternary label | Watermark text | quaternaryLabel | quaternaryLabelColor |

Platform differences: no additional considerations for iOS, iPadOS, tvOS or visionOS. On macOS, to display non-editable text in a label, the isEditable property of NSTextField is used. On watchOS, date and time text components display the current date, the current time, or a combination of the two, with various configurable formats, calendars and time zones; a countdown timer component displays a precise count (counting down or up) in various formats; when using the date and timer components provided by the system, watchOS automatically adjusts the label's presentation to the available space and updates the content without additional input from the app. The article also suggests considering date and timer components in complications.

Platform differences, historical record: the article's change log records an update on June 5, 2023 to reflect changes in watchOS 10.

Links to other articles: Text fields, Text views, and, within the text itself, Color and Complications.

<!-- visual:labels -->
### What the illustrations show
Basis: 1 of 1 illustration sheet open (img 0676 to 0678), code checked; no video.
- The cover swaps the sketch with a guide grid for a specification diagram: the word "Label" centered, large and bold, inside a dotted box that marks its area, over a gradient from orange to pink (img 0676).
- Red arrows dimension the text's bounding box: one vertical above and below, one horizontal crossing the full width of the card and a vertical mark to the right of the word (img 0676).
- Below the word, the annotation names the typographic and color attributes, "System Font, Body (Emphasized)" and "Primary Text Color" (img 0676).
- On watchOS, the date and time label is a black rectangle with rounded corners, with no watch face frame, with white text: the date against the leading edge on the left and the time on the trailing edge on the right, on the same line (img 0677).
- The timer label uses the same rounded black shape, smaller and narrower, with a single large numeric value centered (img 0678).
- The two watchOS examples keep the same container and vary only content and alignment: two values on opposite edges versus a single value at the center (img 0677 and 0678).
Recorded divergences: the official caption talks about a styled text label tinted red, but the image is, in practice, a diagram of measurements and typography (img 0676).
<!-- /visual:labels -->

## Lists and tables (slug: lists-and-tables)

What it governs: lists and tables present data in one or more columns of rows, and can represent data organized into groups or hierarchies, supporting selection, addition, removal and reordering.

Why: the row-based format is especially well suited to making text easy to scan and read; that is why the text recommends preferring lists and tables for textual content and using a collection when items vary a lot in size or there are many images. The choice of table or row style should coordinate with the type of data and the platform, because different styles communicate grouping, hierarchy or platform-specific experiences.

Do and avoid (general):
Prefer displaying text in a list or table; for items that vary a lot in size or many images, consider a collection.
Let people edit a table when it makes sense; they appreciate being able to reorder a list even without being able to add or remove items. On iOS and iPadOS, you need to enter an editing mode before selecting table items.
Provide appropriate feedback when selecting a list item: a table that helps navigate a hierarchy usually highlights the selected row persistently, while an options table usually highlights the row briefly before adding an image, such as a checkmark, indicating selection.

Do and avoid (content):
Keep item text concise so the row's content is comfortable to read, minimizing truncation and line breaking.
Consider ways to preserve the legibility of text that could be cut off or truncated; sometimes an ellipsis in the middle of the text helps distinguish the item because it preserves the beginning and end of the content.
Use descriptive column headers in multi-column tables, with nouns or short noun phrases in title-style capitalization, with no ending punctuation; if there is no column header in a single-column table, use a label or header to give context.

Do and avoid (style):
Choose a table or list style that coordinates with the data and the platform.
Choose a row style suited to the information being displayed, for example a small image on the leading edge followed by a brief explanatory label.

Exact specifications: the text does not give any number, measurement or default value; it mentions style names (grouped, elliptical, bordered) without associated numeric values.

Platform differences:
iOS, iPadOS, visionOS: use an info button (called a detail disclosure button when it appears in a list row) only to reveal more information about a row's content; it does not support navigating through a hierarchical table or list. To allow navigating to a row's subviews, use a disclosure indicator accessory control. Avoid adding an index to a table that displays controls, such as disclosure indicators, on the trailing edge of rows, because both the index and those elements sit on the trailing side and it can be hard to use one without triggering the other.
macOS: when it adds value, let people click a column header to sort the table by that column; if they click the header of an already sorted column, reorder in the opposite direction. Allow resizing columns. Consider using alternating row colors in a multi-column table to help track values across columns, especially in wide tables. Use an outline view instead of a table view to present hierarchical data, since the outline view looks like a table view but includes disclosure triangles to expose nested levels.
tvOS: confirm that images near a table still look good, since each focused row grows slightly in size and stands out; the corners of a focused row can also become rounded, which can affect images on the sides; do not add your own masks to round corners.
watchOS: when possible, limit the number of rows, since short lists are easier to scan, but sometimes people expect to see a long list (the example given is subscribing to many podcasts); help by listing the most relevant items and providing a way to see more. Restrict the length of detail views if you want to support paginated vertical navigation, since that navigation only works when the detail views are short; if they scroll, paginated vertical navigation between them stops working.

Article history record: change log on June 21, 2023 (updated to include guidance for visionOS) and June 5, 2023 (updated to reflect watchOS 10 changes).

Links to other articles: Collections, Outline views, Layout, and within the text, Search fields.

<!-- visual:lists-and-tables -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_lists-and-tables, sheet 0001), codes checked; no video.
- The opening does not use an annotated geometric sketch: it shows directly a grouped example table, tinted red and orange, with header text above the card, three rows inside it and footer text below (img 0697).
- Each row of the opening table carries a chevron at the trailing edge and is separated from the next by a thin divider; header and footer sit outside the card, not inside it (img 0697).
- The grouped list is built as a light gray card with rounded corners that contains an inner white card, with the rows separated by thin dividers (img 0698, img 0699).
- To reveal information without navigating, each row carries the title on the left and a circular blue "i" icon at the trailing edge (img 0698).
- To navigate to the next level, the row swaps the "i" for a chevron pointing right, preceded by secondary gray value text ("Detail"), with the title in bold on the left (img 0699).
- The pair img 0698 and img 0699 keeps the same row structure and changes only the trailing-edge element, which visually isolates the difference between an information button and a navigation indicator.
- The typographic hierarchy of the navigation row is bold title on the left and secondary gray value on the right, next to the chevron (img 0699).
Recorded divergences: in img 0699 the secondary gray text "Detail" appears before the chevron, which the official description does not mention (it cites only the chevron at the trailing edge).
<!-- /visual:lists-and-tables -->

## Lockups (slug: lockups)

What it governs: lockups combine multiple separate views (a content view, a header and a footer) into a single interactive unit, used in tvOS in the cards, caption buttons, monograms and posters variants.

Why: header, footer and content view expand and contract together when the lockup gains focus, so the spacing between lockups needs to account for this growth to avoid overlapping or displacing other lockups. Keeping consistent sizes within a row or group makes the set of buttons or content images more visually pleasing.

Do and avoid:
Leave adequate space between lockups, since a focused lockup expands in size.
Use consistent lockup sizes within a row or group.
In caption buttons, make sure that on gaining focus they tilt following the swipe motion: when aligned vertically, they tilt up and down; when aligned horizontally, they tilt sideways; when arranged in a grid, they tilt in both directions.
In monograms, prefer images to initials, since an image of a person creates a more intimate connection than text; if the image is not available, the person's initials appear in its place.

Exact specifications: the text does not carry any number, measurement or default value.

Platform differences: lockups are not supported on iOS, iPadOS, macOS, visionOS or watchOS; they are a component exclusive to tvOS.

Links to other articles: Designing for tvOS, Layout, and within the text, Image views.

<!-- visual:lockups -->
### What the illustrations show
Basis: 2 illustration sheets viewed (hig-img_lockups, sheets 0001 and 0002), codes checked; no video.
- The opening defines the lockup as a stacked block of a circular icon, a large bold title line and a smaller note line, with dashed rectangles marking each element, a double arrow measuring the width of the circle and a vertical arrow measuring the height of the whole block (img 0733).
- The typographic hierarchy annotated in the lockup is two lines with distinct roles, headline above and footnote below, in clearly different sizes (img 0733).
- Focus on tvOS is signaled by the same contrast: the focused item turns white and stands out from its light gray neighbors (img 0734, img 0735, img 0736, img 0737, img 0738); it also gains a shadow in img 0734, img 0735, img 0737 and img 0738, and appears larger than its neighbors in img 0734, img 0737 and img 0738.
- The spacing between lockups appears as empty vertical bands, highlighted in pink, between content columns, reserving the slack for the item to grow without touching its neighbors (img 0734).
- The focused card shows the division into header, body and footer with a rating example (score and five stars, four filled in yellow) over placeholder text lines, highlighted in white in a row of gray cards (img 0735).
- The focused caption button gains a slight sideways rotation, consistent with the horizontal row, while the other three buttons stay straight and gray (img 0736).
- In the focused monogram, the circle grows, gains a shadow and a sharper person icon, and only it displays the two caption lines, title and subtitle; the neighboring monograms are smaller and without legible text (img 0737).
- The poster is a vertical image with a label below, arranged in a row under a header band near the bottom edge of the screen; the focused poster rises in layer and increases in size (img 0738).
Recorded divergences: the focus tilt only appears in the horizontal variant (img 0736); the vertical variant described in the text is not shown.
<!-- /visual:lockups -->

## Outline views (slug: outline-views)

What it governs: an outline view presents hierarchical data in a scrollable list of cells organized in columns and rows, with at least one column containing the primary hierarchical data; parent containers have disclosure triangles that expand to reveal their children.

Why: the outline view serves to display text-based content well and usually appears on the leading side of a split view, with related content on the opposite side; keeping the hierarchy exposed in only one column, with other columns showing supplementary attributes, avoids confusing the data structure. Retaining the person's expansion choices avoids them needing to renavigate to the same point next time.

Do and avoid:
Use a table instead of an outline view for non-hierarchical data.
Expose the data hierarchy only in the first column; other columns show attributes that apply to the hierarchical data.
Use descriptive column headers, with nouns or short noun phrases in title-style capitalization and no punctuation, especially avoiding a trailing colon. Always provide column headers in a multicolumn outline view; in a single-column outline view with no header, use a label or another way to give context.
Consider letting people click column headers to sort; in a sortable outline view, clicking a header sorts ascending or descending by that column, with additional secondary sorting possibly happening behind the scenes; clicking the primary column header sorts at each level of the hierarchy (in the Finder, for example, all top-level folders are sorted, then the items within each folder); clicking again on an already sorted header reverses the direction.
Let people resize columns.
Make it easy to expand or collapse nested containers; for example, clicking the disclosure triangle of a folder in the Finder expands only that folder, but Option-clicking the disclosure triangle expands all subfolders.
Retain the person's expansion choices, storing the state to display it again next time.
Consider alternating row colors in multicolumn outline views to help track values across columns.
Let people edit data if it makes sense in the app; in an editable cell, people expect to be able to click once to edit the content, and it can respond differently to a double click (for example, a single click edits a file's name, a double click opens the file). Also consider allowing rows to be reordered, added and removed.
Consider using a centered ellipsis to truncate cell text instead of clipping it, since the ellipsis in the middle preserves the start and end of the content.
Consider offering a search field to help find values quickly in an extensive outline view; windows with an outline view as the main feature usually include a search field in the toolbar.

Exact specifications: the text does not carry any number, measurement or default value.

Platform differences: outline views are not supported on iOS, iPadOS, tvOS, visionOS or watchOS (exclusive to macOS).

Links to other articles: Column views, Lists and tables, Split views, and within the text, Search fields. There is also a related video cited ("Stacks, Grids, and Outlines in SwiftUI").

<!-- visual:outline-views -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_outline-views, sheet 0001), codes checked; no video.
- The outline view appears as a four-column table with short noun headers (name, date modified, size, type), separated by thin vertical lines (img 0826).
- Parent containers carry a disclosure arrow: pointing down when the folder is expanded and to the right when it is collapsed, with a folder or image icon before each name (img 0826).
- Measurement guides annotated in darker red mark the indent of the children relative to the parent folder: a vertical dashed guide and bracket-shaped markers in the left margin indicating the indentation at two different levels (img 0826).
- A vertical guide with a height marker next to the child rows annotates the row height (img 0826).
- The selected row receives a solid red fill with white text, inverting the contrast relative to the unselected rows (img 0826).
Recorded divergences: the official description talks only about the list of folders and images in four columns; the indentation-by-level and row-height annotations appear only in the image.
<!-- /visual:outline-views -->

## Split views (slug: split-views)

What it governs: a split view manages the presentation of multiple adjacent panes of content, each one able to contain tables, collections, images or custom views, typically to show multiple levels of the app's hierarchy at the same time and support navigation between them.

Why: when an item is selected in the primary pane, the secondary pane displays that item's content (and a tertiary pane can exist if the secondary one also has additional content). It is common to use a split view to display a navigation sidebar, where the initial pane lists the top-level items or collections and the secondary and tertiary panes present child collections and item details. Persistently highlighting the current selection in each pane that leads to a detail view clarifies the relationship between the content of the various panes and helps the person orient themselves.

Do and avoid:
To support navigation, persistently highlight the current selection in each pane that leads to the detail view.
Consider allowing drag and drop of content between panes, since the split view gives access to multiple levels of hierarchy and this makes it easier to move content from one part of the app to another.

Exact specifications: in tvOS, by default a split view dedicates one third of the screen width to the primary pane and two thirds to the secondary pane, and can also use a half-and-half layout. In macOS, the divider in thin divider style measures one point wide.

Platform differences:
iOS: prefer to use split view in a regular environment, not compact, since it needs horizontal space to display multiple panes; in a compact environment, such as iPhone in portrait, it becomes difficult to display multiple panes without text wrapping or truncation.
iPadOS: can include two vertical panes, like Mail, or three vertical panes, like Keynote. You need to consider narrow, compact and intermediate window widths, since iPad windows are fluidly resizable, ensuring that it's possible to navigate between panes logically at each width.
macOS: panes can be arranged vertically, horizontally or both, with dividers between panes that support dragging to resize. Set reasonable defaults for minimum and maximum pane sizes, keeping the divider visible (if a pane gets too small, the divider can seem to disappear and become hard to use). Consider letting a pane be hidden when it makes sense, as in Keynote, which lets you hide the navigator and the presenter notes to reduce distractions or gain editing space. Provide multiple ways to reveal hidden panes, such as a toolbar button or a menu command with a keyboard shortcut. Prefer the thin divider style, avoiding thicker styles unless there's a specific need, such as when both sides of the divider use strong linear elements that make it hard to distinguish a thin divider.
tvOS: a split view can work well for filtering content, displaying in the secondary pane the results of the filter category chosen in the primary pane. Choose a split view layout that keeps the panes balanced (one third/two thirds by default, or half-and-half). Display a single title above the split view for the content as a whole, with no separate titles per pane. Choose the title alignment according to the type of content in the secondary pane: if it contains a collection of content, consider centering the title in the window; if it contains a single main view of important content, consider positioning the title above the primary pane to give more space to the content.
visionOS: to display supplemental information, prefer a split view over a new window, since it gives convenient access to more information without leaving the current context, while opening a new window can confuse someone who is navigating or repositioning content and requires managing the relationship between views across multiple windows. If you need to request a small amount of information or present a simple task before the person returns to the main task, use a Sheet.
watchOS: the split view displays the list view or a detail view as a full-screen view. Automatically display the most relevant detail view when the app launches, showing information relevant to location, time or recent actions. If the app displays multiple detail pages, put the detail views in a vertical Tab view, allowing the Digital Crown to be used to scroll between tabs; watchOS also displays a page indicator next to the Digital Crown, showing the number of tabs and the one currently selected.

Article history log: change log on June 9, 2025 (platform considerations added for iOS and iPadOS), December 5, 2023 (guidance added for split views in visionOS) and June 5, 2023 (guidance added for split views in watchOS).

Links to other articles: Sidebars, Tab bars, Layout, and within the text, Drag and drop, Sheets, Tab views.

<!-- visual:split-views -->
### What the illustrations show
Basis: 2 illustration sheets viewed (hig-img_split-views, sheets 0001 and 0002), codes checked; no video.
- The opening names the three roles of a three-column split view, sidebar, canvas and inspector, inside a window with the three control circles in the upper left corner (img 1099).
- The opening's measurement arrows cover the full width of the window and, at the base, only the side columns; the central canvas has no arrow of its own and fills the remaining space (img 1099).
- In macOS, the anatomy is diagrammed as a laptop's entire screen divided by straight lines into light blue blocks, with no overlap or transparency, changing only the position of the dividers from one example to another (img 1100, img 1101, img 1102).
- Stacked panes: a single horizontal line separates a large upper pane from a smaller pane at the base (img 1100).
- Side-by-side panes: a single vertical line separates a noticeably narrower left pane from a wider right pane, that is, an asymmetric proportion (img 1101).
- Mixed arrangement: a narrow column on the left occupies the full height, and the area on the right is subdivided by a horizontal line into a larger pane on top and a smaller one at the bottom (img 1102).
- In watchOS, the screen shows a vertical list with a title in blue, a section header in white and three items separated by thin lines, on a black background, with no side-by-side panes (img 1103).
- Navigation between pages on the watch is indicated by a thin column of marks next to the Digital Crown, with a longer, lighter segment highlighted, which suggests a position indicator, with no text or arrows (img 1103).
Recorded divergences: at the resolution viewed, it was not possible to confirm that the highlighted segment in img 1103 corresponds to the fifth tab, as the official description states; only a multi-position indicator with one highlighted can be seen.
<!-- /visual:split-views -->

## Tab views (slug: tab-views)

What it governs: a tab view presents multiple mutually exclusive content panes in the same area, between which people switch using a tabbed control.

Why: the appearance of a tab view strongly suggests enclosure, so people expect each tab to show content that's somehow similar to or related to that of the other tabs. The preference for a tabbed control over a pop-up button is justified because the former requires a single click or tap to select (versus two for the pop-up) and presents all the options on screen at the same time, while the pop-up requires clicking to see the options.

Do and avoid:
Use a tab view to present closely related areas of content.
Make sure the controls within a pane affect only the content of that same pane, since panes are mutually exclusive and must be fully self-contained.
Provide a label for each tab that describes the content of its pane, generally with nouns or short noun phrases (a verb or short verb phrase can make sense in some contexts), using title-style capitalization.
Avoid using a pop-up button to switch between tabs, except when there are too many panes to reasonably display as tabs, in which case the pop-up can be a reasonable alternative.
Avoid providing more than six tabs in a tab view, since this can overload it and create layout problems; for six or more panes, consider another way of implementing the interface, such as presenting each tab as a view option in a pop-up button menu.

Anatomy: the tabbed control appears at the top edge of the content area, and can be hidden when the app switches between panes programmatically. When the tabbed control is hidden, the content area can be borderless, bezeled or bordered with a line; a borderless view can be solid or transparent. Generally, the tab view is inset, leaving a window-body area margin on all sides; it's possible to extend the tab view to the edges of the window, but this layout is uncommon.

Exact specifications: a maximum of six tabs recommended in a tab view (above that, consider another approach).

Platform differences: not supported on iOS, iPadOS, tvOS or visionOS. On iOS and iPadOS, for similar functionality, consider using a segmented control. On watchOS, tab views are displayed using page controls.

Article history log: change log on June 5, 2023 (guidance added for using tab views in watchOS).

Links to other articles: Tab bars, Segmented controls.

<!-- visual:tab-views -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_tab-views, sheet 0001), codes checked; no video.
- The opening shows the tab view as a rectangular container with measurement marks on the four edges and a pill-shaped segmented control overlapping the top edge, with three generic-label tabs (img 1118).
- The active tab is marked by a more opaque background, not by an underline or text color (img 1118, img 1119).
- The dividers between tabs disappear next to the selected tab: there's a thin vertical line between the second and third tabs, but none between the first, which is highlighted, and the second (img 1118).
- In the actual macOS window, the three-tab control sits at the top edge, with the first one selected over a rounded light gray background and the window body below empty (img 1119).
- The opening's measurement marks are vertical arrows at the top and bottom and horizontal arrows on both sides, treating the entire container as the measured area, not just the tab control (img 1118).
- On watchOS there is no visible segmented control: the current page is marked in a vertical column of dots next to the Digital Crown, where the current dot is larger and white and the others are smaller (img 1120).
- The watch screen uses a black background with time and title in blue at the top and an empty body, isolating the page indicator as the sole navigation element (img 1120).
<!-- /visual:tab-views -->

## What this group reveals about the Apple way

Apple treats hierarchical layout as a central macOS problem and solves the same problem in three distinct ways depending on the expected navigation pattern: column views for frequent back and forth between levels without needing to sort, outline views for hierarchical data with multiple attribute columns and sorting, and split views for showing several levels simultaneously side by side (column-views, outline-views, split-views).

Several organization components (column views, outline views, tab views) are explicitly exclusive to macOS or have very limited support outside it, which shows that macOS maintains an information-density vocabulary that the other platforms, optimized for touch, do not inherit (column-views, outline-views, tab-views).

Repeatedly the documentation recommends hiding complexity by default and revealing it only on demand: boxes avoid visual nesting, disclosure controls hide advanced options, outline views hide levels via disclosure triangles (boxes, disclosure-controls, outline-views).

Centered ellipsis (ellipsis in the middle of the text) appears as a recurring solution for truncation in at least two distinct components, signaling a consolidated interface pattern and not a one-off choice (lists-and-tables, outline-views).

Alternating row colors to make it easier to track values in wide tables appear as a repeated recommendation in three different tabular data components, showing that it is a platform convention, not an app whim (lists-and-tables, outline-views, split-views, the latter regarding the equivalent observation about strong linear elements next to dividers).

Navigation state (highlighted selection, container expansion) must be persisted and resumed, not just shown in the moment: outline views store expansion choices and split views keep the highlighted selection persistent to orient the person (outline-views, split-views).

tvOS components (lockups, the focus behavior in lists-and-tables, split views on tvOS) share their own vocabulary of focus, tilt and expansion when gaining prominence, distinct from the rest of the platforms, because remote control navigation requires constant visual indication of where the focus is (lockups, lists-and-tables, split-views).

Several articles reference one another forming explicit decision pairs that the documentation uses to guide the choice of the right component: table versus outline view for hierarchical data, column view versus split view for hierarchical navigation on iPadOS/visionOS, tab view versus pop-up button when there are many options (lists-and-tables, outline-views, column-views, split-views, tab-views).

Apple is consistent in asking for title-style capitalization with no final punctuation for column headers and tab labels, and sentence-style capitalization for descriptive titles such as a box's, a text style distinction applied systematically across components (boxes, lists-and-tables, outline-views, tab-views).

Concrete limit rules (maximum number of tabs, minimum number of disclosure buttons per view) appear only where Apple has already tested the point at which the interface stops working well, and do not appear in components without this type of excess risk, such as boxes or lockups.

## Reading evidence

/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/boxes.md, 32 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/collections.md, 30 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/column-views.md, 26 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/disclosure-controls.md, 46 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/labels.md, 52 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/lists-and-tables.md, 63 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/lockups.md, 48 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/outline-views.md, 38 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/split-views.md, 66 lines read, to the end: yes
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/tab-views.md, 43 lines read, to the end: yes
