#xu_yang 2020/5/25 cell_detection_1.0.0
#get masked cells image
import cv2 as cv
import shutil
import os
import matplotlib.pyplot as plt
import time
from math_test import area_calculate_from_points
import numpy
from pylab import *
from pixelbetweenpoints import pixel_between_two_points

import tkinter as tk
from tkinter import filedialog


def step1():
    cell_area_hist_list=[]
    print("============Step 1 Start============")
    # 初始化

    path = 'G:\\2020summer\\Project\\Cell_classfication_1.0.0\\Single_Cell'
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            for f in os.listdir(path_file):
                path_file2 = os.path.join(path_file, f)
                if os.path.isfile(path_file2):
                    os.remove(path_file2)

    #-----read-----
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    #img=cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\4.jpg")
    img = cv.imread(file_path)
    img_original=img
    print("Img size: [Width :",img.shape[0],"]","[Height :",img.shape[1],"]")

    img= cv.copyMakeBorder(img,80,450,60,60, cv.BORDER_CONSTANT,value=[255,255,255])
    #img=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

    img_masked=img.copy()
    img_nucleus_white_img=img.copy()

    #-----preprocess-----
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imshow("gray", gray)

    gauss = cv.GaussianBlur(gray, (5, 5), 5)
    #cv.imshow("gauss1",gauss)

    ret, thresh = cv.threshold(gauss, 190, 255, 0)
    cv.imwrite("G:\\2020summer\\Project\\Chromophobe_dataset1\\figure3_left.jpg",thresh)
    #cv.imshow("thresh",thresh)

    erode = cv.erode(thresh, None, iterations=1)
    #cv.imshow("erode",erode)


    #-----remove outlines-----

    #cv.imshow("erode",erode)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            erode[0][j]=255
    #-----find contours-----
    cnts, hierarchy = cv.findContours(erode.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)


    def cnt_area(cnt):
      area = cv.contourArea(cnt)
      return area
    counter_number=0
    location_cells_center={}
    area_of_cells_nucleus=[]
    Whole_pic_cell_area_ave_percent=[]
    Whole_pic_cell_color_ave = []
    for i in range(0, len(cnts)):
        if 250 <= cnt_area(cnts[i]) <= 0.2*(img.shape[0]*img.shape[1]):


            cell_area_hist_list.append(cnt_area(cnts[i]))
            #print(cnts[i])
            #cell_area_hist_list.append(area_calculate_from_points(cnts[i]))
            counter_number+=1
            #print(cnts[i])
            #print("======")
            cv.drawContours(img_masked, cnts[i], -1, (0, 0, 255), 2) #draw contours
            cv.drawContours(img_nucleus_white_img, [cnts[i]], -1, (255, 255, 255), -1)#masked white
            M = cv.moments(cnts[i])


            #检索每个细胞的内部颜色
            x, y, w, h = cv.boundingRect(cnts[i])


            #cv.imshow('single_cell', newimage)

            cell_area_percent=0

            for row in range (y,y+h):
                for col in range(x,x+w):
                    result = cv.pointPolygonTest(cnts[i], (col, row), False)
                    if result==-1:

                        cv.circle(gray, (col, row), 1, 255, -1)
                        cv.circle(img, (col, row), 1, (255,255,255), -1)
                        cell_area_percent+=1
            cv.rectangle(img, (x, y), (x + w, y + h), (153, 153, 0), 1)
            newimage_gray = gray[y:y + h, x:x + w]
            cv.imwrite("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\Single_Cell\\"+str(counter_number)+".jpg",newimage_gray)
            Single_Cell_Color_Distrution=[]
            for row in range (h):
                for col in range(w):
                    if newimage_gray[row,col]!=255:
                        Single_Cell_Color_Distrution.append(newimage_gray[row,col])

            '''
            plt.hist(Single_Cell_Color_Distrution,bins=50)
            plt.title(str(counter_number))
            plt.show()
            '''
            #print("this cell area percent= ",str(cell_area_percent/(w*h)))
            numpy.set_printoptions(precision=3)
            Whole_pic_cell_area_ave_percent.append(cell_area_percent/(w*h))
            Whole_pic_cell_color_ave.append(numpy.mean(Single_Cell_Color_Distrution))
            """#找出masked细胞内点的坐标
            rect = cv.minAreaRect(cnts[i])
            cx, cy = rect[0]
            box = cv.boxPoints(rect)
            box = np.int0(box)
            cv.drawContours(img_masked, [box], 0, (0, 0, 255), 2)
            #cv.circle(img_masked, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)

            box_gray_color=[]
            for by in range(box[2][1],box[0][1]+1):
                for bx in range(box[1][0],box[3][0]+1):
                    #print(bx,by)
                    #cv.circle(img_masked,(bx, by), 1, (255, 0, 0), 2, 8, 0)
                    box_gray_color.append(gray[bx,by])
            plt.hist(box_gray_color)

            plt.hist(box_gray_color,bins=50)
            plt.title(str(counter_number))
            plt.show()

            dist=cv.pointPolygonTest(cnts[i],(50,50),True)
            """
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv.circle(img_masked, (cX, cY), 3, (255, 255, 255), -1)
                cv.putText(img_masked, str(counter_number), (cX - 20, cY - 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                area_of_cells_nucleus.append(cnt_area(cnts[i]))
                location_cells_center[counter_number]=[cX,cY]
            except:
                pass
            if counter_number==1:
                x1=cX
                y1=cY
            if counter_number==2:
                x2=cX
                y2=cY
            if counter_number==20:
                x_sample=cX
                y_sample=cY

            #cv.drawContours(img_masked, [cnts[i]], -1, (255, 255, 255), -1)#mask contours
    print("Whole pic average cell nucleus area percent: ", Whole_pic_cell_area_ave_percent)
    print("Whole pic average cell nucleus area percent_ave: ", numpy.mean(Whole_pic_cell_area_ave_percent))
    print("Whole pic average cell nucleus color deep percent: ", Whole_pic_cell_color_ave)
    print("Whole pic average cell nucleus color deep percent_ave: ", numpy.mean(Whole_pic_cell_color_ave))
    cv.imshow('single_cell', img)
    #-----put Text-----
    print("total cells number : ", counter_number)

    #cv.line(img_masked, (x1,y1), (x2,y2), (0,0,255), 2)

    list_of_two_points=pixel_between_two_points(x1,x2,y1,y2)

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
        #print(height)
        height_of_two_points.append(height)
    img_sample=img.copy()
    cv.circle(img_sample, (x_sample, y_sample), 3, (0, 0, 255), -1)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img_sample, "Sample_Point",(x_sample - 20, y_sample - 20),font, 0.7, (255, 255, 255), 2)
    #cv.imshow("img_sample_location_RED_DOT", img_sample)


    # save to local
    f = open("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\dict.txt", 'w')
    f.write(str(location_cells_center))
    f.close()


    # < list save
    file1 = open('area_of_nucleus.txt', 'w')
    for fp in area_of_cells_nucleus:
        file1.write(str(fp))
        file1.write('\n')
    file1.close()
    # list save >




    cv.imwrite("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp.bmp",img_masked)
    cv.imwrite("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp_1.bmp",img_nucleus_white_img)
    cv.imwrite("G:\\2020summer\\Project\\Chromophobe_dataset1\\figure3_right.jpg", img_masked)
    #================hist of cells area==================
    #plt.hist(cell_area_hist_list)
    #plt.show()

    #=================================
    #-----
    #=================================UI/
    cv.putText(img_masked, "Overview", (80, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    image_size_text="Image size: [Width :"+str(img_original.shape[0])+"]"+"[Height :"+str(img_original.shape[1])+"]"
    cv.putText(img_masked, image_size_text, (80, img.shape[0]-400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv.putText(img_masked, "Total cells number: "+str(counter_number), (80, img.shape[0]-350), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv.putText(img_masked, "Close window to continue", (80, img.shape[0]-250), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)
    #=================================/UI
    cv.imshow('img_copy', img_masked)
    print("============Step 1 End============")
    cv.waitKey()
    return counter_number
step1()