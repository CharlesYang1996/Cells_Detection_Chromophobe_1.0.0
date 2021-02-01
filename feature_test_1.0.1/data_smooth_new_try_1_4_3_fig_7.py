import matplotlib.pyplot as plt
import numpy as np
import random
from math_test import find_longest_element_index
from math_test import relocate_start_point
import math
from itertools import chain
from data_smooth import outliers_detect
def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数


def step3(cell_id):
    file = open('test_list.txt', 'r')
    dataset = [float(x.strip()) for x in file]
    file.close()
    t = np.linspace(start = -4, stop = 4, num = len(dataset))
    y=np.array(dataset)
    a = dataset.copy()
    #===============loop start==============
    for loop_time in range(0,1):
        print("================= Loop times : ",loop_time+1,"================= ")
        total_list=[]
        temp_list=[]
        for i in range(0,len(a)-1):
            temp_list.append(a[i])

            fall=a[i+1]-a[i]
            if abs(fall)>4:
                total_list.append(temp_list)
                temp_list=[]
            if i == len(a)-2:
                temp_list.append(dataset[-1])
                total_list.append(temp_list)

        new_list=total_list.copy()


        for loop_time_1 in range(0,20):
            start_point_in_original_list = find_longest_element_index(total_list)
            i4=relocate_start_point(len(total_list),start_point_in_original_list)
            error_detect=0
            try:
                for i in range(0,30):

                    fall_list=round(new_list[i+1][0]-new_list[i][-1])
                    if (abs(fall_list)>6 and len(new_list[i+1])<=6) or (np.mean(new_list[i+1])>=50 and len(new_list[i+1])>=3):
                        outlier_list=new_list[i+1]
                        makeup_length=len(outlier_list)
                        new_list.remove(outlier_list)


                        for m in range(1,makeup_length+1):
                            makeup_part=new_list[i][-1]
                            new_list[i].append(makeup_part)

                        error_detect=1

            except:
                pass
            c = []
            for i in range(0, len(new_list)):
                for m in range(0, len(new_list[i])):
                    c.append(new_list[i][m])


            #test on

            #plt.show()



            if loop_time_1!=1 and error_detect==0:
                standard_circle_list = [round(np.mean(sum(new_list, [])),1)] * len(dataset)

                plt.savefig("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\output_smooth\\"+str(cell_id)+".jpg")
                break




        new_list=sum(new_list,[])

        #data_smooth_update
        def moving_average(interval, window_size):
            window = np.ones(int(window_size)) / float(window_size)
            return np.convolve(interval, window, 'same')  # numpy的卷积函数

        t = np.linspace(start=-4, stop=4, num=len(new_list))

        window_size_number=4
        y_av = moving_average(interval=new_list, window_size=window_size_number)
        y_av[0:round(window_size_number/2)]=y[0:round(window_size_number/2)]
        y_av[-round(window_size_number / 2):] = y[-round(window_size_number / 2):]

        #test_mode


        #plt.title("Smoothed_Data",size=20)

        standard_circle_list = [round(np.mean(y), 1)] * len(dataset)
        plt.plot(t, y, "r.-", t, y_av, "g.-")
        plt.plot(t, standard_circle_list, "y.-")
        plt.legend(['original data', 'smooth data','standard circle'], prop={'size': 15})

        font1 = {
                 'weight': 'normal',
                 'size': 20,
                 }

        plt.tick_params(labelsize=15)
        plt.xlabel('Number of Points', font1)
        plt.ylabel('Distance to Center', font1)
        plt.show()


        new_list=y_av



        a=new_list
        #============Loop End============

    #output
    file = open('data_smooth_output.txt', 'w')
    for fp in new_list:
        file.write(str(fp))
        file.write('\n')
    file.close()

step3(3)