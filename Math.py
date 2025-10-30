1 import math

2

3 # Input

4 N =

int(input("Enter the number of cells: ")) #7

5 ioN-1

6 n = float(input("Enter the path loss exponent: ")) # 3

7

8 # Calculation

9 SIR (math.sqrt(3 * N)) **nio

10 db = 10 * math.log10(SIR)

11

12 # Output

13 print("Signal to Interference Ratio (SIR):", SIR)

14 print("SIR in dB:", db)
