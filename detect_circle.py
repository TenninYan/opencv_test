# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import datetime
import numpy as np
 
#small resolution
#VIDEO_WIDTH = 640
#VIDEO_HEIGHT = 480

#high resolution
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 960

fontType = cv2.FONT_HERSHEY_SIMPLEX

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (VIDEO_WIDTH, VIDEO_HEIGHT)
camera.framerate = 2
rawCapture = PiRGBArray(camera, size=(VIDEO_WIDTH, VIDEO_HEIGHT))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	output = image.copy()
	image = cv2.medianBlur(image,9)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,200,
                            param1=50,param2=30,minRadius=100,maxRadius=0)

	# ensure at least some circles were found
	if circles is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")

		(x, y, r) = circles[0]
		cv2.putText(output,"x: "+ str(x) + " y: "+ str(y) + " r: " + str(r),(int(VIDEO_WIDTH/10), int(VIDEO_HEIGHT/10)),fontType,1,(0,0,255), 2,cv2.LINE_AA)
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
