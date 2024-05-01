import cv2 as cv

# Reading an image
img = cv.imread('../img/dog.jpg')
cv.imshow('dog', img)
cv.waitKey(0)


# # Reading from video

# cv.namedWindow("preview")
# vc = cv.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv.waitKey(20)
#     if key == 27: # exit on ESC
#         break

# cv.destroyWindow("preview")
# cv.release()



# # Video Reading

# capture = cv.VideoCapture('../videos/cat.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()