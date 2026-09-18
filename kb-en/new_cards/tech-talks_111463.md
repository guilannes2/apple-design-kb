## Strike a pose with adaptive layouts on iPhone Duo (id: tech-talks_111463, 18.0 min)

Basis: transcript (frames not viewed yet). Local automatic transcript made with Whisper, it is not Apple's official one; proper names and terms may carry hearing errors. Source: https://developer.apple.com/videos/play/tech-talks/111463/.

Central thesis: On iPhone Duo, the hinge and the cameras create reserved regions, and good design depends on knowing when to adapt: move, resize or reorganize what already exists (the displacement pattern) to keep content and controls visible, reachable and unobstructed in any pose. For this, Apple presents the reserved regions API, for hand-built layouts, and the arrangements (split and overlay), layout containers for two views, always adapting only when it improves the experience.

The design process Apple describes:
1. Understand the device: several screens, each with its own size class, which should sound familiar to anyone who already designs for resizing; hardware features (the hinge and the two cameras of the external and internal screens) shape the available space and are called reserved regions, to be treated like any other area the layout already adapts to.
2. Understand each screen: on the external one, the camera is always present and system toolbars and tab bars are arranged vertically inside the new safe area; on the internal one, the interface can adapt to the fold or to the new FaceTime camera when active; with the device partially folded like a book, the fold divides the internal screen into several usable regions.
3. Know when to adapt: many interfaces flow naturally around the reserved regions; others call for an intentional approach, displacement.
4. Choose the scope of the displacement: from a button to an entire container or larger parts of the layout.
5. Decide where the element goes, guided by its purpose and by the device's pose (like a book or resting on a table), prioritizing what is contextual when more than one region serves.
6. Consider how the element adapts to the new surroundings: position and size are the most common changes, but other visual properties can also change.
7. Implement with the reserved regions API in SwiftUI or UIKit, querying division and occlusion regions, active or inactive.
8. Take advantage of the system components that already adapt to the fold and, for two-view layouts, use arrangements, choosing between split and overlay and recognizing when an arrangement is not the right tool.
9. Final preparation checklist: audit the app's centralized layouts; consider whether they can be turned into a two-column layout or which displacement pattern makes sense; use standard system containers and presentations, which bring a lot of behavior for free; in custom horizontal split or overlay layouts, consider the arrangement view to handle the layout on every supported device; identify the highest-priority controls positioned manually and adopt the Reserved Regions API for custom displacement where needed.
10. To use the hinge beyond layout, there is another API that responds to the fold state, covered in the session Leverage Multiple Displays and Scenes on iPhone Duo.

Principles stated and why:
- Content and controls that cross the fold behave like a photo spread across the two pages of a book. Why: near the spine, parts of the image become hard to see and it stops being read as a continuous image.
- On the internal screen, if the FaceTime camera viewfinder is central to the experience, keep important content and controls outside that area (the speech does not give a reason beyond that).
- Displacement adjusts the frame of existing elements according to the available space. Why: keep important content visible, reachable and unobstructed, even with the device partially folded.
- Choose the scope that matches the content: an element that adapts independently moves alone; elements that work together move together. Why: preserve the relationship between them.
- Be careful with excessive movement. Why: moving an element too far from its origin weakens the visual relationship between the two.
- Continuous scrolling content (articles, feeds, documents and lists) does not get displaced. Why: these experiences already adapt through scrolling, and moving them between regions can interrupt continuity.
- The purpose of the content decides where it goes, and that place can change as the device is used.
- With the device folded like a book, alerts go to the trailing side. Why: they end up closer to where they will appear when the device closes and the experience continues on the external screen.
- With the device resting on a table, the top region serves content that benefits from visibility at a distance, and the bottom one serves interactive controls. Why: the alert stays easy to find on top, and at the bottom the tappable elements have a more stable surface for touch.
- When several regions serve, prioritize the contextual one, as on iPhone the focused search sits above the keyboard (the speech gives the example, not a separate reason).
- Action sheets, alerts, menus and popovers are lightweight contextual experiences that can appear over a reserved region; the main goal is to keep them fully visible, and the system repositions them automatically.
- What all the examples have in common is moving, resizing or reorganizing what already exists; keeping content, functionality and layouts available. Why: people should have access to the full experience, whatever way they use the iPhone Duo.
- Inactive regions serve high-level decisions about the app, such as preferring an even number of columns in grids when there is a division region, active or not (the speech does not give the reason).
- When choosing an arrangement, follow first the patterns the app already uses. Why: HStack and VStack translate naturally into split, and ZStack into overlay, with built-in support for iPhone Duo.
- With no existing pattern, use overlay when there is a clear foreground and background relationship between the views. Why, in the example given: since the background content can be scrolled over the overlay, there is no problem with it being partially covered sometimes.
- Use split when the relationship is primary and detail. Why: it is important that neither of the two views is covered.
- Do not place navigation containers, such as Navigation Split View, inside an arrangement view. Why: arrangement views do not provide navigation infrastructure.
- Do not place arrangement views inside List and Scroll View. The reason given is just the nature of these scrollable views.
- Adaptive layouts should move, resize and adapt only when it makes the experience better, so the app feels designed for each pose.

