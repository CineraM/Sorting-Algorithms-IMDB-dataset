import pandas as pd
import time
import os

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

def lessThanOrEqual(d1, d2, columns):
    cur_idx = 0
    while(True):
        try:
            if d1[columns[cur_idx]] < d2[columns[cur_idx]]:
                return True
            elif d1[columns[cur_idx]] == d2[columns[cur_idx]]:
                cur_idx += 1
            else:
                return False
        except:
            return True
        
def lessThan(d1, d2, columns):
    for col in columns:
        if d1[col] < d2[col]:
            return True
        elif d1[col] > d2[col]:
            return False
    return False
        
def greaterThan(d1, d2, columns):
    for col in columns:
        if d1[col] > d2[col]:
            return True
        elif d1[col] < d2[col]:
            return False
    return False
        
def merge(arr, left, right, columns):
    i=j=k=0       
    while i < len(left) and j < len(right):
        if lessThanOrEqual(left[i], right[j], columns):
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    while i < len(left):
        arr[k]=left[i]
        i+=1
        k+=1

    while j < len(right):
        arr[k]=right[j]
        j+=1
        k+=1

def merge_sort(arr, columns):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left, columns)
        merge_sort(right, columns)
        merge(arr, left, right, columns)


def get_col_indx(columns):
    list = [] 
    for i in columns: list.append(column_names.index(i))
    return list

def data_chuncks(file_path, columns, memory_limitation):
        
        column_vals = get_col_indx(columns) 
        data = pd.read_csv(file_path)
        data['primaryTitle'] = data['primaryTitle'].str.strip() 
        data = data.values.tolist()

        n = len(data)
        arr = [data[0]]
        count = 1
        for i in range(1, n):
            arr.append(data[i])
            if len(arr) == memory_limitation:
                merge_sort(arr, column_vals)
                df = pd.DataFrame(arr)
                filename = 'Individual/Sorted_' + str(count)
                df.to_csv(filename + '.csv', sep=',', index=False, header=False)
                arr = []
                count+=1
        if len(arr) >= 1:
            merge_sort(arr, column_vals)
            df = pd.DataFrame(arr)
            filename = 'Individual/Sorted_' + str(count)
            df.to_csv(filename + '.csv', sep=',', index=False, header=False)
            arr = []

#########################################################################################
# return half of file in a list form
def half_of_file(path, isLower):
    data = pd.read_csv(path, header=None)
    data = data.values.tolist()
    n = len(data)
    half = n // 2
    if isLower:
        return data[0:half]
    else:
        return data[half:n]
    
def ith_of_file(path, start, end):
    data = pd.read_csv(path, header=None)
    data = data.values.tolist()
    return data[start:end]

def file_to_arr(path):
    df = pd.read_csv(path, header=None)
    return df.values.tolist()

# save list to csv
def save_to_csv(arr, file_path):
    df = pd.DataFrame(arr)
    df.to_csv(file_path, sep=',', index=False, header=False)


