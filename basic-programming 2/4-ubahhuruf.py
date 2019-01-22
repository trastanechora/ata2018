def ubahHuruf(kata):
    # return(ord("a"), ord("z"))
    hasilGabung = ""
    listKata = list(kata)
    for i in range(len(listKata)):
        num = ord(listKata[i]) + 1
        hasilGabung = hasilGabung + chr(num)
    return(hasilGabung)

print(ubahHuruf("wow"))
print(ubahHuruf("developer"))
print(ubahHuruf("keren"))
print(ubahHuruf("semangat"))