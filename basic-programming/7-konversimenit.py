def konversiMenit(menit):
    hour = str(int(menit / 60))
    minute = str(menit % 60)
    if int(minute) < 10:
        minute = "0" + minute
        
    return(hour + ":" + minute)

print(konversiMenit(63))
print(konversiMenit(124))
print(konversiMenit(53))
print(konversiMenit(88))
print(konversiMenit(120))