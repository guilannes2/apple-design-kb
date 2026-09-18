# ess-07: recurring visual patterns (video batch)

Basis: 18 visual syntheses read in full, all from the visual_synthesis_videos directory. Each pattern below appears in at least two videos.

## The talk's index stays on screen as a progress marker, with hierarchy made only by color and opacity, the current item in full white and the rest in gray
- Evidence: wwdc2019_809 (agenda slide in two columns with ten topics, sheet 0006 q0047 to q0048, sheet 0013 q0112 to q0113, sheet 0016 q0144, sheet 0020 q0177 to q0178, sheet 0024 q0212 to q0213)
- Evidence: wwdc2020_10103 (menu in white text on black, "Ideation" on sheet 0003 q0019, "Principles" on sheet 0005 q0038, "Editing" on sheet 0006 q0051, "Creation" on sheet 0007 q0055)
- Evidence: wwdc2020_10171 (summary always in the same right corner over the blurred video, sheet 0003 q0026 and q0027, reappearing on sheets 0004 to 0010)
- Evidence: wwdc2020_10020 (recurring index screen always in the same vertical position, sheets 0002, 0003 q0019, 0010 q0090, 0011 and 0013)
- Evidence: wwdc2019_805 (agenda slide on black background, current item in bold white, sheet 0001 q0003 to q0009, reused in the "Summary" on sheet 0010)
- Evidence: wwdc2020_10162 (the list of three principles reappears overlaid on the presenter with only the item in focus in white, sheet 0002 q0018, sheet 0004 q0029, sheet 0005 q0039)
- What this teaches about building interfaces: progress state can be communicated without a badge, marker, numbering or bar, just by varying the opacity of the same text; and the block's fixed position on screen is what makes the reader recognize it as a compass rather than new content.

## Lists grow by accumulation between frames, with the item that just entered in strong white and the previous ones demoted to gray
- Evidence: wwdc2020_10019 (happens in "Switch Control users" sheet 0002 q0012 to q0015, "Special considerations" sheet 0004 q0033 to q0035, "Challenges for Switch Control" sheet 0007 q0056 to q0061, "Best practices" sheet 0011 q0094 to q0097)
- Evidence: wwdc2019_810 ("Utility" receives "Moderation", then "Focus", then "Keep it simple", sheet 0012 q0100 to q0105)
- Evidence: wwdc2019_809 (context menu recommendations are revealed one at a time, fading the ones already stated, sheet 0019 q0170 to q0171)
- Evidence: wwdc2020_10172 (summary lists grow line by line, four items on sheet 0012 q0104 to q0107 and four on sheet 0019 q0167 to q0170, never going beyond four simultaneous sentences)
- Evidence: wwdc2019_806 (bullets that accumulate next to the corresponding screenshot in the feature triage, sheet 0003 q0021 to q0026)
- What this teaches about building interfaces: progressive reveal does not need an entrance animation, a change in visual weight is enough; and the ceiling of four simultaneous lines is an observable density rule, not a preference.

## Design judgment is taught as a pair in the same frame, two versions of the same component varying one detail, one with a green check and the other with a red X
- Evidence: wwdc2020_10103 (two layout variations with stove burner holes sheet 0010 q0088 to q0089, two tip cards sheet 0012 q0100, and two note cards that differ only in whether the word appears before the time or not, sheet 0012 q0101)
- Evidence: wwdc2019_808 (grid labeled "fillColor" with a red X against the same grid with "systemGrey5" and a green check in the same frame, sheet 0007 q0056, and two modal cards of different heights with X and check, sheet 0018 q0160 and q0161)
- Evidence: wwdc2019_809 (four sidebar mockups over the wallpaper, each pair with a different selection color and a red X or green check below, sheet 0009 q0074 to q0075)
- Evidence: wwdc2019_806 (soup list with a repeated button on each row marked with a red X, sheet 0004 q0033 to q0036, against the status screen with a single button in the footer and a green seal, sheet 0005 q0038 and q0041)
- Evidence: wwdc2020_10145 (vertical list with a green checkmark seal on the approved term and a gray X on the rejected ones, applied to the service name sheet 0004 q0031, to the profile sheet 0006 q0054 and to the leaderboards sheet 0013 q0109)
- What this teaches about building interfaces: the difference between right and wrong becomes legible when only one variable changes between the two instances, and the verdict comes as a seal attached to the example, not as a separate caption.

