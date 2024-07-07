#5.4 中值滤波
#中值滤波原理非常简单，假设有一个数组[1556789],取其中的中间值（即中位数）作为卷积后的结果值即可。中值滤波对胡椒噪音（也叫椒盐噪音）效果明显
#medianBlur(src,ksize[,dst])

import cv2
import numpy as np

pepper = cv2.imread('./pepper.png')

median_pepper = cv2.medianBlur(pepper,5)#这里的ksize即卷积核的大小为一个数字

cv2.imshow('median_pepper',np.hstack((pepper,median_pepper)))
cv2.waitKey(0)
cv2.destroyWindow()
#效果拔群！！！