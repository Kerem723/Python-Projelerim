
print (" ")
print ("İstediğiniz kara milini km'ye çevirmek için önce mil değerini giriniz.")
print (" ")

mil = input ("mil: ")
print (" ")

if mil.find('.') == -1:
  mil = int(mil)      #Sizin girdiğiniz mil sayısında nokta yoksa mil değişkeninin type'ını int'e çevirir. Nokta yazmadıysanız tam sayıdır.
                   
  
elif mil.find('.0') != -1:
  mil = mil.replace(".0","")
  mil = int(mil)                #Sizin girdiğiniz mil sayısında .0 varsa .0 kısmını siler ve mil değişkeninin type'ını int'e çevirir.
                                  #Çünkü .0 yazdıysanız o bir tam sayıdır.
else:
  mil = float(mil)      #Yukarıdaki şartların sağlanmadığı her durumda sayınız küsüratlıdır ve mil sayınız bir float'a dönüştürülür.
  
km = mil*1.609344     #Yukarıda normalde str kabul edilen mil'i her halükarda bir sayı olarak tanımladığımız için...
                      #...burada mil'in başına int veya float yazmamız gerekmedi.


if str(km).find('.0') == -1:
    print (mil , " kara mili," , km , "km etmektedir.")     #km'ye çevrilen sayıda .0 yoksa küsüratlı sayıdır ve float olarak kalmaya devam eder.

else:
    print (mil , " kara mili," , int(km) , "km etmektedir.")    #Çarpım sonucu tam sayı ise int'e çevirerek yazar böylece yanında .0 yazmaz.

print (" ")
print ("Yazdığınız değer: " , mil , "mil") 


#SONUÇ: Size sorulan mil sayısının sonuna .0 dahi yazsanız tam sayı olduğu sürece printlerin hiçbir kısmında sayıların sonu .0 ile bitmez.
