# Components / Menus and actions

Index group 7 of the hig list in groups.json. Covers the components Apple uses to expose commands and actions: activity views, buttons, context menus, dock menus, edit menus, home screen quick actions, menus (the general article), ornaments, pop up buttons, pull down buttons, the menu bar and toolbars.

## Activity views (slug: activity-views)

An activity view, also called a share sheet, presents a range of tasks the person can perform in the current context: sharing (messages, social networks) and actions like Copy and Print, plus quick access to frequently used apps.

Why: sharing and the actions related to a piece of content are frequent but heterogeneous tasks (they can involve third-party apps, extensions, system services). Centralizing everything in a single, familiar entry point (the Share button) keeps each app from reinventing its own version of "sharing" and lets the system list, alongside the app's actions, the actions of other apps and of the system, keeping things predictable for whoever uses it.

Do and avoid:
- Avoid duplicating actions that already exist in the activity view, such as your own Print; if you need something similar but with different behavior, give it a specific title (e.g. "Print Transaction") instead of reusing the generic name.
- Consider using an SF Symbols symbol to represent the custom activity; if you need your own interface icon, center it in an area of approximately 70x70 pixels.
- Write a short, descriptive title for each custom action, preferably a verb or a brief verb phrase; avoid including the company or product name in the action title (unlike the sharing activity, which displays the company name below the icon).
- Make sure the displayed activities make sense in the current context; although it is not possible to reorder the tasks provided by the system, it is possible to exclude the ones that do not apply to the app (for example, excluding Print if printing does not make sense).
- Use the Share button to open the activity view; do not create an alternative path to the same function, since people already expect to find it there.
- For share extensions, prefer the composition view provided by the system, which guarantees a consistent sharing experience; for action extensions, include the app name and, if you need to present your own interface, use elements that resemble the app's interface.
- Simplify and limit the interaction: a sharing extension can, for example, post an image to a social network with a single tap or click.
- Avoid placing a modal view above the extension; the system already displays the extension inside a modal view by default, and alerts above it should be the exception, not the rule.
- If necessary, provide an image that communicates the extension's purpose: the share extension automatically uses the app icon, and the action extension should prefer a symbol or interface icon that clearly identifies the task.
- Use the main app to indicate the progress of a long operation, since the activity view closes as soon as the person completes the task in the extension; if the task takes a while, continue in the background and provide a way to check status in the main app. A notification can warn about a problem, but should not be used only to notify that the task finished.

Exact specifications: custom interface icon centered in an area of approximately 70x70 pixels. No other numerical measurement appears in the text.

Platform differences: supported, with no additional notes, on iOS, iPadOS and visionOS. Not supported on macOS, tvOS or watchOS, but on macOS it is possible to create share and action extensions even without the system's activity view (accessed through a Share button in the toolbar or through Share in a context menu, or through a quick action in a Finder window).

Links to other articles: Sheets, Popovers.

<!-- visual:activity-views -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_activity-views, sheet 0001), codes checked; no video.
- The opening stylizes the share sheet inside the outline of an iPhone: a header with a square on the left representing the shared item and a title with subtitle, followed by two rows of circular icons (img 0036).
- In the stylized version the real app and contact icons become generic monochrome circles in red, and only the text labels keep the real names of apps and system actions (img 0036).
- On the real Notes screen, before any tap, the Share button sits in the top right corner grouped with the more options button (img 0037).
- The pair img 0037 and img 0038 keeps the same note in the background and changes only the presence of the activity view, isolating the transition of before and after tapping Share.
- The real activity view is an overlaid white card that covers the lower part of the content, with a header showing the icon and title of the shared document (img 0038).
- The content of the real card is organized into three distinct rows: frequent contacts as colored avatars with initials, sharing apps with their colored icons, and local actions on the document ending in "More" (img 0038).
- The stylization has only two rows, with apps in the first and system actions in the second, while the real capture adds its own row of contacts and separates contacts, apps and actions into three bands (img 0036 compared to img 0038).
<!-- /visual:activity-views -->

## Buttons (slug: buttons)

A button initiates an instant action; it combines three attributes (style, content and role) to communicate its function clearly.

Why: a button only works if it is recognizable and easy to understand at first glance. Separating style (visual appearance), content (symbol, text or both) and role (the semantic meaning, which can affect appearance) gives Apple a consistent vocabulary for prioritizing actions on any screen, and lets system styles already come with interaction states, accessibility support and appearance adaptation ready, without each app needing to rebuild it.

