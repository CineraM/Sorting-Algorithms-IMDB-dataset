import pandas as pd
import shutil
import math
import os
import csv

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


def insertion_sort(arr, columns):
    n = len(arr)
    for i in range(1, n):
        
        key = arr[i]
        j = i-1
        
        while j >= 0 and lessThan(key, arr[j], columns):
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    
    return arr


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
            if len(arr) == 2000:
                merge_sort(arr, column_vals)
                df = pd.DataFrame(arr)
                filename = 'Individual/Sorted_' + str(count)
                df.to_csv(filename + '.csv', sep=',', index=False, header=False)
                arr = []
                count+=1

        merge_sort(arr, column_vals)
        df = pd.DataFrame(arr)
        filename = 'Individual/Sorted_' + str(count)
        df.to_csv(filename + '.csv', sep=',', index=False, header=False)
        arr = []

# return half of file in a list form
def half_of_file(path, isLower):
    data = pd.read_csv(path, header=None)
    data = data.values.tolist()
    if isLower:
        return data[0:1000]
    else:
        return data[1000:2000]
    
def ith_of_file(path, start, end):
    data = pd.read_csv(path, header=None)
    data = data.values.tolist()
    return data[start:end]

# save list to csv
def save_to_csv(arr, path):
    df = pd.DataFrame(arr)
    df.to_csv(path, sep=',', index=False, header=False)

def Mystery_Function(file_path, memory_limitation, columns):
    column_vals = get_col_indx(columns)

    # for i in range(1, 94):
    #     src = file_path + "/Sorted_" + str(i) + ".csv"
    #     dst = "Final/Sorted_" + str(i) + ".csv"
    #     data = pd.read_csv(src, header=None)
    #     data = data.values.tolist()
    #     merge_sort(data, column_vals)
    #     save_to_csv(data, dst)

    # 2 temp files, max, min, temp?

    
    idx_check = {}
    for i in range(1,94):
        idx_check[i] = 0

    path = "Final/Sorted_1.csv"
    arr = []

    i = 1
    while len(arr) != 2000:
        print(len(arr))
        min = ith_of_file(path, idx_check[1], idx_check[1]+1)
        min = min[0]
        min_idx = 1
        for i in range(1,93):
            if idx_check[i] > 1999: continue
            path = "Final/Sorted_" + str(i) + ".csv"
            cur = ith_of_file(path, idx_check[i], idx_check[i]+1)
            cur = cur[0]
            if greaterThan(min, cur, column_vals):                
                min = cur
                min_idx = i

        arr.append(min)
        idx_check[min_idx]+=1

    save_to_csv(cur, "temp.csv") 
    #     path = "Final/Sorted_" + str(i) + ".csv"
    #     cur_list += ith_of_file(path, 0, 21)

    # for i in range(1,94):
    #    if len(cur_list) == 2000: break 


Mystery_Function("Individual", 2000, ['tconst', 'startYear','runtimeMinutes' ,'primaryTitle'])

#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
# data_chuncks('imdb_dataset.csv', ['startYear'], 2000)

#Test Case 14
#data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
#data_chuncks('imdb_dataset.csv', ['startYear','runtimeMinutes' ,'primaryTitle'], 2000)


#Test Case 13
# Mystery_Function("Individual", 2000, ['tconst', 'startYear','runtimeMinutes' ,'primaryTitle'])

#Test Case 14
#Mystery_Function(file_path="Individual", 2000, ['primaryTitle'])

#Test Case 15
#Mystery_Function(file_path="Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])



'''

def Mystery_Function(file_path, memory_limitation, columns):
    column_vals = get_col_indx(columns)

    # for i in range(1, 94):
    #     src = file_path + "/Sorted_" + str(i) + ".csv"
    #     dst = "Final/Sorted_" + str(i) + ".csv"
    #     data = pd.read_csv(src, header=None)
    #     data = data.values.tolist()
    #     merge_sort(data, column_vals)
    #     save_to_csv(data, dst)

    # 2 temp files, max, min, temp?
    i = 1
    for j in range(i+1, 94):
        
        path  = "Final/Sorted_" + str(i) + '.csv'
        path2 = "Final/Sorted_" + str(j) + '.csv'
        
        if j != 93:
            arr1, arr2 = half_of_file(path, True), half_of_file(path2, True)
            target_idx = -1

            for idx in range(1000):
                if greaterThan(arr1[idx], arr2[idx], column_vals):
                    target_idx = idx
                    break
            
            arr1, arr2 = half_of_file(path, False), half_of_file(path2, False)
            if target_idx == -1:
                for idx in range(1000):
                    if greaterThan(arr1[idx], arr2[idx], column_vals):
                        target_idx = idx
                        break

            if target_idx == -1: continue

            temp_arr = ith_of_file(path, 0, target_idx) + ith_of_file(path2, 0, 2000-target_idx) # min values
            insertion_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "temp.csv")

            
            temp_arr = ith_of_file(path, target_idx, 2000) + ith_of_file(path2, 2000-target_idx, 2000) # min values
            insertion_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, path2)

            # temp_arr = arr1 + arr2 # min values
            # merge_sort(temp_arr, column_vals)
            # save_to_csv(temp_arr, "temp.csv")

            # temp_arr = half_of_file(path, True) + half_of_file(path2, True)
            # merge_sort(temp_arr, column_vals)
            # save_to_csv(temp_arr, path2)

            shutil.copyfile("temp.csv", path) # copy temp into path
        else:
            temp_arr = ith_of_file(path, 0, target_idx) + ith_of_file(path2, 0, 265) 
            merge_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "temp.csv")

            temp_arr = ith_of_file(path, 1735, 2000)
            merge_sort(temp_arr, columns)
            save_to_csv(temp_arr, path2)

            shutil.copyfile("temp.csv", path) # copy temp into path
'''