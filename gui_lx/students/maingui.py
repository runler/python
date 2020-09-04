from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
import os


class MainWindow(Tk):
    def __init__(self, current_user, current_time):
        super().__init__()
        self.title("主窗体")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)
        self["bg"] = "royalblue"
        self.login_user = current_user
        self.login_time = current_time
        self.all_student_list = []
        self.query_result_list = []
        self.file_path = "Student.txt"
        self.load_file_student_info()
        # 加载gui
        self.setup_UI()
        self.load_treeview(self.all_student_list)

    def setup_UI(self):
        # 设定Style
        self.Style01 = Style()
        self.Style01.configure("left.TPanedwindow", background="navy")
        self.Style01.configure("right.TPanedwindow", background="skyblue")
        self.Style01.configure("TButton", width=10, font=("华文黑体", 15, "bold"))
        # Top_banner
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "stu_main_top_banner.png")
        self.Lable_image = Label(self, image=self.Login_image)
        self.Lable_image.pack()
        # 左边：按钮区域,创建一个容器
        self.Pane_left = PanedWindow(width=200, height=540, style="left.TPanedwindow")
        self.Pane_left.place(x=4, y=94)
        self.Pane_right = PanedWindow(width=685, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=210, y=94)
        # 添加左边按钮
        self.Button_add = Button(self.Pane_left, text="添加学生", style="TButton")
        self.Button_add.place(x=40, y=20)
        self.Button_update = Button(self.Pane_left, text="修改学生", style="TButton")
        self.Button_update.place(x=40, y=45)
        self.Button_delete = Button(self.Pane_left, text="删除学生", style="TButton")
        self.Button_delete.place(x=40, y=70)
        self.Button_modify = Button(self.Pane_left, text="更改密码", style="TButton")
        self.Button_modify.place(x=40, y=120)
        # 右边：查询、TreeView
        self.Pane_right = PanedWindow(width=725, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=170, y=94)
        # LabelFrame
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="学生信息查询", width=700, height=70)
        self.LabelFrame_query.place(x=10, y=10)
        # 添加控件
        self.Label_sno = Label(self.LabelFrame_query, text="学号：")
        self.Label_sno.place(x=5, y=13)
        self.var_sno = StringVar()
        self.Entry_sno = Entry(self.LabelFrame_query, width=8, textvariable=self.var_sno)
        self.Entry_sno.place(x=40, y=10)
        self.Label_name = Label(self.LabelFrame_query, text="姓名：")
        self.Label_name.place(x=125, y=13)
        self.var_name = StringVar()
        self.Entry_name = Entry(self.LabelFrame_query, width=8, textvariable=self.var_name)
        self.Entry_name.place(x=160, y=10)
        self.Label_mobile = Label(self.LabelFrame_query, text="电话：")
        self.Label_mobile.place(x=245, y=13)
        self.var_mobile = StringVar()
        self.Entry_mobile = Entry(self.LabelFrame_query, width=8, textvariable=self.var_mobile)
        self.Entry_mobile.place(x=280, y=10)
        self.Label_id = Label(self.LabelFrame_query, text="身份证：")
        self.Label_id.place(x=365, y=13)
        self.var_id = StringVar()
        self.Entry_id = Entry(self.LabelFrame_query, width=10, textvariable=self.var_id)
        self.Entry_id.place(x=420, y=10)
        self.Button_query = Button(self.LabelFrame_query, text="查询", width=4, command=self.get_query_result)
        self.Button_query.place(x=520, y=10)
        self.Button_all = Button(self.LabelFrame_query, text="显示全部", width=8, command=self.load_all_student)
        self.Button_all.place(x=590, y=10)
        # 添加TreeView控件
        self.Tree = Treeview(self.Pane_right, columns=("sno", "names",
                                                       "gender", "birthday", "mobile", "email", "address"),
                             show="headings", height=20)
        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("sno", width=100, anchor="center")
        self.Tree.column("names", width=80, anchor="center")
        self.Tree.column("gender", width=80, anchor="center")
        self.Tree.column("birthday", width=100, anchor="center")
        self.Tree.column("mobile", width=100, anchor="center")
        self.Tree.column("email", width=100, anchor="center")
        self.Tree.column("address", width=120, anchor="center")
        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("names", text="姓名")
        self.Tree.heading("gender", text="性别")
        self.Tree.heading("birthday", text="生日")
        self.Tree.heading("mobile", text="手机号码")
        self.Tree.heading("email", text="邮箱地址")
        self.Tree.heading("address", text="家庭住址")
        self.Tree.place(x=10, y=80)
        # 在Top_banner中通过标签将user信息展示出来
        self.Label_login_user = Label(self, text="当前用户:" + str(self.login_user).title()
                                                 + "\n登录时间:" + self.login_time)
        self.Label_login_user.place(x=650, y=40)

    def load_all_student(self):
        # 把所有查询条件文本框清空
        self.var_sno.set("")
        self.var_name.set("")
        self.var_mobile.set("")
        self.var_id.set("")
        # 加载所有的学生信息到treeview
        self.load_treeview(self.all_student_list)

    def get_query_result(self):
        # 把当前TreeView中的内容清空
        for i in self.Tree.get_children():
            self.Tree.delete(i)
        self.query_result_list.clear()  # 清空结果列表
        # 准备查询条件，去空格后往列表中添加数据
        query_condition = []
        query_condition.append(self.Entry_sno.get().strip())  # 采集学号信息
        query_condition.append(self.Entry_name.get().strip())  # 采集姓名信息
        query_condition.append(self.Entry_mobile.get().strip())  # 采集手机号码信息
        query_condition.append(self.Entry_id.get().strip())  # 采集身份证号码信息
        # 遍历List获取符合条件的学生信息
        for item in self.all_student_list:
            if query_condition[0] in item[0] and query_condition[1] in item[1] and \
                    query_condition[2] in item[4] and query_condition[3] in item[7]:
                # 满足条件的学生
                self.query_result_list.append(item)
        # 把结果加载的TreeView中
        self.load_treeview(self.query_result_list)

    def load_file_student_info(self):
        # 读取文件中的学生信息
        if not os.path.exists(self.file_path):
            showinfo("系统消息", "提供的文件名不存在！")
        else:
            try:
                with open(file=self.file_path, mode="r") as fd:
                    # 一次读一行
                    current_line = fd.readline()
                    while current_line:
                        temp_list = current_line.split(",")  # 长字符串分割层三个
                        self.all_student_list.append(temp_list)
                        # 读取下一行,读完了循环就结束了
                        current_line = fd.readline()
            except:
                showinfo("系统消息", "文件读取出现异常！")

    def load_treeview(self, current_list: list):

        # 判断是否有数据：
        if len(current_list) == 0:
            showinfo("系统消息", "没有数据加载")
        else:
            for index in range(len(current_list)):
                self.Tree.insert("", index, values=(current_list[index][0], current_list[index][1],
                                                    current_list[index][2], current_list[index][3],
                                                    current_list[index][4],
                                                    current_list[index][5], current_list[index][6]))


if __name__ == '__main__':
    this_main = MainWindow('test', '20200903')
    this_main.mainloop()
