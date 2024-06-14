import sounddevice as sd
import wavio 

# Settings
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration of recording in seconds

# Record audio
print("Recording audio...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording finished.")

# Save the recorded audio as a WAV file
wavio.write("output.wav", audio, sample_rate, sampwidth=2)
print("Audio saved as 'output.wav'.")
