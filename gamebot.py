import numpy as np
import cv2
from pynput.keyboard import Key, Controller
import mss
import time

# initializing the keyboard
keyboard = Controller()


# To print the y and x value when the screen is clicked
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
            print(flags, param)
            print('x = %d, y = %d' % (x, y))


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 150, 'left': 150, 'width': 800, 'height': 640}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))

        # Using the np import and passing the image
        img_np = np.array(img)

        # TODO: Replace the pixel values with a Pixel range
        color0 = img[65, 65]
        # Getting the values of specific pixels
        color1 = img[315, 320]
        color2 = img[305, 288]
        color3 = img[315, 292]
        color4 = img[310, 310]
        color5 = img[300, 266]

        color6 = img[254, 253]
        color7 = img[255, 258]
        color8 = img[256, 259]
        color9 = img[270, 253]
        color10 = img[277, 270]

        color11 = img[320, 320]
        color12 = img[281, 324]
        color13 = img[324, 316]
        color14 = img[280, 319]
        color15 = img[328, 320]

        color16 = img[210, 318]
        color17 = img[214, 316]
        color18 = img[334, 306]
        color19 = img[336, 304]
        color20 = img[338, 302]

        color21 = img[330, 270]
        color22 = img[332, 275]
        color23 = img[334, 265]
        color24 = img[336, 280]
        color25 = img[338, 290]

        end = img[604, 260]

        #   print(end)
        #
        # print("start")
        # print(color0)
        # print(color1)
        # print(color2)
        # print(color3)
        # print(color4)
        # print(color5)
        # print("end")
        # if 43 in end:
        #     print("##########################"
        #       "##########################"
        #       "##########################"
        #       "##########################"
        #       "##########################")

        if 255 in color0:

            # If statement to check the pixel color value
            if 83 in color1:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 83 in color2:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 83 in color3:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 83 in color4:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 83 in color5:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 83 in color6 and 83 in color7 and 83 in color8:
                # press and release key up
                keyboard.press(Key.down)

        if 0 in color0:

            # If statement to check the pixel color value
            if 255 in color1:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 255 in color2:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 255 in color3:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 255 in color4:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 255 in color5:
                # press and release key up
                keyboard.press(Key.up)
                # End of the if statement

            # If statement to check the pixel color value
            if 255 in color6 and 83 in color7 and 83 in color8:
                # press and release key up
                keyboard.press(Key.down)

        # Display the picture
        cv2.imshow('images', img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        # cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Call the onMouse function when the window is clicked
        cv2.setMouseCallback('images', on_mouse)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
