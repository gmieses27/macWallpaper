import subprocess
# import quartz  # only if using PyObjC for better wallpaper control
# import ctypes
# import re

def get_screen_resolution():
    import AppKit
    screen = AppKit.NSScreen.mainScreen()
    frame = screen.frame()
    return int(frame.size.width), int(frame.size.height)

def is_dark_mode_active():
    result = subprocess.run(
        ['defaults', 'read', '-g', 'AppleInterfaceStyle'],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )
    return "Dark" in result.stdout

def update_wallpaper(image_path):
    image_path = str(image_path)
    script = f'tell application "System Events" to set picture of desktop 1 to "{image_path}"'
    subprocess.run(["osascript", "-e", script], check=True)