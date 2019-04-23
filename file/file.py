with open('filetest.txt', 'r+') as f:
    try:
        data = f.readlines()
        print("read", data)
    except:
        print('cant read')
    try:
        f.write("hello2 world2 ")
        print("write ok!")
    except:
        print('cant wirte')

'''
    文件不存在创建文件
w:可写不可读，覆盖原内容，
w+:可读可写，但是读到内容为空，(先清空再写入)
    文件不存在报错
r:只能读取文件
r+:可读可写，在文件末尾写入(同时调用读和写)，但是本次写入不能读出来
    文件不存在创建文件
a:在末尾追加的方式写入，无法读取
a+:在末尾追加的方式写入，读取数据为空
'''