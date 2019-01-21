rows = int(input("Jika row = "))
y = rows
while y > 0:
    asteriks = 0
    for x in range(rows):
        asteriks = "*" * rows
    y -= 1

    print(asteriks)

