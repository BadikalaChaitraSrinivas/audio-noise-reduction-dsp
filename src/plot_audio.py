import librosa
import matplotlib.pyplot as plt

audio, fs = librosa.load("noisy_audio.wav", sr=None)

print("Sampling Frequency:", fs)
print("Number of samples:", len(audio))

plt.figure(figsize=(10,4))
plt.plot(audio)
plt.title("Original Audio Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