Do and avoid:
- Give enough space around the button so it can be visually distinguished from the surrounding content and selected easily, whatever the input method.
- Always include a press state in a custom button; without it the button seems unresponsive, and the person is left unsure whether the tap was registered.
- Use a prominent visual style for the most likely action of a view, applying the app's accent color; keep at most one or two prominent buttons per view, because too much prominence increases cognitive load.
- Use style, not size, to distinguish the preferred option among several options; buttons of the same size signal that they form a coherent set of choices, while different sizes make the interface confusing.
- Avoid applying a similar color between the button label and the background of the content layer; if the content is already colorful, prefer the default monochrome appearance of button labels.
- Prefer associating familiar actions with familiar icons (e.g. the square.and.arrow.up symbol for sharing); use text when a short label communicates better than an icon, with title-style capitalization and, preferably, starting with a verb.
- A button's role can be Normal (no specific meaning), Primary (the button the person will most likely choose, uses the app's accent color and responds to the Return key in temporary views), Cancel (cancels the current action) or Destructive (can destroy data, uses the system's red color).
- Never assign the primary role to a button that performs a destructive action, even if it is the most likely choice, because the visual prominence of primary makes people choose without reading.

Exact specifications:
- Minimum hit region of 44x44 pt for any button; on visionOS, 60x60 pt.
- Padding of approximately 10 pixels between the image edges and the button edges, in image buttons on macOS.
- On visionOS, standard button sizes: Mini 28 pt, Small 32 pt, Regular 44 pt, Large 52 pt, Extra large 64 pt (applicable to circular, capsule with text, capsule with text and icon, and rounded rectangle formats, each with its own availability per size).
- On visionOS, button centers must be at least 60 pts apart from each other; if the buttons are 60 pts or larger, add 4 pts of padding around them so the hover effect does not overlap.

Platform differences:
- iOS, iPadOS: a button can display an activity indicator next to the original label or an alternative label (e.g. "Checkout" becomes "Checking out…") when the action does not complete instantly, hiding the button's image if there is one.
- macOS: push buttons are the default type (they can be a default button and receive tint); flexible-height push buttons serve tall or variable-height content, keeping the same corner radius and padding as standard buttons; a push button that opens another window, view or app receives an ellipsis in the title; systems with Magic Trackpad can support spring loading (force click to activate by dragging selected items over the button). Square buttons (also called gradient buttons) contain symbols or icons, not text, sit close to the associated view and should not be used in toolbars or status bars. Help buttons are circular, contain a question mark, and should be limited to one per window; recommended positions: in a dialog with dismiss buttons, in the opposite bottom corner and vertically aligned with them; in a dialog without dismiss buttons or in a settings window/panel, in the bottom left or right corner. Image buttons should sit in a view, not in the window frame, and the label, if any, sits below the image.
- visionOS: buttons have a visible background and a feedback sound on interaction; three standard formats (circle for icon only, roundedRectangle or capsule for text only, capsule for icon and text); four visual interaction states; do not support a custom hover effect; can display a tooltip when looked at for a moment (less necessary when they already have text); Apple recommends a background with thin material when the button appears over glass and using the visionOS material when the button floats in space; avoid a white background with black text or icon, reserved for the toggled state; prefer capsule in a horizontal row and rounded-rectangle in a vertical stack.
- watchOS: all inline buttons use the capsule format and gain a material effect when placed next to content; the toolbar positions buttons in the corners, with the system automatically moving the time and title to accommodate them and applying Liquid Glass appearance to the toolbar buttons; full-width buttons are preferred for primary actions; if two buttons share the same horizontal space, use the same height for both.
- tvOS: no additional considerations beyond the general text.

Links to other articles: Pop-up buttons, Pull-down buttons, Toggles, Segmented controls, Location button, Liquid Glass color.

<!-- visual:buttons -->
### What the illustrations show
Basis: 3 illustration sheets (hig-img_buttons) and 2 videos of one sheet each (hig-vid_buttons__006 and hig-vid_buttons__007) viewed, codes checked.
- The opening annotates with bidirectional red arrows, without numbers, the width of a capsule button and the horizontal spacing between two identical buttons side by side (img 0189).
- In the same iOS alert, three stacked buttons show the hierarchy by role: primary with solid blue background and white text, destructive with light gray background and red text, secondary with light gray background and black text; the destructive's red stays only in the text, not in the background (img 0190).
- The loading state is a before and after pair on the same component: the gray capsule with "Checkout" in blue becomes "Checking out" with a blue spinner at the leading edge, keeping shape and background color, with no perceptible change in size (img 0191, img 0192).
- The four visionOS button states use the same grayish beige circular button with a central icon: at rest and on hover the inner circle is light translucent with a white icon; selected inverts the contrast, with a solid white inner circle and a black outline icon; unavailable appears dimmed (img 0193, img 0194, img 0195, img 0196).
- The visionOS section carries an isolated check in neutral gray on a white background, instead of the green correctness seal used on other pages (img 0197).
- On watchOS, inline buttons are stacked capsules at the base of the screen, with solid color or gradient that contrasts with the screen's colored background to keep it legible (img 0198).
- The watchOS toolbar places circular buttons in the upper corners (close and more options) and three controls at the base, with the central play larger and lighter than the side ones (img 0199).
- In video 006, four circular buttons in a translucent top bar stay identical from q001 to q005; in q006 the more options button lightens the background, and in q007 and q008 it becomes solid white while the neighbors stay gray (hig-vid_buttons__006, sheet 0001).
- The menu triggered by that button appears anchored right below it, partially cut off in q007 and whole in q008, with a bluish translucent background that appears to come from the content behind it (hig-vid_buttons__006, sheet 0001, q007 and q008).
- In video 007, the share icon button appears alone in q001 and q002; the "Share" tooltip emerges with a delay below it in q003, still smaller, and only in q004 does it reach final size and opacity (hig-vid_buttons__007, sheet 0001).
Recorded divergences: the difference in tone between rest and hover on visionOS is not clear in the captures; the official caption speaks of a medium dark background on hover (img 0193, img 0194). The videos add to the official description the progressive contrast of the selected button and the gradual growth of the menu and tooltip.
<!-- /visual:buttons -->

## Context menus (slug: context-menus)

A context menu gives access to functionality directly related to an item, without overloading the main interface; it stays hidden until revealed by a specific action on a selected item.

Why: a context menu does not exist for advanced or rare functions, but to make the most likely commands in the current context immediately accessible, without occupying permanent space on the screen. Since it stays hidden by default, Apple requires that everything that appears in it also be accessible through the main interface, avoiding it becoming the only path to functionality the person might never discover.

Do and avoid:
- Prioritize relevance in choosing items; it is not the place for advanced or rarely used commands.
- Keep the menu short; a long context menu is hard to scan and scroll.
- Support context menus consistently throughout the app; offering them only in some places confuses people about where the function exists.
- Always make the same context menu items available in the main interface too (e.g. in the toolbar).
- If you need submenus to manage complexity, limit it to a single level, and give it an intuitive title that helps predict the content without opening it.
- Hide unavailable items instead of dimming them (dimmed); the exception on macOS is Cut, Copy and Paste, which can appear unavailable even if they do not apply to the context.
- Position the most used items where the person will likely look first, considering that the menu can open above or below the selected content.
- Show keyboard shortcuts in the app's main menus, not in context menus, because they are already a shortcut to task-specific commands.
- Follow separator best practices to group items, avoiding more than approximately three groups in a context menu.
- In iOS, iPadOS and visionOS, warn about items that can destroy data: list them at the end of the menu and identify them as destructive (the system can display them in red).
- A context menu rarely displays a title; include a title only if it clarifies the effect of the menu (e.g. showing how many messages were selected).
- Represent actions with familiar icons, the same ones used elsewhere in the system for Copy, Share, Delete etc.

Exact specifications: no explicit number is given in the text (the guidance of "about three groups" and "one submenu level" is qualitative).

Platform differences:
- iOS, iPadOS: offer a context menu or edit menu for an item, never both at the same time, because it would confuse the person and make it harder for the system to detect intent. In iPadOS, consider a context menu to create a new object (e.g. Files creates a new folder in an area between existing files and folders). In iOS and iPadOS, the context menu can display a preview of the content near the list of commands, and the person can tap the preview to open it or drag it; the preview should have the clipping path adjusted to the shape of the image so the outlines do not appear to change during the animation.
- macOS: the context menu is sometimes called a "contextual menu".
- visionOS: consider a context menu instead of a panel or inspector window to reduce the number of open windows; avoid letting the menu's height exceed the window's height, since a menu that is too tall can obscure system components above and below the window (window management controls and the Share menu).
- No additional considerations on tvOS; not supported on watchOS.

Links to other articles: Menus, Edit menus, Pop-up buttons, Pull-down buttons.

<!-- visual:context-menus -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_context-menus, sheet 0001), codes checked; no video.
- The contextual menu appears anchored to the click point, right below and to the right of the cursor, not centered on the screen (img 0398).
- The list is vertical, with six items, and mixes items with a geometric icon at the leading edge and items without an icon in the same menu (img 0398).
- Items that open a submenu are marked only by a right-pointing arrow at the trailing edge, with no other indicator, and appear together at the end of the list (img 0398).
- The highlighted item, by hover or focus, is signaled by a more saturated background from the same palette as the menu, not by a different accent color (img 0398).
- The item text is dark wine over the menu's light pink background (img 0398).
<!-- /visual:context-menus -->

