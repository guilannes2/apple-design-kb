# Components / Presentation

## Action sheets (slug: action-sheets)

What it governs: an action sheet is a modal view that presents choices related to an action the person deliberately initiated.

Why: Apple distinguishes an action sheet from an alert by intent. An action sheet appears because the person did something that requires clarification (for example, canceling a message being edited), while an alert is generally unexpected, warning about a problem or a change in situation that the person did not directly cause. Interrupting the current task has a cost, so its use should be rare and the text should be quick to understand.

Do and avoid:
- Use an action sheet, not an alert, to offer choices linked to an intentional action.
- Use action sheets with restraint, because they interrupt the current task.
- Keep titles short enough to fit on one line; a long title is hard to read quickly and may truncate or require scrolling.
- Provide a message only if necessary; the title plus the context of the action are usually enough.
- If necessary, provide a Cancel button that allows rejecting an action that would destroy data; position it at the bottom of the action sheet (or in the upper left corner on watchOS). A confirmation dialog in SwiftUI already includes Cancel by default.
- Make destructive choices visually prominent: use the destructive style and position those buttons at the top, where they draw more attention.
- On iOS and iPadOS, use an action sheet, not a menu, for choices linked to an action; people expect a menu when they choose to reveal it, not as a response to an action.
- Avoid letting an action sheet scroll on iOS/iPadOS; the more buttons, the more effort to choose, and scrolling can cause an accidental tap.
- On watchOS, avoid showing more than four buttons, including Cancel; since Cancel is required, the target is at most three additional choices.

Exact specifications: no measurement number (pt, px, ms) is given in the text. The only numeric limit is the one for buttons on watchOS: up to four buttons in total (Cancel included), that is, at most three choices beyond Cancel.

Platform differences:
- iOS, iPadOS: action sheet instead of menu for actions; avoid scrolling.
- watchOS: system-defined style with title, optional message, Cancel button and one or more additional buttons; three system-defined button styles (Default, Destructive, Cancel); appearance varies by device.
- macOS, tvOS: no additional considerations.
- visionOS: not supported.

Links to other articles: Modality, Sheets, Alerts.

<!-- visual:action-sheets -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked; the page has no video.
- The opening diagram isolates a light card with a bold title, a short description below and three stacked pill buttons, with a dashed outline; a horizontal double arrow above measures the total width and a vertical mark on the right measures the height of the card, so the image treats the component as a block of proportions, not as an app screen (img 0025).
- The internal hierarchy of the card is title, then description, then the stack of three actions, all with the same pill shape (img 0025).
- In Mail on iPhone, the first screenshot shows the composition state, with an X close button, a blue circular send button with an upward arrow, and the message fields (img 0026).
- The second screenshot repeats exactly the same screen and only changes the overlay: a floating white card right below the status bar, covering part of the top and leaving the email visible behind it, with two stacked pill buttons (img 0027).
- In that action sheet, the two stacked buttons are "Delete Draft" in red and "Save Draft" in black (img 0027).
- The before-and-after pair with the same background makes it clear, by direct comparison, that this is a two-step flow triggered by the person's action, and not two independent screens (img 0026, img 0027).
- On watchOS, the action sheet occupies the screen over a dark blue to purple gradient, with an X close button in the upper left corner, title and description centered in white, and two large stacked pill buttons, the action in green and Cancel in a purple to magenta gradient, that is, buttons colored by function instead of neutral (img 0028).
Recorded divergences: img 0025 diverges from the official description, which speaks of buttons at the bottom of an iPhone, while the image shows an isolated card with width and height annotations, with no iPhone and no position on the screen; img 0028 shows real text and labels and distinct colors per button, where the official description speaks generically of content that represents text and two stacked buttons.
<!-- /visual:action-sheets -->

## Alerts (slug: alerts)

What it governs: an alert gives the person critical information they need to receive immediately, such as a problem, a warning that the action might destroy data, or the chance to confirm a purchase or another important action they themselves initiated.

Why: alerts interrupt the current task, so Apple treats that interruption as a cost that is only justified when the information is essential and actionable. The document's text insists on a direct and neutral tone because alerts usually describe serious problems, and being vague or accusatory makes the experience worse exactly at the moment when the person most needs clarity. The choice between a complete-sentence title and a sentence fragment follows the same logic of language precision used in other Apple text components.

Do and avoid:
- Use alerts with restraint; each one should offer only essential information and useful actions.
- Avoid using an alert only to inform, with no associated action; prefer communicating that another way within the relevant context.
- Avoid alerts for common, undoable actions, even destructive ones, because the person already intends to discard the data and can undo it.
- Avoid showing an alert when the app starts; if you need to convey something important right from the start, make the information discoverable another way, such as cached data or a discreet label.
- Throughout the alert text, be direct and use a neutral, approachable tone; avoid being oblique, accusatory, or masking the severity.
- Write a title that describes the situation clearly and concisely, describing what happened, the context, and why, without being verbose; avoid empty titles like "Error" or "Error 329347 occurred" and avoid long titles that break into more than two lines.
- If the title is a complete sentence, use sentence-style capitalization and appropriate end punctuation; if it is a fragment, use title-style capitalization and do not use end punctuation.
- Include informative text only if it adds value; if you need it, keep it short, with complete sentences and proper punctuation.
- Avoid explaining the alert's buttons if the text and the button titles are already clear.
- If supported, include a text field only when the person's input is necessary to resolve the situation.
- Create succinct, logical button titles, with one or two words that describe the result of selecting the button; prefer verbs and verb phrases related to the alert text ("View All", "Reply", "Ignore"). In purely informative alerts, you can use "OK" for acceptance, avoiding "Yes" and "No". Always use "Cancel" for the button that cancels the alert's action.
- Avoid using "OK" as the default button title unless the alert is purely informative, because the meaning of "OK" can become ambiguous.
- Position the buttons where the person expects them: in general, the button most likely to be chosen is on the right side (trailing) in a row of buttons or at the top in a stack; the default button is always on the right side or at the top. Cancel buttons are typically on the left side (leading) in a row or at the bottom in a stack.
- Use the destructive style to identify a button that performs a destructive action the person did not deliberately choose. When the person has already deliberately chosen a destructive action (such as Empty Trash), the resulting alert does not apply the destructive style to the button, because the button fulfills the person's original intent.
- If there is a destructive action, include a Cancel button to give a clear, safe way to avoid the action; never make Cancel the default button. If you want to encourage the person to read the alert instead of simply pressing Return, avoid making any button the default. If you need to display an alert with a single button that is also the default, use a Done button, not a Cancel.
- Offer alternative ways to cancel an alert when it makes sense, in addition to the Cancel button.
- On iOS and iPadOS, use an action sheet, not an alert, to offer choices linked to an intentional action (example: canceling a message in Mail offers three choices: delete the edits, save the draft, or go back to editing).
- Avoid, when possible, displaying an alert that scrolls; keep titles short and the message brief, only when necessary.
- On macOS, use the warning symbol (`exclamationmark.triangle`) with restraint, only when the extra attention is truly necessary, such as confirming an action that could cause unexpected data loss; do not use the symbol for tasks whose sole purpose is to overwrite or remove data, such as saving or emptying the trash.

