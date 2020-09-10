from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os


class ChangePasswordWindow(Toplevel):
    def __init__(self, current_login_list):
        super().__init__()
        self.title("修改密码")
        self.geometry("700x550+600+150")
        self.resizable(0, 0)  # 不能改变大小
        self.current_login_list = current_login_list
        self.file_path = "./User.txt"  # 文件路劲  = login0.py中的
        self.all_login_list = []  # 存储所有的用户登录信息
        self.get_all_login()  # 获取所有用户信息
        # 加载界面
        self.setup_UI()

    def setup_UI(self):
        # 设置style
        self.Style01 = Style()
        self.Style01.configure("title.TLabel", font=("微软雅黑", 25, "bold"), foreground="navy")
        self.Style01.configure("TLabel", font=("微软雅黑", 20, "bold"), foreground="navy")
        self.Style01.configure("TButton", font=("微软雅黑", 16, "bold"), foreground="navy")
        self.Style01.configure("TEntry", font=("微软雅黑", 16, "bold"), width=10)
        self.Style01.configure("TRadiobutton", font=("微软雅黑", 16, "bold"), foreground="navy")
        # 加载上面的banner
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "stu_detail_banner.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack()
        # 添加一个title
        self.Label_title = Label(self, text="==修改密码==", style="title.TLabel")
        self.Label_title.place(x=400, y=20)
        # 加载一个pane
        self.Pane_detail = PanedWindow(self, width=590, height=380)
        self.Pane_detail.place(x=5, y=88)
        # 账号
        self.Label_login = Label(self.Pane_detail, text="当前用户名:")
        self.Label_login.place(x=160, y=70)
        self.var_login = StringVar()
        self.Entry_login = Entry(self.Pane_detail, state=DISABLED, textvariable=self.var_login,
                                 font=("微软雅黑", 18, "bold"), width=12)
        self.Entry_login.place(x=310, y=68)
        # 初始化当前用户
        self.var_login.set(self.current_login_list[0])
        # 旧密码
        self.Label_old_password = Label(self.Pane_detail, text="验证旧密码:")
        self.Label_old_password.place(x=160, y=120)
        self.var_old = StringVar()
        self.Entry_old_password = Entry(self.Pane_detail, show="*", textvariable=self.var_old,
                                        font=("微软雅黑", 18, "bold"), width=12)
        self.Entry_old_password.place(x=310, y=118)
        # 新密码
        self.Label_new_password = Label(self.Pane_detail, text="设置新密码:")
        self.Label_new_password.place(x=160, y=170)
        self.var_new = StringVar()
        self.Entry_new_password = Entry(self.Pane_detail, show="*", textvariable=self.var_new,
                                        font=("微软雅黑", 18, "bold"), width=12)
        self.Entry_new_password.place(x=310, y=168)
        # 确认新密码
        self.Label_two_new_password = Label(self.Pane_detail, text="确认新密码:")
        self.Label_two_new_password.place(x=160, y=220)
        self.var_two_new = StringVar()
        self.Entry_two_new_password = Entry(self.Pane_detail, show="*", textvariable=self.var_two_new,
                                            font=("微软雅黑", 18, "bold"), width=12)
        self.Entry_two_new_password.place(x=310, y=218)
        # 放置两个按钮
        self.Button_save = Button(self, text="保存", style="TButton", command=self.commit)
        self.Button_save.place(x=300, y=472)
        self.Button_exit = Button(self, text="关闭", style="TButton", command=self.close_window)
        self.Button_exit.place(x=450, y=472)

    def commit(self):
        # 获取输入的值
        old_pass = self.var_old.get()
        new_pass = self.var_new.get()
        new_two = self.var_two_new.get()
        # 判断旧密码输入是否正确
        if old_pass != self.current_login_list[1]:
            showinfo("系统提示", "旧密码错误")
            return

        if new_pass == old_pass:
            showinfo("系统提示", "新密码和旧密码一样！系统不允许")
            return
        if len(new_pass.strip()) == 0:
            showinfo("系统提示", "新密码不许为空")
            return
        if new_pass != new_two:
            showinfo("系统提示", "两次新密码不一致！")
            return
        # 修改密码
        for index in range(len(self.all_login_list)):
            if self.all_login_list[index][0] == self.current_login_list[0]:
                self.all_login_list[index][1] = new_pass
        # 用户密码写入文件
        try:
            with open(self.file_path, mode="w") as fd:
                fd.write("")
            with open(self.file_path, mode="a") as fd:
                for item in self.all_login_list:
                    temp = ",".join(item)
                    temp = temp.replace("\n", "") + "\n"
                    fd.write(temp)
        except:
            showinfo("系统消息", "写入文件出现异常")
        showinfo("系统消息", '用户【'+self.current_login_list[0]+'】密码已修改并保存成功!')
        self.destroy()

    def close_window(self):
        self.destroy()

    def get_all_login(self):
        if not os.path.exists(self.file_path):
            showinfo("系统消息", "提供的文件名不存在！")
        else:
            try:
                with open(file=self.file_path, mode="r") as fd:
                    # 一次读一行
                    current_line = fd.readline()
                    while current_line:
                        temp_list = current_line.split(",")  # 长字符串分割层三个
                        self.all_login_list.append(temp_list)
                        # 读取下一行,读完了循环就结束了
                        current_line = fd.readline()
            except:
                showinfo("系统消息", "文件读取出现异常！")
