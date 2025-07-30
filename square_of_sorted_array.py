nums = [-5,-1,0,3,4]
left = 0
right = len(nums)-1
output = [0] * len(nums)
r_output = len(output)-1
while left <= right:
    rs = nums[right] * nums[right]
    ls = nums[left] * nums[left]
    if rs >= ls:
        output[r_output] = rs
        right -= 1
        r_output -= 1
    elif rs < ls:
        output[r_output] = ls
        left += 1
        r_output -= 1
print(output)