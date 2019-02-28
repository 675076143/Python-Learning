currency = input("请输入带单位的货币数值：")
while currency[-1] not in ['N','n']:
    if currency[-3:] in ['USD','usd']:
        value = eval(currency[0:-3])*6.69
        print("转换过后的数值为：{:.2f}CNY".format(value))
    elif currency[-3:] in ['CNY','cny']:
        value = eval(currency[0:-3])/6.69
        print("转换过后的数值为：{:.2f}USD".format(value))
    else:
        print("请输入正确的数值")
    currency = input("请输入带单位的货币数值：")
print("Python github test")