## Dock menus (slug: dock-menus)

On the Mac, a secondary click on the app or game icon in the Dock reveals a Dock menu, which presents items provided by the system and custom items.

Why: the Dock menu exists as a quick access point to useful commands even when the app is not in the foreground or has no open windows, without depending on the app being visible on the screen.

Do and avoid:
- Label Dock menu items succinctly and organize them logically, as in any menu.
- Make the Dock menu's custom items available in other places too (such as menu bar menus or in the interface), because not everyone uses the Dock menu.
- Prefer high-value custom items, such as listing all open or recent windows, and consider useful actions when the app is not in the foreground or has no open windows.

Exact specifications: none.

Platform differences: exclusive to macOS; not supported on iOS, iPadOS, tvOS, visionOS or watchOS. On iOS and iPadOS there is an equivalent called Home Screen quick actions, revealed with a touch and hold on the app icon.

Links to other articles: Menus, Home Screen quick actions.

<!-- visual:dock-menus -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_dock-menus, sheet 0001), codes checked; no video.
- The Dock menu appears as a balloon with a triangular tip pointing back to the source icon, positioned above it, which visually ties the menu to the app (img 0469).
- In the stylized Dock, the icons are empty squares and three of them have a small red dot below marking an open app (img 0469).
- The four items are divided into two groups by a dividing line, two items above and two below, with "Show Recents" and "Open" being the second group (img 0469).
- Items that open a submenu carry a chevron to the right, and direct action items have no chevron, in both groups (img 0469).
<!-- /visual:dock-menus -->

## Edit menus (slug: edit-menus)

An edit menu allows changing the selected content in the current view, in addition to offering related commands such as Copy, Select, Translate and Look Up.

Why: being the standard editing mechanism for any selectable content (text, images, files, objects such as contact cards, graphics or locations), the edit menu needs to behave predictably and be triggered by the same gestures people already know on each platform, so editing feels native instead of reinvented by each app.

Do and avoid:
- Prefer the edit menu provided by the system; creating a custom menu with the same commands is redundant and confusing.
- Let the person reveal the edit menu through already familiar interactions (touch and hold on the touchscreen, pinch and hold on visionOS, secondary click with a connected trackpad or keyboard).
- Offer only the commands relevant to the current context, removing or dimming the ones that do not apply (e.g. not showing Copy with nothing selected, nor Paste with nothing to paste).
- List custom commands near the equivalent system commands (e.g. formatting commands after the system commands in the format section).
- When it makes sense, allow selecting and copying non-editable text, such as an image's caption.
- Support undo and redo whenever possible, since an edit menu does not require confirmation before acting.
- In general, avoid creating other controls that duplicate the edit menu's functions; that only occupies space that could be used for less obvious actions.
- Differentiate deletion commands when necessary: Delete behaves like pressing the Delete key, while Cut copies the content to the pasteboard before deleting.
- Create short labels for custom commands, using short verbs or verb phrases.

Exact specifications: none.

Platform differences:
- iOS: the edit menu appears in a compact, horizontal list when touching and holding or double-tapping to select content; the person can tap a chevron at the far edge to expand it into a context menu.
- iPadOS: the edit menu's layout changes according to how it is revealed, horizontal and compact with touch interactions, and directly as a context menu when revealed by keyboard or pointing device.
- macOS: editing commands are accessible in a context menu during an editing task and also through the Edit menu in the menu bar.
- visionOS: the person uses the standard gesture to open the edit menu as a horizontal bar, or can open it as a context menu.
- Not supported in tvOS or watchOS, because editing content is rare in these experiences.

Links to other articles: Menus, Context menus, The menu bar, Undo and redo.

<!-- visual:edit-menus -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_edit-menus, sheet 0001), codes checked; no video.
- The edit menu is a rounded horizontal bar with four commands in sequence (cut, copy, paste, delete), separated by thin vertical lines (img 0471).
- The bar ends in a circular button with a chevron pointing right, which indicates more options after the direct actions (img 0471).
- The menu appears above the selected text, and a thin line connects the left end of the bar to the selection's upper-left handle, marking the relationship of origin (img 0471).
- The text selection is built with a slightly highlighted background over the word, a vertical cursor to its right, and two red circular handles at the ends, one above to the left and another below to the right (img 0471).
<!-- /visual:edit-menus -->

## Home Screen quick actions (slug: home-screen-quick-actions)

Home Screen quick actions give the person a way to perform app-specific actions directly from the Home Screen, without opening the app first.

Why: certain high-value actions (searching near the current location, creating a new item, opening a recent conversation) are worth making accessible with a single touch and hold on the icon, saving the step of opening the app and navigating to the function. That is why Apple recommends reserving this space only for genuinely worthwhile tasks.

Do and avoid:
- Create quick actions only for high-value tasks; it is possible to offer up to four.
- Avoid unpredictable changes in quick actions; dynamic actions (based on location, recent activity, time of day, or settings) need to change in a way the person can predict.
- Write a concise title that instantly communicates the result of the action (ex. "Directions Home", "Create New Contact", "New Message"); use a subtitle if you need more context. Do not include the app name or superfluous information in the title or subtitle, keep the text short to avoid truncation, and take localization into account.
- Provide a familiar interface icon for each quick action, preferably from SF Symbols; if designing a custom icon, use the Quick Action Icon Template from Apple Design Resources.
- Do not use emoji in place of an interface symbol or icon, because emoji is colored while the quick action's symbol is monochrome and changes appearance in Dark Mode to maintain contrast.

Exact specifications: limit of four quick actions per app.

Platform differences: no additional considerations in iOS or iPadOS; not supported in macOS, tvOS, visionOS, or watchOS (on macOS the equivalent is the Dock menu).

Links to other articles: Menus, Dock menus.

