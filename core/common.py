import configparser
from core.front import show_search_result

def __get_config_file():
    config_filepath = 'config.ini'
    return config_filepath

def read_config():
    config_contents = configparser.ConfigParser()
    config_contents.read(__get_config_file())
    return config_contents

def get_db_filepath():
    config = read_config()
    return config.get('db', 'dbfile')

def search_contact(name_to_search):
    from core.Dao import Dao
    db_contents = Dao()
    search_result_list = db_contents.search(name_to_search)
    show_search_result(search_result_list)

