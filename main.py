sozluk = {
    "Esef" : "Olmaması, yaplmaması gereken veya yapılmayan bir şey için duyulan üzüntü.",
    "LOL": "Komik bir şeye verilen cevap"
    
    }
print(*sozluk)
kullanici_istek = input("Hangi kelimenin anlamını öğrenmek istiyorsunuz?")
if kullanici_istek in sozluk.keys():
    print("Girdiğiniz kelimenin anlamı: ",sozluk[kullanici_istek])
else:
        print("Bu kelime sözlükte bulunmuyor!")