Exact specifications:
- visionOS: if you need to display an accessory view in an alert, create a view with a maximum height of 154 pt and a corner radius of 16 pt.
- In all alerts, up to three buttons in total.

Platform differences:
- iOS, iPadOS: prefer action sheet for choices linked to intentional actions; minimize scrolling of the alert.
- macOS: automatically displays the app icon in the alert, but allows an alternative icon or symbol; allows repeatable alerts with suppression of subsequent occurrences; allows a custom accessory view; allows a Help button; measured use of the warning symbol.
- visionOS: in the Shared Space, the alert appears in front of the app's window, slightly ahead on the z axis; if the person moves the window without dismissing the alert, it stays anchored to the window; in the Full Space, the alert appears centered in the field of view.
- tvOS, watchOS: no additional considerations. Alternative ways to cancel vary: exiting to the Home Screen (iOS, iPadOS); Escape or Command-Period with a connected keyboard (iOS, iPadOS, macOS, visionOS); pressing Menu on the remote (tvOS).

Links to other articles: Modality, Action sheets, Sheets.

<!-- visual:alerts -->
### What the illustrations show
Basis: 2 of 2 illustration sheets viewed, plus 1 of 1 sheet from the video hig-vid_alerts__002 and 3 of 3 sheets from the video hig-vid_alerts__003, all codes checked.
- The opening diagram is the only one with dimension marks: double arrows at the top, on the left and on the right of the card, and a small chevron below, which the notes read as dimension annotations and possibly margins; inside, a bold title, a description, and two pill buttons side by side, the secondary one in light pink and the primary one in strong red with larger bold text, which marks the hierarchy between the two actions through color and weight (img 0046).
- On iPhone, the alert is small and centered over a solid gray background, with the two buttons side by side, the secondary one in light gray and the primary one filled in blue (img 0047).
- On Mac, the alert is more compact, centered over the window, and the buttons are stacked, with the filled blue primary on top and the light gray secondary below (img 0048).
- On tvOS, the alert is semitransparent over a landscape photo, offset to the right of center, with the buttons side by side and the primary one filled in blue (img 0049).
- On Vision Pro, the alert is a translucent frosted glass panel over a blurred home environment, with a blue circular exclamation icon at the top and stacked buttons with no solid fill, in the same material as the panel (img 0050).
- On Apple Watch, the title and description are centered in white over a dark blue to purple gradient, with two large stacked pill buttons, the primary one in green and the secondary one in a purple to magenta gradient, the same palette and structure as the watchOS action sheet (img 0051).
- Comparing the platforms, the title and description structure is identical across all of them, and what changes is the arrangement of the buttons (side by side on iPhone and tvOS, stacked on Mac, Vision Pro and Watch) and the material of the background (opaque, semitransparent, glass, or gradient) (img 0047 to img 0051).
- In the Freeform video, the alert does not appear directly: first there is a context menu on the item with "Recover" and "Delete" in red (q001), the Delete option is highlighted (q002, 1.5 s), and only then does the menu disappear and the alert appears with the app icon, a question title, text, a red "Delete" button and "Cancel" (q003, 2.0 s) (hig-vid_alerts__002, sheet 0001).
- In that video, the alert never coincides with the outline of the window behind it: it appears shifted to the right and up in q003 and gets closer to the center of the window in q004 (2.5 s), with identical content, which suggests it floats in front of the window in depth (hig-vid_alerts__002, sheet 0001).
- In the second video, in a living room, the alert is born as a small, semitransparent panel in place of the menu (q003) and forms in front of the window in q004 and q005; from q005 on, the window and the alert progressively become more transparent and start to move together to the left, frame by frame, until q009 (hig-vid_alerts__003, sheet 0001).
- From q010 to q015 the group moves to the left of the room and from q016 to q018 returns to the right, always with the same elevated transparency and the same relative distance between the alert and the window; at q019 (12.0 s) the group is back near the initial position, with the alert still attached to the window (hig-vid_alerts__003, sheets 0002 and 0003).
Recorded divergences: in hig-vid_alerts__002, the frames add to the official description the context menu step before the alert and the variation in the alert's position between q003 and q004; in hig-vid_alerts__003, they add that the window's movement goes to the left and then returns to the right, rather than following a single direction.
<!-- /visual:alerts -->

## Page controls (slug: page-controls)

What it governs: a page control displays a row of indicator images, each representing a page in a flat list, helping navigate to the desired page.

Why: Apple's reasoning is that the page control serves sequential, ordered relationships, not hierarchical ones, and that its legibility depends on keeping the indicators simple and few in number, because dots are counted at a glance, not read like text. Custom imagery is only justified when it reinforces the control's overall meaning; otherwise it becomes visual noise that requires memorization.

Do and avoid:
- Use page controls to represent movement through an ordered list of pages; they don't represent hierarchical or non-sequential relationships. For more complex navigation, consider a sidebar or split view.
- Center a page control at the bottom of the view or window.
- Although the page control can handle any number of pages, avoid displaying too many: more than about 10 dots are hard to count at a glance; beyond that, consider another arrangement, such as a grid.
- By default, the page control uses the system's dot image for all indicators, but it can display a single image to identify a specific page.
- Make sure custom indicator images are simple and clear; avoid complex shapes, negative space, text or internal lines, which make the icon confusing at very small sizes.
- Customize the indicator's default image only when it reinforces the control's overall meaning.
- Avoid using more than two different types of indicator images in the same page control; using several unique images requires the person to memorize the meaning of each one and leaves the control looking cluttered.
- Avoid coloring indicator images; custom colors reduce the contrast that distinguishes the current page's indicator; let the system color it automatically.
- On iOS/iPadOS, the control can shrink indicators on both sides to suggest more pages are available when they don't all fit in the space.
- Avoid animating page transitions during "scrubbing" (dragging); use the animated scroll transition only for tap, because scrubbing can be very fast and constant animation causes lag and visual flashes.
- The page control can include a translucent background in a rounded rectangle with three styles: Automatic (shows the background only during interaction, use when the page control isn't the screen's primary navigational element), Prominent (always shows the background, use only when the control is the screen's main navigational element), Minimal (never shows the background, use when you only want to indicate the current page's position without visual scrubbing feedback).
- Avoid supporting the scrubber when using the minimal background style, since it doesn't give visual feedback during scrubbing.
- On tvOS, use page controls in full-screen page collections; additional controls make it harder to keep focus while moving between pages.
- On visionOS, page controls represent available pages and indicate the current one, but the person doesn't interact with them directly.
- On watchOS, use vertical paging to separate multiple views into distinct pages with a clear purpose, letting the person scroll with the Digital Crown; this approach is more effective than horizontal paging or many levels of hierarchical navigation. Consider limiting the content of an individual page to the height of a single screen.

