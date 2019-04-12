class Student:  #学生对象，包含学号 姓名 和年龄
    def __init__(self, stuNo, stuName, stuAge):
        self.stuNo = stuNo
        self.stuName = stuName
        self.stuAge = stuAge
    def detail(self):
        print(self.stuNo)
        print(self.stuName)
        print(self.stuAge)

class Students:
    def __init__(self):
        self.students = []  #初始化一个列表students存放student

    def init(self): #初始化的方法
        student = Student(stuNo="1706105308", stuName="黄旭震", stuAge="19")
        self.students.append(student)   #添加一条学号为1706105308，姓名为黄旭震，年龄为19的数据
        student = Student(stuNo="1706105300", stuName="Robin", stuAge="20")
        self.students.append(student)   #添加一条学号为1706105300，姓名为Robin，年龄为20的数据

    def show(self): #打印所有学生数据
        for i in self.students:
            print("学号：" + i.stuNo, end="  ")
            print("姓名：" + i.stuName, end="  ")
            print("年龄：" + i.stuAge)

    #通过学号查询
    def query(self,stuNoQuery):
        status = False  #判断是否查到数值
        for i in self.students:
            if i.stuNo == stuNoQuery:
                status = True
                print("学号：" + i.stuNo, end="  ")
                print("姓名：" + i.stuName, end="  ")
                print("年龄：" + i.stuAge)
        if status ==False:
            print("该学号不存在！")

    #新增数据
    def insert(self,stuNoInsert, stuNameInsert, stuAgeInsert):
        status = False  #判断学号是否存在
        for i in self.students:
            if i.stuNo == stuNoInsert:
                status = True
                print("该学号已存在")
        if status == False: #学号不存在时新增数据
            student = Student(stuNo=stuNoInsert, stuName=stuNameInsert, stuAge=stuAgeInsert)
            self.students.append(student)
            print("新增成功！")

    #修改数据
    def update(self, stuNoUpdate, stuNameUpdate, stuAgeUpdate):
        status = False  #判断学号是否存在
        for i in self.students:
            if i .stuNo == stuNoUpdate:
                status = True
                i.stuName = stuNameUpdate
                i.stuAge = stuAgeUpdate
                print("修改成功！")
        if status == False:
            print("该学号不存在")

    #删除数据
    def delete(self,stuNoDelete):
        status = False  #判断学号是否存在
        for i in self.students:
            if i .stuNo == stuNoDelete:
                status = True
                self.students.remove(i)
                print("删除成功！")
        if status == False:
            print("该学号不存在")

class User: #用户对象，包含用户名和密码
    def __init__(self,userName,userPassword):
        self.userName = userName
        self.userPassword = userPassword
    def detail(self):
        print(self.userName)
        print(self.userPassword)

class Users:
    def __init__(self):
        self.users = []     #初始化一个列表users存放user

    def init(self):     #初始化的方法
        user = User(userName="Admin", userPassword="Admin")
        self.users.append(user)     #添加一条用户名为Admin，密码为Admin的数据
        user = User(userName="Robin", userPassword="123456")
        self.users.append(user)     #添加一条用户名为Robin，密码为123456的数据
        #print(self.users[0].userName)
        #print("测试")

    #登录的方法
    def login(self, userName, userPassword):
        status = False  #判断users列表中是否存在该用户名密码的数值
        for i in self.users:
            if userName == i.userName and userPassword == i.userPassword:
                status = True   #找到匹配数值
                print("登录成功")
                init2()  # 调用显示选择操作项的方法
                select2(input("请输入您的选择：\n"))  # 调用判断选择项的方法
        if status == False:
            print("登录失败，用户名或密码错误！")
            users.login(input("请输入用户名\n"),input("请输入密码\n"))
        #print("login")

    #注册的方法
    def register(self, userNameReg, userPasswordReg):
        status = False  #判断用户是否存在
        for i in self.users:
            if userNameReg == i.userName:
                status = True  #找到匹配数值
                print("该用户存在")
                init()  # 调用初始化控制台显示内容（1.登录，2.注册）的方法
                select(input("请输入您的操作："))  # 调用判断选择操作的方法(1.登录，2.注册)的方法
        if status == False:
            user = User(userName=userNameReg, userPassword=userPasswordReg) #实例化一个user
            self.users.append(user)   #向users列表中添加user数据
            print("注册成功，为您跳转到登录...")
            users.login(input("请输入用户名\n"), input("请输入密码\n"))  # 调用login方法



#users.register(input("请输入用户名：\n\r"),input("请输入密码：\n\r"))
#users.login(input("请输入用户名：\n\r"),input("请输入密码：\n\r"))

# students.show()
# students.query(input("请输入要查询的学号：\n\r"))
#初始化控制台显示内容（1.登录，2.注册）
def init():
    print("1.登录")
    print("2.注册")

#初始化控制台显示内容(0.显示全部，1.查询等)
def init2():
    print("0.显示所有")
    print("1.查询")
    print("2.新增")
    print("3.修改")
    print("4.删除")

#判断选择操作的方法(1.登录，2.注册)
def select(a):
    if a == '1':
        users.login(input("请输入用户名\n"),input("请输入密码\n"))
    elif a == '2':
        users.register(input("请输入用户名\n"),input("请输入密码\n"))
    else:
        print("error")

#判断选择操作的方法(0.显示全部，1.查询等)
def select2(a):
    if a == '0':
        students.show()
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '1':
        students.query(input("请输入学号：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '2':
        students.insert(input("请输入学号：\n"),input("请输入姓名：\n"),input("请输入年龄：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '3':
        students.update(input("请输入学号：\n"), input("请输入姓名：\n"), input("请输入年龄：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '4':
        students.delete(input("请输入学号：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    else:
        print("error")
        init2()
        select2(input("请输入您的选择：\n"))

users = Users() #实例化Users
users.init()    #初始化users数据
students = Students()   #实例化Students
students.init()         #初始化students数据
print("默认登录用户名密码均为“Admin”")
print("该系统使用面向对象实现")
init()  #调用初始化控制台显示内容（1.登录，2.注册）的方法
select(input("请输入您的操作："))   #调用#判断选择操作的方法(1.登录，2.注册)的方法