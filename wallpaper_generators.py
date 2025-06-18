from PIL import Image
from datetime import datetime
from pathlib import Path

def generate_julia_set(width, height, dark_mode):
    import numpy as np

    zoom = .4
    x = np.linspace(-zoom, zoom, width)
    y = np.linspace(-zoom, zoom, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = complex(-0.7, 0.27015)
    iterations = 300

    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            z = Z[j, i]
            n = 0
            while abs(z) <= 2 and n < iterations:
                z = z*z + C
                n += 1
            color = (0, 0, 0) if dark_mode else (255, 255, 255)
            if n < iterations:
                color = (n % 8 * 32, n % 16 * 16, n % 32 * 8)
            pixels[i, j] = color


    out_path = Path(f"/tmp/julia_set_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png")
    img.save(out_path)
    return out_path


def generate_mandelbrot(width, height, max_iter=100):
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    # Coordinate space
    # Zoomed-out (default view)
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5

    # Zoomed-in (smaller range, centered at -0.75, 0)
    zoom = 0.5  # smaller = more zoomed in
    center_x, center_y = -0.75, 0.0
    xmin, xmax = center_x - zoom, center_x + zoom
    ymin, ymax = center_y - zoom, center_y + zoom

    for x in range(width):
        for y in range(height):
            zx = xmin + (xmax - xmin) * x / width
            zy = ymin + (ymax - ymin) * y / height
            z = complex(zx, zy)
            c = z
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z * z + c
                n += 1
            color = 255 - int(n * 255 / max_iter)
            pixels[x, y] = (123, color, color)

    out_path = Path(f"/tmp/mandelbrot_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png")
    img.save(out_path)
    return out_path