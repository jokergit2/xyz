# Walsh Code Generation
import numpy as np

def walsh_code(n):
    H = np.array([[1]])

    # Build the Walsh matrix iteratively
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])

    return H

# Example: Generate Walsh code of size 8
n = int(input("enter the value: "))
print(walsh_code(n))
