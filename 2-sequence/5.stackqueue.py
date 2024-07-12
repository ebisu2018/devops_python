# 使用标准库的 collections 模块中的 deque 结构体
# 它被设计成在两端存入和读取都很快的特殊list，可以用来实现栈和队列的功能
# 效率比list的append要高

import collections

queue_and_stack = collections.deque()
queue_and_stack.append(1)
queue_and_stack.append(2)
queue_and_stack.append(3)

print(list(queue_and_stack))

# 实现队列功能，从队列中取一个元素，根据先进先出原则，pop从左侧
print(queue_and_stack.popleft())

# 实现栈功能，从栈里取一个元素，根据后进先出原则,pop()从右侧
print(queue_and_stack.pop())
print(queue_and_stack)
