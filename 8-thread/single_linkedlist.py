'''

单向链表
因为不是列表那种顺序排放的，因粗需要记录下一项

'''

from __future__ import annotations


# 元素的类，又元素自身的值以及指向下个元素的属性
class Node:
    def __init__(self, value, next:Node=None):
        self.item = value
        self.next = next

    def __repr__(self):
        return str(self.item)


# 链表类，记录头和尾的元素
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        return self

    def iternodes(self):
        current:Node = self.head
        while current:
            yield current
            current = current.next


single = LinkedList()
single.append(1).append(2)
for i in single.iternodes():
    print(i)