## Measurement enters as graphic notation over the component itself, with numbers, thin lines and corner marks, and not only as a stated value
- Evidence: wwdc2020_10104 (two stacked toolbars with heights of 52 and 38 annotated on the left, sheet 0008 q0065 and q0066; thin yellow line crossing the frame at the label's height as a baseline guide for the slider, sheet 0015 q0131; typographic scale that gains yellow labels with the point size of each line, from 26 down to 10, sheet 0017 q0145 to q0146)
- Evidence: wwdc2020_10103 (thin purple lines with cross marks at the corners measuring the distance from the holes to the edge of the widget, comparing wide margin and tight margin, sheet 0010 q0089)
- Evidence: wwdc2020_10145 (horizontal color bands crossing the game screen with the numbers 62, 114 and 335 and then 280 and 91 overlaid, sheet 0003 q0019 to q0020; 512-pixel markings in height and width drawn around the circle over the card's own art, sheet 0008 q0070 to q0072)
- Evidence: wwdc2019_809 (typographic table with the macOS column at 13, 11 and 9 points next to the iOS column that starts showing the real values from 26.2 to 7.7 points when the label switches to a 77 percent scale, sheet 0012 q0101 to q0103; iPad Pro diagram with 2048 and 2736 pixels marked, sheet 0011)
- Evidence: wwdc2019_808 (RGB values and opacity percentage annotated per text layer, connected by a thin line to each element of the card, sheet 0004 q0033 to q0036)
- What this teaches about building interfaces: the specification lives glued to the pixel it governs, with an annotation color that does not exist in the real interface (yellow, purple, pink) so the markup is never confused with the design.

## The anatomy of a component is exposed by callout lines that name each zone over the mockup itself
- Evidence: wwdc2020_10172 (straight line and label in a white box pointing to "Title", "Subtitle", "Header" over the cover photo, "Action" on the blue button and "App" on the footer's attribution line, sheet 0010 q0087 to q0089, sheet 0011 q0092 to q0098, sheet 0012 q0103)
- Evidence: wwdc2020_10145 (callout lines labeled "Title" and "Description" pointing to each part of the achievement card, sheet 0009 q0076 to q0079)
- Evidence: wwdc2019_808 (the same card duplicated, the copy on the right receiving role names connected by a line to the elements, LabelColor, SecondaryLabelColor, SeparatorColor, SystemBackground, sheet 0005 q0042 and q0043)
- Evidence: wwdc2020_10162 (callout line pointing to the translucent white halo around the blue dot, sheet 0001 q0008, and another indicating that the distance and time next to the result depend on precise location, sheet 0002 q0010)
- What this teaches about building interfaces: naming a component's zones in the image creates shared vocabulary before any code, and the same drawing serves as a content contract for whoever fills each slot.

## Code appears paired with the screen it produces, growing line by line while the screenshot beside it does not change, with a highlight that moves within the block
- Evidence: wwdc2020_10093 (blocks grow from the isolated property to the function's complete signature, with constant syntax highlighting, property names in purple and values in red, sheet 0006 q0046 to q0051)
- Evidence: wwdc2020_10019 (on sheets 0007 to 0009 each Swift snippet appears beside the screen it affects, and the highlight moves from the whole block to the underlined class name and then to the assignment line, sheet 0009 q0076 to q0078)
- Evidence: wwdc2020_10104 (the code block grows from one to two and then four lines while keeping the same screenshot beside it, sheet 0003 q0019 to q0021)
- Evidence: wwdc2019_805 (the block grows in layers beside a card that does not change, first the intent creation and the donation, then the INImage lines, which reveals which addition produces the photo inside the suggestion circle, sheet 0007 q0058 to q0060)
- Evidence: wwdc2020_10020 (light gray rectangle covering only the snippet under discussion, moving from the standard font block to the accessibility size block while the phone screen changes along with it, sheet 0012 q0100 to q0103)
- What this teaches about building interfaces: the only honest way to show an API's cause and effect is to fix the result and vary the code, and the partial highlight is the reading cursor that says where to look at each instant.

## API novelty has its own seal, a green circle or label attached to the element or line that introduces it
- Evidence: wwdc2019_805 (green circular novelty seal over the mockup, both in the modal and in the gallery's detail view, sheet 0004 q0029 and sheet 0005 q0038)
- Evidence: wwdc2020_10019 (green label next to the line that sets the custom action's image via a system symbol, sheet 0009 q0078 to q0081)
- Evidence: wwdc2020_10020 (green circular seal in the top right corner of the announcement card when the API is new that year, sheets 0004 q0036, 0005 q0039, 0009, 0010, 0013, 0015 and 0016)
- What this teaches about building interfaces: a novelty marker works better anchored to the specific element than to the section title, and the same color reserved for that role avoids competing with the right and wrong seals.

## Emphasis among sibling elements is made by dimming the others, without changing the size, position or frame of any of them
- Evidence: wwdc2019_805 (of the three StickyNote cards, the one in focus keeps full color and the other two darken, sheet 0008 q0066 to q0067)
- Evidence: wwdc2020_10087 (list of eleven context triggers in two columns where only three remain in full white in the following frame, sheet 0004 q0031 to q0032; and forecast cards that fade while the relevant ones remain in full orange, sheet 0014 q0121 to q0125)
- Evidence: wwdc2020_10093 (in the three-row API table, the active row stays in saturated blue and the others are dimmed in dark gray, and the highlight moves from row to row, sheet 0004 q0035 to q0036, sheet 0005 q0037 to q0041)
- Evidence: wwdc2020_10172 (four store icons go from all white to only one in white with the rest grayed out, sheet 0006 q0049 to q0051)
- Evidence: wwdc2019_806 (the same text-authorship contrast made through opacity, the system's portion dimmed and the customized portion in full white, sheet 0013 q0117)
- What this teaches about building interfaces: filtering and focus can be expressed without reflow, which preserves the spatial memory of the viewer; changing opacity costs less attention than changing geometry.

## State is explained by two neighboring frames of the same screen, before and after, with no explanatory text between them
- Evidence: wwdc2020_10020 (the list of signs goes from names in colored text to the same list with a colored circular icon to the left of each name, keeping the color and adding the shape, sheet 0006 q0050 to q0053)
- Evidence: wwdc2020_10171 (the same Messages list without the blue pill and, in the next frame, with the full-width pill at the top pushing the list down, sheet 0010 q0088 to q0089; and the World Clock row partially shifted with the red button emerging from underneath, sheet 0005 q0044 to q0045)
- Evidence: wwdc2020_10162 (the sharp blue dot gives way to the blurred circular area in the same spot on the map, sheet 0003 q0022 to q0023; and the favorites row gains estimated time under each icon, sheet 0003 q0024 to q0026)
- Evidence: wwdc2020_10103 (the calendar card goes from one event to two and then to the message that there are no more events today, sheet 0003 q0025 to q0027; and the weather widget switches from light blue with sun to dark blue rain with a bar chart, sheet 0004 q0032 to q0034)
- Evidence: wwdc2020_10093 (the app background changes from dark to greenish when guide mode is activated and the stitch points accumulate along the dashed line, sheet 0014 q0119 to q0123)
- What this teaches about building interfaces: drawing the intermediate state and the final state side by side reveals what the transition needs to carry, and shows empty and exception states as part of the component, not as an afterthought.

## No screen appears as a raw capture: every interface comes inside a simulated device frame, with a fixed status bar
- Evidence: wwdc2020_10087 (iPhone frame with simulated status bar at 9:41, isolated on a black background when the point is the component and in the context of the lock screen, dock or home screen when the point is integration, observation consolidated in the synthesis and visible on sheet 0003 q0021 to q0024)
- Evidence: wwdc2020_10088 (every app or system screen inside a simulated iPhone or laptop frame, even when the content is just a menu or a notification)
- Evidence: wwdc2020_10172 (semitransparent iPhone mockup overlaid on a photograph of the physical context in a cafe, parking lot, store, restaurant and lookout point, sheets 0014 to 0016 q0119 to q0139)
- Evidence: wwdc2020_10171 (Watch screen mockups dominate sheets 0002 to 0012, including in the juxtapositions of two watches)
- What this teaches about building interfaces: the frame declares the real scale of the target and keeps the slide composition from being confused with the screen; and keeping the clock always at the same time eliminates an irrelevant variable from frame to frame.

## Side-by-side comparison in the same frame is the standard device for proving difference, whether between modes, sizes, devices or states
- Evidence: wwdc2019_808 (pairs of light and dark iPhone mockups with layer names linked to the exact areas, sheet 0006 q0048 to q0052; two iPhones labeled "Base" and "Elevated" with the second one lighter, sheet 0009 q0080)
- Evidence: wwdc2020_10145 (the same three-card structure repeated on phone, tablet, laptop and television within the same sheet, with the first card gaining focus highlight only in the TV version, sheet 0005 q0041 to q0042)
- Evidence: wwdc2020_10103 (compact weather with only the current condition next to the large weather with a six-day forecast, sheet 0009 q0080 to q0081; and summarized usage time next to the large version with hourly bars, sheet 0010 q0083 to q0084)
- Evidence: wwdc2020_10104 (three Mail windows with the same layout and increasing scales of text and icon, sheet 0018 q0157 and q0158; two sliders with and without tick marks, sheet 0015 q0128)
- Evidence: wwdc2019_806 (HomePod with a speech bubble next to the iPhone showing the visual version of the same question, sheet 0010 q0089 and q0090)
- Evidence: wwdc2019_809 (two instances of the same photos window, the inactive one with the sidebar losing sharpness and the active one sharp, with the labels swapping sides between frames, sheet 0008 q0070 to q0072)
- What this teaches about building interfaces: any decision about density, mode or platform must be evaluated with both versions visible at the same time, because the real difference only shows up in the juxtaposition.

## The same component template is reused across different apps and domains, and the app's identity enters only through the icon, the name and the color
- Evidence: wwdc2019_805 (the same action card appears in two different fictional apps with no variation in structure, sheets 0002 and 0008)
- Evidence: wwdc2020_10071 (the confirmation cards repeat a single template across domains, rounded corner sheet, title, body with the relevant data and two text buttons at the base, the neutral one on the left and the action one on the right, sheet 0003 q0024, sheet 0004 q0033, sheet 0005 q0042, sheet 0007 q0059)
- Evidence: wwdc2020_10172 (the Apple Pay checkout reappears with nearly identical composition in different contexts, sheet 0014 q0121, sheet 0015 q0134, sheet 0018 q0162; and the prompt to convert to the full app is the same horizontal card with icon, name, subtitle and button on the right)
- Evidence: wwdc2020_10145 (the three achievement types sit side by side and the difference lies entirely inside the central circle, lock, percentage ring and question mark, while title and description follow the same template, sheet 0008 q0067; and the same card translated into German keeps the identical layout, sheet 0009)
- Evidence: wwdc2020_10088 (the share menu appears with the same anatomy, circular avatars above the row of channel icons, anchored to a photos screen on an iPhone and then to a calendar window on a laptop, sheet 0003 q0022 to q0023)
- What this teaches about building interfaces: an app's personality must fit into the system's slots (icon, color, image, text) and not into redesigning the structure, and a layout that survives translation into another language is proof that the slots were sized correctly.

## Low fidelity comes before the real content: wireframe, labeled empty shape or pencil sketch occupying the place of the final screen
- Evidence: wwdc2020_10103 (empty rounded shape labeled "Small" and larger empty shape labeled "Large", each later replaced by the real filled-in widget, sheet 0007 q0059 to q0062, sheet 0008 q0064 to q0065; and a grid of empty rounded squares with two central slots outlined in thicker white, sheet 0007 q0058 to q0059)
- Evidence: wwdc2019_809 (low fidelity blue wireframe with rectangles marked with an X for content and thin lines for text, first with a single empty area and then with a side column and two areas, sheet 0011 q0094 to q0099)
- Evidence: wwdc2020_10071 (mockups with gray blocks and bars in place of real content, including a loading skeleton on the album screen and grid placeholders in search, sheet 0006 q0047 to q0052)
- Evidence: wwdc2020_10093 (pencil sketch on paper, iPad silhouette with keyboard, serving as background for the topic opening title, sheet 0002 q0010 to q0011)
- Evidence: wwdc2019_806 (the conversation script appears as a physical artifact, a typed sheet of paper that becomes two and then three overlapping sheets as more paths are considered, sheet 0009 q0074 to q0079)
- What this teaches about building interfaces: discussing fit, proportion and flow with the empty shape keeps the conversation from turning into a discussion about content, and the draft stage is shown as a legitimate part of the process, not hidden.

## The real tool appears on screen, with its color scheme and its panels, instead of an illustration of what the tool does
- Evidence: wwdc2020_10093 (Xcode in light theme with a file navigator on the left and a light pink band marking the recently edited area, present in every editor capture, sheets 0008 to 0010 and 0013 to 0015)
- Evidence: wwdc2020_10020 (Xcode's Asset Catalog with sidebar, central preview and attributes panel evolving from one symbol variant to two and then four, sheet 0008 q0070 to q0072 and sheet 0009 q0081; and the contrast calculator with swatches and RGB values, sheet 0009 q0074)
- Evidence: wwdc2020_10104 (Interface Builder with hierarchy, canvas and size inspector, sheet 0003 q0022 to q0027; object library with draggable items, sheet 0010 q0082 to q0084; asset catalog with the accent color square, sheet 0013 q0112)
- Evidence: wwdc2019_808 (symbol catalog app with names under each glyph, sheet 0016 q0136 and q0137, followed by a design tool with a layers panel where the five-star control is edited, q0138 to q0142)
- Evidence: wwdc2019_809 (real documentation pages open in the browser within the presentation and a design tool window with a component library in collapsible sections, sheet 0017 q0146, sheet 0024 q0209, sheet 0025 q0217 to q0219)
- What this teaches about building interfaces: showing exactly where in the application the adjustment happens shortens the distance between understanding and doing, and exposes details the speech never mentions, such as the recent-edit indicator in the editor.

## Box-and-line diagrams translate a code or context relationship into a drawing, before or alongside the concrete example
- Evidence: wwdc2020_10088 (a green bar labeled with an app action linked by a thin vertical line to a dark blue system bar, which in the next frame unfolds into three distinct action bars linked to the same bar, sheet 0002 q0013 to q0014)
- Evidence: wwdc2020_10087 (orange cards with day, time and location linked by a thin line to the corresponding iPhone screen, with both sides changing together between frames, sheet 0004 q0034 to q0036; and the intent card with three fields linked by a dotted line to the generated calendar screen, sheet 0015 q0129 to q0132)
- Evidence: wwdc2020_10093 (composition card with two light blue blocks joined by a plus sign, each with the corresponding line of code on the right, sheet 0006 q0053 and sheet 0007 q0055 to q0060)
- Evidence: wwdc2020_10104 (hierarchy of a window controller linking to a split view controller and to two view controllers, sheet 0003 q0026 and q0027; and an outer green rectangle with a lighter inner one and double arrows on the four edges, sheet 0011 q0098)
- Evidence: wwdc2019_805 (the output of an action drawn as a solid blue block with four stacked properties, linked to the source card by a simple vertical arrow, sheet 0008 q0067 to q0068)
- What this teaches about building interfaces: when the relationship between two things is the subject, the abstract drawing explains better than the real screen, and it can be reused later with the content swapped to prove that the rule is general.

## Components and glyphs are isolated on a black background, with nothing around them, when the subject is their anatomy
- Evidence: wwdc2020_10104 (pop-up button with blue fill, slider with a blue track before the indicator and gray after, and segmented control with the active segment in white over dark gray, sheet 0012 q0105 and q0106)
- Evidence: wwdc2020_10086 (Siri icon isolated on a black background, sphere with a radial gradient, sheet 0001 q0007 to q0008; and the share symbol in a thin white outline isolated beside the presenter, sheet 0002 q0017 to q0018)
- Evidence: wwdc2020_10171 (the menu the button opens is shown first in the context of the screen and then isolated on a black background, sheet 0006 q0053 and q0054, sheet 0007 q0057)
- Evidence: wwdc2019_808 (the group of standard controls, switch, stepper, segmented and slider, repeated in different framings with the slider in distinct positions, sheet 0012 q0104 to q0108)
- Evidence: wwdc2020_10071 (the three ways to trigger the assistant become three dark gray buttons aligned with equal spacing, centered white icon and caption below, with no other element over the black background, sheet 0001 q0009)
- What this teaches about building interfaces: taking the component out of context is what allows judging stroke weight, fill and internal spacing; the neutral black background prevents the color of the environment from contaminating the reading.

## Color carries a fixed role in the interface shown: blue for what is editable or actionable, red for destructive, green for confirmed
- Evidence: wwdc2019_805 (summary sentence with the parameters in underlined blue, and the field not yet filled in with a light gray background and dotted border, sheet 0002 q0013 to q0018)
- Evidence: wwdc2020_10171 (red reserved for the destructive on sheets 0005 and 0010, blue for the new message and purple for the new note on sheet 0002 q0012 and q0016, and the accepted option in green with a checkmark on sheet 0009 q0080 to q0081)
- Evidence: wwdc2019_808 ("Delete Draft" in red at the top of the action sheet, separated by a thin line, sheet 0018 q0158, with the destructive item in the context menu only getting red on sheet 0022 q0192)
- Evidence: wwdc2020_10087 (editable value in blue in the shortcut form, with a solid blue primary button in the footer, sheet 0009 q0073 to q0076)
- Evidence: wwdc2020_10162 (the controls tied to location use the system blue and the halo is translucent white, none of them using the yellow of category points or the colors of favorites, sheets 0001, 0003 and 0004)
- What this teaches about building interfaces: reserving colors by function, not by section, is what lets a new element be read without a caption; and a screen only achieves this if the other colors in circulation are kept out of that role.

## The button hierarchy is constant: filled for the primary action, plain text or neutral for the secondary, and full width when the button closes the screen
- Evidence: wwdc2020_10087 (solid orange primary button and text-only secondary button in the purchase confirmation, sheet 0003 q0021 to q0024)
- Evidence: wwdc2020_10071 (two text buttons at the base of the card, the neutral one on the left and the action one on the right, repeated across four different domains, sheets 0003 to 0007)
- Evidence: wwdc2020_10172 (filled blue pill on the card, with the label changing according to the type of experience but the design the same, sheet 0011 q0098 and sheet 0012 q0102; and the black payment button occupying the width of the footer, sheet 0014 q0121)
- Evidence: wwdc2019_806 (system form with a filled sentence field and a full-width blue button in the footer, sheet 0006 q0054 and sheet 0007 q0056)
- Evidence: wwdc2020_10020 (solid blue pill button as the primary call to action on the real product screen, with metadata in three columns below, sheet 0004 q0028 to q0034)
- What this teaches about building interfaces: the difference between primary and secondary is resolved by fill, not by a different color or size; and full width works as a signal that that button ends the flow.

## A single sentence gets its own card, large centered typography on a black background, with no other element
- Evidence: wwdc2020_10019 (card with a single sentence to fix the thesis that good screen reader support already delivers almost everything else, sheet 0005 q0040 to q0041)
- Evidence: wwdc2020_10162 (framing questions in large centered text over black, in two consecutive frames that change only the question, sheet 0002 q0014 to q0015)
- Evidence: wwdc2020_10171 (centered, standalone text card at the opening, sheet 0001 q0009, with the same type of sentence later migrating beside the watch mockup, sheet 0002 q0011 and q0012)
- Evidence: wwdc2020_10088 (data cards with a large number in bold white, much larger than the short centered caption below, always over the same blurred photograph, sheet 0004 q0031 to q0033)
- What this teaches about building interfaces: when a single statement needs to stay, it becomes the whole screen and loses all company; typographic scale alone does the work of emphasis.

## Conceptual text is overlaid directly on the presenter's video, with no background card, changing alignment according to the framing
- Evidence: wwdc2020_10086 (title sentences in white sans-serif typography over the live footage, switching between left and right alignment according to the pose of the person on screen, sheet 0001 q0006 to q0007, sheet 0002 q0014 to q0015, sheet 0003 q0020 to q0024)
- Evidence: wwdc2020_10088 (short white sans-serif words aligned to the right, one at a time as the speech advances, working as an emphasis caption with no separate slide, sheet 0001 q0009, sheet 0002 q0010 and q0011)
- Evidence: wwdc2020_10071 (block-opening words, two as an isolated card and two overlaid on the presenter's shot, with the card growing in two stages, the word in yellow and the rest in white, sheet 0002 q0017 to q0018, sheet 0008 q0068, sheet 0009 q0076)
- Evidence: wwdc2019_810 (the concept word in a large size overlaid in transparency on the presenter and the mockup, sheet 0008 q0066 and q0067)
- What this teaches about building interfaces: translucent overlay keeps the context alive behind the text, and text alignment becomes a function of the image composition, not a constant of the template.

## The presenter coexists with the interface in the same frame, as a thumbnail in the corner or in a split frame, instead of cutting between one and the other
- Evidence: wwdc2020_10071 (from the middle of the video onward, the editing starts using a split frame, a small portrait of the presenter in one corner and the enlarged iPhone screen beside it, sheet 0006 q0047 and q0048, sheet 0008 q0064 to q0066, sheet 0009 q0078 and q0079)
- Evidence: wwdc2020_10093 (title slide with a video thumbnail of the presenter in the bottom right corner, sheet 0001 q0001 to q0009)
- Evidence: wwdc2020_10162 (the presenter appears several times only as a thumbnail in the corner over the screen)
- Evidence: wwdc2020_10104 (in the opening and closing cards, the presenter appears in a video window in the corner, not alone in the whole frame, sheets 0001 and 0021)
- Evidence: wwdc2019_805 (the presenter appears almost always as an overlaid thumbnail or beside the enlarged screen)
- What this teaches about building interfaces: keeping the human source and the artifact visible at the same time avoids losing context from the cut, and the corner occupied by the thumbnail becomes reserved space that the screen layout needs to respect.

## A change of presenter and setting signals a block change before any card
- Evidence: wwdc2020_10087 (four presenters, each in their own location, from the indoor studio to the outdoors with a road and to the glassed-in hallway, with each change of face and setting anticipating the change of subtopic, sheets 0006, 0012 and 0015, in the transitions q0051 to q0052, q0102 to q0103 and q0134 to q0135)
- Evidence: wwdc2020_10172 (the first presenter stays in a white studio with armchairs and an orange pouf on sheets 0001 to 0012, and the second presenter appears in a glass setting with natural light, opened by a black card with a name credit and a video thumbnail in the corner, sheet 0013 q0109 to q0110)
- Evidence: wwdc2020_10145 (the video alternates close-up segments of the two presenters between the game screens and the specification slides)
- What this teaches about building interfaces: a change of context can be announced by a constant environmental variable, not by a label; the viewer notices the turn before reading anything.

## Real photography of hardware, of a person or of an environment comes in as an argument, not as decorative illustration
- Evidence: wwdc2019_810 (the haptic engine photographed inside the open iPhone with a label overlaid on the component, sheet 0002 q0011 to q0016; and macro shots of golden watchmaking gears leading to the close-up of the knurled crown with a red ring, sheets 0009 and 0010 q0080 to q0086)
- Evidence: wwdc2020_10019 (documentary sequence of the user in a motorized wheelchair traveling the trail to the waterfall, close-up of the mouth switch and the iPhone camera viewfinder, sheet 0003 q0019 to q0025; and a hand pressing two labeled buttons beside the running game, sheet 0010 q0082 to q0085)
- Evidence: wwdc2020_10172 (the code printed on a white triangular totem on the table of a real coffee shop, sheet 0005 q0040 to q0045, and mockups placed over photos of physical context, sheets 0014 to 0016)
- Evidence: wwdc2020_10020 (the star map screen appears being held and tilted in a person's hand to demonstrate the movement effect, sheet 0013 q0114 to q0116)
- What this teaches about building interfaces: when the decision depends on material, physical force or a situation of use, the real-world image proves what no diagram proves, and shows the concrete constraint the interface needs to respect.

## A dashed outline is the convention for marking what is an area, region or empty space, never a solid interface element
- Evidence: wwdc2020_10093 (dashed-border frame overlaid on real screenshots, first covering all the content to explain the default region and then limited to a horizontal band for the custom region, sheet 0011 q0099 and sheet 0012 q0101 and q0102, with the same marking in yellow around a continuous row of samples on sheet 0017)
- Evidence: wwdc2019_805 (parameter not yet filled in with a light gray background and dotted border around the text, marking the field as editable and empty with no extra label, sheet 0002 q0013 to q0014)
- Evidence: wwdc2020_10172 (the App Clip icon is the app's normal icon with a dashed circular border added around it, shown in a labeled side-by-side comparison, sheet 0002 q0017 to q0018, and repeated in the final icon of the closing, sheet 0019 q0170)
- What this teaches about building interfaces: the dashing communicates a boundary without suggesting a surface, which makes it suitable for both an empty field and a capture area, and it is this absence of fill that prevents confusing it with a control.

## Gesture and touch area are annotated as a translucent circle with an arrow, including the middle of the movement and not just the result
- Evidence: wwdc2019_808 (the gesture of dismissing the sheet annotated frame by frame with a semi-transparent blue circle and arrow that changes position over the scrollable text, showing scroll and dismiss as two steps of the same pull, sheet 0018 q0154 to q0156)
- Evidence: wwdc2019_809 (a blue button surrounded by a translucent circle larger than the control itself representing the touch area, with a small button and mouse cursor right below, sheet 0004 q0031 to q0032; and the remapping in pairs, blue circle next to the arrow cursor, sheet 0015 q0131 to q0135)
- Evidence: wwdc2020_10171 (the list appears with the row partially shifted and the red button emerging from underneath, recording the middle of the gesture and not just the result, sheet 0005 q0044 to q0045)
- Evidence: wwdc2019_806 (arrow with a label pointing to the entire card to specify that it is a single button, with the camera zooming in until the annotation fills the screen, sheet 0014 q0122 to q0125)
- What this teaches about building interfaces: the tappable area is larger than how the control is drawn and needs to be specified as such, and showing the gesture's middle frame is what reveals whether the feedback during the movement was designed.

## The same brand vignette opens and closes, and the closing piece repeats the opening one exactly
- Evidence: wwdc2020_10019 (still of the laptop with stickers and the animated avatar beside it in the opening, repeated after the event logo in the closing, sheet 0001 q0002 and q0003, sheet 0013 q0109 to q0111)
- Evidence: wwdc2020_10071 (the same laptop lid with stickers filmed from two angles in the opening and in close-up in the last frame, sheet 0001 q0002 and q0003, sheet 0009 q0081, sheet 0010 q0082)
- Evidence: wwdc2020_10103 (the brand frame with the closed laptop and event logo on sheet 0001 q0002 to q0004 and again on sheet 0012 q0103 to q0105)
- Evidence: wwdc2020_10162 (the same laptop composition with stickers on sheet 0001 q0001 to q0003 and on sheets 0006 and 0007)
- Evidence: wwdc2020_10086 (the same piece filmed from two different angles, with the closing repeating the composition used in another video from the same batch, sheet 0001 q0002 and q0003, sheet 0006 q0046 to q0048)
- What this teaches about building interfaces: an identical frame at both ends closes the piece and creates recognition among items in the same series, with zero production cost because it is literally the same material.

## System symbols are treated as typography, with uniform stroke weight, a grid by category and a scale test next to a letter
- Evidence: wwdc2019_808 (a wall of glyphs in perspective and then a frontal grid organized by category with uniform stroke weight, sheet 0015 q0127 and q0128; and the share symbol used as a proof body for alignment with text, with a blinking cursor beside it and repetition in growing sizes, q0130 to q0135)
- Evidence: wwdc2020_10020 (a dense grid of black and white symbols organized in rows by theme, all with the same weight and regular alignment, and a test board on a white background with a reference letter on the left and the same symbol repeated in three growing sizes per row, sheet 0005 q0042 and q0045)
- Evidence: wwdc2020_10104 (a yellow label pointing to a toolbar icon with size in points, weight and scale written out, sheet 0018 q0155 and q0156; and two boxes overlaid on the same glyph, a yellow one covering the entire image area and a smaller blue one inside it, separating the total rectangle from the alignment rectangle, sheet 0020 q0172)
- What this teaches about building interfaces: a symbol has its own metrics (weight, scale, alignment box) that need to be matched with those of the neighboring text, and the test next to a reference letter is the simple method for checking this at each size.

## Single-source findings

- Typographic scale between platforms resolved by a single factor: the macOS column with 13, 11 and 9 points next to the iOS column that only gets values when the label turns into a 77 percent scale, with 26.2 on the large title and 7.7 on the smaller caption, and the same scale then demonstrated inside a design tool with the width and height indicators at 77 percent (wwdc2019_809, sheet 0012 q0101 to q0108). The emphasis then shifts to the smaller styles, marking in bold exactly the sizes treated as risky (sheet 0013 q0110 to q0111).
- Toolbar height given as a number in the comparison itself, 52 for the unified style and 38 for the compact one, with visibly larger icons in the first (wwdc2020_10104, sheet 0008 q0065 and q0066).
- Text opacity scale in four stacked levels, title, subtitle, placeholder and disabled, each line visibly lighter than the previous one and always in the same order across different sheets (wwdc2019_808, sheet 0005 q0045 and sheet 0006 q0046 and q0047).
- Background hierarchy with layer names annotated over the screen, base, secondary and tertiary in the simple list, and the grouped variant with its own two levels, all in a pair of light and dark mockups (wwdc2019_808, sheet 0006 q0048 to q0052).
- Four levels of translucent material over an orange gradient background, with part of the cards erased in successive frames to make the opacity gradation visible, and then filled in with vibrancy labels at four levels for text and fill (wwdc2019_808, sheet 0011 q0092 to q0099).
- Elevated surface tone proven by comparison: the iPad's right panel darkens in two steps as it gains a divider, two iPhones labeled base and elevated with the second one lighter, and the slide-over app lighter than the background app (wwdc2019_808, sheet 0009 q0077 to q0081).
- Contrast test shown as a measurement with a number on screen: two panels, light and dark, each with the ratio beside it, the failing value crossed out with a red X and the passing one with a green check (wwdc2019_808, sheet 0008 q0066 to q0069).
- Contrast calculator in macOS style with text and background swatches, RGB values below each one, a text size control and the large result of 4.5 to 1 with a yellow triangular badge stating which sizes and weights that ratio meets (wwdc2020_10020, sheet 0009 q0074 and q0075).
- Vision loss spectrum demonstrated with four columns of the same photograph treated with progressive filters, from the sharp image to the fully dark one, and the no-vision column getting highlighted only by a white outline because there is no content to highlight (wwdc2020_10020, sheet 0001 q0009 and sheet 0002 q0010).
- Graphic notation invented for what cannot be seen: continuous sine wave, single transient peak, the same transient reduced to a solid blue rectangle and three shapes that form the sharpness spectrum, rounded drop, bar and triangle, reused as a fixed system throughout the entire video (wwdc2019_810, sheet 0003 q0019 to q0026, sheet 0013 q0111, sheet 0015).
- Two tracks aligned on the same time axis, sound above and haptic response below, with a thin red vertical line marking the reference point, a feature repeated on sheets 0006, 0013, 0014 and 0015 (wwdc2019_810).
- Cartesian axes with intensity from 0.0 to 1.0 on the vertical and sharpness from 0.0 to 1.0 on the horizontal, with the three shapes positioned along the sharpness axis (wwdc2019_810, sheet 0013 q0110 and q0111).
- Masking effect shown as an on-screen fact: four vertical bars of slightly different heights and, in the following frames, the first bar darkening and losing visual weight relative to the other three (wwdc2019_810, sheet 0014 q0123 to q0125).
- Prototype reduced to a minimum to test harmony: an iPhone frame with a single small ball falling from the center to the bottom, flanked by two fixed columns where the real-world column already carries complete visuals, sound and touch and the digital-world one gains these items one by one (wwdc2019_810, sheet 0007 q0057 to q0063).
- Asset specifications always in the same three-line format over a blurred video, with the 2x dimension in a bolder weight: 1846 by 300, then 512 by 512 at 1x and 1024 by 1024 at 2x, then 659 by 371 and 1318 by 742 (wwdc2020_10145, sheets 0006 q0048, 0009 q0075 and 0011 q0098).
- Three-column decision table mapping usage context to the corresponding code value, with the situation headers on top and the value below, in a quick-reference format, and the caveats appearing only in the following frame (wwdc2020_10104, sheet 0016 q0140 and q0141).
- Discouraged practice marked with a circular red X in the corner of the slide with no correct counterpart beside it, including in a code block whose own on-screen comment warns of the blurred result (wwdc2020_10104, sheet 0008 q0066 to q0069 and sheet 0020 q0173 to q0175).
- Category grid differentiated by icon shape and color, translucent gray circle, orange diamond, black octagon and red diamond, in two rows of four with a small label below (wwdc2019_805, sheet 0006 q0052 to q0053).
- Chaining between actions shown as a transformation of the field itself: the parameter goes from a generic placeholder to a named blue variable chip, while the editor beside it shows the corresponding field with a green frame and help text (wwdc2019_805, sheet 0009 q0079 to q0081).
- Accepted synonyms growing as a second italic line under each option on the card, longer with each frame (wwdc2019_806, sheet 0011 q0093 to q0095).
- Text authorship marked in the image by labels pointing out which part of the sentence is written by the developer and which comes from the system category (wwdc2019_806, sheet 0013 q0116).
- Excessive greeting demonstrated through visual repetition: the phrase marked with an X and then repeated in faded copies around it to simulate the effect of hearing it many times (wwdc2019_806, sheet 0015 q0127 and q0128).
- Bar of time-of-day icons, sunrise, car, sun and bed, in which the active icon changes and the featured widget follows along, from weather to music and then news (wwdc2020_10103, sheet 0002 q0011 to q0014).
- Widget spatial fit shown literally with a grid of empty rounded squares representing home screen icons, two center slots outlined in a thicker white, before the grid disappears and only the small-size shape remains (wwdc2020_10103, sheet 0007 q0058 to q0059).
- Mind-map-style diagram in the closing, growing from almost invisible icons and resolving by connecting panel, profile, rankings, achievement cards, friends, multiplayer and store to a colored central icon, an information architecture that no single screen showed before (wwdc2020_10145, sheet 0015 q0127 and q0128).
- Approximate location drawn without a new symbol, as a large blurred, translucent circular area occupying the center of the map in the same place where the sharp point would be, disappearing when the map is zoomed in very close and leaving only the small control in the corner (wwdc2020_10162, sheet 0003 q0022 to q0023 and sheet 0004 q0035 to q0036).
- Exception communicated inside a standard list item without changing the others: only the current-location option gets a short note below the name, the other suggested places stay without a note (wwdc2020_10162, sheet 0005 q0044 and q0045).
- Validity window annotated graphically over a standard notification, clock icon with a circular arrow plus the duration text, then isolated full screen over a black background (wwdc2020_10172, sheet 0018 q0154 to q0157).
- What should be left out of a lightweight experience is shown as exclusion cards with an X in a gray circle, each paired with a screenshot of the screen to be cut, introductions, login and accounts, tab navigation (wwdc2020_10172, sheet 0017 q0147 to q0151).
- Several lock screens overlapped in a fan, like stacked cards, gaining a new notification with each frame, to show accumulation of cases without needing separate screens (wwdc2020_10088, sheet 0003 q0025 to q0027).
- Recent-edit indicator visible in every screenshot of the editor, a light pink band marking the recently changed area, a detail that no speech mentions (wwdc2020_10093, sheets 0008 to 0010 and 0013 to 0015).
- Slide footer with a divider line, session title on the left and event acronym on the right, present in the slides and never spoken (wwdc2020_10093, sheet 0005).
- Pointer changing shape depending on the context within the same app, translucent pink circle over the central area and a crosshair in the following frame, in the same position (wwdc2020_10093, sheet 0011 q0092 to q0093).
- Click area of a control with no visible border suggested by a highlight rectangle that outlines a group of toolbar buttons (wwdc2020_10104, sheet 0007 q0062 and q0063).
- Window focus state proven by side-by-side comparison, the inactive instance with the sidebar losing sharpness and marked with a pink circle with an X, the active one sharp with a green circle, and the labels switching sides between frames (wwdc2019_809, sheet 0008 q0070 to q0072).
- App icon treated as a problem of shape and resolution: an empty white squircle mold inserted in the middle of a row of real icons and then isolated over a checkered background, and the same colored icon side by side, simplified at 16 by 16 pixels against the detailed full-resolution version (wwdc2019_809, sheet 0017 q0148 to q0153 and sheet 0018 q0155 to q0158).
- Menu bar broken down as a cataloging exercise, a two-column table of object and action, followed by the real bar with each menu opened in sequence, and menu stability illustrated by two instances of the same menu side by side, one with no selection and the other with the item selected (wwdc2019_809, sheets 0021 q0183 to q0189 and 0023 q0203 to q0204).
- Top-level menu of the accessibility system shown already with icons applied, a horizontal submenu of four icons with a short caption next to the code that defines them (wwdc2020_10019, sheet 0009).
- Scanning cursor focus with a fixed convention across the screenshots, a solid blue outline rectangle around the element, shifting position between neighboring frames to indicate advancement (wwdc2020_10019, sheet 0007 q0056 to q0057, sheet 0008 q0068 to q0069, sheet 0010 q0084 to q0085).
- High-contrast symbol variant organized in the asset catalog, evolving from a single variant to two stacked ones and then four combining luminosity and contrast level, each with its own tone (wwdc2020_10020, sheet 0008 q0070 to q0072 and sheet 0009 q0081).
- List cell that changes arrangement as the text grows, going from a symbol and name side by side, centered, to stacking the symbol above the left-aligned name, with far fewer items visible per screen (wwdc2020_10020, sheet 0012 q0100 to q0103).
- System settings panel overlaid on the left of the same screen as the affected app, showing configuration and effect in the same frame (wwdc2020_10020, sheet 0014 q0119 to q0120).
- A card in the series breaking its own template, appearing first with only text and no code block, unlike all the others, and only afterward gaining the version with code (wwdc2020_10020, sheet 0015 q0132 and sheet 0016 q0137).
- Contrast in treatment between informational and actionable content on the same screen: the note sits directly on the black background with no container, while the destructive action sits inside a dark rectangular container with red text (wwdc2020_10171, sheet 0010 q0084).
- A gesture that does not translate between platforms marked with an explicit alert, a pull-to-refresh indicator accompanied by a yellow exclamation circle, and the cursor's gain shown in two stacked charts, one pointed to by touch and the other by cursor at the same data point (wwdc2019_809, sheet 0016 q0139 to q0143).
- Pair of complementary animation methods shown as two nearly identical code blocks that swap between each other, entry with opacity zero and exit with opacity one, each with its own comment (wwdc2020_10093, sheet 0017 q0151 to q0152).
- Leaderboard embedded in the game as a compact side panel with a map thumbnail and numbered list, with the player's own row highlighted at the bottom of the list even while outside the top (wwdc2020_10145, sheet 0012 q0105 to q0107).
- Scene transition made only by fully darkening the frame, with no title card and no cut, different from all the other transitions in the same video (wwdc2020_10071, sheet 0007 q0062).
