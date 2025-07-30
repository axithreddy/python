nums = [-5,-1,0,3,4]
left = 0
right = len(nums)-1
output = [0] * len(nums)
r_output = len(output)-1
while left <= right:
    if abs(nums[right]) > abs(nums[left]):
        output[r_output] = nums[right] * nums[right]
        right -= 1
        r_output -= 1
    else:
        output[r_output] = nums[left] * nums[left]
        left += 1
        r_output -= 1
print(output)