import logging
import random

from implementations import get_screen_resolution, is_dark_mode_active, update_wallpaper
from wallpaper_generators import generate_julia_set, generate_mandelbrot

def main():
    logging.basicConfig(level=logging.INFO)
    
    try:
        width, height = get_screen_resolution()
        dark_mode = is_dark_mode_active()
        
        choice = random.choice(["mandelbrot"])

        if choice == "julia":
            saved_image_path = generate_julia_set(width, height, dark_mode)
        elif choice == "mandelbrot":
            saved_image_path = generate_mandelbrot(width, height, 1000)

        logging.info(f"Image saved to: {saved_image_path}")
        update_wallpaper(saved_image_path)

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()