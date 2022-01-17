import cv2
import os
from PIL import Image, ImageFilter
import numpy as np
image = 'DSC_5332'
img = f'/Users/maxwhite/PycharmProjects/masks/test-14-05-2021/{image}.jpg'
mask1_name = f'/Users/maxwhite/PycharmProjects/Results/u2net_results_hum_seg/{image}.png'
mask2_name = f'//Users/maxwhite/PycharmProjects/Results/u2net_results_their/{image}.png'

kernel = np.ones((10,10),np.uint8)
img = cv2.imread(img, cv2.IMREAD_ANYCOLOR)
size = (img.shape[1], img.shape[0])
mask1 = cv2.imread(mask1_name, cv2.IMREAD_ANYCOLOR)
mask2 = cv2.imread(mask2_name, cv2.IMREAD_ANYCOLOR)

th, im_th = cv2.threshold(mask1, 100, 255, cv2.THRESH_BINARY)
#im_th = mask1
#im_th = cv2.morphologyEx(im_th, cv2.MORPH_OPEN, kernel)
th1, im_th1 = cv2.threshold(mask2, 150, 255, cv2.THRESH_BINARY)
#im_th1 = mask2
im_th1 = cv2.morphologyEx(im_th1, cv2.MORPH_CLOSE, kernel)
im_th1 = cv2.erode(im_th1,kernel,iterations = 1)
#im_th = cv2.erode(im_th,kernel,iterations = 1)
#im_th1 = cv2.morphologyEx(im_th1, cv2.MORPH_OPEN, kernel)
#threshold = 50
# #matting *= (matting > threshold)
# #im_th = matting
cv2.imwrite(f'{os.path.splitext(mask1_name)[0]}_binarized.png', im_th)
cv2.imwrite(f'{os.path.splitext(mask2_name)[0]}_binarized1.png', im_th1)

#binarized = Image.open(f'{os.path.splitext(mask1_name)[0]}_binarized.png')
#binarized1 = Image.open(f'{os.path.splitext(mask2_name)[0]}_binarized1.png')
#binarized_smoothed = cv2.blur(im_th,(5,5),0)
#binarized_smoothed1 = cv2.blur(im_th1,(10,10),0)
#binarized_smoothed1 = cv2.erode(im_th1,kernel,iterations = 1)
#binarized_smoothed1 = cv2.bilateralFilter(binarized_smoothed1,17,100,100)
#binarized_smoothed = cv2.bilateralFilter(binarized_smoothed,17,100,100)

binarized_smoothed1 = im_th1
binarized_smoothed = im_th

#binarized_smoothed = binarized.filter(ImageFilter.ModeFilter(size=30))
#binarized_smoothed1 = binarized1.filter(ImageFilter.ModeFilter(size=30))

#binarized_smoothed.save(f'{os.path.splitext(mask1_name)[0]}_binarized_smoothed.png')
#binarized_smoothed1.save(f'{os.path.splitext(mask2_name)[0]}_binarized_smoothed1.png')
cv2.imwrite(f'{os.path.splitext(mask1_name)[0]}_binarized_smoothed.png', binarized_smoothed)
cv2.imwrite(f'{os.path.splitext(mask2_name)[0]}_binarized_smoothed1.png', binarized_smoothed1)

result_mask = cv2.imread(f'{os.path.splitext(mask1_name)[0]}_binarized_smoothed.png', cv2.IMREAD_GRAYSCALE)
result_mask1 = cv2.imread(f'{os.path.splitext(mask2_name)[0]}_binarized_smoothed1.png', cv2.IMREAD_GRAYSCALE)

#result_mask = cv2.resize(result_mask, size)
#result_mask1 = cv2.resize(result_mask1, size)

result = cv2.bitwise_and(img, img, mask=result_mask)
result1 = cv2.bitwise_and(img, img, mask=result_mask1)
#result1 = cv2.blur(result1,(5,5),10)

result[result_mask==0] = [255,255,255]
result1[result_mask1==0] = [255,255,255]

cv2.imwrite(f'{os.path.splitext(mask1_name)[0]}_final.png', result)
cv2.imwrite(f'{os.path.splitext(mask2_name)[0]}_final1.png', result1)

#os.remove(f'{os.path.splitext(f)[0]}_binarized.png')
# os.remove(f'{os.path.splitext(f)[0]}_binarized_smoothed.png')