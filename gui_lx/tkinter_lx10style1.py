'''
Style属性
增强的ttk包里没法用tkinter的传统属性进行设置比如bg和fg，我们需要通过style对象来对其设置；注意：我们对实例化对象style01进行配置,
style01.configure("TLabel",font = ("华文黑体",18),background = "green",foreground = "blue")
第一个参数不是对象的名称,而是对象的某一类，其名称是有规定的，不是随便取的，由于这里是对Label 的style进行命令，
所以我们只能命名成TLabel，具体的组件与名称的对应关系如下：
疑问：
如果此时创建一个Label02对象它的style属性没有绑定style01对象，但是它的属性依然是style01对象里定义的特征，这是怎么回事呢？
解答：
其实只要在配置style的时候，填写标准的Stylename，后面无论某个控件是否绑定，Stylename 对应的控件都会生效；
'''
from tkinter import Tk
from tkinter.ttk import Style, Label

root = Tk()
root.title("style属性")
root.geometry("300x200")
# 实例化一个style对象style01
style01 = Style()
# 对style01进行配置,Stylename属性设置为标准的TLable
style01.configure("TLabel", font=("华文黑体", 18), background="green", foreground="blue")
# 把Label01控件绑定给style01对象
Label01 = Label(root, text="用户名", style="TLabel")
Label01.pack(padx=10, pady=10)
Label02 = Label(root, text="密码")
Label02.pack(padx=10, pady=10)
# 展示窗体
root.mainloop()
