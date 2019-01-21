def balikkata(kata):
    data = list(kata)
    reversed_data = ""
    y = len(data)
    while y > 0:
        y -= 1
        reversed_data = reversed_data + data[y]
    return(reversed_data)

print(balikkata("Hello World and Coders"))
print(balikkata("John Doe"))
print(balikkata("I am a bookworm"))
print(balikkata("Coding id my hobby"))
print(balikkata("Super"))