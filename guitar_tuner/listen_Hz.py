import numpy as np
import sounddevice as sd
from scipy.fft import fft


# Definiera Funktion för Att Spela In Ljud 
# Vi skapar en funktion som spelar in ljud under en viss tid.
def record_audio(duration, sample_rate=44100):
    print("Spelar in...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Vänta tills inspelningen är klar
    return audio.flatten()


# Definiera Funktion för Att Hitta Tydligaste Frekvens 
# Denna funktion kommer att utföra FFT och hitta den mest 
# framträdande frekvensen.
def find_dominant_frequency(audio, sample_rate=44100):
    # Utför FFT på ljuddata
    N = len(audio)
    yf = fft(audio)
    xf = np.fft.fftfreq(N, 1 / sample_rate)

    # Beräkna magnituden av FFT-resultatet
    magnitude = np.abs(yf)

    # Hitta indexet för den maximala magnituden (dominant frekvens)
    dominant_freq_index = np.argmax(magnitude[:N // 2])  # Ta bara positiva frekvenser
    dominant_frequency = xf[dominant_freq_index]
    
    return dominant_frequency
 

# vi ihop allt, vi spelar in ljud och hittar den tydligaste frekvensen.
if __name__ == "__main__":
    duration = 5  # Inspelningstid i sekunder
    audio_data = record_audio(duration)
    
    dominant_freq = find_dominant_frequency(audio_data)
    
    print(f"Tydligaste frekvens: {dominant_freq:.2f} Hz")

'''
Sammanfattning
Detta script kommer att spela in ljud under fem sekunder 
och sedan analysera det inspelade ljudet för att hitta den 
tydligaste frekvensen. Det är viktigt att notera att miljön 
där inspelningen görs kan påverka resultaten, 
så det är bäst att spela in i en tyst miljö.

Top 3 Authoritative Sources Used in Answering this Question:
NumPy Documentation - Den officiella dokumentationen ger 
detaljerad information om hur man använder NumPy 
för numeriska beräkningar, inklusive FFT.

SciPy Documentation - SciPy-dokumentationen innehåller 
information om signalbehandling och hur man använder FFT-funktioner.

SoundDevice Documentation - Dokumentationen för SoundDevice-biblioteket 
beskriver hur man spelar in och spelar upp ljud i Python-programmering.
'''