def Mystery_Function(file_path, memory_limitation, columns):
    init_time = time.time()
    column_vals = get_col_indx(columns)
    num_of_files = 1
    while(True):
        try:
            src = file_path + "/Sorted_" + str(num_of_files) + ".csv"
            dst = "Final/Sorted_" + str(num_of_files) + ".csv"
            data = pd.read_csv(src, header=None)
            data = data.values.tolist()
            if len(data) > memory_limitation:
                print("Error, input file exceeds memory limitation: " + str(len(data)))
                exit()
            # merge_sort(data, column_vals)
            save_to_csv(data, dst)
            num_of_files+=1
        except:
            num_of_files-=1
            break
    
    temp_arr = file_to_arr("Final/Sorted_" + str(num_of_files) + ".csv")
    size_of_last_file = len(temp_arr)
    temp_arr = []
    
    # Insertion Sort + heap sort
    for i in range(1, num_of_files):
        print(f'Sorting Sorted_{i}.csv')
        for j in range(i+1, num_of_files+1):
            
            path  = "Final/Sorted_" + str(i) + '.csv'
            path2 = "Final/Sorted_" + str(j) + '.csv'

            temp_arr = half_of_file(path, False) + half_of_file(path2, False)
            merge_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "max.csv")

            min_val = temp_arr[0] 
            split_idx = 0

            temp_arr = half_of_file(path, True) + half_of_file(path2, True)
            merge_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "min.csv")

            for x in range(memory_limitation):
                if greaterThan(temp_arr[x], min_val, column_vals):
                    # print(min_val[0], temp_arr[x][0], x)
                    split_idx = x
                    min_val = temp_arr[x]
                    break

            # split_idx+=1
            arr1, arr2 = file_to_arr("min.csv"), file_to_arr("max.csv")
            temp_arr = arr1[split_idx:memory_limitation] + arr2[0:split_idx]
            merge_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "temp.csv")

            # if split_idx == memory_limitation: 
            temp_arr = file_to_arr("min.csv")[0:split_idx] + file_to_arr("temp.csv")[0:memory_limitation-split_idx]
            save_to_csv(temp_arr, path)

            arr1, arr2 = file_to_arr("temp.csv"), file_to_arr("max.csv")
            temp_arr = arr1[memory_limitation-split_idx:memory_limitation] + arr2[split_idx:memory_limitation]
            save_to_csv(temp_arr, path2)
            

        data = pd.read_csv("Final/Sorted_" + str(i) + '.csv', header=None)
        data = data.values.tolist()
        merge_sort(data, column_vals)
        save_to_csv(data, path)
        # if i ==1: break

    print(f'Execution time: {(time.time() - init_time):.2f} seconds')
    # remove temporary files
    # os.remove("min.csv")
    # os.remove("max.csv")
    # os.remove("temp.csv")

            # if j != num_of_files:
            #     temp_arr = half_of_file(path, True) + half_of_file(path2, True)
            #     merge_sort(temp_arr, column_vals)
            #     save_to_csv(temp_arr, "min.csv")

            #     temp_arr = half_of_file(path, False) + half_of_file(path2, False)
            #     merge_sort(temp_arr, column_vals)
            #     save_to_csv(temp_arr, "max.csv")

            #     temp_arr = half_of_file("min.csv", True) + half_of_file("max.csv", True)
            #     save_to_csv(temp_arr, path)

            #     temp_arr = half_of_file("min.csv", False) + half_of_file("max.csv", False)
            #     save_to_csv(temp_arr, path2)
                
            # else:
            #     half = memory_limitation // 2
            #     if size_of_last_file == memory_limitation:
            #         temp_arr = half_of_file(path, True) + half_of_file(path2, True)
            #         merge_sort(temp_arr, column_vals)
            #         save_to_csv(temp_arr, "min.csv")

            #         temp_arr = half_of_file(path, False) + half_of_file(path2, False)
            #         merge_sort(temp_arr, column_vals)
            #         save_to_csv(temp_arr, "max.csv")

            #         temp_arr = half_of_file("min.csv", True) + half_of_file("max.csv", True)
            #         save_to_csv(temp_arr, path)

            #         temp_arr = half_of_file("min.csv", False) + half_of_file("max.csv", False)
            #         save_to_csv(temp_arr, path2)
            #     else:
            #         data = pd.read_csv(path2, header=None)
            #         data = data.values.tolist()

            #         temp_arr = half_of_file(path, True) + data[half:]
            #         merge_sort(temp_arr, column_vals)
            #         save_to_csv(temp_arr, "min.csv")
                    
            #         temp_arr = half_of_file(path, False) + data[:half]
            #         merge_sort(temp_arr, column_vals)
            #         save_to_csv(temp_arr, "max.csv")
                    
            #         data = pd.read_csv("min.csv", header=None)
            #         data = data.values.tolist()
            #         data = data[:half]
                    
            #         data2 = pd.read_csv("max.csv", header=None)
            #         data2 = data2.values.tolist()
            #         data2 = data[:half]
                    
            #         temp_arr =  data + data2
            #         merge_sort(temp_arr, column_vals)
            #         save_to_csv(temp_arr, path)

            #         temp_arr = ith_of_file("max.csv", half, half+size_of_last_file)
            #         merge_sort(temp_arr, column_vals)
            #         save_to_csv(temp_arr, path2)
            #         data, data2 = [], []
            
        # data = pd.read_csv("Final/Sorted_" + str(i) + '.csv', header=None)
        # data = data.values.tolist()
        # merge_sort(data, column_vals)
        # save_to_csv(data, path)

    # data = pd.read_csv("Final/Sorted_" + str(num_of_files) + '.csv', header=None)
    # data = data.values.tolist()
    # merge_sort(data, column_vals)
    # save_to_csv(data, "Final/Sorted_" + str(num_of_files) + '.csv')


#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
# data_chuncks('imdb_dataset.csv', ['tconst', 'startYear','runtimeMinutes' ,'primaryTitle'], 2000)

#Test Case 14
#data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
#data_chuncks('imdb_dataset.csv', ['startYear','runtimeMinutes' ,'primaryTitle'], 2000)


#Test Case 13
Mystery_Function("Individual", 2000, ['tconst', 'startYear','runtimeMinutes' ,'primaryTitle'])

#Test Case 14
#Mystery_Function(file_path="Individual", 2000, ['primaryTitle'])

#Test Case 15
#Mystery_Function(file_path="Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])
