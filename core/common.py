import configparser
from core.front import confirm_to_delete, get_new_name, get_new_phone
from core.front import show_search_result, show_message, ask_message

def check_and_run_command(args):
    ###Função para verificar os argumentos e executar os comandos
    def check_name_and_phone():
        ##Subfunção para checar se existe nome e telefone passados nos argumentos
        if args.name and args.phonenumber:  #Se existir nome E telefone
            return True         #Retorna verdadeiro
        else:                   #Se não existir nome E/OU telefone
            show_message('Parâmetro incorreto! Verifique o nome e o telefone do contato.', 'red')
            show_message('Use o argumento "-h" para obter ajuda.')
            return False        #Retorna falso
    
    def check_name():
        ##Subfunção que checa se existe nome passado no argumento
        if args.name:           #Se existir nome
            return True         #Retorna verdadeiro
        else:                   #Se não existir nome
            show_message('Parâmetro incorreto! Verifique o nome do contato. Use o argumento "-h" para obter ajuda.', 'red')
            return False        #Retorna falso
        
    if args.command == 'add':   #Verifica se o comando é 'add'
        if check_name_and_phone():  #Verifica se existe nome e telefone
            from core.Contact import Contact  #Importa a classe Contact
            actual_index = get_last_contact_index() + 1  #Recupera o maior index e adiciona 1 para ser o index do contato atual
            new_contact = Contact(actual_index, args.name, args.phonenumber)  #Cria instância de Contatos
            new_contact.save_to_db()  #Solicita a gravação no banco de dados
    elif args.command == 'modify':  #Verifica se o comando é 'modify'
        if check_name():        #Verifica se existe nome
            search_result = search_contact(args.name, args.command)  #Chama a função de busca, com o modo 'modify'
            modify_contact(search_result)  #Chama a função que altera os dados do contato
    elif args.command == 'del':  #Verifica se o comando é 'del'
        if check_name():        #Verifica se existe nome
            search_result = search_contact(args.name, args.command)  #Chama a função de busca, com o modo 'del'
            delete_contact(search_result)  #Chama a função que exclui o contato
    elif args.command == 'search':  #Verifica se o comando é 'search'
        if check_name():        #Verifica se existe nome
            search_contact(args.name)  #Chama a função de busca
    elif args.command == 'listall':  #Verifica se o comando é 'listall'
        search_contact(args.name, args.command)  #Chama a função de busca, com o modo 'listall'


def __get_config_file():
    ###Retorna o caminho do arquivo de configuração
    config_filepath = 'config.ini'  #Caminho do arquivo de configuração
    return config_filepath      #Retorna o caminho

def read_config(group, param):
    ###Lê as configurações do arquivo de configurações
    config_contents = configparser.ConfigParser()  #Nova instância da classe ConfigParser
    config_contents.read(__get_config_file())  #Lê todas as configurações do arquivo
    return config_contents.get(group, param)  #Retorna as configurações específicadas

def get_db_filepath():
    ###Recupera o caminho do banco de dados das configurações
    return read_config('db', 'dbfile')  #Recupera e retorna apenas o caminho do banco de dados

def search_contact(name_to_search, mode=None):
    ###Motor de busca de contato
    from core.Dao import Dao    #Importa a classe Dao
    db_contents = Dao()         #Nova instância da classe Dao
    search_result_list = db_contents.search(name_to_search, mode)  #Recebe o resultado da busca em lista
    if (mode == 'del') or (mode == 'modify'):  #Verifica o modo de execução, se for alteração ou exclusão
        return search_result_list  #Retorna a lista com o resultado da busca
    else:                       #Se for execução normal,
        show_search_result(search_result_list)  #Mostra o resultado da busca

def get_last_contact_index():
    ###Recupera o último index de contato usado
    from core.Dao import Dao    #Importa a classe Dao
    db_contents = Dao()         #Nova instância da classe Dao
    return db_contents.get_last_index()  #Recupera e retorna o último index

def delete_contact(list):
    ###Apaga um contato
    def __ask_to_delete():
        ###Subfunção que solicita o índice do contato a ser apagado, da lista de resultado de busca
        indexes_list = []       #Lista para os indexes de resultado da busca
        for contact in list:    #Para cada contato da lista
            indexes_list.append(int(contact['index']))  #Adiciona o index na lista
        if indexes_list:        #Se existir index na lista de busca
            index_to_delete = ask_message('Informe o índice do contato a ser excluído: ', indexes_list, int, 'green')  #Solicita
                                #o índice do contato a ser excluído
            return index_to_delete  #Retorna o index a ser excluído
        else:                   #Se não existe index no resultado da busca = busca vazia
            show_message(f'Contato não encontrado!', 'green')  #Mostra msg
    
    def __delete_from_db(index):
        ###Subfunção que solicita a exclusão do contato do banco de dados através da classe Contact
        from core.Contact import Contact
        contact_to_delete = Contact(index, '', '')  #Nova instância da classe Contact
        contact_to_delete.delete_contact(index)  #Solicita a exclusão do contato com o index determinado

    show_search_result(list)    #Mostra o resultado da busca
    index_to_delete = __ask_to_delete()  #Recebe o índice do contado escolhido pelo usuário
    if index_to_delete and confirm_to_delete(index_to_delete):  #Se existe index e a confirmação da exclusão
        __delete_from_db(index_to_delete)  #Chama a função de exclusão do contato
        show_message('Contato excluído com sucesso!', 'green')  #Mostra mensagem

