##IMPORTS
import cv2
import modules
import numpy as np
import matplotlib.pyplot as plt



roi, img = modules.GettingLiveRoi()
print('roi is {}'.format(roi))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#setting tracker
tracker = cv2.TrackerKCF_create()
ret = tracker.init(img, roi)#after a lot of checks - this tracker should suit our needs,
#other trackers not preforming very well on objects such as pen or phone
#KCF isnt recovering well from failure!
#cosider using camshift tracker? # to do and check its preformence



cap = cv2.VideoCapture(0)
ret, old_frame = cap.read() #for direction update
while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x, y, w, h) = tuple(map(int, roi))
    if success:

        #COLOR
        ret , frame2 = cap.read()
        prev_img = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
        next_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        hsvMask = np.zeros_like(old_frame)
        hsvMask[:,:,1] = 255
        flow = cv2.calcOpticalFlowFarneback(prev_img, next_img, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1], angleInDegrees=True)
        hsvMask[:, :, 0] = cv2.normalize(ang, None, 0, 255, cv2.NORM_MINMAX)
        hsvMask[:, :, 2] = 255
        bgr = cv2.cvtColor(hsvMask, cv2.COLOR_HSV2BGR)
        color = int(hsvMask[2,0,0])
        #drawRacktangle()
        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(frame, p1, p2,3)

        #point
        cv2.circle(frame,(round(x+(w/2)),round(y+(h/2))),3,(255,0,0),thickness=-1)

        prvsImg = next_img



    else:
        # Tracking failure
        cv2.putText(frame, "Failure to Detect Tracking!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)




##end while loop
    cv2.putText(frame, 'Tracking - to exit press q', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                (0, 0, 255), 1)
    cv2.imshow('stream2', frame)



    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyWindow('stream2')




## todo create traker

