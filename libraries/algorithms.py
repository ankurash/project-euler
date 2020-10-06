def greatest_product_subarray(arr:list, subarray_len:int):
    """ returns the subarray having the greatest product in the array and the greatest product

    Args:
        arr (list): list of integers
        subarray_len (int): length of subarray

    Returns:
        (list,int): subarray,max product
    """
    if subarray_len >= len(arr):
        return arr
    prod = 1
    for i in range(0, subarray_len):
        prod *= arr[i]
    max_prod = prod
    end_index = subarray_len - 1
    i = end_index+1
    while i in range(end_index+1,len(arr)):
        if arr[i] != 0:
            if arr[i-subarray_len] == 0:
                prod = 1
                for j in range(i-subarray_len+1, i+1):
                    prod *= arr[j]
            else:
                prod = (prod//arr[i-subarray_len])*arr[i]
            if prod > max_prod:
                max_prod = prod
                end_index = i
            i += 1
        else:
            i = i+subarray_len
    return arr[end_index-subarray_len+1:end_index+1], max_prod
