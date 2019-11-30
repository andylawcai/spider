import pytesseract as pt
from PIL import Image
image=Image.open(r'C:\Users\andylawcai\Desktop\45.png')
# threshold = 200
# def erzhihua(image,threshold):
# ''':type image:Image.Image'''
image=image.convert('1')
#     table=[]
#     for i in range(256):
#         if i <  threshold:
#             table.append(0)
#         else:
#             table.append(1)
#             # print(len(table))
#     return image.point(table,'1')
# image_er=erzhihua(image,180)
image.show()

# print()
# text=pt.image_to_string(image_er)

# print(text)
