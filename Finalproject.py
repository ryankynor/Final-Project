"""
Ryan Kynor
Geostationary orbit calculator
"""
import math


deltav = 0

#parameters of rocket
staticmass = int(input("What is the dry mass of the rocket in kg? "))
fuelmass = int(input("What is the mass of the fuel in the rocket in kg? "))
thrustvelocity = int(input("What is the thrust velocity of the engine used in the rocket in meters per second? "))


#calculating the total mass of the rocket in kg
totalmass = fuelmass + staticmass


#calculation
deltav = thrustvelocity * math.log(totalmass/staticmass)


if deltav >= 13500:
    print("Yay! Your rocket made it to geostatonary orbit!")
    print("Your Delta-V was {0}",deltav)
    print("You need 13,500 meters per second of acceleration to reach geostationary orbit.")
else:
    print("Your rocket didn't make it to geostationary orbit.")
    print("Your Delta-V was {0}",deltav)
    print("You need 13,500 meters per second of Delta-V to reach geostationary orbit.")
    
    
#program written with idea of optimal orbital trajectory and average amount of aerodynamics



