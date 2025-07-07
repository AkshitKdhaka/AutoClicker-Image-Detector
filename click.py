import pyautogui
import time
import keyboard
import os
import traceback  # Added for detailed error logging

# Image path
IMAGE_PATH = r'C:\Users\akshi\OneDrive\Desktop\project\click\heart2.png'

# Validate image path
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"❌ Image file not found at {IMAGE_PATH}. Please check the path.")

# Delay to prevent overloading the system
DELAY_BETWEEN_CHECKS = 0.5  # seconds

print("🚀 Script started! Waiting for the image to appear... Press 'q' to stop.")

try:
    while True:
        # Check if 'q' is pressed to stop the script
        if keyboard.is_pressed('q'):
            print("🛑 Stop command received. Exiting the script...")
            break
        
        try:
            # Try locating the image on the screen
            image_location = pyautogui.locateOnScreen(IMAGE_PATH, confidence=0.7)
            
            if image_location:
                image_center = pyautogui.center(image_location)
                pyautogui.moveTo(image_center)
                pyautogui.click()
                print("✅ Image detected and clicked!")
                time.sleep(1)  # Pause briefly to avoid rapid re-clicking
            else:
                print("🔍 Image not found. Still waiting...")

        except pyautogui.ImageNotFoundException:
            print("❌ pyautogui could not find the image on the screen.")
        except Exception as inner_e:
            print(f"❌ An error occurred while locating/clicking the image: {inner_e}")
            traceback.print_exc()  # Print detailed error traceback
        
        # Short delay before the next iteration
        time.sleep(DELAY_BETWEEN_CHECKS)

except KeyboardInterrupt:
    print("🛑 Script interrupted manually. Exiting...")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
    traceback.print_exc()  # Print detailed error traceback
