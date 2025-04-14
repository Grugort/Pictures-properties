from exif import Image as Img
from PIL import Image, ImageDraw, ImageFont
import os
import math
# with open ('od.JPG', 'rb') as image_file:
#     my_image=Img(image_file)
# print(my_image.get_all())
# a=my_image.model
# b=my_image.make
# c=my_image.f_number
# d=my_image.focal_length
# print(a)
# image=Image.open("end.png")
# font=ImageFont.truetype("arial.ttf", 25)
# drawer=ImageDraw.Draw(image)
# drawer.text((500,500), a, font=font, fill='red')
# drawer.text((500,400), b, font=font, fill='red')
# image.save('new_img.png')
# image.show()
files=[]
files +=os.listdir()
png = []
for i in range (0, len(files)):
    if ".JPG" in files[i]:
        png.append(files[i])
sorted(png)


for i in range(0,len(png)):
    with open(png[i], 'rb') as image_file:
        my_image = Img(image_file)
    a = my_image.make
    b = "Model: " +my_image.model
    c = "F: "+ str(my_image.f_number)
    d = "F.Range: "+str(my_image.focal_length)
    f="Lens: "+str(my_image.lens_model)
    x=my_image.pixel_x_dimension
    y=my_image.pixel_y_dimension
    xy=math.sqrt(x**2+y**2)
    raz=xy/100
    xn=x-800
    yn=y-600
    image=Image.open(png[i])
    font=ImageFont.truetype("CHILLER.TTF", raz)
    drawer=ImageDraw.Draw(image)
    drawer.text((xn,yn), text=a, font=font,fill='red')
    drawer.text((xn,yn+50), text=b, font=font, fill='red')
    drawer.text((xn, yn+100), text=c, font=font, fill='red')
    drawer.text((xn, yn+150), text=d, font=font, fill='red')
    drawer.text((xn, yn+200), text=f, font=font, fill='red')
    #image.save(str(i)+'new_img.png')
    image.save(f'C:/Users/Сотрудник 052/Desktop/kartinki/itog/{i}new_img.png')

