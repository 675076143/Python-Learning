import csv
import math

saveFile = []
class Student:  #学生对象，包含学号 姓名 和年龄
    def __init__(self, stuNo, stuName, chinese=0, math=0, english=0):
        self.stuNo = stuNo
        self.stuName = stuName
        self.chinese = int(chinese)
        self.math = int(math)
        self.english = int(english)
        self.total = int(chinese) + int(math) + int(english)
    def __repr__(self): # 迭代
        return repr((self.stuNo, self.stuName, self.chinese, self.math, self.english))
    def __iter__(self): # 迭代
        return self
    def detail(self):
        print(self.stuNo)
        print(self.stuName)
        print(self.chinese)
        print(self.math)
        print(self.english)

class Students:
    def __init__(self):
        self.students = []  #初始化一个列表students存放student

    def init(self): #初始化的方法
        csv_file = csv.reader(open('marks.csv', 'r'))
        for i in csv_file:
            if i[0] != '学号':
                students.insert(i[0], i[1], i[2], i[3], i[4])

        print("读取成功！")


    def show(self): #打印所有学生数据
        for i in self.students:
            print("学号：" + i.stuNo, end="  ")
            print("姓名：" + i.stuName, end="  ")
            print("语文：", i.chinese, end="  ")
            print("数学：", i.math, end="  ")
            print("英语：", i.english, end="  ")
            print("总分：",i.total)

    def save(self): #保存数据
        for i in self.students:
            saveDict = {}
            saveDict["学号"] = i.stuNo
            saveDict["姓名"] = i.stuName
            saveDict["语文"] = i.chinese
            saveDict["数学"] = i.math
            saveDict["英语"] = i.english
            saveFile.append(saveDict)

    #通过学号查询
    def query(self,stuNoQuery):
        status = False  #判断是否查到数值
        for i in self.students:
            if i.stuNo == stuNoQuery:
                status = True
                print("学号：" + i.stuNo, end="  ")
                print("姓名：" + i.stuName, end="  ")
                print("语文：", i.chinese, end="  ")
                print("数学：", i.math, end="  ")
                print("英语：", i.english)

        if status ==False:
            print("该学号不存在！")

    #新增数据
    def insert(self,stuNoInsert, stuNameInsert, chineseInsert, mathInsert, englishInsert):
        status = False  #判断学号是否存在
        for i in self.students:
            if i.stuNo == stuNoInsert:
                status = True
                print("该学号已存在")
        if status == False: #学号不存在时新增数据
            student = Student(stuNo=stuNoInsert, stuName=stuNameInsert, chinese=chineseInsert, math=mathInsert, english=englishInsert)
            self.students.append(student)
            print("新增成功！")

    #修改数据
    def update(self, stuNoUpdate, stuNameUpdate, chineseUpdate, mathUpdate, englishUpdate):
        status = False  #判断学号是否存在
        for i in self.students:
            if i .stuNo == stuNoUpdate:
                status = True
                if(stuNameUpdate != ""):
                    i.stuName = stuNameUpdate
                if(chineseUpdate != ""):
                    i.chinese = chineseUpdate
                if(mathUpdate != ""):
                    i.math = mathUpdate
                if(englishUpdate !=""):
                    i.english = englishUpdate
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

    def sort(self, rule):
        if rule == "chinese":
            self.students=sorted(self.students,key=lambda student:student.chinese)
            students.show()
        elif rule == "math":
            self.students=sorted(self.students, key=lambda student: student.math)
            students.show()
        elif rule == "english":
            self.students=sorted(self.students, key=lambda student: student.english)
            students.show()
        elif rule == "total":
            self.students=sorted(self.students, key=lambda student: student.total)
            students.show()

    #统计数据
    def stat(self, rule):
        print(len(self.students))
        chinese = 0
        math = 0
        english = 0
        for i in self.students:
            chinese += i.chinese
            math += i.math
            english += i.english

        if rule == "average":
            print("语文平均分：", chinese / len(self.students))
            print("数学平均分：", math / len(self.students))
            print("英语平均分：", english / len(self.students))
        elif rule == "variance":
            varianceChinese = 0
            varianceMath = 0
            varianceEnglish = 0
            for i in self.students:
                x = i.chinese - (chinese / len(self.students))
                varianceChinese += pow(x,2)
                y = i.math - (math / len(self.students))
                varianceMath += pow(y, 2)
                z = i.english - (english / len(self.students))
                varianceEnglish += pow(z, 2)

            print("语文均方差：", varianceChinese / len(self.students))
            print("数学均方差：", varianceMath / len(self.students))
            print("英语均方差：", varianceEnglish / len(self.students))

    def range(self):
        chinese60 = 0
        chinese70 = 0
        chinese80 = 0
        chinese90 = 0
        chinese100 = 0
        for i in self.students:
            if 0<=i.chinese<=60:
                chinese60 +=1
            elif 60<=i.chinese<=70:
                chinese70 += 1
            elif 70<=i.chinese<=80:
                chinese80 += 1
            elif 80<=i.chinese<=90:
                chinese90 += 1
            elif 90<=i.chinese<=100:
                chinese90 += 1
        print("语文分段：")
        print("0-60分的人数为：", chinese60, "人")
        print("60-70分的人数为：", chinese70, "人")
        print("70-80分的人数为：", chinese80, "人")
        print("80-90分的人数为：", chinese90, "人")
        print("90-100分的人数为：", chinese100, "人")
        print("-------------------------")
        math60 = 0
        math70 = 0
        math80 = 0
        math90 = 0
        math100 = 0
        for i in self.students:
            if 0<=i.math<=60:
                math60 +=1
            elif 60<=i.math<=70:
                math70 += 1
            elif 70<=i.math<=80:
                math80 += 1
            elif 80<=i.math<=90:
                math90 += 1
            elif 90<=i.math<=100:
                math90 += 1
        print("数学分段：")
        print("0-60分的人数为：", math60, "人")
        print("60-70分的人数为：", math70, "人")
        print("70-80分的人数为：", math80, "人")
        print("80-90分的人数为：", math90, "人")
        print("90-100分的人数为：", math100, "人")
        print("-------------------------")
        english60 = 0
        english70 = 0
        english80 = 0
        english90 = 0
        english100 = 0
        for i in self.students:
            if 0<=i.english<=60:
                english60 +=1
            elif 60<=i.english<=70:
                english70 += 1
            elif 70<=i.english<=80:
                english80 += 1
            elif 80<=i.english<=90:
                english90 += 1
            elif 90<=i.english<=100:
                english90 += 1
        print("英语分段：")
        print("0-60分的人数为：", english60, "人")
        print("60-70分的人数为：", english70, "人")
        print("70-80分的人数为：", english80, "人")
        print("80-90分的人数为：", english90, "人")
        print("90-100分的人数为：", english100, "人")


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


