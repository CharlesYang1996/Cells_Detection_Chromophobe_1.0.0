
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


def distance(x1,y1,x2,y2):
    result=((x1-x2)**2+(y1-y2)**2)**0.5

    return round(result,2)



def quantile_p(data,p):
    pos = (len(data) + 1)*p
    #pos = 1 + (len(data)-1)*p
    pos_integer = int(math.modf(pos)[1])
    pos_decimal = pos - pos_integer
    Q = data[pos_integer - 1] + (data[pos_integer] - data[pos_integer - 1])*pos_decimal
    return Q

def ourliers_clean(list):#not finished
    list.sort()
    print(list)
    Q1=quantile_p(list,0.25)
    Q2=quantile_p(list,0.5)
    Q3=quantile_p(list,0.75)
    #print(list)

    IQR=Q3-Q1
    Min_limit=Q1-1.5*IQR
    Max_limit=Q3+1.5*IQR
    print(" Q1:", Q1, " Q2:", Q2, " Q3:", Q3, "Min_limit:", Min_limit,"Max_limit:",Max_limit)

    for i in range(0,len(list)):
        if list[i]<=Min_limit and list[i]>=Max_limit:
            list.remove(list[i])
    print(list)
    return list


ourliers_clean([6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49,1100])

def combine_two_2d_list(a,b):
    for i in range(0, len(a)):
        print(a[i])

        print(b[i])
        a[i].append(b[i][0])

    return a