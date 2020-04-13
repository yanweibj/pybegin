# 在控制台中获取圆形的半径
# 计算面积(3.14 * r 的平方)与周长(2 * 3.14 * r)

str_r = input("请输入圆的半径:")
float_r = float(str_r)
float_c = 2 * 3.14 * float_r
str_c = str(float_c)
float_s = 3.14 * float_r * float_r
str_s = str(float_s)
print("圆的半径为：" + str_r + ", 周长为：" + str_c + "， 面积为：" + str_s + "。")