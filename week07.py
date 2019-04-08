def que01():
    file = 'learning_python.txt'
    print("第一次打印:")
    with open(file) as openFile:
        contents = openFile.read()
        print(contents)
    print("\n")

    print("第二次打印:")    
    with open(file) as openFile:
        for line in openFile:
            print(line)
    print("\n")

    print("第三次打印:")    
    with open(file) as openFile:
        lines = openFile.readlines()
    print(lines)



dict0 = {}
countLine = 0 #用一个int值来计算第几行
file = open("07.txt")
for line in file:
   countLine +=1
   line = line.strip('\n')
   lineStr = line.split()  #空格分隔
   for i in lineStr:
      dict0.setdefault(countLine,[]).append(i)  #内容为Key，行号为Value
print(dict0)

