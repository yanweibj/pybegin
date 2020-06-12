# 3.  一注彩票７个球
# 　　前六个是红球：１　－－　３３　之间的数字，且不能重复．
#     最后一个是蓝球：１　－－　１６　之间的数字
#     （１）　在控制台中购买彩票
#     （２）　随机产生一注彩票

import random

blue = []
while(len(blue) < 6):
    x = random.randint(1,33)
    if x not in blue:
        blue.append(x)
blue.sort()
red = []
red.append(random.randint(1,16))
print("篮球号码为: " + str(blue) +", 红球号码为: " + str(red))