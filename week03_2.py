import random

def que01():
    inputOrigin = input("请输入一行字符：")
    inputList = list(inputOrigin)   #将输入的字符存储在list中
    countDigit = 0  #统计数字
    countAlpha = 0  #统计字母
    countSpace = 0  #统计空格
    countSp = 0     #统计特殊字符
    for i in range(len(inputList)):  #遍历List
        if(inputList[i].isdigit()):   #判断是否为数字
            countDigit += 1
        elif(inputList[i].isalpha()):    #判断是否为字母
            countAlpha += 1
        elif(inputList[i]==" "):  #判断是否为空格
            countSpace += 1  
        else:  #判断是否为特殊字符
            countSp += 1
    print("数字个数={};字母个数={};空格个数={};特殊字符个数={};".format(countDigit,countAlpha,countSpace,countSp))

def que02():    #猜数游戏续
    try:
        num = random.randint(0,100)
        print(num)
        guess = input("请输入您猜测的数字：")
        if (guess.isdigit()):
            if(eval(guess) == num):
                print("恭喜您猜中了！")
            else:
                print("猜测失败")
        else:
            print("请输入整数！")
    except:
        print("Error！")
    que02()

def que03():    #羊车门问题
    resultOrigin = 0    #选手更换门
    resultChange = 0    #选手不更换门
    times = 1000000     #抽奖次数
    for i in range(times):
        if(random.randint(1,3)==1):  #如果random抽到1，代表抽到车了
            resultOrigin += 1
    for i in range(times):
        if(random.randint(1,3)==1):  #如果random抽到1，代表抽到车了
            resultChange += 1
        else:  #如果random没抽到1，代表剩下两扇门中必有一辆车
            if(random.randint(1,2)==1):
                resultChange += 1        
    print("选手不更换门的情况：在{}次数中,抽到了{}次,概率约为{}".format(times,resultOrigin,resultOrigin/times))
    print("选手更换门的情况：在{}次数中,抽到了{}次,概率约为{}".format(times,resultChange,resultChange/times))
            
    
que03()
