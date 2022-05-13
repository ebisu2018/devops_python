# 1. 打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j}', sep='\t', end='\t')
    print()


# 2. 用户登陆，输入错误超过3次则锁死
count = 0
while count < 3:
    username = input('Username: ')
    password = input('Password: ')
    if username == 'admin' and password == 'admin':
        print('welcome back, {}'.format(username))
        break
    else:
        print('Incorrect username or password')
        count += 1
else:
    print('Locked')


# 求100以内奇数的和
sum = 0
for i in range(1, 10, 2):
    sum += i
print(f'100以内奇数的和是{sum}')

# 求100以内斐波那契数列的和
# 0 1 1 2 3
a = 0
b = 1
sum = 0
for i in range(5):
    sum = a + b
    a = b
    b = sum

print(f'100以内斐波那契数列的和是{sum}')

# 求斐波那契数列第101项的值