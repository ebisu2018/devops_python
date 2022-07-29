'''

IO
一个进程在内存中的模型
用户空间：想用内核空间的数据需要从内核态复制过来
内核空间：只操作系统内核使用，被保护的

CPU级别：
ring0，级别最高，可以使用所有范围内存，特权指令如系统调用
ring3，用户指令，只在用户空间使用

IO的两个阶段：
从设备读取数据到内核空间缓冲区
从内核空间的数据复制到用户空间缓冲区

分类：
阻塞IO，同步阻塞IO，比如socket的recv，需要多个线程，切换线程代价高
非阻塞IO，同步非阻塞IO，效率低，总是轮询，少用
IO多路复用，事件驱动IO，重要！

IO多路复用：
OS代替而不用自己阻塞或者轮询
事件驱动，如果数据到了会中断
select可以注册很多事件

bio就是同步IO
aio就是异步IO


'''