Exact specifications: the only explicit number is the practical limit of about 10 dots before visual counting becomes difficult.

Platform differences:
- Not supported on macOS.
- iOS, iPadOS: adaptive indicators (shrink, highlight the current page), tap interaction and scrubbing, three background styles (Automatic, Prominent, Minimal).
- tvOS: used in full-screen page collections.
- visionOS: non-interactive indicators.
- watchOS: horizontal paging (at the bottom of the screen) or vertical (next to the Digital Crown); indicator transitions between page navigation and scrolling the content of a long page.

Links to other articles: Scroll views.

<!-- visual:page-controls -->
### What the illustrations show
Basis: 2 of 2 illustration sheets viewed, all codes checked; the page has no video.
- The opening diagram places the page control at the base of a rounded-corner window, with the active page as a solid black dot and the others in lighter red; a double vertical arrow covers almost the entire height of the window and another, short one sits next to the control, suggesting the measurement of the component's position and height relative to the window (img 0827).
- Incorrect use, marked with a gray X: in the Weather app's bar, the central pill swaps the dots for a sequence of gray weather-condition icons that differ from each other, between a circular map button on the left and a list button on the right (img 0828 with img 0829).
- Correct use, marked with a green check: the same bar, but the pill shows only the location icon at the start followed by simple dots, with the current page in black and the others in light gray, limiting the control to two types of indicator (img 0830 with img 0831).
- In both Weather examples the page control lives inside a pill flanked by circular buttons, and the difference between right and wrong is only in the pill's content (img 0828, img 0830).
- On iOS and iPadOS, a light gray pill with nine dots shows the size gradation: the five central ones at standard size, the second and second-to-last smaller, and the first and last smaller still, with the central dot filled in black as the current page (img 0832).
- On vertical watchOS, a column of small dots sits on the right side of the screen, in the Digital Crown's position, with the current dot in white and the others in dark gray (img 0833).
- On horizontal watchOS, five dots sit in a row at the bottom of the screen, with the current one in white and the others in dark gray, showing that the same pattern changes axis depending on the paging direction (img 0834).
- In all variations the current indicator is distinguished by solid fill in contrast with the others, black on light in the light versions and white on black on watchOS (img 0827, img 0830, img 0832, img 0833, img 0834).
<!-- /visual:page-controls -->

## Panels (slug: panels)

What it governs: in a macOS app, a panel typically floats above other open windows, providing controls, options or supplementary information related to the active window or the current selection.

Why: the panel exists to give quick access to important controls without competing with the main window for attention; that's why it has a less prominent appearance than macOS window states. The distinction between an inspector panel (updates as the selection changes) and an Info window (always keeps the same content) reflects the principle that the type of container should match the content's expected behavior.

Do and avoid:
- Use a panel to give quick access to important controls or information related to the content the person is working on.
- Consider using a panel for inspector functionality, which displays details of the selected item and updates automatically when the item changes; for content that doesn't change with the selection (Info window), use a regular window, not a panel. Depending on the layout, also consider a split view pane for the inspector.
- Prefer simple adjustment controls in a panel; avoid controls that require typing text or selecting items, because they require multiple steps; prefer sliders and steppers, which give more direct control.
- Write a brief title that describes the panel's purpose, using a noun or noun phrase with title capitalization (examples: "Fonts", "Colors", "Inspector").
- Show and hide panels appropriately: when the app becomes active, bring all open panels to the front, regardless of which window was active when the panel opened; when the app becomes inactive, hide all its panels.
- Avoid including panels in the Window menu's document list; it's acceptable to include commands to show/hide panels in the Window menu, but panels aren't documents or standard windows.
- In general, avoid leaving a panel's minimize button available, since the person doesn't normally need to minimize it.
- Refer to panels by their title in the interface and in help documentation, without including the term "panel" in menus (for example, "Show Fonts", "Show Colors", "Show Inspector"); in documentation, it can be helpful to add "window" to the title when it aids clarity.
- A HUD-style panel serves the same function as a standard panel, but has a darker, more translucent appearance; it works well in apps with highly visual or immersive content, such as media editing.
- Prefer standard panels over HUD; the person can get distracted or confused by a HUD with no logical reason for its presence, and the HUD may not match the currently configured appearance. Use HUD only in media-oriented apps (movies, photos, slides), when a standard panel would obscure essential content, or when you don't need to include controls (most system controls don't match the HUD's appearance, except the disclosure triangle).
- Keep a single panel style when the app changes mode; for example, if you use HUD in full-screen mode, prefer keeping the HUD style when leaving full-screen mode.
- Use color sparingly in HUDs; excess color in a HUD's dark appearance is distracting. Generally small amounts of high-contrast color are enough to highlight important information.
- Keep HUDs small; don't let a HUD obscure the content it adjusts or compete with the content for attention.

Exact specifications: no number (pt, px, ms) is given in the text.

Platform differences: not supported on iOS, iPadOS, tvOS, visionOS or watchOS. The entire article is macOS-specific.

Links to other articles: Windows, Modality.

<!-- visual:panels -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked; the page has no video.
- The opening diagram shows the standard panel as a compact, dark secondary window, with a title bar and a circular close button, floating over a larger main window with a gradient (img 0835).
- The panel appears shifted to the left and down relative to the background window's center, covering only part of the main content and not all of it (img 0835).
- Measurement arrows dimension the panel as a specification: a double horizontal one below for the width and a double vertical one on the right for the height (img 0835).
- The HUD style is shown with a real macOS screenshot: a dark, translucent "Inspector" panel, with a red close button in the top-left corner, through which the colored wallpaper behind it is visible (img 0836).
- The HUD's content is organized in label-and-value pairs aligned against each other, with the file name and date at the top and then sections with a disclosure triangle: "General" open, with origin, resolution, size and data rate, format and other fields, and "Video Details" still collapsed, which forms a dense, hierarchical inspector (img 0836).
Recorded divergences: the notes record that img 0836 adds details to the official description such as the file's full path, the resolution in pixels and the existence of the second collapsible section "Video Details", which the description doesn't mention.
<!-- /visual:panels -->

