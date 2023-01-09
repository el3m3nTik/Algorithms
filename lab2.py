s = input('Введите выражение без знака = ')
stack = []
is_true = True
for i in s:
    if i in '([{':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            is_true = False
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        if open_bracket == '[' and i == ']':
            continue
        if open_bracket == '{' and i == '}':
            continue
        is_true = False
        break
if is_true and len(stack) == 0:
    print(eval(s))
else:
    print('Проверьте правильность скобок', end='\n')