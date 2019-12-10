
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x

        temp_value = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_value    
                # next_smallest = smallest_index + 1
        # print(cur_index, smallest_index)


        # TO-DO: swap



   
    return arr
sample = [10, 4, 8, 3, 12, 2]
print(selection_sort(sample))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr