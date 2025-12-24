n = int(input("Enter number: "))
octal = oct(n)[2:]
print(octal.zfill(10))






print("Octal representation (10 digits):", octal.zfill(10))