# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import datetime
import numpy as np
import detect_wafer
 
#small resolution
#VIDEO_WIDTH = 640
#VIDEO_HEIGHT = 480

#high resolution
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 960

fontType = cv2.FONT_HERSHEY_SIMPLEX

np.set_printoptions(suppress=True)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (VIDEO_WIDTH, VIDEO_HEIGHT)
camera.framerate = 2
rawCapture = PiRGBArray(camera, size=(VIDEO_WIDTH, VIDEO_HEIGHT))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera

counter = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	output, output_array = detect_wafer.detect_wafer(image)

	# show the frame
	#output = cv2.resize(output, (0,0), fx=0.5, fy=0.5)
	if output_array[3] != None:
		counter = 5
		save_array = output_array
		cv2.imshow("Frame", output)
	else:
		counter -= 1
	if counter <= 0:
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
	elif key == ord("w"):
		time_now = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d %H:%M:%S')
		np.savetxt('data_' + time_now + '.csv', save_array, fmt="%.0f", delimiter=",")
