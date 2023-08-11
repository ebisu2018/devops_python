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
# 普通版本
def fib1(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

print(fib1(10))


# 生成器函数版本
def fib2():
    a = 1
    yield a
    b = 1
    yield b
    while True:
        a, b = b, a + b
        yield b


# 递归版本
def fib3(n, a=1, b=1):
    if n < 3:
        return b
    a, b = b, a + b
    return fib3(n - 1, a, b)


print(fib3(10))

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


'''
9. 冒泡排序算法
5， 8， 4， 1
长度是n，要比n-1轮
每一轮要比较n-轮数-1

第一轮
5841
5481
5418

第二轮
4518
4158

第三轮
1458

'''

data = [5, 8, 4, 1]
for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)
