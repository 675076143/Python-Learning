def f(n):
    array = []
    resultSum = 0           #统计偶数之和
    x = 0                   #判断输入的数值在数列的第几位
    for i in range  (20):   #获取斐波那契数列前20项
        if i==0 or i==1:
            array.append(1)
        else:            
            array.append(array[i-2]+array[i-1])              
    
    for i in range(0,len(array)):
        if(array[i]>=n):    #遍历数列，找到第一个大于n的数值，跳出循环
            #print(array[i-1])#前一个数值则为不超过输入的数值的最大项
            x=(i-1)
            break

    for i in range(x):
        if i==0 or i==1:
            x = 0
        else:
            if(array[i-2]+array[i-1])%2==0:
                resultSum+=(array[i-2]+array[i-1])

    return resultSum

#print(f(eval(input("请输入斐波那契数列的最大值: "))))


import calendar
def que02(year):
    return calendar.calendar(year)
#print(que02(eval(input("请输入要查询的年份: "))))

# 定义判断闰年的函数,是闰年返回True,不是返回False
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# 定义计算从1970年到截止到今年的 年天数的函数
def yearsDays(year):
    totalDays = 0
    if year >= 1970:
        for i in range(1970, year):
            # print("%d年" % i)
            if isLeapYear(i):
                totalDays += 366
            else:
                totalDays += 365
    else:
        for i in range(year, 1970):
            # print("%d年" % i)
            if isLeapYear(i):
                totalDays += 366
            else:
                totalDays += 365
    return totalDays


# 定义计算本年一月截止到目前月的 月天数的函数
def monthsDays(year, month):
    s = ("0", "31", "60", "91", "121", "152", "182", "213", "244", "274", "305", "335")
    days = int(s[month - 1])
    # print(month,"月")
    if isLeapYear(year):
        days = days
    else:
        if month == 1:
            days = 0
        elif month == 2:
            days == 31
        else:
            days = days - 1
    return days


# 定义计算本月的天数
def thisMonthDays(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif isLeapYear(year) and month == 2:
        return 29
    elif (not isLeapYear(year)) and month == 2:
        return 28
    else:
        return 30


# 计算本月一号是星期几的函数
def week(year, month):
    thisDay = 0
    yDays = yearsDays(year)
    mDays = monthsDays(year, month)
    # 计算出来年天数和月天数的总和
    if year >= 1970:
        sumDays = yDays + mDays
        if sumDays % 7 == 0:
            thisDay = 4
        else:
            if sumDays % 7 + 4 > 7:
                thisDay = abs(sumDays % 7 - 3)
            else:
                thisDay = sumDays % 7 + 4
    else:
        sumDays = yDays - mDays
        if sumDays % 7 == 0:
            thisDay = 4
        else:
            lastDay = sumDays % 7
            thisDay = 4 - lastDay
            if thisDay < 0:
                thisDay += 7

    return thisDay


# 定义打印顶部标题栏函数
def printTitle(year, month):
    print("-" * 36, "%s年%d月" % (year, month), "-" * 36)
    s = ("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六")
    for i in s:
        print("%-10s" % i, end="")
    print()


# 打印主体部分

def printMain(year, month):
    day1 = week(year, month)
    day2 = thisMonthDays(year, month)
    # 打印空白地方
    if day1 != 7:
        for i in range(1, day1 + 1):
            s = " "
            print("%-13s" % s, end="")
    # 打印其他地方
    for j in range(day1 + 1, day1 + day2 + 1):

        if j % 7 == 0:
            print("%-13d" % (j - day1))
        else:
            print("%-13d" % (j - day1), end="")


year = int(input("请输入年份:"))
month = int(input("请输入月份："))
printTitle(year, month)
printMain(year, month)
