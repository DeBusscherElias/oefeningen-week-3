def print_lijst_getallen(startwaarde, stapgrootte, aantal):
    stop = startwaarde + (stapgrootte * aantal)
    for getal in range(startwaarde, stop+1, stapgrootte):
        print(f"{getal}")

start = int(input('Geef een startwaardee >'))
stapgrootte = int(input('Per hoeveel wil je stijgen? >'))
aantal = int(input("Hoeveel getallen wil je zien? >"))

print_lijst_getallen(start, stapgrootte, aantal)
