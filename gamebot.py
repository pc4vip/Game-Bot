import numpy as np
import cv2
from PIL import ImageGrab
from pynput.keyboard import Key, Controller

# initializing the keyboard
keyboard = Controller()


# To print the y and x value when the screen is clicked
def on_mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
            print(flags, param)
            print('x = %d, y = %d' % (x, y))


while True:
    # Grab a specific regain on the screen
    img = ImageGrab.grab(bbox=(150, 150, 800, 640))

    # Grab a specific regain on the screen
    px = ImageGrab.grab(bbox=(150, 150, 800, 640)).load()

    # Using the np import and passing the image
    img_np = np.array(img)

    # TODO: Replace the pixel values with a Pixel range

    # Getting the values of specific pixels
    color1 = px[318, 272]
    color2 = px[320, 288]
    color3 = px[314, 292]
    color4 = px[323, 286]
    color5 = px[317, 266]

    color6 = px[310, 330]
    color7 = px[312, 328]
    color8 = px[314, 326]
    color9 = px[316, 324]
    color10 = px[318, 322]

    color11 = px[320, 320]
    color12 = px[281, 324]
    color13 = px[324, 316]
    color14 = px[280, 319]
    color15 = px[328, 320]

    color16 = px[210, 318]
    color17 = px[214, 316]
    color18 = px[334, 306]
    color19 = px[336, 304]
    color20 = px[338, 302]

    color21 = px[330, 270]
    color22 = px[332, 275]
    color23 = px[334, 265]
    color24 = px[336, 280]
    color25 = px[338, 290]

    # If statement to check the pixel color value
    if color1 == (83, 83, 83)\
       or color2 == (83, 83, 83)or color3 == (83, 83, 83)\
       or color4 == (83, 83, 83)or color5 == (83, 83, 83)\
       or color6 == (83, 83, 83)or color7 == (83, 83, 83)\
       or color8 == (83, 83, 83) or color9 == (83, 83, 83)\
       or color10 == (83, 83, 83)or color11 == (83, 83, 83)\
       or color12 == (83, 83, 83)or color13 == (83, 83, 83)\
       or color14 == (83, 83, 83)or color15 == (83, 83, 83)\
       or color16 == (83, 83, 83)or color17 == (83, 83, 83)\
       or color18 == (83, 83, 83)or color19 == (83, 83, 83)\
       or color20 == (83, 83, 83)or color21 == (83, 83, 83)\
       or color22 == (83, 83, 83)or color23 == (83, 83, 83)\
       or color24 == (83, 83, 83)or color25 == (83, 83, 83):
        # press and release key up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    # End of the if statement

    # Display the window on screen
    cv2.imshow("images",  img_np)

    # Call the onMouse function when the window is clicked
    cv2.setMouseCallback('images', on_mouse)

    # Close the window if letter q is pressed and destroy all windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        # End the while loop
        break
