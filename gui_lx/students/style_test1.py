from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("style属性")
root.geometry("300x200")
# 实例化一个style对象style01
style01 = Style()
# 对style01进行配置,Stylename属性设置为password.TLable
style01.configure("password.TLabel", font=("华文黑体", 18), background="green", foreground="blue")
# 把Label01控件绑定给style01对象
Label01 = Label(root, text="用户名", style="password.TLabel")
Label01.pack(padx=10, pady=10)
Label02 = Label(root, text="密码")
Label02.pack(padx=10, pady=10)
# 展示窗体
root.mainloop()
