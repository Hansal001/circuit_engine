import ctypes
import os

# 1. Load the compiled C library
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "libengine.dylib"))
engine = ctypes.CDLL(lib_path)

# 2. Define the argument types (float array, integer length, float max_voltage)
engine.clip_voltage.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_float]

# 3. Create a simulated input waveform
input_wave = [2.5, 4.2, 5.8, 3.1, 7.0]
length = len(input_wave)
clipping_threshold = 5.0

print("Original Wave:", input_wave)

# 4. Convert Python list to C array and call the function
c_array = (ctypes.c_float * length)(*input_wave)
engine.clip_voltage(c_array, length, clipping_threshold)

# 5. Print the processed results
print("Clipped Wave: ", [round(x, 2) for x in c_array])
