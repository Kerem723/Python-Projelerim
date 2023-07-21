print (" ")
print ("Sizden 3 adet rakamsal değer girmeniz istenmektedir. Girdiğiniz değerlere göre ekranda en büyük ve en küçük değerler belirtilecektir. ") 
print (" ")

degisken1 = input ("1. Değer = ")
degisken2 = input ("2. Değer = ")
degisken3 = input ("3. Değer = ")
print (" ")

if degisken1>degisken2>degisken3:
  print ("En büyük değer: " , degisken1)

elif degisken1>degisken3>degisken2:
  print ("En büyük değer: " , degisken1)

elif degisken2>degisken1>degisken3:
  print ("En büyük değer: " , degisken2)

elif degisken2>degisken3>degisken1:
  print ("En büyük değer: " , degisken2)

else:
  print ("En büyük değer: " , degisken3)

if degisken1<degisken2<degisken3:
  print ("En küçük değer: " , degisken1)

elif degisken1<degisken3<degisken2:
  print ("En küçük değer: " , degisken1)

elif degisken2<degisken1<degisken3:
  print ("En küçük değer: " , degisken2)

elif degisken2<degisken3<degisken1:
  print ("En küçük değer: " , degisken2)

else:
  print ("En küçük değer: " , degisken3)