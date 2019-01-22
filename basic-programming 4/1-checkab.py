def checkAB(str):
    characters = list(str)
    indexA = []
    indexB = []
    if characters.count("a") and characters.count("b") != 0:
        for a in range(len(characters)):
            if characters[a] == "a":
                indexA.append(a)
            if characters[a] == "b":
                indexB.append(a)
        print(indexA, indexB)
    else:
        return False

# print(checkAB("lane borrowed"))
# print(checkAB("i am sick"))
# print(checkAB("you are boring"))
# print(checkAB("barbarian"))
print(checkAB("bacon and meat"))