<!-- visual:home-screen-quick-actions -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_home-screen-quick-actions, sheet 0001), codes checked; no video.
- The quick actions menu is a single, light card, with well-rounded corners, anchored just above the app icon that originated it (img 0543).
- The content is a vertical list of four lines, each with a simple geometric symbol at the leading edge and the label in red to the right (img 0543).
- The other icons in the row are deliberately blurred, while the origin icon appears sharper, transferring the screen's focus to the active menu (img 0543).
Recorded divergences: the official description only talks about menu items coming out of an app icon; the line structure with symbol and label, the rounded card, and the blur of the neighboring icons appear only in the image.
<!-- /visual:home-screen-quick-actions -->

## Menus (slug: menus)

A menu reveals its options when the person interacts with it, functioning as a space-efficient way to present commands; this article establishes the general rules of labeling and organization that apply to all types of menu (pop-up buttons, pull-down buttons, context menus, the menu bar etc.).

Why: menus are ubiquitous, so most people already know how to use them; Apple invests in keeping a consistent vocabulary of labeling, icons, organization, submenus, and toggled items because that is what makes a system menu, or any app's menu, feel familiar even the first time someone opens it.

Do and avoid (Labels):
- Write a label that clearly and concisely describes the item; use a verb or verb phrase for actions (View, Close, Select).
- Use title-style capitalization to stay consistent with the rest of the platform (although a game can have its own style).
- Remove articles (a, an, the in English) from labels to save space, since they rarely increase comprehension.
- Show when an item is unavailable, typically dimmed and unresponsive to interactions; if all items in a menu are unavailable, the menu itself needs to remain accessible.
- Add an ellipsis to the label when the action requires more information before completing.

Do and avoid (Icons):
- Represent common actions consistently, using the system's standard icons for Share, Print, Search etc.
- Use icons with moderation and purpose, only when they help find the item faster or clarify what the selection does; do not display an icon if you cannot find one that represents the item well.
- Apply a uniform visual treatment within the same group: either all items in the group have an icon, or none do.

Do and avoid (Organization):
- List the most important or most frequently used items first, because people tend to scan the menu from top to bottom.
- Group logically related items and use a separator to visually distinguish them.
- Keep related commands in the same group even if they have different importance from each other.
- Pay attention to the menu's length; consider splitting into separate menus or using a submenu if it is too long. The exception is content defined by the person or generated dynamically (like History and Bookmarks in Safari), where a long, scrolling menu is acceptable.

Do and avoid (Submenus):
- Use submenus with moderation, since each one adds complexity and hides the items it contains; consider a submenu when a term appears in more than two items in the same group.
- Limit depth and length: restrict to a single hierarchical level, and if the submenu has more than approximately five items, consider creating a new menu instead.
- Keep a submenu item accessible even when the nested items are unavailable.
- Prefer a submenu over indenting items, because indentation is inconsistent with the system.

Do and avoid (Toggled items):
- Consider a mutable label that describes the current state (ex. an item that toggles between "Show Map" and "Hide Map") instead of two separate items.
- Include a verb if the mutable label is not clear enough on its own (ex. "Turn HDR On" / "Turn HDR Off" instead of just "HDR On" / "HDR Off").
- If necessary, display both action or state items at the same time, instead of a single toggled item.
- Consider using a checkmark to show that an attribute is in effect, and offer an item that removes several toggled attributes at once (ex. "Plain").

Do and avoid (In-game menus): let players navigate the game's menus using the platform's standard interaction method, and make sure the menus remain easy to open and read across all supported platforms, adjusting tap target size and the way content is communicated when necessary.

Exact specifications: in iOS, iPadOS, and visionOS, the menu's small layout shows a row of four items at the top (symbol or icon only, no label); the medium layout shows a row of three items (symbol or icon above a short label); the large layout (default) shows all items in a list. A submenu with more than approximately five items suggests creating a new menu; menus in general, at most about three groups separated by a separator.

Platform differences:
- iOS, iPadOS: three possible layouts (small, medium, large, described above); the medium layout works well for about three important actions (ex. Notes uses Scan, Lock, Pin); the small layout works for closely related actions that appear as a group (ex. Bold, Italic, Underline, Strikethrough), each with a recognizable symbol and no label.
- visionOS: can use the small or large layouts defined for iOS/iPadOS; it is possible to apply a breakthrough effect to keep the menu visible even when other content occludes it; as in macOS, a menu opened in a visionOS window can appear outside the window's bounds. Prefer showing the menu near the content it controls. The subtle effect is the default and blends the presentation with the surrounding content; prominent shows the menu more prominently over the whole scene but can be distracting and cause discomfort; none fully hides the menu behind other 3D content, which can make it harder to access.
- No additional considerations in macOS, tvOS, or watchOS.

Links to other articles: Pop-up buttons, Pull-down buttons, Context menus, The menu bar.

<!-- visual:menus -->
### What the illustrations show
Basis: 3 illustration sheets viewed (hig-img_menus, sheets 0001 to 0003), codes checked; no video.
- The opening shows a cascading menu: three items with keyboard shortcuts aligned to the right, a separator, and a submenu item with an arrow pointing right that opens the secondary list beside it (img 0790).
- Inside the submenu, the active item receives a solid, contrasting red fill, which is the way of signaling hover or momentary selection (img 0790).
- A wrong-and-right pair with the same content, the days of the week: the wrong one puts an arbitrary icon on each day, unrelated to the item, marked with an X in a gray circle (img 0791, img 0792).
- The right one shows the same menu with only left-aligned text, no icon at all, marked with a check in a green circle (img 0793, img 0794).
- The rule of uniform treatment per group appears in a real macOS window menu: the first group has no icons and carries shortcuts on the right; after the separator, the second group has an icon on every item and a submenu arrow on the right; callout lines name each group (img 0795).
- A toggled state is marked only by a checkmark on the item's left margin, in a list with no icons, without duplicating the item for each state (img 0796).
- The contrast between img 0790 and img 0796 visually separates the momentary highlight, in solid color, from the persistent marked state, in a discreet checkmark.
- The three iOS and iPadOS menu layouts are compared with the same set of six actions: in the small one, four actions become just icons in a compact row and the rest stay below as items; in the medium one, three actions become larger buttons with icon and caption and the others follow in a list with icon on the right; in the large one, all six are in a vertical list with text on the left and icon on the right (img 0797).
- In visionOS, the menu is anchored just below the more-options button, which appears selected in solid white, over a real app window (img 0798).
- This visionOS menu combines a row of three icons at the top with a list of items with an icon on the right, divided into two groups by a separator (img 0798).
<!-- /visual:menus -->

## Ornaments (slug: ornaments)

In visionOS, an ornament presents controls and information related to a window without crowding or obscuring the window's content; it floats on a plane parallel to the window and slightly in front of it on the z axis.

