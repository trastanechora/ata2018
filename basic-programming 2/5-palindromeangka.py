def cekPalindrome(toBeChecked):
    n = toBeChecked
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if(rev == temp):
        return True
        
def angkaPalindrome(num):
    nomor = num + 1
    while cekPalindrome(nomor) != True:
        nomor += 1
    return(nomor)

print(angkaPalindrome(8))
print(angkaPalindrome(10))
print(angkaPalindrome(117))
print(angkaPalindrome(175))
print(angkaPalindrome(1000))
print(angkaPalindrome(218))