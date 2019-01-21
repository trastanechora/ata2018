def faktorBilangan(angka):
    x = angka
    hasil = []
    bilanganFaktor = ""

    while x > 0:
        if angka % x == 0:
            hasil.append(x)
        x -= 1

    for h in hasil:
        bilanganFaktor = bilanganFaktor + " " + str(h)
        
    print(bilanganFaktor)

faktorBilangan(6)
faktorBilangan(12)
faktorBilangan(14)
faktorBilangan(16)
faktorBilangan(20)