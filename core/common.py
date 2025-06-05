import configparser
from core.front import show_search_result, show_message, ask_message

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

def search_contact(name_to_search, mode=None):
    from core.Dao import Dao
    db_contents = Dao()
    search_result_list = db_contents.search(name_to_search, mode)
    if mode == 'del':
        return search_result_list
    else:
        show_search_result(search_result_list)

def get_last_contact_index():
    from core.Dao import Dao
    db_contents = Dao()
    return db_contents.get_last_index()

def delete_contact(list):
    def ask_to_delete():

        ask_message('red', 'Informe o índice do contato a ser excluído: ', [1, 2])


    print(f'DEBUG 1: list = {list}')
    show_search_result(list)
    ask_to_delete()