import os

def my_fun(args):
    for root, dirs, files in os.walk('E:\WorkNote\\note\\'):
        for file in files:
            if args in file:
                path = os.path.join(root, file)
                print(path)
                print('dirname',os.path.dirname(path))  # 目录
                print('abspath', os.path.abspath(path)) #绝对完整路径
                print('basename', os.path.basename(path)) #文件名
                print(os.path.splitext(path))   #分割路径和后缀
                #print(os.environ)
            # else:
            #     print('no:',os.path.join(root, file))

def v1(addr):
    # 取每个数
    id = [int(x) for x in addr.split(".")]
    print(id)
    return [id[i] << [24, 16, 8, 0][i] for i in range(4)]


if __name__ == "__main__":
    my_fun('flask')
    print(v1("127.0.0.1"))


