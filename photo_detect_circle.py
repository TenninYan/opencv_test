# import the necessary packages
import cv2
import numpy as np
 
image = cv2.imread('photo1.jpg',0)
output = image.copy()
image = cv2.medianBlur(img,5)
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
key = cv2.waitKey(1) & 0xFF

# clear the stream in preparation for the next frame
rawCapture.truncate(0)

# if the `q` key was pressed, break from the loop
if key == ord("q"):
	break
elif key == ord("s"):
	time_now = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d %H:%M:%S')
	print('image_' + time_now + '.jpg')
	cv2.imwrite('image_' + time_now + '.jpg',output)