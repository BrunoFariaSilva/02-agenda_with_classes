import configparser
from core.front import confirm_to_delete, get_new_name, get_new_phone
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
    if (mode == 'del') or (mode == 'modify'):
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
        if indexes_list:
            index_to_delete = ask_message('Informe o índice do contato a ser excluído: ', indexes_list, int, 'green')
            return index_to_delete
        else:
            show_message(f'Contato não encontrado!', 'green')
    
    def __delete_from_db(index):
        from core.Contact import Contact
        contact_to_delete = Contact(index, '', '')
        contact_to_delete.delete_contact(index)

    show_search_result(list)
    index_to_delete = __ask_to_delete()
    if index_to_delete and confirm_to_delete(index_to_delete):
        __delete_from_db(index_to_delete)
        show_message('Contato excluído com sucesso!', 'green')

def modify_contact(list):
    def _ask_to_modify():
        indexes_list = []
        for contact in list:
            indexes_list.append(int(contact['index']))
        if indexes_list:
            index_to_modify = ask_message('Informe o índice do contato a ser alterado: ', indexes_list, int, 'green')
            return index_to_modify
        else:
            show_message(f'Contato não encontrado!', 'green')        

    def _get_actual_contact_infos(index):
        from core.Dao import Dao
        dao_conn = Dao()
        for contact in dao_conn.db_contents:
            if index == int(contact['index']):
                actual_name = contact['name']
                actual_phone = contact['phone']
                break
        return [actual_name, actual_phone]
        
    def _check_infos(old, check):
        new = []
        if check[0] != '':
            new.append(check[0])
        else:
            new.append(old[0])
        if check[1] != '':
            new.append(check[1])
        else:
            new.append(old[1])
        return new

    def _get_new_contact_infos(index):
        actual_infos = _get_actual_contact_infos(index)
        new_infos = [get_new_name(actual_infos[0]), get_new_phone(actual_infos[1])]
        checked_infos = _check_infos(actual_infos, new_infos)
        if actual_infos != checked_infos:
            contact_modified = {'index': index,
                                'name': checked_infos[0],
                                'phone': checked_infos[1]}
            return contact_modified
        else:
            show_message('O contato não foi alterado!', 'red')
            return False

    def _save_changes_to_db(contact):
        from core.Contact import Contact
        contact_to_change = Contact('', '', '')
        contact_to_change.change_contact(contact)

    show_search_result(list)
    index_to_modify = _ask_to_modify()
    if index_to_modify:
        contact_has_changed = _get_new_contact_infos(index_to_modify)
        if contact_has_changed:
            _save_changes_to_db(contact_has_changed)
            show_message('Contato alterado com sucesso!', 'green')