import math
base = 3
exponent = 4
square = 49
angle = 0.5

sq_result = math.sqrt(square)
pow_result = pow(base, exponent)
sin_result = math.sin(angle)
cos_result = math.cos(angle)

print(f"{base} raised to {exponent} = {pow_result}")
# Output: 81
print(f"Sine of {angle} = {sin_result:.2f}")
# Output: 0.48
print(f"Cosine of {angle} = {cos_result:.2f}")
# Output: 0.88
print(f"Square root of {square} = {sq_result:.2f}")
# Output: 7.00


