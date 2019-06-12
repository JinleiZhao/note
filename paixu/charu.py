def func(l):
    print(l)
    for i in range(1,len(l)):
        ele, index = l[i], i  # 当前需要排序的元素,# 用来记录排序元素需要插入的位置
        while index > 0 and l[index-1] > ele:
            l[index] = l[index-1]    # 把已经排序好的元素后移一位，留下需要插入的位置
            index -=1
        l[index] = ele   # 把需要排序的元素，插入到指定位置
        print(l)
        
import random
l = list(range(10))
random.shuffle(l)
func(l)