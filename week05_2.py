vowel = "aeiou" #元音
def PigLatin():
    array = input("请输入一系列单词，单词之间用空格分隔\n")
    array = array.lower().split()    
    
    array04 = ""
    array04END=""
    for i in range(len(array)):
        if(array[i][:1] in vowel):
            array[i] +="hay"
        elif(array[i][:2]=="qu"):
            array = array[i][len(array[i]):]+"quay"
        else:
            array04 = condition04(array[i])
            array[i] = array[i][array04:]+array[i][0:array04]+"ay"
    return array;
def condition04(array04):
    for i in range(len(array04)):#下方判断，如果y不在第一个字母，当成元音
        if((array04[i] in vowel) or (i!=0 and array04[i] =="y")):
            return i;
    return len(array04);

#print(PigLatin())

import string
import keyword

def que02(s):
    if s not in keyword.kwlist:  #字符串不能是关键字
        if  (s[0].isalpha()) or (s[0]=="_"):#首字符必须是字母或者下划线
            for i in s[1:]:
                if (i.isalpha()!=True) and (i.isdigit()!=True) and (i!="_"): #由数字字母下划线组成
                    return False
            return True    
    return False      
#print(que02(input("请输入字符串:")))

def que03(s):
    s = s.lower() #转换成小写
    result = 0
    for i in s:
        result += ord(i)-96 #通过ascii码计算
    return result
    
print(que03(input("请输入要计算字母值的字符串:\n")))

