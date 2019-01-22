def tentukanDeretGeometri(arr):
    arr2 = []
    x = arr[1] / arr[0]
    number = arr[0]
    for i in range(len(arr)):
        arr2.append(number)
        number = arr[i] * int(x)
    if arr == arr2:
        return True
    else:
        return False
    
print(tentukanDeretGeometri([1, 3, 9, 27, 81]))
print(tentukanDeretGeometri([2, 4, 8, 16, 32]))
print(tentukanDeretGeometri([2, 4, 6, 8]))
print(tentukanDeretGeometri([2, 6, 18, 54]))
print(tentukanDeretGeometri([1, 2, 3, 4, 7, 9]))