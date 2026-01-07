import numpy as np
import librosa
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import soundfile as sf

audio, fs = librosa.load("noisy_audio.wav", sr=None)

# ---------- Low Pass Filter ----------
cutoff = 800   # cutoff frequency in Hz
b, a = butter(6, cutoff/(fs/2), btype='low')
filtered = filtfilt(b, a, audio)

# Save filtered audio
sf.write("filtered_audio.wav", filtered, fs)

print("Filtering done! Check 'filtered_audio.wav'")
