nums = [1,12,-5,-6,50,3]
k = 4
curr = sum(nums[0:k])
maxv = curr / k
start = 0
for i in range(k,len(nums)):
    curr = curr + nums[i] - nums[start]
    maxv = max(maxv,curr/k)
    start += 1
print(maxv)