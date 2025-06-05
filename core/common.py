import configparser
from core.front import show_search_result, show_message, ask_message, confirm_to_delete

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
    def __ask_to_delete():
        indexes_list = []
        for contact in list:
            indexes_list.append(int(contact['index']))

        index_to_delete = ask_message('Informe o índice do contato a ser excluído: ', indexes_list, int, 'green')
        return index_to_delete
    
    def __delete_from_db(index):
        from core.Contact import Contact
        contact_to_delete = Contact(index, '', '')
        contact_to_delete.delete_contact(index)

    show_search_result(list)
    index_to_delete = __ask_to_delete()
    if index_to_delete and confirm_to_delete(index_to_delete):
        __delete_from_db(index_to_delete)
        show_message('Contato excluído com sucesso!', 'green')