from core.File import File

class Dao:
    def __init__(self):
        self.db_file = File()
        self.db_contents = self.db_file.read_file()

    def save_contact(self, dict):
        self.db_contents['contacts'].append(dict)
        self.__save_file(self.db_contents)

    def __save_file(self, contents):
        self.db_file.save_file(contents)
        
    def search(self, name, mode):
        name = name.casefold()
        self.db_contents = self.db_contents['contacts']
        search_result = []
        for contact in self.db_contents:
            if mode == 'listall':
                search_result.append(contact)
            else:
                actual_name = contact['name'].casefold()
                if name in actual_name:
                    search_result.append(contact)
        return search_result
    