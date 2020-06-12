#1. 在控制台中循环录入字符串，输入ｑ时退出．
#　　然后显示一个新的字符串．

sentense = ""
print("请输入您的字符串，如输入q则结束并显示全部输入内容。")
while True:
    content = input("请输入字符串：")
    if content == "q":
        break
    sentense += content
print("您的输入内容为" + sentense)