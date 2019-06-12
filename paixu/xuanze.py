def func(l):
    for i in range(len(l)-1):  #循环次数
        minindex = l[i]        #每次取出选择位
        for j in range(i+1,len(l)): #从当前位置向后寻找
            if l[j] < l[minindex]:   
                minindex = j   #选出此次循环最小值的位置
        l[i],l[minindex] = l[minindex],l[i]   #本次结束后进行交换
        print(l)

import random
l = list(range(10))
random.shuffle(l)
func(l)