#Program that calculates the measures of the sides of a right triangle using the Pythagorean formula.#

import math

cateto1 = float(input())
cateto2 = float(input())

hipotenusa =  math.sqrt(cateto1**2 + cateto2**2)

print("%.2f" % hipotenusa)
