##IMPORTS
import cv2
import modules




roi, img = modules.GettingLiveRoi()
print('roi is {}'.format(roi))
cap = cv2.VideoCapture(0)
while True:
    ret, frame_now = cap.read()
    cv2.putText(frame_now, 'Tracking - to exit press q', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                (0, 0, 255), 1)
    cv2.imshow('stream2',frame_now)


    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyWindow('stream2')




