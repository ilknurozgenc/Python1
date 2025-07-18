decimal=int(input("decimal bir sayı giriniz: "))

def binarry(n):
    output= " "
    while n >0:
        output= " {} {}".format(n % 2, output)
        n= n // 2
    return output

print(binarry(decimal))

print(bin(decimal)[2:])

print("{0: b}".format(decimal))