import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

noisy, fs = librosa.load("noisy_audio.wav", sr=None)
filtered, _ = librosa.load("filtered_audio.wav", sr=None)

plt.figure(figsize=(10,4))
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(noisy)), ref=np.max),
                         sr=fs, x_axis='time', y_axis='hz')
plt.title("Original Noisy Spectrogram")
plt.colorbar()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(filtered)), ref=np.max),
                         sr=fs, x_axis='time', y_axis='hz')
plt.title("Filtered Spectrogram")
plt.colorbar()
plt.tight_layout()
plt.show()
