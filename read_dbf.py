#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'mayi'
# pip install dbfread
# 导入模块 from dbfpy import dbf
from dbfread import DBF

# 数据表文件名
table = DBF('test.dbf')

# 遍历dbf文件结构
for field in table.fields:
    print(field)

# 遍历数据表中（没加删除标志）的记录
for record in table:
    for field in record:
        print(field, "=", record[field], end=",")
    print()

print("*" * 40)

# 遍历数据表中（加了删除标志）的记录
for record in table.deleted:
    for field in record:
        print(field, "=", record[field], end=",")
    print()
