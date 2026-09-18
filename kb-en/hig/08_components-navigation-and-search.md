# Components / Navigation and search

## Path controls (slug: path-controls)

What it governs: a path control shows the file system path of a selected file or folder, like the Finder's path bar.

Why: the goal is to give hierarchical location context (root disk, parent folders, selected item) in a compact way, and to allow both viewing and navigating or selecting a new item through that hierarchy.

Do and avoid:
- Use the path control in the window's body, not in the window frame.
- Path controls are not meant for toolbars or status bars (the Finder's path bar sits in the window's body, at the bottom, not in the status bar).
- In the standard variant, if the list is too long to fit, the control hides names between the first and last item.
- If you make the control editable in the standard variant, the person can drag an item onto the control to select it and display its path.
- In the pop up variant, if you make the control editable, the menu gains an additional Choose command to select an item; it is also possible to drag an item onto the control.

Exact specifications: the text does not include numbers, measurements or values.

Platform differences: not supported on iOS, iPadOS, tvOS, visionOS or watchOS. It is a macOS-exclusive component (AppKit, NSPathControl).

Links to other articles: File management.

<!-- visual:path-controls -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_path-controls, sheet 0001), codes checked; no video.
- The opening shows the path control as a horizontal chain of segments, each with an icon and name, joined by arrows, below a document icon that gives the file's context, separated by a horizontal line (img 0837).
- Annotation labels connected by thin vertical lines name the role of each link: root disk, parent folder and selected item (img 0837).
- Each segment uses an icon that indicates the type of location: disk for the root, folder for the parent folder and file for the selected item (img 0837).
- The standard variant appears as a Finder path bar in light gray, with four locations in sequence and placeholder labels, a disk icon on the first and a folder icon on the other three, separated by arrows pointing right (img 0838).
- The pop-up variant is a single compact segment in light gray, with a blue folder icon, a title and a pair of up and down arrows at the trailing edge, instead of the linear chain (img 0839).
<!-- /visual:path-controls -->

## Search fields (slug: search-fields)

What it governs: the search field is an editable text field that allows searching a set of content by specific terms, combining a search icon, a Clear button and placeholder text.

Why: Apple treats search as something that should feel responsive and contextual, each platform has a search access pattern compatible with its goals and layout, and placeholder text and suggestions exist to reduce the cognitive effort of whoever is searching, helping the person understand the scope even before typing.

Do and avoid:
- Use placeholder text to indicate what can be searched, reinforcing the scope of the search or educating about the type of accessible content.
- If possible, start the search immediately as the person types, to give a sense of continuous response.
- Consider showing suggested search terms, such as recent searches before typing begins or predictive suggestions while the person types.
- Simplify the results: show the most relevant ones first to minimize scrolling, and consider categorizing them.
- Consider allowing results to be filtered, for example with a scope bar in the results' content area.
- Use a scope bar to filter between clearly defined search categories, helping move from a broader scope to a narrower one.
- Start from a broader scope by default and let the person refine it as needed.
- Use tokens to filter by common search terms or items; a token gets visual treatment that indicates it can be selected and edited as a single item.
- Consider combining tokens with search suggestions, since people may not know which tokens exist.

Exact specifications: the text does not include numbers in pt, px or ms.

Platform differences:
- No additional considerations for visionOS.
- iOS: there are three main positions for the search entry point: as a tab in a tab bar, in a toolbar (at the top or at the bottom), or inline with the content. As a tab, there are two styles: standard tab (leads to a search destination page with the field at the top, good for exploring rich content, as in the Apple TV example) and button appearance (focuses the field and shows the keyboard immediately, ideal for quick, transient search). In a bottom toolbar, the field can appear expanded or as a button that animates into a search field above the keyboard; positioning it at the bottom is preferable when search is a priority (examples: Settings, Mail, Notes). In a top toolbar (navigation bar), search appears as a toolbar button; use it at the top when it's important not to cover content at the bottom or when there is no bottom toolbar (example: Wallet). As an inline field, placing the search next to the content it searches reinforces the relationship between the two, useful when the app has more than one search field and location matters for the scope (example: Music, library); when at the top, position it above the list it searches and consider pinning it to the top toolbar during scrolling.
- iPadOS and macOS: the placement and behavior of the search field are similar between the two platforms, and if the app exists on both, keep the experience consistent. Place the field at the trailing edge of the toolbar for many common uses, especially apps with split views that search across multiple columns of information (Mail, Notes, Voice Memos); this position makes good use of space because it allows navigating results while keeping the selection visible in the detail view. Include search at the top of the sidebar when it filters content or navigation there (example: Settings, which filters the sidebar and exposes sections across multiple levels). Include search as an item in the sidebar or tab bar when you want a dedicated area for discovery, useful when the search comes with rich suggestions, categories or content that needs more space (examples: Music, TV). In a dedicated search area, consider focusing the field automatically when navigating to the area, except on iPad when only the virtual keyboard is available, in which case it's better to leave the field unfocused so as not to unexpectedly cover the view with the keyboard. Take window resizing into account: on iPad the field resizes fluidly as on the Mac, but in compact views it's important to keep search available wherever it's most useful contextually (example: Notes and Mail position the search above the content list column when they resize to a compact view).
- tvOS: the search screen is a specialized keyboard screen that helps enter search text, displaying results below the keyboard in a fully customizable view. Providing suggestions is important because, on tvOS, people typically don't want to type much; popular and context-specific suggestions, including recent searches when available, improve the experience.
- watchOS: when the search field is tapped, the system displays a text entry control that covers the entire screen; the app only returns to the search field after the person taps Cancel or Search.

