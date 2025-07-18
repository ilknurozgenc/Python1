#Girilen metin boşluklardan parçalanıyor ve her parçanın tamamen noktalama
# işaretlerinden oluşup oluşmadığı kontrol ediliyor.
# Uygun kelimeler sayılıp sonuç ekrana yazılıyor
import string

def is_word(text):
    for char in text:
        if not char in string.punctuation:
            return True
    return False


def word_count(value, output=0):
    potential_words = value.split(" ")

    for word in potential_words:
        if is_word(word):
            output += 1

    return output


text = raw_input("Tell something: ")
print("Total words: {}".format(word_count(text)))