import cv2

def nothing(n):
    pass

original = cv2.imread('mathAndArt/teammateArt.jpg')
original = cv2.resize(original, dsize=(0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
height, width, channel = original.shape

#Tile size trackbar config
tileSizes = []
for n in range(1, height, 1):
    if height % n == 0 and width % n == 0:
        tileSizes.append(n)
cv2.namedWindow('Original')
cv2.createTrackbar('#Tile', 'Original', 2, len(tileSizes), nothing)
cv2.setTrackbarPos('#Tile', 'Original', 2)
cv2.createTrackbar('Lighting', 'Original', 0, 100, nothing)
cv2.setTrackbarPos('Lighting', 'Original', 0)

while True:
    #init
    tileSize = tileSizes[cv2.getTrackbarPos('#Tile', 'Original') - 1]
    B, G, R = 0, 0, 0
    mosaicRectangle = original.copy()
    mosaicCircle = original.copy()

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
            B += cv2.getTrackbarPos('Lighting', 'Original')
            G /= tileSize ** 2
            G += cv2.getTrackbarPos('Lighting', 'Original')
            R /= tileSize ** 2
            R += cv2.getTrackbarPos('Lighting', 'Original')
            cv2.rectangle(mosaicRectangle, (tileX*tileSize, tileY*tileSize), (tileX*tileSize+tileSize, tileY*tileSize+tileSize), (B, G, R), -1)
            cv2.circle(mosaicCircle, (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2)), int(tileSize/2 + cv2.getTrackbarPos('#Tile', 'Original')), (B, G, R), cv2.FILLED)
            B, G, R = 0, 0, 0
    
    #Display img
    cv2.imshow('Original', original)
    cv2.imshow('Mosaic', mosaicRectangle)
    cv2.imshow('Pointillism', mosaicCircle)

    #exit
    if cv2.waitKey(1) > 0: break

#cache release & close window
cv2.destroyAllWindows()

original = cv2.imread('kittenInSewerWithEyes.jpg')
original = cv2.resize(original, dsize=(0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
height, width, channel = original.shape

cv2.namedWindow('Original')
cv2.createTrackbar('#Tile', 'Original', 2, len(tileSizes), nothing)
cv2.setTrackbarPos('#Tile', 'Original', 2)
cv2.createTrackbar('Lighting', 'Original', 0, 100, nothing)
cv2.setTrackbarPos('Lighting', 'Original', 0)

while True:
    #init
    tileSize = tileSizes[cv2.getTrackbarPos('#Tile', 'Original') - 1]
    B, G, R = 0, 0, 0
    mosaicRectangle = original.copy()
    mosaicCircle = original.copy()

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
            B += cv2.getTrackbarPos('Lighting', 'Original')
            G /= tileSize ** 2
            G += cv2.getTrackbarPos('Lighting', 'Original')
            R /= tileSize ** 2
            R += cv2.getTrackbarPos('Lighting', 'Original')
            cv2.rectangle(mosaicRectangle, (tileX*tileSize, tileY*tileSize), (tileX*tileSize+tileSize, tileY*tileSize+tileSize), (B, G, R), -1)
            cv2.circle(mosaicCircle, (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2)), int(tileSize/2 + cv2.getTrackbarPos('#Tile', 'Original')), (B, G, R), cv2.FILLED)
            B, G, R = 0, 0, 0
    
    #Display img
    cv2.imshow('Original', original)
    cv2.imshow('Mosaic', mosaicRectangle)
    cv2.imshow('Pointillism', mosaicCircle)

    #exit
    if cv2.waitKey(1) > 0: break

#cache release & close window
cv2.destroyAllWindows()

original = cv2.imread('seat88.jpg')
original = cv2.resize(original, dsize=(0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
height, width, channel = original.shape

cv2.namedWindow('Original')
cv2.createTrackbar('#Tile', 'Original', 2, len(tileSizes), nothing)
cv2.setTrackbarPos('#Tile', 'Original', 2)
cv2.createTrackbar('Lighting', 'Original', 0, 100, nothing)
cv2.setTrackbarPos('Lighting', 'Original', 0)

while True:
    #init
    tileSize = tileSizes[cv2.getTrackbarPos('#Tile', 'Original') - 1]
    B, G, R = 0, 0, 0
    mosaicRectangle = original.copy()
    mosaicCircle = original.copy()

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
            B += cv2.getTrackbarPos('Lighting', 'Original')
            G /= tileSize ** 2
            G += cv2.getTrackbarPos('Lighting', 'Original')
            R /= tileSize ** 2
            R += cv2.getTrackbarPos('Lighting', 'Original')
            cv2.rectangle(mosaicRectangle, (tileX*tileSize, tileY*tileSize), (tileX*tileSize+tileSize, tileY*tileSize+tileSize), (B, G, R), -1)
            cv2.circle(mosaicCircle, (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2)), int(tileSize/2 + cv2.getTrackbarPos('#Tile', 'Original')), (B, G, R), cv2.FILLED)
            B, G, R = 0, 0, 0
    
    #Display img
    cv2.imshow('Original', original)
    cv2.imshow('Mosaic', mosaicRectangle)
    cv2.imshow('Pointillism', mosaicCircle)

    #exit
    if cv2.waitKey(1) > 0: break

#cache release & close window
cv2.destroyAllWindows()