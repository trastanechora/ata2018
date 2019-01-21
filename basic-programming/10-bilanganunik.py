def bilanganUnik(bil):
    listBilangan = ""
    for i in range(1, bil + 1):
        number = i
        for x in [2, 3, 5]:
            while number % x == 0:
                number = number / x
                if number == 1:
                    listBilangan = listBilangan + str(i) + " "
                    break
    print(listBilangan)

bilanganUnik(20)