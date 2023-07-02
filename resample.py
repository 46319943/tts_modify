"""
Resample all the wav files in the folder to 16kHz in place.
"""
import os
import glob
import librosa
import soundfile as sf
from tqdm import tqdm

input_folder = r'D:\AISHELL-3_16k'

for wav_file in tqdm(glob.glob(os.path.join(input_folder, '**', '*.wav'), recursive=True)):
    wav, sr = librosa.load(wav_file, sr=16000)
    sf.write(wav_file, wav, sr)