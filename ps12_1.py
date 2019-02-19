"A.1"
tlist0 = [(1,2),(3,4),(5,6),(7,8)]
tlist1 = [(3,5),(8,8),(6,1),(7,6)]

def tuple_separater(tlist):
    rlist_a = []
    rlist_b = []
    for item in tlist:
        rlist_a.append(item[0])
        rlist_b.append(item[1])
    return rlist_a, rlist_b

print(tuple_separater(tlist0))

"A.2"
matrix0 = [[1,2],[3,4]]
tuple0 = (8,9)

def tuple_mat_mult(matrix,tuple):
    tuple_elm0 = matrix[0][0]*tuple[0]+matrix[0][1]*tuple[1]
    tuple_elm1 = matrix[1][0]*tuple[0]+matrix[1][1]*tuple[1]
    return tuple_elm0, tuple_elm1

print(tuple_mat_mult(matrix0,tuple0))

"A.3"
import os
import csv

def tuples_from_csv(filename):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    tuple_list = []
    with open(my_dir + "/" + filename, "r") as infile:
        reader = csv.reader(infile)
        for row in reader:
            tuple_list.append((int(row[0]),int(row[1])))
    return tuple_list

print(tuples_from_csv("parta.csv"))

"A.4"
def mult_with_list(matrix,tuple_list):
    a = len(tuple_list)
    result_tuple_list = []
    for elm in range(a):
        result_tuple_list.append(tuple_mat_mult(matrix,tuple_list[elm]))
    return result_tuple_list

print(mult_with_list(matrix0,tuples_from_csv("parta.csv")))

"B Setup"
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

"B.1"
def graph_arrays(x_array, y_array):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.plot(x_array, y_array)
    plt.show()

def graph_csv(filename):
    my_x_array = np.array(tuple_separater(tuples_from_csv(filename))[0])
    my_y_array = np.array(tuple_separater(tuples_from_csv(filename))[1])
    graph_arrays(my_x_array,my_y_array)

graph_csv("parta.csv")

"B.2"
from math import sin, cos, radians, degrees
from ps10_dup import rotate_n_degrees

def rotate_tuples_90(filename):
    list_tuples = tuples_from_csv(filename)
    new_tuple_list = []
    for item in list_tuples:
        new_tuple_list.append(rotate_n_degrees(item,90))
    my_x_list,my_y_list = tuple_separater(new_tuple_list)
    my_x_array = np.array(my_x_list)
    my_y_array = np.array(my_y_list)
    graph_arrays(my_x_array,my_y_array)

rotate_tuples_90("parta.csv")

"B.3"
def rotate_tuples_24(filename):
    list_tuples = tuples_from_csv(filename)
    new_tuple_list = []
    for item in list_tuples:
        new_tuple_list.append(rotate_n_degrees(item,24))
    my_x_list,my_y_list = tuple_separater(new_tuple_list)
    my_x_array = np.array(my_x_list)
    my_y_array = np.array(my_y_list)
    graph_arrays(my_x_array,my_y_array)

rotate_tuples_24("parta.csv")

"B.4"
def rotate_tuples_all(filename,angle):
    list_tuples = tuples_from_csv(filename)
    new_tuple_list = []
    for item in list_tuples:
        new_tuple_list.append(rotate_n_degrees(item,angle))
    my_x_list,my_y_list = tuple_separater(new_tuple_list)
    my_x_array = np.array(my_x_list)
    my_y_array = np.array(my_y_list)
    graph_arrays(my_x_array,my_y_array)

angle_list0 = [20,30,40,70,120,250,270,300]

def many_rotate_tuples(filename,angle_list):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    for angle in angle_list:
        list_tuples = tuples_from_csv(filename)
        new_tuple_list = []
        for item in list_tuples:
            new_tuple_list.append(rotate_n_degrees(item,angle))
        my_x_list,my_y_list = tuple_separater(new_tuple_list)
        my_x_array = np.array(my_x_list)
        my_y_array = np.array(my_y_list)
        plt.plot(my_x_array,my_y_array)
    plt.show()

many_rotate_tuples("parta.csv",angle_list0)
