arr1 = [1,4,7,20]
arr2 = [3,5,6]

def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
        print(f"test1:{ans}")
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
        print(arr1)
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans
    
print(combine(arr1, arr2))