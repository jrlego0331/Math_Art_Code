import cv2
import numpy as np

def skip(n):
    pass

#cam config
cam = cv2.VideoCapture(int(input('Enter 0 for default webcam\n')))
width, height = 640, 480
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

tileSize = 6

while True:
    #camread
    ret, original = cam.read()
    pointillism = np.zeros((height, width, 3), np.uint8)
    cv2.rectangle(pointillism, (0,0), (width, height), (255,255,255), cv2.FILLED)
    B, G, R = 0, 0, 0

    #BGR Extraction & drawing shapes
    for tileX in range(int(width/tileSize)):
        for tileY in range(int(height/tileSize)):
            for pixelX in range(tileSize):
                for pixelY in range(tileSize):
                    pos = tileY*tileSize+pixelY, tileX*tileSize+pixelX
                    B += int(original[pos][0])
                    G += int(original[pos][1])
                    R += int(original[pos][2])
            B /= tileSize ** 2
            G /= tileSize ** 2
            R /= tileSize ** 2
            brightness = 1 - (B+G+R) / (255*3)

            r = int(tileSize * brightness)
            circleMid = (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2))
            cv2.circle(pointillism, circleMid, r, (0, 0, 0), cv2.FILLED)
            B, G, R = 0, 0, 0
    
    #Display img
    cv2.imshow('Pointillism Vison', cv2.hconcat([original, pointillism]))

    #exit
    if cv2.waitKey(1) > 0: break

#cache release & close window
cam.release()
cv2.destroyAllWindows()