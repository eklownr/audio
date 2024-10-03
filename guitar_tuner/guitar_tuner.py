import threading

import sounddevice as sd
import soundfile as sf

data, samplerate = sf.read('../sounds/e2.mp3')
sf.write('new_fileE2.flac', data, samplerate)