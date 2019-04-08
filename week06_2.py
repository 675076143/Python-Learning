'''
fin = open('1.txt', 'r')

forward_index = {}
for line in fin:
    line = line.strip().split()
    forward_index[int(line[0])] = {}
    words = line[1].split(',')
    for i, index in enumerate(words):
        if int(index) not in forward_index[int(line[0])].keys():
            forward_index[int(line[0])][int(index)] = [i]
        else:
            forward_index[int(line[0])][int(index)].append(i)
print ('forward_index:', forward_index )

inverted_index = {}
for doc_id, words in forward_index.items():
    for word_id in words.keys():
        if word_id not in inverted_index.keys():
            inverted_index[word_id] = [doc_id]
        elif doc_id not in inverted_index[word_id]:
            inverted_index[word_id].append(doc_id)
#print ('inverted_index:', inverted_index)
'''
'''
list_dict_all = []               #创建一个空列表，全局变量，用来存放字典
def AddtoDict(str_1):            # 定义一个函数，功能：把文件里面的内容添加到字典中

   list_str1 = str_1.split(",")  # 读取的行内容以字符串的形式显示出来, 使用‘,’分隔字符串

   line_str = []                 # 创建一个空列表，用来接收去掉'\n'的行字符串
   for i in list_str1:
       x = i.strip("\n")
       line_str.append(x)
   # print(line_str)

   dict_all = {}                         # 创建一个空字典
   for item in line_str:                 # 遍历列表中的行内容，列表中有3个元素
         dict = {item: 1}
         dict_all.update(dict)            # 添加dict到空字典dict_all中

   list_dict_all.append(dict_all)                     # 将字典添加到list列表中


def list_dict(file_1):
    file = open(file_1, "r+")
    while True:
        line = file.readline()
        if line:
            AddtoDict(line)
        if not line:
            break
    file.close()
    print(list_dict_all)

list_dict("1.txt")  
'''
dict0 = {}
countLine = 0 #用一个int值来计算第几行
file = open("1.txt")
for line in file:
   countLine +=1
   line = line.strip('\n')
   lineStr = line.split()  #空格分隔
   for i in lineStr:
      dict0.setdefault(i,[]).append(countLine)  #值为列表的构造方法
                                                #内容为Key，行号为Value
for i in dict0.items(): #分行打印字典
   print(i)
   
print("-----------------------\n")

import collections

def que03(query):
   isExist = False
   if(query[0:4]=="AND:"):#包含全部关键字
      queryAnd = query[4:].split()#空格分隔单词
      listAnd = []   #创建空列表
      for i in queryAnd:#遍历列表中所有单词
         for key,val in dict0.items():
            if key == i:
               #print(val)
               listAnd = listAnd + val #合并列表
               isExist = True
         if isExist == False:
            print("None")  #不存在输出None
      if(([item for item, count in collections.Counter(listAnd).items() if count > 1])!=[]):
         print([item for item, count in collections.Counter(listAnd).items() if count > 1])
      else:
         print("None")

         
   elif(query[0:3]=="OR:"):#只要出现了一个关键字就满足条件
      queryOr = query[3:].split()#空格分隔单词
      for i in queryOr:#遍历列表中所有单词
         for key,val in dict0.items():
            if key == i:
               print(val)
               isExist = True
         if isExist == False:
            print("None")  #不存在输出None
            
   else:
      queryAnd = query.split()#空格分隔单词
      listAnd = []   #创建空列表
      for i in queryAnd:#遍历列表中所有单词
         for key,val in dict0.items():
            if key == i:
               #print(val)
               listAnd = listAnd + val #合并列表
               isExist = True
         if isExist == False:
            print("None")  #不存在输出None
      if(([item for item, count in collections.Counter(listAnd).items() if count > 1])!=[]):
         print([item for item, count in collections.Counter(listAnd).items() if count > 1])
      else:
         print("None")
      
que03(input("请输入要查询的单词：\n"))
que03(input("请输入要查询的单词：\n"))
