import cv2 as cv

img = cv.imread('img/car_resized.jpg')
cv.imshow('image', img)

# # converting to grayscale
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray_image', gray_img)


# # blur image
# # kernal size must be odd number (change kernel size to see bluring effects)
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)


# # edge cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny', canny)


# # dilating the image
# dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('dilated', dilated)

# # eroding
# eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('erode', eroded)


# resize image
# resized = cv.resize(img, (720, 460), interpolation=cv.INTER_AREA)
# # cv.INTER_LINEAR, cv.INTER_CUBIC used when output image is has more resolutoion than the input image
# cv.imshow('resized', resized)


# # cropping
# cropped = img[200:500, 200:900]
# cv.imshow('cropped', cropped)

cv.waitKey(0)