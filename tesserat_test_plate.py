import cv2
from matplotlib import pyplot as plt 
import numpy as np
import imutils 
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"D:\studia\praca_dyplomowa\tesseract\tesseract.exe"
import glob
import time

folder_with_pic = glob.glob(r"D:\studia\praca_dyplomowa\pytorch_detect\yolov5\runs\detect\exp7\crops\LP\*")

points = 0
no_contur = 0

for file in folder_with_pic:

  start = time.time()
  img = cv2.imread(file)
  try: 

    data = pytesseract.image_to_string(img, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 8 --oem 3')
          
    str(data)

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