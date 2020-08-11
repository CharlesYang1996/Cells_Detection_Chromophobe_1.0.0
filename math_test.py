
import math

#print ("cos(3) : ",  math.cos(3))
#print ("cos(-3) : ",  math.cos(-3))
#print ("cos(0) : ",  math.cos(0))
#print ("cos(math.pi) : ",  math.cos(math.pi))
#print ("cos(2*math.pi) : ",  math.cos(2*math.pi))
#print ("sin(1/6*math.pi) : ",  math.sin(1/6*math.pi))

def angle_round(cx,cy,d):
    angle_round_list=[]
    angle_unit_number=36 #一个pi分成18份，没一份10度"
    print("Warning: A circle is divided into ",angle_unit_number," parts, each part of ",round(180/angle_unit_number,1)," degrees")
    for i in range(1,angle_unit_number*2+1):
        #print (i)
        #print("sin ",i,"/",angle_unit_number," pi = ", round(math.sin(i / angle_unit_number * math.pi),3))
        #print("cos ", i, "/",angle_unit_number," pi = ", round(math.cos(i / angle_unit_number * math.pi), 3))
        x1= round(math.cos(i / angle_unit_number * math.pi), 3) * d + cx
        y1 = round(math.sin(i / angle_unit_number * math.pi), 3) * d + cy
        angle_round_list.append([x1,y1])
    print(angle_round_list)
    return angle_round_list




def cell_wall_ray_lenth(cx,cy,x1,y1):
    distance=round(((x1-cx)**2+(y1-cy)**2)**0.5,3)
    return distance

a=cell_wall_ray_lenth(0,0,2,0)
