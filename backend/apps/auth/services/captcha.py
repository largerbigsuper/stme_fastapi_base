import base64
import io
import os
import random
import string
from random import randint

from PIL import Image, ImageDraw, ImageFont


async def get_captcha():
    # 生成随机验证码字符串
    captcha_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    # 创建新图像
    image = Image.new("RGB", (100, 50), (124, 231, 122))
    # 创建画布
    draw = ImageDraw.Draw(image)  
    # 加载字体 是Windows自带的
    font_path = os.path.join("static", "fonts", "Arial.ttf")
    font = ImageFont.truetype(font_path, size=30)
    x = 15
    for i in captcha_string: # 随机验证码
        # 为每个验证码字符设置不同的RGB颜色
        R = str(randint(0, 255))
        G = str(randint(0, 255))
        B = str(randint(0, 255))
        draw.text((x, 10),
                text=i,
                font=font,
                fill="rgb(" + R + "," + G + "," + B + ")",
                direction=None)
        x += 20 

    # # 添加干扰线条
    # for i in range(1, randint(7, 15)): # 线条数量在7-15间
    #     x, y = randint(0, 100), randint(0, 50) # 线条起点
    #     x2, y2 = randint(0, 100), randint(0, 50) # 线条终点
        
    # 	# 随机颜色
    #     R = str(randint(0, 255))
    #     G = str(randint(0, 255))
    #     B = str(randint(0, 255))
    #     # 绘制线条 宽度为2
    #     draw.line((x, y, x2, y2), fill="rgb(" + R + "," + G + "," + B + ")", width=2)

    # image.show()
    # 创建空的字节流对象
    stream = io.BytesIO()

    # 将图像保存到字节流对象中
    image.save(stream, format="PNG")

    # 将字节流对象指针重置到开头
    stream.seek(0)

    # 获取字节流对象的值
    binary_data = stream.getvalue()

    # 将二进制数据转换为Base64编码的字符串
    base64_data = base64.b64encode(binary_data).decode("utf-8")
    return base64_data
    # image.save("CAPTCHA.png")

