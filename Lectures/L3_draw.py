import cv2 as cv
import numpy as np

# create a blank image
blank = np.zeros((400,600,3), dtype='uint8')
cv.imshow('Blank', blank)

# # paint a color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# # draw a solid rectange
# blank[0:200, 0:300] = 0,255,0
# cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (200,200), (0,0,255), thickness=1)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
cv.imshow('rectangle', blank)

# thickness=cv.FILLED, thickness=-1


# # draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('circle', blank)

# # draw a line
# cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.line(blank, (100,100), (300,300), (255,255,255), thickness=3)
# cv.imshow('line', blank)

# # put text on image
# cv.putText(blank, 'hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow('text', blank)

cv.waitKey(0)