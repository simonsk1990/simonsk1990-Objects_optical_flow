#!/usr/bin/python3
##IMPORTS
import cv2
import modules
import time



roi, img = modules.GettingLiveRoi() #check documentation GettingLiveRoi

#setting tracker
tracker = cv2.TrackerKCF_create() #initilizing tracker
ret = tracker.init(img, roi)#after a lot of checks - this tracker should suit our needs,
#other trackers not preforming very well on objects such as pen or phone
#KCF isnt recovering well from failure!
#cosider using camshift tracker? #
#TODO: check camshift and check its preformence



cap = cv2.VideoCapture(0)#start video capture
while True:
#We want 2 things: 1) tracking 2) indicator where the object is moving
#for tracking we will use tracker.update and if tracker succeseded to find var:success will be == True
#for movement indication we will check enviroment of movement of the 4 pixels in the (dx,dy) direction under
#the region of interest. Foe this to work we will wait 1 milisecond between frames to capture the (dx,dy)

    #getting 4 frames
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x, y, w, h) = tuple(map(int, roi))


    ret , frame2 = cap.read()
    _, roi2 = tracker.update(frame2)
    (x2, y2, _, _) = tuple(map(int, roi2))


    ret , frame3 = cap.read()#this happennning fast?? 30 FPS?
    _, roi3 = tracker.update(frame3)
    (x3, y3, _, _) = tuple(map(int, roi3))


    ret, frame4 = cap.read()  # this happennning fast?? 30 FPS?
    _, roi3 = tracker.update(frame4)
    (x4, y4, _, _) = tuple(map(int, roi3))


    movement = modules.colorMovemet(x,x2,x3,x4,y,y2,y3,y4)#see colorMovement documentation
    cv2.putText(frame, movement, (round(x+(w/2)), round(y+(h/2))-10), cv2.FONT_HERSHEY_DUPLEX,0.5,
                    (0, 255, 0), 1)

    if success:
        p1 = (x, y)
        p2 = (x + w, y + h)
    #racrangle
        cv2.rectangle(frame, p1, p2, 0, 3)
    #point for (dx,dy) tracking
        cv2.circle(frame,(round(x+(w/2)),round(y+(h/2))),3,(255,0,0),thickness=-1)

    else:
        # Tracking failure
        cv2.putText(frame, "Failure to Detect Tracking!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

##end while loop
    cv2.putText(frame, 'Tracking - to exit press q', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                (0, 0, 255), 1)
    cv2.imshow('stream2', frame)

    if cv2.waitKey(10) & 0xff == ord('q'):#press q to break
        break




#closing stream
cap.release()
cv2.destroyWindow('stream2')