Links to other articles: Searching, Token fields (for the related component on macOS).

<!-- visual:search-fields -->
### What the illustrations show
Basis: 3 illustration sheets viewed (hig-img_search-fields, sheets 0001 to 0003), codes checked; no video.
- The opening diagrams the search field with placeholder, a text cursor at the leading edge and a microphone icon at the trailing edge, with width and height measurement arrows and dotted lines delimiting the text area; it is the only dimension annotation on the page (img 0983).
- In iPhone Mail, the two-segment scope bar sits above the filled-in field, and right below it a list of token-shaped suggestions (icon, label in gray and term in black), with the keyboard open; callouts with a line and text name the scope bar and the tokens (img 0984).
- Search as a tab bar tab is shown in a pair: first as the fifth item within the same rounded grouping, with no distinction from the other tabs; then as a separate circular button, outside the group, at the trailing edge of the screen (img 0985, img 0986).
- In the iPhone's bottom toolbar, the search field occupies the center of a floating bar, between a filter button on the left and a compose button on the right (img 0987).
- In the iPhone's top toolbar, search becomes a magnifying glass button grouped with the more-options button on the right, with the add button separate from that group and the back button at the leading edge (img 0988).
- On iPad, the field sits at the trailing edge of the top toolbar, with a suggestions menu right below and the first suggestion highlighted in gray (img 0989).
- On macOS, the filled-in field gets a clear button, and the suggestions below carry a magnifying glass icon, with the first one highlighted in orange-yellow (img 0990).
- In the iPad's sidebar, the search field with a microphone sits right below the header and above the list of items with thumbnails (img 0991).
- In an iPad top tab bar, search enters as a dedicated magnifying glass item, highlighted in blue, at the right edge of the same tab bar (img 0992).
- On tvOS, the search screen has a dark background, a field at the top, a horizontal alphabetic keyboard with the focused key in white, a row of five suggestion pills right below and, further down, a grid of results in cards with a circular or square image, a first line in bold and a secondary second line (img 0993).
- Search as a tab is compared in an almost identical pair that only changes the position of the search tab, and search in the toolbar is compared between the bottom and top bars; the page does not use right-or-wrong badges (img 0985 and img 0986; img 0987 and img 0988).
Recorded divergences: in img 0993 it was not possible to identify a scope bar as a separate control; the row of suggestions and the keyboard occupy the space where the official text describes the scope bar.
<!-- /visual:search-fields -->

## Sidebars (slug: sidebars)

What it governs: the sidebar appears at the leading edge of a view and allows navigating between areas of the app or top-level content collections, such as folders and playlists.

Why: sidebars require a good deal of vertical and horizontal space; when space is limited or you want to dedicate more screen to other information or functionality, a more compact control like the tab bar can offer better navigation. For many apps there's no need to choose between tab bar or sidebar, since there is a tab bar style that offers both.

