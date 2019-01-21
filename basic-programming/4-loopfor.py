first = " - I love coding"
second = " - I will become fullstack developer"

n = 0

print("LOOPING PERTAMA")
for x in range(10):
    n += 2
    number = str(n)
    print(number + first)

n += 2

print("LOOPING KEDUA")
for x in range(10):
    n -= 2
    number = str(n)
    print(number + second)