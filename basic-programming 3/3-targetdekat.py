def targetTerdekat(arr):
    xnum = []
    onum = []
    palingKecil = 100
    if arr.count("x") != 0:
        for i in range(len(arr)):
            if arr[i] == "x":
                xnum.append(i)
            if arr[i] == "o":
                onum.append(i)
        for i in xnum:
            for y in onum:
                kecil = i - y
                if palingKecil > abs(kecil):
                    palingKecil = abs(kecil)
    else:
        palingKecil = 0
    return(palingKecil)

print(targetTerdekat([" ", " ", "o", " ", " ", "x", " ", "x"]))
print(targetTerdekat(["o", " ", " ", " ", "x", "x", "x"]))
print(targetTerdekat(["x", " ", " ", " ", "x", "x", "o", " "]))
print(targetTerdekat([" ", " ", "o", " "]))
print(targetTerdekat([" ", "o", " ", "x", "x", " ", " ", "x"]))