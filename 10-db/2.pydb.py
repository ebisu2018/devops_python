'''

pymysql是python写的mysql客户端

'''

import pymysql
import simplejson

with open('conf.json', encoding='utf-8') as f:
    conf = simplejson.load(f)

print(conf)
conn = None
cursor = None
try:
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()
    isql = """insert into student (name, age) values ('tim', 20)"""
    i = cursor.execute(isql)
    print(i)
    conn.commit()

    ssql = '''select * from student'''
    cursor.execute(ssql)
    print(cursor.rownumber, cursor.rowcount)
    print(cursor.fetchone())
    print(cursor.fetchall())


except Exception as e:
    conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
