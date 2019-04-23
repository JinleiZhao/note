import os
def test():
    pat = os.path.abspath(__file__)
    print(pat)
    for root, _dirs, _files in os.walk('E:\StudyNote\html'):
        'root当前执行路劲，_dirs当前路径下的所有文件夹list类型，_files当前路径下的所有文件list类型'
        if root.split('\\')[-1] == 'images':
            print(root)
            break

import sys

print('_____________________________________')
print(os.path.abspath('static'))
print(os.path.dirname('static'))

def Getdir(filename,dirs = None):
    dirs = [] if dirs == None else dirs
    for file in os.listdir(filename):
        full_path = os.path.join(filename, file)
        if os.path.isfile(full_path):
            dirs.append(full_path)
        else:
            dirs= None if not dirs else dirs
            print(dirs)
            Getdir(full_path,dirs )
    return dirs

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        raise "Please Inter the filename!"
    for root_path, dirs, filrs in os.walk('E:\\vmshare\game\game'):
        if root_path.split('\\')[-1] == filename:
            file = root_path
            break
    print(file)
    files = Getdir(file)
    print(files)