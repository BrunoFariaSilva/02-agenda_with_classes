from core.Dao import Dao

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save_to_db(self):
        new_contact_dict = {'name': self.name.title(),
                            'phone': self.phone}
        dao_conn = Dao()
        dao_conn.save_contact(new_contact_dict)