def modify_contact(list):
    ###Altera dados de um contato
    def _ask_to_modify():
        ###Subfunção que pergunta ao usuário o contato a ser alterado
        indexes_list = []       #Lista para os indexes de resultado de busca
        for contact in list:    #Para cada contato da lista
            indexes_list.append(int(contact['index']))  #Adiciona o index na lista
        if indexes_list:        #Se existir index na lista de busca
            index_to_modify = ask_message('Informe o índice do contato a ser alterado: ', indexes_list, int, 'green')  #Solicita
                                #o índice do contato a ser alterado
            return index_to_modify  #Retorna o index a ser alterado
        else:                   #Se não existir index no resultado da busca = busca vazia
            show_message(f'Contato não encontrado!', 'green')  #Mostra msg

    def _get_actual_contact_infos(index):
        ###Subfunção que recupera os dados atuais do contato
        from core.Dao import Dao
        dao_conn = Dao()        #Nova instância da classe Dao
        for contact in dao_conn.db_contents:  #Para cada contato no banco de dados
            if index == int(contact['index']):  #Verifica se é o contato escolhido
                actual_name = contact['name']  #Recupera o nome atual do contato
                actual_phone = contact['phone']  #Recupera o telefone atual do contato
                break           #Interrompe o for assim que achar o contato
        return [actual_name, actual_phone]  #Retorna os dados atuais em lista
        
    def _check_infos(old, check):
        ###Subfunção que verifica se houve, de fato, alteração dos dados pelo usuário
        new = []                #Lista com os dados do contato
        if check[0] != '':      #Verifica se houve alteração do nome do contato
            new.append(check[0])  #Se houve alteração, salva na lista nova
        else:                   #Se não houve alteração
            new.append(old[0])  #Salva o nome que já existia na lista nova
        if check[1] != '':      #Verifica se houve alteração do telefone do contato
            new.append(check[1])  #Se houve alteração, salva na lista nova
        else:                   #Se não houve alteração
            new.append(old[1])  #Salva o telefone que já existia na lista nova
        return new              #Retorna a lista com os dados (atuais e/ou novos)

    def _get_new_contact_infos(index):
        ###Subfunção que recebe do usuário as novas informações do contato
        actual_infos = _get_actual_contact_infos(index)  #Lista com os dados atuais do contato no BD
        new_infos = [get_new_name(actual_infos[0]), get_new_phone(actual_infos[1])]  #Lista com as
                                #informações inseridas pelo usuário
        checked_infos = _check_infos(actual_infos, new_infos)  #Lista recebe as informações após
                                #checagem se houve alteração (nome e/ou telefone)
        if actual_infos != checked_infos:  #Verifica se houve alteração (nome e telefone)
            contact_modified = {'index': index,  #Novo dicionário após as informações serem conferidas
                                'name': checked_infos[0],
                                'phone': checked_infos[1]}
            return contact_modified  #Retorna os dados alterados
        else:                   #Se não houve nenhuma alteração
            show_message('O contato não foi alterado!', 'red')  #Mostra msg
            return False        #Retorna False

    def _save_changes_to_db(contact):
        ###Subfunção que chama a gravação das alterações no BD através da classe Contact
        from core.Contact import Contact
        contact_to_change = Contact('', '', '')  #Nova intância da classe Contact
        contact_to_change.change_contact(contact)  #Solicita a alteração passando todos os dados do contato

    show_search_result(list)    #Mostra o resultado da busca
    index_to_modify = _ask_to_modify()  #Recebe o índice do contado escolhido pelo usuário
    if index_to_modify:         #Se existe index para alteração de dados
        contact_has_changed = _get_new_contact_infos(index_to_modify)  #Solicita os novos dados do contato
        if contact_has_changed:  #Verifica se houve alguma alteração
            _save_changes_to_db(contact_has_changed)  #Solicita a gravação das alterações no BD
            show_message('Contato alterado com sucesso!', 'green')  #Mostra msg de sucesso