## Popovers (slug: popovers)

What it governs: a popover is a transient view that appears above other content when the person clicks or taps a control or interactive area.

Why: the popover exists to expose a small amount of information or functionality without consuming the permanent space of a sidebar or panel; because it is ephemeral, Apple limits its scope to a few related tasks and treats its automatic dismissal as expected behavior, reserving explicit confirmation (Cancel/Done) only for when there is real risk of losing work.

Do and avoid:
- Use a popover to expose a small amount of information or functionality, limiting it to a few related tasks, since it disappears after the interaction.
- Consider using popovers when you want more space for content, avoiding the space cost of sidebars and panels, for temporary content.
- Position popovers appropriately: the arrow should point as directly as possible to the element that revealed it; ideally the popover does not cover that element or essential content.
- Use a Close button (including Cancel or Done) only for confirmation and guidance, when it brings clarity (such as exiting while saving or not); otherwise, the popover closes normally when clicking/tapping outside it or selecting an item in it. If multiple selections are possible, keep the popover open until the person explicitly dismisses it or clicks/taps outside it.
- Always save the work when automatically closing a non-modal popover, since the person can dismiss it unintentionally by clicking outside; discard the work only when the person clicks an explicit Cancel button.
- Show only one popover at a time; multiple popovers clutter the interface and cause confusion. Never show a cascade or hierarchy of popovers, one emerging from another; if you need to show a new one, close the open one first.
- Do not show another view over a popover; nothing should appear over it, except an alert.
- When possible, allow closing a popover and opening another with a single click or tap, especially when several bar buttons open different popovers.
- Avoid making a popover too large; make it only large enough to display its content and point to the location of origin; the system can adjust the size to ensure a good fit.
- Offer a smooth transition when changing the size of a popover, animating the change so as not to give the impression that a new popover replaced the old one.
- Avoid using the word "popover" in help documentation; refer to the specific task or selection.
- Avoid using a popover to show a warning, since the person can miss it or close it unintentionally; use an Alert.
- On iOS/iPadOS, avoid displaying popovers in compact views; reserve popovers for wide views, and for compact views use all available space with a full-screen modal view such as a sheet.
- On macOS, it is possible to make a popover detachable, which turns it into a separate panel when dragged, remaining visible while the person interacts with other content. Consider allowing the person to detach a popover; make minimal appearance changes to the detached popover to maintain context.

Exact specifications: no number (pt, px, ms) is given in the text.

Platform differences:
- No additional considerations for visionOS.
- Not supported on tvOS or watchOS.
- iOS, iPadOS: avoid popovers in compact views, reserve for wide views.
- macOS: support for detachable popover, turning into a panel.

Links to other articles: Sheets, Action sheets, Alerts, Modality.

<!-- visual:popovers -->
### What the illustrations show
Basis: 1 of 1 illustration sheet viewed, code checked; the page has no video.
- The opening diagram defines the canonical shape of the popover with no internal content: a translucent white rectangle with well-rounded corners with a small triangle at the top pointing to the origin, and measurement arrows marking total width at the base and total height on the right (img 0886).
- In macOS Calendar, the attached popover extends from the event's compact block through a small tip and sits beside it, without covering it, larger than the block of origin (img 0887).
- The attached popover has no title bar or close button; the content follows a hierarchy of the event name highlighted, full date and time, recurrence with icon, an action button and the guest list with green checks (img 0887).
- The detached popover becomes an independent panel: it loses the tip that connected it to the event, gains a title bar with a close X on the left and the title "Info" centered, and sits farther from the block of origin (img 0888).
- Between the two states the internal content remains identical; the only addition in the detached one is a "Show" button at the base of the panel (img 0887, img 0888).
<!-- /visual:popovers -->

## Scroll views (slug: scroll-views)

What it governs: a scroll view allows viewing content larger than the bounds of the view, moving the content vertically or horizontally.

Why: Apple treats scrolling as expected systemic behavior across all platforms, so the central guidance is to support the standard gestures and shortcuts rather than recreate custom behaviors. The scroll edge effect exists to visually separate floating elements (such as toolbars) from the content scrolling behind them, and it is not decorative: it exists to keep controls distinguishable, not to darken or block. Look to Scroll reflects the same principle of giving the person a choice (gesture or gaze) without replacing the standard behavior.

Do and avoid:
- Support the standard scrolling gestures and keyboard shortcuts; if you build custom scrolling, make sure the indicators use the expected elastic behavior.
- Make it apparent when content is scrollable, for example by displaying partial content at the edge of the view to indicate there is more in that direction.
- Avoid placing a scroll view inside another with the same orientation, as this creates an unpredictable and hard-to-control interface; it is acceptable to place a horizontal scroll view inside a vertical one (or vice versa).
- Consider supporting page-by-page scrolling when it makes sense for the content, defining the page size (typically the current height or width of the view) and, if desired, an overlap unit to maintain context.
- In certain cases, scroll automatically to help the person find their place: when an operation selects content or positions the cursor in a hidden area; when the person starts typing in a location that is not visible; when the pointer passes the edge of the view during a selection; when the person selects something and scrolls to a new location before acting on the selection. In all cases, scroll automatically only as much as necessary to maintain context.
- If you support zoom, define appropriate maximum and minimum scale values.
- Scroll edge effect: use the automatic style by default, which provides more opaque visual separation for top toolbars with many controls, text outside Liquid Glass controls and pinned table headers; if you use the soft style, test readability well across various contexts.
- Use scroll edge effect only when a scroll view is behind floating interface elements; it is not decorative, it does not block or darken like an overlay, it exists to keep controls visually distinct.
- Apply one scroll edge effect per view; in split view layouts on iPad and Mac, each pane can have its own effect, keeping consistent height between them for alignment.
- On iOS/iPadOS, consider showing a page control when the scroll view is in page-by-page mode; if you show a page control together with a scroll view, do not show the scroll indicator on the same axis, to avoid redundant controls.
- On macOS, a scroll indicator is commonly called a scroll bar; if necessary, use small or mini scroll bars in a panel, keeping the same size for all controls in that panel.
- On tvOS, views can scroll but are not treated as distinct objects with scroll indicators; when the content exceeds the screen, the system automatically scrolls the interface to keep focused items visible.
- On visionOS, the scroll indicator has a small, fixed size, appearing in a predictable location (centered vertically on the trailing edge during vertical scrolling; centered horizontally on the bottom edge of the window during horizontal scrolling). Looking at the indicator and starting a drag gesture enables a jog bar experience that allows manipulating scroll speed, revealing marks that accelerate or decelerate according to small adjustments in the gesture. Consider increasing margins if the content uses tight margins, so as not to overlap the indicator.
- Look to Scroll (visionOS): allows scrolling with just the eyes, starting when the person looks near the edge of the scroll view (top/bottom for vertical, sides for horizontal); it works alongside the existing behavior, so the person chooses gesture or gaze. Support Look to Scroll for reading or navigation views; avoid using it for secondary content with controls or dense information that requires precise, fast scrolling. Maintain consistency between similar views. Define clear scroll areas, preferring that the view occupy the full width or height of the window; if the view is inset from the window, provide clear boundaries. Remove custom scroll effects or animations (such as parallax) before supporting Look to Scroll, as they can cause unexpected behavior.
- On watchOS, prefer content with vertical scrolling, since the person is used to using the Digital Crown to navigate; if the app has a single list or content view, turning the Digital Crown scrolls vertically when the content is taller than the screen. Use tab views for page-by-page scrolling; if stacked vertically, the person can turn the Digital Crown to move vertically through full-screen pages, with a page indicator beside the Digital Crown. When displaying paginated content, consider limiting the content of an individual page to the height of one screen; for long pages, the Digital Crown can both navigate between short pages and scroll the content of a longer page, because the page indicator expands into a scroll indicator when needed.

