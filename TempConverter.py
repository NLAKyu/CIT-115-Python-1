#Temp Converter HW
#1.Input / Conversion
sMsg = print("Kayla's Temperature Converter: " + '\n')
fTemp = float(input("Enter a temperature: "))
sTempScale = input("Is the temperature F for Fahrenheit or C for Celsius? ")

#3. Calculations
fFahrenheit = ((9.0 / 5.0) * fTemp) + 32
fCelsius = (5.0 / 9) * (fTemp - 32)

#4. Output
if (sTempScale != 'F' and sTempScale != 'C') and (sTempScale != 'f' and sTempScale != 'c'):
    print("You must enter F or C")
    raise SystemExit
if fTemp >= 100 and (sTempScale == 'C' or sTempScale == 'c'):
        print("Temperature cannot be > 100")
elif fTemp <= 100 and (sTempScale == 'C' or sTempScale == 'c'):
    print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}")
elif fTemp >= 212 and (sTempScale == 'F' or sTempScale == 'f'):
    print("Temperature cannot be > 212")
elif fTemp <= 212 and (sTempScale == 'F' or sTempScale == 'f'):
    print(f"The Celsius equivalent is: {fCelsius:.1f}")
