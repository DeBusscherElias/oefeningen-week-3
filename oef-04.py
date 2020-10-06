start = 10 
stop = 129

tekst = ""

if start % 2 != 0:
    start += 1

for getal in range(start+2, stop + 1, 2):
    tekst = f"{tekst} - {getal}"

print(f"{tekst}")