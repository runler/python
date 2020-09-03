import os
from datetime import datetime
from tkinter import *
from tkinter.ttk import *


class IDCheckGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("身份证信息校验系统")
        self.geometry("900x510+400+200")
        self.resizable(0, 0)
        self["bg"] = "whitesmoke"
        self.setup_UI()

    def setup_UI(self):
        self.style01 = Style()
        self.style01.configure("input.TLabel", font=("微软雅黑", 20, "bold"))
        self.style01.configure("TLabel", font=("微软雅黑", 20, "bold"), foreground="navy")
        self.style01.configure("TButton", font=("微软雅黑", 20, "bold"), background="lightblue")
        # 图片
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "id2.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.place(x=25, y=25)
        # 输入信息
        self.Label_id_input = Label(self, text="请输入身份证号码:", style="input.TLabel")
        self.Label_id_input.place(x=400, y=20)
        self.var_input = StringVar()
        self.Entry_id_input = Entry(self, textvariable=self.var_input, width=20, font=("微软雅黑", 18, "bold"))
        self.Entry_id_input.place(x=400, y=70)
        self.Button_id_input = Button(self, text="校验", command=self.get_info)
        self.Button_id_input.place(x=700, y=70)
        # 具体信息
        self.Label_is_exsit = Label(self, text="是否有效：")
        self.Label_is_exsit.place(x=400, y=170)
        self.var_enable = StringVar()
        self.Entry_is_exsit = Entry(self, state=DISABLED, textvariable=self.var_enable, width=10,
                                    font=("微软雅黑", 18, "bold"))
        self.Entry_is_exsit.place(x=530, y=165)
        self.Label_is_gender = Label(self, text="性       别：")
        self.Label_is_gender.place(x=400, y=220)
        self.var_gender = StringVar()
        self.Entry_is_gender = Entry(self, state=DISABLED, textvariable=self.var_gender, width=10,
                                     font=("微软雅黑", 18, "bold"))
        self.Entry_is_gender.place(x=530, y=215)
        self.Label_is_birthday = Label(self, text="出生日期：")
        self.Label_is_birthday.place(x=400, y=270)
        self.var_birthday = StringVar()
        self.Entry_is_birthday = Entry(self, state=DISABLED, textvariable=self.var_birthday, width=18,
                                       font=("微软雅黑", 19, "bold"))
        self.Entry_is_birthday.place(x=530, y=265)
        self.Label_is_area = Label(self, text="所  在  地：")
        self.Label_is_area.place(x=400, y=320)
        self.var_area = StringVar()
        self.Entry_is_area = Entry(self, state=DISABLED, textvariable=self.var_area, width=18,
                                   font=("微软雅黑", 19, "bold"))
        self.Entry_is_area.place(x=530, y=315)
        self.Button_close = Button(self, text="关闭", command=self.close_window)
        self.Button_close.place(x=650, y=450)

    def close_window(self):
        self.destroy()

    def get_info(self):
        id_number = self.var_input.get()
        if len(id_number) == 18:
            check_id = IdCheck(id_number)
            if check_id.is_true_id_number == 0 or len(check_id.birthday) == 0 or len(check_id.area_name) == 0:
                self.var_enable.set("无效!")
            else:
                self.var_enable.set("有效")
                self.var_gender.set(check_id.gender)
                self.var_birthday.set(check_id.birthday)
                self.var_area.set(check_id.area_name)
        else:
            self.var_enable.set("无效")
            self.var_gender.set("")
            self.var_birthday.set("")
            self.var_area.set("")
            # showinfo("系统消息", "输入的身份证号码不满18位，请重新输入！")
            self.var_area.set("输入的身份证号码不满18位，请重新输入！")


class IdCheck():
    def __init__(self, id):
        self.id_number = id
        self.is_true_id_number = 1
        self.birthday = ''
        self.gender = ''
        self.area_name = '上海'

    def get_id_list(self):
        # 地区码
        self.id_list.append(self.id_number[:6])
        # 出生日期码
        self.id_list.append(self.id_number[6:14])
        # 顺序码
        self.id_list.append(self.id_number[14:17])
        # 校验码
        self.id_list.append(self.id_number[17:])
        return self.id_list

    def get_check_number(self):
        """
        取出校验码
        :return: 返回的校验码
        """
        number = self.id_number[:17]
        xi_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 每个位上乘的系数列表
        check_number = ["1", "0", "x", "9", "8", "7", "6", "5", "4", "3", "2"]  # 返回的校验码列表
        sum_of_number = 0
        for index in range(len(number)):
            sum_of_number += int(number[index]) * xi_list[index]
        # 余数
        yu_number = sum_of_number % 11
        return check_number[yu_number]

    def validate_check_number(self):
        if self.get_check_number() == self.id_list[3]:
            self.is_true_id_number = 1

    def validate_birthday(self):
        date_from = datetime(year=1900, month=1, day=1)
        date_to = datetime.today()
        id_birthday = datetime(year=int(self.id_number[6:10]), month=int(self.id_number[10:12]),
                               day=int(self.id_number[12:14]))
        if id_birthday > date_from and id_birthday < date_to:
            self.birthday = self.id_number[6:10] + "年" + self.id_number[10:12] + "月" + self.id_number[12:14] + "日"

    def import_area_id(self):
        print('area')
        pass
        try:
            with open(file=self.file_path, mode="r", encoding="UTF-8") as fd:
                current_line = fd.readline()
                while current_line:
                    current_area_list = current_line.split(",")
                    if len(current_area_list[0]) == 6:
                        self.area_list.append(current_area_list)
                        current_line = fd.readline()
        except:
            # showinfo("系统提醒", "地区文件读取失败")
            self.var_area.set("地区文件读取失败")

    def validate_area_id(self):
        for index in range(len(self.area_list)):
            if self.area_list[index][0] == self.id_list[0]:
                self.area_name = self.area_list[index][1]
                break

    def get_gender(self):
        if int(self.id_list[2]) % 2 == 0:
            self.gender = "女"
        else:
            self.gender = "男"


if __name__ == '__main__':
    check_gui = IDCheckGUI()
    check_gui.mainloop()
