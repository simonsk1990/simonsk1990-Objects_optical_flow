##IMPORTS
import cv2
import modules
import numpy as np
import matplotlib.pyplot as plt
import math



roi, img = modules.GettingLiveRoi()
# print('roi is {}'.format(roi))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#setting tracker
tracker = cv2.TrackerKCF_create()
ret = tracker.init(img, roi)#after a lot of checks - this tracker should suit our needs,
#other trackers not preforming very well on objects such as pen or phone
#KCF isnt recovering well from failure!
#cosider using camshift tracker? # to do and check its preformence



cap = cv2.VideoCapture(0)
ret, old_frame = cap.read()
(x_old, y_old, w, h) = tuple(map(int, roi))
x_old = round(x_old+(w/2))
y_old = round(y_old+(h/2))
while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x, y, w, h) = tuple(map(int, roi))
    # COLOR with coordinates
    color = 0
    x_new = round((x) + (w / 2))
    y_new = round((y) + (h / 2))
    if x_new==x_old:
        dDegrees = 0
    else:
        dRadians = math.atan2((y_new-y_old),(x_new-x_old))
        dDegrees = math.degrees(dRadians)
    print(dDegrees)



    if success:
    #     if x_new > x_old and y_new > y_old:
    #         color = (255,0,0)
    #     if x_new < x_old and y_new > y_old:
    #         color = (0,255,0)
    #     if x_new < x_old and y_new < y_old:
    #         color = (0,0,255)
    #     if x_new > x_old and y_new < y_old:
    #         color = (255,255,0)
    #     print(color)

    # COLOR

        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(frame, p1, p2, color, 3)

    #point
        cv2.circle(frame,(round(x+(w/2)),round(y+(h/2))),3,(255,0,0),thickness=-1)
        x_old = x_new
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

