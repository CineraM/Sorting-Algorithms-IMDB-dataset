import pandas as pd
import time, os, shutil

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


def delete_files_in_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def data_chuncks(file_path, columns, memory_limitation):
        delete_files_in_folder('Individual/')   # flush the contents of previos sorts
        delete_files_in_folder('Final/')

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

# return # of lines in file
def number_of_lines_in_file(path):
    data = pd.read_csv(path, header=None)
    return len(data)

# return a csv file as a 2d list
def file_to_arr(path):
    df = pd.read_csv(path, header=None)
    return df.values.tolist()

# save 2dlist to csv
def save_to_csv(arr, file_path):
    df = pd.DataFrame(arr)
    df.to_csv(file_path, sep=',', index=False, header=False)

def Mystery_Function(file_path, memory_limitation, columns):
    init_time = time.time()

    missing_tconst = False
    if 'tconst' not in columns: # adding tconst if needed
        missing_tconst = True
        columns = ['tconst'] + columns
    column_vals = get_col_indx(columns)
    num_of_files = 1
    while(True):
        try:
            src = file_path + "/Sorted_" + str(num_of_files) + ".csv"
            dst = "Final/Sorted_" + str(num_of_files) + ".csv"
            data = pd.read_csv(src, header=None)
            data = data[data.columns[column_vals]]
            data = data.values.tolist()

            if len(data) > memory_limitation:
                print("Error, input file exceeds memory limitation: " + str(len(data)))
                exit()

            save_to_csv(data, dst)
            num_of_files+=1
        except:
            num_of_files-=1
            break
    
    temp_arr = file_to_arr("Final/Sorted_" + str(num_of_files) + ".csv")
    size_of_last_file = len(temp_arr)
    temp_arr = []

    # getting new colums
    new_col_vals = []
    for i in range(len(column_vals)):new_col_vals.append(i)
    if missing_tconst: new_col_vals.pop(0) # pop arr[0] if tconst was insertedm it should not sort based on tsort
    column_vals = new_col_vals
    
    # Insertion Sort + heap sort
    # sort file 1 and 2, then 1&3, 1&4 ...
    # do the same for all files.
    for i in range(1, num_of_files):
        print(f'Sorting Sorted_{i}.csv')
        for j in range(i+1, num_of_files+1):
            path  = "Final/Sorted_" + str(i) + '.csv'
            path2 = "Final/Sorted_" + str(j) + '.csv'
            # this file will contain the last 1000 values from both files file1[1000: 2000] + file1[1000: 2000]
            # basically, the 1000 max values 
            temp_arr = half_of_file(path, False) + half_of_file(path2, False)
            merge_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "max.csv")

            # store the value of the first value in max
            min_val = temp_arr[0] 
            split_idx = 0

            # this file will contain the last 1000 values from both files file1[0: 1000] + file1[0: 1000]
            # basically, the 1000 max values
            temp_arr = half_of_file(path, True) + half_of_file(path2, True)
            merge_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "min.csv")

            # find the index where the min value of max.csv[min] < min.csv[i]
            # store that value for a third temporary file
            for x in range(memory_limitation):
                if greaterThan(temp_arr[x], min_val, column_vals):
                    split_idx = x
                    min_val = temp_arr[x]
                    break

            # this temp file will hold values from min[i:2000] (where i is the index when max.csv[min] < min.csv[i])
            # + max[0:i]
            # This ensures the temp array holds the bridging values between the two arrays
            temp_arr = file_to_arr("min.csv")[split_idx:memory_limitation] + file_to_arr("max.csv")[0:split_idx]
            merge_sort(temp_arr, column_vals)
            save_to_csv(temp_arr, "temp.csv")

            if j != num_of_files:
                #Use min and the bridge array to get the first 2000 values and sotre it on the first file
                # this ensures it gets the all the 2000 minimum values out of the 4000
                temp_arr = file_to_arr("min.csv")[0:split_idx] + file_to_arr("temp.csv")[0:memory_limitation-split_idx]
                save_to_csv(temp_arr, path)

                # same logic for path 2, store the max 2000 values out of the two files with the use of temp and the max files
                temp_arr = file_to_arr("temp.csv")[memory_limitation-split_idx:memory_limitation] + file_to_arr("max.csv")[split_idx:memory_limitation]
                save_to_csv(temp_arr, path2)
            else:
                # In case the last file is less than the memory limit, follow the same logic with the max size changed, and
                # then dump the contents from file2 to file1 until file 2 number of lines is = to the original
                temp_size = number_of_lines_in_file("temp.csv")
                temp_arr = file_to_arr("min.csv")[0:split_idx] + file_to_arr("temp.csv")[0:temp_size-split_idx]
                save_to_csv(temp_arr, path)

                temp_arr = file_to_arr("temp.csv")[temp_size-split_idx:temp_size] + file_to_arr("max.csv")[split_idx:memory_limitation]
                save_to_csv(temp_arr, path2)

                path_size = number_of_lines_in_file(path)
                temp_arr = file_to_arr(path) + file_to_arr(path2)[0:memory_limitation-path_size]
                merge_sort(temp_arr, column_vals)
                save_to_csv(temp_arr, path)

                path_size = number_of_lines_in_file(path2)
                temp_arr = file_to_arr(path2)[path_size-size_of_last_file:path_size]
                merge_sort(temp_arr, column_vals)
                save_to_csv(temp_arr, path2)

        # sort the first file and sotre it
        data = pd.read_csv("Final/Sorted_" + str(i) + '.csv', header=None)
        data = data.values.tolist()
        merge_sort(data, column_vals)
        save_to_csv(data, path)

    
    print(f'Execution time: {(time.time() - init_time):.2f} seconds')

    # add headers to all files, done after sorting
    for i in range(1, 94):
        path = 'Final/Sorted_' + str(i) + '.csv'
        data = pd.read_csv(path, header=None)
        data = data.values.tolist()
        data = [columns] + data
        save_to_csv(data, path)
    # delete temporary files
    os.remove("min.csv")
    os.remove("max.csv")
    os.remove("temp.csv")

# sample test-cases
#Test Case 13
# data_chuncks('imdb_dataset.csv', ['tconst', 'startYear','runtimeMinutes' ,'primaryTitle'], 2000)

#Test Case 14
# data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
data_chuncks('imdb_dataset.csv', ['startYear','runtimeMinutes' ,'primaryTitle'], 2000)


#Test Case 13
# Mystery_Function("Individual", 2000, ['tconst', 'startYear','runtimeMinutes' ,'primaryTitle'])

#Test Case 14
# Mystery_Function("Individual", 2000, ['primaryTitle'])

#Test Case 15
Mystery_Function("Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])
