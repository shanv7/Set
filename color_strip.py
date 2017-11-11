import cv2
import numpy as np
numcards = 9
ids = np.zeros((4,numcards))

white_MIN = np.array([100, 100, 100], np.uint8)
white_MAX = np.array([255, 255, 255], np.uint8)


for k in range(1,10):
	image=cv2.imread(str(k)+".jpg")
	dst = cv2.inRange(image, white_MIN, white_MAX)
	rows,cols,channel=image.shape
	no_white = cv2.countNonZero(dst)
	print(no_white)
	#print('The number of white pixels is: ' + str(no_white))
	#rows,cols,channels=image.shape
	#print(rows,cols)
	if no_white>=150000:

		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		blur = cv2.pyrMeanShiftFiltering(image,9,33)
		gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
		flag,thresh=cv2.threshold(gray,110,255,cv2.THRESH_BINARY)
		img , contours,_ =cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		a = sorted(contours,key=cv2.contourArea)
		#cv2.imshow('img',img)
		print ("number of contour detected %d -> " %len(contours))
		cv2.drawContours(image,contours,0,(0,0,255),6)
		cv2.imshow('ar',thresh)

		if len(contours)>12:
			print("The image has stripes")
		else:
			print("The image is a solid color")
	else:
		print("The image is empty")

	cv2.waitKey(0)
	cv2.destroyAllWindows()