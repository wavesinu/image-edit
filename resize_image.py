import os
import cv2
from PIL import Image


with Image.open('/Users/wavesinu/Documents/WORKSPACE/Projects/image-edit/img_01.jpg') as img:
    img.save('/Users/wavesinu/Documents/WORKSPACE/Projects/image-edit/img_01_resized.jpg',quality=40)


a = cv2.imread('/Users/wavesinu/Documents/WORKSPACE/Projects/image-edit/img_01_resized.jpg')
if a is not None:
    cv2.imshow('display', a)
cv2.waitKey(0)
cv2.destoryAllWindows()