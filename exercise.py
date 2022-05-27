'''
1. 打印九九乘法表
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end='\t' if i != j else '\n')


'''
2. 用户登陆, 只允许登陆3次，超过3次则锁死
'''
def login_account():
    count = 0
    while count < 3:
        username = input('Username: ')
        password = input('Password: ')
        if username == 'admin' and password == 'admin':
            print('welcome back, {}'.format(username))
            break
        else:
            print('Invalid. Try again')
            count += 1
    else:
        print('Locked')


'''
3. 求100以内奇数的和
'''
total = 0
for i in range(1, 100, 2):
    total += i
print(f'100以内奇数的和是{total}')


'''
4. 求斐波那契数列
'''
a = 0
b = 1
print(b, end=' ')
while True:
    if a + b >= 10:
        break
    print(a + b, end=' ')
    a, b = b, a + b

print()

a = 0
b = 1
count = 1
print(count, b, end=' ')
while True:
    count += 1
    if count > 11:
        break
    a, b = b, a + b
    print(count, b, end=' ')

print()


'''
5. 打印菱形
序列  空格  星号  空格  总空格
1     3     1     3     6
2     2     3     2     4
3     1     5     1     2
4     0     7     0     0
5     1     5     1     2
6     2     3     2     4
7     3     1     3     6

核心是找空格的规律，3210123，可以用range(-3, 4)取出
3是总数7的地板除
星号的规律是 总数-2*空格数的绝对值

'''
n = 7
e = 7 // 2
for i in range(-e, e + 1):
    print(' ' * abs(i), '*' * (n - 2 * abs(i)), sep='')

print()

for i in range(-e, e + 1):
    print('{:^{}}'.format('*' * (n - 2 * abs(i)), n))

'''
居中打印
'''
print(1, 'central'.center(30, '#'))
print(2, '{:#^30}'.format('central'))
print(3, '{:#^{}}'.format('central', 30))

