import random
import numpy as np
from math_test import*

file=open('test_list.txt', 'r')
test_dataset = [float(x.strip()) for x in file]
file.close()
print(test_dataset)

def k_means_1d_def(dataset,k,loop_times):

    finial_result=[]
    random_list=[]
    counter=0



    while (counter < k):
        random_seed = random.randint(0, len(dataset) - 1)
        if random_seed not in random_list:
            random_list.append(random_seed)
            counter+=1
            finial_result.append([])
    # <create loop times matlab list
    loop_times_list =random_list
    # create loop times matlab list>
    print("random seed list is : ",random_list)

    loop_counter=0
    while loop_counter<loop_times:
        print("####################The ", loop_counter+1," times loop ############################")
        if loop_counter!=0:
            random_list=finial_result
            finial_result=[]
            for i in range(0,k):
                finial_result.append([])
            print("random_list=finial_result, this random list is: ", random_list,"清零成功！清零后：",finial_result)
        for i in range(0,len(dataset)-1):
            distance=max(dataset)

            choice_which_crowd=0#初始化选哪一个
            for m in range(0,k):
                print("m is :",m)
                distance_temp=abs(round(dataset[i]-random_list[m]))
                print("distance is :", distance_temp)
                if distance_temp<=distance:
                    distance=distance_temp
                    choice_which_crowd=int(m)
            print("$$$$$$this time insert: ",dataset[i],"in crowd: ", choice_which_crowd,"cuz the distance is the smallest: ", distance)
            if loop_counter==1:
                print("%%%% final result: ",finial_result)
            finial_result[choice_which_crowd].append(dataset[i])#把距离最近的那个点归为choice_which_crowd
            print("######### the final list is", finial_result)


        if loop_counter==loop_times-1:
            print("# The finial result is: ", finial_result)
            print("max1:",max(finial_result[0]),"min1:",min(finial_result[0]))
            print("max2:", max(finial_result[1]), "min2:", min(finial_result[1]))
            print("max3:", max(finial_result[2]), "min3:", min(finial_result[2]))
        for n in range(0,k):
            if len(finial_result[n])==0:
                finial_result[n].append(0)
            finial_result[n]=int(round(np.mean(finial_result[n])))
        loop_counter+=1
        #insert matleb data:
        print("&&&&&&&, final result:",finial_result)

        #insert matleb data:
    print(loop_times_list)
    return finial_result,loop_times_list
k_means_1d_def(test_dataset,3,15)