Why: windows in visionOS exist in three-dimensional space, so Apple created the ornament as a way to keep frequent controls in a consistent, predictable place relative to the window (following it if it moves, remaining unchanged if the content scrolls) without competing for space inside the content itself.

Do and avoid:
- Consider an ornament to present controls or information frequently needed in a consistent location that doesn't overload the window; because it stays attached to the window, the person always knows where to find it (e.g. Music uses an ornament for the Now Playing controls).
- In general, keep an ornament visible; it can make sense to hide it when the person immerses in the window's content (watching a video, viewing a photo), but in most cases people prefer constant access.
- If you need multiple ornaments, prioritize the window's overall visual balance; consider limiting the total number so as not to increase visual weight, and if you decide to remove an ornament, you can relocate its elements into the main window.
- Keep the ornament's width equal to or narrower than the width of the associated window, because a wider ornament can interfere with a tab bar or other vertical content on the side of the window.
- Consider using borderless buttons in an ornament, since the ornament's default background is already the visionOS material, and the system automatically applies the hover effect when the person looks at the button.
- Use toolbars and tab bars provided by the system instead of creating your own ornament for that, because in visionOS toolbars and tab bars already appear automatically as ornaments.

Exact specifications: none.

Platform differences: exclusive to visionOS; not supported in iOS, iPadOS, macOS, tvOS or watchOS.

Links to other articles: Layout, Toolbars.

<!-- visual:ornaments -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_ornaments, sheet 0001), codes checked; no video.
- The ornament is drawn as a pill-shaped bar, with fully rounded corners, overlaid on the bottom edge of the window, and not inside its body (img 0825).
- Red measurement arrows dimension the ornament as a component with its own dimensions: a double horizontal arrow above it marks the width and a double vertical arrow to the right marks the height (img 0825).
- The pill, white or light pink, contrasts in tone with the coral red window, which has rounded corners at the base (img 0825).
- Below the pill appears a pagination indicator, a filled dot and an elongated bar, suggesting the current page among several (img 0825).
Recorded divergences: the official description suggests a design tool grid in the background, but in the visible area of the image the grid does not appear clearly; only the measurement arrows are visible.
<!-- /visual:ornaments -->

## Pop-up buttons (slug: pop-up-buttons)

A pop-up button displays a menu of mutually exclusive options; after the person chooses an item, the menu closes and the button can update its content to indicate the current selection.

Why: there is a deliberate distinction between "choosing a state among exclusive options" (pop-up button) and "choosing an action" (pull-down button); using the right component communicates in advance whether the interaction changes a value or triggers a command, which helps the person predict the outcome before tapping.

Do and avoid:
- Use a pop-up button to present a simple list of mutually exclusive options or states; use a pull-down button, instead, to offer a list of actions, allow multiple selection or include a submenu.
- Provide a useful default selection; if the person hasn't chosen anything yet, the button shows the specified default item, preferably the one most people are likely to want.
- Give a way to predict the pop-up button's options without opening it, such as an introductory label or a label on the button itself that describes the effect.
- Consider using a pop-up button when space is limited and it isn't necessary to show all the options all the time, since it's a space-efficient way to present a wide range of choices.
- If necessary, include a Custom option in the menu to offer additional items useful only in some situations, avoiding crowding the interface with rarely used controls; it's possible to display explanatory text below the list.

Exact specifications: none.

Platform differences: no additional considerations in iOS, macOS or visionOS; not supported in tvOS or watchOS. In iPadOS, inside a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options in a list item, when the set of options is small and well defined, allowing a choice without navigating to a detail view.

Links to other articles: Pull-down buttons, Buttons, Menus.

<!-- visual:pop-up-buttons -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_pop-up-buttons, sheet 0001), codes checked; no video.
- The opening diagrams the pop-up button as a list of four options inside a dashed rectangle, with the current option highlighted in a solid white rectangle with rounded corners (img 0883).
- The pop-up button's indicator is a double arrow control, up and down, inside a red button at the end edge of the selected row (img 0883).
- Measurement arrows annotate the total width of the menu and the height of the selected row, with no real app screen (img 0883).
- In the real Calendar screen, the closed control sits in a standard grouped list, with labels on the left and values aligned to the right, and shows the currently chosen value (img 0884).
- On the same screen, the start and end dates and times appear in gray capsules (img 0884).
- Open, the menu is a white card with a shadow that emerges over the list itself, partially covering the neighboring rows, without opening a new panel (img 0885).
- The current option is marked with a check, and the custom option is set apart at the end by a separator (img 0885).
- The pair img 0884 and img 0885 shows the same control first closed and then open, as a before and after.
<!-- /visual:pop-up-buttons -->

## Pull-down buttons (slug: pull-down-buttons)

A pull-down button displays a menu of items or actions directly related to the button's own purpose; after the person chooses an item, the menu closes and the app performs the chosen action.

Why: the pull-down button solves the case where a button needs variations of the same action (for example, "Add" can add different types of item) without multiplying buttons in the interface; that's why Apple insists on balancing the length of the menu, since opening the menu is already an extra step before acting.

Do and avoid:
- Use a pull-down button for commands or items directly related to the button's action (e.g. an Add button whose menu specifies the type of item to add; a Sort button whose menu chooses the sorting attribute; a Back button whose menu chooses a specific location to revisit).
- If you need a list of mutually exclusive choices that aren't commands, use a pop-up button instead.
- Avoid putting all of a view's actions in a single pull-down button; primary actions need to be easily discoverable, not hidden behind a menu the person has to open before doing anything.
- Balance the length of the menu with ease of use: since it's necessary to interact with the button before seeing the menu, listing at least three items helps make the interaction worthwhile; for one or two items, consider other components (buttons for actions, toggles or switches for selections); listing too many items slows down the search for a specific item.
- Display a concise menu title only if it adds meaning; in general the button's content combined with descriptive menu items already gives enough context.
- Warn when a menu item is destructive and ask for confirmation; red text highlights potentially destructive actions, and when one of them is chosen the system displays an action sheet (iOS) or popover (iPadOS) to confirm or cancel, which helps avoid accidental data loss.
- Include an interface icon alongside a menu item when it adds value, preferably using SF Symbols to keep alignment with the text at any scale.

Exact specifications: recommended minimum of three items to justify a pull-down button.

Platform differences: no additional considerations in macOS or visionOS; not supported in tvOS or watchOS. In iOS and iPadOS, it's possible to reveal a pull-down menu through a specific gesture on a button (e.g. since iOS 14, Safari responds to touch and hold on the Tabs button by showing a menu of tab-related actions, such as New Tab and Close All Tabs); consider a pull-down More button to present items that don't need a prominent position in the main interface, weighing the convenience of size against the impact on discoverability, since the ellipsis icon doesn't necessarily help the person predict the content.

Links to other articles: Pop-up buttons, Buttons, Menus.

<!-- visual:pull-down-buttons -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_pull-down-buttons, sheet 0001), codes checked; no video.
- The opening repeats the pop-up button diagram (items stacked in a dashed rectangle, one of them in a solid white block, width and height measurement arrows), but swaps the double arrow for a simple chevron pointing down (img 0915).
- This indicator swap is the visual mark that separates a list of actions from a single-value choice (img 0915).
- In the real Notes screen, the closed More button sits at the right edge of the top bar, which also carries the back button and the share icon (img 0916).
- Open, the menu is a white card with a shadow that covers part of the note's content (img 0917).
- The same menu mixes two formats: at the top, three quick actions in icons side by side; below, a vertical list of items with an icon on the left (img 0917).
- Some items in the list carry a submenu arrow, and one of them displays secondary text that complements the label (img 0917).
- The destructive action comes last, set apart by a separator and written in red (img 0917).
- The pair img 0916 and img 0917 shows the same button closed and open, with the same note in the background.
<!-- /visual:pull-down-buttons -->

## The menu bar (slug: the-menu-bar)

On the Mac or on an iPad, the menu bar at the top of the screen displays the app's or game's top-level menus; Mac users already know the menu bar well and rely on it to learn what an app does and find the commands they need.

Why: the menu bar is the complete, always available inventory of everything an app can do, so Apple defines a fixed order of menus and a standardized internal structure for each one (App, File, Edit, Format, View, app-specific menus, Window, Help): this lets anyone, even someone using the app for the first time, know where to look for a command, and it lets you assign keyboard shortcuts and give access via Full Keyboard Access to commands that might not even appear in the main interface.

Do and avoid:
- Support the standard menus defined by the system and their ordering; in many cases the system already implements the functionality of the standard items (e.g. Edit > Copy becomes available automatically when selecting text in a standard field).
- Always show the same set of menu items; if an item is not actionable in the current context, disable the action instead of hiding it, so the person keeps learning what the app supports.
- Represent actions with familiar icons, the same ones used elsewhere in the system.
- Support the keyboard shortcuts defined for the standard items (Copy, Cut, Paste, Save, Print etc.); define custom shortcuts only when necessary.
- Prefer short, one-word menu titles; if you need more than one word, use title-style capitalization.
- Always display the About item first in the app menu, followed by a separator so it stays alone in its own group.
- In the File menu, for "Open", include an ellipsis if the person needs to select an item in a separate interface; in "Open Recent", list recognizable names (never file paths), from most recent to oldest.
- Prefer "Duplicate" over items like "Save As", "Export" or "Copy To", because those don't make clear the relationship between the original file and the new one.
- In the Edit menu, make the target of Undo and Redo clear (e.g. "Undo Paste and Match Style", "Undo Typing"); use "Delete" (not "Erase" or "Clear") because it is equivalent to pressing the Delete key.
- In the View menu, make sure each show/hide item reflects the current state of the corresponding view (e.g. "Show Toolbar" when it is hidden, "Hide Toolbar" when it is visible); offer a View menu even if the app supports only a subset of the standard functions.
- Position the app-specific menus between View and Window, reflecting the app's hierarchy and ordering from most general or common to least used.
- Offer a Window menu even if the app has only one window, including the Minimize and Zoom items for access via Full Keyboard Access; list open windows in alphabetical order, without listing panels or other modals.
- In the Help menu, keep the total number of items small so as not to overwhelm someone looking for help; use a separator between the main documentation and additional items.
- Use a dynamic menu item (one that changes behavior when a modifier key is held) with restraint, requiring only one modifier key, and never as the only way to perform a task, since it stays hidden by default; prefer using it in menu bar menus, not in context menus or Dock menus, where discovery is even harder.
- For menu bar extras, use a symbol (icon or SF Symbol) to represent the extra, display a menu (not a popover) on click, and let the person (not the app) decide whether to place the extra in the menu bar, typically via settings; consider offering this during setup for discovery. Don't rely on the extra's presence, since the system can hide it; also consider a Dock menu, which stays available at all times while the app runs.

Exact specifications:
- Fixed order of menus in the menu bar: YourAppName, File, Edit, Format, View, app-specific menus (if any), Window, Help; on macOS, the Apple menu sits at the leading edge and the menu bar extras at the trailing edge.
- Short app name in the "About YourAppName" item: prefer 16 characters or fewer, with no version number.
- The menu bar's height is 24 pt.
- Table of standard app menu items, in order: About YourAppName, Settings…, optional app-specific items, Services (macOS only), Hide YourAppName (macOS only), Hide Others (macOS only), Show All (macOS only), Quit YourAppName.
- Table of standard File menu items, in order: New Item, Open, Open Recent, Close, Close Tab, Close File, Save, Save All, Duplicate, Rename…, Move To…, Export As…, Revert To, Page Setup…, Print….
- Table of standard Edit menu items, in order: Undo, Redo, Cut, Copy, Paste, Paste and Match Style, Delete, Select All, Find (with submenus Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, Jump to Selection), Spelling and Grammar (with submenus Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, Correct Spelling Automatically), Substitutions (with submenus Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, Text Replacement), Transformations (with submenus Make Uppercase, Make Lowercase, Capitalize), Speech (with Start Speaking, Stop Speaking), Start Dictation, Emoji & Symbols.
- Table of standard Format menu items: Font (submenus Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, Paste Style) and Text (submenus Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, Paste Ruler).
- Table of standard View menu items: Show/Hide Tab Bar, Show All Tabs/Exit Tab Overview, Show/Hide Toolbar, Customize Toolbar, Show/Hide Sidebar, Enter/Exit Full Screen.
- Table of standard Window menu items, in order: Minimize, Zoom, Show Previous Tab, Show Next Tab, Move Tab to New Window, Merge All Windows, Enter/Exit Full Screen (only if the app has no View menu), Bring All to Front, the name of each specific open window (in alphabetical order).
- Table of Help menu items: Send YourAppName Feedback to Apple, YourAppName Help, Additional Item.

