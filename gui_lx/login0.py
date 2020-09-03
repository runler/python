from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import os


class LoginWindow(Tk):
    """
    创建登录窗体的GUI界面已经登录的方法
    """

    def __init__(self):
        super().__init__()  # 先执行tk这个类的初始化
        self.title("登录界面")
        # self.geometry("620x420")
        self.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
        self.iconbitmap("." + os.sep + "img" + os.sep + "msn.ico")
        # self["bg"] = "royalblue"
        # 加载窗体
        self.setup_UI()

    def setup_UI(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="royalblue")
        self.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="royalblue")
        # 创建一个Label标签展示图片
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "logingui.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack(padx=10, pady=10)
        # 创建一个Label标签 + Entry   --- 用户名
        self.var_user = StringVar()
        self.var_password = StringVar()
        self.Label_user = Label(self, text="用户名:", style="user.TLabel")
        self.Label_user.pack(side=LEFT, padx=10, pady=10)
        self.Entry_user = Entry(self, width=12, textvariable=self.var_user)
        self.Entry_user.pack(side=LEFT, padx=10, pady=10)
        # 创建一个Label标签 + Entry   --- 密码
        self.Label_password = Label(self, text="密码:", style="user.TLabel")
        self.Label_password.pack(side=LEFT, padx=10, pady=10)
        self.Entry_password = Entry(self, width=12, show="*", textvariable=self.var_password)
        self.Entry_password.pack(side=LEFT, padx=10, pady=10)
        # 创建一个按钮    --- 登录
        self.Button_login = Button(self, text="登录", width=4, command=self.login)
        self.Button_login.pack(side=LEFT, padx=20, pady=10)

    def login(self):
        # 获取用户的用户名和密码
        user = self.var_user.get()
        password = self.var_password.get()
        showinfo(message="用户名：" + user + "密码：" + password)  # 暂时用弹窗测试一下内容获取是否正常


if __name__ == '__main__':
    this_login = LoginWindow()
    this_login.mainloop()
