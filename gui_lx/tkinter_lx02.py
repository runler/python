import tkinter as tk

'''
    tkinter常用的控件属性
（1）定义控件的名称使用参数text，传入的字符串值即为控件的名称；
（2）定义控件高度使用参数hight，宽度使用参数width，传入的值为整形数值；
（3）定义控件在空间中的位置，使用参数anchor，传入的字符参数为e、s、w、n以地图的东南西北来定义为右下左上，也可以同时设置左下sw、左上nw、右下se、右上ne；
（4）定义控件的背景色，使用参数bg，前景色使用参数fg，传入字符值可以直接是对应颜色的英文名称；
（5）设置布局在pack()函数里，使用参数side，传入的值为常量tk.LEFT或者tk.RIGHT，表示从左到右或者从右到左布局
（6）创建图片控件时，图片控件的文件源使用参数file，传入的字符值为为文件路径，在控件中使用图片则使用参数image，传入的值为图片控件变量；
（7）设置整个窗体的尺寸，使用参数geometry，传入的值为字符值，注意乘号用小写字母x代替；如果要设置长400宽300的窗体则使用语句geometry = "400x300"
（8）设置控件与边界的距离在pack函数里使用参数padx，设置左右距离；使用pady设置上下距离。
'''
# 新建一个窗体名称:root
root = tk.Tk()
# 为窗体添加一个标题
root.title("第二个Python窗体")
# 新建标签
Label01 = tk.Label(root, text="第一个Label标签", anchor="sw").pack(side=tk.LEFT)
photo = tk.PhotoImage(file="./img/yusheng.png")
imageLable01 = tk.Label(root, image=photo).pack(side=tk.LEFT)
Label02 = tk.Label(root, text="第二个Label标签", bg="blue", fg="white", font=("华文宋体", 20)).pack()
Label03 = tk.Label(root, text="第三个Label标签", ).pack()
Label04 = tk.Label(root, text="第四个Label标签").pack()
Label05 = tk.Label(root, text="第五个Label标签").pack()
Button01 = tk.Button(root, text="确定").pack()
# 显示
root.mainloop()
