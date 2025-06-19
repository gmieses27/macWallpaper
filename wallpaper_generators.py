from PIL import Image
from datetime import datetime
from pathlib import Path
import random
import numpy as np

def random_palette():
    # Generate a list of random RGB tuples
    return [(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    ) for _ in range(256)]

def generate_julia_set(width, height, dark_mode):
    zoom = .4
    x = np.linspace(-zoom, zoom, width)
    y = np.linspace(-zoom, zoom, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = complex(-0.7, 0.27015)
    iterations = 300

    palette = random_palette()
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            z = Z[j, i]
            n = 0
            while abs(z) <= 2 and n < iterations:
                z = z*z + C
                n += 1
            if n < iterations:
                color = palette[n % len(palette)]
            else:
                color = (0, 0, 0) if dark_mode else (255, 255, 255)
            pixels[i, j] = color

    out_path = Path(f"/tmp/julia_set_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png")
    img.save(out_path)
    return out_path

def generate_mandelbrot(width, height, max_iter=1000, zoom=0.5, center_x=-0.75, center_y=0.0, dark_mode=False):
    x = np.linspace(center_x - zoom, center_x + zoom, width)
    y = np.linspace(center_y - zoom, center_y + zoom, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    div_time = np.zeros(C.shape, dtype=int)
    mask = np.ones(C.shape, dtype=bool)
    palette = random_palette()

    for i in range(max_iter):
        Z[mask] = Z[mask] ** 2 + C[mask]
        mask, old_mask = np.abs(Z) < 2, mask
        div_time[mask ^ old_mask] = i

    img = Image.new("RGB", (width, height))
    pixels = img.load()
    for i in range(width):
        for j in range(height):
            n = div_time[j, i]
            if n < max_iter - 1:
                color = palette[n % len(palette)]
            else:
                color = (0, 0, 0) if dark_mode else (255, 255, 255)
            pixels[i, j] = color

    out_path = Path(f"/tmp/mandelbrot_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png")
    img.save(out_path)
    return out_path