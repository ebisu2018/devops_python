'''

CSV 称为逗号分隔值文件
逗号分隔值
每一行都是记录
每一项都转换成字符串
两个双引号表示一个双引号

'''

import csv

with open('info.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='.')
    writer.writerow(['www.biancheng.net'] * 5 + ['how are you'])
    writer.writerows([('hello world'), ('web site'), ('www.biancheng.net')])


with open('name.csv', 'w', newline='') as csvobj:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvobj, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Lovely', 'last_name': 'Spam'}])
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


with open('info.csv', 'r') as fobj:
    reader = csv.reader(fobj, delimiter='.')
    for row in reader:
        print(';'.join(row))


with open('name.csv') as fobj:
    reader = csv.DictReader(fobj)
    for row in reader:
        print(row)
