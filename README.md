# simonsk1990-Objects_optical_flow
Objects_Optical_Flow
Tracking objects and movement direction using KCF traker - see more documentation inside main and modules.
instructions appear on screen - terminal run python main.py (using webcam)

#TODO: 
def GettingLiveRoi(): - I used mouse events EVENT_LBUTTONDOWN
to stop frame, would suggest using ord('c') for charecter rather
then mouse event

def colorMovemet() workaround to object direction tracking.
Tried various methods including math.ata2() for alpha,
Dense Optical Flow inside roi to track color movement,
none with ok result, tracking 4 pixles direction gave ok
result.
Would suggest adding more directions.

