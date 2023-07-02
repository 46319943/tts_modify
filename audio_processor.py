from TTS.tts.models.vits import CharactersConfig, Vits, VitsArgs, VitsAudioConfig
from TTS.utils.audio import AudioProcessor

audio_config = VitsAudioConfig(
    sample_rate=16000,
    win_length=1024,
    hop_length=256,
    num_mels=80,
    mel_fmin=0,
    mel_fmax=None,
)

ap = AudioProcessor(
    **audio_config.to_dict(),
    do_trim_silence=True, trim_db=15,
    # resample=True
)


wav = ap.load_wav(r'D:\AISHELL-3\train\wav\SSB0005\SSB00050001.wav')
print(wav)