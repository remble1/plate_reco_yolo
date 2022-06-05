import os
from re import X
import sys
import glob
import cv2







# zapisanie w zmiennych parametrów danej klasy 
# z xywh na xyxy 
# obliczenie nakładania się kwadratów 


def picSize(picName): # pic name in str type 
  img = cv2.imread(f"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\zdjecia_walidacyjne\{picName}.jpg")
  height, width, channels = img.shape
  return width, height

def xywhToXyxy(x,y,w,h): # value in px! 
  x1 = x - w/2
  y1 = y - h/2
  x2 = x + w/2
  y2 = y + h/2
  return [x1,y1,x2,y2]

def scaleToPix(xywh, picX, picY):
  x = xywh[0]
  y = xywh[1]
  w = xywh[2]
  h = xywh[3]

  xInPix = x*picX
  yInPix = y*picY
  wInPix = w*picX
  hInPix = h*picY
  
  return [xInPix,yInPix,wInPix,hInPix] # in pixels 


def countFieldBox(humanBox, yoloBox):
  # print(f"{humanBox} to są dane człowieka, {yoloBox} to są dane YOLO")
  obj_class_h, xh, yh, wh, hh = humanBox
  obj_class_y, xy, yy, wy, hy = yoloBox
  xywhHuman = xh, yh, wh, hh
  xywhYolo = xy, yy, wy, hy
  return xywhHuman, xywhYolo
  

pic = rf"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\zdjecia_walidacyjne\*.jpg"
folderHum = rf'D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\labels_human\*.txt'
folderYolo = rf'D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\labels_yolo\*.txt'

listOfHumanBox = glob.glob(folderHum)
listOfYolobox = glob.glob(folderYolo)
listOfPic = glob.glob(pic)
result = []
for file in listOfHumanBox: # tutaj mamy jeden notatnik z listy człowieka
  basename = os.path.basename(file)
  # print(basename)
  fileName = basename.split(".")
    
  xHuman, yHuman = picSize(fileName[0])
  with open(file) as f:   
      lines = f.readlines()  # all line 
      for line in lines: # tutaj mamy jedną linie ############################################################
        # print(line)
        singleLineHumanList = line.split(" ") # tu ją splitniemy  #################################################333
        # print(singleLineHumanList[-1])
        # print(f"{singleLineHumanList[0]}, human choose in {fileName[0]} ")
        # here i have one class human decision 
        for fileYolo in listOfYolobox: # tutaj bierzemy jeden plik txt yolo 
          # print(f"plik ludzki {file}, plik yolo {fileYolo}") # a tu sprawdzmy czy na pewno mamy plik taki sam yolo i humana

          with open(fileYolo) as fy: 
            linesYolo = fy.readlines()
            for lineY in linesYolo: # tutaj szukamy jednej linijki z yolo takiej samej jak w human
              singleLineYoloList = lineY.split(" ")
              # print(singleLineYoloList[0])
              if singleLineHumanList[0] == singleLineYoloList[0]:
                print(f"human: {singleLineHumanList}, yolo: {singleLineYoloList}") # tu coś zrób tutaj przelicz te boxy



                break
              else:
                print(f"problem ze znalezieninem box-ow")
                continue
        break      
      xywhHuman, xywhYolo = countFieldBox(singleLineHumanList, singleLineYoloList)
      fix, fiy, fiw, fih = scaleToPix(xywhHuman, xHuman, yHuman)
      # print(fix, fiy, fiw, fih)
          

            
      
      break









#             lineList = list(line.split(" "))
#             try:
#                 if int(lineList[0]) > 52:
#                     result.append({file})
#                     # print(f"znaleziono błąd w {file}")
#                     # del line
#                     break
#                 else:
#                     pass
#             except:
#                 print(f"Sprawdzić plik: {file}")
#                 pass
# print(result)