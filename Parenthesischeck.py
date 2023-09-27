n = input()

count = 0

for i in n:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
    if count < 0:
        break

if count == 0:
    print('Valid')
else:
    print(f'Invalid Parenthesis')