x = 50
for i in range(1, x):
    for x in range(0, x):
        for y in range(0, x):
            for z in range(0, x):
                if 3**x * 5**y * 7**z == i:
                    print(i)