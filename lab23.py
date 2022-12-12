#Lab2
'''
expression = input('Напишите выражение без знака равно')
print(eval(expression))
'''

#lab3
def get_factors(n):
    factors = []
    div = 2
    while div <= n:
        if n % div == 0:
            factors.append(div)
            n /= div
        else:
            div += 1

    return factors

interval = int(input('Введите x: '))

for i in range(1, interval + 1 ):
    glist = get_factors(i)
    if (7 in glist) and (3 in glist) and (5 in glist):
        print(i)