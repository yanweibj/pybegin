# 一个球从100m的高度落下,每次弹回原高度的一半.
#   总共弹起多少次?(假定:最小弹起高度是0.01m)
#   总共走了多少米.

#初始高度100米
float_height = 100.0

#设定初始距离为0
float_sum= 0.0
#设定初始弹起次数为0
int_count = 0
#当小球高度大于0.01米时进行循环
while float_height >= 0.01:
    int_count += 1
    float_sum += float_height
    float_height /= 2
    float_sum += float_height
    print("第%d次弹起来的高度是%f." % (int_count, float_height))
#加入最后一次落地的高度
float_sum += float_height
print("一共弹起%d次" %int_count)
print("总共走了%.2f米" % float_sum)