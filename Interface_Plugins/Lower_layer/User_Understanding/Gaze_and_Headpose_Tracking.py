#Gase and head pose detection with 
#OpenCV and dlib
#from V.Agarwal

import cv2 
import dlib
import numpy as np
import threading
import sys



class User_Tracking(object):

	def __init__(self):

		self.predictor_file = 'C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/Interface_Plugins/Lower_layer/Workspace_Understanding/Predictors/shape_predictor_68_face_landmarks'
      	
      	self.detector = dlib.get_frontal_face_detector()

      	self.predictor = dlib.shape_predictor(self.predictor_file)

      	self.left = [36, 37, 38, 39, 40, 41]

      	self.right = [42, 43, 44, 45, 46, 47]




    def initialization(self):

    	self.cap = cv2.VideoCapture(0)
    	self.ret, self.img = self.cap.read()
        self.thresh = img.copy() # Tengo que revisar esto, es el threshold para el brightness
        cv2.namedWindow('image')
        self.kernel = np.ones((9, 9), np.uint8)
        cv2.createTrackbar('threshold', 'image', 0, 255, nothing)


    def nothing(self, x):

    	pass



    def process(self):

    	while(True):

    		ret, img = cap.read()
    		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    		rects = detector(gray, 1)
    		for rect in rects:

    			shape = predictor(gray, rect)
    			shape = shape_to_np(shape)
    			mask = np.zeros(img.shape[:2], dtype=np.uint8)
    			mask = eye_on_mask(mask, left)
    			mask = eye_on_mask(mask, right)
    			mask = cv2.dilate(mask, kernel, 5)
    			eyes = cv2.bitwise_and(img, img, mask=mask)
    			mask = (eyes == [0, 0, 0]).all(axis=2)
    			eyes[mask] = [255, 255, 255]
    			mid = (shape[42][0] + shape[39][0]) // 2
    			ees_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
    			threshold = cv2.getTrackbarPos('threshold', 'image')
    			_, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
    			thresh = cv2.erode(thresh, None, iterations=2) #1
    			thresh = cv2.dilate(thresh, None, iterations=4) #2
    			thresh = cv2.medianBlur(thresh, 3) #3
    			thresh = cv2.bitwise_not(thresh)
    			contouring(thresh[:, 0:mid], mid, img)
    			contouring(thresh[:, mid:], mid, img, True)
    			# for (x, y) in shape[36:48]:
    			# cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
    		# show the image with the face detections + facial landmarks
    		cv2.imshow('eyes', img)
    		cv2.imshow("image", thresh)
    		if cv2.waitKey(1) & 0xFF == ord('q'):
    			break



	def shape_to_np(self, shape, dtype="int"):

		# initialize the list of (x, y)-coordinates
		coords = np.zeros((68, 2), dtype=dtype)
		# loop over the 68 facial landmarks and convert them
		# to a 2-tuple of (x, y)-coordinates
		for i in range(0, 68):

			coords[i] = (shape.part(i).x, shape.part(i).y)
		return coords

	def eye_on_mask(mask, side):

		points = [shape[i] for i in side]
		points = np.array(points, dtype=np.int32)
		mask = cv2.fillConvexPoly(mask, points, 255)
		return mask

	def contouring(thresh, mid, img, right=False):

		cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
		try:
			cnt = max(cnts, key = cv2.contourArea)
			M = cv2.moments(cnt)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			if right:
				cx += mid
			cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
		except:
			pass



	def start(self):

		self.go_on = True


	def pause(self):

        self.go_on = False


    def launch_thread(self):

    	self.t = threading.Thread(target = self.process)
        self.t.start()





	




	




