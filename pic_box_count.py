import os
from re import X
import sys
import glob
import cv2

def getPicSize(picName): # pic name in str type 
  img = cv2.imread(f"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\zdjecia_walidacyjne\{picName}.jpg")
  height, width, channels = img.shape
  return width, height

def getYoloList(file):
  yolo = f"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\labels_yolo\{file}.txt"
  with open(yolo) as fy:
    list_of_yolo_lines = fy.readlines()
  return list_of_yolo_lines

def getHumanList(file):
  yolo = f"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\labels_human\{file}.txt"
  with open(yolo) as f:
    list_of_human_lines = f.readlines()
  return list_of_human_lines

def xywhToxyxy(listXywh):
  x,y,w,h = listXywh
  x1 = x - (w/2)   # top left
  y1 = y - (h/2)
  x2 = x + (w/2)    # botton right
  y2 = y + (h/2)

  # x1 = x + (w/2)   # botton left
  # y1 = y - (h/2)
  # x2 = x - (w/2)    # top right
  # y2 = y + (h/2)


  return x1,y1,x2,y2 


def countBox(humanList, yoloList, xPic, yPic, picName):
  class_human, x_human, y_human, w_human, h_human = humanList
  class_yolo, x_yolo, y_yolo, w_yolo, h_yolo = yoloList

  h_human.replace('\n',"")
  h_yolo.replace('\n',"")

  x_human = float(x_human) * xPic
  x_yolo = float(x_yolo) * xPic

  y_human = float(y_human) * yPic
  y_yolo = float(y_yolo) * yPic

  w_human = float(w_human) * xPic
  w_yolo = float(w_yolo) * xPic

  h_human = float(h_human) * yPic
  h_yolo = float(h_yolo) * yPic

  # print(x_human, x_yolo, y_human, y_yolo, w_human, w_yolo, h_human, h_yolo)

  xywh_human = x_human, y_human, w_human, h_human
  xywh_yolo = x_yolo, y_yolo, w_yolo, h_yolo

  # print(f"to jest pole kwadratu humana czerwony box {w_human*h_human}")

  x1h,y1h,x2h,y2h = xywhToxyxy(xywh_human)
  x1y,y1y,x2y,y2y = xywhToxyxy(xywh_yolo)




  img = cv2.imread(f"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\zdjecia_walidacyjne\{picName}.jpg")

  start_pointy = (int(x1y), int(y1y))
  end_pointy = (int(x2y), int(y2y))
  thickness = 2

  start_pointh = (int(x1h), int(y1h))
  end_pointh = (int(x2h), int(y2h))
  thickness = 2
  # image = cv2.circle(img, (int(x1), int(y1)), radius=2, color=(0, 0, 255), thickness=-1)
  # image = cv2.circle(img, (int(x2), int(y2)), radius=2, color=(255, 0, 0), thickness=-1)
  img = cv2.rectangle(img, start_pointh, end_pointh, (255, 0, 0), thickness)
  img = cv2.rectangle(img, start_pointy, end_pointy, (0, 0, 255), thickness)

  # cv2.imshow('img',img)
  # cv2.waitKey(0)

  
  ra = (x1y, y1y, x2y, y2y)
  rb = (x1h, y1h, x2h, y2h)

  l1 = [x1y, y1y]
  r1 = [x2y, y2y]
  l2 = [x1h, y1h]
  r2 = [x2h, y2h]

  def overlappingArea(l1, r1, l2, r2):
    x = 0
    y = 1
 
    # Area of 1st Rectangle
    area1 = abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])
 
    # Area of 2nd Rectangle
    area2 = abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])
 
    ''' Length of intersecting part i.e 
        start from max(l1[x], l2[x]) of 
        x-coordinate and end at min(r1[x],
        r2[x]) x-coordinate by subtracting 
        start from end we get required 
        lengths '''
    x_dist = (min(r1[x], r2[x]) -
              max(l1[x], l2[x]))
 
    y_dist = (min(r1[y], r2[y]) -
              max(l1[y], l2[y]))
    areaI = 0
    if x_dist > 0 and y_dist > 0:
        areaI = x_dist * y_dist
 
    result = float((area1 + area2 - areaI))
    return result


  # print(f" pole: {overlappingArea(l1, r1, l2, r2)}")

  overlap_field = (overlappingArea(l1, r1, l2, r2))
  human_filed = (w_human*h_human)
  filed = (human_filed * 100 / overlap_field)
  # print(f"wartość procentowa nakładania się decyzji ludzkiej i yolo {filed}")
  print(f"{filed}")

  return x_human, x_yolo, y_human, y_yolo, w_human, w_yolo, h_human, h_yolo


pic = rf"D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\zdjecia_walidacyjne\*.jpg"
folderHum = rf'D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\labels_human\*.txt'
folderYolo = rf'D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\zdjecia_walidacyjne\labels_yolo\*.txt'

listOfHumanBox = glob.glob(folderHum)
listOfYolobox = glob.glob(folderYolo)
listOfPic = glob.glob(pic)

for file in listOfHumanBox: # tutaj mamy jeden notatnik człowieka
  basename = os.path.basename(file)
  # print(basename)
  fileName = basename.split(".")
    
  xPic, yPic = getPicSize(fileName[0]) # tu mamy x i y foty tego pliku 
  listYoloElement = getYoloList(fileName[0])
  listHumanElement = getHumanList(fileName[0])
  # print(basename, xPic, yPic, listHumanElement, listYoloElement)
  for lineHuman in listHumanElement:
    lineHuman = lineHuman.split(" ")
    humanClass = lineHuman[0]
    for lineYolo in listYoloElement:
      lineYolo = lineYolo.split(" ")
      yoloClass = lineYolo[0]
      if yoloClass == humanClass:
        # print(f"mam takie same linijki human {lineHuman} oraz yolo {lineYolo}")
        x_human, x_yolo, y_human, y_yolo, w_human, w_yolo, h_human, h_yolo = countBox(lineHuman, lineYolo, xPic, yPic, fileName[0])
        # print(x_human, x_yolo, y_human, y_yolo, w_human, w_yolo, h_human, h_yolo)
        break
      else:
        continue
  # tu mamy iterowanie plik po pliku i mamy do roboty 2 listy 