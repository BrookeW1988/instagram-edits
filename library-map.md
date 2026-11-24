# Edits library map

Known-good picks from Edits' built-in library, so each reel reuses them instead of searching again (ids are Edits'
own library ids, November 2026). Her OWN confirmed picks go in `profile.md` under "My Edits picks".

## The four styles
| Style | Recipe |
|---|---|
| Clean | `styles/clean.md` |
| Show it | `styles/show-it.md` |
| B-roll story | `styles/broll-story.md` |
| Minimal | `styles/minimal.md` |

## Known facts
- Claude CAN search sound effects (`searchSoundEffects`, up to 20 ids for `addSoundEffect`).
- Claude CAN search the music library (`listMusicTracks` with a query and `license` royaltyFree) and place a song
  with `addSongToComposition`. Royalty-free songs survive Claude's export (tested 24/11/2026).
  `addMusicTrack` reports success but does NOT place a clip: don't use it.
- Claude can NOT search GIFs or stickers (`addGif` / `addSticker` only take a file path).
- Claude's export works (`resolutionType` HD, `aspectRatio` nineBySixteen, `quality` high).

## Picks used in the demo reels
| Moment | Type | Search term | Item name / id | Used in |
|---|---|---|---|---|
| A card or receipt lands | SFX | pop | Lip pop (sharp) / 2129253541286265, vol 0.35 | Show it |
| The split screen drops in | SFX | page flip | Page flip 1 / 1436387947653003, vol 0.3 | Show it |
| The one big punch-in | SFX | whoosh | Whoosh (airy) 6, trimmed ~1 s, vol 0.35 | Clean |
| Soft bed under her voice | Music | soft lofi | Seasons (LAVLO) / 1033616122917539, royalty-free, vol 0.18 | B-roll story |
| A blurred background behind a card | Effect | n/a | `video_simple_blur` | Show it |
| A white frame round a GIF | Effect | n/a | `video_plain_frame` | any GIF |

Sound rules: tactile real-object sounds, never notification or UI blips (most "pop" results are blips), about
6-10 dB under the voice, on the frame the thing lands, and nothing on top of a comment keyword.
