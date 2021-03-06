#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 03, 2020 02:18:08 PM CST  platform: Windows NT


import sys
import pymysql
import updategrade
import matplotlib.pyplot as plt
import matplotlib
global f,a1
f = 0

try:
    import Tkinter as tk
    import Tkinter.messagebox as v
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as v
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def mat(n_list,z_list):
    # 设置中文字体和负号正常显示
    a2 = w.TCombobox1.get()
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    label_list = n_list    # 横坐标刻度显示值
    num_list1 = z_list     # 纵坐标值1
    print(num_list1)
    print(type(num_list1))
    #num_list2 = [15, 30, 40, 20,20]      # 纵坐标值2
    x1 = range(len(num_list1))
    """
    绘制条形图
    left:长条形中点横坐标
    height:长条形高度
    width:长条形宽度，默认值0.8
    label:为后面设置legend准备
    """
    rects1 = plt.bar(x=x1, height=num_list1, width=0.4, alpha=0.5, color='red')
    #rects2 = plt.bar(x=[i + 0.4 for i in x1], height=num_list2, width=0.4, color='green', label="二部门")
    plt.ylim(0, 100)     # y轴取值范围
    plt.ylabel("学生平均成绩")
    """
    设置x轴刻度显示值
    参数一：中点坐标
    参数二：显示值
    """
    plt.xticks([index + 0.2 for index in x1], label_list)
    plt.xlabel("姓名")
    plt.title(a2+"学生平均成绩统计图")
    plt.legend()     # 设置题注
    # 编辑文本
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height-2, str(height), ha="center", va="bottom")
    # for rect in rects2:
    #     height = rect.get_height()
    #     plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
    plt.show()

def set_Tk_var():
    global combobox
    combobox = tk.StringVar()

def adds():
    import addgrade
    addgrade.vp_start_gui()
    sys.stdout.flush()

def delButton():
    x=w.Scrolledtreeview1.get_children()
    for item in x:
        w.Scrolledtreeview1.delete(item)

def allfind():
    global f
    f = 0
    delButton()
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    cur.execute('select student.*,class.cname,grade.grade FROM student,class,'\
                'grade where student.sno = grade.sno and class.cno = grade.cno')
    r = cur.fetchall()
    i = 0

    for r1 in r:
        w.Scrolledtreeview1.insert('', i, values=(r1[0], r1[1], r1[2],r1[3],r1[4],r1[5],r1[6],r1[7]))
        i += 1

    sys.stdout.flush()

def p(event):#bind函数
    cur = w.Scrolledtreeview1.focus()
    return w.Scrolledtreeview1.item(cur)

def deletes():
    global f
    c = p('')
    w.Scrolledtreeview1.bind('<ButtonRelease-1>', p)
    if c.get('values') != '':
        sno = c.get('values')[0]
        conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
        cur = conn.cursor()
        cur.execute('DELETE FROM student WHERE sno = %s', sno)
        conn.commit()
        v.showinfo('suessful', '删除成功')
    if f == 0:
        allfind()
    elif f == 2:
        snofind()
    elif f == 1:
        namefind()
    sys.stdout.flush()

