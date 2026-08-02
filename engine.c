#include <stdio.h>

// 1. Existing Clipper
void clip_voltage(float* wave, int length, float max_voltage) {
    for (int i = 0; i < length; i++) {
        if (wave[i] > max_voltage) {
            wave[i] = max_voltage;
        }
    }
}

// 2. Half-Wave Rectifier: Blocks the negative half of the wave (sets it to 0)
void half_wave_rectifier(float* wave, int length) {
    for (int i = 0; i < length; i++) {
        if (wave[i] < 0.0) {
            wave[i] = 0.0;
        }
    }
}

// 3. Full-Wave Rectifier: Inverts the negative half of the wave to positive
void full_wave_rectifier(float* wave, int length) {
    for (int i = 0; i < length; i++) {
        if (wave[i] < 0.0) {
            wave[i] = -wave[i];
        }
    }
}

// 4. Clamper: Shifts the entire wave up or down by a DC voltage amount
void clamper(float* wave, int length, float shift_amount) {
    for (int i = 0; i < length; i++) {
        wave[i] = wave[i] + shift_amount;
    }
}
