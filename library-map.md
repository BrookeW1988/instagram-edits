# Edits library map

What's known to work inside Edits' built-in library, so each reel reuses a known-good pick instead of
searching again. The ids are Edits' own library ids, found in testing (November 2026). **Nobody has
listened to these in a finished reel yet**: play them before you trust them.

Your OWN confirmed picks go in `profile.md` under "My Edits picks" (that file is yours and survives updates).

## Look and format recipes
Every look and format is built with Edits' own tools from its recipe in `styles/`. The numbers come from its
`SPEC.md` in the Reel Looks library (`LOOKS/looks/<slug>/` or `LOOKS/formats/<slug>/`).

| Look or format | Slug | Recipe |
|---|---|---|
| Just you | `just-you` | `styles/just-you.md` |
| Full | `full` | `styles/full.md` |
| Hormozi classic | `hormozi-classic` | `styles/hormozi-classic.md` |
| Hormozi 2026 | `hormozi-2026` | `styles/hormozi-2026.md` |
| Codie Sanchez | `codie-sanchez` | `styles/codie-sanchez.md` |
| Diary of a CEO | `diary-of-a-ceo` | `styles/diary-of-a-ceo.md` |
| Nana Del Rey | `nana-del-rey` | `styles/nana-del-rey.md` |
| Mariah Brunner | `mariah-brunner` | `styles/mariah-brunner.md` |
| Nick Saraev | `nick-saraev` | `styles/nick-saraev.md` |
| Iman Gadzhi | `iman-gadzhi` | `styles/iman-gadzhi.md` |
| Calm luxury | `calm-luxury` | `styles/calm-luxury.md` |
| Pop-up proof (format) | `pop-up-proof` | `styles/pop-up-proof.md` |
| Text over B-roll (format) | `text-over-broll` | `styles/text-over-broll.md` |
| Serialised episode (format) | `serialised-episode` | `styles/serialised-episode.md` |
| Before-and-after (format) | `before-after-reveal` | `styles/before-after-reveal.md` |
| POV skit (format) | `pov-skit` | `styles/pov-skit.md` |
| Green-screen proof (format) | `green-screen-proof` | `styles/green-screen-proof.md` |
| Timestamp vlog (format) | `timestamp-vlog` | `styles/timestamp-vlog.md` |
| Yes... but (format) | `yes-but-split` | `styles/yes-but-split.md` |

## Known facts
- Claude CAN search the sound-effect library by keyword (`searchSoundEffects`, up to 20 ids for `addSoundEffect`).
- Claude can NOT search GIFs or stickers (`addGif` / `addSticker` only take a file path).
- See-through video overlays she supplies (a .mov with transparency) keep it in the preview and the export.
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
