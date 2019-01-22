def perkalianUnik(arr):
    arr2 = []
    for i in range(len(arr)):
        hasil = 1
        for j in range(len(arr)):
            if i != j:
                hasil = hasil * arr[j]
        arr2.append(hasil)
    return(arr2)

print(perkalianUnik([2, 4, 6]))
print(perkalianUnik([1, 2, 3, 4, 5]))
print(perkalianUnik([1, 4, 3, 2, 5]))
print(perkalianUnik([1, 3, 3, 1]))
print(perkalianUnik([2, 1, 8, 10, 2]))