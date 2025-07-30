a = [2,4]
b = [16,32,96]

c1 = []
r = max(a)
i = 1
m = 0
while m < min(b):
     m = r * i
     i += 1
     print(m)
     if all (m % j == 0 for j in a):
        c1.append(m)
count = 0
result = []
for i in c1:
     if all (j % i == 0 for j in b):
          count += 1
print (count)


