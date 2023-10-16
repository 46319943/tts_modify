"""
Load npy files from cache and inspect the data.
"""
import os
import numpy as np

filepath = r'C:\Document\Maperson\TTS\recipes\multilingual\vits_tts\phoneme_cache\YWlzaGVsbDMjdHJhaW5cd2F2XFNTQjA0MjdcU1NCMDQyNzA0Nzg=_phoneme.npy'

phoneme = np.load(filepath)
print(phoneme)
