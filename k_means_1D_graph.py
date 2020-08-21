from k_means_1D import k_means_1d_def
file=open('test_list.txt', 'r')
test_dataset = [float(x.strip()) for x in file]
file.close()
print(test_dataset)


output=k_means_1d_def(test_dataset,3,5)[1]
print(output)