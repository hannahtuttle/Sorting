
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


        # TO-DO: swap
        temp_value = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_value    



   
    return arr

sample = [10, 4, 8, 3, 12, 2]
# print(selection_sort(sample))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    j = 1
    while j < len(arr):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
        j+=1

    return arr

print(bubble_sort(sample))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr