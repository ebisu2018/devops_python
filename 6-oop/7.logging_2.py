'''

设置basicConfig，针对的是root logger的设置

如果使用的是如logging.info()的调用，默认使用的是root logger

提前进行basicConfig的设置，因为level只能设置一次！

basic config会设置level，format，datefmt，handler

'''

import logging

root = logging.getLogger()
print(root.level, root.getEffectiveLevel(), root.handlers)

FORMAT ='%(asctime)s %(name)s %(threadName)s %(message)s'
logging.basicConfig(
    level=logging.INFO, format=FORMAT, datefmt="%Y%m%d%H:%M:%S"
    # filename='1.log' # 可以指定输出到文件，不加则输出到控制台
)
logging.info('test info')

print(root.level, root.getEffectiveLevel(), root.handlers)
