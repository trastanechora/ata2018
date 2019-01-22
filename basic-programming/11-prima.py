def primakah(n):
    pembagi = 0
    for i in range(1, n + 1):
        if n % i == 0:
            pembagi += 1
    if pembagi == 2:
        print("%d adalah bilangan prima" % n)
    else:
        print("%d adalah bukan bilangan prima" % n)

x = int(input("Masukkan angka: "))
primakah(x)