"""
Grupo DEV Carlo Acutis - Bruno Faria

Registrar em arquivo local nome e número de telefone
- Funcionalidades: inserir, excluir, alterar, "olhar"
- "Olhar": lista tabular de contatos em ordem alfabética com nome e telefone
- Busca de contatos por nome insensível

brunofariasilva@gmail.com
31/05/2025 - 

Problemas conhecidos:
1 - Solicita índice para exclusão mesmo sem nenhum contato na lista de busca
2 - Solicita índice para alteração mesmo sem nenhum contato na lista de busca

Implementar:
1 - Totalizador de contatos no 'listall'
2 - Totalizador de contatos no 'search'
3 - Melhorar a exibição da lista de contatos (listall e search)
"""

import sys
from core.Args import Args
from core.front import final_message

def main():
    args = __build_and_get_args()
    args.check_and_run_command(args.command)
    final_message()

def __build_and_get_args():
    args = Args(sys.argv)
    return args

if __name__ == "__main__":
    main()
