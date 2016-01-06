"""
Ryan Kynor
Geostationary orbit calculator
"""
import math


deltav = 0
staticmass = int(input("What is the static mass of the rocket in kg? "))
fuelmass = int(input("What is the mass of the fuel in the rocket in kg? "))
thrustvelocity = int(input("What is the thrust velocity of the engine used in the rocket in meters per second? "))

totalmass = fuelmass + staticmass


deltav = thrustvelocity * math.log(fuelmass/totalmass)





if deltav >= 13500:
    print("Yay! Your rocket made it to geostatonary orbit!")
    print("Your Delta-V was {0}",deltav)
    print("You need 13,500 meters per second of acceleration to reach geostationary orbit.")
else:
    print("Your rocket didn't make it to geostationary orbit.")
    print("Your Delta-V was {0}",deltav)
    print("You need 13,500 meters per second of acceleration to reach geostationary orbit.")
