import rand #for generation of random arrays

def merge_sort(arr):
    if len(arr1) == 1:
        return arr1

    half = len(arr1)//2
    
    return recombine(merge_sort(arr1[:half]), merge_sort(arr1[half:]))

def recombine(left_arr, right_arr):
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
    
    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr1)

print(arr_out)


