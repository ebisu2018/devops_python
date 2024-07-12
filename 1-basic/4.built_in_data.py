'''
内建类型表示python天生具有的，不需要import就可以直接使用
python中常用的内建数据类型：
数值型，如int，float，bool
序列类型，list，tuple，bytes，bytearray
键值对类型，set，dict类型

父类都是type类型
python有隐式类型转换，如整型和浮点型相加得到浮点数
'''

import math

# // 整除，向下取整
print(1//2, 3//2, 5//2, 7//2)
print(-1//2, -3//2, -5//2, -7//2)

# 向下取整
print(math.floor(1.1), math.floor(1.5), math.floor(1.8))
print(math.floor(-1.1), math.floor(-1.5), math.floor(-1.8))

# 向上取整
print(math.ceil(1.1), math.ceil(1.5), math.ceil(1.8))
print(math.ceil(-1.1), math.ceil(-1.5), math.ceil(-1.8))

# 取整，保留整数部分
print(int(1.1), int(-1.1))

# 四舍五入
print(round(1.2), round(2.6), round(3.5))

# 幂运算，math模块的更精确
print(pow(2, 3), 2 ** 3, math.pow(2, 3))

# 开方
print(2 ** 0.5, math.sqrt(2))

# 返回最大值，参数要么是值，要么是可迭代对象
print(max(1, 2, 4, 8))
print(max(range(10)))
