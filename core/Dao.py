from core.File import File

class Dao:
    def __init__(self):
        self.db_file = File()
        self.db_contents = self.db_file.read_file()

    def save_contact(self, dict):
        self.db_contents.append(dict)
        self.__save_file(self.db_contents)

    def __save_file(self, contents):
        self.db_file.save_file(contents)
        
    def search(self, name, mode):
        name = name.casefold()
        search_result = []
        for contact in self.db_contents:
            if mode == 'listall':
                search_result.append(contact)
            else:
                actual_name = contact['name'].casefold()
                if name in actual_name:
                    search_result.append(contact)
        return search_result
    
    def get_last_index(self):
        last_index = 0
        if self.db_contents:
            for contact in self.db_contents:
                if int(contact['index']) > last_index:
                    last_index = int(contact['index'])
        return last_index

    def delete_from_db(self, index_to_delete):
        for index, contact in enumerate(self.db_contents):
            if index_to_delete == int(contact['index']):
                self.db_contents.pop(index)
                break
        self.__save_file(self.db_contents)
