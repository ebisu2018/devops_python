'''

logging模块非常重要！

组件：
Logger，日志记录器，负责有效级别设定，父子类的继承关系
RootLogger，Logger的子类，作用同Logger
Handler，日志处理器，负责生成处理日志的
Formatter，负责格式输出的

logging.getLogger()
如果没找到名字，会创建一个该名字的logger
如果没指定名字，则返回root logger
自定义logger是root logger的子类

root的默认level是30，自定义名字的level默认是0，需要自己设定
EffectiveLevel默认都是30
机制：
如果level是0，EffectiveLevel会向上继承其父类（root）的level 30
如果level非0，则EffectiveLevel和level相同

输出日志信息的原则：
msg的level必须 大于等于 EffectiveLevel，才会输出msg

问题：为什么已经setLevel到20，依然无法打印info的日志？

'''

import logging

root = logging.getLogger()
# print(root)

# 一般是__name__来设定自定义名
log1 = logging.getLogger(__name__)
# print(log1)

# 第一次会默认使用30，自定义会继承30，但是level没有设置一定是0
print(root.level, root.getEffectiveLevel(), log1.level, log1.getEffectiveLevel())
log1.warning('test warning')

# Issue
log1.setLevel(20)
print(log1.level, log1.getEffectiveLevel())
log1.info('test info')

