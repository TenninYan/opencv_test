# import the necessary packages
import cv2
import numpy as np
import datetime
import detect_wafer
 
np.set_printoptions(suppress=True)

image = cv2.imread('photo6.jpg',1)

output, output_array = detect_wafer.detect_wafer(image)
#output = detect_wafer.detect_wafer(image)

# show the frame
cv2.imshow("Frame", output)
print (output_array)
key = cv2.waitKey(0)
if key == ord("q"):
	cv2.destroyAllWindows()
elif key == ord("s"):
	time_now = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d %H:%M:%S')
	print('image_' + time_now + '.jpg')
	cv2.imwrite('image_' + time_now + '.jpg',output)
elif key == ord("w"):
	time_now = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d %H:%M:%S')
	np.savetxt('data_' + time_now + '.csv', output_array, fmt="%.0f", delimiter=",")

