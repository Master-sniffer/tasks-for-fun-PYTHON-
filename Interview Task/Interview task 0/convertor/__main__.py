import argparse
from convertor.encode_convertor import encode as encod
from convertor.decode_convertor import Decoder
import re
import sys
import string
#KEY_FILE = 'key'
from pathlib import Path
import os
import convertor
KEY_FILE = Path(os.path.dirname(convertor.__file__)) / 'key'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_text',
                        type=str,
                        help='Returns encoded or decode text')
    return parser.parse_args()


def decode():
    text=str(sys.argv[1])
    code=Decoder(KEY_FILE)
    text=code.convert_text(text)
    return text
    raise NotImplementedError('Not implemented [4]')


def encode():

    text=str(sys.argv[1])
    code = encod(KEY_FILE)
    text=code.convert_text(text)
    return text
    raise NotImplementedError('Not implemented [5]')


def prepare_text_source(text: str):
    return re.sub(string.punctuation, '', text.lower())