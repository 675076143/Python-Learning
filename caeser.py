def caesar():#加密的方法
    inputOrigin = input("请输入需要加密的信息：")
    inputList = list(inputOrigin)
    inputEncrypted = inputList
    for i in range(len(inputEncrypted)):
        if inputEncrypted[i] == " ":
            i = i+1
        else:
            inputEncrypted[i] = chr(ord(inputEncrypted[i])+3)
            
    print("信息加密成功："+"".join(inputEncrypted))
    show()
    
def caesarDecryption():#解密的方法
    inputOrigin = input("请输入需要解密的信息：")
    inputList = list(inputOrigin)
    inputEncrypted = inputList
    for i in range(len(inputEncrypted)):
        if inputEncrypted[i] == " ":
            i = i+1
        else:
            inputEncrypted[i] = chr(ord(inputEncrypted[i])-3)
            
    print("信息解密成功："+"".join(inputEncrypted))
    show()

def show():
    inputOrigin = input("请选择您的操作：\n1.加密\n2.解密\n")
    if inputOrigin == "1":caesar()
    elif inputOrigin == "2":caesarDecryption()
    else:
        print("请输入正确的选项")
        show()
show()
