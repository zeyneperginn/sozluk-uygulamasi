import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parolanın uzunluğu ne kadar olmalı?"))
sifre = ""
for i in range (uzunluk):
    sifre = random.choice(karakterler) + sifre
print(sifre)    
