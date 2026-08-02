import ctypes
import os

# 1. Load the compiled C library
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "libengine.dylib"))
engine = ctypes.CDLL(lib_path)

# 2. Define the argument types for ALL functions
engine.clip_voltage.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_float]
engine.half_wave_rectifier.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
engine.full_wave_rectifier.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
engine.clamper.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_float]

# 3. Create a simulated input waveform (with positive and negative voltages)
input_wave = [5.0, 2.5, 0.0, -2.5, -5.0, -2.5, 0.0, 2.5, 5.0]
length = len(input_wave)

print("Original Wave:      ", input_wave)

# --- Test Half-Wave Rectifier ---
# We have to recreate the C array each time because C modifies it in place
c_array_half = (ctypes.c_float * length)(*input_wave)
engine.half_wave_rectifier(c_array_half, length)
print("Half-Wave Rectified:", [round(x, 2) for x in c_array_half])

# --- Test Full-Wave Rectifier ---
c_array_full = (ctypes.c_float * length)(*input_wave)
engine.full_wave_rectifier(c_array_full, length)
print("Full-Wave Rectified:", [round(x, 2) for x in c_array_full])

# --- Test Clamper (Shift up by 2.0V) ---
c_array_clamp = (ctypes.c_float * length)(*input_wave)
engine.clamper(c_array_clamp, length, 2.0)
print("Clamped (+2.0V):    ", [round(x, 2) for x in c_array_clamp])
