from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string #string模块中自带数字、字母、特殊字符变量集合
import uuid
try:
    from io import  BytesIO #py3
except ImportError:
    from cStringIO import cStringIO as BytesIO #py2

class Code(object):
    
    __letter_cases = "abcdefghigklmnopqrstuvwxyz"
    __upper_cases = "ABCDEFGHIGKLMNOPQRSTUVWXZYZ"
    __number_cases = "23456789"
    __init_chars = "".join((__letter_cases, __upper_cases, __number_cases))
    __default_font = "/usr/share/fonts/truetype/DejaVuSans.ttf"

    def __init__(self, size=(120, 30),
                 chars=__init_chars,
                 img_type="GIF",
                 mode="RGB",
                 bg_color=(255, 255, 255),
                 fg_color=(0, 0, 255),
                 font_size=18,
                 font_type=__default_font,
                 length=4,
                 draw_lines=True,
                 n_line=(1, 2),
                 draw_points=True,
                 point_chance=3,
                 save_img=False):
        """
        生成验证码图片
        size: 图片的大小，格式（宽，高），默认为(120, 30)
        chars: 允许的字符集合，格式字符串
        img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
        mode: 图片模式，默认为RGB
        bg_color: 背景颜色，默认为白色
        fg_color: 前景色，验证码字符颜色，默认为蓝色  # 0000FF
        font_size: 验证码字体大小
        font_type: 验证码字体，默认为 DejaVuSans.ttf
        length: 验证码字符个数
        draw_lines: 是否划干扰线
        n_line: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
        draw_points: 是否画干扰点
        point_chance: 干扰点出现的概率，大小范围[0, 100]
        save_img: 是否保存为图片
        [0]: 验证码字节流, [1]: 验证码图片中的字符串
        """

        self.size = size
        self.chars = chars
        self.img_type = img_type
        self.mode = mode
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.font_size = font_size
        self.font_type = font_type
        self.length = length
        self.draw_lines = draw_lines
        self.n_line = n_line
        self.draw_points = draw_points
        self.point_chance = point_chance
        self.save_img = save_img
    
    def generate_verify_image(self):

        self.width, self.height = self.size
        #创建图形
        self.img = Image.new(self.mode, self.size, self.bg_color)
        #创建画笔
        self.draw = ImageDraw.Draw(self.img) 

    def get_chars(self):
        """生成给定长度的字符串，返回列表格式"""
        show_chars = random.sample(self.chars, self.length)
        return show_chars

    def create_lines(self):
        """绘制干扰线"""
        line_num = random.randint(*self.n_line) #干扰线条数
        for i in range(line_num):
            #起始点
            begin = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
            #终止点
            end = (random.randint(0,self.size[0]), random.randint(0, self.size[1]))
            self.draw.line([begin, end], fill=tuple(0 for i in range(3)))

    def create_points(self):
        """画干扰点"""

        for x in range(self.width):
            for y in range(self.height):
                tmp = random.randint(0,100)
                if tmp > (100 - self.point_chance):
                    self.draw.point((x, y), 
                    fill=tuple(0 for i in range(3)))
                del tmp

    def create_strs(self):
        """绘制验证码"""
        #生成验证字符
        chars = self.get_chars()
        strs = " %s " % " ".join(chars)
         
        font = ImageFont.truetype(self.font_type, self.font_size) 
        font_width, font_height = font.getsize(strs)

        self.draw.text(((self.width-font_width)/3, (self.height-font_height)/3), 
                        strs, font=font, fill=self.fg_color)
        
        return "".join(chars)

    def generate_img(self):
        
        self.generate_verify_image()

        if self.draw_lines:
            self.create_lines()
        if self.draw_points:
            self.create_points()
        
        strs = self.create_strs()
        # 图形扭曲参数
        params=[1 - float(random.randint(1, 2)) / 100,
                0,
                0,
                0,
                1 - float(random.randint(1, 10)) / 100,
                float(random.randint(1, 2)) / 500,
                0.001,
                float(random.randint(1, 2)) / 500
        ]
        #创建扭曲
        self.img = self.img.transform(self.size, Image.PERSPECTIVE, params)
        # 滤镜，边界加强（阈值更大）
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
        path = BytesIO()
        self.img.save(path, self.img_type) 
        
        self.img.show(path.getvalue())
        if self.save_img:
            self.img.save("code.gif", self.img_type)
        
        return path,strs

    def remind(self):
        """传递给前端要进行转换 """
        from flask import jsonify
        return jsonify({'code': 0, 'img': img.getvalue().encode('base64')})
        """
        ("#img").attr("src", "data:image/gif;base64," + data.img);
        """

if __name__ == "__main__":
    verify_code = Code()
    img, code = verify_code.generate_img()
    print(img.getvalue(), code)

