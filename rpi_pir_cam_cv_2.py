import cv2
from gpiozero import MotionSensor

def video_feed(): 
    # define a video capture object
    vid = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # output the frame
        out.write(hsv) 
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

while True:
	pir.wait_for_motion()
	print("You moved")
    video_feed()
	pir.wait_for_no_motion()