#Create a circle around the nucleus and walk through all the rays coming from the center, looking for the cell wall
#Xu_Yang 2020.8.11

import math_test
import cv2 as cv
from math_test import *
from pylab import *
from pixelbetweenpoints import pixel_between_two_points


img=cv.imread("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp_1.jpg")
#img=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

cv.imshow("img", img)
#-----preprocess-----
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)

#cv.imshow("gauss1",gauss)
#print("gauss_test: ",gauss[361][616])
'''
x_sample = :  616
y_sample = :  361
'''
img_shape=gauss.shape
print(img_shape[0],img_shape[1])
x_sample = 50
y_sample = 60
angle_temp_list=angle_round(x_sample,y_sample,35)#第三个参数为圆的半径
contour_cell=[]

for i in range(1,73):
    x1=angle_temp_list[i-1][0]
    y1 = angle_temp_list[i - 1][1]
    cx=x_sample
    cy=y_sample
    temp_list=pixel_between_two_points(cx,round(x1),cy,round(y1))

    ray_lenth = 0
    compare_distance_value=0
    compare_color_value=255
    color_hist=[]

    for m in range(0,len(temp_list)):
        x_temp=temp_list[m][0]
        y_temp=temp_list[m][1]



        single_lenth=cell_wall_ray_lenth(cx,cy,x_temp,y_temp)
        if gauss[y_temp][x_temp] <= compare_color_value:
            compare_color_value =gauss[y_temp][x_temp]
            compare_distance_valuevalue=single_lenth

            x_final=x_temp
            y_final=y_temp
        else:
            pass
        #==hist graph
        color_hist.append(gauss[y_temp][x_temp])
    #plt.plot(color_hist, color="black")
    #plt.show()
    cv.circle(img, (round(x_final), round(y_final)), 3, (0, 0, 255), -1)

    #cv.circle(img, (round(x1), round(y1)), 3, (0, 0, 255), -1) #半径显示
cv.imshow("img_test_round", img)




cv.waitKey()