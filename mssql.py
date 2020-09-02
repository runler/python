# pymssql官方:https://pypi.org/project/pymssql/      
# import pymssql  # 引入pymssql模块


# def conn():
#     connect = pymssql.connect('190.5.58.7', 'sa','cjl2012', 'This40_yy')  # 服务器名,账户,密码,数据库名
#     if connect:
#         print("连接成功!")

#     return connect

# if __name__ == '__main__':
#     conn = conn()

# #  创建一个新数据库表:
import pymssql
connect = pymssql.connect('190.5.58.7', 'sa','cjl2012', 'This40_yy')   # 建立连接
if connect:
    print("连接成功!")

# 增删改查(CRUD)
cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
# cursor.execute("create table C_test(id varchar(5),name varchar(10),sex varchar(4))")  # 执行sql语句
sql = "insert into C_test (id, name, sex)values(1004, '李四', '男')"
cursor.execute(sql)  # 执行sql语句
connect.commit()  # 提交
cursor.close()
# 查询(Retrieve):
cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
sql = "select id,name, sex from C_test"
cursor.execute(sql)  # 执行sql语句
row = cursor.fetchone()  # 读取查询结果,
while row:  # 循环读取所有结果
    print("Id=%s,Name=%s, Sex=%s" % (row[0], row[1], row[2]))  # 输出结果
    row = cursor.fetchone()

cursor.close()
connect.close()

# # 配置数据库读取存储过程
# # 注：变量前面要加@，要是调用存储过程无需传参可忽略；
# # pymssql 2.0以上可通过cursor.callproc方法调用存储过程cursor.callproc('存储过程','参数元组') 需使用cursor.nextset()才能得到结果集
# # # import pymssql
# """配置"""
# server = 'xxx'
# user = 'xxx'
# password = 'xxx'
# database = 'xxx'
# """连接数据库"""
# conn = pymssql.connect(server, user, password, database)
# cursor = conn.cursor()
# cursor.execute(f"exec 存储过程名称 @参数1='xxx',@参数2='xxx',@参数3='xxx',@参数4='xxx'")
# result = cursor.fetchall()  # 得到结果集
# for i in result:
#     print(i)  # 遍历打印查询结果集的数据
