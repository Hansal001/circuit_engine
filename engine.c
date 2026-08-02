#include <stdio.h>

void clip_voltage(float* wave, int length, float max_voltage) {
    for (int i = 0; i < length; i++) {
        // If the voltage exceeds the threshold, clip it
        if (wave[i] > max_voltage) {
            wave[i] = max_voltage;
        }
    }
}
