import numpy as np
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

capture = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

capture.set(3, 1200)
capture.set(4, 720)

background = cv.imread('resources\Background.png')
background = cv.resize(background, (int(capture.get(3)), int(capture.get(4))))
ball = cv.imread('resources\Ball.png', cv.IMREAD_UNCHANGED)
bat1 = cv.imread('resources\Bat1.png', cv.IMREAD_UNCHANGED)
bat2 = cv.imread('resources\Bat2.png', cv.IMREAD_UNCHANGED)
gameover = cv.imread('resources\GameOver.png')

position=[100,100]
isOver = False
speedX, speedY = 10,10
score = [0,0]

while True:
    isTrue, frame = capture.read()
    frame = cv.flip(frame, 1)
    hands, frame = detector.findHands(frame, flipType=False)

    frame = cv.addWeighted(frame, 0.5, background, 0.5, 0.0)

    cv.imshow('Pong Game', frame)
    
    key = cv.waitKey(1)

    if key == ord('q'):
        break