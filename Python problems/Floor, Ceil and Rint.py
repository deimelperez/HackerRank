import numpy

my_array = numpy.array(list(map(float, input().rstrip().split())))
arr_floor = numpy.floor(my_array)
arr_ceil = numpy.ceil(my_array)
arr_rint = numpy.rint(my_array)
for i in range(len(my_array)):
    arr_floor[i] = ' ' + str(arr_floor[i])
    arr_ceil[i] = ' ' + str(arr_ceil[i])
    arr_rint[i] = ' ' + str(arr_rint[i])
print(arr_floor)
print(arr_ceil)
print(arr_rint)
