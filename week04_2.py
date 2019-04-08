import turtle
import datetime

def drawLine(draw):
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def que01():#倒计时
    for i in range(10): #循环绘画9-1
        turtle.speed(1)
        turtle.fd(-60)
        turtle.clear()
        drawDigit(10-i)

def que02(num):#绘制带小数点的7段数码管
    turtle.speed(0)
    for i in num:       
        if i == '.': #遍历字符串，如果为"."绘画小数点
            turtle.right(90)
            turtle.fd(50)
            turtle.write('.',font=(18))
            turtle.right(180)
            turtle.fd(50)
            turtle.right(90)
            turtle.fd(15)
        else:
            drawDigit(eval(i))
            
def que03(): #输出生日的十种日期格式
    print(datetime.date(1999,6,16).strftime('%Y年%m月%d日'))
    print(datetime.date(1999,6,16).strftime('%Y.%m.%d'))
    print(datetime.date(1999,6,16).strftime('%Y:%m:%d'))
    print(datetime.date(1999,6,16).strftime('%Y%m%d'))
    print(datetime.date(1999,6,16).strftime('%Y-%m-%d'))
    print(datetime.date(1999,6,16).strftime('%Y/%m/%d'))
    print(datetime.date(1999,6,16).strftime('%Yy%mm%dd'))
    print(datetime.date(1999,6,16).strftime('%Y|%m|%d'))
    print(datetime.date(1999,6,16).strftime('%Y  %m  %d'))
    print(datetime.date(1999,6,16).strftime('%Y·%m·%d'))

    

a=0
def que04(n,A,B,C): #汉罗塔
    if(n == 1):
        global a
        a+=1
        print('第{}次移动：{}移动到{}'.format(a,A,C))
        return
    que04(n-1,A,C,B)
    a+=1
    print('第{}次移动：{}移动到{}'.format(a,A,C))
    que04(n-1,B,A,C)
    

que04(eval(input("请输入汉罗塔的层数：")),'A','B','C')
print("finished")


import calendar

def que05(years,month): #获取所在月份的天数    
    num = calendar.monthrange(years,month)
    print("{}年{}月有{}天".format(years,month,num[1]))

#que05(eval(input("请输入要查询的年份: ")),eval(input("请输入要查询的月份: ")))

