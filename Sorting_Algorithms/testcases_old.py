from sorting_algos import sorting_algorithms
from sorting_algos import data_filtering
import json


# import sys
# sys.setrecursionlimit(10**6)

total=0
f=0

with open("Output.json", "r") as file:
    data = json.load(file)

def testcase_1_1():
    global total
    global f
    sorted_testcase_1_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 1)

    # with open(r'out_test.txt', 'w') as fp:
    #     for item in sorted_testcase_1_1[1]:
    #         fp.write("%s\n" % item)

    # with open(r'.txt', 'w') as fp:
    #     for item in sorted_testcase_1_1[1]:
    #         fp.write("%s\n" % item)

    if(data["testcase_1_1"][1]==sorted_testcase_1_1[1]):
        print("TestCase 1_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_1_1[0]))
    else:
        print("TestCase 1_1 failed")
        f+=1
    total+=1

    return sorted_testcase_1_1

def testcase_1_2():
    global total
    global f
    sorted_testcase_1_2 =  sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 1)
    if(data["testcase_1_2"][1]==sorted_testcase_1_2[1]):
        print("\nTestCase 1_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_1_2[0]))
    else:
        print("\nTestCase 1_2 failed")
        f+=1
    total+=1

    return sorted_testcase_1_2

def testcase_1_3():
    global total
    global f
    sorted_testcase_1_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 1)
    if(data["testcase_1_3"][1]==sorted_testcase_1_3[1]):
        print("\nTestCase 1_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_1_3[0]))
    else:
        print("\nTestCase 1_3 failed")
        f+=1
    total+=1

    return sorted_testcase_1_3

def testcase_2_1():
    global total
    global f
    sorted_testcase_2_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 2)
    if(data["testcase_2_1"][1]==sorted_testcase_2_1[1]):
        print("\nTestCase 2_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_2_1[0]))
    else:
        print("\nTestCase 2_1 failed")
        f+=1
    total+=1

    return sorted_testcase_2_1


def testcase_2_2():
    global total
    global f
    sorted_testcase_2_2 = sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 2)
    if(data["testcase_2_2"][1]==sorted_testcase_2_2[1]):
        print("\nTestCase 2_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_2_2[0]))
    else:
        print("\nTestCase 2_2 failed")
        f+=1
    total+=1

    return sorted_testcase_2_2

def testcase_2_3():
    global total
    global f
    sorted_testcase_2_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 2)
    if(data["testcase_2_3"][1]==sorted_testcase_2_3[1]):
        print("\nTestCase 2_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_2_3[0]))
    else:
        print("\nTestCase 2_3 failed")
        f+=1
    total+=1
    return sorted_testcase_2_3

def testcase_3_1():
    global total
    global f
    sorted_testcase_3_1 = sorting_algorithms("imdb_dataset.csv", ['startYear'], 3)

    for i in range(len(sorted_testcase_3_1[1])):
        # if sorted_testcase_3_1[1][i] != data["testcase_3_1"][1][i]:
            print(f'i:{i}, sort:{sorted_testcase_3_1[1][i]}, test:{data["testcase_3_1"][1][i]}')
    if(data["testcase_3_1"][1]==sorted_testcase_3_1[1]):
        print("\nTestCase 3_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_3_1[0]))
    else:
        print("\nTestCase 3_1 failed")
        f+=1
    total+=1

    return sorted_testcase_3_1


def testcase_3_2():
    global total
    global f
    sorted_testcase_3_2 = sorting_algorithms("imdb_dataset.csv", ['averageRating'], 3)
    if(data["testcase_3_2"][1]==sorted_testcase_3_2[1]):
        print("\nTestCase 3_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_3_2[0]))
    else:
        print("\nTestCase 3_2 failed")
        f+=1
    total+=1

    return sorted_testcase_3_2

def testcase_3_3():
    global total
    global f
    sorted_testcase_3_3 = sorting_algorithms("imdb_dataset.csv", ['primaryTitle'], 3)

    if(data["testcase_3_3"][1]==sorted_testcase_3_3[1]):
        print("\nTestCase 3_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_3_3[0]))
    else:
        print("\nTestCase 3_3 failed")
        f+=1
    total+=1
    return sorted_testcase_3_3

def testcase_4_1():
    global total
    global f
    testcase_4_1 = sorting_algorithms("imdb_dataset.csv", ['startYear'], 4)
    if(data["testcase_4_1"][1]==testcase_4_1[1]):
        print("\nTestCase 4_1 Passed and your Algorithm Time Complexity = {}".format(testcase_4_1[0]))
    else:
        print("\nTestCase 4_1 failed")
        f+=1
    total+=1
    return testcase_4_1

def testcase_4_2():
    global total
    global f
    testcase_4_2 = sorting_algorithms("imdb_dataset.csv", ['averageRating'], 4)
    if(data["testcase_4_2"][1]==testcase_4_2[1]):
        print("\nTestCase 4_2 Passed and your Algorithm Time Complexity = {}".format(testcase_4_2[0]))
    else:
        print("\nTestCase 4_2 failed")
        f+=1
    total+=1
    return testcase_4_2

def testcase_4_3():
    global total
    global f
    testcase_4_3 = sorting_algorithms("imdb_dataset.csv", ['primaryTitle'], 4)
    if(data["testcase_4_3"][1]==testcase_4_3[1]):
        print("\nTestCase 4_3 Passed and your Algorithm Time Complexity = {}".format(testcase_4_3[0]))
    else:
        print("\nTestCase 4_3 failed")
        f+=1
    total+=1
    return testcase_4_3

def testcase_5_1():
    global total
    global f
    testcase_5_1 = sorting_algorithms("imdb_dataset.csv", ['startYear'], 5)

    if(data["testcase_5_1"][1]==testcase_5_1[1]):
        print("\nTestCase 5_1 Passed and your Algorithm Time Complexity = {}".format(testcase_5_1[0]))
    else:
        print("\nTestCase 5_1 failed")
        f+=1
    total+=1
    return testcase_5_1

def testcase_5_2():
    global total
    global f
    testcase_5_2 = sorting_algorithms("imdb_dataset.csv", ['averageRating'], 5)
    if(data["testcase_5_2"][1]==testcase_5_2[1]):
        print("\nTestCase 5_2 Passed and your Algorithm Time Complexity = {}".format(testcase_5_2[0]))
    else:
        print("\nTestCase 5_2 failed")
        f+=1
    total+=1
    return testcase_5_2

def testcase_5_3():
    global total
    global f
    testcase_5_3 = sorting_algorithms("imdb_dataset.csv", ['primaryTitle'], 5)

    for i in range(len(testcase_5_3[1])):
            if testcase_5_3[1][i] != data["testcase_5_3"][1][i]:
                print(f'i:{i}, sort:{testcase_5_3[1][i]}, test:{data["testcase_5_3"][1][i]}')


    if(data["testcase_5_3"][1]==testcase_5_3[1]):
        print("\nTestCase 5_3 Passed and your Algorithm Time Complexity = {}".format(testcase_5_3[0]))
    else:
        print("\nTestCase 5_3 failed")
        f+=1
    total+=1
    return testcase_5_3

def testcase_6_1():
    global total
    global f
    testcase_6_1 = sorting_algorithms("imdb_dataset.csv", ['startYear'], 6)

    if(data["testcase_6_1"][1]==testcase_6_1[1]):
        print("\nTestCase 6_1 Passed and your Algorithm Time Complexity = {}".format(testcase_6_1[0]))
    else:
        print("\nTestCase 6_1 failed")
        f+=1
    total+=1
    return testcase_6_1


def testcase_6_2():
    global total
    global f
    testcase_6_2 = sorting_algorithms("imdb_dataset.csv", ['averageRating'], 6)
    if(data["testcase_6_2"][1]==testcase_6_2[1]):
        print("\nTestCase 6_2 Passed and your Algorithm Time Complexity = {}".format(testcase_6_2[0]))
    else:
        print("\nTestCase 6_2 failed")
        f+=1
    total+=1
    return testcase_6_2

def testcase_6_3():
    global total
    global f
    testcase_6_3 = sorting_algorithms("imdb_dataset.csv", ['primaryTitle'], 6)
    if(data["testcase_6_3"][1]==testcase_6_3[1]):
        print("\nTestCase 6_3 Passed and your Algorithm Time Complexity = {}".format(testcase_6_3[0]))
    else:
        print("\nTestCase 6_3 failed")
        f+=1
    total+=1
    return testcase_6_3

def testcase_7_1():
    global total
    global f
    testcase_7_1 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 1)
    if(data["testcase_7_1"][1]==testcase_7_1[1]):
        print("\nTestCase 7_1 Passed and your Algorithm Time Complexity = {}".format(testcase_7_1[0]))
    else:
        print("\nTestCase 7_1 failed")
        f+=1
    total+=1
    return testcase_7_1

def testcase_7_2():
    global total
    global f
    testcase_7_2 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 2)
    if(data["testcase_7_2"][1]==testcase_7_2[1]):
        print("\nTestCase 7_2 Passed and your Algorithm Time Complexity = {}".format(testcase_7_2[0]))
    else:
        print("\nTestCase 7_2 failed")
        f+=1
    total+=1
    return testcase_7_2

def testcase_7_3():
    global total
    global f
    testcase_7_3 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 3)
    if(data["testcase_7_3"][1]==testcase_7_3[1]):
        print("\nTestCase 7_3 Passed and your Algorithm Time Complexity = {}".format(testcase_7_3[0]))
    else:
        print("\nTestCase 7_3 failed")
        f+=1
    total+=1
    return testcase_7_3

def testcase_7_4():
    global total
    global f
    testcase_7_4 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 4)
    if(data["testcase_7_4"][1]==testcase_7_4[1]):
        print("\nTestCase 7_4 Passed and your Algorithm Time Complexity = {}".format(testcase_7_4[0]))
    else:
        print("\nTestCase 7_4 failed")
        f+=1
    total+=1
    return testcase_7_4

