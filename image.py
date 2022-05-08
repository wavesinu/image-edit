from PIL import Image
img = Image.open('gif/panda.gif')
print(img.size)
print(img.format)

# 이미지 잘라내기
xy = (100, 200, 600, 700) # (100, 200)~ (600, 700)
crop_img = img.crop(xy)
crop_img.show()

# 이미지 붙여넣기 
xy = (0, 0, 500, 500)
img.paste(crop_img, xy)  # xy에 자른 이미지를 병합한다. 
img.show()
