

def pixel_between_two_points(x1, x2, y1, y2):
    two_points_list=[]
    x_distance = (x2 - x1)
    y_distance = (y2 - y1)
    a=0
    b=0
    if x_distance>0:
        a=1
    else:
        a=-1
    if y_distance>0:
        b=1
    else:
        b=-1

    if abs(y_distance) < abs(x_distance):

        div_1 = y_distance / x_distance

        for i in range(0, x_distance,a):
            pixel = [x1 + i, y1 + round(i * div_1)]
            #print(pixel)
            two_points_list.append(pixel)
            lenth_of_list = len(two_points_list)

    else:
        div_1 = x_distance / y_distance

        for i in range(0, y_distance,b):
            pixel = [x1 + round(i * div_1), y1 + i]
            #print(pixel)
            two_points_list.append(pixel)
            lenth_of_list=len(two_points_list)

    return two_points_list

test=pixel_between_two_points(168, 132,
                         179, 150)
print(test)
print(test[2])

