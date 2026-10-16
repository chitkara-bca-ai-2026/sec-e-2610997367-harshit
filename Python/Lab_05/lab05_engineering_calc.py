import math

print("=" * 45)
print("       ENGINEERING CALCULATION TOOL")
print("=" * 45)

value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal = float(input("Enter a decimal measurement: "))

print("\n--- Results ---")
print(f"Value                 : {value}")
print(f"Exponent              : {exponent}")
print(f"Power (pow)           : {pow(value, exponent)}")
print(f"Square Root (sqrt)    : {math.sqrt(value):.4f}")
print(f"Decimal Value         : {decimal}")
print(f"Ceil Value            : {math.ceil(decimal)}")
print(f"Floor Value           : {math.floor(decimal)}")
print("=" * 45)