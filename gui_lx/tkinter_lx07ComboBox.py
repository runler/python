from tkinter import Label, StringVar, Tk
from tkinter.ttk import Combobox

# ComboBox 控件 --- 下拉框单选

root = Tk()
root.title("ComboBox控件")
root.geometry("400x100")


# 做下拉选择的时候定义函数一定要使用可变长参数
def sel_gender(*args):
    Label_select_gender["text"] = combo_gender.get()


def sel_education(*args):
    Label_select_education["text"] = combo_education.get()


# 性别单选
Label_gender = Label(root, text="性别")
Label_gender.grid(row=0, column=0, padx=5, pady=5)
gender = StringVar()
combo_gender = Combobox(root, textvariable=gender)   #
combo_gender["values"] = ["男", "女"]  # 下拉列表填充
combo_gender["state"] = "readonly"  # 只允许读，如果没有这个参数，输入框可以输入值
combo_gender.current(0)  # 默认情况下选择的值的索引
combo_gender.grid(row=0, column=1)
# 学历单选
education_list = ["高中", "专科", "本科", "硕士", "博士"]
Label_education = Label(root, text="学历:")
Label_education.grid(row=1, column=0)
education = StringVar()
combo_education = Combobox(root, textvariable=education, values=education_list)  #
combo_education["state"] = "readonly"
combo_education.current(0)
combo_education.grid(row=1, column=1)
# 绑定选择性别的事件
combo_gender.bind("<<ComboboxSelected>>", sel_gender)
# 绑定选择学历的事件
combo_education.bind("<<ComboboxSelected>>", sel_education)
# 获取结果：
Label01 = Label(root, text="所选的值为:")
Label01.grid(row=2, column=0)
Label_select_gender = Label(root, text="")
Label_select_gender.grid(row=2, column=1, )
Label_select_education = Label(root, text="")
Label_select_education.grid(row=2, column=2, sticky="e")
# 窗体展示
root.mainloop()
