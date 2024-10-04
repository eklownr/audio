#3. Implementering
# Här är en översiktlig kodsnutt som visar hur man kan kombinera dessa steg med hjälp av Python:

import pyaudio
import numpy as np

# Inställningar för PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

try:
    while True:
        data = stream.read(1024)
        # Omvandla byte-data till numpy-array
        samples = np.frombuffer(data, dtype=np.int16)
        
        # Utför FFT för att få frekvenserna
        fft_result = np.fft.fft(samples)
        frequencies = np.fft.fftfreq(len(fft_result))

        # Beräkna magnituden av FFT-resultatet
        magnitude = np.abs(fft_result)

        # Hitta den mest framträdande frekvensen
        peak_freq_index = np.argmax(magnitude)
        peak_freq = abs(frequencies[peak_freq_index] * 44100)  # Justera med samplingsfrekvens

        print(f"Frekvens: {peak_freq:.2f} Hz")
except KeyboardInterrupt:
    pass

# Stäng strömmen och PyAudio-instansen
stream.stop_stream()
stream.close()
audio.terminate()
