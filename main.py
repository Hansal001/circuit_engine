import ctypes
import os
import math
import matplotlib.pyplot as plt

# 1. Load the compiled C library
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "libengine.dylib"))
engine = ctypes.CDLL(lib_path)

# 2. Define the argument types for the C functions
engine.half_wave_rectifier.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]

# 3. Generate a smooth sine wave
num_points = 100
original_wave = []
for i in range(num_points):
    # Amplitude of 5.0V
    val = 5.0 * math.sin(i * 0.2)
    original_wave.append(val)
    
length = len(original_wave)

# 4. Convert the Python list to a C array
c_array = (ctypes.c_float * length)(*original_wave)

# 5. Process the wave through the C engine (Half-Wave Rectifier)
engine.half_wave_rectifier(c_array, length)

# 6. Extract the processed data back into a Python list
processed_wave = [c_array[i] for i in range(length)]

# 7. Plot the results using Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(original_wave, label="Original Sine Wave", linestyle="--", color="gray")
plt.plot(processed_wave, label="Half-Wave Rectified", color="blue", linewidth=2)

# Format the graph
plt.title("Physics Engine: Half-Wave Rectifier")
plt.xlabel("Time (Arbitrary Units)")
plt.ylabel("Voltage (V)")
plt.axhline(0, color='black', linewidth=1)
plt.legend()
plt.grid(True)

# Display the graph window
plt.show()
