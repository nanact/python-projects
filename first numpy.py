import numpy as np 

data_type = [("name","S15"), ("class",int),("height",float)]

student_details = [("James", 5, 48.5), ("Hail",6,52.2),("Paul",5,42.10)]

student = np.array(student_details, dtype = data_type)

print("Original array")

print(student)

print("sort by height")

print(np.sort(student, order="height"))