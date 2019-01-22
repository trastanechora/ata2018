def cariMedian(arr):
    median = len(arr)
    if len(arr) % 2 == 0:
        hasil = 0
        median = int((median - 1) / 2)
        hasil = (arr[median] + arr[median + 1]) / 2
        return(hasil)
    else:
        median = int((median - 1) / 2)
        return(arr[median])

print(cariMedian((1, 2, 3, 4, 5)))
print(cariMedian((1, 3, 4, 10, 12, 13)))
print(cariMedian((3, 4, 7, 6, 10)))
print(cariMedian((1, 3, 3)))
print(cariMedian((7, 7, 8, 8)))