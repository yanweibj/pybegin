#2. 判断字符串是否是回文：
#    上海自来水来自海上
#    奶牛产牛奶
#    提示：字符串翻转

#solution 1
# string1 = "上海自来水来自海上"
# string1_1 = "".join(reversed(string1))
# if string1 == string1_1:
#     print(string1 + " 是回文")
# else:
#     print(string1 + " 不是回文")

# string2 = "奶牛产牛奶"
# string2_1 = "".join(reversed(string2))
# if string2 == string2_1:
#     print(string2 + " 是回文")
# else:
#     print(string2 + " 不是回文")

#solution 2
string1 = "上海自来水来自海上"
string2 = "奶牛产牛奶"
#选定用哪个字符串
prostring = string1
#运用list方式
list1 = list(prostring)
#正数和倒数的string相同，则为回文，判定距离为list长度一半取整
for i in range(len(list1)//2):
   if list1[i] != list1[-(i+1)]:
       print(prostring + " 不是回文")
       break
else:
  print(prostring + " 是回文")






