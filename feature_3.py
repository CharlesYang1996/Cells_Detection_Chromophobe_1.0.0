import cv2
import numpy as np

ball_color = 'cell_wall'

color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'cell_halo': {'Lower': np.array([215, 210, 220]), 'Upper': np.array([235, 225, 235])},
              'cell_wall': {'Lower': np.array([205, 170, 200]), 'Upper': np.array([210, 185, 210])},

              }


#frame=cv2.imread("G:\\2020summer\Project\output_test\\1.jpg")
frame=cv2.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\1.jpg")
frame_2=frame.copy()
img4=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

gs_frame = cv2.GaussianBlur(frame, (5, 5), 0)                     # 高斯模糊
#hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
erode_hsv = cv2.erode(gs_frame, None, iterations=2)                   # 腐蚀 粗的变细
inRange_hsv = cv2.inRange(erode_hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])

mask = cv2.inRange(gs_frame,  color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])
cv2.imshow('Mask', mask)

cnts, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print("total cells number : ", len(cnts))
for i in range(0, len(cnts)):
    cv2.drawContours(frame_2, [cnts[i]], -1, (0, 0, 0),-1)

c = max(cnts, key=cv2.contourArea)
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect)
cv2.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)

cv2.imshow('frame_2', frame_2)
cv2.waitKey(1)


cv2.waitKey(0)
cv2.destroyAllWindows()
