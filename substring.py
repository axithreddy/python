
def check_p(x):
    for i in range(len(x)):
       if i < len(x)-i-1 and x[i] != x[len(x)-i-1]:
           return False
    return True
    
def get_nbp(x):
    cnt = 0
    print(f'test0:{x}')
    for b in range(1,len(x)):
        print(f'test1:{x}')
        if x[0:b] == x[-b:] and check_p(x[0:b]):
            print(f'test2:{x[0:b]}')
            cnt += 1
            print(cnt)
    return cnt

s = 'aaaa'
sub_strings = []
for i in range(len(s)):
    for j in range(i + 1,len(s)+1):
        sub_strings.append(s[i:j])
print(sub_strings)

count = 0

for x in sub_strings:
    if len(x) < 2:
        continue
    #print(f'test0:{x}')
    count = count + get_nbp(x)
print(count)