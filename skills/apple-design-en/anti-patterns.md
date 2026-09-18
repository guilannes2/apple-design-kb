# Anti-patterns Apple explicitly condemns

Literal copy of section 6 of the essence (`kb-en/00_APPLE_ESSENCE.md`). Each item cites the card that supports it: `hig/NN slug` is a file in `kb-en/hig/`, `vid/NN id` is a file in `kb-en/videos/`. None of these patterns may enter an interface made with this skill.

## Anti-patterns Apple explicitly condemns

Structure and navigation
1. Hamburger menu to hide the main navigation (`vid/03 wwdc2017_802`; `vid/09 wwdc2021_10126`; `vid/15 wwdc2025_359`).
2. Hiding, disabling or switching tabs automatically; using the tab bar for actions; a generic "Home" tab that duplicates other tabs (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`; `vid/04 wwdc2018_802`).
3. Modal used because the animation is pleasing, modal that becomes an "app inside the app", stacked modals, more than one alert at the same time (`vid/05 wwdc2019_808`; `hig/03 modality`; `hig/09 sheets`, `popovers`; `vid/11 wwdc2022_10001`).
4. Putting all of a view's actions behind a single button or hiding a primary action in a "More" menu (`hig/07 pull-down-buttons`; `vid/07 wwdc2020_10205`, `wwdc2020_10171`).
5. Leaving the only way to do something in a gesture, in a context menu, in a dynamic menu with a modifier key or in a nearby interaction (`hig/07 context-menus`, `the-menu-bar`; `hig/13 gestures`, `nearby-interactions`; `vid/09 wwdc2021_10126`).
6. Hiding unavailable menu items in the menu bar instead of dimming them (`hig/07 the-menu-bar`; `vid/15 wwdc2025_208`).
7. Nesting scroll views in the same orientation (`hig/09 scroll-views`).

Interface and system
8. Recreating system components (windows, context menus, video player, purchase confirmation) without need; the imperfect replica looks broken or dated (`hig/09 windows`; `hig/03 playing-video`; `hig/15 in-app-purchase`; `vid/05 wwdc2019_808`; `vid/17 wwdc2026_251`).
9. Redefining standard gestures and shortcuts for other functions, or inventing a new gesture for a standard action (`hig/13 gestures`, `keyboards`, `pointing-devices`; `hig/04 undo-and-redo`).
10. Liquid Glass in the content layer, glass over glass, mixing Regular and Clear variants, custom backgrounds in bars (`hig/02 materials`; `vid/16 wwdc2025_219`, `wwdc2025_356`; `vid/15 wwdc2025_284`; `vid/00 meet-with-apple_256`, nested glass).
11. Scroll edge effect as decoration or where there is no floating interface (`hig/09 scroll-views`; `vid/16 wwdc2025_356`).
12. Custom button with no pressed state; buttons that do not look like buttons; button shape on content that is not clickable (`hig/07 buttons`; `vid/02 wwdc2015_805`).
13. Primary role on a destructive button; Cancel as the default button in a destructive alert (`hig/07 buttons`; `hig/09 alerts`).
14. Destructive actions in quick menus with no confirmation somewhere else (`vid/07 wwdc2020_10205`).
15. Pointer with magnetism without a custom shape; decorative pointer effects; instructional text next to the pointer (`vid/07 wwdc2020_10640`; `hig/13 pointing-devices`).

Brand and color
16. Launch screen as a brand screen; logo repeated throughout the app; brand competing with the content (`hig/01 branding`; `hig/03 launching`; `vid/17 wwdc2026_251`).
17. Color as the only means of conveying information; color hard-coded; redefining the semantics of system colors; tinting everything (`hig/01 color`, `accessibility`; `vid/16 wwdc2025_219`).
18. The app's own appearance setting in place of the system Dark Mode (`hig/01 dark-mode`).
19. Using Activity rings, the Apple Health icon, AirPlay or the Apple Pay mark as decoration, as a button or as an altered element (`hig/11 activity-rings`; `hig/15 healthkit`; `hig/14 airplay`, `apple-pay`).
20. SF Symbols in app icons or logos; replicas of Apple hardware (`hig/02 sf-symbols`; `hig/01 app-icons`, `icons`).

Icons
21. Text, photos or interface screenshots in the app icon; baked shadows, bevels and highlights; exporting the layer with the mask already applied (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`).
22. Emoji in place of a symbol in quick actions (`hig/07 home-screen-quick-actions`).

Permissions, data and trust
23. Asking for permissions when the app opens without need; pre-alert screens with "Allow" or that nudge people into tracking (`hig/02 privacy`; `vid/03 wwdc2017_816`; `vid/17 wwdc2026_250`).
24. Requiring an account before showing value; asking for a password from people who use Sign in with Apple; burying account deletion (`hig/03 managing-accounts`; `hig/16 sign-in-with-apple`).
25. Notifications for marketing without consent, Time Sensitive for promotion, several notifications for the same subject, a notification only to open the app, a badge for something other than unread messages (`hig/03 managing-notifications`; `hig/12 notifications`; `vid/04 wwdc2018_806`).
26. Making subscription cancellation difficult (`hig/15 in-app-purchase`).
27. AI that makes the person think they are talking to a human, automates destructive actions or presents facts without verified data (`hig/14 generative-ai`); raw confidence percentages and attributions that assume tastes ("love") (`hig/15 machine-learning`; `vid/06 wwdc2019_803`).

Feedback, onboarding and text
28. Long mandatory tutorials, onboarding that teaches the system, a floating arrow or hand pointing out where to tap (`hig/03 onboarding`; `vid/03 wwdc2017_811`; `vid/09 wwdc2021_10126`).
29. An alert when the app starts, an alert that is only informative, an alert for a common action that can be undone, an alert with an error code, an alert as a patch for an avoidable problem (`hig/09 alerts`; `vid/03 wwdc2017_813`).
30. Asking for a rating on the first launch or in the middle of a task (`hig/03 ratings-and-reviews`).
31. A progress indicator that is stopped or moves at an unrealistic pace; vague descriptions such as "loading" (`hig/11 progress-indicators`).
32. "Yes" and "No" on buttons, ambiguous "OK", generic "Confirm", "oops", "Click here", jargon and filler (`hig/09 alerts`; `hig/02 writing`; `vid/11 wwdc2022_10037`, `wwdc2022_10169`; `vid/15 wwdc2025_404`).
33. Choosing a font because the name matches the theme, the "Lack of Typographic Imagination" (`vid/03 wwdc2017_815`).

Platforms and body
34. Porting the interface of one platform to another: Watch as a miniature iPhone, console controls overlaid on touch, an iPad layout scaled on the Mac (`vid/02 wwdc2015_802`, `wwdc2014_602`; `hig/15 mac-catalyst`).
35. On visionOS: content locked to the head, depth in text, oscillation near 0.2 Hz, motion in the periphery, rotating the world, too many windows, requiring physical movement, custom gestures without need (`hig/02 spatial-layout`, `motion`; `vid/13 wwdc2023_10078`; `vid/14 wwdc2024_10094`).
36. On CarPlay, requiring the iPhone or showing errors on it (`hig/14 carplay`).
37. Truncating text when the size increases, ignoring accessibility preferences because the effect is part of the identity (`vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`).
