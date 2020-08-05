import cv2 as cv

img=cv.imread("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp.jpg")

cv.imshow("img", img)
#-----preprocess-----
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
cv.imshow("gauss1",gauss)

ret, thresh = cv.threshold(gauss, 203, 255, 0)
cv.imshow("thresh",thresh)

erode = cv.erode(thresh, None, iterations=2)
cv.imshow("erode",erode)

cv.waitKey()