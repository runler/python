# 导包的时候使用*，创建控件的时候不用写类名了
from tkinter import *

'''
演示：画出能计算加法的计算器界面
'''
# 创建一个窗体，名称为root
root = Tk()  # 为窗体添加标题
root.title("求两数之和")
root.geometry("700x100")
photo = PhotoImage(file="./img/calc.png")
# 定义控件
PhotoLabel = Label(root, image=photo).pack(side=LEFT, padx=10, pady=5)
# 第一个数字文本框
Entry01 = Entry(root, bg="pink", width=10, font=("华文黑体", 20)).pack(side=LEFT, padx=5, pady=5)
# 加号
Label_plus = Label(root, text="+", font=("华文黑体", 20)).pack(side=LEFT, padx=5, pady=5)
# 第二个数字文本框
Entry02 = Entry(root, bg="pink", width=10, font=("华文黑体", 20)).pack(side=LEFT, padx=5, pady=5)
# 等于号
Label_equal = Label(root, text="=", font=("华文黑体", 20)).pack(side=LEFT, padx=5, pady=5)
# 第三个数字文本框
Entry03 = Entry(root, bg="green", width=10, font=("华文黑体", 20)).pack(side=LEFT, padx=5, pady=5)
Button01 = Button(root, text="计算", width=10, height=2, font=("华文黑体", 15)).pack(side=LEFT, padx=10, pady=5)
# 运行
root.mainloop()
