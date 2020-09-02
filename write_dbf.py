'''
写DBF文件
@filename 文件名
@header   列头
@content  内容
'''
from dbfpy import dbf  # 报错


def writeDbfFile(filename, header, content):
    # 打开dbf
    db = dbf.Dbf(filename, new=True)
    # 写列头
    for field in header:
        # 此处需要改成长度可配的，长度太短会导致数据被截断
        if type(field) == unicode:
            field = field.encode('GBK')
        db.addField((field, 'C', 20))

    # 写数据
    for record in content:
        rec = db.newRecord()
        for key, value in itertools.izip(header, record):
            if type(value) == unicode:
                rec[key] = value.encode('GBK')
            else:
                rec[key] = value
            rec.store()
    # 关闭文档
    db.close()
