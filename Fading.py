# MICS EXP 5

# Speed of Light (m/s)
c = 3 * (10 ** 8)

# User inputs
v = float(input("Enter the velocity (m/s): "))
f = float(input("Enter the frequency (Hz): "))

# Wavelength
LAMBDA = c / f

# Doppler Frequency
fd = v / LAMBDA

# Doppler spread
Bd = 2 * fd

# Coherence time
Tc = 0.423 / fd

# Get symbol period in microseconds and convert to seconds
Ts_micro = float(input("Enter the symbol period (in microseconds): "))
Ts = Ts_micro * 1e-6

# Get signal bandwidth in kHz and convert to Hz
sigB_kHz = float(input("Enter the signal bandwidth (in kHz): "))
sigB = sigB_kHz * 1e3

# Decision Logic
if (Bd > sigB) and (Tc < Ts):
    print("It is a fast fading channel")
elif (Bd < sigB) and (Tc > Ts):
    print("It is a slow fading channel")
else:
    print("It cannot be predicted")
