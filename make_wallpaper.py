from PIL import Image, ImageFont, ImageDraw

img = Image.open('sample.jpg')

draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("Aaargh.ttf", 48)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((800, 500),"Sample Text",(255,255,255),font=font)
img.save('wallpaper.jpg')