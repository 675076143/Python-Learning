import math
def que01():    #第一题
    result = 0
    times = eval(input("请输入您要计算的次数："))
    for i in range(times+1):
        if(i%2 == 1):
            result += i
            print("第{}次计算的结果={}".format(i,result))
        else:
            result -= i
            print("第{}次计算的结果={}".format(i,result))

def que02():    #第二题3位水仙花数字
    for num in range(100,1000):
        a = (num%10)    #个位
        b = (int(num/100))  #百位
        c = int((num-b*100)/10)  #十位      
        if num == a**3+b**3+c**3:
            print(num,end=",")
          
def que03():    #第三题用户登录的三次机会
    failetimes = 2    #提供两次失败的次数
    while failetimes >= 0:
        userName = input("请输入用户名：")
        password = input("请输入密码：")
        if(userName=="Kate" and password=="666666"):
            print("登录成功")
            break
        elif(userName=="" or password==""): #非空验证
            print("用户名或密码为空！")
        else:
            if failetimes !=0:
                print("登录失败，请你还剩余{}次机会！".format(failetimes))
                failetimes -=1
            else:
                print("您的次数耗尽，程序终止！")                  

que01()
