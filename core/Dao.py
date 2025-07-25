from core.common import normalize_word
from operator import itemgetter
from core.File import File

class Dao:
    def __init__(self):
        ###Construtor da classe
        self.db_file = File()   #Instância da classe File
        self.db_contents = self.db_file.read_file()  #Solicita a leitura dos dados do arquivo de BD

    def save_contact(self, dict):
        ###Método para salvar um novo contato no BD
        self.db_contents.append(dict)  #Adiciona o novo contato na lista atual do BD (local)
        self.__sort_contacts()  #Ordenação dos contatos da lista de contatos (local)
        self.__save_to_db(self.db_contents)  #Solicita a gravação da lista (local) do BD no arquivo

    def __sort_contacts(self):
        ###Método para ordenação alfabética da lista de contatos
        self.db_contents = sorted(self.db_contents, key=itemgetter('normalized_name'))  #Utiliza a função sorted com o método
                                #'itemgetter' do módulo 'operator' para ordenação da lista de dicionários

    def __save_to_db(self, contents):
        ###Método para gravação do arquivo de BD
        self.db_file.save_file(contents)  #Solicita à classe File a gravação do arquivo
        
    def search(self, name, mode):
        ###Método para busca de contato
        search_result = []      #Lista para o resultado da busca
        if mode != 'listall':
            name = normalize_word(name)
        if (name) and (len(name) == 1) and (mode != 'listall'):  #Se existe conteúdo para busca,
                            #E é apenas uma letra E o modo não é listagem completa (busca por letra inicial)
            for contact in self.db_contents:  #Para cada contato na lista de contatos
                actual_name = contact['normalized_name']  #Recupera o nome do contato atual
                if name == actual_name[0]:  #Verifica se o contato atual possui a letra inicial informado pelo usuário
                    search_result.append(contact)  #Adiciona o contato atual na lista de resultado de busca
        else:                   #Se é busca por nome ou parte do nome
            for contact in self.db_contents:  #Para cada contato na lista de contatos
                if mode == 'listall':  #Se o modo de busca é 'listall'
                    search_result.append(contact)  #Adiciona todos os contatos na lista resultado de busca
                else:           #Se o modo de busca for normal
                    actual_name = contact['normalized_name']  #Recupera o nome do contato atual
                    if name in actual_name:  #Verif se o cont. atual possui o nome ou parte do nome inform pelo usuário
                        search_result.append(contact)  #Adiciona o contato atual na lista de resultado de busca
        return search_result    #Retorna a lista com o resultado da busca
    
    def get_last_index(self):
        ###Método para obter o maior index já utilizado
        last_index = 0          #Atribui zero como último índex
        if self.db_contents:    #Se o banco de dados não for vazio
            for contact in self.db_contents:  #Para cada contato na lista de contatos
                if int(contact['index']) > last_index:  #Se o índice atual é maior do que o já registrado
                    last_index = int(contact['index'])  #Salva o índice atual
        return last_index       #Retorna o último index utilizado

    def delete_from_db(self, index_to_delete):
        ###Método para excluir um contato do BD
        for index, contact in enumerate(self.db_contents):  #Para cada contato na lista de contatos
            if index_to_delete == int(contact['index']):  #Se o index para exclusão for igual ao index do contato atual
                self.db_contents.pop(index)  #Exclui o contato atual (local)
                break           #Interrompe o for
        self.__save_to_db(self.db_contents)  #Solicita a gravação da lista local no arquivo de BD

    def change_contact(self, changed_contact):
        ###Método para alteração do contato
        for contact in self.db_contents:  #Para cada contato na lista de contatos
            if changed_contact['index'] == contact['index']:  #Verifica se o contato alterado é o atual do for
                contact['name'] = changed_contact['name']  #Atualiza o nome do contato
                contact['phone'] = changed_contact['phone']  #Atualiza o telefone do contato
                break           #Interrompe o for
        self.__sort_contacts()  #Ordenação dos contatos da lista de contatos (local)
        self.__save_to_db(self.db_contents)  #Solicita a gravação da lista local no arquivo de BD
        