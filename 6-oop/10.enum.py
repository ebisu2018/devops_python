'''
Python 3.4 中新增加了 Enum 枚举类
枚举类需要继承自 enum 模块中的 Enum 类
枚举类的每个成员都由 2 部分组成，分别为 name 和 value
其中 name 属性值为该枚举值的变量名（如 red），value 代表该枚举值的序号（序号通常从 1 开始）
枚举类不能用来实例化对象
枚举类中各个成员的值，不能在类的外部做任何修改

'''

from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


print(Color.red)
print(Color['blue'])
print(Color(1))

print(Color.red.name)
print(Color.red.value)

for color in Color:
    print(color.name, color.value)


season = Enum("Season", ('spring', 'summer', 'autumn', 'winter'))
print(season['summer'])

for s in season:
    print(s)
