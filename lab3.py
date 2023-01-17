import math
x = 10000000
count = 0
for y in range(1, int(math.log(x))):
    for z in range(0, int(math.log(x))):
        for u in range(0, int(math.log(x))):
            if (3**y * 5**z * 7**u) < x:
                print(3**y * 5**z * 7**u)
                count += 1
            else:
                break
print(count)