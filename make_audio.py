import numpy as np
import soundfile as sf

fs = 16000       # Sampling frequency (16 kHz)
duration = 4     # seconds

t = np.linspace(0, duration, int(fs*duration), endpoint=False)

# Clean voice-like tone (just for testing)
clean_signal = 0.6 * np.sin(2 * np.pi * 440 * t)

# Add random noise
noise = 0.3 * np.random.normal(0, 1, len(clean_signal))

# Final noisy signal
noisy_audio = clean_signal + noise

# Save file
sf.write("noisy_audio.wav", noisy_audio, fs)

print("noisy_audio.wav created successfully!")
