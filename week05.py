def que01():
    ls = [2,5,7,1,6]
    ls.sort()
    print(ls)

def que02():
    ls1=[30,1,2,0]
    ls2=[1,21,133]
    print(ls1)
    print(ls2)    
    print("ls1中比ls2多了{}".format(list(set(ls1).difference(set(ls2)))))
    print("ls2中比ls1多了{}".format(list(set(ls2).difference(set(ls1)))))

def que03():
    ls1=[1,43]
    ls2=ls1
    print("ls2的初始值为：{}".format(ls2))
    print("ls1的初始值为：{}".format(ls1))
    ls1[0]=22
    print("ls2的当前值为：{}".format(ls2))
    print("ls1的当前值为：{}".format(ls1))
    print(ls2)

def que04():
    ls=[[2,3,7],[[3,5],25],[0,9]]
    print("len(ls)={}".format(len(ls)))

from math import sqrt
def getNum():
    nums =[]
    iNumStr = input("请输入数字（直接输入回车退出）：")
    while iNumStr !="":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（直接输入回车退出）：")
    return nums
def mean(numbers):
    s=0.0
    for num in numbers:
        s = s+num
    return s/len(numbers)
def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev +(num-mean)**2
    return sqrt(sdev/(len(numbers)-1))
def median(numbers):    #计算中位数
    numbers.sort(reverse=True)  #改写21行
    size = len(numbers)
    if size % 2 ==0:
        med =(numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med
def FindMax(numbers):
    maxValue = max(numbers)
    return maxValue
def FindMin(numbers):
    minValue = min(numbers)
    return minValue
n = getNum()
m = mean(n)
print("平均值：{},方差：{:.2},中位数：{}.".format(m,dev(n,m),median(n)))
print("最大值：{}，最小值：{}".format(FindMax(n),FindMin(n)))

    
    
