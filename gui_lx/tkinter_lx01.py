import tkinter as tk  # 给tkinter重命名为tk
'''
来源于 头条 小雨编程
'''
# root = tk.Tk()  # 新建一个窗体
# root.mainloop()  # 展示窗体

root = tk.Tk()  # 新建一个窗体

# 为窗体设置一个标题
root.title("第一个tkinter窗体title")
# 指定窗体的大小，这里的乘号是小写字母x
root.geometry("400x300")
# 添加一个标签
Label01 = tk.Label(root, text="第一个label标签")
# 将标签布局到窗体上
Label01.pack()
# 添加一个按钮,可以在创建按钮的同时在句尾调用pack语句进行布局
Button01 = tk.Button(root, text="确定Button").pack()
# 添加一个单行文本框
Entry01 = tk.Entry(root).pack()

root.mainloop()  # 展示窗体
