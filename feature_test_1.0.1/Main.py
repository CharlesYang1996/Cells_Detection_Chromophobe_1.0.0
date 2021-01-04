#feature_1
#feature_3
#data_smooth_new_try_1_4_1
#feature_4
import cv2 as cv
from shutil import copyfile
from feature_1 import step1
#from feature_3_1_10_17 import step2 as step2_1
from feature_3 import step2
from data_smooth_new_try_1_4_3 import step3
from feature_4 import step4
from feature_4_all import step5
import numpy as np
import time
import matplotlib.pyplot as plt

not_circle_rate=[]
non_circle_rate_list=[]
Cells_quantity=step1()
print(Cells_quantity)
for i in range(1,Cells_quantity):
    try:
        step2(i)


        step3(i)

        non_circle_rate_list.append(step4(i))
        step5(i,Cells_quantity,not_circle_rate)

        #copyfile("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\ouput_marked.bmp","G:\\2020summer\\Project\\Cell_classfication_1.0.0\\output\\"+str(i)+".bmp")
    except:
        pass
display=cv.imread("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\output\\temp_display.bmp")
cv.putText(display, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), (80, 60), cv.FONT_HERSHEY_SIMPLEX, 0.5,
           (0, 0, 0), 1)
cv.putText(display, "Result Value:"+str(np.mean(not_circle_rate)), (80, display.shape[0]-400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv.putText(display, "The lower the value, the higher the probability of Chromophobe", (80, display.shape[0]-350), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
cv.putText(display, "Total cells number: "+str(Cells_quantity), (80, display.shape[0]-300), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)

cv.imshow("Final output", display)

print("===================Result===================")
print(np.mean(not_circle_rate))

plt.hist(non_circle_rate_list,bins=20)
plt.title('non_circle_rate')
plt.show()
cv.waitKey()
