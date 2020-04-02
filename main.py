##IMPORTS
import numpy as np
import cv2
import matplotlib.pyplot as plt


roi = None
def selectObject(event,x,y,flags,params):
    global roi, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        ret_now, frame = cap.read()
        roi = cv2.selectROI(frame, False)
        if roi!= None:

            pass



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == True:##This VM has drivers issues between host and VM
        ##TODO Select Object to detect
        cv2.imshow('stream', frame)
        cv2.putText(frame, 'When ready - freeze the frame by pressing the mouse', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
        cv2.setMouseCallback('stream',selectObject)
        cv2.destroyWindow('ROI selector')

        print(roi)
        tracker = cv2.TrackerMedianFlow_create()
        ret = tracker.init(frame, roi)








    if cv2.waitKey(10) & 0xff == ord('q'):
        # press q to exit
        break




#TODO Create tracking like
#TODO color the tracking line for directions

#Stop parameters
## stop params





cap.release()


