import jieba


def que01():
   list01 = list()
   list01 = list(jieba.cut("中华人民共和国是一个伟大的国家"))
   return list01

print(que01())
    
def que02():
    jieba.add_word("Java是世界上最好的语言")
    return jieba.lcut("我认为在众多编程语言中，Java是世界上最好的语言！")

dict = {"Robin":0,"Jacky":0,"John":0}
def CountVote(name):
    dict[name] +=1
    print("-------------------\n")
    for k in sorted(dict,reverse=True):
        print(k,dict[k])
    return CountVote(input("请输入您要投给的人(Robin,Jacky,John)：\n"))
    

#print(CountVote(input("请输入您要投给的人(Robin,Jacky,John)：\n")))

def que04(words):
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
        

#que04(input("请输入英文文章：\n"))