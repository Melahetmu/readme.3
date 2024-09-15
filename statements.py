#Tapsiriq1
a = 70 

if a < 18: 
    print("Siz hələ az yaşlısız")

elif 18 <= a <= 65:
    print("Siz hele yetkinsiniz")

else: 
    print("Siz pensionersiz.")



#Tapsiriq2
a = 100

if 90 < a <=100:
    print("Siz 'A' almisiz")
    

elif 80 < a <=90:
    print("Siz 'B' almisiz")

elif 70 < a <=80:
    print ("Siz 'C' almisiz")

elif 60 < a <=70:
    print ("Siz 'D' almisiz")

elif 50 < a <=60:
    print ("Siz 'E' almisiz")

else:
    print("Siz 'F' almisiz")



#Tapsiriq3

b = 34

if b < 0:
    print("The weather is cold")

elif 0 < b < 20:
    print("The weather is cool")

elif 20 < b < 30:
    print("The weather is warm today")

else:
    print("The weather is hot")



#Tapsiriq4

a = 0

if a < 0:
    print("Eded menfidir.")

elif a > 0:
    print("Eded musbetdir")

else:
    print("Eded 0-a beraberdir")



 #Tapsiriq5

ad = 'admin'
parol = 1294

if ad == 'admin' and parol == 1234:
    print("Sistemə uğurla daxil oldunuz")

elif ad != 'admin' and parol == 1234:
    print("İstifadəçi adı yanlışdır")

else:
    print("Parol yanlışdır.")


#Tapsiriq6

a = 1

if a == 1:
    print("Menyu 1 seçildi")

elif a == 2:
    print("Menyu 2 seçildi")

elif a == 3:
    print("Menyu 3 seçildi")

else:
    print("Yanlış seçim")



#Tapsiriq7

b = 7

if b == 1:
    print("Monday")

elif b == 2:
    print("Tuesday")

elif b == 3:
    print("Wednesda")

elif b == 4:
    print("Thursday")

elif b == 5:
    print("Friday")

elif b == 6:
    print("Saturday")

elif b == 7:
    print("Sunday")

else:
    print("Wrong number")


#Tapsiriq8

saat = 4

if  6 < saat < 12:
    print("seher")

elif 12 < saat < 18:
    print("gunorta")

elif 18 < saat < 24:
    print("axsham")

else:
    print("gece")