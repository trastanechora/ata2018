def primakah(n):
    pembagi = 0
    for i in range(1, n + 1):
        if n % i == 0:
            pembagi += 1
    if pembagi == 2:
        return True

def primaSebelumN(m):
    bilangan = m - 1
    while primakah(bilangan) != True:
        bilangan -= 1
    print("Bilangan primanya adalah %d" % bilangan)

x = int(input("Masukkan bilangan sembarang: "))
primaSebelumN(x)