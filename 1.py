import cv2

cam = cv2.VideoCapture(0)

while True:
	ret, img = cam.read()

	cv2.imwrite("Artem.png", img)
	# cv2.imshow('')
	break