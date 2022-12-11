# import the opencv library
import cv2
import serial
import time
import numpy as np

arduino = serial.Serial(port='/dev/cu.usbmodem144401', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(str(x), 'utf-8'))
    time.sleep(0.05)

positions = []

# define a video capture object
vid = cv2.VideoCapture(0)

for x in range(0, 500):

    # Capture the video frame
    # by frame
    write_read(x)

    ret, frame = vid.read()

    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    print(maxLoc)
    positions.append(maxLoc)
    cv2.circle(frame, maxLoc, 5, (0, 0, 255), 2)
    # display the results of the naive attempt

    # Display the resulting frame
    #image = cv2.circle(frame, coords, radius=0, color=(0, 0, 255), thickness=-1)
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

# find the max value x and y coordinates
max_x = max(positions, key=lambda item:item[0])[0]
max_y = max(positions, key=lambda item:item[1])[1]

# load img.png
img = cv2.imread('img.png')

#rotate image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# resize the image to the max x and y coordinates
img = cv2.resize(img, (max_x+1, max_y+1))

print(img.shape)
print(max_x, max_y)
#show the image with opencv
cv2.imshow('image', img)

input("Press Enter to continue...")

# loop through the positions and turn the pixels on if they are white
for idx, position in enumerate(positions):
    if img[position[1], position[0]][0] > 10 or img[position[1], position[0]][1] > 10 or img[position[1], position[0]][2] > 10:
        write_read(idx)
        print("written")
