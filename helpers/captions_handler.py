import pandas as pd
from collections import defaultdict
import re


class CaptionsHandler:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.captions = defaultdict(list)
        self.start_token = '<start>'
        self.end_token = '<end>'

    def load_captions(self):
        data = pd.read_csv(self.data_path, encoding='utf-8', sep='|')
        data[' comment'] = data[' comment'].apply(lambda x: self.__process_caption(x))
        for img_name, comment in data[['image_name', ' comment']].values:
            self.captions[img_name.replace('.jpg', '')].append(comment)

    @staticmethod
    def __process_caption(text):
        text = re.sub(r'\s+([.,!?;:])', r'\1', text)
        text = re.sub(r'(["\'])(\s*)(.*?)(\s*)(\1)', r'\1\3\1', text)
        text = re.sub(r"\s*'\s*n\s*'\s*", r"'n'", text)
        text = re.sub(r"\s+'s\b", r"'s", text)
        text = re.sub(r'\s*\(\s*(.*?)\s*\)\s*', r'(\1)', text)
        return text.lstrip()
