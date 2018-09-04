import xyz
import other.xyz

'在同一目录下可以直接引用，不用添加__init__.py文件'
print(__name__)
print(xyz.get_name())