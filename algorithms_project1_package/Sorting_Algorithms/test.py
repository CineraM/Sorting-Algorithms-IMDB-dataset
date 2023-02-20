import numpy as np
import pandas as pd
import csv

data = []

csv_data = open('test_file.csv')
arr = np.loadtxt(csv_data, delimiter=",")

print(arr)

