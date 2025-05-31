"""
Registrar em arquivo local nome e número de telefone
- Funcionalidades: inserir, excluir, alterar, "olhar"
- "Olhar": lista tabular de contatos em ordem alfabética com nome e telefone
- Busca de contatos por nome insensível
"""
import sys
from core.Contact import Contact
from core.common import search_contact

def main():
    args = __get_args()
    if check_args(args):
        go_to_commands(args)

def __get_args():
    args = sys.argv
    args.pop(0)
    return args

def go_to_commands(args):
    if args[0] == 'add':
        name = args[1]
        phone = args[2]
        new_contact = Contact(name, phone)
        new_contact.save_to_db()
    elif args[0] == 'modify':
        pass
    elif args[0] == 'del':
        pass
    elif args[0] == 'search':
        name_to_search = args[1]
        search_contact(name_to_search)

def check_args(args):
    if len(args) >= 2:
        return True

if __name__ == "__main__":
    main()
