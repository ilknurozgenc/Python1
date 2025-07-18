import random

kelimeler = ["kedi", "kumsal", "çoban", "baklava", "balina", "kan", "ampul", "orman", "lojman", "alışveriş"]
secilen_kelime = random.choice(kelimeler)
gecerliharfler = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
toplamhak = 5
yapilantahmin = ""
dosyay_kontrol_et_yoksa_olustur= ""


# Oyun görselleri
ADAM_ASMACA_GORSLLERI =
    """
      --------
      |    |
      |
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   /
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   / \
      |
    """[
]

print(" adam asmaca oyunumuza hoşgeldiniz :) ")
while toplamhak>0:
    gercekkelime= ""
    for harf in secilen_kelime:
        if harf in yapilantahmin:
           gercekkelime += harf
        else:
            gercekkelime += "_"

    if gercekkelime == secilen_kelime:
        print(gercekkelime)
        print("tebrikler kazandınız!")
        break

    print(ADAM_ASMACA_GORSLLERI[5-toplamhak])
    print("bir tahmin yapın", gercekkelime)
    print(f"kalan hakkınız ", {toplamhak})

    tahmin= input("bir harf tahmin ediniz: ").lower()

    if tahmin in gecerliharfler:
        yapilantahmin += tahmin
        if tahmin not in secilen_kelime:
            toplamhak -= 2

    else:
        print("lütfen geçerli bir harf tahmin ediniz: ")

else:

    print("malesef kaybettiniz doğru kelime: ", secilen_kelime)






