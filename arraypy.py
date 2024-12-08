import array as arr

array_num = arr.array("i",[1,2,3,4,5,3,4,3,5,6,7,3,5,1,2,7,2,4,7,4,1,9])

print("oranginal array: ",str(array_num))

print("the numbe rof 3 is, ",array_num.count(3))

array_num.reverse()
print("This is an revarsed num of the array")
print(str(array_num))