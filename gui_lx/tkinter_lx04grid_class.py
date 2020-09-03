from tkinter import *
from tkinter.messagebox import *

'''
这里我们使用类来封装GUI程序，以至于我们后面需要调用的时候直接实例化一个对象就可以产生一个窗口，类与对象的知识我们后面会深入讲解，
现在我们只需怎么使用即可；我们把前面的登录窗口通过类来进行封装
需求：
（1）如果用户名为admin，密码为123.com,显示登录成功！
（2）如果用户名不对，显示用户名不存在；
（3）如果密码不对，显示密码错误，如果错误三次，提示：账号已锁定。
提示：实现窗体的关闭，可以使用方法self.frame.destory()关闭窗体；
'''


class LoginGUI(object):
    def __init__(self):
        """
        窗体的构造函数，用来做界面的初始化，GUI代码放在此函数中
        """
        self.frame = Tk()
        self.frame.title("用户登录")
        self.frame.geometry("520x270")
        # 表格图片
        self.photo = PhotoImage(file="./img/login.png")
        self.img_label = Label(self.frame, image=self.photo).grid(row=0, column=0, rowspan=2)
        # 第一行 第二列
        self.Label_username = Label(self.frame, text="用户名：", font=("华文黑体", 16)).grid(row=0, column=1)
        # 第一行 第三列
        # 注意：控件基本属性的设定和控件的布局语句要分开,否则取出文本框的数值可以使用get()方法取不到，设置文本框的数值可以使用set()方法；；
        self.Entry_username = Entry(self.frame, font=("华文黑体", 16))
        self.Entry_username.grid(row=0, column=2)
        # self.Entry_username = Entry(self.frame, font=("华文黑体", 16)).grid(row=0, column=2)
        # 第二行 第二列
        self.Label_password = Label(self.frame, text="密  码：", font=("华文黑体", 16)).grid(row=1, column=1)
        # 第二行 第三列
        self.Entry_password = Entry(self.frame, show="*", font=("华文黑体", 16))
        self.Entry_password.grid(row=1, column=2)
        # 第四行 第二列
        self.Button_login = Button(self.frame, text="登录", width=8, font=("华文黑体", 16),
                                   command=self.login).grid(row=3, column=2, sticky="e")
        # 第四行 第三列
        self.Button_cancer = Button(self.frame, text="取消", width=8, font=("华文黑体", 16),
                                    command=self.cancer).grid(row=3, column=2, sticky="w")
        # 定义全局变量
        self.password_error_times = 0
        self.is_disable = False

    def run(self):
        self.frame.mainloop()

    def login(self):
        # 【1】先获取用户名和密码
        username = str(self.Entry_username.get())
        password = str(self.Entry_password.get())
        # 【2】验证
        if username.strip().lower() != "admin":
            showinfo("系统消息", "用户名不存在，请核实后再登录！")
        elif password.strip() != "123.com":
            self.password_error_times += 1
            # 判断是否达到三次
            if self.password_error_times >= 3:
                self.is_disable = True
            # 判断禁用标志
            if self.is_disable:
                showinfo("系统消息", "密码输入错误已达三次，账号已锁定，请联系管理员")
            else:
                showinfo("系统消息", "密码错误！")

        else:
            showinfo("系统消息", "登录成功")
            # 如果在3次以内输入正确，则错误次数计数归零
            self.password_error_times = 0

    def cancer(self):
        # 实现窗体的关闭
        self.frame.destroy()


if __name__ == '__main__':
    # 由窗体的模板实例化一个具体的登录窗体
    this_login = LoginGUI()
    # 展示窗体
    this_login.run()