Do and avoid:
- Extend visually rich content underneath the sidebar. On iOS, iPadOS and macOS, sidebars can float over the content in the Liquid Glass layer; to reinforce the separation, you can extend the content under the sidebar by letting it scroll horizontally or by applying a background extension effect, which mirrors the adjacent content to give the impression of stretching it under the sidebar.
- When possible, let the person customize the sidebar's content, since they navigate to the app's most important areas, and the person can decide which areas those are and in what order they appear.
- Group the hierarchy with disclosure controls if the app has a lot of content, to keep the sidebar's vertical space manageable.
- Consider using familiar symbols (SF Symbols) to represent items in the sidebar; if you need a custom icon, prefer creating a custom symbol instead of using a bitmap image.
- Consider allowing the sidebar to be hidden, using the platform-specific interactions people already know (for example, an edge swipe gesture on iPadOS, a show/hide button or View menu commands on macOS); on visionOS, the window generally expands to accommodate the sidebar, so it is rarely necessary to hide it. Avoid hiding the sidebar by default, so it remains discoverable.
- In general, show at most two levels of hierarchy in the sidebar; when the data hierarchy is deeper than two levels, consider a split view interface with a content list between the sidebar items and the detail view.
- If you need to include two levels of hierarchy in the sidebar, use succinct, descriptive labels to title each group, omitting unnecessary words.
- Make sure the sidebar icon colors serve a clear purpose. By default, icons use the app accent color; on macOS, the person can change the system's accent color, and expects all sidebar icons to reflect that choice. Fixed colors, used sparingly, can clarify an icon's meaning or draw attention to it (example: the VIP icon in Mail uses yellow to stand out from the others).

Exact specifications: the text does not give any pt, px or ms numbers; the only quantification is qualitative ("at most two levels of hierarchy").

Platform differences:
- No additional considerations for tvOS; not supported on watchOS.
- iOS, iPadOS: when using the sidebarAdaptable tab view style to present a sidebar, you can choose to display a sidebar or a tab bar when the app opens; both variations include a button to switch between them. This style also adapts its appearance according to the platform and automatically responds to rotation and window resizing. To display only a sidebar, with no conversion, use NavigationSplitView (to present the sidebar in the primary pane of a split view) or UISplitViewController. Consider using a tab bar first, since it offers more space to highlight content and flexibility to navigate between the main areas; if you need to expose more areas than fit in the tab bar, the tab bar's sidebar-convertible appearance can give access to less frequently used content. If you are not using SwiftUI to create the sidebar, you can use the UICollectionLayoutListConfiguration.Appearance.sidebar appearance of a collection view list layout.
- macOS: the sidebar's row height, text and glyph size depend on the overall size, which can be small, medium or large; the size can be set programmatically, but the person can also change it by selecting a different sidebar icon size in general settings. Consider hiding and revealing the sidebar automatically when the container window is resized (example: shrinking the Mail viewer window can automatically collapse the sidebar to give more space to the message content). Avoid placing critical information or actions at the bottom of the sidebar, since people often reposition the window in a way that hides the bottom edge.
- visionOS: if the app's hierarchy is deep, consider using a sidebar inside a tab bar tab, where the sidebar can support secondary navigation within the tab; in that case, you need to prevent selections in the sidebar from changing which tab is open.

Links to other articles: Split views, Tab bars, Layout.

<!-- visual:sidebars -->
### What the illustrations show
Basis: 2 of 2 illustration sheets viewed, all codes checked; the page has no video.
- The construction illustration draws the top of a sidebar as a component: a section header with a collapse chevron, a button to toggle the sidebar in the top right corner, and three item rows with a folder icon on the left, a label in the middle and a star on the right (img 1047).
- Over this illustration, vertical dashed guide lines align the folder icons and the star icons across the three rows, and a vertical two-headed arrow on the right annotates the height or spacing of an item row; the alignment guides and the item-spacing measurement are what the image adds (img 1047).
- The first item appears highlighted in solid red, indicating selection, in an illustration entirely in gradient tones of red and pink (img 1047).
- Incorrect use, marked with a gray X: on an iPad, the flower image at the top of the content area stops exactly at the sidebar's edge, with no transition at all (img 1048 with img 1049).
- Correct use, marked with a green check: the same screen, with the same items, title and text, but the image continues blurred and mirrored behind the sidebar items all the way to the window's edge; the only difference between the pair is in the area behind the sidebar, which shows the background extension effect as blurred continuity, not a cutoff (img 1050 with img 1051).
- The iPad sidebar in this pair carries the collapse-sidebar icon, the back arrow and three items, each with an icon (img 1048, img 1050).
- On visionOS, the Music app uses a translucent glass panel over the blurred environment, with a narrow strip of icons only on the left, then the sidebar with the "Library" header and its items, and below it an expandable "Playlists" group with an arrow and subitems, of which the selected one appears highlighted (img 1052).
- Next to this sidebar, a secondary panel carries a playlists header, a playlist count, its own search field and a grid of playlist thumbnails (img 1052).
Recorded divergences: the notes record that img 1047 adds alignment guides and a spacing measurement that the official description does not detail, and that img 1052 shows a narrow strip of icons only to the left of the sidebar that the official description does not mention.
<!-- /visual:sidebars -->

