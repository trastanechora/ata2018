def primakah(angka):
        counter = 0
        for i in range(1, angka+1):
                if angka % i == 0:
                        counter += 1
        if counter == 2:
                return True

def primaSegiEmpat(P, L, X):
        listPrima = []
        number = X 
        n = P * L
        total = 0
        for f in range(n):
                y = 0
                while y < 1:
                        number += 1
                        if primakah(number):
                                listPrima.append(number)
                                y += 1
                                total += number
        indx = 0
        abc = ""
        for a in range(len(listPrima)):
                indx += 1
                abc = abc + " " + str(listPrima[a])
                if indx == P:
                        abc = abc + "\n"
                        indx = 0
        print(abc)
        print("Total: %d" % total)

primaSegiEmpat(2, 3, 13)
primaSegiEmpat(5, 2, 1)
