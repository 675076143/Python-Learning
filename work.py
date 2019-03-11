import math

def work_without_rest():    #每天进步1%
    result = math.pow((1.0+0.01),365)
    print("A君：{:.5f}".format(result))
    
def work_rest():    #每周工作5天休息2天
    result = 1
    for i in range(52):     #365/7= 52......1
        for x in range(5):  #进步
            result = (result*0.01+result)
        for y in range(2):  #休息
            result = (result*0.01-result)
    result = (result*0.01+result)
    print("B君：{:.5f}".format(result))

def rule(words):    #第三题字符串格式规范
    print(words.strip().lower().replace(" u ","you").replace(" lili"," LiLi").replace(" u"," you").replace(" 2"," to"))

    
'''
a=1
for i in range(365):
   a=(a*0.01+a)
   print(a)
'''
print("--------------------\n第1题：")
work_without_rest()
work_rest()

print("--------------------\n第2题：")
a = eval(input("请输入一个数a："))
print("a的次方为：\n{:-^20.2f}".format(a*a*a))

print("--------------------\n第3题：")
rule("      haPPy BiRthDAy To u");
rule("Happy biRthDAy To you")
rule(" haPpy BirThdAy 2 deAr LiLi       ")
rule("happy birthday 2 u")
