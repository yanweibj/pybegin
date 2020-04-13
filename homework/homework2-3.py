# 修改exercise03中的练习,如果金额不足,提示还差多少钱,如果金额够,提示应找回多少钱.
#- - 尝试:如果总价到达100元,打八折.

# 练习1:在控制台中获取一个商品单价  10
#      在获取一个商品数量   3
#      在获取一个金额  50
#      计算:应该找回多少钱 20

str_unit_price = input("请输入商品单价:")
float_unit_price = float(str_unit_price)
amount = int(input("请输入商品数量:"))
#计算商品总价格
float_total = float_unit_price * amount
#如果总价格大于100，则打八折
if float_total >= 100 :
    float_total = float_total * 0.8
    print("商品总价格超过100.打八折")
print("商品总价为:" + str(float_total))

money = float(input("请输入付款金额:"))
result = money - float_total
if result > 0 :
    print("应找回:"+str(result))
elif result == 0 :
    print("金额正好。")
else:
    print("你的付款不够，还差:" + str(0-result))

