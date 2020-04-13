# 在控制台中获取华氏度,计算摄氏度
print("输入华氏度，计算摄氏度")
str_h_tem = input("请输入华氏度:")
float_h_tem= float(str_h_tem)
float_s_tem = (float_h_tem -32)/1.8
print("你输入的华氏度为：" + str_h_tem + "，切换为摄氏度为: " + str(float_s_tem) + ".")


#在控制台中获取摄氏度,计算华氏度
print("输入摄氏度，计算华氏度和开氏度")
str_s_tem = input("请输入摄氏度:")
float_s_tem = float(str_s_tem)
float_h_tem = float_s_tem * 1.8 + 32
float_k_tem = float_s_tem + 273.15
str_h_tem = str(float_h_tem)
str_k_tem = str(float_k_tem)
print("你输入的摄氏度为:" + str_s_tem + ", 切换为华氏度为:" + str_h_tem + "." ) 
print("切换为开氏度为:" + str_k_tem + ".")

