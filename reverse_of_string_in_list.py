s = ["h","e","l","l","o"]
left = 0
right = len(s)-1
r = []
while left < right:
    s[left],s[right] = s[right],s[left]
    print(s[left])
    # print(s[right])
    left += 1
    right -= 1
print(r)