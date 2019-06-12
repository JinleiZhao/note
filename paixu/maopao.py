def func(l):
    print(l)
    for i in range(len(l)-1):   #循环次数（每次取出最大最小值）/最后一次固定最大/最小
        for j in range(len(l)-i-1):  #交换相邻的位置：排好序的无需在交换 
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
        print(l)

import random
l = list(range(10))
random.shuffle(l)
func(l)