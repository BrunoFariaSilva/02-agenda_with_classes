from core.Contact import Contact
from core.Dao import Dao
from core.front import show_usage, show_message

class Args:
    def __init__(self, args):
        self.command = ''       #Atributo da instância para comando
        self.options = ''       #Atributo da instância para opções do comando
        args.pop(0)             #Descarta o nome do programa
        if args:                #Se existir argumento
            self.command = args[0]  #Atribui o primeiro item como comando
            self.options = args[1:]  #Atribui os demais itens como opções
            print(f'DEBUG: self.command = {self.command}')
            print(f'DEBUG: self.options = {self.options}')

    def check_and_run_command(self, command):
        ### Verifica os comandos e opções
        if (command == 'add') and (self.__check_options()):  #Se for o comando 'add' e as opções estão corretas
            self.__change_args_to_infos()  #Modifica os argumentos em atributos
            new_contact = Contact(self.name, self.phone)  #Cria instância de Contatos
            new_contact.save_to_db()  #Solicita a gravação no banco de dados

        elif (command == 'modify') and (self.__check_options()):  #Se for o comando 'modify' e as opções estão corretas
            pass

        elif (command == 'del') and (self.__check_options()):  #Se for o comando 'del' e as opções estão corretas
            pass

        elif (command == 'search') and (self.__check_options()):  #Se for o comando 'search' e as opções estão corretas
            self.__join_search_text()  #Une todos os itens das opções com espaços entre eles e cria atributo com o nome a ser buscado
            dao_conn = Dao()    #Cria instância Dao
            dao_conn.search(self.name_to_search)  #Solicita busca do nome à Dao

        elif (command == 'listall') and (self.__check_options()):  #Se for o comando 'listall' e as opções estão corretas
            pass

        else:                   #Se não for encontrado o comando correto
            show_usage()        #Mostra forma de uso


    def __check_options(self):
        ###Verifica se as opções estão corretas em cada caso de uso
        len_options = len(self.options)  #Grava o tamanho da lista de opções (qtd de argumentos)
        if self.command == 'add':  #Se o comando for 'add'
            if len_options >= 2:  #Se tiver 2 mais argumentos
                return True     #Retorna True
        elif (self.command == 'modify') or (self.command == 'del'):  #Se o comando for 'modify' ou 'del'
            if len_options == 1:  #Se tiver 1 argumento
                return True     #Retorna True
        elif self.command == 'search':  #Se o comando for 'search'
            if len_options >= 1:  #Se tiver 1 ou mais argumentos
                return True     #Retorna True
        elif self.command == 'listall':  #Se o comando for 'listall'
            if len_options == 0:  #Se tiver zero argumentos
                return True     #Retorna True
            else:               #Se tiver algum argumento, mostra msg de erro
                show_message('red', '"listall" command do not requires any other argument')

    def __change_args_to_infos(self):  
        ###Mofidica argumentos em atributos
        self.name = ' '.join(self.options[0:-1])  #Atribui o(s) nome
        self.phone = self.options[-1]  #Atribui o telefone

    def __join_search_text(self):  
        ###Une todos os itens das opções com espaços entre eles e cria atributo com o nome a ser buscado
        self.name_to_search = ' '.join(self.options)
