# Editor moves -> the Edits way to do them

An editor thinks in moves ("cut the false start", "punch in on the big line", "J-cut into the B-roll"). This is
how to do each move with Edits' own tools. Rows marked (untested) use a tool that exists in Edits but hasn't been
used in a real edit yet: try it once, check the frame, and note the result in `profile.md`. Everything else was
tested in Edits for Mac (November 2026). The judgement
(WHEN to make each move) lives in `editing-craft.md`; this file is the HOW.

Times: Edits works in timeline seconds. After a cut or a speed change the timeline shifts, so re-read positions
with `clips` (or `captions`) before the next move instead of reusing old numbers.

## Reading the take
| Move | In Edits |
|---|---|
| Know every word and when it's said | `transcribeClip` (id, language "en", mergeSplitWords true, background false) -> `jobStatus` until done. Returns each word with start/end. |
| Find the silences | `findPauses` (or the gaps between words from `transcribeClip`) |
| Look at a moment | `captureFrame` with a list of times (small `maxWidth` for a quick look) |
| See the whole edit | `frameSheet`, or export + `scripts/contact_sheet.sh` (the real check) |
| Hear the level | `loudness` on the clip; target about -14 LUFS for the whole reel |

## Cutting
| Move | In Edits |
|---|---|
| Hard cut / remove a stretch (pause, false start, retake) | `splitAt` (all cut points in one call) -> `selectById` each dead piece (`addToSelection` true) -> `delete`. The main track closes the gap. |
| Jump cut (same shot, time skipped) | Same as above: the join is the jump cut. Hide it with a punch-in if it jumps visibly. |
| Trim a clip's start or end | `trim` with `side` left/right and `deltaSeconds` (positive shortens, negative lengthens) |
| Speed up talking | `setSpeed` (e.g. 1.1-1.3) on every main-track piece |
| Reorder a section | `reorderClip` (rarely needed for talking heads) (untested) |
| J-cut / L-cut (voice runs over the next shot) | `extractAudio` on the take (voice on its own track), then cut the PICTURE where you like with `splitAt` + `replaceElementMedia`; the voice keeps running underneath. |

## Framing
| Move | In Edits |
|---|---|
| Punch-in (hard zoom cut on the same shot) | `splitAt` at the word gap -> `setTransform` on that piece: scale 1.06-1.30, y = 0.5 - (chin - 0.5) x (scale - 1) so her face stays put (chin ~0.73: 1.10 -> 0.477, 1.18 -> 0.459, 1.30 -> 0.431) |
| Back out to wide | the next piece stays at scale 1.0 (each piece keeps its own framing) |
| Two-camera fake | alternate 1.00 / 1.18 on every other piece |
| Slow push-in (creep) | `setTransformKeyframe` twice on one piece (one call per keyframe, timeline seconds): scale 1.0 near its start (easing linear) -> 1.06-1.08 near its end, y chin-anchored. Use rarely. (`setTransformKeyframes`, plural, doesn't exist in this build.) |
| Re-centre / reframe vertical from wide | `setTransform` with `fitMode` fill and `focusX` / `focusY` on her face (untested) |
| Move her down under a screen (split) | `setTransform` y ~0.68, scale 1, `allowBeyondCanvas` true |

## Cutaways and B-roll
| Move | In Edits |
|---|---|
| Cut away to B-roll (voice continues) | `extractAudio` -> `splitAt` the stretch -> `replaceElementMedia` with the clip -> `setVolume` 0 on the video piece |
| Picture-in-picture / small screenshot | `addOverlay` (x, y, scale = fraction of canvas width) then `trim` to the moment |
| Full-screen screenshot or graphic | `addOverlay` x 0.5 y 0.5 scale 1 |
| Blur the background behind a card | `splitAt` the piece -> `applyEffect` `video_simple_blur` |
| Black-and-white beat | `applyFilter` (Greyscale) on that piece |

## Words on screen
| Move | In Edits |
|---|---|
| Captions | `generateCaptions` (straight after the rough cut) -> `splitCaption` -> `setCaptionStyle` -> `setCaptionHighlightColor` -> `editCaption` -> `setTextFont` / `setTextStyle` / `setTextPosition` |
| Text hook / label | `addText` (atSeconds, duration) -> `setTextFont`, `setTextStyle`, `setTextPosition`, `setEmphasis` (outline or backgroundPill), `setTextAnimation` (none = hard on/off) |
| Big designed text, cards with a screenshot | PNG from `scripts/word_stacks.py` / `scripts/show_it_cards.py` -> `addOverlay` |
| Text appears on the exact word | read the word time from `transcribeClip` or a `splitCaption` split, then place at that time |
| Hide a caption under a graphic | `setTextStyle` size 1 |

## Sound
| Move | In Edits |
|---|---|
| Sound effect on a moment | `pause` -> `seek` to the frame -> `searchSoundEffects` -> `addSoundEffect` -> `setVolume` 0.3-0.35 |
| Music bed | `listMusicTracks` (query, license royaltyFree) -> `seek` 0 -> `addSongToComposition` -> `setVolume` ~0.15-0.2 |
| Duck music under voice | `setDucking` on the music clip (behaviour "video" or "any", level ~0.3) (untested) |
| Fade in / out (audio) | `setFade` fadeIn / fadeOut seconds on a music, sound or video clip (untested) |
| Clean up a noisy room | `setVoiceEnhance` on the voice (untested) |

## Look
| Move | In Edits |
|---|---|
| Grade | `addAdjustmentLayer` (first one covers the whole reel) -> `applyAdjust` per slider |
| A LUT / filter | `applyFilter` (tested) or `applyLUT` (untested) |

## Finishing
| Move | In Edits |
|---|---|
| Save | `saveProject` after each big step |
| Export | `setExportSettings` (HD, nineBySixteen, high, 30, sdr: all of them) -> `export` to a full path in ~/Movies |
| Check | `scripts/contact_sheet.sh` on the export + the checklist in `editing-craft.md` |

**Moves we don't make** (they read as cheap on talking-head reels): Edits transitions, shake / spin / glitch /
zoom-bounce effects, subject cut-outs (`addStickerFromCutout`) on a moving person, stickers over her face.
