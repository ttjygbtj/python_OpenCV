import cv2
import numpy as np


wndName1="pic1"

i,j=0,0
src =cv2.imread("../lena.jpg",0)
rows,cols=src.shape[:2]

#在彩色图中
#src.item(行,列,通道值),
#src.itemset((行,列,原来的通道值),通道值的新值)
for i in range(10,100):
    for j in range(10,100):
        # src[i,j]=random.randint(0,255)#random.randint(0,255),从0-255中随机生成一个整型数
        src.itemset((i,j),255)

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)

cv2.waitKey(0)