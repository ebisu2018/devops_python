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
