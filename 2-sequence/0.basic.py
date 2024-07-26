'''
线性表分为顺序表（序列）和链表
Python 序列（Sequence）是指按特定顺序依次排列的一组数据，它们可以占用一块连续的内存，也可以分散到多块内存中。
Python 中的序列类型包括列表（list）、元组（tuple）、字典（dict）和集合（set）

列表（list）和元组（tuple）比较相似，它们都按顺序保存元素，所有的元素占用一块连续的内存，每个元素都有自己的索引
因此列表和元组的元素都可以通过索引（index）来访问
它们的区别在于：列表是可以修改的，而元组是不可修改的。
字典（dict）和集合（set）存储的数据都是无序分散的，每份元素占用不同的内存，其中字典元素以 key-value 的形式保存。

顺序表：物理内存中开辟一段连续有序的空间，首地址已经分配固定，用index来表示索引，每个元素占用4字节
链表:
内存中没有顺序存放，但是依然有index的有序序列
链表自己记录了head地址，tail地址，和前一个以及后一个的地址

栈，属于LIFO，后进先出
<<<<<<< HEAD
队列，分为FIFO，先进先出

时间复杂度是效率考量标准，O(1)表示固定的，随着N增大，时间依然不变
O(N)表示随着N的增大，耗时增加
'''
