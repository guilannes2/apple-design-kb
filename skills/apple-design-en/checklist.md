# Review checklist against the Apple standard

Literal copy of section 7 of the essence (`kb-en/00_APPLE_ESSENCE.md`). Every screen produced or reviewed with this skill goes through these 38 questions before it is delivered. A "no" answer to any of them is a blocker, not a remark.

## Checklist for reviewing an interface against the Apple standard

Answer yes or no. Each question indicates the source that supports it.

Purpose and structure
1. Does each screen clearly answer "where am I", "what can I do" and "where can I go"? (`vid/15 wwdc2025_359`; `vid/03 wwdc2017_802`)
2. Does every feature present have a clear purpose for the person using it, and has what is not essential been cut or moved to progressive disclosure? (`hig/00 design-principles`; `vid/17 wwdc2026_250`; `hig/01 layout`)
3. Do the tabs represent the real hierarchy, with short, specific labels, with no actions in the tab bar and no generic tab that duplicates others? (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`)
4. Is push used to go down the hierarchy and modal only for a self-contained task, with a title that names the task and an obvious way out? (`vid/11 wwdc2022_10001`; `hig/03 modality`)
5. Is the content ordered by importance, from the top and the leading edge, and grouped by real behavior? (`hig/01 layout`; `vid/09 wwdc2021_10126`)
6. Does every action available in a gesture, a context menu or a hidden menu also exist in a visible place? (`hig/07 context-menus`; `hig/13 gestures`; `vid/09 wwdc2021_10126`)

System and platform
7. Were system components, symbols and behaviors used where they exist, and does each customization have an explicit reason? (`hig/03`, insight 4; `vid/03 wwdc2017_809`; `vid/17 wwdc2026_251`)
8. Does the layout use size classes, safe areas and margins, and keep the same functionality when the size changes, with no destructive changes? (`hig/01 layout`; `vid/15 wwdc2025_208`)
9. Was the interface designed for this platform, and not ported from another? (`vid/07 wwdc2020_10206`; `vid/02 wwdc2015_802`; `hig/15 mac-catalyst`)
10. On the Mac, is every command in the menu bar, with standard shortcuts, and do unavailable items appear dimmed? (`hig/07 the-menu-bar`, `toolbars`)

Content and brand
11. Is the content the dominant element, and does the brand live in the content layer, with no repeated logo and no brand launch screen? (`hig/01 branding`; `hig/03 launching`; `vid/17 wwdc2026_251`)
12. Is Liquid Glass only in the controls and navigation layer, with no glass over glass, no custom backgrounds in the bars and with the right variant? (`hig/02 materials`; `vid/16 wwdc2025_219`, `wwdc2025_356`)

Typography and color
13. Does the text use system text styles or a custom font with Dynamic Type, respecting the platform's default and minimum size? (`hig/02 typography`; `hig/01 accessibility`)
14. Does the interface stay legible, without truncating useful information, at the largest accessibility size? (`hig/02 typography`; `vid/05 wwdc2019_244`)
15. Does the contrast reach 4.5:1 for text up to 17 pt and 3:1 for text of 18 pt or bold, in light, dark and increased contrast modes? (`hig/01 accessibility`, `dark-mode`)
16. Does no information depend on color alone? (`hig/01 color`; `vid/05 wwdc2019_244`)
17. Are the colors semantic, with light, dark and increased contrast variants, and does the accent color appear only in primary actions and states? (`hig/01 color`, `branding`; `vid/15 wwdc2025_323`)

Interaction and feedback
18. Does every interactive target meet the platform minimum (44 x 44 pt on iOS, 60 pt on visionOS, 28 x 28 pt on the Mac) with adequate spacing? (`hig/01 accessibility`; `hig/07 buttons`)
19. Does every custom control have normal, pressed and disabled states, and does it respond immediately? (`hig/07 buttons`; `vid/03 wwdc2017_811`; `vid/04 wwdc2018_804`)
20. Do gestures follow the platform standard, can they be interrupted, and do they have a button alternative? (`hig/13 gestures`; `vid/04 wwdc2018_803`; `hig/01 accessibility`)
21. Do destructive actions use the destructive style, stay out of quick menus, and can they be undone or do they ask for confirmation when the loss is unexpected and irreversible? (`hig/03 feedback`; `hig/04 undo-and-redo`; `vid/07 wwdc2020_10205`)
22. Is progress determinate whenever possible, always moving and with an option to cancel? (`hig/11 progress-indicators`)
23. Does loading show something as soon as possible and never leave an empty screen? (`hig/03 loading`)
24. Do animations have a purpose, are they brief, do they respect Reduce Motion and do they avoid blocking the next action? (`hig/02 motion`; `hig/01 accessibility`)
25. Do haptics and sound follow documented meanings, are they synchronized with the visuals, are they rare and can they be turned off? (`hig/03 playing-haptics`; `vid/05 wwdc2019_810`; `vid/03 wwdc2017_803`)

Writing
26. Do buttons use specific verbs, without "Yes" and "No" and without an ambiguous "OK"? (`hig/02 writing`; `hig/09 alerts`; `vid/11 wwdc2022_10037`)
27. Do error messages stay near the problem, avoid blaming and say how to fix it? (`hig/02 writing`; `vid/03 wwdc2017_813`)
28. Has the text been read aloud and is it free of filler, repetition, jargon or implementation terms? (`vid/15 wwdc2025_404`; `vid/11 wwdc2022_10037`; `hig/15 healthkit`, `nfc`)
29. Are capitalization and terminology consistent, with a word list for the app? (`hig/02 writing`; `vid/15 wwdc2025_404`)
30. Do empty states say the next step, and does an empty search show the term that was searched? (`hig/02 writing`; `vid/17 wwdc2026_292`)

Responsibility
31. Are permissions asked for at the moment the feature needs them, with a specific purpose string, and only for what is necessary? (`hig/02 privacy`; `vid/03 wwdc2017_816`; `vid/07 wwdc2020_10162`)
32. Can the person use the app without an account until the account is essential, and can they delete the account inside the app? (`hig/03 managing-accounts`)
33. Do alerts and notifications have honest urgency, are they rare and actionable, and does the badge count only unread items? (`hig/03 managing-notifications`; `hig/09 alerts`; `hig/12 notifications`)
34. Do AI features indicate where there is AI, allow undo and redo, warn about errors and have safeguards against harm? (`hig/14 generative-ai`; `vid/17 wwdc2026_250`)

Accessibility and inclusion
35. Do all elements have descriptive VoiceOver labels, are decorative images excluded and is the reading order logical? (`hig/16 voiceover`; `vid/09 wwdc2021_10275`)
36. Do language, images, names and gender options include people, without stereotypes? (`hig/01 inclusion`; `vid/09 wwdc2021_10275`)
37. Does the app work with Switch Control, Voice Control, Full Keyboard Access and without depending on a single sense? (`hig/01 accessibility`; `vid/16 wwdc2025_316`)

Process
38. Has the interface been tested on the real device, in the real context and with people from the audience, without defending the design during the test? (`vid/02 wwdc2014_223`; `vid/03 wwdc2017_818`; `vid/16 wwdc2025_303`)
