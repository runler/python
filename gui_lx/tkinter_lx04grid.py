# grid窗体布局
from tkinter import *

'''
grid是一种网格布局，grid(row = 1,column = 2)，n行n列分别表示表格的行数和列数，从0开始计数；
可以使用参数sticky控制控件靠近单元格的位置，字符值可以给出n、s、w、e设置上、下、左、右，我们还是以登录窗体为例：
'''
root = Tk()
root.title("用户登录")
root.geometry("520x270")
# 表格图片
photo = PhotoImage(file="./img/login.png")
img_label = Label(root, image=photo).grid(row=0, column=0, rowspan=2)
# 第一行 第二列
Label_username = Label(root, text="用户名：", font=("华文黑体", 16)).grid(row=0, column=1)
# 第一行 第三列
Entry_username = Entry(root, font=("华文黑体", 16)).grid(row=0, column=2)
# 第二行 第二列
Label_password = Label(root, text="密  码：", font=("华文黑体", 16)).grid(row=1, column=1)
# 第二行 第三列
Entry_password = Entry(root, font=("华文黑体", 16)).grid(row=1, column=2)
# 第四行 第二列
Button_login = Button(root, text="登录", width=8, font=("华文黑体", 16)).grid(row=3, column=2, sticky="e")
# 第四行 第三列
Button_cancer = Button(root, text="取消", width=8, font=("华文黑体", 16)).grid(row=3, column=2, sticky="w")

root.mainloop()
