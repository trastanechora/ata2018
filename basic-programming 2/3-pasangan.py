def pasanganTerbesar(num):
    array = list(str(num))
    besar = 1
    for i in range(len(array)-1):
        nomor = array[i] + array[i+1]
        if int(nomor) > besar:
            besar = int(nomor)
    return(besar)

print(pasanganTerbesar(641573))
print(pasanganTerbesar(12783456))
print(pasanganTerbesar(910233))
print(pasanganTerbesar(71856421))
print(pasanganTerbesar(79918293))