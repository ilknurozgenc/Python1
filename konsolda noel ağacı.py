yükseklik= int(input(" noel ağacının yüksekliğini giriniz: "))

for i in range(int(yükseklik* 0.7)):
     print( (" "* (yükseklik - (i // 2))) + ("* "* i))

for i in range(int(yükseklik* 0.7), yükseklik):
     print((" " * (yükseklik - 1)) + " || ")
