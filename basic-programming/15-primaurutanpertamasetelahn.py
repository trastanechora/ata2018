def primakah(n):
    pembagi = 0
    for i in range(1, n + 1):
        if n % i == 0:
            pembagi += 1
    if pembagi == 2:
        return True

def urutan3PrimaSetelah(m):
    listPrima = []
    bilangan = m + 1
    for j in range(3):
        while primakah(bilangan) != True:
            bilangan += 1
        listPrima.append(bilangan)
        bilangan += 1

    print(listPrima)

x = int(input("Masukkan bilangan sembarang: "))
urutan3PrimaSetelah(x)