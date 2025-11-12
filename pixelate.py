import sys
from PIL import Image, ImageDraw
from collections import Counter

def pixelate_dominant_with_grid_ignore_edge(input_path, output_path, pixel_size, debug_grid=False):
    # Open the image and ensure it's in RGB mode
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()
    w, h = img.size

    # Create a new empty image for output, same size as original
    out_img = Image.new("RGB", (w, h))
    out_pixels = out_img.load()

    edge = 2  # Number of edge pixels to ignore (on each side)

    # Loop over blocks of pixels, stepping by pixel_size (the "cell" size)
    for y in range(0, h, pixel_size):
        for x in range(0, w, pixel_size):
            colors = []
            # Only count colors from inside the edge, skip outer 'edge' pixels
            for dy in range(edge, pixel_size-edge):
                for dx in range(edge, pixel_size-edge):
                    px = x + dx
                    py = y + dy
                    if px < w and py < h:
                        colors.append(pixels[px, py])
            # If no colors collected (block too small), just fall back to the center pixel
            if not colors:
                px = x + pixel_size // 2
                py = y + pixel_size // 2
                if px >= w: px = w - 1
                if py >= h: py = h - 1
                colors = [pixels[px, py]]

            color_count = Counter(colors)
            dominant_color = color_count.most_common(1)[0][0]

            # Paint the whole block with the dominant color
            for dy in range(pixel_size):
                for dx in range(pixel_size):
                    px = x + dx
                    py = y + dy
                    if px < w and py < h:
                        out_pixels[px, py] = dominant_color

    # Optionally draw grid lines on top (using ImageDraw)
    if debug_grid:
        draw = ImageDraw.Draw(out_img)
        grid_color = (0, 0, 0)  # Black, can change to (255, 255, 255) or other colors
        for x in range(0, w, pixel_size):
            draw.line([(x, 0), (x, h)], fill=grid_color)
        for y in range(0, h, pixel_size):
            draw.line([(0, y), (w, y)], fill=grid_color)

    out_img.save(output_path)
    msg = "WITH GRID" if debug_grid else "without grid"
    print(f"Saved dominant-color pixelated image {msg} to {output_path} with pixel size {pixel_size}")

if __name__ == '__main__':
    # Parse CLI args; look for '--debug' as optional 4th arg
    if len(sys.argv) < 4:
        print("Usage: python pixelate_dominant_grid_ignore_edge.py input_image.png output_image.png pixel_size [--debug]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        pixel_size = int(sys.argv[3])
        debug_grid = (len(sys.argv) > 4 and sys.argv[4] == "--debug")
        pixelate_dominant_with_grid_ignore_edge(input_file, output_file, pixel_size, debug_grid)