Exact specifications: no number (pt, px, ms) is explicitly given in the text for dimensions or durations.

Platform differences:
- iOS, iPadOS: page control combined with scroll view, avoiding redundant indicator on the same axis; scroll edge effects.
- macOS: scroll bar as the term; small/mini scroll bars in panels; scroll edge effects.
- tvOS: automatic system scrolling to keep focused items visible, with no distinct indicators.
- visionOS: small, fixed-position scroll indicator; jog bar when looking and dragging; Look to Scroll.
- watchOS: vertical scrolling via Digital Crown; tab views for pagination; page indicator that expands into a scroll indicator.

Links to other articles: Page controls, Gestures, Pointing devices.

<!-- visual:scroll-views -->
### What the illustrations show
Basis: 1 of 1 illustration sheet and 2 of 2 sheets of the video hig-vid_scroll-views__041 viewed, all codes checked.
- The opening is decorative: a rounded image frame with sun and mountains, tinted orange-red, with a thin, dark vertical scroll bar in the top-right corner (img 0980).
- The hard edge effect appears in an iPhone app with a translucent top bar (back, "Title" and add) over a photo of a palm tree: the blur behind the bar is more opaque, with a dark, sharp top, and ends in a well-defined edge just below the bar (img 0981).
- The soft effect uses exactly the same screen and changes only the treatment behind the bar: the area becomes much lighter, with no defined opaque background, and the blur gradually dissolves into the content with no cut line, leaving the title and buttons almost floating over the photo (img 0982).
- The pair reuses the same screen, photo and controls and changes only the blur treatment, allowing a side-by-side comparison of the two edge styles in the same layout (img 0981, img 0982).
- In the video, a note from Notes floats in a 3D room in visionOS; from q001 to q003 it stays still at the top of the document and starting at q004 the content scrolls up, with title, paragraph and drawings exiting through the top in sequence (q005, q006) and a new drawing entering from the bottom at q007 (sheet 0001).
- The scroll goes past the end of the content: in q008 and q009, and still in q010 and q011, the board shows only a blank area; in q012 a block of text enters cut off by the top edge, in q013 and q014 leaf drawings appear, and in q015 the top of the document returns, until q016 and q017 become practically identical to q001 through q003 (sheets 0001 and 0002).
- A thin, translucent vertical mark next to the right edge of the board, consistent with a scroll indicator, appears in almost all frames with content from the first sheet, in all frames with content from the second, and also in the blank frames q008 and q009; in the still frames it is not possible to confirm distinct marks within it or measure a change in length or position of the stroke (sheet 0001 q001 to q009, sheet 0002 q012 to q017).
Recorded divergences: the section where the scroll passes through a blank area and returns to the top (q008 to q011) is not mentioned in the official description, which speaks only of the indicator reacting to the speed of the scroll.
<!-- /visual:scroll-views -->

## Sheets (slug: sheets)

What it governs: a sheet helps the person perform a limited task that is strongly related to the current context, such as providing specific information or completing a simple task before returning to the parent view.

Why: the article's central distinction is between modal and non-modal sheets: in macOS, tvOS, visionOS and watchOS the sheet is always modal, preventing interaction with the parent view until it is dismissed; in iOS and iPadOS it can be non-modal, affecting the parent view without closing. This flexibility in iOS/iPadOS exists because, on these platforms, the sheet can work as a tool for continuous editing (like the text formatting sheet in Notes) instead of just collecting a one-time input. The rule about never stacking sheets reflects Apple's general principle that the person should always know how to get back to where they came from.

