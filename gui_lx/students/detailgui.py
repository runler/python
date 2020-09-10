from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
import os

'''
显示学生明细信息。主要显示的内容有：学号、姓名、性别、出生日期、身份证号码、手机号码、邮箱地址、家庭住址、入学时间、专业、紧急联系人、
紧急联系电话；其中性别我们通过Radiobutton的方式显示，其余都通过Label和Entry来显示。
'''


class DetailWindow(Toplevel):  # 已经Tk实例化了一个主窗体,第二个窗体必须要以子窗体的形式打开 Toplevel
    def __init__(self, action_flag, current_student, all_student_list):
        super().__init__()
        self.title("学生明细信息")
        self.geometry("700x550+600+150")
        self.resizable(0, 0)  # 不能改变大小
        # action_flag = 1
        self.flag = action_flag
        self.current_student_list = current_student
        self.all_student_list = all_student_list
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
        self.Button_save = Button(self, text="保存", style="TButton", command=self.commit).place(x=350, y=472)
        self.Button_exit = Button(self, text="关闭", style="TButton", command=self.colse_window).place(x=502, y=472)

    def load_student_detail(self):
        if self.flag != 2 and len(self.current_student_list) == 0:
            showinfo("系统消息", "没有任何数据需要展示!")
        else:
            if self.flag == 2:
                self.current_student_list = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '','' ]
            self.var_sno.set(self.current_student_list[0])  # 学号
            self.var_name.set(self.current_student_list[1])  # 姓名
            if "男" in self.current_student_list[2]:  # 性别
                self.var_gender.set(1)
            else:
                self.var_gender.set(2)
            self.var_age.set(self.current_student_list[3])  # 生日
            self.var_mobile.set(self.current_student_list[4])  # 电话号码
            self.var_email.set(self.current_student_list[5])  # 邮箱
            self.var_address.set(self.current_student_list[6])  # 地址
            self.var_id.set(self.current_student_list[7])  # 身份证号
            self.var_studyin.set(self.current_student_list[8])  # 入学时间
            self.var_pro.set(self.current_student_list[9])  # 专业
            self.var_emcon.set(self.current_student_list[10])  # 紧急联系人
            self.var_emtel.set(self.current_student_list[11])  # 紧急联系号码

    def load_windows_flag(self):
        if self.flag == 1:
            self.Label_title.configure(text="==查看学生明细==")
            # self.Button_save.place_forget()  # 报错！！！
            self.Entry_sno["state"] = DISABLED
            self.Entry_name["state"] = DISABLED
            self.Radio_man["state"] = DISABLED
            self.Radio_woman["state"] = DISABLED
            self.Entry_age["state"] = DISABLED
            self.Entry_id["state"] = DISABLED
            self.Entry_mobile["state"] = DISABLED
            self.Entry_email["state"] = DISABLED
            self.Entry_home["state"] = DISABLED
            self.Entry_studyin["state"] = DISABLED
            self.Entry_pro["state"] = DISABLED
            self.Entry_emcon["state"] = DISABLED
            self.Entry_emtel["state"] = DISABLED
        elif self.flag == 2:
            self.Label_title.configure(text="==新建学生明细==")
        elif self.flag == 3:
            self.Label_title.configure(text="==修改学生明细==")
            # 填充数据
            self.load_student_detail()
            # 学号不允许修改
            self.Entry_sno["state"] = DISABLED

        self.load_student_detail()

    def colse_window(self):
        self.userinfo = 0
        # 关闭窗口
        self.destroy()

    def commit(self):
        self.userinfo = 1
        if self.flag == 3:  # 修改
            # 把当前界面中的数据存储在集合中
            temp_list = []
            if len(str(self.Entry_sno.get()).strip()) == 0:
                showinfo("系统消息", "学号不能为空！")
                return
            else:
                temp_list.append(str(self.Entry_sno.get()).strip())
                temp_list.append(str(self.Entry_name.get()).strip())
                if self.var_gender.get() == 1:
                    temp_list.append("男")
                else:
                    temp_list.append("女")
                temp_list.append(str(self.Entry_age.get()).strip())
                temp_list.append(str(self.Entry_mobile.get()).strip())
                temp_list.append(str(self.Entry_email.get()).strip())
                temp_list.append(str(self.Entry_home.get()).strip())
                temp_list.append(str(self.Entry_id.get()).strip())
                temp_list.append(str(self.Entry_studyin.get()).strip())
                temp_list.append(str(self.Entry_pro.get()).strip())
                temp_list.append(str(self.Entry_emcon.get()).strip())
                temp_list.append(str(self.Entry_emtel.get()).strip())
                # 遍历集合
                for index in range(len(self.all_student_list)):
                    if self.all_student_list[index][0] == self.current_student_list[0]:
                        self.all_student_list[index] = temp_list
                        # 提醒修改成功
                        showinfo("系统消息", "学生信息修改成功")
        elif self.flag == 2:  # 添加
            # 准备数据
            temp_list = []
            if len(str(self.Entry_sno.get()).strip()) == 0:
                showinfo("系统消息", "学号不能为空！")
            else:
                temp_list.append(str(self.Entry_sno.get()).strip())
                temp_list.append(str(self.Entry_name.get()).strip())
                if self.var_gender.get() == 1:
                    temp_list.append("男")
                else:
                    temp_list.append("女")
                temp_list.append(str(self.Entry_age.get()).strip())
                temp_list.append(str(self.Entry_mobile.get()).strip())
                temp_list.append(str(self.Entry_email.get()).strip())
                temp_list.append(str(self.Entry_home.get()).strip())
                temp_list.append(str(self.Entry_id.get()).strip())
                temp_list.append(str(self.Entry_studyin.get()).strip())
                temp_list.append(str(self.Entry_pro.get()).strip())
                temp_list.append(str(self.Entry_emcon.get()).strip())
                temp_list.append(str(self.Entry_emtel.get()).strip())
                # 添加到all_student_list
                self.all_student_list.append(temp_list)
                # 提醒添加成功
                showinfo("系统消息", "学生信息添加成功")

        # 关闭窗体
        self.destroy()


if __name__ == '__main__':
    this_window = DetailWindow()
    this_window.mainloop()
