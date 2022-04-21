import cv2
from matplotlib import pyplot as plt 
import numpy as np
import imutils 

img = cv2.imread(r'D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\dane_kontrolne_1\mario.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

bfilter = cv2.bilateralFilter(gray, 11, 17, 17) # noise reduction 
edged = cv2.Canny(bfilter, 30, 200) # Edge detection
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
  approx = cv2.approxPolyDP(contour, 10, True)
  if len(approx) == 4:
    location = approx 
    break 

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
cor_to_list = location.tolist()

print(cor_to_list)

from PIL import Image

plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
LT = cor_to_list[3][0]
LB = cor_to_list[0][0]
RT = cor_to_list[2][0]
RB = cor_to_list[1][0]
print(LT,LB,RT,RB)

x, y = LT # 113, 174 
h = 210-174
w = 233-103

pic_to_reco = new_image[y:y+h, x:x+w]

plt.imshow(cv2.cvtColor(pic_to_reco, cv2.COLOR_BGR2RGB))

plt.imshow(cv2.cvtColor(pic_to_reco))