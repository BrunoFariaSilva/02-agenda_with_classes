from core.common import get_db_filepath
from pathlib import Path
import json

class File:
    def __init__(self):
        self.json_file = Path(get_db_filepath())  #'contacts.json'
        self.__check_file()

    def __check_file(self):
        if not self.json_file.exists():
            #erro arquivo não existe
            self.__create_file()

    def __create_file(self):
        with self.json_file:
            Path.touch(self.json_file, mode=0o777, exist_ok=False)
        self.__initialize_file()

    def __initialize_file(self):
        init_dict = {'contacts':[]}
        with open(self.json_file, 'w', newline='\n') as file_to_initialize:
            json.dump(init_dict, file_to_initialize, indent=4)

    def read_file(self):
        with open(self.json_file, 'r', newline='\n') as file_to_read:
            file_contents = json.load(file_to_read)
        
        print(f'DEBUG 2: file_contents = {file_contents}')
        return file_contents

    def save_file(self, dict):
        with open(self.json_file, 'w', newline='\n') as file_to_save:
            json.dump(dict, file_to_save, indent=4)
            