def mat1():
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    cur.execute('select cno from grade GROUP BY cno')
    r = cur.fetchall()
    k = []
    for r1 in r:
        r2 = r1[0]
        k.append(r2)
    print(k)
    cur.execute('select cname from class GROUP BY cno')
    r = cur.fetchall()
    k1 = []
    for r1 in r:
        r2 = r1[0]
        k1.append(r2)
    print(k1)
    k3 = []
    for i in range(0,len(k)):
        cur.execute('select count(*) from grade where grade >= 60 and cno = %s',k[i])
        r = cur.fetchone()
        k3.append(int(r[0]))
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    label_list = k1   # 横坐标刻度显示值
    num_list1 = k3   # 纵坐标值1
    print(num_list1)
    print(type(num_list1))
    #num_list2 = [15, 30, 40, 20,20]      # 纵坐标值2
    x1 = range(len(num_list1))
    """
    绘制条形图
    left:长条形中点横坐标
    height:长条形高度
    width:长条形宽度，默认值0.8
    label:为后面设置legend准备
    """
    rects1 = plt.bar(x=x1, height=num_list1, width=0.4, alpha=0.5, color='red')
    #rects2 = plt.bar(x=[i + 0.4 for i in x1], height=num_list2, width=0.4, color='green', label="二部门")
    plt.ylim(0, 50)     # y轴取值范围
    plt.ylabel("及格人数")
    """
    设置x轴刻度显示值
    参数一：中点坐标
    参数二：显示值
    """
    plt.xticks([index + 0.2 for index in x1], label_list)
    plt.xlabel("课程名称")
    plt.title("各科及格人数统计图")
    plt.legend()     # 设置题注
    # 编辑文本
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height-2, str(height), ha="center", va="bottom")
    # for rect in rects2:
    #     height = rect.get_height()
    #     plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
    plt.show()
    sys.stdout.flush()

def namefind():
    global f
    f = 1
    delButton()
    sname = w.fname.get()
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    cur.execute('select student.*,class.cname,grade.grade FROM student,class'\
                ',grade where student.sno = grade.sno and class.cno = grade.cno and sname = %s',sname)
    r = cur.fetchall()
    i = 0
    if r != ():
        for r1 in r:
            w.Scrolledtreeview1.insert('', i, values=(r1[0], r1[1], r1[2],r1[3],r1[4],r1[5],r1[6],r1[7]))
            i += 1
    else:
        v.showerror('error',sname+"信息不存在，请检查后重新输入")
    sys.stdout.flush()

def snofind():
    global f
    f = 2
    delButton()
    sno = w.fsno.get()
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    cur.execute('select student.*,class.cname,grade.grade FROM student,class'\
                ',grade where student.sno = grade.sno and class.cno = grade.cno and student.sno = %s', sno)
    r = cur.fetchall()
    i = 0
    if r != ():
        for r1 in r:
            w.Scrolledtreeview1.insert('', i, values=(r1[0], r1[1], r1[2],r1[3],r1[4],r1[5],r1[6],r1[7]))
            i += 1
    else:
        v.showerror('error', sno + '不存在，请检查后重新输入')
    sys.stdout.flush()

def updates():
    c = p('')
    w.Scrolledtreeview1.bind('<ButtonRelease-1>',p)
    if c.get('values') != '':
        sno = c.get('values')[0]
        cname = c.get('values')[6]
        grade = c.get('values')[7]
        conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
        cur = conn.cursor()
        cur.execute('select cno from class where cname = %s', cname)
        r = cur.fetchone()
        cno = r[0]
        updategrade.vp_start_gui(sno,cno,grade)
    sys.stdout.flush()


def delButton1():
    x = w.Scrolledtreeview1_1.get_children()
    for item in x:
        w.Scrolledtreeview1_1.delete(item)

def xspm():
    delButton1()
    a2 = w.TCombobox1.get()
    print(a2)
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    cur.execute('select grade.sno,student.sname,student.sex,student.sage,student.dept,student.class,avg(grade)'\
                ' from  student NATURAL JOIN grade GROUP BY grade.sno HAVING grade.sno in'\
                ' (select sno from student where dept = %s)  ORDER BY avg(grade) desc',a2)
    r = cur.fetchall()
    i = 0
    z_list = []
    n_list = []
    if r != ():
        for r1 in r:
            zf = r1[6]
            zf = float('%.2f' % zf)
            w.Scrolledtreeview1_1.insert('', i, values=(r1[0], r1[1], r1[2],r1[3],r1[4],r1[5],zf))
            i += 1
            n_list.append(r1[1])
            z_list.append(zf)
    mat(n_list,z_list)
    sys.stdout.flush()

def init(top, gui, a,*args, **kwargs):
    global w, top_level, root,a1
    a1 = a
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import querygrade
    querygrade.vp_start_gui()




