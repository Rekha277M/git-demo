n = int(input())
s = list(map(int, input("enter: ").split()))
count_positive = 0
count_negitive = 0
count_zeros = 0
for i in s:
    if i > 0:
        count_positive += 1
    elif i < 0:
        count_negitive += 1
    else:
        count_zeros += 1
print(count_positive, count_negitive, count_zeros)