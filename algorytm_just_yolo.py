from detect import run
import os

plate_dir = r"D:\studia\praca_dyplomowa\pytorch_detect\yolov5\runs\detect\exp7\crops\LP"

list = os.listdir(plate_dir) # dir is your directory path

plates=run(source= plate_dir) #yolo engine

points = 0
pic = len(list)
for plate in plates:
    plate_name = plate[0].replace("_", "")
    predict_plate = "".join(plate[1]).lower()
    
    if plate_name == predict_plate:
        points += 1
        print(f"Nazwa pliku:         {plate_name}     Odczytana wartość:       {predict_plate} ")



    else:
        print(f"Nazwa pliku:         {plate_name}     Odczytana wartość:       {predict_plate} ------ bad")
        # print(f"Dobre rozpoznanie numer {points}")

print(f"Rozpoznano poprawnie {points} na {pic}")


#