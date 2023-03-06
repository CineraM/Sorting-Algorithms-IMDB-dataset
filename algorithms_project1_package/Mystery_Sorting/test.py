                else:
                    data = pd.read_csv(path2, header=None)
                    data = data.values.tolist()

                    temp_arr = half_of_file(path, True) + data[half:]
                    merge_sort(temp_arr, column_vals)
                    save_to_csv(temp_arr, "min.csv")

                    temp_arr = half_of_file(path, False) + data[:half]
                    merge_sort(temp_arr, column_vals)
                    save_to_csv(temp_arr, "max.csv")
                    
                    data = pd.read_csv("min.csv", header=None)
                    data = data.values.tolist()
                    data = data[:half]
                    
                    data2 = pd.read_csv("max.csv", header=None)
                    data2 = data2.values.tolist()
                    data2 = data[:half]
                    
                    temp_arr =  data + data2
                    merge_sort(temp_arr, column_vals)
                    save_to_csv(temp_arr, path)

                    temp_arr = ith_of_file("max.csv", half, half+size_of_last_file)
                    merge_sort(temp_arr, column_vals)
                    save_to_csv(temp_arr, path2)
                    data, data2 = [], []