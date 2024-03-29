'''

open返回的是一个文件对象迭代器
可以用for循环逐行读取，需要调用encode().strip()方法去除换行

文件描述符：
0  标准输入
1  标准输出
2  标准错误输出

主模式：
r 只读模式，指针从0，如果没有文件则抛出异常
w 只写模式，如果没有则会新建文件，如果有文件会覆盖之前的内容，不能读只能写，指针从0
a 追加模式，如果没有文件则新建文件指针从0，如果文件已存会追加在文件末尾指针在EOF，需要添加换行符
x 新写模式，只创建新文件并有写的能力，不能读，文件存在则抛出异常，指针从0

主模式不能共存，只能使用其中之一

副模式：
t模式，必须要结合主模式一起使用，默认rt模式，代表text文本模式打开
b模式，二进制模式，rb，wb结合使用，读和写都是encode类型
+模式，补全模式，可以和主模式结合使用
        r+，可读写，指针从头开始，慎用
        w+，可读写，指针从头开始，慎用
        a+，可读写，指针在0或EOF打开，读取不到内容，想读则用seek到0
读和写一定要清楚文件指针的位置！否则读取异常

用wb的时候必须要编码写入字节序列
文件查看是字符串因为方便人阅读，如果用rb方式读则是byte类型

操作系统不会立刻把数据写入磁盘，而是先缓存起来
只有调用close()时，操作系统才会保证把没有写入的数据全部写入磁盘文件中
如果向文件写入数据后，不想马上关闭文件，也可以调用文件对象提供的 flush() 函数，它可以实现将缓冲区的数据写入文件中

文本文件在磁盘上就是二进制形式保存的字节序列，和编码无关
但是如果显示需要指定编码，每个编码不同对应的字符也不同

编码和解码必须用同一个字符集才可以，否则会乱码
在磁盘中都是0和1组成和字符集无关
所有文件都可以文本文件打开，只不过是乱码

seek操作的是字节指针！
seek(index， whence)，设置偏移量，whence：默认0代表相对于开头，1代表相对于current位置做偏移，2代表相对于EOF位置做偏移
seek(0)，到开头位置，可以非0，但不能负数
seek(0, 1)，相对于当前位置偏移0，文本模式只能写0；二进制模式可以是负数但不能左超界，可以右超界
seek(0, 2)，相对于结尾位置偏移0，文本模式只能是0；二进制模式可以是负数但不能左超界，可以右超界

tell()，返回当前的字位置，会调用flush()，指针会去EOF
flush(),将缓冲区内容写入磁盘

一般读写文件用a模式或者a+模式

read()，读出所有内容显示
readline()，读一行
readlines()，读完放到列表中，占用内存

with 关键字，自动close文件对象，防止文件抛出异常而没有关闭文件

'''

print('r模式'.center(30, '#'))
f = open('test', mode='r')
print(f, f.name, f.closed)
print(f.read())
f.seek(0)
print(f.readline().strip())
f.seek(0)
print(f.readlines())
f.close()

print('w模式'.center(30, '#'))
f = open('test', mode='w')
print(f.encoding)
f.write('如果打开文件模式中包含 w（写入），会先清空原文件中的内容，然后再写入新的内容\n')
f.close()

print('a模式'.center(30, '#'))
f = open('test', mode='a')
print(f.encoding)
f.write('如果打开文件模式中包含 a（追加），则不会清空原有内容，而是将新写入的内容会添加到原内容后边\n')
f.close()

print('rb模式'.center(30, '#'))
f = open('test', 'rb')
print(f.read())
f.close()

# print('r+模式'.center(30, '#'))
# f = open('test', 'r+')
# f.write('rrrrr+++++')
# f.close()

# 会清空之前的内容
print('w+模式'.center(30, '#'))
f = open('test', 'w+')
print(f.read())
f.write('w+会覆盖之前的内容\n')
f.close()

# # 指针会在EOF打开
f = open('test', 'a+')
f.write('aaaaa+++++\n')
f.close()

with open('test') as fo:
    print(fo.read())