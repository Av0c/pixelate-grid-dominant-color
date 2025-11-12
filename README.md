# Pixelate by Dominant Color

Pixelates an image by blocks of chosen size, painting each block with its dominant color, instead of using the average color like a normal pixelate filter.
Dominant color selection ignores the outer edge of each block to avoid misrepresentative colors.

Optionally overlays a grid for visual debugging.

## Example
Input:

<img src="/example/in.jpg" alt="Input" width="200"/>

Output:

<img src="/example/out.jpg" alt="Output" width="200"/>

## Uses

- Correcting artifacts to pixel-art images introduced by compression, scaling,....
- Turning AI-generated pixel-"art" images into pixel-perfect canvas for further editing.  

## Usage

First determine the pixel size, this should be as accurate as possible for the output to be meaningful, use any image editor/viewer that supports showing a grid, and start resizing that grid (grid size must be uniform in both direction) until pixels fit neatly into each cell.

```bash
pip install pillow
python pixelate_dominant_grid_ignore_edge.py input.png output.png PIXEL_SIZE [--debug]
```

- `input.png`: input image file
- `output.png`: output file
- `PIXEL_SIZE`: size of each block (e.g. 8)
- `--debug` (optional): draws grid overlay
