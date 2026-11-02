# Motion Blur for Horizon

A native mod for [Horizon](https://github.com/horizon-rust/horizon) that blurs what moves, by levzzz5154.
Moving mobs, players, items, minecarts and boats blur along their own motion. The camera's motion
(turning, walking) can blur too, and is off by default.

Each frame the mod:

1. Works out every pixel's motion since the last frame. The world's part comes from the depth
   buffer and the camera's motion. Entities are drawn again over it with last frame's vertices,
   so their own motion counts.
2. Finds the largest motion near each 16 × 16 tile and its neighbours, so the blur reaches past a
   moving object's edges.
3. Gathers along that motion with depth-aware weights: McGuire et al., "A Reconstruction Filter
   for Plausible Motion Blur" (2012).

## Settings

**Options → Mods → Motion Blur → Settings.** Each button cycles through its choices, applies at
once, and is kept for the next game.

| Button | Choices |
|---|---|
| Motion blur | On, off |
| Moving things | 0 % to 400 % blur from moving mobs, items and vehicles |
| Camera motion | 0 % to 400 % blur from the camera turning and moving (0 % by default) |
| Shutter | How long the shutter stays open, 90° to 720° of a frame (180° by default) |
| Exposure | By shutter, or a fixed 8, 12, 16 or 33 ms: the same blur at any frame rate |
| Longest blur | 32 px to 1024 px, or no limit |
| Quality | 6 to 32 samples along the blur |
| Blur yourself | Your own body in third person |
| Show motion | Draws each pixel's motion as colour, to see what blurs |

Turning the mod off in Options → Mods stops the blur at once.

## Install

Install it from the launcher's mod browser. It's a native mod: the launcher builds a copy of the
game with it (Settings → Game → Native mods). It uses only Horizon's native hook points, so it
builds on any Horizon that has them (`hooks` in `compatibility.json`).

## Build the package

```sh
python3 tools/package.py
```

This writes `target/motion_blur-<version>.hnmod` and prints its SHA-256.

MIT licensed. No Minecraft code or assets are included.
