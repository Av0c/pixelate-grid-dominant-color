# Pixelate by Dominant Color

Pixelates an image by blocks of chosen size, painting each block with its dominant color, instead of using the average color like a normal pixelate filter.
Dominant color selection ignores the outer edge of each block to avoid misrepresentative colors.

Optionally overlays a grid for visual debugging.

## Usage

```bash
pip install pillow
python pixelate_dominant_grid_ignore_edge.py input.png output.png PIXEL_SIZE [--debug]
```

- `input.png`: input image file
- `output.png`: output file
- `PIXEL_SIZE`: size of each block (e.g. 8)
- `--debug` (optional): draws grid overlay
