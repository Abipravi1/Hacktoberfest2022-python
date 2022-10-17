#Program that calculates the pH of any solution.#

indice_acid = float(input())

while indice_acid != -1:
    if indice_acid < 7:
        print("ACIDA")
    if indice_acid == 7:
        print("NEUTRA")
    if indice_acid > 7:
        print("BASICA")
    indice_acid = float(input())
