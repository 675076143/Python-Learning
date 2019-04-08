def que01(value):
    file = open("guest.txt", "w")
    file.write(value)
    file.close

def que02():    
    whileBool = True
    while whileBool:
        file = open("guest_book.txt", "a")
        file.write('\n'+input("请输入您的用户名：\n"))
        file.close

def que03():    
    whileBool = True
    while whileBool:
        file = open("reasons.txt", "a")
        file.write('\n'+input("为何喜欢编程?：\n"))
        file.close

que03()
