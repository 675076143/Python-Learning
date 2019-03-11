import turtle

def draw_square(times,size):    #画正方形螺旋线
    for i in range(times):
        turtle.right(90)
        turtle.fd(size)
        size+=10

def draw_diebian(times,size):   #画叠边型
    for i in range(times):
        turtle.right(80)
        turtle.fd(size)


#draw_square(100,10)
draw_diebian(100,100)
