from detect import run
import os

list = os.listdir(rf"D:\studia\praca_dyplomowa\pytorch_detect\yolov5\dane_pomiarowe\dane_kontrolne_101") # dir is your directory path

plates=run() #yolo engine

points = 0
pic = len(list)
for plate in plates:
    plate_name = plate[0].replace("_", "")
    predict_plate = "".join(plate[1]).lower()
    
    if plate_name == predict_plate:
        points += 1
        print(f"Nazwa pliku:         {plate_name}     Odczytana wartość:       {predict_plate}  ----------------------- zgadza się")
    else:
        print(f"Nazwa pliku:         {plate_name}     Odczytana wartość:       {predict_plate}")
        # print(f"Dobre rozpoznanie numer {points}")

print(f"Rozpoznano poprawnie {points} na {pic}")


#