# RadioButton 单选框
from tkinter import *

# from tkinter.ttk import *
# radiobutton --- 单选框----多个值中只能选一个
root = Tk()
root.title("RadioButton组件")
root.geometry("400x100")


def sel_gender():
    if gender_check.get() == 0:
        Label_select_gender["text"] = "女"
    else:
        Label_select_gender["text"] = "男"


def sel_education():
    Label_select_education["text"] = education_list[int(education_check.get())]


# 性别单选
Label_gender = Label(root, text="性别:")
Label_gender.grid(row=0, column=0, padx=5, pady=5)
gender_check = IntVar()
# 用哪个变量接收它是否被选中，variable，绑定的值是同一个表示一组,variable通过get方法能获得value的值
# 最终选中后取什么值： value，同一组radiobutton中value的值最好是不同的
# 性别的单选
radio_boy = Radiobutton(root, text="男", variable=gender_check, value=1, command=sel_gender)
radio_boy.grid(row=0, column=1, padx=5, pady=5)
radio_boy = Radiobutton(root, text="女", variable=gender_check, value=0, command=sel_gender)
radio_boy.grid(row=0, column=2, padx=5, pady=5)
# 学历
education_list = ["高中", "专科", "本科", "硕士", "博士"]
Label_education = Label(root, text="学历:")
Label_education.grid(row=1, column=0, padx=5, pady=5)
education_check = IntVar()
for i in range(0, len(education_list)):
    radio = Radiobutton(root, text=education_list[i], variable=education_check, value=i, command=sel_education)
    radio.grid(row=1, column=i + 1, padx=5, pady=5)
Label01 = Label(root, text="所选的值为:")
Label01.grid(row=2, column=0)
Label_select_gender = Label(root, text="")
Label_select_gender.grid(row=2, column=1)
Label_select_education = Label(root, text="")
Label_select_education.grid(row=2, column=2)
# 展示控件
root.mainloop()
