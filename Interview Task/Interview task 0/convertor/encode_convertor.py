import os, glob
from abc import ABC
from pathlib import Path
from convertor.abstract_base_convertor import AbstractFileConvertor




class encode(AbstractFileConvertor):

    def __init__(self, key_file: [str, ...] = None, **_):
        assert key_file is None or os.path.isfile(key_file)
        self._latter_mapper = self._create_map(key_file)

    def _create_map(self, file: [str, ...], **kwargs) -> dict[str, str]:
        dicts={}
        if file==None:
            dicts[""]=""
        else:
            with open(file, "r") as f:
                textes=f.readlines()
                for line in textes:
                    letter=line[0]
                    line=str(line[3:].split(',')[0])
                    if (line==""):
                        pass
                    else:
                        dicts[line]=letter
            return dicts

    def convert_files(self, *, input_dir: str, input_mask: str,
                    output_dir: str, input_prefix: str,
                    output_prefix: str):
        listes=[]
        for filename in glob.glob(os.path.join(input_dir, input_mask)):
            output_name = self.output_name_generator(
                filename,
                input_prefix,
                output_prefix,
                output_dir,
            )
            with open(filename) as file:
                with open(output_name, 'w') as outfile:
                    converted_text = self.convert_text(file.read())
                    outfile.write(converted_text)
                    listes.append(converted_text)
        return listes

    @staticmethod
    def output_name_generator(input_file_name: str, input_prefix: str,
                            output_prefix: str, output_dir: str):
        """A method for getting output file name based on input one and prefix
        :return: output name
        """
        _, name = os.path.split(input_file_name)
        name, ext = os.path.splitext(name)
        common_suffix = name.removeprefix(input_prefix)
        return os.path.join(output_dir, f'{output_prefix}{common_suffix}{ext}')

    def convert_text(self, input_text: str) -> str:
        if (input_text[0].isalpha):
            print ("decode -> encode")
            for replace, original in self._latter_mapper.items():
                input_text = input_text.lower().replace(original.lower(),replace, -1)
        else:
            print ('encode -> decode')
            for original, replace in self._latter_mapper.items():
                input_text = input_text.replace(replace, original, -1)
        return input_text