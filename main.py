##IMPORTS
import numpy as np
import cv2
import matplotlib.pyplot as plt


##TODO start capture

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == True:##This VM has drivers issues between host and VM
        cv2.imshow('stream',frame)

        if cv2.waitKey(10) & 0xff == ord('q'):
            # press q to exit
            break


    else:
        print('cant capture video')


cv2.destroyAllWindows()
cap.release()

plt.show()

##TODO Select Object to detect
# will use Dense optical flow to calcute the histogram area around (window size small for laptopcam)




#TODO start tracking
#make sure rectangle changes size



#TODO Create tracking like



#TODO color the tracking line for directions

