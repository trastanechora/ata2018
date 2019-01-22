def primakah(n):
    pembagi = 0
    for i in range(1, n + 1):
        if n % i == 0:
            pembagi += 1
    if pembagi == 2:
        return True

def urutanPrima(m):
    listPrima = []
    for f in range(m):
        bilangan = f
        if primakah(bilangan) == True:
            listPrima.append(bilangan)
    print(listPrima)

x = int(input("Masukkan bilangan sembarang: "))
urutanPrima(x)