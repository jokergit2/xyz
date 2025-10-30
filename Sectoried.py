# Exp 3 Ratio of S/I
import math

# Input path loss exponent
n = float(input("Enter path loss exponent (n): "))

# ----------- For Three Sector -----------
print("\n% For Three sector")

N = 4
Q = math.sqrt(3 * N)
CI = (1 / ((Q**n) + (0.7)**n))
print(f"Q = {Q:.4f}")
print(f"CI = {CI:.4f}")

N = 7
Q = math.sqrt(3 * N)
CI = (1 / ((Q**n) + (0.7)**n))
print(f"Q = {Q:.4f}")
print(f"CI = {CI:.4f}")

print("As N increases S/I ratio increases")

# ----------- For Six Sector -----------
print("\n% For Six sector")

N = 4
Q = math.sqrt(3 * N)
CI = (1 / ((Q**n) + (0.7)**n))
print(f"Q = {Q:.4f}")
print(f"CI = {CI:.4f}")

N = 7
Q = math.sqrt(3 * N)
CI = (1 / ((Q**n) + (0.7)**n))
print(f"Q = {Q:.4f}")
print(f"CI = {CI:.4f}")

print("Sectoring increases S/I ratio increases")
