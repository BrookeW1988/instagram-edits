# Edits library map

What's known to work inside Edits' built-in library, so each reel reuses a known-good pick instead of
searching again. The ids are Edits' own library ids, found in testing (November 2026). **Nobody has
listened to these in a finished reel yet**: play them before you trust them.

Your OWN confirmed picks go in `profile.md` under "My Edits picks" (that file is yours and survives updates).

## Known facts
- Claude CAN search the sound-effect library by keyword (`searchSoundEffects`, up to 20 ids for `addSoundEffect`).
- Claude can NOT search GIFs or stickers (`addGif` / `addSticker` only take a file path).
- Transparent ProRes 4444 overlays keep their transparency in the preview and the export.
- An overlay clip's own audio plays and exports.
- Claude's export works (`resolutionType` HD, `aspectRatio` nineBySixteen, `quality` high).
- Library MUSIC goes silent in Claude's exports. Library SFX in exports: not yet checked.

## Picks found in testing
| Moment | Type | Edits search term | Item name / id | Notes |
|---|---|---|---|---|
| Card lands | SFX | whoosh | Whoosh (airy) 8 / 2398146380920271 (0.38 s) | not yet listened to |
| GIF lands | SFX | pop | Lip pop (sharp) / 2129253541286265 (0.3 s) | most other "pop" results are notification blips: avoid |
| Money | SFX | cash register | Ka-ching / 1500116367839672 (1.9 s) | not yet listened to |
| Result / big number | SFX | sparkle | Sparkle / 1510313150012788 (3.5 s, trim to ~1.4 s + fade) | not yet listened to |
| Base caption style | Caption | n/a | "Word Highlight Box 2" | + highlight colour, font and y 0.86 (see references/edits-tool-notes.md) |

## Moment map (what to search for)
| Moment in the reel | Edits search (SFX) | GIF / sticker (her own file or the free editing pack) |
|---|---|---|
| A card or screenshot lands | whoosh, swipe | n/a |
| She names a tool / clicks something | mouse click, tap | n/a |
| A prompt being typed | keyboard, typing | n/a |
| "Wait, what?" / contrarian turn | record scratch | confused, wait what |
| Result / mind blown | sparkle, ding | mind blown |
| Yes / love it | pop | yes, love it |
| Nope / don't do this | buzzer, wrong | nope, no |
| Money / price | cash register, coins | money |
| Overwhelm | none (let it breathe) | overwhelmed, stressed |
| Win / celebrate | crowd cheer, applause | celebrate, party |
| Awkward / cringe | crickets | awkward, cringe |

Sound rules: tactile sounds (real objects), never notification or UI blips, about 6-10 dB under the voice, lined up
with the thing on screen, and nothing on top of a comment keyword.
