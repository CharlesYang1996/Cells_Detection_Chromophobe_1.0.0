#Create a circle around the nucleus and walk through all the rays coming from the center, looking for the cell wall
#Xu_Yang 2020.8.11

import math_test
import cv2 as cv
from math_test import *
from pylab import *

from pixelbetweenpoints import pixel_between_two_points
def step2(cell_id):

    print("============Step 2 Start============")

    img=cv.imread("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp_1.bmp")
    img_result=img.copy()
    #img=cv.cvtColor(img,cv.COLOR_BGR2BGRA)


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


    # read from local
    f = open("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\dict.txt", 'r')
    dict_ = eval(f.read())
    f.close()

    # distance from single point to center
    distance_from_single_point_to_center_list=[]
    result_dot_location_x_y =[]
    for m in range(cell_id,cell_id+1):
        x_sample = dict_[m][0]
        y_sample = dict_[m][1]
        angle_temp_list = angle_round(x_sample, y_sample, 65)  # 第三个参数为圆的半径

        for i in range(1,73):
            x1=angle_temp_list[i-1][0]
            y1 = angle_temp_list[i - 1][1]
            cx=x_sample
            cy=y_sample
            temp_list=pixel_between_two_points(cx,round(x1),cy,round(y1))
            #print(len(temp_list))
            ray_lenth = 0
            compare_distance_value=0
            compare_color_value=255
            color_hist=[]
            #单条射线的所有点，颜色深度的集合，找出前三名
            color_deep_rank={}
            for m in range(0,len(temp_list)):
                x_temp=temp_list[m][0]
                y_temp=temp_list[m][1]
                single_lenth=cell_wall_ray_lenth(cx,cy,x_temp,y_temp)
                color_deep_rank[y_temp, x_temp] = gauss[y_temp][x_temp]
                sorted_color_deep_rank = sorted(color_deep_rank.items(), key=lambda kv: (kv[1], kv[0]), reverse=False)

                if gauss[y_temp][x_temp] <= compare_color_value:
                    compare_color_value =gauss[y_temp][x_temp]
                    compare_distance_valuevalue=single_lenth

                    x_final=x_temp
                    y_final=y_temp
                else:
                    pass
                #==hist graph
                color_hist.append(gauss[y_temp][x_temp])

            #print("**************** test: compare_color_value: ", compare_color_value,"dic rank: ", sorted_color_deep_rank[0],sorted_color_deep_rank[1],sorted_color_deep_rank[2])
            #plt.plot(color_hist, color="black")
            #plt.show()
            cv.circle(img, (round(x_final), round(y_final)), 1, (0, 0, 255), -1)

            if i==55:
                cv.circle(img, (round(x_final), round(y_final)), 1, (0, 255, 0), -1)
            #cv.circle(img, (round(sorted_color_deep_rank[1][0][1]), round(sorted_color_deep_rank[1][0][0])), 1, (0, 255, 255), -1)
            #cv.circle(img, (round(sorted_color_deep_rank[2][0][1]), round(sorted_color_deep_rank[2][0][0])), 1, (0, 255, 255), -1)
            #cv.circle(img, (round(sorted_color_deep_rank[3][0][1]), round(sorted_color_deep_rank[3][0][0])), 1,(0, 255, 255), -1)
            #cv.circle(img, (round(sorted_color_deep_rank[4][0][1]), round(sorted_color_deep_rank[4][0][0])), 1,(0, 255, 255), -1)
            #fixed_data_list = un_angle_round(x_sample,y_sample,fixed_data)
            #cv.circle(img, (round(fixed_data_list[i-1][0]), round(fixed_data_list[i-1][1])), 1, (0, 255, 255), -1)
            #cv.circle(img, (round(x1), round(y1)), 1, (255, 0, 255), -1) #半径显示

            #distance test and upload
            distance_from_single_point_to_center_list.append(distance(x_final,y_final,cx,cy))
            result_dot_location_x_y.append([x_final,y_final])

        #<grouping
        #print(result_dot_location_x_y)
        result_grouping=[[]]
        for i in range(0,72-1):
            p1_x=result_dot_location_x_y[i][0]
            p1_y=result_dot_location_x_y[i][1]
            p2_x=result_dot_location_x_y[i+1][0]
            p2_y=result_dot_location_x_y[i+1][1]
            if distance(p1_x,p1_y,p2_x,p2_y)<=5:
                result_grouping[-1].append(i)#先以id记录
            else:
                result_grouping.append([])
                result_grouping[-1].append(i)
        #print(result_grouping)

        res=result_grouping.index(max(result_grouping))
        #print(res)
        #print(result_grouping[res])
        # grouping>

        # <loop for recorrect

        for loop in range(1,2):

            for i in range(result_grouping[res][0]+2, result_grouping[res][0]-1,-1):


                x1 = angle_temp_list[i - 1][0]
                y1 = angle_temp_list[i - 1][1]
                cx = x_sample
                cy = y_sample
                temp_list = pixel_between_two_points(cx, round(x1), cy, round(y1))

                # 单条射线的所有点，颜色深度的集合，找出前5名
                color_deep_rank = {}
                for m in range(0, len(temp_list)):
                    x_temp = temp_list[m][0]
                    y_temp = temp_list[m][1]
                    single_lenth = cell_wall_ray_lenth(cx, cy, x_temp, y_temp)
                    color_deep_rank[y_temp, x_temp] = gauss[y_temp][x_temp]
                    sorted_color_deep_rank = sorted(color_deep_rank.items(), key=lambda kv: (kv[1], kv[0]),
                                                    reverse=False)


                if i==result_grouping[res][0]+2:
                    standard_point=[sorted_color_deep_rank[0][0][0],sorted_color_deep_rank[0][0][1],sorted_color_deep_rank[0][1]]
                    print(standard_point)
                else:
                    distance_temp = []

                    for t in range(0,4):
                        distance_temp.append(distance(sorted_color_deep_rank[t][0][0],sorted_color_deep_rank[t][0][1],standard_point[0],standard_point[1]))

                    print(distance_temp)
                    min_dis_id=distance_temp.index(min(distance_temp))
                    x_final=sorted_color_deep_rank[min_dis_id][0][1]
                    y_final = sorted_color_deep_rank[min_dis_id][0][0]
                    color=sorted_color_deep_rank[min_dis_id][1]
                    standard_point=[x_final,y_final,color]

                    print("x:",sorted_color_deep_rank[0][0][0])


                    cv.circle(img, (x_final, y_final), 1, (255, 0, 0), -1)
                   # loop for recorrect>

        #< list save
        file = open('test_list.txt', 'w')
        for fp in distance_from_single_point_to_center_list:
            file.write(str(fp))
            file.write('\n')
        file.close()
        #list save >
        plt.plot(distance_from_single_point_to_center_list, color="black")
        from k_means_1D import k_means_1d_def
        #temp_list_1=k_means_1d_def(3,30)[2]
        #plt.plot([temp_list_1[0]]*len(a), color="red", linestyle='--')
        #plt.plot([temp_list_1[1]] * len(a), color="red", linestyle='--')

        #plt.show()



    cv.imshow("img_test_round", img)
    cv.imwrite("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\step2_output.bmp",img)


    print("============Step 2 End / Dataset Saved============")
    cv.waitKey()
