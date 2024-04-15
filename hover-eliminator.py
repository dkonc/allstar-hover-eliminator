import pyautogui
import time
from PIL import Image

def take_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

def compare_pixels(screenshot, x, y):
    screenshot_pixel = screenshot.getpixel((x, y))
    pyautogui.moveTo(x, y)
    hover_pixel = pyautogui.pixel(x, y)
    if screenshot_pixel != hover_pixel:
        return True
    else:
        return False

def main():

    #Da imaš cajt se premaknit na tapravi zavihek v Chrome/Firefox itd.Ko se enkrat zažene ni poti nazaj :D
    time.sleep(5)
    screenshot = take_screenshot()
    
    width, height = pyautogui.size()
    
    #Kok veliko sliko voč, da veš kje je napaka.
    error_area_size = 150
    
    #Najmanjša ikonca je 16px. Lahko daš na manj, samo se bo dalj izvajalo.
    pixel_step = 15 
    
    #Chrome/Firefox tabs etc. Naštimaj po volji
    top_margin = 85
    #Windows/iOS bottom nav bar etc. Naštimaj po volji
    bottom_margin = 40
    
    #Če testiraš popupe, da ti ni treba čez celoten background
    #Vsaj eden od telih naj bo vsaj 1, da ni potrebno FAILSAFE pri pyautogui izklopit
    left_margin = 470
    right_margin = 400

    for x in range(left_margin, width - right_margin, pixel_step):
        for y in range(top_margin, height - bottom_margin, pixel_step):
            if compare_pixels(screenshot, x, y):
                error_area = screenshot.crop((x - error_area_size//2, y - error_area_size//2, 
                                                x + error_area_size//2, y + error_area_size//2))
                error_area.save(f"error_{x}_{y}.png")
                print(f"Error detected at ({x}, {y})")

if __name__ == "__main__":
    main()
