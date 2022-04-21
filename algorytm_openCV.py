import cv2
from matplotlib import pyplot as plt 
import numpy as np
import imutils 
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"D:\studia\praca_dyplomowa\tesseract\tesseract.exe"
import glob
import time

folder_with_pic = glob.glob(r"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\dane_kontrolne_1000\*")

points = 0
no_contur = 0

for file in folder_with_pic:

  start = time.time()
  img = cv2.imread(file)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # cv2.imshow('1', gray)
  # cv2.waitKey(0)

  bfilter = cv2.bilateralFilter(gray, 11, 17, 17) # noise reduction 
  edged = cv2.Canny(bfilter, 30, 200) # Edge detection
  # cv2.imshow('2',edged)
  # cv2.waitKey(0)

  keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  contours = imutils.grab_contours(keypoints)
  contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

  location = None
  for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
      location = approx 
      break 

  try:
      
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow('3',new_image)
    # cv2.waitKey(0)

    (x,y) = np.where(mask==255)
    (x1,y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))

    cropped_image = gray[x1:x2+1, y1:y2+1]

    # cv2.imshow('3',cropped_image)
    # cv2.waitKey(0)

    data = pytesseract.image_to_string(cropped_image, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 8 --oem 3')
          
    str(data)

    # cv2.imshow('1', gray)
    # cv2.imshow('2',edged)
    # cv2.imshow('3',new_image)
    # cv2.imshow('4',cropped_image)
    # cv2.waitKey(0)

    file_name = file.split("\\")
    plate = file_name[-1]
    just_plate = plate.split(".")
    plate_name = just_plate[0].replace("_", "")
    my_data = data.rstrip("\n")
    predict_plate = my_data.lower()
    end = time.time()
    final_time = str(round(end-start, 3))
    if plate_name == predict_plate:
      points += 1
      print("Orginalna tablica:",plate_name,"\t\t\t","Odczytana wartość:",predict_plate,"\t\t\t","czas:",final_time,"---good")

    else:
      print("Orginalna tablica:",plate_name,"\t\t\t","Odczytana wartość:",predict_plate,"\t\t\t","czas:",final_time)
          # print(f"Dobre rozpoznanie numer {points}")
  
  except:
    no_contur+=1
    pass


print(f"Rozpoznano poprawnie {points} na {len(folder_with_pic)} pominięto {no_contur}")