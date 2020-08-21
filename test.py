key_value ={}
key_value[1,2] = 56
key_value[3,4] = 2
key_value[5,6] = 12
key_value[7,8] = 24
key_value[8,9] = 18
key_value[10,10] = 323

print("按值(value)排序:")
sorted_key_value=sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]),reverse=True)
print(sorted_key_value)
print(sorted_key_value[0])
print(sorted_key_value[0][0][0])
print(sorted_key_value[0][0][1])

# read from local
f = open("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\dict.txt", 'r')
dict_ = eval(f.read())
f.close()
print("read from local : ", dict_)
print(dict_[1][0],dict_[1][1])





a=[[1],[1],[1]]
b=[[2],[2],[2]]

c=[[1, 2], [1, 2], [1, 2]]
def combine_two_2d_list(a,b):
    for i in range(0, len(a)):
        print(a[i])

        print(b[i])
        a[i].append(b[i][0])

    return a
print(combine_two_2d_list(c,a))
c.remove(c[2])
print(c)