def init():     # 初始化控制台显示内容（1.登录，2.注册）
    print("1.登录")
    print("2.注册")


def init2():    # 初始化控制台显示内容(0.显示全部，1.查询等)
    print("---------------")
    print("init.读取文件")
    print("0.显示 | 1.查询")
    print("2.新增 | 3.修改")
    print("4.删除 | 5.保存")
    print("order.排序")
    print("stat.成绩统计")
    print("range.分段统计")


def select(a):      # 判断选择操作的方法(1.登录，2.注册)
    if a == '1':
        users.login(input("请输入用户名\n"),input("请输入密码\n"))
    elif a == '2':
        users.register(input("请输入用户名\n"),input("请输入密码\n"))
    else:
        print("error")

#判断选择操作的方法(0.显示全部，1.查询等)
def select2(a):
    if a == 'init':
        students.init()
        print("init success!")
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '0':
        students.show()
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '1':
        students.query(input("请输入学号：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '2':
        students.insert(input("请输入学号：\n"),
                        input("请输入姓名：\n"),
                        input("请输入语文成绩：\n"),
                        input("请输入数学成绩：\n"),
                        input("请输入英语成绩：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '3':
        students.update(input("请输入学号：\n"),
                        input("请输入姓名：\n"),
                        input("请输入语文成绩：\n"),
                        input("请输入数学成绩：\n"),
                        input("请输入英语成绩：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '4':
        students.delete(input("请输入学号：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '5':
        students.save()

        headers = ['学号', '姓名', '语文', '数学', '英语']
        with open('marks.csv', 'w', newline="") as f:
            f_scv = csv.DictWriter(f, headers)
            f_scv.writeheader()
            f_scv.writerows(saveFile)
        print("保存成功！")
        init2()
        select2(input("请输入您的选择：\n"))

    elif a == 'stat':
        a = input("选择您的统计规则：\n\r1.平均数\n\r2.方差\n\r")
        if a == "1":
            students.stat("average")
            init2()
            select2(input("请输入您的选择：\n"))
        elif a == "2":
            students.stat("variance")
            init2()
            select2(input("请输入您的选择：\n"))
        else:
            print("请输入正确的选择! ")
            init2()
            select2(input("请输入您的选择：\n"))

    elif a == 'order':
        b = input("选择您的排序规则：\n\r1.语文\n\r2.数学\n\r3.英语\n\r4.总分\n\r")
        if b == '1':
            students.sort("chinese")
            init2()
            select2(input("请输入您的选择：\n"))
        elif b == '2':
            students.sort("math")
            init2()
            select2(input("请输入您的选择：\n"))
        elif b == '3':
            students.sort("english")
            init2()
            select2(input("请输入您的选择：\n"))
        elif b == '4':
            students.sort("total")
            init2()
            select2(input("请输入您的选择：\n"))
        else:
            print("输入错误")
            init2()
            select2(input("请输入您的选择：\n"))
    elif a=="range":
        students.range()
        init2()
        select2(input("请输入您的选择：\n"))
    else:
        print("error")
        init2()
        select2(input("请输入您的选择：\n"))


users = Users()  # 实例化Users
users.init()
students = Students()   # 实例化Students
print("默认登录用户名密码均为“Admin”")
print("该系统使用面向对象实现")
init()  # 调用初始化控制台显示内容（1.登录，2.注册）的方法
select(input("请输入您的操作：\n\r"))   # 调用#判断选择操作的方法(1.登录，2.注册)的方法