Do and avoid:
- For complex or extended flows, consider alternatives to the sheet: in iOS/iPadOS, a full-screen modal view (for videos, photos, camera or multistep tasks); in macOS, consider opening a new window or full-screen mode; in visionOS, consider transitioning to a Full Space.
- Display only one sheet at a time from the main interface; if closing a sheet would lead back to another sheet, the person can get lost; if something inside a sheet results in another sheet, close the first before showing the new one, reopening it afterward if necessary.
- Use a non-modal view when you want to present supplementary items that affect the main task in the parent view; consider split view (visionOS) or panel (macOS); in iOS/iPadOS, use a non-modal sheet for this flow.
- Offer an alternative to the Done button: if you provide Done, always pair it with Cancel (to dismiss without confirming/saving) or Back (to return to a previous step); depending only on Done implies that completing the task is the only way out, which can seem restrictive or misleading.
- Avoid showing all three buttons together, Cancel, Done and Back.
- Common buttons: Cancel (or Close) dismisses the sheet without saving changes; Done dismisses after completing the task or saving explicitly; Back navigates to a previous step in a multistep flow or to a parent view in a hierarchy, without dismissing the sheet.
- In iOS/iPadOS, for single-view sheets, Cancel sits at the leading edge of the top toolbar; when present, Done sits at the trailing edge. In multistep flows, button position can vary between steps.
- Resizable sheets expand when the person scrolls the content or drags the grabber (the small horizontal indicator at the top of the sheet); they resize according to detents, heights at which the sheet naturally rests. System-defined detents: large (fully expanded height) and medium (about half of the fully expanded height). Sheets can have one or more custom detent values.
- Sheets automatically support the large detent; adding the medium detent allows resting at both heights, while specifying only medium prevents expansion to full height.
- In an iPhone app, consider supporting the medium detent to allow progressive disclosure of content; consider not supporting it when the content only makes sense at full height.
- Include a grabber in a resizable sheet: it shows that it can be dragged to resize, and the person can also tap to cycle through the detents; it works with VoiceOver to resize without seeing the screen.
- Support swiping to dismiss a sheet; the person expects this gesture instead of tapping a dismiss button; if there are unsaved changes, use an action sheet to confirm.
- In an iPadOS app, prefer the page or form sheet presentation styles, which use a standard size, centering the content over a darkened background.
- In macOS, the sheet is a card-shaped view with rounded corners that floats over the parent window; the parent window becomes darkened while the sheet is on screen, signaling that it cannot be used until the sheet is dismissed; however, the person expects to be able to interact with other windows of the app before dismissing the sheet.
- Present the sheet in a reasonable standard size in macOS, since the person generally does not expect to resize it, although in some cases it may be good to support resizing.
- Allow interacting with other windows of the app without first dismissing the sheet in macOS: when the sheet opens, the parent window (and its modeless document panels, if applicable) come to the front; make sure other windows of the app can also come to the front even with the sheet open.
- Use a panel instead of a sheet in macOS when the person needs to provide input repeatedly and observe results, such as a find and replace panel.
- In visionOS, the sheet floats in front of the parent window, darkening it and becoming the target of interaction. Avoid showing a sheet that emerges from the bottom edge of the window; prefer centering it in the field of view. Present it in a standard size that helps maintain context, avoiding covering most or all of the window, but consider allowing resizing.
- In watchOS, the sheet is a full-screen view that slides over the app's current content, semitransparent to help maintain context, with material that blurs and desaturates the covered content. Use a sheet only when the modal task requires a custom title or custom content presentation; if you need to give important information or present choices, consider Alert or Action sheet. Keep sheet interactions brief and occasional, using it only as a temporary interruption for an important task; avoid using it to navigate the app's content. If you change the default label, prefer SF Symbols to represent the action, avoiding a label that suggests hierarchical navigation or that looks like a page/app title, since the person would not know how to dismiss the sheet.

Exact specifications: the only values given are qualitative (large = fully expanded height; medium = about half of the fully expanded height); no number in pt, px or ms is provided in the text.

Platform differences:
- No additional considerations for tvOS.
- iOS, iPadOS: modal or non-modal; Cancel/Done/Back buttons positioned on the toolbar; detents (large, medium); grabber; swipe to dismiss; page/form sheet styles on iPadOS.
- macOS: always modal; card shape with rounded corners; parent window darkened but other windows of the app remain accessible; reasonable standard size, resizable when it makes sense; prefer panel for repeated input with observation of results.
- visionOS: always modal; floats in front of the window, darkening it; avoid emerging from the bottom edge, prefer centering; standard size that preserves context.
- watchOS: always modal; full-screen semitransparent view with blur/desaturation material; use restricted to tasks that require a custom title or presentation; label preferably in SF Symbols.

Links to other articles: Modality, Action sheets, Popovers, Panels.

<!-- visual:sheets -->
### What the illustrations show
Basis: 5 of 5 illustration sheets and 1 of 1 sheet of the video hig-vid_sheets__053 (frames q001 to q004) viewed, all codes checked.
- The opening sketch shows a desktop window with three circles in the top-left and a lighter sheet descending from the top of the window, with two-headed arrows in the four directions around it, which the notes read as measurement or the possibility of resizing (img 1029).
- In Notes on iPhone, the non-modal "Format" sheet occupies the bottom half over the note, which stays visible above; the sheet has a row of text style tabs, with the active one in orange, and two rows of icons for formatting, list, indent and alignment (img 1030).
- With another passage selected, the same open sheet now highlights the italic button in orange, that is, the state of the controls follows the selection in the parent view without the sheet closing (img 1031).
- Incorrect use, marked with a gray X: top of a sheet with grabber, centered title and only one blue confirmation button on the right, with no alternative way out (img 1032 with img 1033).
- Correct use, marked with a green check: gray cancel X on the left, title in the center and blue confirmation button on the right (img 1034 with img 1035).
- Pattern to avoid: back arrow on the left and, grouped on the right, the cancel X and the confirm check, bringing all three buttons together at once (img 1036).
- The multistep flow repeats the same composition and changes only two elements: first an X on the left with an inactive gray check, then a back arrow in place of the X with the check still inactive, and finally back with the check active in blue, a button state machine taught by comparison and not by annotation (img 1037, img 1038, img 1039).
- In the large detent, the crop shows the grabber and gray X just below the status bar and the rest of the screen blank, with the sheet occupying almost the entire visible area (img 1040); in the medium detent, the top half shows the view behind in gray and the bottom half is a white rectangle with rounded corners with a circular X in the top-left corner (img 1041).
- In macOS, the sheet is a card with rounded corners centered over the darkened Notes window, with a title, a list of three new features each with an icon, and a yellow "Continue" button in the bottom-right corner of the card (img 1042).
- In watchOS, the sheet is full screen over a blue-to-magenta gradient, with a translucent circular X in the top-left corner, the time on the right and a large pill-shaped button for the primary action at the bottom (img 1043); the variation swaps the X for a back arrow (img 1044), and the contrast between a "Title" text label in a pill in the top-left corner and the standard X illustrates the label that can look like hierarchical navigation (img 1045, img 1046).
- In the visionOS video, q001 shows only the translucent, blurred window over a 3D room; in q002 a gray rectangle with rounded corners appears in the center, more opaque and defined than the background, which grows in q003 and even more in q004, always centered and with no internal content, with the parent window blurred throughout the opening (0.0 s to 2.0 s).
- The opening in visionOS appears as scaling growth from the center, not as a rise from the bottom edge, and the room behind becomes less sharp after the sheet appears than in q001 (hig-vid_sheets__053).
Recorded divergences: img 1029 adds measurement or resizing arrows that the official description does not detail; in the video, the official description speaks of a blank window, but the background is a blurred living room with recognizable furniture.
<!-- /visual:sheets -->

## Windows (slug: windows)

What it governs: a window presents the views and UI components of an app or game; in iPadOS, macOS and visionOS, windows define the visual boundaries of the app's content, separate it from other areas of the system, and enable multitasking flows within and between apps.

Why: Apple distinguishes the primary window (navigation and main content, with associated actions) from the auxiliary window (a specific task or area, dedicated to one experience, with no navigation to other areas of the app, typically with a close button). This distinction guides when to open a new window: doing so helps multitasking and preserving context, but opening too many new windows creates confusion and makes navigation harder. The rejection of custom window UI follows the same principle as other components: system-provided windows are already recognized by the person, and replicating the appearance without perfection makes the app look broken.