Concrete interface-building techniques, with exact numbers when spoken:
- Numbers stated: 50/50 split of the columns in Reminders; the fold's division region, with the device open and flat, is inactive and has zero width; system-provided arrangements available in iOS 27.1; an arrangement organizes two views. The speech does not give point, margin or duration values.
- External screen: camera always present; system toolbars and tab bars arranged vertically inside the new safe area (refers to the session Raise the Bar with iPhone Duo).
- Basic displacement: an element centered with the device open moves, when folded, to the region that serves its purpose.
- Context menu: when selecting a photo in an album, instead of centering the menu in the trailing region, photo and menu move together and align around the fold.
- Search: with the device open, the field takes advantage of the extra space; when folded, width and position adapt to sit over the view being searched.
- System split view: keeps the two columns visible by adjusting the width and positioning them in a 50/50 split.
- Custom grid: preserve the outer margins and increase the spacing around the hinge, keeping each container within its region, so that all the grid items remain interactive when folded.
- Reserved regions in SwiftUI: query with a geometry proxy coming from a geometry reader or from the "non-geometry change modifier" (uncertain term in the automatic transcription), using the geometry proxy's new reserved region method to get the view's regions.
- Reserved regions in UIKit: reserved region method available on UIView.
- The frame property of a reserved region lets you incorporate it into your own layout.
- State: a region can be active or inactive; by default only the active ones are returned, and the inactive ones are obtained with the include inactive query option of the reserved region method.
- Division reserved region: represents the fold, because it divides a larger area into several smaller ones; it is only active when the device is folded.
- Occlusion region: does not divide areas, it occludes; it works as smaller frames inside the view's bounds. The FaceTime camera is an occlusion region, queried by passing the occlusion type to the reserved region method; it is active when the camera is active.
- System components that adapt to the fold: navigation containers such as navigation stacks, navigation split views and "tap views" (uncertain term in the automatic transcription); content containers such as List and Scroll View.
- Arrangements: layout containers positioned between the navigation ones and the content ones, which organize two views according to a set of rules. The inputs considered are the horizontal and vertical size class, the width-to-height ratio and the presence of active division regions; the outputs are whether the view appears and, if it appears, what its frame is. This function from inputs to outputs is the arrangement.
- SwiftUI: add an arrangement view inside the navigation stack, passing a primary view and a secondary one.
- UIKit: use UIArrangementViewController as the root view controller of the UINavigationController and configure the primary and secondary view controllers.
- Style: configured with the arrangement view style modifier; the default is split.
- Split arrangement: divides the bounds between the primary view and the secondary one; by default it splits horizontally when the view is wider than tall and vertically when it is taller than wide.
- Restricting axes: axes method of the split arrangement style. If the split cannot divide on the primary axis, the arrangement view shows only one view; in the example, with the view taller than wide and only horizontal division, only the player appears.
- UIKit for the same case: update arrangement method of the UIArrangementViewController with the UI split arrangement type configured with horizontal axis.
- Overlay arrangement: unlike split, which prefers side by side, it prefers to position the content with one view above or below the other; when the device is folded, it switches to preferring the primary and secondary side by side.
- Overlay Z-index in SwiftUI: overlay arrangement Z-index environment property, which changes as the device is folded and unfolded; in the example, used to switch between the collapsed and expanded version of the up next view.
- Overlay Z-index in UIKit: StateForViewPlacement method of the UIArrangementViewController and Z-index property of the returned state.

Examples cited:
- iPadOS window controls: an example of an area layouts already adapt to, of how reserved regions should be treated.
- A book with a photo spread across both pages: shows why content that crosses the fold loses readability.
- Photo album with a context menu: elements that work together move together and align around the fold.
- Alert in book pose (trailing side) and in resting-on-table pose (top region): the destination depends on how the device is used.
- Media controls in the bottom region with the device on the table: touchable controls gain a stable surface.
- Search field on iPhone and on iPhone Duo: prioritize the contextual.
- Reminders: the system split view adjusted to 50/50.
- Fitness design in a grid: outer margins preserved and greater spacing around the hinge.
- Grid with an even number of columns when there is a division region: use of inactive regions for high-level decisions.
- Podcasts app on iPad and on iPhone Duo: the transcript splits the layout in half; when hiding it on the folded iPhone Duo, the now playing view does not return to the center as on iPad and stays restricted to the left region defined by the fold, keeping the controls reachable and unobstructed; with the device rotated to portrait, there is no split and the transcript appears inline. It is also the example of a primary-and-detail relationship that calls for split.
- Harry's audio notes app, with player and up next: demonstrates split with a restricted axis, overlay with collapsed state and Z-index; the final answer is split, because the up next list details the playback state instead of being the player's background. In one passage the speech calls the app "Audio Node app" (uncertain term in the automatic transcript).
- Accessibility Reader: controls in the foreground and readable content in the background, a case of overlay.
- Sessions cited: Raise the Bar with iPhone Duo and Leverage Multiple Displays and Scenes on iPhone Duo.

Quotes:
"great design for iPhone Duo hinges on knowing when to adapt."
"Adaptive layouts help your app feel thoughtfully designed for every pose."
