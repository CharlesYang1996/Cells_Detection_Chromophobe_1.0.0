#xu_yang 2020/5/25 cell_detection_1.0.0
#get masked cells image
import cv2 as cv
import matplotlib.pyplot as plt

from pylab import *
from pixelbetweenpoints import pixel_between_two_points
#-----read-----
img=cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\1.jpg")
#img=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

img_masked=img.copy()
cv.imshow("img", img)
#-----preprocess-----
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
cv.imshow("gauss1",gauss)

ret, thresh = cv.threshold(gauss, 180, 255, 0)
cv.imshow("thresh",thresh)

erode = cv.erode(thresh, None, iterations=2)
cv.imshow("erode",erode)
#-----remove outlines-----
print(erode[0][0])
cv.imshow("erode",erode)
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        erode[0][j]=255
#-----find contours-----
cnts, hierarchy = cv.findContours(erode.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)


def cnt_area(cnt):
  area = cv.contourArea(cnt)
  return area
counter_number=0
for i in range(0, len(cnts)):
    if 200 <= cnt_area(cnts[i]) <= 0.8*(img.shape[0]*img.shape[1]):
        counter_number+=1
        #print(cnts[i])
        #print("======")
        cv.drawContours(img_masked, cnts[i], -1, (0, 0, 255), 2) #draw contours
        M = cv.moments(cnts[i])
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv.circle(img_masked, (cX, cY), 3, (255, 255, 255), -1)
            cv.putText(img_masked, str(counter_number), (cX - 20, cY - 20),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        except:
            pass
        if counter_number==40:
            x1=cX
            y1=cY
        if counter_number==36:
            x2=cX
            y2=cY
        #cv.drawContours(img_masked, [cnts[i]], -1, (255, 255, 255), -1)#mask contours
#-----put Text-----
print("total cells number : ", counter_number)

cv.line(img_masked, (x1,y1), (x2,y2), (0,0,255), 2)

list_of_two_points=pixel_between_two_points(x1,x2,y1,y2)
print(list_of_two_points)

#-----output information on the line
height_of_two_points=[]
height_of_two_points_B=[]
height_of_two_points_G=[]
height_of_two_points_R=[]

for m in range(0,len(list_of_two_points)):
    height = img[list_of_two_points[m][1], list_of_two_points[m][0]]
    try:
        height_B=img[list_of_two_points[m][1],list_of_two_points[m][0]][0]
        height_G = img[list_of_two_points[m][1], list_of_two_points[m][0]][1]
        height_R = img[list_of_two_points[m][1], list_of_two_points[m][0]][2]
        height_of_two_points_B.append(height_B)
        height_of_two_points_G.append(height_G)
        height_of_two_points_R.append(height_R)
    except:
        pass
    print(height)
    height_of_two_points.append(height)
plt.plot(height_of_two_points,color="black")
plt.show()
try:
    plt.plot(height_of_two_points_B, color="blue")
    plt.plot(height_of_two_points_G, color="green")
    plt.plot(height_of_two_points_R, color="red")

    plt.show()
except:
    pass

cv.circle(img, (x2, y2), 3, (0, 0, 0), -1)

cv.imshow("img_test", img)
print("x1:",x1," y1",y1)
print("x2:",x2," y2",y2)
print("x1 y1  color: ",img[y1][x1])
print("x1 y1  color B: ",img[y1][x1][0])
print("x1 y1  color G: ",img[y1][x1][1])
print("x1 y1  color R: ",img[y1][x1][2])
print("x2 y2  color: ",img[y2][x2])




#-----
cv.imshow('img_copy', img_masked)
cv.imwrite("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp.jpg",img_masked)
#==================================






cv.waitKey()



