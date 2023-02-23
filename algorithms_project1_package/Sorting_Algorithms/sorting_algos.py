import csv
import time
import json
import pandas as pd

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

# comparison function
# If first element is less than second return true, else false.
def is_less(d1, d2, columns):
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
            return False

def is_less_or_equal(d1, d2, columns):
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

# Quick Sort
# https://www.geeksforgeeks.org/python-program-for-quicksort/
# based of ^
# def pivot_element(arr, low, high, columns):
#     pivot = arr[high]
#     i = low-1

#     for j in range(low, high):
#         # if arr[j][columns[0]] < pivot[columns[0]]:
#         if is_less(arr[j], pivot, columns): # ^
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]

#     return i+1

# def quicksort_recursive(arr, low, high, columns):
#     if low < high:
#         # Find pivot element such that
#         # element smaller than pivot are on the left
#         # element greater than pivot are on the right
#         pi = pivot_element(arr, low, high, columns)
#         # Recursive call on the left of pivot
#         quicksort_recursive(arr, low, pi - 1, columns)
#         # Recursive call on the right of pivot
#         quicksort_recursive(arr, pi + 1, high, columns)

# def quicksort(arr, columns):
#     n = len(arr)
#     quicksort_recursive(arr, 0, n - 1, columns)
#     return arr



def partition(arr, l, h, columns):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l, h):
        if is_less_or_equal(arr[j], x, columns):
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)
  
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr, l, h, columns):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h, columns)
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def quicksort(arr, columns):
    n = len(arr)
    quickSortIterative(arr, 0, n - 1, columns)
    return arr



# Selection Sort
def selection_sort(arr, columns):
    n = len(arr)
    
    # 2d - arr, always increase by one 
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            # if arr[j][columns[0]] <= arr[min_idx][columns[0]]:
            if is_less(arr[j], arr[min_idx], columns):#^
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

    if l < n and is_less(arr[max], arr[l], columns):
        max = l

    if r < n and is_less(arr[max], arr[r], columns):
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
    gap = int(n/2)
 
    while gap > 0:
 
        for i in range(gap, n):
 
            key = arr[i]
            j = i
            while j >= gap and is_less(key, arr[j-gap], columns):
                arr[j] = arr[j-gap]
                j -= gap
 
            arr[j] = key
        gap /= 2
        gap = int(gap)
    
    return arr

#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
#Merge Sort
def merge(arr, left, right, columns):
    i=j=k=0       
    while i < len(left) and j < len(right):
        if is_less_or_equal(left[i], right[j], columns):
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
        # key[columns[0]] < arr[j][columns[0]]
        while j >= 0 and is_less(key, arr[j], columns):
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    
    return arr

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

def data_filtering(a, b):
    return []