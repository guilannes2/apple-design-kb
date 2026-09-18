# Knowledge base coverage and fidelity check

Date: 15/09/2026. Scope: /Users/guilhermelannes/Downloads/apple-design-kb/kb/ (18 files in kb/hig, 18 in kb/videos) against groups.json and the source texts in text/hig and text/transcripts. No file of the base was changed.

## Summary

| Check | Result |
|---|---|
| HIG slugs missing from kb/hig | 0 of 173 |
| Video ids missing from kb/videos | 0 of 188 |
| Files marked as not read to the end | 0 of 355 entries |
| Claims checked | 20 (12 HIG, 8 videos) |
| Claims that do not check out | 0 |
| Claims of having viewed screens, frames or videos | 0 |

## 1. Coverage

Method: a Python script read groups.json (18 HIG groups with 173 unique slugs; 18 video groups with 188 unique ids), concatenated the files of each folder and searched for every slug and every id, first by substring and then with a word boundary. The two searches gave the same result.

HIG slugs missing: none.
Video ids missing: none.

Additional check: all 173 slugs have a file in text/hig and all 188 ids have a file in text/transcripts.

## 2. Evidence of reading

All 36 files have the section. In kb/videos/04_wwdc2018.md the heading is without the accent ("## Evidencia de leitura"), so a search for the accented heading does not find it; the content exists and is complete.

Result of the cross-check by group: every slug and every id of the group appears listed in the evidence section of the corresponding file (355 entries in total).

Files marked as not read to the end: none. All 355 entries carry "to the end: yes".

Additional check: the number of lines declared in each entry was compared with the real count of the source file (wc -l, tolerance of one line). No divergence.

Observations recorded by the files themselves, which are not incomplete reading:
1. kb/videos/11_wwdc2022-parte-1.md reports that wwdc2022_110342 and wwdc2022_10037 carry "Duration: 0.0 min" in the header and marks the duration as not reported.
2. meet-with-apple_270 and meet-with-apple_274 have only 4 lines in the source (header, with no transcript); kb/videos/00_meet-with-apple.md states "No transcript available" for both, which checks out against the source.

## 3. Fidelity

### HIG part

| # | Claim in the base | Base file | Source | Result | Source excerpt |
|---|---|---|---|---|---|
| 1 | Allow text to be enlarged by at least 200% (140% in watchOS) | 01_foundations-part-1.md | text/hig/accessibility.md | checks out | "enlarge text by at least 200 percent (or 140 percent in watchOS apps)" |
| 2 | Minimum contrast of 4.5:1 for text up to 17 pts | 01_foundations-part-1.md | text/hig/accessibility.md | checks out | "Up to 17 pts, All, 4.5:1" (table row) |
| 3 | Dimming layer of 35% under Liquid Glass clear on a bright background | 02_foundations-part-2.md | text/hig/materials.md | checks out | "a dark dimming layer of 35% opacity" |
| 4 | Increase the RTL font by about 2 points next to uppercase Latin | 02_foundations-part-2.md | text/hig/right-to-left.md | checks out | "increase the RTL font size by about 2 points" |
| 5 | visionOS component centers at least 60 points apart, with 16 points or more between them | 02_foundations-part-2.md | text/hig/spatial-layout.md | checks out | "centers are at least 60 points apart, leaving 16 points or more" |
| 6 | Custom activity icon centered in an area of about 70x70 pixels | 07_components-menus-and-actions.md | text/hig/activity-views.md | checks out | "center it in an area measuring about 70x70 pixels" |
| 7 | The menu bar height is 24 pt | 07_components-menus-and-actions.md | text/hig/the-menu-bar.md | checks out | "The menu bar's height is 24 pt." |
| 8 | Window title under 15 characters (Toolbars section) | 07_components-menus-and-actions.md | text/hig/toolbars.md | checks out | "keep the title under 15 characters long" |
| 9 | visionOS alert accessory view: maximum height 154 pt, corner radius 16 pt | 09_components-presentation.md | text/hig/alerts.md | checks out | "maximum height of 154 pt and a 16-pt corner radius" |
| 10 | Default visionOS window 1280x720 pt, at about two meters, apparent width of about three meters | 09_components-presentation.md | text/hig/windows.md | checks out | "a window measures 1280x720 pt ... about two meters ... about three meters" |
| 11 | App Clip Card: 1800x1200 px image, title up to 30 and subtitle up to 56 characters | 14_technologies-part-1.md | text/hig/app-clips.md | checks out | "1800x1200 px PNG or JPEG"; "no more than 30 characters ... no more than 56" |
| 12 | A 35 mm NFC tag requires a printed code of at least 1.37 inches (3.48 cm) | 14_technologies-part-1.md | text/hig/app-clips.md | checks out | "at least 1.37 inches (3.48 cm) in diameter" |

