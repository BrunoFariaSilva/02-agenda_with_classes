from core.Contact import Contact
from core.Dao import Dao
from core.front import show_usage

class Args:
    def __init__(self, args):
        self.command = ''
        self.options = ''        
        args.pop(0)
        if args:
            self.command = args[0]
            self.options = args[1:]
            print(f'DEBUG: self.command = {self.command}')
            print(f'DEBUG: self.options = {self.options}')

    def check_and_run_command(self, command):
        if (command == 'add') and (self.__check_options()):
            self.__change_args_to_infos()
            new_contact = Contact(self.name, self.phone)
            new_contact.save_to_db()

        elif (command == 'modify') and (self.__check_options()):
            pass

        elif (command == 'del') and (self.__check_options()):
            pass

        elif (command == 'search') and (self.__check_options()):
            self.__join_search_text()
            dao_conn = Dao()
            dao_conn.search(self.name_to_search)

        elif (command == 'listall') and (self.__check_options()):
            pass

        else:
            show_usage()


    def __check_options(self):
        len_options = len(self.options)
        if self.command == 'add':
            if len_options >= 2:
                return True
        elif (self.command == 'modify') or (self.command == 'del'):
            if len_options == 1:
                return True
        elif self.command == 'search':
            if len_options >= 1:
                return True
        elif self.command == 'listall':
            if len_options == 0:
                return True

    def __change_args_to_infos(self):
        self.name = ' '.join(self.options[0:-1])
        self.phone = self.options[-1]

    def __join_search_text(self):
        self.name_to_search = ' '.join(self.options)
