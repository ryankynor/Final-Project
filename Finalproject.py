"""
Ryan Kynor
Geostationary orbit calculator
"""
import math


deltav = 0
staticmass = input("What is the static mass of the rocket? ")
fuelmass = input("What is the mass of the fuel in the rocket? ")
thrustvelocity = input("What is the thrust velocity of the engine used in the rocket? ")

totalmass = fuelmass + staticmass


deltav = thrustvelocity * ln(totalmass/fuelmass)
print(math)




if deltav >= 13500:
    print("Yay! Your rocket made it to geostatonary orbit!")
else:
    print("Your rocket didn't make it to geostationary orbit.")
