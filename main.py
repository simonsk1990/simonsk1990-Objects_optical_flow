##IMPORTS
import numpy as np
import cv2
import matplotlib.pyplot as plt

def selectObject(event,x,y,flags,params):
    global roi
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.destroyWindow('stream')
        cv2.putText(frame, 'select region and press enter', (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
        roi = cv2.selectROI(frame, False)






cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == True:##This VM has drivers issues between host and VM
        ##TODO Select Object to detect
        roi = None
        cv2.putText(frame, 'When ready - freeze the frame by pressing the mouse', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
        cv2.imshow('stream', frame)
        cv2.setMouseCallback('stream', selectObject)
        cv2.destroyWindow('ROI selector')
        if roi != None:
            break








#TODO Create tracking like
#TODO color the tracking line for directions

#Stop parameters
## stop params

    if cv2.waitKey(10) & 0xff == ord('q'):
        # press q to exit
        break

cv2.destroyAllWindows()
cap.release()

