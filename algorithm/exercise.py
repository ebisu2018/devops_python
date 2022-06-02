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

# login_account()

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
6. 对3个整数进行大小比较，升序输出
'''
def sort_abc():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    if a > b:
        if c > a:
            print(c, a, b)
        elif c < a and c > b:
            print(a, c, b)
        else:
            print(a, b, c)
    else:
        if c > b:
            print(c, b, a)
        elif b > c and c > a:
            print(b, c, a)
        else:
            print(b, a, c)
# sort_abc()


'''
7. 基于一个列表生成一个新列表，元素是第一个相邻2项的和
'''
l1 = [1, 4, 9, 16, 25, 36]
l2 = [l1[i] + l1[i + 1] for i in range(len(l1) - 1)]
print(l2)


'''
8. 随机生成100个产品ID
数字6位，分隔符号，10个随机小写英文
'''
import string
import random

alphabet = string.ascii_lowercase
for i in range(10):
    prod_id = "{:0>6}.{}".format(i, ''.join(random.choices(alphabet, k=10)))
    print(prod_id)
