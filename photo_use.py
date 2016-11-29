# import the necessary packages
import cv2
import numpy as np
import datetime
import detect_wafer
 
image = cv2.imread('photo1.png',1)

output = detect_wafer.detect_wafer(image)

# show the frame
cv2.imshow("Frame", output)
key = cv2.waitKey(0)
if key == ord("q"):
	cv2.destroyAllWindows()
elif key == ord("s"):
	time_now = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d %H:%M:%S')
	print('image_' + time_now + '.jpg')
	cv2.imwrite('image_' + time_now + '.jpg',output)

