from tkinter import *
from tkinter.ttk import *
import os

'''
显示学生明细信息。主要显示的内容有：学号、姓名、性别、出生日期、身份证号码、手机号码、邮箱地址、家庭住址、入学时间、专业、紧急联系人、
紧急联系电话；其中性别我们通过Radiobutton的方式显示，其余都通过Label和Entry来显示。
'''


class DetailWindow(Toplevel):  # 已经Tk实例化了一个主窗体,第二个窗体必须要以子窗体的形式打开 Toplevel
    def __init__(self, action_flag):
        super().__init__()
        self.title("学生明细信息")
        self.geometry("700x550+600+150")
        self.resizable(0, 0)  # 不能改变大小
        # action_flag = 1
        self.flag = action_flag
        # 加载控件
        self.setup_UI()
        self.load_windows_flag()

    def setup_UI(self):
        # 设置style
        self.Style02 = Style()
        self.Style02.configure("title.TLabel", font=("微软雅黑", 25, "bold"), foreground="navy")
        self.Style02.configure("TLabel", font=("微软雅黑", 15, "bold"), foreground="navy")
        self.Style02.configure("TButton", font=("华文黑体", 15, "bold"), foreground="navy")
        self.Style02.configure("TEntry", font=("微软雅黑", 15, "bold"), width=10)
        self.Style02.configure("TRadiobutton", font=("微软雅黑", 15, "bold"), foreground="navy")
        # 加载上面的banner
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "stu_detail_banner.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack()
        # 添加一个title
        self.var_title = StringVar()
        self.Label_title = Label(self, text="==明细窗体==", style="title.TLabel")
        self.Label_title.place(x=395, y=20)
        # 加载一个pane
        self.Pane_detail = PanedWindow(self, width=680, height=380)
        self.Pane_detail.place(x=5, y=88)
        # 添加属性
        # 第一排：学号
        self.Label_sno = Label(self.Pane_detail, text="学号:")
        self.Label_sno.place(x=30, y=10)
        self.var_sno = StringVar()
        self.Entry_sno = Entry(self.Pane_detail, textvariable=self.var_sno, font=("微软雅黑", 16, "bold"), width=10)
        self.Entry_sno.place(x=80, y=8)
        # 姓名
        self.Label_name = Label(self.Pane_detail, text="姓名:")
        self.Label_name.place(x=220, y=10)
        self.var_name = StringVar()
        self.Entry_name = Entry(self.Pane_detail, textvariable=self.var_name, font=("微软雅黑", 16, "bold"), width=10)
        self.Entry_name.place(x=270, y=8)
        # 性别
        self.Label_gender = Label(self.Pane_detail, text="性别:").place(x=460, y=10)
        self.var_gender = IntVar()
        self.Radio_man = Radiobutton(self.Pane_detail, text="男", variable=self.var_gender, value=1)
        self.Radio_man.place(x=510, y=10)
        self.Radio_woman = Radiobutton(self.Pane_detail, text="女", variable=self.var_gender, value=0)
        self.Radio_woman.place(x=560, y=10)
        # 第二排：出生日期
        self.Label_age = Label(self.Pane_detail, text="出生日期:")
        self.Label_age.place(x=30, y=60)
        self.var_age = StringVar()
        self.Entry_age = Entry(self.Pane_detail, textvariable=self.var_age, font=("微软雅黑", 16, "bold"), width=12)
        self.Entry_age.place(x=125, y=58)
        # 身份证号码
        self.Label_id = Label(self.Pane_detail, text="身份证号码:")
        self.Label_id.place(x=295, y=60)
        self.var_id = StringVar()
        self.Entry_id = Entry(self.Pane_detail, textvariable=self.var_id, font=("微软雅黑", 16, "bold"), width=19)
        self.Entry_id.place(x=410, y=58)
        # 第三排：手机号码
        self.Label_mobile = Label(self.Pane_detail, text="手机号码:")
        self.Label_mobile.place(x=30, y=110)
        self.var_mobile = StringVar()
        self.Entry_mobile = Entry(self.Pane_detail, textvariable=self.var_mobile, font=("微软雅黑", 16, "bold"), width=14)
        self.Entry_mobile.place(x=130, y=108)
        # 邮箱地址
        self.Label_email = Label(self.Pane_detail, text="邮箱地址:")
        self.Label_email.place(x=320, y=110)
        self.var_email = StringVar()
        self.Entry_email = Entry(self.Pane_detail, textvariable=self.var_email, font=("微软雅黑", 16, "bold"), width=19)
        self.Entry_email.place(x=415, y=108)
        # 第四排：家庭住址
        self.Label_home = Label(self.Pane_detail, text="家庭住址:")
        self.Label_home.place(x=30, y=160)
        self.var_address = StringVar()
        self.Entry_home = Entry(self.Pane_detail, textvariable=self.var_address, font=("微软雅黑", 16, "bold"), width=41)
        self.Entry_home.place(x=130, y=158)
        # 第五排：入学时间
        self.Label_studyin = Label(self.Pane_detail, text="入学时间:")
        self.Label_studyin.place(x=30, y=210)
        self.var_studyin = StringVar()
        self.Entry_studyin = Entry(self.Pane_detail, textvariable=self.var_studyin, font=("微软雅黑", 16, "bold"), width=12)
        self.Entry_studyin.place(x=130, y=208)
        # 专业：
        self.Label_pro = Label(self.Pane_detail, text="专业:")
        self.Label_pro.place(x=300, y=210)
        self.var_pro = StringVar()
        self.Entry_pro = Entry(self.Pane_detail, textvariable=self.var_pro, font=("微软雅黑", 16, "bold"), width=24)
        self.Entry_pro.place(x=350, y=208)
        # 第六排：紧急联系人
        self.Label_emcon = Label(self.Pane_detail, text="紧急联系人:")
        self.Label_emcon.place(x=30, y=260)
        self.var_emcon = StringVar()
        self.Entry_emcon = Entry(self.Pane_detail, textvariable=self.var_emcon, font=("微软雅黑", 16, "bold"), width=11)
        self.Entry_emcon.place(x=150, y=258)
        # 紧急联系电话
        self.Label_emtel = Label(self.Pane_detail, text="紧急联系人电话:")
        self.Label_emtel.place(x=300, y=260)
        self.var_emtel = StringVar()
        self.Entry_emtel = Entry(self.Pane_detail, textvariable=self.var_emtel, font=("微软雅黑", 16, "bold"), width=16)
        self.Entry_emtel.place(x=460, y=258)
        # 放置两个按钮
        self.Button_save = Button(self, text="保存", style="TButton").place(x=350, y=472)
        self.Button_exit = Button(self, text="关闭", style="TButton").place(x=502, y=472)

    def load_windows_flag(self):
        if self.flag == 1:
            self.Label_title.configure(text="==查看学生明细==")
        elif self.flag == 2:
            self.Label_title.configure(text="==新建学生明细==")
        elif self.flag == 3:
            self.Label_title.configure(text="==修改学生明细==")


if __name__ == '__main__':
    this_window = DetailWindow()
    this_window.mainloop()
