
def sort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right


        array[index], array[min_index] = array[min_index], array[index]


array = [9, 8, 7, 3, 4, 2, 1]
sort(array)
print(array)


           

     