### Videos part

| # | Claim in the base | Base file | Source | Result | Source excerpt |
|---|---|---|---|---|---|
| 13 | Reference screen of 375 by 667 points, the iPhone 6 resolution | 02_wwdc2014-2016.md | text/transcripts/wwdc2016_805.md | checks out | "375 by 667 points, because this is the resolution of an iPhone 6" |
| 14 | In the Top Shelf, the person stays on a poster for 5 seconds before the trailer | 05_wwdc2019-part-1.md | text/transcripts/wwdc2019_211.md | checks out | "we hold on a poster image for five seconds" |
| 15 | Pixelmator Photo: Core ML model trained with more than 20 million pairs, more than 32 adjustments | 05_wwdc2019-part-1.md | text/transcripts/wwdc2019_104.md | checks out | "over 20 million image pairs ... over 32 different adjustments" |
| 16 | Color blindness affects almost 5% of the population; aim for 4.5:1 with Increase Contrast | 09_wwdc2021-part-1.md | text/transcripts/wwdc2021_10275.md | checks out | "affects almost 5% of the world's population"; "aspire to a minimum of 4.5:1" |
| 17 | Maximum of 10 App Shortcuts, recommendation of 2 to 5; disambiguation for 5 values or fewer | 11_wwdc2022-part-1.md | text/transcripts/wwdc2022_10169.md | checks out | "The maximum you can create is 10 ... two to five high-quality app shortcuts" |
| 18 | More than 700 new symbols, library above 4,000 | 11_wwdc2022-part-1.md | text/transcripts/wwdc2022_10157.md | checks out | "over 700 ... 4,000 unique symbols" |
| 19 | Moon: 350,000 triangles after reduction; almost 60,000 and 110,000 removed in culling; 180,000 afterwards | 15_wwdc2025-part-1.md | text/transcripts/wwdc2025_305.md | checks out | "down to just 350,000"; "just under 60,000 are removed"; "110,000 triangles were Culled"; "now just 180,000" |
| 20 | Hysteresis usually of 10 points on iOS; Music uses 100% damping on the tap and 80% on the swipe | 04_wwdc2018.md | text/transcripts/wwdc2018_803.md | checks out | "hysteresis, and is usually 10 points in iOS"; "we use 100% damping"; "we use 80%" |

### Additional checks (outside the sample of 20, all check out)

| Claim | Source | Source excerpt |
|---|---|---|
| Sign in with Apple button: the title font is 43% of the height; the height is 233% of the font (16_technologies-part-3.md) | text/hig/sign-in-with-apple.md | "the title's font size would be 43% of the button's height" |
| Drag image after about 3 points (03_patterns-part-1.md) | text/hig/drag-and-drop.md | "as soon as people drag a selection about three points" |
| Tooltip with a maximum of 60 to 75 characters (03_patterns-part-1.md) | text/hig/offering-help.md | "a maximum of 60 to 75 characters" |
| tvOS: minimum delay of 0.5 s for the overlay; 160 px thumbnails (03_patterns-part-1.md) | text/hig/playing-video.md | "minimum delay of 0.5 seconds"; "each measure 160 px in width" |
| Circular complication 40mm: 42x42 pt image (12_components-system-experiences.md) | text/hig/complications.md | "Image, 42x42 pt (84x84 px @2x)" |
| Button sizes macOS 28x28/20x20 and tvOS 66x66/56x56 (00_getting-started.md) | text/hig/designing-for-games.md | "macOS, 28x28 pt, 20x20 pt"; "tvOS, 66x66 pt, 56x56 pt" |
| Lowe's: a three-person team in a company of 300 thousand associates, speech by Steve Lindgren (00_meet-with-apple.md) | text/transcripts/meet-with-apple_208.md | "Lowe's has 300,000 associates"; "really three core members" |
| 1024px canvas for iPhone, iPad and Mac; Watch 1088px (15_wwdc2025-part-1.md) | text/transcripts/wwdc2025_361.md | "the same 1024px canvas"; "Watch is now 1088px" |
| Minimum eye target area of 60 points (13_wwdc2023.md) | text/transcripts/wwdc2023_10073.md | "minimum area that your element needs for eye target is 60 points" |
| "15-second highlights" on the controller's Share button (09_wwdc2021-part-1.md) | text/transcripts/wwdc2021_10081.md | "15-second highlights" |
| Quote "Do not delegate critical thinking to these tools." (17_wwdc2026.md) | text/transcripts/wwdc2026_227.md | identical sentence on line 14 |
| New York Times: reading the story would take "way more than two to five seconds" (02_wwdc2014-2016.md) | text/transcripts/wwdc2015_802.md | "way more than two to five seconds" |

