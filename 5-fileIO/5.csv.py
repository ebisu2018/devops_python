'''

csv
逗号分隔值
每一行都是记录
每一项都转换成字符串
两个双引号表示一个双引号


'''

import csv

rows = [
    ('id', 'name', 'age', 'desc'),
    [1, 'Josh', 50, """Josh"s name"""],
    [2, 'Leo', 45, "Leo's name"],
    [3, 'Jack', 30, "Jack's name"]
]

# with open('info.csv', 'w') as fo:
#     for line in rows:
#         fo.write(",".join(map(str, line)) + '\n')

with open('info.csv', 'w') as f:
    writer = csv.writer(f)
    # writer.writerow(rows[0])
    writer.writerows(rows[:])


with open('info.csv', 'r') as f:
    reader = csv.reader(f) # 返还迭代器
    for line in reader:
        print(line)
