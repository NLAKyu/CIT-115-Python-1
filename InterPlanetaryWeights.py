#Inter Planetary Weights HW

# 1. Constants
MERCURY_SGF = 0.38
VENUS_SGF = 0.91
MOON_SGF = 0.165
MARS_SGF = 0.38
JUPITER_SGF = 2.34
SATURN_SGF = 0.93
URANUS_SGF = 0.92
NEPTUNE_SGF = 1.12
PLUTO_SGF = 0.066

# 2. Inputs, the users name & weight
sName = input("What is your name: ")
nEarthWeight = float(input("What is your weight: "))

# 3. Calculations user's earth weight * SGF's
fMercuryWt = nEarthWeight * MERCURY_SGF
fVenusWt = nEarthWeight * VENUS_SGF
fMoonWt = nEarthWeight * MOON_SGF
fMarsWt = nEarthWeight * MARS_SGF
fJupiterWt = nEarthWeight * JUPITER_SGF
fSaturnWt = nEarthWeight * SATURN_SGF
fUranusWt = nEarthWeight * URANUS_SGF
fNeptuneWt = nEarthWeight * NEPTUNE_SGF
fPlutoWt = nEarthWeight * PLUTO_SGF

#4. Output
print(f"{sName} here are your weights on our Solar System's planets:")
print(f"{'Weight on Mercury:':21} {fMercuryWt:10.2f}")
print(f"{'Weight on Venus:':21} {fVenusWt:10.2f}")
print(f"{'Weight on our Moon:':21} {fMoonWt:10.2f}")
print(f"{'Weight on Mars:':21} {fMarsWt:10.2f}")
print(f"{'Weight on Jupiter:':21} {fJupiterWt:10.2f}")
print(f"{'Weight on Saturn:':21} {fSaturnWt:10.2f}")
print(f"{'Weight on Uranus:':21} {fUranusWt:10.2f}")
print(f"{'Weight on Neptune:':21} {fNeptuneWt:10.2f}")
print(f"{'Weight on Pluto:':21} {fPlutoWt:10.2f}")
