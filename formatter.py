import os
from glob import glob

import pandas as pd


def aidatatang(root_path, meta_file=None, ignored_speakers=None):
    """
    Chinese multi-speaker dataset from https://openslr.org/62/
    """
    if meta_file is None or meta_file == '':
        meta_file = "transcript/aidatatang_200_zh_transcript.txt"
    txt_file = os.path.join(root_path, meta_file)
    items = []

    filename_to_text_dict = {}
    with open(txt_file, "r", encoding="utf-8") as ttf:
        for line in ttf:
            filename = line[:15]
            text = line[15:].replace(' ', '', -1).strip()
            filename_to_text_dict[filename] = text

    for wav_file_path in glob(os.path.join(root_path, 'corpus/**/*.wav'), recursive=True):
        wav_filename = os.path.basename(wav_file_path).split('.wav')[0]
        speaker = wav_filename[5:10]

        # ignore speakers
        if isinstance(ignored_speakers, list):
            if speaker in ignored_speakers:
                continue

        items.append({
            'audio_file': wav_file_path,
            'text': filename_to_text_dict[wav_filename],
            'speaker_name': speaker,
            'root_path': root_path
        })

    return items


def aishell3(root_path, meta_file=None, ignored_speakers=None):
    """
    Chinese multi-speaker dataset from https://openslr.org/93/
    """
    if meta_file is None or meta_file == '':
        meta_file = "train/label_train-set.txt"
    txt_file = os.path.join(root_path, meta_file)
    meta_dir = os.path.dirname(txt_file)
    items = []

    with open(txt_file, "r", encoding="utf-8") as ttf:
        for line in ttf:
            if line.startswith('#'):
                continue
            if line.strip() == '':
                continue

            # labeled file
            if '|' in line:
                wav_name = line.split('|')[0]
                text = line.split('|')[1].strip()

            # unlabeled file
            else:
                wav_name = line[:11]
                text = line[16:]
                # Get the even split
                text = ' '.join(text.split(' ')[1::2])

            speaker = wav_name[:7]
            wav_file_path = os.path.join(root_path, meta_dir, 'wav', speaker, wav_name + '.wav')

            # ignore speakers
            if isinstance(ignored_speakers, list):
                if speaker in ignored_speakers:
                    continue

            items.append({
                'audio_file': wav_file_path,
                'text': text,
                'speaker_name': speaker,
                'root_path': root_path
            })

    return items


def st_cmds(root_path, meta_file=None, ignored_speakers=None):
    """
    Chinese multi-speaker dataset from http://www.openslr.org/38/
    """

    items = []

    # BaseDatasetConfig() with "" meta_file will be input by load_tts_samples by default.
    if meta_file is not None and meta_file != '':
        txt_file = os.path.join(root_path, meta_file)
        metadata = pd.read_csv(txt_file, encoding="utf-8")
        for row in metadata.itertuples():
            wav_file_path = os.path.join(root_path, row.audio_file)
            items.append({
                'audio_file': wav_file_path,
                'text': row.text,
                'speaker_name': row.speaker_name,
                'root_path': root_path
            })

    else:
        # Iterate over all the files with ".wav" suffix in the root_path
        for wav_file_path in glob(os.path.join(root_path, '**', '*.wav'), recursive=True):
            wav_filename = os.path.basename(wav_file_path).split('.wav')[0]
            speaker = wav_filename[-8:-4]

            txt_file_path = wav_file_path.replace('.wav', '.txt')
            with open(txt_file_path, "r", encoding="utf-8") as ttf:
                text = ttf.read().strip()

            # ignore speakers
            if isinstance(ignored_speakers, list):
                if speaker in ignored_speakers:
                    continue

            items.append({
                'audio_file': wav_file_path,
                'text': text,
                'speaker_name': speaker,
                'root_path': root_path
            })

    return items

def magic(root_path, meta_file=None, ignored_speakers=None):
    """
    Chinese multi-speaker dataset from http://www.openslr.org/68/
    The train meta file has mistakenly included the dev files. Directly fix it by copy the dev files into the train folder.
    """
    items = []

    if meta_file is None or meta_file == '':
        meta_file = "train/TRANS.txt"

    txt_file = os.path.join(root_path, meta_file)
    meta_dir = os.path.dirname(txt_file)

    metadata = pd.read_csv(txt_file, encoding="utf-8", sep='\t')
    for row in metadata.itertuples():

        # ignore speakers
        if isinstance(ignored_speakers, list):
            if row.SpeakerID in ignored_speakers:
                continue

        wav_file_path = os.path.join(meta_dir, row.SpeakerID, row.UtteranceID)
        items.append({
            'audio_file': wav_file_path,
            'text': row.Transcription,
            'speaker_name': row.SpeakerID,
            'root_path': root_path
        })

    return items


# items = aidatatang(r'D:\aidatatang_200zh')
# print('.')
#
# # text = guang3 zhou1 nv3 da4 xue2 sheng1 deng1 shan1 shi1 lian2 si4 tian1 jing3 fang1 zhao3 dao4 yi2 si4 nv3 shi1\n
# items = aishell3(r'D:\AISHELL-3', 'train/content.txt')
# print('.')
#
# items = st_cmds(r'D:\ST-CMDS-20170001_1-OS')
# print('.')
#
# items = st_cmds(r'D:\ST-CMDS-20170001_1-OS', 'D:\ST-CMDS-META.csv')
# print('.')

items = magic(r'D:\MagicData')
print('.')