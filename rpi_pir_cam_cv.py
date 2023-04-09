from picamera.array import PiRGBArray
from picamera import PiCamera
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import time
import cv2

pir = MotionSensor(4)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
# capture frames from the camera
while True:
	pir.wait_for_motion()
	print("You moved")
	# capture vid
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break