## Tab bars (slug: tab-bars)

What it governs: the tab bar allows navigating between an app's top-level sections, helping people understand the different types of information or functionality the app offers and quickly switch between sections while preserving each one's navigation state.

Why: the tab bar exists to represent the app's hierarchy in a stable and predictable way; it should not be confused with an actions mechanism, and its visual consistency (always visible, buttons never disabled or hidden) is what ensures the person never loses track of where they are in the app.

Do and avoid:
- Use a tab bar to support navigation, not to provide actions; if you need controls that act on elements of the current view, use toolbars.
- Make sure the tab bar stays visible when the person navigates between sections, since hiding it makes the person forget which area of the app they are in; the exception is when a modal view covers the tab bar, since a modal is temporary and self-contained.
- Use the appropriate number of tabs needed to help with navigation; weigh the complexity of additional tabs against the need for frequent access to each section, since it is generally easier to navigate between fewer tabs. Where available, consider a sidebar or a tab bar that adapts to a sidebar as an alternative for apps with a complex information structure.
- Avoid tabs in overflow: depending on the device's size and orientation, the number of visible tabs can be smaller than the total; if horizontal space limits the number of visible tabs, the final tab becomes a More tab on iOS and iPadOS, revealing the remaining items in a separate list, which makes it harder to access and perceive the hidden content, so limit the scenarios where this happens.
- Do not disable or hide tab bar buttons, even when the content is unavailable, since this makes the interface unstable and unpredictable; if a section is empty, explain why the content is unavailable.
- Include tab labels to help with navigation, using single words whenever possible.
- Consider using SF Symbols for familiar, scalable tab bar icons, which automatically adapt to different contexts (the tab bar can be regular or compact depending on device and orientation); in compact views the icons appear above the labels, in regular views they appear side by side; prefer filled symbols or icons for consistency with the platform.
- Use a badge (a red oval with white text, a number or an exclamation point) to indicate critical information available in a tab; reserve badges for critical information so as not to dilute their impact and meaning.
- Avoid applying a similar color between the tab labels and the content layer's backgrounds; if the app already has colorful, vibrant content in the content layer, prefer a monochromatic appearance for tab bars, or choose an accent color with enough visual differentiation.

Exact specifications: on tvOS, the tab bar height is 68 points, and its top edge sits 46 points from the top of the screen; neither value can be changed. For apps with a customizable tab bar on iPadOS, if the person can select their own tabs, aim for a default list of five or fewer to preserve continuity between compact and regular view sizes.

