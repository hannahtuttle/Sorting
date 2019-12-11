# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # Create an array arr3[] of size n1 + n2.
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    for i in range(0, len(merged_arr)):
        if not arrA:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif not arrB:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrA[0] > arrB[0]:
            merged_arr[i] = arrB[0]
            del arrB[0]
        else:
            merged_arr[i] = arrA[0]
            del arrA[0]
    # i=0
    # # Simultaneously traverse arrA and arrB.
    # for item in arrA[:]:
    #     for it in arrB[:]:
    #     # Pick smaller of current elements in arrA and arrB, copy this smaller element to next position in merged_arr and move ahead in merged_arr and the array whose element is picked.
    #             if it < item:
    #                 # if it already exists in merged_ then skip it and go to the next value
    #                 if (it in merged_arr):
    #                     pass
    #                 else:
    #                     merged_arr[i] = it
    #                     i += 1
    #             elif item < it:
    #                 if (item in merged_arr):
    #                     pass
    #                 else:
    #                     merged_arr[i] = item
    #     i += 1
    # # If there are remaining elements in arrA or arrB, copy them also in merged_arr.
    # if (arrA[-1] in merged_arr):
    #     pass
    # else:
    #     instert_here = merged_arr.index(arrB[-1]) +1
    #     for item in arrA:
    #         if(item in merged_arr):
    #             pass
    #         else:
    #             print('last inserted value', instert_here)
    #             merged_arr[instert_here] = item
    #             instert_here +=1

    # if (arrB[-1] in merged_arr):
    #     pass
    # else:
    #     for item in arrB:
    #         if(item in merged_arr):
    #             pass
    #         else:
    #             merged_arr[i] = item
    #             i+=1

    # print('index of merge after loop', i)
    return merged_arr
sampleA = [1, 3, 5, 6, 9, 10]
sampleB = [2, 4, 7, 8, 11, 12]
print(merge(sampleA, sampleB))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    # this finds the index of the widdle of hthe array rounded to an int.
    middle = round(len(arr)/2)
    # this splits the arr into two new smaller arr
    first_half = arr[:middle]
    second_half= arr[middle:]
    # print('first half', first_half)
    # print('second half', second_half)
    
    x = merge_sort(first_half)
    y = merge_sort(second_half)
    # split_arr = [merge_sort(first_half)]
    # print(split_arr)

    return merge(x, y)

sampleC = [12, 1, 10, 8, 4, 2, 7, 5, 6]
# print(merge_sort(sampleC))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
