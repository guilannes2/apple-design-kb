## Raise the bar with iPhone Duo (id: tech-talks_111462, 15.7 min)

Basis: transcript (frames not viewed yet). Local automatic transcript made with Whisper, it is not Apple's official one; proper names and terms may carry hearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111462/.

Central thesis: In iPhone Duo, the first iPhone with multiple screens and a wider ratio, the controls that normally sit at the top and bottom (navigation bar, toolbar and tab bar) move to the side, where they are easier to reach and leave the vertical space for the content; they are the same components adapted to a different layout. To take advantage of this, the app needs to be recompiled with the new SDKs, use the bars from the system's containers, prepare the custom items for the vertical axis and declare overflow priorities so the system can adapt.

The design process Apple describes:
1. Understand the device and the principle: the wider silhouette gives horizontal space, the controls move to the side, the position stays the same when opening to the inner screen in landscape, and when opening in portrait, the larger screen returns to the familiar layout with horizontal bars.
2. Enable the new behavior: recompile the app with the most recent SDKs and use the bars provided by the navigation containers, instead of hand-assembled bars.
3. Understand where the content is positioned: navigation, toolbar and tab bar coexist in a shared region, with their own rules for Split View, inspectors, sheets and right-to-left languages.
4. Audit the toolbar's current configuration and make sure the controls follow the recommended order, from top to bottom.
5. Prepare the toolbar content for the vertical axis: provide title and icon for each item, adjust the axis when the default does not fit, reduce text-only items and adapt the custom views.
6. Manage the overflow: decide whether the toolbar or the tab bar compresses first, consolidate the app's own overflow into a single system-managed menu and assign visibility priorities.
7. Assess whether the app or a specific sheet should disable the vertical bar.
8. Closing: the idea was born from asking whether the bars really needed to stay at the top and bottom; the final outline repeats four steps (recompile with the new SDKs, audit the bars, update custom items, assign overflow priorities).

