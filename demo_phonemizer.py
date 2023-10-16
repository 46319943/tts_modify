from TTS.tts.utils.text.chinese_mandarin.phonemizer import chinese_text_to_phonemes

print(
    chinese_text_to_phonemes(
        'hao3 hao3 xue2 xi2'
    ),
    chinese_text_to_phonemes(
        '好好学习'
    ),
    chinese_text_to_phonemes(
        '胡老师无敌'
    )
)
