def get_all_max(arr):
    max_val = max(arr)
    return [x for x in arr if x == max_val]
arr=[4,4,3,1]
result = get_all_max(arr)
print(result)

