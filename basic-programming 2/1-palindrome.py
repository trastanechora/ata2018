def palindrome(kata):
    kata2 = ""
    i = len(kata)-1
    while i > -1:
        kata2 = kata2 + kata[i]
        i -= 1

    if kata == kata2:
        return True
    else:
        return False

print(palindrome("katak"))
print(palindrome("blanket"))
print(palindrome("civic"))
print(palindrome("kasur rusak"))
print(palindrome("mister"))