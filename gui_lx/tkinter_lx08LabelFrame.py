# 把具有相同功能的模块组合在一起，并且加上一个名字，这个控件能让你的界面更加有条理
# LabelFrame
from tkinter import Tk, Label, LEFT, Entry, Button, LabelFrame
# from tkinter.ttk import LabelFrame

root = Tk()
root.title("LabelFrame控件")
LabelFrame_query = LabelFrame(root, text="学生信息查询")
LabelFrame_query.pack(padx=10, pady=10)
# 如果不加控件的话，LabelFrame是看不见的
Label01 = Label(LabelFrame_query, text="学号")
Label01.pack(side=LEFT, padx=5, pady=5)
Entry01 = Entry(LabelFrame_query, width=10)
Entry01.pack(side=LEFT, padx=5, pady=5)
Label02 = Label(LabelFrame_query, text="姓名")
Label02.pack(side=LEFT, padx=5, pady=5)
Entry02 = Entry(LabelFrame_query, width=10)
Entry02.pack(side=LEFT, padx=5, pady=5)
Label03 = Label(LabelFrame_query, text="班级")
Label03.pack(side=LEFT, padx=5, pady=5)
Entry03 = Entry(LabelFrame_query, width=10)
Entry03.pack(side=LEFT, padx=5, pady=5)
Button01 = Button(LabelFrame_query, text="查询", width=5)
Button01.pack(side=LEFT, padx=15, pady=5)
root.mainloop()
