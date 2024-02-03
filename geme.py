from pengaturan_angka import *

while tebakan != jawaban:
    print("")
    print(petunjuk_1)
    print(petunjuk_2)
    print(petunjuk_3)
    print(petunjuk_4)
    print(petunjuk_5)
    tebakan = input('berapa jawabannya? ')
    if tebakan == "nyerah":
        print("payah lu...")
        break

else:
    print("anjay, pinter juga lu...")
    print("")
    print("")
    print("")
    print("")
    print("")