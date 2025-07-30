
def line_jumps(x1,v1,x2,v2):
    j = 1
    p1 = x1
    p2 = x2
    while p1 < p2:
        p1 = x1 + (j * v1)
        p2 = x2 + (j * v2)
        j += 1
    if p1 == p2:
        print("YES")
    else:
        print("NO")
x1, v1, x2, v2 = map(int, input().split())
if v1 == v2 and x1 != x2:
    print("NO")
elif v2 < v1:
    line_jumps(x1,v1,x2,v2)
else:
    line_jumps(x2,v2,x1,v1)


            