Do and avoid:
- Make sure windows adapt fluidly to different sizes to support multitasking flows and multiple windows.
- Choose the right moment to open a new window: opening content in a separate window helps multitasking or preserving context (example: Mail opens a new window when composing, keeping the new message and the existing email visible at the same time); avoid opening new windows as default behavior, unless it makes sense for the app.
- Consider offering the option to view content in a new window, for example via a command in a context menu or in the File menu.
- Avoid creating custom window UI; system windows have recognizable appearance and behavior; do not create custom frames or controls, and do not try to replicate the system's appearance, because doing so without a perfect match makes the app look broken.
- Use the term "window" in content facing the person; the system refers to app windows as "windows" regardless of type; using other terms, including "scene" (which refers to the implementation), tends to confuse.
- In iPadOS, windows appear in two forms, depending on the choice in Multitasking & Gestures: full screen (the app fills the whole screen, and the person switches between apps or windows of the same app through the app switcher) or windowed (freely resizable, multiple simultaneous windows, repositionable and able to be brought to the front; the system remembers size and position even with the app closed).
- In iPadOS, make sure window controls do not overlap toolbar items; when in windowed mode, window controls appear on the leading edge of the toolbar; if the app has buttons on that edge, move them inward when the window controls appear.
- In iPadOS, consider allowing a gesture to open content in a new window, like the pinch gesture in Notes to expand an item into a new window.
- In macOS, the person generally runs several apps at the same time, seeing windows from multiple apps in the same workspace and frequently switching between them.
- Window anatomy in macOS: it consists of a frame and a body area; the person moves the window by dragging the frame and often resizes it by dragging the edges. The frame appears above the body area and can include window controls and a toolbar; in rare cases, the window can display a bottom bar, part of the frame that appears below the body content.
- Window states in macOS: Main (the front window the person sees is the app's main window; there can only be one main window per app), Key (also called the active window, accepts the person's input; there can only be one key window on screen at a time; although the main window of the foreground app is usually the key window, another window, like a floating panel, can be the key), Inactive (a window that is not in the foreground).
- The system gives different appearances to main, key and inactive windows to help identify them visually: the key window uses color on the title bar's close, minimize and zoom options; inactive windows and main windows that are not key use gray on those options. Inactive windows also do not use Materials (an effect that pulls color from the content behind the window), which makes them look more discreet and visually more distant.
- Some windows, typically panels like Colors or Fonts, only become the key window when the person clicks the title bar or a component that requires keyboard input, like a text field.
- Make sure custom windows use the appearances defined by the system, since the person relies on the visual differences to identify the foreground window and know which one will receive their input; with system-provided components, the window's background and button appearance update automatically when the state changes; with custom implementations, this work needs to be done manually.
- Avoid placing critical information or actions in a bottom bar, because the person often repositions the window in a way that hides its bottom edge; if you need to use one, use it only for a small amount of information directly related to the window's content or to a selected item in it (example: Finder uses the status bar to show the total number of items, selected items and available disk space); for more information, consider an inspector, typically presented on the trailing side of a split view.
- In visionOS, the system defines two main window styles: default (called window) and volumetric (called volume); both can display 2D and 3D content, and the person can see multiple windows and volumes simultaneously in the Shared Space and in a Full Space.
- There is also the plain window style in visionOS, similar to default, except that the vertical plane does not use the glass background.
- The system defines the initial position of the first window or volume the person opens in the app or game; both in the Shared Space and in a Full Space, the person can move windows and volumes to new locations.
- Default window in visionOS: it consists of a vertical plane that uses a non-modifiable Materials background called glass and includes a close button, window bar and resize controls; it can also include a Share button, tab bars, toolbars and one or more ornaments. By default, visionOS uses dynamic scaling to help the window's apparent size stay consistent regardless of the viewer's proximity.
- Prefer using a window to present familiar interface and support familiar tasks, reserving more immersive experiences for meaningful content and activities; if you want to show bounded 3D content like a game board, consider using a volume.
- Keep the window's glass background: it helps the content look like part of the environment, adapting dynamically to lighting, using specular reflections and shadows to communicate scale and position; removing it tends to make UI elements and text less legible and look less related to each other; an opaque background obscures the environment and can make the window look confining and heavy.
- Choose an initial window size that minimizes empty areas; by default, a window measures 1280x720 pt. When a window opens for the first time, the system positions it about two meters in front of the person wearing the device, giving it an apparent width of about three meters. Too much empty space inside the window can make it look unnecessarily large and obscure other content in the person's space.
- Aim for an initial shape that matches the window's content (example: a standard Keynote window is wide because slides are wide, while a standard Safari window is tall because web pages tend to be much longer than they are wide).
- Choose a minimum and maximum size for each window, to keep the content looking good at every size the person might choose when resizing.
- Minimize the depth of 3D content displayed in a window; the system adds highlights and shadows to the views and controls inside the window to give an appearance of depth; although it is possible to display 3D content in a window, the system clips it if it extends too far outside the window's surface; for content with greater depth, use a volume.
- Volumes in visionOS: display 2D or 3D content that can be viewed from any angle; they include window-management controls like a normal window, but a volume's close button and window bar change position to face the viewer as the person moves around it.
- Prefer using a volume to display rich 3D content; to present familiar, UI-centered interface, it is generally better to use a window.
- Position 2D content so it looks good from multiple angles inside a volume, since the person's perspective changes as they move; to attach 2D content to specific areas of 3D content inside a volume, you can use an attachment.
- In general, use dynamic scaling in volumes, to help content stay legible and easy to interact with even at a distance; if you want the content to represent a real object (like a product in a retail app), you can use fixed scale (default).
- The default baseplate appearance (the volume's horizontal "floor") helps the person perceive the volume's edges; starting with visionOS 2, the system automatically makes the baseplate visible with a soft glow around the edge when the person looks at it; if the content does not fill the volume, this glow helps indicate the edges, especially useful for keeping the resize control easy to find; if the content is full bleed or fills the volume's boundaries, or if a custom baseplate is displayed, the default glow may not be desired.
- Consider offering high-value content in an ornament; starting with visionOS 2, a volume can include an ornament in addition to a toolbar and tab bar, useful for reducing visual clutter and elevating important views or controls; when using an attachment anchor to specify the ornament's position (like `topBack` or `bottomFront`), it stays in the same position relative to the viewer's perspective as the person moves around the volume; avoid positioning an ornament on the same edge as a toolbar or tab bar, and prefer creating only one additional ornament so as not to obscure the volume's important content.
- Choose an alignment that supports the way the person interacts with the volume; as they move it, the baseplate can stay parallel to the ground of the environment, or it can tilt to match the angle the person is looking at; in general, a volume parallel to the ground works well for content with little interaction, while a volume that tilts with the gaze keeps the content comfortably usable even with the person reclined.

Exact specifications:
- visionOS: standard initial window size of 1280x720 pt; positioned about two meters in front of the viewer; apparent width of about three meters.

Platform differences: not supported on iOS, tvOS or watchOS.
- iPadOS: full screen mode (with app switcher) or windowed mode (freely resizable, position and size remembered by the system); window controls on the leading edge of the toolbar; pinch gesture to open in a new window.
- macOS: frame and body anatomy; frame with window controls, toolbar and, rarely, bottom bar; three window states (Main, Key, Inactive), each with a distinct appearance; use of Materials to differentiate states; recommendation against critical information in the bottom bar.
- visionOS: two main styles (default window with glass background, and volume) plus the plain window style; default window of 1280x720 pt at two meters of distance; dynamic scale; volumes with baseplate, adjustable alignment, ornaments and dynamic or fixed scale.

Links to other articles: Layout, Split views, Multitasking (and, within the text, references to Spatial layout, Materials, Depth, Immersive experiences).

<!-- visual:windows -->
### What the illustrations show
Basis: 3 of 3 illustration sheets viewed, all codes checked; the page has no video.
- The opening reduces the window to a silhouette with no content: three round buttons in the top left corner, translucent bubbles on the right side of the title bar and two-headed measurement arrows on the right and bottom edges for height and width, the only image on the page that communicates resizing by dimension (img 1324).
- On iPadOS, the same Notes document appears in full screen without a frame, without the Dock and without the Home Screen (img 1325), and in windowed mode as a rectangle with rounded corners and a shadow, centered over the wallpaper and with the Dock at the bottom; the three elements appear together or disappear together, and that is what distinguishes the two modes (img 1326).
- On macOS, three windows stacked diagonally receive labels that point to each state: the inactive one in the back, a Finder window with colorless window controls; the key window, the Colors panel with a color wheel and colored window controls; and the main window, the Notes one (img 1327).
- In this illustration the key window is the color panel, not the app's main window, and the differentiation between states relies on stacking depth and text labels, not only on color (img 1327).
- On visionOS, the abstract illustration distinguishes the two styles by shape: the window is a thin, double and tilted plane, in monochromatic blue with dashed outlines, and the volume is a translucent cube with dashed faces and a more solid bottom face, both over a thin bar (img 1328, img 1329).
- A real visionOS window floats over a room, with a glass background that lets the environment show through slightly; the content follows image at the top, title, subtitle and three columns of text, each with a title and a short paragraph (img 1330).
- In the window with 3D content, another screen from the same app carries a title, explanatory text on the left, a button and options at the bottom, and a rendered 3D satellite appears outside the window's rectangle, overlaid on the real scene (img 1331).
- The volume shows a 3D globe over the coffee table, side by side with a translucent window with text and a button, and a small control bar with four icons just below the globe, which puts window and volume coexisting in the same space (img 1332).
<!-- /visual:windows -->

## What this group reveals about the Apple way

1. The choice between alert, action sheet, sheet and popover systematically depends on who initiated the event and how much attention it deserves: alert for the unexpected or critical (alerts), action sheet for a choice resulting from an intentional action (action-sheets), sheet for a bounded task within the current context (sheets), popover for small, transient information (popovers). The same logic of "don't interrupt unnecessarily" appears in all four.
2. Apple treats interruption as an explicit and recurring cost throughout the presentation documentation: "use sparingly" appears almost literally in alerts, action-sheets and sheets, always justified by the same argument that the component takes the person out of the current task.
3. Stacking is treated as an orientation failure in several components: never a cascade of popovers, never show more than one sheet at the same time from the main interface (sheets), never show another view over a popover except an alert (popovers). The systematic pattern is to always keep the person with an obvious way back.
4. Several components reuse the same button logic: Cancel always on the least prominent side or position and never as the default button when there is a destructive action (alerts), always paired with Done or Back so it doesn't look like the only way out (sheets), present by default in confirmation dialogs (action-sheets).
5. The destructive button style follows a consistent and subtle rule between alerts and action-sheets: it marks an action the person did not deliberately choose, but it is removed once the person has already shown explicit intent (such as choosing "Empty Trash"), because in that case the button only fulfills the original intent.
6. Apple values stable, person-facing terminology: always use "window" instead of "scene" (windows), avoid the word "popover" in help documentation (popovers), refer to panels by their title without the word "panel" in menus (panels). In every case, the technical implementation term is hidden from the vocabulary facing the end user.
7. There is an implicit hierarchy of presentation "weight": popover and page control for small doses of temporary information; sheet for a bounded task; panel for macOS-specific persistent controls; window for the most complete and structured container. Each following level takes up more screen space and more permanence.
8. Platform adaptation follows a pattern of "convergence with particularity": almost all components exist on iOS/iPadOS/macOS with small variations, but each platform introduces its own interaction mechanic, coherent with its dominant paradigm: watchOS uses the Digital Crown and limits content to the screen height (page-controls, scroll-views, sheets); visionOS introduces depth, glass, ornaments and volumes (windows); tvOS eliminates distinct indicators in favor of automatic focus (scroll-views).
9. Purely decorative elements are explicitly rejected in favor of functional elements: the scroll edge effect "is not decorative" (scroll-views); color in HUDs should be used "sparingly" and only to highlight information (panels); page control indicators should not be colored, so as not to reduce functional contrast (page-controls).
10. Apple is consistent in prohibiting the recreation of system UI: do not create custom window UI (windows), make sure custom windows use system-defined appearances (windows), let the system automatically color the page control indicators (page-controls). The repeated justification is that replicating without perfection makes the app look broken or confuses the system's visual reading.
11. Several articles point to "Modality" as an umbrella concept (action-sheets, alerts, panels, popovers, sheets), confirming that Apple organizes this entire family of presentation components around a single central principle of modality, of which each component is a variation of scope and weight.
12. Changes in guidance over time (recorded in the change logs of alerts, scroll-views, sheets and windows) show recent and active evolution: scroll edge effect guidance (2025/2026), Look to Scroll on visionOS (2026), button guidance in sheets (2026) and resizable windows on iPadOS (2025), indicating that Apple keeps adjusting these presentation components together with broader system design changes, such as Liquid Glass.

## Reading evidence

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/action-sheets.md, 45 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/alerts.md, 81 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/page-controls.md, 68 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/panels.md, 43 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/popovers.md, 46 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/scroll-views.md, 82 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sheets.md, 96 lines read, yes, to the end.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/windows.md, 100 lines read, yes, to the end.

No file in the group is just a collection index page; all eight have complete text of their own.
