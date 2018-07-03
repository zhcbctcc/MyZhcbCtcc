#第一个代码：打开图像，计算像素
# from PIL import Image
#
# im  = Image.open("psb.jpg") #
# w,h = im.size
# print('Original image size :%s%s' % (w,h))
#
# im.thumbnail((w/2,h/2))
# print('Resized image to %s%s' % (w//2,h//2))
#
# im.save('thumbnail.jpg','jpeg')

# #第二个代码：裁剪图像，并以另一种格式存储
# from PIL import Image,ImageFilter
# im = Image.open('psb.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')

# #第三个代码：生成随机验证码
# from PIL import Image, ImageDraw,ImageFont,ImageFilter
# import random
#
# def rndChar():
#     return chr(random.randint(65,90))
#
# def rndColor():
#     return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#
# def rndColor2():
#     return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#
# width = 60*4
# height = 60
# image = Image.new('RGB',(width,height),(255,255,255))
# font = ImageFont.truetype('C:/WORK/ANACONDA3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/cmb10.ttf',36)
# draw = ImageDraw.Draw(image)
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rndColor())
# for t in range(4):
#     draw.text((60*t + 10,10),rndChar(),font=font,fill=rndColor2())
#
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg','jpeg')