Principles stated and why:
- Every designer is an engineer and every engineer is a designer. Why: you need to understand both sides to build a great app.
- Top and bottom controls move to the side in the wide ratio. Why: it takes advantage of the width, preserves vertical space for the content and makes the controls easier to reach.
- The position of the bars stays the same when opening the device to the inner screen in landscape, and in portrait the larger screen returns to the familiar horizontal bars. The speech does not give a specific why; it only notes that they are the same components, adapted to a different layout.
- Keep the controls associated with their container, even though it is tempting to change the axis of all of them. The speech presents this as a summary of the previous rules: in complex layouts, items only move to the vertical axis when the container is at the edge of the screen.
- Expanded inspectors do not get their own vertical bar, since the Detail column already has one. Why: avoid confusion.
- The bar stays on the same side of the device in right-to-left languages; the content adapts around it and it remains fixed. Why: the bar is aligned to the hardware.
- Vertically, the items keep a clear hierarchy from top to bottom, with main navigation at the top and prominent actions next.
- Keep control positioning consistent. Why: not every pose uses vertical bars, and people should not have to relearn where the actions are.
- Vertical bars work better with symbol-only items. Why: unlike horizontal ones (fixed height, flexible width), vertical ones have fixed width and flexible height.
- Provide all of the item's information up front and let the system choose the representation for each context. Why: even an image item needs a title, because the system uses it when the item goes into the overflow or into an expanded form.
- Related items stay on the same axis. Why: an item that alternates between symbol and text, like the edit button, should not go to the vertical bar even if the symbol would fit in it.
- Minimize title-only items and custom views with text and image. Why: this way more content can go into the vertical bar, and in most cases these items can use the symbol representation.
- Ask whether the text only reinforces the symbol or carries its own information. Why: if it is supplementary, the symbol alone usually communicates the action clearly; if it carries meaningful information, the control should stay in the horizontal bar.
- Accessory bars remain attached to the keyboard, without moving to the vertical axis (the speech does not give the why).
- The app should not create additional spacing, whether the bar is horizontal or vertical (the speech does not give the why here and refers to Maria's video at DubDub25, a term uncertain in the automatic transcription).
- In navigation-focused experiences, the toolbar compresses first. Why: the main destinations remain accessible. This is the default behavior.
- In task-oriented experiences, the tab bar compresses first. Why: preserve the frequently accessed actions.
- Consolidate the app's own overflow into a single system-managed menu; not every existing menu should become overflow.
- The ellipsis is the standard overflow symbol on iPhone, so it should be reserved for that use, without bringing in symbols from other platforms, and other menus should get a distinct symbol. The reason given is simply that it is the standard symbol.
- When assigning priorities, think about what people access most often: frequently used actions should be among the last to go into the overflow. Likewise, controls that show important status, like items with a badge, stay visible for longer. Why, for these: preserve quick reading (glanceability).
- Most apps are good candidates for the vertical bar, but there are cases where it is worth disabling the bar. Why: in a single-page app with a heavy layout at the bottom, the horizontal layout can let the content expand fully; in a sheet full of controls with a single item, the vertical bar would reduce the available space.
- Result sought: content with a sense of space and accessible controls, the same familiar experience made for a completely new iPhone.

Concrete interface-building techniques, with exact numbers when spoken:
- The speech doesn't give numeric interface values (points, sizes, spacing, durations). The numbers mentioned are contextual: imagining the bars rotating 90 degrees into a vertical stack; badge API added in iOS 26; Maria's video at DubDub25 (uncertain term in the automatic transcription); What's new in SwiftUI from WWDC 26.
- Enablement: recompile with the latest SDKs. For other behaviors enabled by recompiling, the speech points to the session Prepare Your App for iPhone Duo.
- Containers in SwiftUI: use the toolbar modifier together with Navigation Stack or Navigation Split View; use Tab View.
- Containers in UIKit: prefer UINavigationController and UITabBarController, which manage their own bars; set the toolbar items on the view controller and place it inside a navigation controller, instead of creating a custom UIToolbar. In custom bars, the content of subcomponents such as UIToolBar, UINavigationBar or UITabBar is not taken into account.
- Shared region: navigation, toolbar and tab bar coexist in a shared region, in combinations that depend on the layout.
- Split View: only the Detail column takes part in the vertical bar; items in the other columns stay horizontal. Expanded inspectors don't get a bar of their own.
- Sheets: on the external screen, if the sheet already has a toolbar, it appears on the vertical bar; on the internal screen, they're centered by default with horizontal items. With the Preferred Placement API, a sheet positioned on the left has no vertical bar and one positioned on the right gets one.
- Right-to-left languages: the bar stays on the same side of the device and the content adapts around it.
- Item order: the top is reserved for primary navigation, such as back or close, followed by prominent actions, such as complete (done). With a navigation controller, the back button is added automatically.
- Custom back or close buttons: in SwiftUI, placement cancellation action; in UIKit, leading item with leftItemSupplementsBackButton set to false, which is the default.
- Prominent actions: in SwiftUI, placement top bar pinned trailing; in UIKit, pinned trailing group.
- The remaining items keep their original grouping, with a vertical spacer visually separating the top and bottom placements, even when unified into a single bar.
- Item representation: the app provides an icon and a title. In the top and bottom bars, the item prefers to show the icon (share button); without an icon, it shows the text (edit button); in the overflow, it shows title and icon. This doesn't change with vertical bars.
- Axis choice by the system: items described in the speech as Text-only items with an icon (uncertain term in the automatic transcription), such as back and share, move to the vertical axis; text-only items, such as edit, stay on the horizontal axis. Using Label in SwiftUI or the title and image properties of UIBarButtonItem already prepares the item.
- By default, SwiftUI and UIKit infer the axis from the item's content. To adjust it, there's the new AxisBehavior API.
- The system edit button stays on the horizontal bar automatically. Custom item that toggles between symbol and text: use the horizontal only axis behavior.
- A custom view in UIKit or a more complex view in SwiftUI stays horizontal by default; if it has a vertical representation, set the preferred vertical axis behavior to allow it to go to the vertical bar.
- Badge: instead of keeping the inline count, use a badge on the icon to turn an item with text and symbol into a symbol-only item; adopt the iOS 26 badge API for standard system appearance across all devices.
- Custom views on the vertical bar: they must fit within the bar's fixed width or have a layout adapted to vertical; consider adjusting metrics for the vertical representation.
- Detecting the vertical bar: read the toolbar vertical edge environment property or trait, inside the item's content view or custom view. The value is populated when the items can go on the vertical axis and is nil or unspecified when they can't.
- Material: like the horizontal bars, the vertical bar has no scroll edge effect by default, but gains a background when the Reduce Transparency accessibility setting is on; the content of custom views must stay legible in any case.
- Spacers: flexible ones have zero size on the vertical axis by default; fixed ones still respect the minimum size.
- If the bars haven't been updated to the new design yet, or the items haven't been grouped at the leading and trailing edges yet, the speech says now is the time to do it.
- Overflow: on the external screen in landscape, items overflow more because there's less vertical space; the bar also overflows when competing elements appear, such as the keyboard or picture in picture in OpenPortrait (uncertain term in the automatic transcription).
- Toolbar compression behavior API: configures, per view, whether the toolbar or the tab bar compresses first.
- System overflow menu: toolbar overflow menu in SwiftUI; additional overflow items in UIKit.
- Visibility priority: toolbar visibility priority lets you assign each item a high, low or custom priority, controlling the order in which they collapse. Prioritize by groups first, then, if needed, within each group. Visibility priority APIs exist in SwiftUI and UIKit.
- Disabling the vertical bar: the toolbar vertical behavior and preferred vertical bar behavior APIs.

Examples cited:
- Maria's app: it was already resizable, but the bars stayed horizontal. It teaches that recompiling with the new SDKs and using the containers' bars is still needed.
- Notes uses a toolbar, Clock uses a tab bar and Fitness uses both a toolbar and a tab bar. It teaches that the shared region receives different combinations depending on the layout.
- Share and edit buttons: they show how the system chooses between icon and text and which axis each item ends up on.
- The Clock edit button, which toggles between symbol and text: it doesn't go to the vertical bar, because related items must stay on the same axis.
- Custom selection button: uses the horizontal only axis behavior.
- Compass view in the top right corner: a custom view that supports a vertical representation and so gets the preferred vertical axis behavior.
- Inbox with the inline count swapped for a badge: it becomes a symbol-only item, suited to the vertical bar.
- Cart button with the total value in dollars: the text carries information of its own, so it stays on the horizontal bar.
- Custom action panel: it hides the titles and gets a little shorter when there's a vertical bar, freeing up space for other content.
- Podcast view: a navigation experience in which the toolbar compresses first, the default.
- Games app: a task-oriented experience in which the tab bar compresses first.
- Compose in Mail and new note in Notes: frequent actions that should be among the last to go to the overflow.
- Calculator: a single-page app with a heavy layout at the bottom, a candidate for keeping the horizontal layout.
- A sheet full of controls with only the close button: a candidate for disabling the vertical bar so as not to reduce the space.
- Closing joke: asked if there was anything else, the answer is that it's in the overflow menu.

Quotes:
"What if bars didn't have to be at the top and the bottom?"
