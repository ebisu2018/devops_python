'''

序列化：就是把内存中的数据结构保存到磁盘上或在网络上传输的格式
遵循一定的协议
内存到二进制是序列化
二进制到内存是反序列化

数据在内存中都是0和1，转换成16进制，如何解读数据取决于用什么方式打开
数据在内存中需要有类型，数据，边界才能确保能被反序列化

dump(obj, file)，把数据结构序列化到文件
dumps(obj)，把数据结构序列化成二进制
load(file)，从文件中反序列化到数据结构
loads(obj)，从序列化对象中反序列化到数据结构

pickle库只是python中用的，不能实现跨语言
一般使用公共的格式如json，可以跨语言处理

文本序列化主要用Json，Netscape公司的产品，简单易读，多种编程语言都支持
用文本定义，可以直接处理

Json特点：
字符串必须用双引号，key必须是字符串
都是小写的，支持的类型是常用的基本数据类型
可以对顺序表序列化，集合不支持序列化，元组类型会被转换成列表类型

Json被大括号包裹起来，序列化后本质是字符串类型
使用场景：配置文件，web开发


msgpack序列化
二进制序列化，节省空间，效率高跨语言，比pickle好

'''

import pickle
import json
import msgpack

l = 'a'
with open('pickle.txt', 'wb') as fo:
    pickle.dump(l, fo)

s = pickle.dumps(l)
print(s, type(s))

print(pickle.loads(s))

with open('pickle.txt', 'rb') as fo:
    x = pickle.load(fo)
    print(x, type(x))

print('Json'.center(30, '#'))

d = {'name': 'jose', 'color': 'blue', 'class': ['python'], 'interest': ('movie', 'music')}

# 序列化成json
x = json.dumps(d)
print(x, type(x))

# 反序列化成python对象
d1 = json.loads(x)
print(d1, type(d1))

with open('d.json', 'w') as f:
    json.dump(d, f)

with open('d.json', 'r') as f:
    p = json.load(f)
    print(p, type(p))


print('msgpack'.center(30, '#'))

x = msgpack.dumps(d)
print(x, type(x))

y = msgpack.loads(x)
print(y, type(y))

print(msgpack, msgpack.__name__)

print(msgpack.__file__)

content = 'abd 123 ** 9 {. {"id":"10"} aaasd {"foo": {"id": [1234]}} aae 324'


def extract_json_blobs(input_content):
    for i in range(len(input_content)):
        if input_content[i] == '{':
            for j in range(len(input_content) - 1, i, -1):
                if input_content[j] == '}':
                    try:
                        print(json.loads(content[i: j + 1]))
                        # yield json.loads(content[i: j + 1])
                        i = j
                        break
                    except json.JSONDecodeError as e:
                        print(e)


extract_json_blobs(content)

payload = ''
filename = 'foldername/MyFilename.json'
# filename = 'MyFilename'
error_folder = 'error'
new_filename = filename.replace('json', 'txt') if filename.endswith('.json') else f'{filename}.txt'
part_list = new_filename.split('/')
part_list.insert(-1, error_folder)
error_path = '/'.join(part_list)
print(error_path)
