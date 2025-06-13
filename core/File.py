from core.common import get_db_filepath
from core.front import show_message
from pathlib import Path
import json

class File:
    def __init__(self):
        ###Construtor da classe
        self.json_file = Path(get_db_filepath())  #Recupera o caminho e nome do arquivo de BD
        self.__check_file()     #Chama a verificação da existência do arquivo

    def __check_file(self):
        ###Método que verifica a existência do arquivo de BD
        if not self.json_file.exists():  #Se o arquivo não existe
            show_message('Arquivo de banco de dados não encontrado!', 'red')
            self.__create_file()  #Chama a criação do arquivo

    def __create_file(self):
        ###Método que cria o arquivo de BD
        with self.json_file:    #Caminho do arquivo
            Path.touch(self.json_file, mode=0o777, exist_ok=False)  #Cria o arquivo na pasta
            show_message('Arquivo de banco de dados criado com sucesso!', 'green')
        self.__initialize_file()  #Chama a inicialização do arquivo vazio criado

    def __initialize_file(self):
        ###Método que inicializa o arquivo vazio criado
        init_list = []          #Lista vazia a ser inserida no arquivo
        with open(self.json_file, 'w', newline='\n') as file_to_initialize:  #Abre o arquivo para gravação
            json.dump(init_list, file_to_initialize, indent=4)  #Faz o dump json da lista no arquivo
            show_message('Arquivo de banco de dados inicializado com sucesso!', 'green')

    def read_file(self):
        ###Método para leitura do arquivo
        with open(self.json_file, 'r', newline='\n') as file_to_read:  #Abre o arquivo para leitura
            file_contents = json.load(file_to_read)  #Faz a leitura json no conteúdo do arquivo
        return file_contents    #Retorna o conteúdo do arquivo em lista

    def save_file(self, dict):
        ###Método para gravação de dados
        with open(self.json_file, 'w', newline='\n') as file_to_save:  #Abre o arquivo para gravação
            json.dump(dict, file_to_save, indent=4)  #Faz o dump json da lista de contatos no arquivo
