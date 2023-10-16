import os
from glob import glob
import pandas as pd



def generate_for_st_cmds():
    root_path = r"D:\ST-CMDS-20170001_1-OS"
    output_path = r"D:\ST-CMDS-META.csv"

    items = []

    for txt_file_path in glob(os.path.join(root_path, '**', '*.txt'), recursive=True):
        text_basename = os.path.basename(txt_file_path)
        txt_filename = os.path.basename(txt_file_path).split('.txt')[0]
        speaker = txt_filename[-8:-4]

        with open(txt_file_path, "r", encoding="utf-8") as ttf:
            text = ttf.read().strip()

        wav_file_path = text_basename.replace('.txt', '.wav')
        items.append({
            'audio_file': wav_file_path,
            'text': text,
            'speaker_name': speaker,
        })

    df = pd.DataFrame(items)
    df.to_csv(output_path, index=False, encoding="utf-8")


if __name__ == '__main__':
    generate_for_st_cmds()
