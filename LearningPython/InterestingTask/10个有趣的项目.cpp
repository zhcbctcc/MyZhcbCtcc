https://www.jianshu.com/p/6ec91271ec33
  
#第一个程序：图片转字符串
#图片转字符画的关键思想是将图片的灰度值与你自己设定的字符集之间建立映射关系，不同区间的灰度值对应不同的字符，之后将
#图片每一个像素对应的字符打印出来就是我们要的字符画啦~ 
# 这里提供两种方法：
# 先将彩色图片转换为黑白图片，然后直接将每个像素点的灰度值与字符集建立映射。
# 获取图片的RGB值，利用公式： Gray = R*0.299 + G*0.587 + B*0.114
# 计算可得每个像素点的灰度值，之后再建立映射即可。

示例中的代码是用第一种方法

from PIL import Image

codeLib = '''朝冰 '''#生成字符画所需的字符集
count = len(codeLib)

def transform1(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数"L"表示黑白模式 黑白图片只有一个通道
    codePic = ''
    for h in range(0,image_file.size[1]):  #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h)) #返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]#建立灰度与字符集的映射
        codePic = codePic+'\r\n'
    return codePic

def transform2(image_file):
    codePic = ''
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]):
            g,r,b = image_file.getpixel((w,h))
            gray = int(r* 0.299+g* 0.587+b* 0.114)
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]
        codePic = codePic+'\r\n'
    return codePic


fp = open(u'psb.jpg','rb')
image_file = Image.open(fp)
image_file=image_file.resize((int(image_file.size[0]*0.75), int(image_file.size[1]*0.5)))#调整图片大小
print (u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)

tmp = open('tmp.txt','w')
tmp.write(transform1(image_file))
tmp.close()

# #第二个程序：生成分形图片
# import pygame, math
# 
# pygame.init()
# window = pygame.display.set_mode((600, 600))
# pygame.display.set_caption("Fractal Tree")
# screen = pygame.display.get_surface()
# 
# def drawTree(x1, y1, angle, depth):
#     if depth:
#         x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
#         y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
#         pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
#         drawTree(x2, y2, angle - 20, depth - 1)
#         drawTree(x2, y2, angle + 20, depth - 1)
# 
# def input(event):
#     if event.type == pygame.QUIT:
#         exit(0)
# 
# drawTree(300, 550, -90, 9)
# pygame.display.flip()
# while True:
#     input(pygame.event.wait())

