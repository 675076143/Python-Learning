import math

def test01():    
    for i in range(11):
        if 1%5 == 0:
            for j in range(11):
                if j%5== 0:
                    if j == 10:
                        print("+")
                    else:
                        print("+",end="")
                else:
                    print("-",end="")
        else:
            for k in range(11):
                if k%5 == 0:
                    if k == 10:
                        print("|")
                    else:
                        print("|",end="")
                else:
                    print(" ",end="")

                    

def que01():#打印田字格
    for i in range(21):       
        if i %5 == 0:
            print("+ - - - - + - - - - + - - - - + - - - - +")
        else:
            print("1         1         1         1         1")

def que02(*n):#multi()函数
    result = 1
    for i in n:
        result = result * i
    print(result)

def que03(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:    #对2直到自身的开方取模
            print("{}不是素数".format(n))
            return False;
    print("{}是素数".format(n))
    return True;
que03(10)
que03(7)
    
