import pandas as pd
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
        arr = []
        count = 1
        for i in range(n):
            if i % memory_limitation == 0 and i!=0:
                # sort arr then save
                arr.append(data[i])
                merge_sort(arr, column_vals)
                df = pd.DataFrame(arr) # columns=column_names
                filename = 'Final/Sorted_' + str(count)
                df.to_csv(filename + '.csv', sep=',', index=False, header=False)
                arr = []
                count+=1
            else:
                arr.append(data[i])

        merge_sort(arr, column_vals)
        df = pd.DataFrame(arr) # columns=column_names
        # df.set_index('tconst', inplace=True)
        filename = 'Final/Sorted_' + str(count)
        df.to_csv(filename + '.csv', sep=',', index=False)
        arr = []

def Mystery_Function(file_path, memory_limitation, columns):
    """
    # file_path :  file_path for Individual Folder (datatype : String)
    # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer : 2000)
    # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
    # **NOTE : In this Mystery_Function records are accessed from only the folder Individual.

    #Store all the output files in Folder named "Final".
    #The below Syntax will help you to store the sorted files :
                # name_of_csv = "Final/Sorted_" + str(i + 1)
                # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)
    #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
    # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which might have less
                #than 2000 records.
    """

    # Need to Code
    # Helps to Sort all the 1,84,265 rows with limitation.
    pass


#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
data_chuncks('imdb_dataset.csv', ['startYear'], 2000)

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
