dictUsers = {"Admin":"Admin","Robin":"123456"}
dictStudents = {"1706105308":["黄旭震","19"],"1706105300":["Admin","20"]}

def int():
    print("1.登录")
    print("2.注册")

def int2():
    print("0.显示所有")
    print("1.查询")
    print("2.新增")
    print("3.修改")
    print("4.删除")


def select(a):
    if a == '1':
        login(input("请输入用户名\n"),input("请输入密码\n"))
    elif a == '2':
        register(input("请输入用户名\n"),input("请输入密码\n"))
    else:
        print("error")

def select2(a):
    if a == '0':
        print(dictStudents)
        select2(input("请输入您的选择：\n"))
    elif a == '1':
        query(input("请输入学号：\n"))
        select2(input("请输入您的选择：\n"))
    elif a == '2':
        insert(input("请输入学号：\n"),input("请输入姓名：\n"),input("请输入年龄：\n"))
        select2(input("请输入您的选择：\n"))
    elif a == '3':
        update(input("请输入学号：\n"), input("请输入姓名：\n"), input("请输入年龄：\n"))
        select2(input("请输入您的选择：\n"))
    elif a == '4':
        delete(input("请输入学号：\n"))
        select2(input("请输入您的选择：\n"))
    else:
        print("error")
        select2(input("请输入您的选择：\n"))

def login(a,b):
    if a in dictUsers.keys():
        if b==dictUsers[a]:
            print("登陆成功！")
            int2()
            select2(input("请输入您的选择：\n"))
    else:
        print("请检查您的用户名和密码")
        login(input("请输入用户名\n"),input("请输入密码\n"))

def register(a,b):
    if a in dictUsers.keys():
        print("用户名已存在！")

    else:
        dictUsers[a] = b
        print("注册成功！为您跳转到登录...")
        login(input("请输入用户名\n"), input("请输入密码\n"))

def query(a):
    print(dictStudents[a])

def insert(a,b,c):
    info = [b,c]
    if a in dictStudents.keys():
        print("该学号已存在！")
    else:
        dictStudents[a] = info

def update(a,b,c):
    info = [b, c]
    if a in dictStudents.keys():
        dictStudents[a] = info
    else:
        print("该学号不存在！")

def delete(a):
    if a in dictStudents.keys():
        dictStudents.pop(a)
    else:
        print("该学号不存在")
#int()
#select(input("请输入您的操作："))

class User:
    def __init__(self,userName,userPassword):
        self.userName = userName
        self.userPassword = userPassword
    def detail(self):
        print(self.userName)
        print(self.userPassword)
class Users:
    def __init__(self):
        self.users = []
    def insert(self):
        user = User(userName="Admin", userPassword="Admin")
        self.users.append(user)
        user = User(userName="Admin2", userPassword="Admin")
        self.users.append(user)
        print(self.users[0].userName)
        print("测试")

    def login(self):
        for i in self.users:
            print(self.users.index(i))
        #print("login")
users = Users()
users.login()