Platform differences:
- No additional considerations for macOS; not supported on watchOS.
- iOS: the tab bar floats over the content at the bottom of the screen, with its items over a Liquid Glass background that lets the content underneath show through. For tab bars with an attached accessory, like the MiniPlayer in Music, you can choose to minimize the tab bar and move the accessory to sit inline with it when the person scrolls down; the person exits the minimized state by tapping a tab or scrolling to the top of the view. The tab bar can include a dedicated search tab at the trailing edge.
- iPadOS: the system displays the tab bar near the top of the screen. You can choose to have the tab bar appear as a fixed element, or with a button that converts it into a sidebar. To present a sidebar without the option to convert to a tab bar, use a navigation split view instead of a tab view. Prefer a tab bar for navigation, since it gives access to the most-used sections; if the app is more complex, you can offer the option to convert the tab bar into a sidebar to access a broader set of navigation options. You can let the person customize the tab bar, selecting frequently used items to add them, or removing the less frequently used ones (example: in Music, the person can choose a favorite playlist to display in the tab bar).
- tvOS: the tab bar is highly customizable (you can specify the tab bar's tint, color or background image; choose a font for the items, including a different font for the selected item; specify tints for selected and unselected items; add button icons such as settings and search). By default the tab bar is translucent, and only the selected tab is opaque; when the person uses the remote to focus on the tab bar, the selected tab gains a drop shadow that emphasizes its selected state. If there are more items than fit in the tab bar, the system truncates the rightmost item by applying a fade effect that starts from the right side of the tab bar; if there are enough items to cause scrolling, the system also applies a truncating fade effect from the left side. By default, the person can scroll the tab bar off the screen when the current tab contains a single main view (examples: the Watch Now, Movies, TV Show, Sports and Kids tabs of the TV app); the exception is when the screen contains a split view, such as the Library tab of the TV app or a Settings screen, in which case the tab bar stays fixed at the top of the view while the person scrolls the content of the split view's primary and secondary panes. Regardless of a tab's content, focus always returns to the tab bar at the top of the page when the person presses Menu on the remote. In live-streaming apps, organize the tabs consistently in the order: live content, Cloud DVR or other recorded content, other content.
- visionOS: the tab bar is always vertical, floating in a fixed position relative to the window's leading edge. When the person looks at the tab bar, it expands automatically; to open a specific tab, the person looks at the tab and taps. While expanded, the tab bar can temporarily obscure the content behind it. Provide a symbol and a text label for each tab; the tab's symbol is always visible in the tab bar, and when the person looks at the tab bar the system also reveals the labels, which should be short for quick reading. If it makes sense in the app, consider using a sidebar inside a tab when the hierarchy is deep, supporting secondary navigation within the tab; in that case you need to prevent selections in the sidebar from changing which tab is open.

Links to other articles: Tab views, Toolbars, Sidebars, Materials, Search fields, Notifications, Live-viewing apps, Liquid Glass color.

<!-- visual:tab-bars -->
### What the illustrations show
Basis: 3 of 3 illustration sheets and 2 of 2 video sheets (hig-vid_tab-bars__059, frames q001 to q011) viewed, all codes checked.
- The opening anatomy groups four tabs, each with icon over label, inside a pill-shaped container, and leaves search as a separate circular button, icon only; horizontal dimension lines mark the distance at the left edge and the gap between the pill and the search button, and a vertical dimension line sits above the third and fourth tabs (img 1108).
- The selected state in this anatomy is a white background with a black icon, while the unselected tabs have a dark red icon on a transparent background (img 1108).
- On iPhone, the same five-tab bar changes only the relationship between icon and label: in landscape the icon sits to the left of the text on the same line, in portrait the icon is stacked above the label (img 1109).
- The anatomy diagram names the two parts of a tab with callouts "Icon" and "Label"; the active tab has the icon in blue and the rest in black, with search set apart (img 1110).
- The badge appears as a small red circle attached to the upper right corner of the icon, on two of the four tabs, with no visible number in this instance (img 1111).
- On iOS with an accessory, the expanded state shows the "Not Playing" accessory as a rounded rectangle above the four-tab bar; in the minimized state the bar shrinks to a circular button with only the active tab on the left, the accessory becomes an elongated pill in the center and search sits in an isolated circular button on the right, all on a single line (img 1112, img 1113).
- On iPadOS, the horizontal bar near the top has a sidebar button, items with the active one in red and search on the right; converted, it becomes a vertical sidebar with the same destinations plus "Library" and "Playlists" sections, while the content screen behind it remains identical, meaning only the navigation container changes (img 1114, img 1115).
- On visionOS, the collapsed bar is a translucent vertical pill of frosted glass with icons only, with a lighter background circle on the highlighted icon; expanded, it becomes wider and each row gains the label next to the icon inside an individual pill, with slightly different backgrounds between the rows suggesting distinct states, such as hover or selection (img 1116, img 1117).
- In the video, the photos app bar starts collapsed with six icons and no text (q001, q002), expands between q002 and q003 (from 0.5 s to 1.0 s) showing the full labels with the "Memories" row in a highlighted pill, and stays stable in that state until q009 (5.5 s) (sheet 0001).
- The bar returns to the collapsed state at q010 (6.0 s) and stays that way at q011; in the sampled frames no intermediate state appears between collapsed and expanded, the change goes from one fixed frame straight to the next (sheet 0002).
- The icon that will be highlighted on expansion already shows a slight lighter background circle in the collapsed state, before and after the expansion (q001, q002, q010).
Recorded divergences: the notes record that the video shows the slight background highlight on the "Memories" icon also in the collapsed state (q001, q002, q010), something the official description does not mention.
<!-- /visual:tab-bars -->

## Token fields (slug: token-fields)

What it governs: a token field is a type of text field that converts text into tokens that are easy to select and manipulate, like in the address fields of the Mail compose window.

Why: the token gives visual treatment to a term (such as a recipient's name), turning it into a manipulable object (selectable, draggable, editable) instead of just loose text, and the contextual menu on a token exists to add information or editing options without leaving the typing flow.

Do and avoid:
- Add value with a context menu, since people tend to benefit from additional options or information about a token (example: in Mail, the contextual menu of a recipient token has commands to edit the name, mark as VIP and view the contact card).
- Consider providing additional ways to convert text into tokens; by default, text becomes a token when the person types a comma, and it is possible to specify additional shortcuts, such as pressing Return.
- Consider customizing the delay the system uses before showing suggested tokens; by default the suggestions appear immediately, but suggestions that are too fast can distract whoever is typing, so consider adjusting the delay to a comfortable level.

Exact specifications: the text does not give numbers, measurements or delay values; it only mentions that by default the suggestions appear immediately and that the comma is the default conversion trigger.

Platform differences: not supported on iOS, iPadOS, tvOS, visionOS and watchOS. It is a macOS-exclusive component (AppKit, NSTokenField).

Links to other articles: Text fields, Search fields, Context menus.

<!-- visual:token-fields -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked; the page has no video.
- The conceptual illustration places in the same field, between the magnifying glass on the left and the circular clear button on the right, a light pink pill token with a person icon and name, followed by loose text not yet converted; the contrast between formatted object and free text is what the image teaches (img 1160).
- In the Mail compose window on the Mac, the "To:" field shows two recipients already converted into light blue pills and a third name still being typed as plain text, with a suggestions dropdown right below, two address options and the first one highlighted in blue (img 1161).
- In the next moment, the third name has already become a full pill and appears selected, opening a contextual menu of its own for the token (img 1162).
- This menu organizes the options into blocks separated by dividers: the current address with a checkmark and actions to edit, remove and copy; then add to VIPs and block sender; then remove from the previous recipients list and add to contacts; and finally search by name (img 1162).
- In the real captures the tokens are rounded-corner rectangular pills in light blue, visually distinct from the field's normal text, the same pill shape as the conceptual illustration (img 1160, img 1161, img 1162).
<!-- /visual:token-fields -->

## What this group reveals about the Apple way

1. macOS-exclusive components (path-controls, token-fields) show that Apple accepts fragmenting platform parity when the interaction pattern (dragging items, inline editing, file system conventions) only makes sense in the Mac's windows-and-mouse model; both are "Not supported" on all other platforms.
2. Apple prefers adapting a single component to multiple contexts instead of multiplying components: the tab bar that converts into a sidebar (sidebarAdaptable, tabBarOnly) appears in both sidebars and tab-bars as the recommended solution for apps that need compact navigation as well as rich navigation, avoiding forcing a binary choice.
3. Search is treated as a problem of contextual placement, not a single component: search-fields devotes most of the article to where to place the field (tab, toolbar, inline, sidebar) according to the app's layout, instead of prescribing a single correct place.
4. Liquid Glass is cited as a visual layer shared between sidebars and tab-bars (both "float" over the content with a translucent background), revealing a unified material language across distinct navigation components.
5. Apple is consistent in never hiding or disabling primary navigation controls: tab-bars prohibits hiding or disabling tab buttons even with unavailable content, and sidebars recommends not hiding the sidebar by default, reflecting a larger principle of spatial predictability in navigation.
6. User customization is valued, but with limits of continuity: sidebars suggests allowing the sidebar content to be customized, and tab-bars allows customizing the tabs but recommends a default of five or fewer tabs to maintain visual continuity across screen sizes.
7. Color as a functional, not decorative, signal: sidebars advises icons to respect the app accent color (or the system color chosen on macOS) and to reserve fixed color only to highlight specific items (the yellow VIP example in Mail); tab-bars asks to avoid a label color similar to the content background. Both treat color as a vehicle of meaning that the person controls, not as an aesthetic choice isolated from the app.
8. Shallow hierarchy is the preferred default: sidebars recommends at most two visible levels before introducing an additional split view, reinforcing Apple's preference for flattened navigation over deep trees.
9. tvOS receives separate treatment across almost the whole group (search-fields, tab-bars), with its own mechanics of remote-control focus, fade truncation and tab bar pinning in split views, showing that the Apple TV's "point and focus" interaction requires navigation rules structurally different from those of touch or click.
10. visionOS treats the sidebar and the tab bar as elements that respond to gaze (expansion on gaze, tap to confirm) and avoids hiding the sidebar by default because the window adapts to the space, an interaction pattern that has no direct equivalent in the other platforms cited in the group.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/path-controls.md: 26 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/search-fields.md: 101 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sidebars.md: 64 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/tab-bars.md: 89 lines read, to the end: yes.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/token-fields.md: 30 lines read, to the end: yes.
