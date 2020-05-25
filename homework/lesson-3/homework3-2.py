#2. (扩展)在控制台中录入一个整数,判断是否为素数.
#  只能被1和自身整除的数字

number = int(input("请输入一个正整数，我来判定它是否是素数："))
base = 2
while base < number:
    if number % base == 0:
        print(str(number)+" 不是素数")
        break
    else:
        base += 1
else:
    print(str(number)+" 是素数")

