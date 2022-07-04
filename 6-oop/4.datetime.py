'''
datetime 模块

datetime，可以相减，得到是delta对象
timezone，表示时区
timedelta，表示时间的增量，可以和datetime对象相加相减

'''

import datetime
import time

# 获取当前时间
d = datetime.datetime.now()
print(d)


# 1970年开始的秒数
print(d.timestamp())


# 通过时间戳来构建时间对象
d2 = datetime.datetime.fromtimestamp(d.timestamp())
print(d2)


# 通过字符串构建时间对象，格式必须和字符串一样
dstr = "2018-07-10 12:30:3"
d3 = datetime.datetime.strptime(dstr, "%Y-%m-%d %H:%M:%S")
print(d3)


# 通过时间对象构建字符串，格式必须和时间对象一样
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
d4 = d2.strftime('%Y-%m-%d %H:%M:%S')
print(d4)


d5 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
print(d5)


# 对当前时间做增量
d6 = d + datetime.timedelta(minutes=20, days=10)
print(d6)


# 获取当前UTC时间
print(datetime.datetime.utcnow())


# 获取年，月，周几
print(d.year, d.month, d.isoweekday())


# 当前线程阻塞一段时间
# time.sleep(5)

