from core.Dao import Dao

class Contact:
    def __init__(self, index, name, phone):
        self.index = index
        self.name = name
        self.phone = phone

    def save_to_db(self):
        new_contact_dict = {'index': self.index,
                            'name': self.name.title(),
                            'phone': self.phone}
        dao_conn = Dao()
        dao_conn.save_contact(new_contact_dict)
        from core.front import show_message
        show_message(f'Contato "{new_contact_dict['name']}" adicionado com sucesso!', 'green')

    def delete_contact(self, index_to_delete):
        dao_conn = Dao()
        dao_conn.delete_from_db(index_to_delete)

    def change_contact(self, contact):
        dao_conn = Dao()
        dao_conn.change_contact(contact)
        