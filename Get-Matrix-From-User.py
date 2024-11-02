import numpy as np

rows = int(input("please enter your rows number :"))
cols = int(input("please enter your cells number :"))

matrix = []

print("please add Matrix elements : ")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"please enter your element {i+1},{j+1}: "))
        row.append(element)
    matrix.append(row)

matrix_np = np.array(matrix)

print(matrix_np)