Platform differences: not supported on iOS (outside the iPad context), tvOS, visionOS or watchOS.
- iPadOS: the person reveals the menu bar by moving the pointer to the top edge of the screen or swiping down from it; when visible, it occupies the same vertical space as the status bar. Differences from macOS, according to the table in the text: visibility (hidden until revealed, versus visible by default on macOS), horizontal alignment (centered, versus leading edge on macOS), menu bar extras (not available on iPadOS), window controls (in the menu bar when the app is in full screen on iPadOS, never in the menu bar on macOS), Apple menu (not available on iPadOS), app menu (no About, Services or app visibility items on iPadOS). Reserve the app menu's Settings item to open the app's page in iPadOS Settings; if the app has its own internal preferences, add a separate item below Settings in the same group. For apps with tab navigation, consider adding each tab as a View menu item, possibly with keyboard shortcuts. Consider grouping items into submenus more often than on macOS, since menu item rows on iPad use more space to make touch easier.
- macOS: the Apple menu is always the first item at the leading edge and cannot be modified or removed; when space is limited, the system prioritizes the display of essential menus and menu bar extras, and may truncate titles; when entering full screen, the menu bar typically hides itself until revealed.

Links to other articles: Menus, Dock menus, Standard keyboard shortcuts, Offering help, Status bars, Going full screen, Sidebars, Toolbars, Tab bars.

<!-- visual:the-menu-bar -->
### What the illustrations show
Basis: 1 illustration sheet viewed (hig-img_the-menu-bar, sheet 0001), codes checked; no video.
- The opening shows a complete macOS menu bar with the app name, file, edit, format, view, window and help menus, with the edit menu open and highlighted in a stronger red (img 1144).
- The edit menu is organized into three groups separated by dividers: undo and redo; cut, copy, paste and delete; and find last (img 1144).
- Each edit menu item has an icon at the leading edge, and the cut, copy, paste and find commands show the keyboard shortcut on the right (img 1144).
- On iPad, in dark mode, the menu bar appears centered at the top, between the date and time on the left and the network and battery icons on the right (img 1145).
- The iPad edit menu repeats the macOS structure exactly, but as a light floating panel over the screen's black background (img 1144 compared to img 1145).
- The menu bar extras sit in the top right corner of the Mac, as four icons before the date and time (img 1146).
- An extra's menu is a more compact panel, with three items, a divider before the item that opens the settings, and no keyboard shortcuts next to the items (img 1146).
Recorded divergences: the official description speaks of a stylized representation, but img 1144 shows a functional, detailed menu bar; the stylization is limited to the gradient background.
<!-- /visual:the-menu-bar -->

## Toolbars (slug: toolbars)

A toolbar gives convenient access to frequently used commands, controls, navigation and search; it is made up of one or more sets of controls arranged horizontally at the top or bottom edge of the view, grouped into logical sections.

