
import turtle as tu
import random as ra
import tkinter as tk
import math
def Meteors():
    tu.setup(1.0, 1.0)
    tu.screensize(1.0, 1.0)    #设置画布大小
    tu.bgcolor('black')  #设置画布颜色
    tu.title("流星雨")
    t = tu.Pen()
    t.hideturtle()               #隐藏画笔
    # colors = ['skyblue', 'white', 'cyan', 'aqua']   #流星的颜色列表，蓝色
    colors = ['skyblue', 'white', 'cyan', 'aqua', 'gold', 'violet']   #流星的颜色列表，蓝色
    class Star():    #流星类
        def __init__(self):
            self.r = ra.randint(50,100)
            self.t = ra.randint(1,3)
            self.x = ra.randint(-2000,1000)   #流星的横坐标
            self.y = ra.randint(444, 999)  #流星的纵坐标
            self.speed = ra.randint(5,10)     #流星移动速度
            self.color = ra.choice(colors)    #流星的颜色
            self.outline = 1                 #流星的大小
        def star(self):                #画流星函数
            t.pensize(self.outline)    #流星的大小
            t.penup()                  #提笔
            t.goto(self.x,self.y)      #随机位置
            t.pendown()                #落笔
            t.color(self.color)
            t.begin_fill()
            t.fillcolor(self.color)
            t.setheading(-30)
            t.right(self.t)
            t.forward(self.r)
            t.left(self.t)
            t.circle(self.r*math.sin(math.radians(self.t)),180)
            t.left(self.t)
            t.forward(self.r)
            t.end_fill()
        def move(self):                    #流星移动函数
            if self.y >= -500:            #当流星还在画布中时
                self.y -= self.speed     #设置上下移动速度
                self.x += 2*self.speed   #设置左右移动速度
            else:
                self.r = ra.randint(50,100)
                self.t = ra.randint(1,3)
                self.x = ra.randint(-2000,1000)
                self.y = 444
                self.speed = ra.randint(5,10)
                self.color = ra.choice(colors)
                self.outline = 1
    Stars = []            #用列表保存所有流星
    for i in range(100):
        Stars.append(Star())
    while True:           #开始绘制
        tu.tracer(0)
        t.clear()
        for i in range(100):    #80个流星
            Stars[i].move()
            Stars[i].star()
        tu.update()
    tu.mainloop()

def love():
    root = tk.Tk()
    root.title('❤')
    root.resizable(0, 0)
    root.wm_attributes("-toolwindow", 1)
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    widths = 300
    heights = 100
    x = (screenwidth - widths) / 2
    y = (screenheight - heights) / 2
    root.geometry('%dx%d+%d+%d' % (widths, heights, x, y))  # 设置在屏幕中居中显示
    tk.Label(root, text='亲爱的，做我女朋友好吗？', width=37, font=('宋体', 12)).place(x=0, y=10)


    def OK():  # 同意按钮
        root.destroy()
        # 同意后显示相应的效果
        Meteors()

    def NO():  # 拒绝按钮，拒绝不会退出，必须同意才可以退出哦~
        tk.messagebox.showwarning('❤', '再给你一次机会！')


    def closeWindow():
        tk.messagebox.showwarning('❤', '逃避是没有用的哦')


    tk.Button(root, text='好哦', width=5, height=1, command=OK).place(x=80, y=50)
    tk.Button(root, text='不要', width=5, height=1, command=NO).place(x=160, y=50)
    root.protocol('WM_DELETE_WINDOW', closeWindow)  # 绑定退出事件
    root.mainloop()

if __name__ == "__main__":
    love()
