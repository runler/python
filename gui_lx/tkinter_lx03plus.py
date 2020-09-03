# 实现加法计算器的的GUI界面
from tkinter import *
from tkinter.messagebox import *


# 写一个类：实现两数相加的页面和功能
class get_sum(object):
    def __init__(self):
        # 新建一个窗体
        self.frame = Tk()
        # 窗体添加标题
        self.frame.title("实现两数相加")
        self.frame.geometry("700x100")
        self.photo = PhotoImage(file="./img/calc.png")
        # 定义控件
        self.img_Label = Label(self.frame, image=self.photo)
        self.img_Label.pack(side=LEFT, padx=10, pady=5)
        # 第一个数字文本框
        self.num01_Entry = Entry(self.frame, bg="pink", width=10, font=("华文黑体", 20))
        self.num01_Entry.pack(side=LEFT, padx=5, pady=5)
        # 加号
        self.Label01 = Label(self.frame, text="+", font=("华文黑体", 20))
        self.Label01.pack(side=LEFT, padx=5, pady=5)
        # 第二个数字文本框
        self.num02_Entry = Entry(self.frame, bg="pink", width=10, font=("华文黑体", 20))
        self.num02_Entry.pack(side=LEFT, padx=5, pady=5)
        # 等于号
        self.Label02 = Label(self.frame, text="=", font=("华文黑体", 20))
        self.Label02.pack(side=LEFT, padx=5, pady=5)
        # 第三个数字文本框
        self.var = StringVar()
        self.result_Entry = Entry(self.frame, bg="green", width=10, font=("华文黑体", 20), textvariable=self.var)
        self.result_Entry.pack(side=LEFT, padx=5, pady=5)
        self.cal_Button = Button(self.frame, text="计算", width=10, height=2, font=("华文黑体", 15), command=self.cal_sum)
        self.cal_Button.pack(side=LEFT, padx=10, pady=5)

    # 展示窗体
    def run(self):
        self.frame.mainloop()

    # 实现两数相加
    def cal_sum(self):
        # 先取出字符串
        num01 = self.num01_Entry.get()
        num02 = self.num02_Entry.get()
        # 判断
        if num01.isdigit() and num02.isdigit():
            self.var.set(str(int(num01) + int(num02)))
        else:
            showinfo("系统提示", "输入的值不都是数字无法计算")


if __name__ == '__main__':
    # 由窗体的模板实例化一个具体的登录窗体
    this_main = get_sum()
    # 展示窗体
    this_main.run()
