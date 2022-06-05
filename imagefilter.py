#Import required image modules
from PIL import Image, ImageFilter

#Import all the enhancement filter from pillow
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)



#Create image object
# img = Image.open('pa.png')

# resize_image = img.resize((round(img.size[0]*2), round(img.size[1]*2)))

# #Applying the blur filter
# img1 = resize_image.filter(DETAIL)
# img1.save('paa.png')
# img1.show()

def convertImage():
    img = Image.open("./na.png")
    img = img.convert("RGBA")
  
    datas = img.getdata()
  
    newData = []
  
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)
    img.save("./na1.png", "PNG")
    print("Successful")
  
convertImage()