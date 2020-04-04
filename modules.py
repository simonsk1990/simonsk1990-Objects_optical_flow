#Modules file

#imports
import cv2

#initializing parameters
roi = None
roi_img = None
def GettingLiveRoi():
    '''
    Calling this function will start a live camera stream to select region of interest - roi
    instructions on capturing will pre presented on the screen
    :returns: roi (tuple): (x,y,width,height)
              roi_img - an img of the roi

    '''
    close = 0 #need this parameter to close getting live stream
    def selectObject(event,x,y,flags,params):
        '''
        interactive event function checking if mouse was pressed
        '''
        global roi, roi_img
        if event == cv2.EVENT_LBUTTONDOWN: #checking if user was ready in the stream with the object
            ret_roi, frame_roi = cap.read()
            cv2.putText(frame_roi, 'select the object and press enter twice,', (20, 20),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.putText(frame_roi, 'keep the object still during the selection,', (20, 40),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

            roi = cv2.selectROI(frame_roi, False)
            roi_img = frame_roi
            pass


    cap = cv2.VideoCapture(0) #start capture
    while True:
        ret, frame = cap.read()
        if ret == True:##This VM has drivers issues between host and VM
            cv2.putText(frame, 'When ready - freeze the frame by pressing the mouse,', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.imshow('stream',frame)
            cv2.setMouseCallback('stream',selectObject) #if mouse was pressed - select roi
            cv2.destroyWindow('ROI selector') #after roi was selected - kill this window
            print(roi) #todo - remove this check at the end
            if roi != None:
                close =1

        if cv2.waitKey(10) & close ==1 : #if we have roi (couldn't check with roi variable itself)
            break
    cap.release()
    cv2.destroyWindow('stream') #kill everything
    return roi , roi_img




def drawTrackingRacktangle():
    pass

