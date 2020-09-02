import PySimpleGUI as sg

layout = [
[sg.Text('Enter a Number')],
[sg.Input()],
[sg.OK()]
]

event,(number,) = sg.Window('Enter a number example').Layout(layout).Read()

sg.Popup(event,number)


##############下拉选项框########################

layout = [
[sg.Text('请选择你的性别',auto_size_text=True)],
[sg.InputCombo(['男','女','保密'],auto_size_text=True)],
[sg.OK('确认',auto_size_button=True)]
]

with sg.FlexForm('信息录入',auto_size_text=True) as form:
    button_name ,(gender,) = form.Layout(layout).Read()
    sg.Popup(button_name,gender)


##############滑动条#############################

layout = [
[sg.Text('选择你一个你喜欢的程度',auto_size_text=True)],
[sg.Slider(range=(1,500),default_value = 200,orientation ='h')],
[sg.OK('确认',auto_size_button=True)]
]

with sg.FlexForm('请滑动',auto_size_text=True) as form:
    button_name,(likelevel,) = form.Layout(layout).Read()
    sg.Popup(button_name,likelevel)


############################按钮################

layout = [
[sg.Text('你的学历是',auto_size_text=True)],
[sg.Radio('高中',group_id=1)],   #h 或者 v 表示水平或者垂直
[sg.Radio('本科',group_id=1)],
[sg.Radio('硕士',group_id=1)],
[sg.Radio('博士',group_id=1)],
[sg.OK('确认',auto_size_button=True)]
]

with sg.FlexForm('按钮',auto_size_text=True) as form:
    button_name,level = form.Layout(layout).Read()
    sg.Popup(button_name,level)


############################复选框####################

layout = [
[sg.Text('你的学历是',auto_size_text=True)],
[sg.Checkbox('游泳',default=True)],   #h 或者 v 表示水平或者垂直
[sg.Checkbox('篮球')],
[sg.Checkbox('足球')],
[sg.Checkbox('羽毛球')],
[sg.OK('确认',auto_size_button=True)]
]

with sg.FlexForm('复选框',auto_size_text=True) as form:
    button_name,choices = form.Layout(layout).Read()
    sg.Popup(button_name,choices)