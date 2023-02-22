import csv
import time
import json

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

#Quick Sort
def pivot_element(arr):
    #CODE For identifiying the pivot element
    return pivot
def quicksort(arr, columns):
    """
    The function performs the QuickSort algorithm on a 2D array (list of lists), where
    the sorting is based on specific columns of the 2D array. The function takes two parameters:

    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on

    The function first checks if the length of the input array is less than or equal to 1,
    in which case it returns the array as is. Otherwise, it selects the middle element of
    the array as the pivot, and splits the array into three parts: left, middle, right.

    Finally, the function calls itself recursively on the left and right sub-arrays, concatenates
    the result of the recursive calls with the middle sub-array, and returns the final sorted 2D array.
    """
    if len(arr) <= 1:
        return arr
    pivot = pivot_element(arr)
    #NEED TO CODE
    #Implement Quick Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#Selection Sort
def selection_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    #NEED TO CODE
    #Implement Selection Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.



#Heap Sort
def build_max_heap(arr, n, i, columns):
    """
    In the build_max_heap function, arr is the input array that we want to sort. n is the size of the array,
    and i is the index of the root node. The build_max_heap function uses i as the starting point to traverse
    down the heap tree and maintain the max heap property. l and r are the indices of the left and right
    children of the root node, respectively. The function compares the root node with its children and
    swaps the root node with the largest child node if necessary to maintain the max heap property.

    The recursive calls continue until the heap property is restored,
    i.e., the largest element is at the root of the sub-heap.
    """
    #NEED TO CODE
    #Implement heapify algorithm here


def heap_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    #NEED TO CODE
    #Implement Heap Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#Shell Sort
def shell_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    #NEED TO CODE
    #Implement Shell Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#Merge Sort
def merge(left, right, columns):
    """
    left: a list of lists representing the left sub-array to be merged
    right: a list of lists representing the right sub-array to be merged
    columns: a list of integers representing the columns to sort the 2D array on

    Finally, after one of the sub-arrays is fully merged, the function extends the result
    with the remaining elements of the other sub-array and returns the result as the final
    sorted 2D array.
    """
    #NEED TO CODE
    #Implement merge Logic
    #return Sorted array

def merge_sort(data, columns):
    """
    data: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, the function returns the result of the merge operation as the final sorted 2D array.
    """
    #NEED TO CODE
    if len(data) <= 1:
        return data
    mid = #Mid value
    #Need to Code
    #Implement Merge Sort Algorithm
    #return Sorted array
    return merge(left, right, columns)
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.




#Insertion Sort
def insertion_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    #NEED TO CODE
    #Insertion Sort Implementation
    #Return : List of tconst values which are obtained after sorting the dataset.
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.



def sorting_algorithms(file_path, columns, select):
    """
    # file_path: a string representing the path to the CSV file
    # columns: a list of strings representing the columns to sort the 2D array on
    # select: an integer representing the sorting algorithm to be used

    # colum_vals: is a list of integers representing the indices of the specified columns to be sorted.

    # data: is a 2D array of values representing the contents of the CSV file, with each row in
    the array corresponding to a row in the CSV file and each element in a row corresponding to a value
    in a specific column.

    More Detailed Description:
    
    df= #read imdb_dataset.csv data set using pandas library

    column_vals = #convert the columns strings passed from the test cases in the form of indices according to
                  #the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  #Columns provided you must also include 0 column in the first place of list in column_vals
                  #for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).
    """
    #NEED TO CODE
    #Read imdb_dataset.csv
    #write code here Inorder to read imdb_dataset
    df= #read imdb_dataset.csv data set using pandas library

    column_vals = #convert the columns strings passed from the test cases in the form of indices according to
                  #the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  #Columns provided you must also include 0 column in the first place of list in column_vals
                  #for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).

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
