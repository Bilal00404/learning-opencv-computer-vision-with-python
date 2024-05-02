# resize and reshale images and videos in opencv

import cv2 as cv

# resize frame function 
def rescale_frame(frame, scale=0.75):
    '''Works for images, videos and live videos'''
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height) 
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def chenge_res(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)


# Reading video
capture = cv.VideoCapture('videos/waterfall.mp4')

while True:
    isTrue, frame = capture.read()

    resized_frame = rescale_frame(frame, scale=0.2)
    
    cv.imshow('video', frame)
    cv.imshow('video resized', resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()