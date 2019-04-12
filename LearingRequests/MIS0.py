dictUsers = {"Admin":"Admin","Robin":"123456"}  #存放用户名(Key)和密码(value)的字典
dictStudents = {"1706105308":["黄旭震","19"],"1706105300":["Admin","20"]}  #存放学号(Key) 姓名+年龄(value)的字典

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
        login(input("请输入用户名\n"),input("请输入密码\n"))
    elif a == '2':
        register(input("请输入用户名\n"),input("请输入密码\n"))
    else:
        print("error")

#判断选择操作的方法(0.显示全部，1.查询等)
def select2(a):
    if a == '0':
        print(dictStudents)
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '1':
        query(input("请输入学号：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '2':
        insert(input("请输入学号：\n"),input("请输入姓名：\n"),input("请输入年龄：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '3':
        update(input("请输入学号：\n"), input("请输入姓名：\n"), input("请输入年龄：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    elif a == '4':
        delete(input("请输入学号：\n"))
        init2()
        select2(input("请输入您的选择：\n"))
    else:
        print("error")
        init2()
        select2(input("请输入您的选择：\n"))

#登录的方法
def login(a,b): #a(用户名) b(密码)
    if a in dictUsers.keys():   #判断字典dictUser中是否有Key a
        if b==dictUsers[a]:     #如果有，并且Key为a的value为b
            print("登陆成功！")  #输出登录成功
            init2()              #调用显示选择操作项的方法
            select2(input("请输入您的选择：\n"))    #调用判断选择项的方法
    else:
        print("请检查您的用户名和密码")
        login(input("请输入用户名\n"),input("请输入密码\n"))

#注册的方法
def register(a,b):  #a(用户名) b(密码)
    if a in dictUsers.keys():   #如果字典dictUser中存在Key a
        print("用户名已存在！")    #输出用户名已存在
        init()  # 调用初始化控制台显示内容(0.显示全部，1.查询等)
        select(input("请输入您的选择：\n"))
    else:   #否则
        dictUsers[a] = b    #向字典dictUser中新增一条Key a value为b的键值对
        print("注册成功！为您跳转到登录...")    #输出注册成功，为您登录
        login(input("请输入用户名\n"), input("请输入密码\n"))  #调用login方法

#查询数据的方法
def query(a):   #a(学号)
    if a in dictStudents.keys():    #如果字典dictStudents中存在Key a(学号)
        print(dictStudents[a])  #输出字典dictStudent中Key为a的键值对
    else:
        print("该学号不存在")

#新增数据的方法
def insert(a,b,c):  #a(学号) b(姓名) c(年龄)
    info = [b,c]    #将b(姓名),c(年龄)保存在列表info中
    if a in dictStudents.keys():    #如果字典dictStudents中存在Key a
        print("该学号已存在！")    #显示该学号存在
    else:       #否则
        dictStudents[a] = info      #插入一条Key为a，value的数据
        print("新增成功")

#更新数据的方法
def update(a,b,c):  #a(学号) b(姓名) c(年龄)
    info = [b, c]   #将b(姓名),c(年龄)保存在列表info中
    if a in dictStudents.keys():    #如果字典dictStudents中存在Key a
        dictStudents[a] = info      #更新Key为a的value
        print("更新成功！")
    else:
        print("该学号不存在！")

#删除数据的方法
def delete(a):  #a(学号)
    if a in dictStudents.keys():    #如果字典dictStudents存在Key a
        dictStudents.pop(a)         #删除Key为a的键值对
        print("删除成功！")
    else:
        print("该学号不存在")

print("默认登录用户名密码均为“Admin”")
print("该系统使用字典+列表实现")
init()  #调用初始化控制台显示内容（1.登录，2.注册）的方法
select(input("请输入您的操作："))   #调用#判断选择操作的方法(1.登录，2.注册)的方法