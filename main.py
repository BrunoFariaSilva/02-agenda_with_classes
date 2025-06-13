"""
Grupo DEV Carlo Acutis - Bruno Faria

Registrar em arquivo local nome e número de telefone
- Funcionalidades: inserir, excluir, alterar, "olhar"
- "Olhar": lista tabular de contatos em ordem alfabética com nome e telefone
- Busca de contatos por nome insensível

brunofariasilva@gmail.com
31/05/2025 - 06/06/2025

Problemas conhecidos:
1 - Listagem alfabética não considera acentos, fazendo com que a lista de nomes que começam
    com acento comece no final da lista dos que não tem acento   
2 - Busca não funciona corretamente com acentos

Implementar:
- 
"""

import argparse
from core.front import final_message
from core.common import check_and_run_command

def main():
    args = __build_and_get_args()
    check_and_run_command(args)
    final_message()

def __build_and_get_args():
    parser = argparse.ArgumentParser(description='Armazena e gerencia contatos telefônicos')
    parser.add_argument('command', choices=['add', 'modify', 'del', 'search', 'listall'])
    parser.add_argument('-n', '--name', type=str.title, help='Especifica o nome do contato')
    parser.add_argument('-p', '--phonenumber', help='Especifica o telefone do contato')
    return parser.parse_args()

if __name__ == "__main__":
    main()
