import os
from glob import glob


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


items = aidatatang(r'D:\aidatatang_200zh')
print()

items = aishell3(r'D:\AISHELL-3', 'train/content.txt')
print()

items = aishell3(r'D:\AISHELL-3', 'train/content.txt')
print()
