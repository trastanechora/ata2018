def angkaPrima(angka):
    counter = 0
    for i in range(1, angka+1):
        if angka % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False

print(angkaPrima(1))
print(angkaPrima(3))
print(angkaPrima(7))
print(angkaPrima(6))
print(angkaPrima(23))