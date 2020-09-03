'''
Style属性
拓展：如果只想对某类中的某些控件生效，那么就必须要使用custom.Stylename格式来进行命名；如我创建的style01的Stylename名称是username.TLabel，
这里的username是自定义字段，那么后面的Label控件如果没有指定style是username.TLabel就不会具有style01的属性
这样就能使具体某一个组件生效，这样就能做到既能控制全局保持整体的统一，又能对具体某一类或者某一个特别对待，这种机制就很棒！
好啦，关于Tkinter的基础知识点就介绍到这里啦！如果觉得文章还不错的话，欢迎点赞关注，感谢你的支持^-^
'''
from tkinter import Tk
from tkinter.ttk import Style, Label

root = Tk()
root.title("style属性")
root.geometry("300x200")
# 实例化一个style对象style01
style01 = Style()
# 对style01进行配置,Stylename属性设置为username.TLable
style01.configure("username.TLabel", font=("华文黑体", 18), background="green", foreground="blue")
# 把Label01控件绑定给style01对象
Label01 = Label(root, text="用户名", style="username.TLabel")
Label01.pack(padx=10, pady=10)
Label02 = Label(root, text="密码")
Label02.pack(padx=10, pady=10)
# 展示窗体
root.mainloop()
