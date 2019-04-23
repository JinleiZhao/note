# import xyz
from other import xyz  

'不在同一文件下，windows可以不加__init__,linux 无论python几都需要加'
'在同一目录下可以直接引用，不用添加__init__.py文件'
# print(__name__)
# print(xyz.get_name())
# print(other_xy())
print(xyz.other_xy())
