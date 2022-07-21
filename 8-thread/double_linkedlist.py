'''

双向链表

'''

from __future__ import annotations


class Node:
    def __init__(self, item, next: Node = None, prev: Node = None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "{} <<== {} ==>> {}".format(
            self.prev.item if self.prev else None,
            self.item,
            self.next.item if self.next else None
        )


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
            node.prev = self.tail
        self.tail = node
        return self

    def iternodes(self, reverse=False):
        current:Node = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def pop(self):
        if self.head is None:
            raise Exception('Empty')

        node = self.tail
        # 只有一个的
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else: # 假设多个
            prev = node.prev
            prev.next = None
            self.tail = prev
        return node

    def insert(self, index, value):
        if index < 0:
            raise IndexError(f'Not negative Index: {index}')

        current = None
        for i, node in enumerate(self.iternodes()):
            if index == i:
                current = node
                break
        else: # 没找到则追加尾部
            self.append(value)
            return

        node = Node(value)
        # 只有一个元素插入
        if current.prev is None:
            self.head = node
        else: # 从中间插入
            node.prev = current.prev
            current.prev.next = node
        node.next = current
        current.prev = node

    def remove(self, index):
        if self.head is None:
            raise Exception('Empty')
        if index < 0:
            raise IndexError(f'Not negative Index: {index}')

        current = None
        for i, node in enumerate(self.iternodes()):
            if index == i:
                current = node
                break
        else:
            raise IndexError(f'Index out of range: {index}')

        # 只有1个元素
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # 开头元素
        elif current.prev is None:
            self.head = current.next
            current.next.prev = None
        # 末尾位置
        elif current.next is None:
            self.tail = current.prev
            current.prev.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        del current


dou = LinkedList()
dou.append(1).append(2).append(3)
for i in dou.iternodes():
    print(i)
dou.pop()