from typing import List

import jieba
import pypinyin

from pinyinToPhonemes import PINYIN_DICT


def chinese_text_to_phonemes(text: str, seperator: str = "|") -> str:
    # If the text has already separated, use it directly.
    if ' ' in text:
        cut_text = text.split(' ')
    # If the text is not separated, use jieba to separate it for better pinyin results.
    else:
        cut_text = jieba.cut(text, HMM=False)

    pinyined_text = pypinyin.lazy_pinyin(cut_text, style=pypinyin.Style.TONE3, neutral_tone_with_five=True)

    results: List[str] = []

    for token in pinyined_text:
        # If the token is a pinyin, look up the pinyin dictionary and get the phoneme.
        if token[-1] in "12345" and token[:-1] in PINYIN_DICT:
            phoneme = PINYIN_DICT.get(token[:-1]) + token[-1]
            results.append(phoneme)

            # Add space between phonemes.
            if token != pinyined_text[-1]:
                results.append(' ')
        else:
            results.append(token)

    return seperator.join(results)


print(
    chinese_text_to_phonemes('叶公好龙，不好好学习')
)
print(
    chinese_text_to_phonemes('zheng4 le5 $ bu2 dao4 % ba1 bai3 % kuai4 qian2 $')
)