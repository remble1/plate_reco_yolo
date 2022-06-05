import os
import sys
import glob

filePath = rf'D:\studia\praca_dyplomowa\pytorch_detect\dane_pomiarowe\dane_do_uczenia\DATASET_ALL\DATASET_ALL\labels\*.txt'
folder = glob.glob(filePath)
result = []

list15 = 0
list16 = 0 
list17 = 0 
list18 = 0 
list19 = 0 
list20 = 0
list21 = 0 
list22 = 0
list23 = 0 
list24 = 0
list25 = 0 
list26 = 0
list27 = 0 
list28 = 0
list29 = 0 
list30 = 0
list31 = 0 
list32 = 0
list33 = 0 
list34 = 0
list35 = 0
list36 = 0 
list37 = 0
list38 = 0 
list39 = 0
list40 = 0 
list41 = 0
list42 = 0
list43 = 0
list44 = 0 
list45 = 0
list46 = 0 
list47 = 0
list48 = 0
list49 = 0 
list50 = 0
list51 = 0 
list52 = 0
list53 = 0


for file in folder:
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            lineList = list(line.split(" "))
            # print(lineList)
            
            try:
                if int(lineList[0]) == 15:
                    list15+=1
                if int(lineList[0]) == 16:
                    list16+=1
                if int(lineList[0]) == 17:
                    list17+=1
                if int(lineList[0]) == 18:
                    list18+=1                
                if int(lineList[0]) == 19:
                    list19+=1
                if int(lineList[0]) == 20:
                    list20+=1
                if int(lineList[0]) == 21:
                    list21+=1
                if int(lineList[0]) == 22:
                    list22+=1
                if int(lineList[0]) == 23:
                    list23+=1
                if int(lineList[0]) == 24:
                    list24+=1
                if int(lineList[0]) == 25:
                    list25+=1
                if int(lineList[0]) == 26:
                    list26+=1
                if int(lineList[0]) == 27:
                    list27+=1
                if int(lineList[0]) == 28:
                    list28+=1
                if int(lineList[0]) == 29:
                    list29+=1
                if int(lineList[0]) == 30:
                    list30+=1
                if int(lineList[0]) == 31:
                    list31+=1
                if int(lineList[0]) == 32:
                    list32+=1
                if int(lineList[0]) == 33:
                    list33+=1
                if int(lineList[0]) == 34:
                    list34+=1
                if int(lineList[0]) == 35:
                    list35+=1
                if int(lineList[0]) == 36:
                    list36+=1
                if int(lineList[0]) == 37:
                    list37+=1
                if int(lineList[0]) == 38:
                    list38+=1
                if int(lineList[0]) == 39:
                    list39+=1
                if int(lineList[0]) == 40:
                    list40+=1
                if int(lineList[0]) == 41:
                    list41+=1
                if int(lineList[0]) == 42:
                    list42+=1
                if int(lineList[0]) == 43:
                    list43+=1
                if int(lineList[0]) == 44:
                    list44+=1
                if int(lineList[0]) == 45:
                    list45+=1
                if int(lineList[0]) == 46:
                    list46+=1
                if int(lineList[0]) == 47:
                    list47+=1
                if int(lineList[0]) == 48:
                    list48+=1
                if int(lineList[0]) == 49:
                    list49+=1
                if int(lineList[0]) == 50:
                    list50+=1
                if int(lineList[0]) == 51:
                    list51+=1
                if int(lineList[0]) == 52:
                    list52+=1
                if int(lineList[0]) == 53:
                    list53+=1
            except:
                print(f"jakaś lipa {lineList[0]}")



            try:
                if int(lineList[0]) > 52:
                    result.append({file})
                    # print(f"znaleziono błąd w {file}")
                    # del line
                    break
                else:
                    pass
            except:
                print(f"Sprawdzić plik: {file}")
                pass
print(
list15,
list16,
list17,
list18,
list19,
list20,
list21,
list22,
list23,
list24,
list25,
list26,
list27,
list28,
list29,
list30,
list31,
list32,
list33,
list34,
list35,
list36,
list37,
list38,
list39,
list40,
list41,
list42,
list43,
list44,
list45,
list46,
list47,
list48,
list49,
list50,
list51,
list52,
list53
)

