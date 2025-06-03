"""
Grupo DEV Carlo Acutis - Bruno Faria

Registrar em arquivo local nome e número de telefone
- Funcionalidades: inserir, excluir, alterar, "olhar"
- "Olhar": lista tabular de contatos em ordem alfabética com nome e telefone
- Busca de contatos por nome insensível

brunofariasilva@gmail.com
31/05/2025 - 

Problemas conhecidos:
1 - Checagem de argumentos ainda não funciona corretamente
2 - Busca por parte do nome não funciona
3 - 
"""

import sys
from core.Contact import Contact
from core.common import search_contact
from core.front import show_usage, final_message

def main():
    args = __get_args()
    __go_to_commands(args)
    final_message()

def __get_args():
    args = sys.argv
    args.pop(0)
    return args

def __go_to_commands(args):
    def _change_args_to_infos():
        name = args[1:-1]
        name = ' '.join(name)
        phone = args[-1]
        return name, phone
    
    if args[0] == 'add':
        if __check_args(args, 'add'):
            name, phone = _change_args_to_infos()
            new_contact = Contact(name, phone)
            new_contact.save_to_db()
    elif args[0] == 'modify':
        if __check_args(args, 'modify'):
            pass
    elif args[0] == 'del':
        if __check_args(args, 'del'):
            pass
    elif args[0] == 'search':
        if __check_args(args, 'search'):
            name_to_search = args[1]
            search_contact(name_to_search)
    else:
        show_usage()

def __check_args(args, command):
    len_args = len(args)
    if command == 'add':
        if len_args >= 3:
            return True
        else:
            show_usage()
    elif (command == 'modify') or (command == 'del') or (command == 'search'):
        if len_args == 2:
            return True
        else:
            show_usage()

if __name__ == "__main__":
    main()
