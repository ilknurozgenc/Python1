import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int (input('1 ile {50} arasında bir tahmin yapın:  '))
        if guess< random_number:
            print("çok düşük, tekrar deneyin")

        elif guess > random_number:
            print("çok yüksek, tekrar deneyin")
    print("tebrikler doğru tahmin")
guess(50)