def testcase_7_5():
    global total
    global f
    testcase_7_5 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 5)
    if(data["testcase_7_5"][1]==testcase_7_5[1]):
        print("\nTestCase 7_5 Passed and your Algorithm Time Complexity = {}".format(testcase_7_5[0]))
    else:
        print("\nTestCase 7_5 failed")
        f+=1
    total+=1
    return testcase_7_5

def testcase_7_6():
    global total
    global f
    testcase_7_6 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 6)
    if(data["testcase_7_6"][1]==testcase_7_6[1]):
        print("\nTestCase 7_6 Passed and your Algorithm Time Complexity = {}".format(testcase_7_6[0]))
    else:
        print("\nTestCase 7_6 failed")
        f+=1
    total+=1
    return testcase_7_6


def testcase_8_1():
    global total
    global f
    testcase_8_1 = sorting_algorithms("imdb_genres_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 1)
    if(data["testcase_8_1"][1]==testcase_8_1[1]):
        print("\nTestCase 8_1 Passed and your Algorithm Time Complexity = {}".format(testcase_8_1[0]))
    else:
        print("\nTestCase 8_1 failed")
        f+=1
    total+=1
    return testcase_8_1

def testcase_8_2():
    global total
    global f
    testcase_8_2 = sorting_algorithms("imdb_genres_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 2)
    if(data["testcase_8_2"][1]==testcase_8_2[1]):
        print("\nTestCase 8_2 Passed and your Algorithm Time Complexity = {}".format(testcase_8_2[0]))
    else:
        print("\nTestCase 8_2 failed")
        f+=1
    total+=1
    return testcase_8_2

def testcase_8_3():
    global total
    global f
    testcase_8_3 = sorting_algorithms("imdb_genres_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 3)
    if(data["testcase_8_3"][1]==testcase_8_3[1]):
        print("\nTestCase 8_3 Passed and your Algorithm Time Complexity = {}".format(testcase_8_3[0]))
    else:
        print("\nTestCase 8_3 failed")
        f+=1
    total+=1
    return testcase_8_3

def testcase_8_4():
    global total
    global f
    testcase_8_4 = sorting_algorithms("imdb_genres_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 4)
    if(data["testcase_8_4"][1]==testcase_8_4[1]):
        print("\nTestCase 8_4 Passed and your Algorithm Time Complexity = {}".format(testcase_8_4[0]))
    else:
        print("\nTestCase 8_4 failed")
        f+=1
    total+=1
    return testcase_8_4

def testcase_8_5():
    global total
    global f
    testcase_8_5 = sorting_algorithms("imdb_genres_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 5)
    if(data["testcase_8_5"][1]==testcase_8_5[1]):
        print("\nTestCase 8_5 Passed and your Algorithm Time Complexity = {}".format(testcase_8_5[0]))
    else:
        print("\nTestCase 8_5 failed")
        f+=1
    total+=1
    return testcase_8_5

def testcase_8_6():
    global total
    global f
    testcase_8_6 = sorting_algorithms("imdb_genres_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 6)
    if(data["testcase_8_6"][1]==testcase_8_6[1]):
        print("\nTestCase 8_6 Passed and your Algorithm Time Complexity = {}".format(testcase_8_6[0]))
    else:
        print("\nTestCase 8_6 failed")
        f+=1
    total+=1
    return testcase_8_6

def testcase_9_1():
    global total
    global f
    testcase_9_1 = sorting_algorithms("imdb_professions_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 1)
    if(data["testcase_9_1"][1]==testcase_9_1[1]):
        print("\nTestCase 9_1 Passed and your Algorithm Time Complexity = {}".format(testcase_9_1[0]))
    else:
        print("\nTestCase 9_1 failed")
        f+=1
    total+=1
    return testcase_9_1

def testcase_9_2():
    global total
    global f
    testcase_9_2 = sorting_algorithms("imdb_professions_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 2)
    if(data["testcase_9_2"][1]==testcase_9_2[1]):
        print("\nTestCase 9_2 Passed and your Algorithm Time Complexity = {}".format(testcase_9_2[0]))
    else:
        print("\nTestCase 9_2 failed")
        f+=1
    total+=1
    return testcase_9_2

def testcase_9_3():
    global total
    global f
    testcase_9_3 = sorting_algorithms("imdb_professions_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 3)
    if(data["testcase_9_3"][1]==testcase_9_3[1]):
        print("\nTestCase 9_3 Passed and your Algorithm Time Complexity = {}".format(testcase_9_3[0]))
    else:
        print("\nTestCase 9_3 failed")
        f+=1
    total+=1
    return testcase_9_3

def testcase_9_4():
    global total
    global f
    testcase_9_4 = sorting_algorithms("imdb_professions_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 4)
    if(data["testcase_9_4"][1]==testcase_9_4[1]):
        print("\nTestCase 9_4 Passed and your Algorithm Time Complexity = {}".format(testcase_9_4[0]))
    else:
        print("\nTestCase 9_4 failed")
        f+=1
    total+=1
    return testcase_9_4

def testcase_9_5():
    global total
    global f
    testcase_9_5 = sorting_algorithms("imdb_professions_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 5)
    if(data["testcase_9_5"][1]==testcase_9_5[1]):
        print("\nTestCase 9_5 Passed and your Algorithm Time Complexity = {}".format(testcase_9_5[0]))
    else:
        print("\nTestCase 9_5 failed")
        f+=1
    total+=1
    return testcase_9_5

def testcase_9_6():
    global total
    global f
    testcase_9_6 = sorting_algorithms("imdb_professions_df.csv", ['startYear','runtimeMinutes' ,'primaryTitle'], 6)
    if(data["testcase_9_6"][1]==testcase_9_6[1]):
        print("\nTestCase 9_6 Passed and your Algorithm Time Complexity = {}".format(testcase_9_6[0]))
    else:
        print("\nTestCase 9_6 failed")
        f+=1
    total+=1
    return testcase_9_6


def testcase_10_1():
    global total
    global f
    testcase_10_1 = sorting_algorithms("imdb_vowel_names_df.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 1)
    if(data["testcase_10_1"][1]==testcase_10_1[1]):
        print("\nTestCase 10_1 Passed and your Algorithm Time Complexity = {}".format(testcase_10_1[0]))
    else:
        print("\nTestCase 10_1 failed")
        f+=1
    total+=1
    return testcase_10_1

def testcase_10_2():
    global total
    global f
    testcase_10_2 = sorting_algorithms("imdb_vowel_names_df.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 2)
    if((data["testcase_10_2"][1]==testcase_10_2[1])):
        print("\nTestCase 10_2 Passed and your Algorithm Time Complexity = {}".format(testcase_10_2[0]))
    else:
        print("\nTestCase 10_2 failed")
        f+=1
    total+=1
    return testcase_10_2

def testcase_10_3():
    global total
    global f
    testcase_10_3 = sorting_algorithms("imdb_vowel_names_df.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 3)
    if(data["testcase_10_3"][1]==testcase_10_3[1]):
        print("\nTestCase 10_3 Passed and your Algorithm Time Complexity = {}".format(testcase_10_3[0]))
    else:
        print("\nTestCase 10_3 failed")
        f+=1
    total+=1
    return testcase_10_3

def testcase_10_4():
    global total
    global f
    testcase_10_4 = sorting_algorithms("imdb_vowel_names_df.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 4)
    if(data["testcase_10_4"][1]==testcase_10_4[1]):
        print("\nTestCase 10_4 Passed and your Algorithm Time Complexity = {}".format(testcase_10_4[0]))
    else:
        print("\nTestCase 10_4 failed")
        f+=1
    total+=1
    return testcase_10_4

def testcase_10_5():
    global total
    global f
    testcase_10_5 = sorting_algorithms("imdb_vowel_names_df.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 5)
    if(data["testcase_10_5"][1]==testcase_10_5[1]):
        print("\nTestCase 10_5 Passed and your Algorithm Time Complexity = {}".format(testcase_10_5[0]))
    else:
        print("\nTestCase 10_5 failed")
        f+=1
    total+=1
    return testcase_10_5

def testcase_10_6():
    global total
    global f
    testcase_10_6 = sorting_algorithms("imdb_vowel_names_df.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 6)
    if(data["testcase_10_6"][1]==testcase_10_6[1]):
        print("\nTestCase 10_6 Passed and your Algorithm Time Complexity = {}".format(testcase_10_6[0]))
    else:
        print("\nTestCase 10_6 failed")
        f+=1
    total+=1
    return testcase_10_6

def testcase_11_1():
    global total
    global f
    testcase_11_1 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'primaryTitle'], 6)
    if(data["testcase_11_1"][1]==testcase_11_1[1]):
        print("\nTestCase 11_1 Passed and your Algorithm Time Complexity = {}".format(testcase_11_1[0]))
    else:
        print("\nTestCase 11_1 failed")
        f+=1
    total+=1

    return testcase_11_1

def testcase_11_2():
    global total
    global f
    testcase_11_2 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'primaryTitle'], 3)
    if(data["testcase_11_2"][1]==testcase_11_2[1]):
        print("\nTestCase 11_2 Passed and your Algorithm Time Complexity = {}".format(testcase_11_2[0]))
    else:
        print("\nTestCase 11_2 failed")
        f+=1
    total+=1

    return testcase_11_2

def testcase_12_1():
    global total
    global f
    testcase_12_1 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 6)
    if(data["testcase_12_1"][1]==testcase_12_1[1]):
        print("\nTestCase 12_1 Passed and your Algorithm Time Complexity = {}".format(testcase_12_1[0]))
    else:
        print("\nTestCase 12_1 failed")
        f+=1
    total+=1

    return testcase_12_1

def testcase_12_2():
    global total
    global f
    testcase_12_2 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'], 3)
    if(data["testcase_12_2"][1]==testcase_12_2[1]):
        print("\nTestCase 12_2 Passed and your Algorithm Time Complexity = {}".format(testcase_12_2[0]))
    else:
        print("\nTestCase 12_2 failed")
        f+=1
    total+=1

    return testcase_12_2
################
data_filtering("imdb_dataset.csv", 1)
data_filtering("imdb_dataset.csv", 2)
data_filtering("imdb_dataset.csv", 3)
data_filtering("imdb_dataset.csv", 4)
testcase = {}
testcase['testcase_1_1'] = testcase_1_1() # pass
testcase['testcase_1_2'] = testcase_1_2() # pass
testcase['testcase_1_3'] = testcase_1_3() # pass

testcase['testcase_2_1'] = testcase_2_1() # pass
testcase['testcase_2_2'] = testcase_2_2() # pass
testcase['testcase_2_3'] = testcase_2_3() # pass

testcase['testcase_3_1'] = testcase_3_1() # FAIL
testcase['testcase_3_2'] = testcase_3_2() # FAIL
testcase['testcase_3_3'] = testcase_3_3() # FAIL

testcase['testcase_4_1'] = testcase_4_1() # pass
testcase['testcase_4_2'] = testcase_4_2() # pass
testcase['testcase_4_3'] = testcase_4_3() # pass

testcase['testcase_5_1'] = testcase_5_1() # pass
testcase['testcase_5_2'] = testcase_5_2() # pass
testcase['testcase_5_3'] = testcase_5_3() # pass

testcase['testcase_6_1'] = testcase_6_1() # pass
testcase['testcase_6_2'] = testcase_6_2() # pass
testcase['testcase_6_3'] = testcase_6_3() # pass

testcase['testcase_7_1'] = testcase_7_1() # pass
testcase['testcase_7_2'] = testcase_7_2() # pass
testcase['testcase_7_3'] = testcase_7_3() # FAIL
testcase['testcase_7_4'] = testcase_7_4() # pass
testcase['testcase_7_5'] = testcase_7_5() # pass
testcase['testcase_7_6'] = testcase_7_6() # pass

testcase['testcase_8_1'] = testcase_8_1() # pass
testcase['testcase_8_2'] = testcase_8_2() # pass
testcase['testcase_8_3'] = testcase_8_3() # FAIL
testcase['testcase_8_4'] = testcase_8_4() # pass
testcase['testcase_8_5'] = testcase_8_5() # pass
testcase['testcase_8_6'] = testcase_8_6() # pass

testcase['testcase_9_1'] = testcase_9_1() # pass
testcase['testcase_9_2'] = testcase_9_2() # pass
testcase['testcase_9_3'] = testcase_9_3() # FAIL
testcase['testcase_9_4'] = testcase_9_4() # pass
testcase['testcase_9_5'] = testcase_9_5() # pass
testcase['testcase_9_6'] = testcase_9_6() # pass

testcase['testcase_10_1'] = testcase_10_1() # pass
testcase['testcase_10_2'] = testcase_10_2() # pass
testcase['testcase_10_3'] = testcase_10_3() # FAIL
testcase['testcase_10_4'] = testcase_10_4() # pass
testcase['testcase_10_5'] = testcase_10_5() # pass
testcase['testcase_10_6'] = testcase_10_6() # pass
testcase['testcase_11_1'] = testcase_11_1() # pass
testcase['testcase_11_2'] = testcase_11_2() # FAIL
testcase['testcase_12_1'] = testcase_12_1() # pass
testcase['testcase_12_2'] = testcase_12_2() # FAIL

print("\n\nTotal Test Cases Passed : {}\nTotal Test Cases Failed : {}".format(total-f,f))
