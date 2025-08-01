nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
left = curr = ans = right = 0
for right in range(len(nums)):
    if nums[right] == 0:
        curr += 1
    while curr > k:
        if nums[left] == 0:
            curr -= 1
        left += 1
    ans = max(ans,right-left+1)
print(ans)





# count = zeros = max_count =0
# for i in range(len(nums)):
#     if nums[i] == 1:
#         count += 1
#     else:
#         if zeros <= k:
#             zeros += 1
#             count += 1
#         else:
#             max_count = max(max_count,count)
#             count = 0
# print(max_count)