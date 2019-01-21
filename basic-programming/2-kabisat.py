tahun = int(input("Silahkan masukkan tahun: "))
if tahun % 4 == 0:
    if tahun % 100 != 0:
        print("tahun %d adalah tahun kabisat" % tahun)
    elif tahun % 100 == 0:
        if tahun % 400 == 0:
            print("tahun %d adalah tahun kabisat" % tahun)
        else:
            print("tahun %d bukan tahun kabisat" % tahun)
else:
    print("tahun %d bukan tahun kabisat" % tahun)
