import cv2

roi = None
roi_img = None
def GettingLiveRoi():

    close = 0
    def selectObject(event,x,y,flags,params):
        global roi, roi_img
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.putText(frame, 'select the object and press enter twice,', (20, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            roi = cv2.selectROI(frame, False)
            roi_img = frame[roi[1]:roi[1]+roi[3],roi[0]:roi[0]+roi[2]]
            pass


    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret == True:##This VM has drivers issues between host and VM
            ##TODO Select Object to detect LIVE!
            cv2.putText(frame, 'When ready - freeze the frame by pressing the mouse,', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.imshow('stream',frame)
            cv2.setMouseCallback('stream',selectObject)
            cv2.destroyWindow('ROI selector')
            print(roi)
            if roi != None:
                close =1

        if cv2.waitKey(10) & close ==1 :
            break
    cap.release()
    cv2.destroyAllWindows()
    return roi , roi_img
