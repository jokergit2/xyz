# To study capacity of mobile system

# Input: Radius
r = float(input("Enter the radius: "))
ac = 2.598 * (r ** 2)
print("Area of cell (ac):", ac)

# Input: Total number of channels
Tc = int(input("Enter the total number of channels: "))

# For small cluster size
d1 = int(input("Enter number of cells (small cluster): "))
c1 = Tc / d1
print("Channels per cell (c1):", c1)

S1 = int(input("Enter number of cells in system (small cluster): "))
Sc1 = S1 * c1
print("System small cell capacity (Sc1):", Sc1)

# For large cluster size
d2 = int(input("Enter number of cells (large cluster): "))
c2 = Tc / d2
print("Channels per cell (c2):", c2)

S2 = int(input("Enter the total number of cells in system (large cluster): "))
Sc2 = S2 * c2
print("System capacity (Sc2):", Sc2)

# Comparison
if Sc1 > Sc2:
    print("Capacity increases with decrease in cluster size")
else:
    print("Capacity decreases with increase in cluster size")