## 4. Honesty

Searches made in kb/ (excluding "framework"): "I saw ", "we saw", "I watched", "we watched", "I observed", "I looked", "in the video appears", "shows on the screen", "appears on the screen", "on the screen appears", "the frame shows", "in the frames", "in the frame", "screen capture", "screenshot", "looking at the video", "frames of", "in the frames", "image from the video", "slide", "live".

Claims of having viewed screens, frames or videos: none.

Occurrences that look visual but are text of the base itself or a description taken from the speech, checked against the transcript:
1. kb/hig/12_components-system-experiences.md:526, "what appears on the screen": this is about the Siri rule, not an observation.
2. kb/videos/14_wwdc2024.md:55, quote "Notice how the two screens cast light effects on their surroundings": a literal sentence from the wwdc2024_10116 transcript, not an observation of its own.
3. kb/videos/11_wwdc2022-parte-1.md:121, "live demonstration of the Variable Color slider": the wwdc2022_10158 transcript narrates the demo ("pull the slider all the way down").
4. kb/videos/08_wwdc2020-parte-2.md:64, case study with Starstruck and Sneaky Sasquatch: both named in the speech of wwdc2020_10020.
5. kb/videos/14_wwdc2024.md:256, 280 and 291, "live" constructions of effects: the wwdc2024_10151 transcript narrates the construction step by step (RippleModifier, Ripple shader).
6. Occurrences of "visually", "live" in the sense of live content (live viewing) and "slide" (Slide Over, Keynote slides) in kb/hig and kb/videos: vocabulary of the content, with no claim of having viewed anything.

One reading inference, not a visual one, is recorded: kb/videos/14_wwdc2024.md:291 states that in wwdc2024_10151 "there are no real third-party apps cited". No complete scan of the transcript was made to confirm the absence.

## 5. Correction on 15/09/2026, after the strict per-card check

The coverage check above searched for each id anywhere in the file. That let through one video whose id appeared only in the evidence-of-reading list, with no card of its own. The check was redone requiring a heading of its own in the format "## title (id: ..., duration)" for each video and "## title (slug: ...)" for each HIG page.

Result of the strict check:
1. HIG: the 173 slugs have their own title. Four collection index pages (presentation, content, navigation-and-search, status) have a short body because the page itself has no text beyond the list.
2. Videos: the card for wwdc2023_10115 (Design with SwiftUI, with an official transcript) was missing. Eight videos with media and without an official transcript had an empty card or no card at all: meet-with-apple_270, meet-with-apple_274, tech-talks_111461, tech-talks_111462, tech-talks_111463, tech-talks_111466, wwdc2020_20022 and wwdc2026_8012.
3. The nine cards were written from the entire transcript (official in the case of wwdc2023_10115, local automatic with Whisper in the other eight, marked as such on the card itself) and each one went through a verifier that cross-checked every claim against the transcript. No claim was removed for lack of basis, except two (one in wwdc2020_20022 and one in wwdc2026_8012); the remaining corrections were of meaning or of precision.
4. After the insertion: no video with media without a card, no short card, no duplicate card. The 13 videos without media on the site remain only listed, with no card, because there is neither transcript nor video.
5. Wrong durations because of my own error when gathering the data, not the site's. When the video table was assembled, the durations from the Design topic list were associated with the neighboring video, out of order. The site shows the right duration next to each video. Proof: in the 108 videos whose recorded duration diverged, the duration of the downloaded file is identical to that of the file on Apple's server, and the 443 media links carry the number of the video itself, so no video was swapped or downloaded halfway. Correction applied: the duration now comes from the measured file (175 videos with media) and, in the videos without media, from the Design topic list matched by title. The manifest, the video index, the transcript headers and the card titles were corrected.

Translator's note: this file is the English translation of a verification record. The checks it describes were run on the Portuguese base in `kb/`, so the paths above are the Portuguese ones. The English copy in `kb-en/` mirrors that base line by line.
