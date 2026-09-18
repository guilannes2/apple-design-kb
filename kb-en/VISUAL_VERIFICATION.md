# Visual layer verification

How the proof works: each frame sheet and each illustration sheet received, in the image itself, a five-character code derived from a secret key kept outside the knowledge base. The code can only be obtained by looking at the image. The agent that viewed the sheet wrote down the code, and the check recalculates the expected code and compares.

## Numbers

| Item | Value |
|---|---|
| Videos with a file on the site | 175 |
| Videos processed into sheets | 175 |
| Frame sheets | 3072 |
| Sheets checked | 3072 |
| Videos watched in full | 175 |
| HIG units (illustration pages and demonstration videos) | 219 |
| HIG sheets checked | 552 of 552 |
| Codes that did not match | 0 |
| Visual syntheses written | 175 for video and 158 for the HIG |
| Syntheses with a recorded divergence between image and official description | 222 |
| Videos with no file on the site, not watched | 13 |

## What was left incomplete

No processed video was left with an unchecked sheet.

## Videos with no file on the site

These have neither video nor transcript at the source, so they were not watched and did not get a card:

- wwdc2019_801
- wwdc2022_10175
- wwdc2022_110484
- wwdc2022_110530
- wwdc2022_110531
- wwdc2022_110532
- wwdc2022_110533
- wwdc2023_10337
- wwdc2023_111243
- wwdc2023_111324
- wwdc2023_111484
- wwdc2023_111520
- wwdc2023_111522

## Limits of the method

1. The sheets carry one frame per scene change and at least one every 12 seconds, not every frame of the video. Continuous movement appears as the difference between still frames.
2. Fast effects may not appear between two frames. When that happened, it is recorded in the sheet's note.
3. The HIG illustrations were viewed in the light version; the dark version entered on the color, dark mode, materials and icons pages.
4. Thumbnails and icons that the page only uses as links to other pages were left out.

Translator's note: this file is the English translation of a verification record. The reading and the code checks it describes were run once, on the frames and illustrations themselves, and recorded in Portuguese in `kb/visual/`, `kb/visual_hig/` and `kb/visual_logs/`.
