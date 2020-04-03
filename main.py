##IMPORTS
import cv2
import modules
import matplotlib.pyplot as plt



roi, img = modules.GettingLiveRoi()
print('roi is {}'.format(roi))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#setting tracker
tracker = cv2.TrackerKCF_create()#after a lot of checks - this tracker should suit our needs
#KCF isnt recovering well from failure!
ret = tracker.init(img, roi)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x, y, w, h) = tuple(map(int, roi))
    if success:
        # Tracking success
        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)
    else:
        # Tracking failure
        cv2.putText(frame, "Failure to Detect Tracking!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.putText(frame, 'Tracking - to exit press q', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                (0, 0, 255), 1)
    cv2.imshow('stream2', frame)



    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyWindow('stream2')




