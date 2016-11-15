# import the necessary packages
import cv2
import numpy as np
 
image = cv2.imread('photo1.png',1)
output = image.copy()
image = cv2.medianBlur(image,5)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,600,
                    param1=50,param2=30,minRadius=100,maxRadius=0)

# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")

	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1) 

# show the frame
cv2.imshow("Frame", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
