'''

handler是负责日志真正输出的，可以输出到控制台或者文件
日志格式是定义在handler的Formatter中
常用的是StreamHandler和FileHandler
如果没有创建handler则是[]

如果自定义的logger中没有定义handler，则会用root的handler输出
默认handler的level是0，handler只有level，没有EffectiveLevel
propagate，控制是否想穿透root logger传播，logger打印的同时，root logger也会打印

当调用方法输出message的时候，决定了使用的log level级别
首先会和当前logger的EffectiveLevel比较，必须大于等于EffectiveLevel才会继续
然后和当前logger的handler的level比较，大于等于level时才会输出message
判断是否传播，如果是true，查找该logger的父类的handler并把message传递给其handler
如果是False，则不会传播给父类的handler输出

'''

import logging
from logging import handlers
import sys

root = logging.getLogger()
log1 = logging.getLogger(__name__)

# 创建stream handler
h1 = logging.StreamHandler(sys.stdout)
# 创建file handler
h2 = logging.FileHandler('2.log')

# 配置Formatter
h1.setFormatter(logging.Formatter('** %(message)s **'))
h2.setFormatter(logging.Formatter('-- %(message)s --'))

# 添加handler
log1.addHandler(h1)
log1.addHandler(h2)

print(log1.handlers)

# 是否传播给root
log1.propagate = False

log1.info('handler info')
log1.warning('handler warning')


# 创建一个时间滚动的Handler
# h3 = handlers.TimedRotatingFileHandler('time.log', 's', 10)
# h3.setFormatter(logging.Formatter('%(asctime)s --- %(message)s'))
# log1.addHandler(h3)
