import pandas as pd


def half_of_file(path, isLower):
    data = pd.read_csv(path, header=None)
    data = data.values.tolist()
    if isLower:
        return data[0:1000]
    else:
        return data[1000:2000]
    
file_name = "Individual/Sorted_"

data = pd.read_csv("Individual/Sorted_92.csv", header=None)
data = data.values.tolist()


data2 = pd.read_csv("Individual/Sorted_93.csv", header=None)
data2 = data2.values.tolist()
# data = data[999: 2000]

# data1 = data[0:1000]
# data2 = data[1000:2000]

# print(len(data1))
# print(data1)


temp_arr = data[0:1735] + data2[0:265]
arr = [1, 2, 4, 5, 6, 7, 8]

print(arr[10:])




'''
for i to 93
    for j to 93

    
1250


1000


2000
265    
    
'''

