"""
Grupo DEV Carlo Acutis - Bruno Faria

Registrar em arquivo local nome e número de telefone
- Funcionalidades: inserir, excluir, alterar, "olhar"
- "Olhar": lista tabular de contatos em ordem alfabética com nome e telefone
- Busca de contatos por nome insensível

brunofariasilva@gmail.com
31/05/2025 - 16/06/2025

Problemas conhecidos:
- 

Implementar:
- 
"""

import argparse
from core.front import final_message
from core.common import check_and_run_command

def main():
    args = __build_and_get_args()  #Constrói e recupera os argumentos da linha de comando
    check_and_run_command(args)  #Verifica e executa os comandos passando os argumentos
    final_message()             #Mostra mensagem final

def __build_and_get_args():
    ###Função que constrói os argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Armazena e gerencia contatos telefônicos')
    parser.add_argument('command', choices=['add', 'modify', 'del', 'search', 'listall'])
    parser.add_argument('-n', '--name', type=str.title, help='Especifica o nome do contato')
    parser.add_argument('-p', '--phonenumber', help='Especifica o telefone do contato')
    return parser.parse_args()

if __name__ == "__main__":
    main()
