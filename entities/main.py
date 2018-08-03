import turtle as t
import time


pensize = 50 #画笔宽度


t.screensize(400, 300, "#66ccff")


a = t.window_width()
b = t.window_height()




#初始化画笔
t.pensize(pensize)
t.pencolor("#FF0000")
t.penup()
t.speed(10)
t.setx(-a/2)
t.sety(b/2-20)
#画笔宽度初始化
hight = b/2-20
count = int(round(hight / pensize))


#开始循环
t.begin_fill()
t.pendown()
for num in range(count*2+1):
    hight = hight - pensize
    t.forward(1000)
    t.right(90) #顺时针转
    t.sety(hight)   #设置Y轴位置
    t.left(-90) #逆时针转
t.end_fill()
t.penup()
#结束循环


print("循环结束")
#初始化画笔
t.pensize(pensize-40)
t.pencolor("#66CCFF")
t.speed(10)
t.setx(0+70)
t.sety(0)
t.penup()
#画笔宽度初始化


#画太阳花
t.pendown()
t.color("#66CCFF", "yellow")
t.speed(10)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(130)
t.end_fill()
#画太阳花结束