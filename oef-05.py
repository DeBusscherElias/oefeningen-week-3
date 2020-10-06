start = 99
stop = 0
if start % 2 == 0:
    start -= 1

for getal in range(start, stop-1, -3):
    if getal % 2 != 0:
        print(f"{getal}")
