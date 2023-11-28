import random
import os
qwe = ["tas","kagit","makas"]
sen = 0
pc = 0
zort = "tas,kagit,makas oyunu"
print(zort)
while True:
    if pc == 3:
        print("sen:{} pc:{}".format(sen,pc),end="\n\n")
        print("\t\t\t\t\t"+"KAYBETTIN")
        tekrar = input("tekrar oynamak istermisin?: ")
        if tekrar == "evet":
            pc = 0
            sen = 0
            os.system("cls")
            print(zort)
        else:
            break
    elif sen == 3:
        print("sen:{} pc:{}".format(sen,pc),end="\n\n")
        print("\t\t\t\t\t"+"---KAZANDIN---")
        tekrar = input("tekrar oynamak istermisin?: ")
        if tekrar == "evet":
            pc = 0
            sen = 0
            os.system("cls")
            print(zort)
        else:
            break
    islem1 = input("seciniz!(tas,kagit,makas): ")
    islem2 = random.choice(qwe)
    if islem1 == islem2:
        print("sen:{} pc:{} berabere!".format(islem1,islem2),end="\n\n")
    elif (islem1 == "tas" and islem2 == "makas") or (islem1 == "kagit" and islem2 == "tas") or (islem1 == "makas" and islem2 == "kagit"):
        print("sen:{} pc:{} sana 1 puan".format(islem1,islem2),end="\n\n")
        sen == sen + 1
    elif (islem1 == "makas" and islem2 == "tas") or (islem1 == "tas" and islem2 == "kagit") or (islem1 == "kagit" and islem2 == "makas"):
        print("sen:{} pc:{} pcye 1 puan".format(islem1,islem2),end="\n\n")
        pc == pc + 1
