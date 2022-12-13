# import the necessary packages
import cv2

vid = cv2.VideoCapture(0)

r = 30
#get image from camera
ret, image = vid.read()

orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# perform a naive attempt to find the (x, y) coordinates of
# the area of the image with the largest intensity value
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)
# display the results of the naive attempt
cv2.imshow("Naive", image)
# apply a Gaussian blur to the image then find the brightest
# region

blur = cv2.GaussianBlur(gray, (r, r), 0)


(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = orig.copy()
cv2.circle(image, maxLoc, r, (255, 0, 0), 2)
# display the results of our newly improved method
cv2.imshow("Robust", image)
cv2.waitKey(0)
