start = 200
stop = 308

for getal in range(start, stop+1):
    if getal % 7 == 0 and getal % 5 != 0:
        print(f"{getal}")