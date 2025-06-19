import logging
import secrets
# import time

from implementations import get_screen_resolution, is_dark_mode_active, update_wallpaper
from wallpaper_generators import generate_julia_set, generate_mandelbrot_set, generate_tree_fractal

def main():
    logging.basicConfig(level=logging.INFO)
    
    try:
        width, height = get_screen_resolution()
        dark_mode = is_dark_mode_active()
        
        choice = secrets.choice(["julia", "mandelbrot", "tree"])
        logging.info(f"Selected fractal type: {choice}")
        if choice == "julia":
            saved_image_path = generate_julia_set(width, height, dark_mode)
        elif choice == "mandelbrot":
            saved_image_path = generate_mandelbrot_set(width, height, 1000, dark_mode=dark_mode)
        elif choice == "tree":
            saved_image_path = generate_tree_fractal(width, height, dark_mode)

        logging.info(f"Image saved to: {saved_image_path}")
        # time.sleep(1)
        update_wallpaper(saved_image_path)

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()