Why: a toolbar needs to balance three functions at the same time (the current view's title, navigation, and actions on the content), so Apple structures the space into three fixed zones (leading, center, trailing) with their own rules for what fits in each one, so the person always knows where to look for back, the title or an action, regardless of the app.

Do and avoid:
- Choose items deliberately to avoid overloading; define which items migrate to the overflow menu as the toolbar gets narrower, but don't add that overflow manually (the system already does this automatically on macOS and iPadOS) and don't create layouts that cause overflow by default.
- Add a More menu for additional actions, prioritizing the least important ones; try to include everything in the toolbar first and only use More if you really need to.
- On iPadOS and macOS, consider allowing toolbar customization to include the person's most common items, especially in apps with many items or ones used for long periods.
- Reduce the use of custom backgrounds and tinted controls in the toolbar, because they can overlap or interfere with the system's background effects; use the content layer to convey color and appearance, and a ScrollEdgeEffectStyle when you need to distinguish the toolbar area from the content area.
- Avoid applying similar colors between toolbar item labels and the content layer's background.
- Prefer standard components in the toolbar, whose corner radius is already concentric with the bar's corners; if you create a custom component, ensure the same concentricity.
- Consider temporarily hiding the toolbar for a distraction-free experience, contextually, offering a reliable way to restore the hidden elements.
- Give each window a useful title; if titling it seems redundant, leave the title area empty. Don't use the app's name as the window title. Write a concise title, under 15 characters, to leave room for other controls.
- Use the standard Back and Close buttons, with the standard symbols, without a "Back" or "Close" text label; if you create a custom version, ensure it keeps the same appearance and behavior throughout the app.
- Provide actions that support the main tasks, prioritizing the most likely commands; make the meaning of each control clear, preferring simple, recognizable symbols over text (except for actions like edit, which symbols represent poorly).
- Prefer system-provided symbols with no border, since the section already provides a visible container and the system already defines the hover and selection states automatically.
- Use the .prominent style for key actions like Done or Submit, specifying only one primary action, positioned at the trailing edge of the toolbar.
- Position items in the three zones: leading (elements for going back to the previous document, showing/hiding the sidebar, the view's title and, next to it, a document menu with commands like Duplicate, Rename, Move, Export; items in this zone are not customizable, to guarantee constant availability), center (common, useful controls, and the view's title if it is not in leading; on macOS and iPadOS it can be customizable by the person, and it collapses automatically into the overflow menu when the window shrinks), trailing (important items that need to stay always available, buttons that open nearby inspectors, an optional search field, the More menu, and the primary action such as Done when it exists; it stays visible at any window size).
- Group items logically by function and frequency of use; group navigation controls and critical actions (Done, Close, Save) into dedicated sections that are familiar and visually distinct.
- Keep groupings and positioning consistent across platforms.
- Minimize the number of groups, with a maximum of about three overall.
- Keep actions with text labels separate from actions with symbols, inserting fixed space between buttons to prevent the text of different labels from appearing to merge.

Exact specifications: window title under 15 characters; at most about three groups of items in the toolbar.

Platform differences:
- iOS: prioritize only the most important items in the toolbar's main area, since space is limited, creating a More menu for the rest; use a large title to help with orientation during navigation and scrolling, which by default transitions to a standard title on scroll and returns to large at the top.
- iPadOS: consider combining a toolbar with a tab bar, since they can coexist in the same horizontal space at the top of the view, useful for navigating between a few main areas while keeping the full width available for content.
- macOS: the toolbar sits in the window's upper frame, below or integrated with the title bar; window titles can appear inline with the controls, and toolbar items have no bezel; make every toolbar item also available as a command in the menu bar, since the toolbar can be customized or hidden and cannot be the only place that presents a command (the reverse is not necessary: not every menu item needs space in the toolbar).
- visionOS: the system toolbar sits at the bottom edge of the window, above the window management controls, on a plane parallel and slightly in front of the window on the z axis; it uses a variable blur on the bar's background to keep item legibility as content scrolls behind it; you can provide a symbol, a text label, or both for each item, and looking at an item with a symbol reveals the text label in visionOS; prefer the toolbar provided by the system, optimized for gaze and hand input; avoid creating a vertical toolbar, because tab bars are already vertical in visionOS and this would create confusion; try to prevent the window from resizing below the toolbar's width, since visionOS has no menu bar as a safety net; avoid using a pull-down menu in a toolbar, because it can obscure the standard window controls that sit below the bottom edge.
- watchOS: a toolbar button can sit in the upper corners or along the bottom; if placed above scrolling content, it stays visible while the content scrolls underneath; you can also place a button in the scroll view itself, which by default stays hidden until the person scrolls up, taking advantage of the habit of scrolling to the top; use a scrolling toolbar button for an important action that is not the view's primary function (e.g. Mail offers New Message in a toolbar button at the top of the Inbox, whose primary function is to display the list of messages).
- No additional considerations on tvOS.

Links to other articles: Sidebars, Tab bars, Layout, Buttons, Search fields, Apple Design Resources, Going full screen, Immersive experiences, Pull-down buttons, Icons, SF Symbols, Liquid Glass color.

<!-- visual:toolbars -->
### What the illustrations show
Basis: 6 illustration sheets viewed (hig-img_toolbars, sheets 0001 to 0006), codes checked; no video.
- The opening places the back button isolated at the leading edge and three controls (edit, share, more options) in a single capsule at the trailing edge, with ruler arrows marking the bar's total extent and the buttons' height (img 1163).
- In Notes on the Mac, the wide window shows the entire toolbar with the More menu open; when the window narrows, few icons remain and an overflow button with a double arrow appears, whose menu collapses the items that did not fit, including More itself (img 1164, img 1165).
- Wrong and right pair on the back button: the capsule with an arrow and the word "Back" gets the gray X stamp; the circular button with only the symbol gets the green check; the stamps sit beside the button, never over it (img 1166, img 1167, img 1168, img 1169).
- The same group of three actions appears first in text, separated by thin dividers inside the capsule, and then in symbols (filter lines, trash, plus sign), more compact and with no visible dividers (img 1170, img 1171).
- Symbols with their own circular outline inside the capsule are contrasted with the same symbols loose, without a border, over the group's shared background (img 1172, img 1173).
- The primary action appears as a filled blue circular button with a white check at the trailing edge, separate from the filter button, which stays unhighlighted (img 1174).
- On iPad, zone labels connected by thin lines divide the Freeform toolbar into three regions: back and title at the leading edge, a group of six tools in the center, a group of four actions at the trailing edge (img 1175).
- On iPhone, the same set of controls is compared in a single capsule and in two capsules, with back and forward isolated from the tool and from more options (img 1176, img 1177).
- A text label and a symbol sharing the same capsule are contrasted with the version where each one gets its own capsule (img 1178, img 1179).
- On macOS, straight-line callouts name the Finder window's top strip as toolbar and the outer edge as the window frame (img 1180).
- On visionOS, the toolbar is translucent and sits at the bottom edge of the window, with the note count label and icons divided by a separator; isolated, it shows four label items with the selected one on a more opaque background and the blurred environment visible through the material (img 1181, img 1182).
- On watchOS, the toolbar buttons occupy the upper corners around the blue title, or sit in a pair at the bottom of the screen; and an almost identical pair shows the list with no action button and then with a large green button revealed between the title and the items, on scrolling to the top (img 1183, img 1184, img 1185, img 1186).
Recorded divergences: in img 1174 the primary action uses a check icon, not the text "Done" cited in the official description.
<!-- /visual:toolbars -->

## What this group reveals about the Apple way

- Every component that hides an action (context menu, edit menu, pull-down button, Home Screen quick action) comes with the rule that the same action must exist somewhere visible in the main interface: context-menus, edit-menus, pull-down-buttons, the-menu-bar (macOS: "make every toolbar item also available in the menu bar").
- Apple treats "hiding an unavailable item" and "dimming an unavailable item" as two distinct techniques with opposite contexts of use: normal menus and the menu bar dim (to teach what exists), context menus hide (because they only show what is already relevant): context-menus, menus, the-menu-bar.
- There is a systematic distinction between "mutually exclusive state" components (pop-up buttons) and "action or command" components (pull-down buttons, toolbars, context menus), each with its own semantics for what it can and cannot contain: pop-up-buttons, pull-down-buttons.
- Many articles in this group explicitly restrict the number of simultaneous elements the person should see: one or two prominent buttons, at most about three groups in a context menu or a toolbar (context-menus, toolbars), up to four Home Screen quick actions (home-screen-quick-actions), a single help button per window (buttons), submenus limited to one level (context-menus, menus).
- Structural order matters as much as content: the menu bar has a fixed sequence of menus and each menu has a table of items in a defined order (the-menu-bar); the toolbar has three fixed zones with their own customization rules per zone (toolbars).
- On unconventional input platforms (visionOS), almost every component gains an extra layer of rules about spatial perception: depth relative to the window (ornaments, toolbars), breakthrough effect (menus), hover effect and sound feedback instead of haptic (buttons, ornaments).
- Apple prefers system symbols (SF Symbols) to text whenever the action is recognizable, reserving text for when a short label communicates more than an icon; this preference appears almost identically in buttons, toolbars, menus and home-screen-quick-actions.
- Destructive actions receive specific, repeated visual and flow treatment: the system's red color, position at the end of the menu, and mandatory confirmation via a separate alert before executing, present in buttons, context-menus and pull-down-buttons.
- Several components in this group have direct equivalents between macOS and iOS/iPadOS that Apple documents side by side, treating them as the same function adapted to the platform: Dock menu (macOS) and Home Screen quick actions (iOS/iPadOS); the menu bar on macOS and on iPadOS, compared item by item in a table.
- The capacity for personalization (toolbar customization, menu bar extras, dynamic quick actions) always comes conditioned on a fixed, non-customizable anchor that guarantees minimal predictability: the toolbar's leading zone is not customizable (toolbars), the Apple menu cannot be modified (the-menu-bar), and dynamic quick action changes must be predictable (home-screen-quick-actions).
- Third-party extensions and integrations (share/action extensions, menu bar extras, Dock menu) are treated as deliberate second-class participants: they can be hidden, reordered or disabled by the system or by the person at any time, and so none of them can be the only path to a function (activity-views, the-menu-bar).

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/activity-views.md, 46 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/buttons.md, 141 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/context-menus.md, 63 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/dock-menus.md, 25 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/edit-menus.md, 53 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/home-screen-quick-actions.md, 27 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/menus.md, 95 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/ornaments.md, 37 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pop-up-buttons.md, 42 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pull-down-buttons.md, 44 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/the-menu-bar.md, 196 lines, read to the end: yes
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/toolbars.md, 136 lines, read to the end: yes

All 12 files in the group were read in full in a single call of the Read tool each, with no truncation reported by the tool. No article in this group is only a collection index: all 12 have text of their own.

