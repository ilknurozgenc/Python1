#girilen değer kadar fibonacci sayıları üretir.
def fibonacci(n, output=[]):
    a, b = 1,1
    for i in range(n):
        a, b = b, a+ b
        output.append(str(a))

    return output
number= int(input("fibonacci sayısının uzunluğunu giriniz: "))

print("çözümleme: {}".format(",".join(fibonacci(number))))
