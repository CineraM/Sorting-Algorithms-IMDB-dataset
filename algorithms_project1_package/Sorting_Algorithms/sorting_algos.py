import time
import pandas as pd
import sys
sys.setrecursionlimit(10**6)
"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']
   
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

def is_equal(d1, d2, columns):
    for col in columns:
        if d1[col] != d2[col]:
            return False
    return True    

# quicksort
def pivot_element(arr):
    #CODE For identifiying the pivot element
    pivot = arr[len(arr)//2]
    return pivot

def quicksort(arr, columns):
    if len(arr) <= 1:
        return arr
    pivot = pivot_element(arr)
    # rename to lessThan
    left = [x for x in arr if lessThan(x, pivot, columns)]
    middle = [x for x in arr if is_equal(x, pivot, columns)]
    right = [x for x in arr if greaterThan(x, pivot, columns)]

    return quicksort(left, columns) + middle + quicksort(right, columns)

# Selection Sort
def selection_sort(arr, columns):
    n = len(arr)
    
    # 2d - arr, always increase by one 
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if lessThan(arr[j], arr[min_idx], columns):
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# https://www.geeksforgeeks.org/heap-sort/
# Heap Sort - based on ^^^
def max_heapify(arr, n, i, columns):
    max = i
    # left and right children of node i
    l = 2 * i + 1 
    r = 2 * i + 2

    if l < n and lessThan(arr[max], arr[l], columns):
        max = l

    if r < n and lessThan(arr[max], arr[r], columns):
        max = r

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        max_heapify(arr, n, max, columns)

def build_max_heap(arr, n, i, columns):

    first_idx = n // 2 -1
    for j in range(first_idx, -1, -1):
        max_heapify(arr, n, j, columns)


def heap_sort(arr, columns):
    n = len(arr)
    build_max_heap(arr, n, -1, columns)
    
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        max_heapify(arr, i, 0, columns)
    return arr

# https://www.geeksforgeeks.org/python-program-for-shellsort/
# based from ^
# Shell Sort
def shell_sort(arr, columns):
    n = len(arr)
    gap = n//2
 
    while gap > 0:
 
        for i in range(gap, n):
 
            key = arr[i]
            j = i
            while j >= gap and lessThan(key, arr[j-gap], columns):
                arr[j] = arr[j-gap]
                j -= gap
 
            arr[j] = key
        gap //= 2
    
    return arr

#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
#Merge Sort
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

def merge_sort_recursive(arr, columns):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_recursive(left, columns)
        merge_sort_recursive(right, columns)
        merge(arr, left, right, columns)

def merge_sort(arr, columns):
    merge_sort_recursive(arr, columns)
    return arr


# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# based of ^
# insertion_sort
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

def data_filtering(filepath, select):
    data = pd.read_csv(filepath)
    if (select == 1):
        
        new_data = []
        data = data.values.tolist()
        for i in data:
            if int(i[3]) >= 1941 and int(i[3]) <= 1955:
                new_data.append(i)

        df = pd.DataFrame(new_data, columns=column_names)
        df.set_index('tconst', inplace=True)
        df.to_csv('imdb_years_df.csv', sep=',')
        
    elif(select == 2):
        genres = ['Adventure', 'Drama']
        new_data = []
        data = data.values.tolist()
        for i in data:
            if i[5] in genres:
                new_data.append(i)

        df = pd.DataFrame(new_data, columns=column_names)
        df.set_index('tconst', inplace=True)
        df.to_csv('imdb_genres_df.csv', sep=',')

    elif(select == 3):
        new_data = []
        profession = ['assistant_director', 'casting_director', 'art_director', 'cinematographer']
        data = data.values.tolist()
        for i in data:
            for p in profession:
                if p in i[16]:
                    new_data.append(i)
                    break

        df = pd.DataFrame(new_data, columns=column_names)
        df.set_index('tconst', inplace=True)
        df.to_csv('imdb_professions_df.csv', sep=',')

    elif(select == 4):
        vowel = 'aeiouAEIOU'
        new_data = []
        data = data.values.tolist()
        
        for i in data:
            if i[13][0] in vowel:
                new_data.append(i)

        df = pd.DataFrame(new_data, columns=column_names)
        df.set_index('tconst', inplace=True)
        df.to_csv('imdb_vowel_names_df.csv', sep=',')



#columns: a list of integers representing the columns to sort the 2D array on
def get_col_indx(columns):
    list = [] 
    for i in columns: list.append(column_names.index(i))
    return list

def sorting_algorithms(file_path, columns, select):
    column_vals = get_col_indx(columns)
    data = pd.read_csv(file_path)
    # "   Ironman" to     "Ironman"
    data['primaryTitle'] = data['primaryTitle'].str.strip() 
    data = data.values.tolist()

    if(select==1):
        start_time = time.time()
        output_list = insertion_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==2):
        start_time = time.time()
        output_list = selection_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==3):
        start_time = time.time()
        output_list = quicksort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==4):
        start_time = time.time()
        output_list = heap_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==5):
        start_time = time.time()
        output_list = shell_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==6):
        start_time = time.time()
        output_list = merge_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    
# comparison function
# If first element is less than second return true, else false.
# def is_less(d1, d2, columns):
#     cur_idx = 0
#     while(True):
#         try:
#             if d1[columns[cur_idx]] < d2[columns[cur_idx]]:
#                 return True
#             elif d1[columns[cur_idx]] == d2[columns[cur_idx]]:
#                 cur_idx += 1
#             else:
#                 return False
#         except:
#             return False

# def is_equal(d1, d2, columns):
#     cur_idx = 0
#     while(True):
#         try:
#             if d1[columns[cur_idx]] == d2[columns[cur_idx]]:
#                 cur_idx += 1
#             else:
#                 return False
#         except:
#             return True    
        
# def greaterThan(d1, d2, columns):
#     cur_idx = 0
#     while(True):
#         try:
#             if d1[columns[cur_idx]] < d2[columns[cur_idx]]:
#                 return False
#             elif d1[columns[cur_idx]] == d2[columns[cur_idx]]:
#                 cur_idx += 1
#             else:
#                 return True
#         except:
#  