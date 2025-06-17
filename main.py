import subprocess
import os

def set_mac_wallpaper(image_path):
    # Ensure the path is absolute
    abs_path = os.path.abspath(image_path)
    script = f'''osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{abs_path}"' '''
    subprocess.run(script, shell=True, check=True)

# Dummy call
set_mac_wallpaper('dummy.jpg')