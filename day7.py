
num = [1, 6, 4, 5, 3]
target = 11
res =  '-1'
flag = False
for i in range(len(num)-1):
    for j in range(i+1, len(num)):
        if num[i]+num[j] == target:
            res = num[i], num[j]
            break
print(res)

num = [1, 6, 4, 5,3]
target = 11
unique = set()
for i in num:
    required = target - i
    if required in unique:
        print(i, required)
        break
    unique.add(i)
    
num = [1, 2, 4, 5]
for i in range(len(num)-1):
    if num[i]+1 != num[i+1]:
        print(num[i]+1)
        break
    
l = [1, 2, 3, 4, 5]
k = 2
print( l[-k: ]+l[ :-k] )

#list rotation
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int(input())
rotation = k % len(l)
print(l[-rotation:]+l[:-rotation])