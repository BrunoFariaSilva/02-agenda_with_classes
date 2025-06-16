from core.common import normalize_word
from core.Dao import Dao

class Contact:
    def __init__(self, index, name, phone):
        ###Construtor do contato
        self.index = index      #Atributos da classe
        self.name = name
        self.normalized_name = normalize_word(self.name)
        self.phone = phone

    def save_to_db(self):
        ###Método para salvar o novo contato no BD
        new_contact_dict = {'index': self.index,  #Dicionário com as informações do contato
                            'name': self.name.title(),
                            'normalized_name': self.normalized_name,
                            'phone': self.phone}
        dao_conn = Dao()        #Instancia para conexão com a classe DAO
        dao_conn.save_contact(new_contact_dict)  #Solicita a gravação do contato no BD
        from core.front import show_message  #Importação da função de mensagem ao usuário
        show_message(f'Contato "{new_contact_dict['name']}" adicionado com sucesso!', 'green')  #Mostra msg de sucesso

    def delete_contact(self, index_to_delete):
        ###Método para exclusão de um contato
        dao_conn = Dao()        #Instancia para conexão com a classe DAO
        dao_conn.delete_from_db(index_to_delete)  #Solicita a exclusão do contato passando o index

    def change_contact(self, contact):
        ###Método para alteração do contato
        dao_conn = Dao()        #Instancia para conexão com a classe DAO
        dao_conn.change_contact(contact)  #Solicita a alteração do contato passando todos os dados
        