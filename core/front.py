def __clear_screen():
    print('\n' * 30)

def __show_header():
    print('AGENDA DE TELEFONES DO SEU JOÃO')
    print('===============================\n')

def __show_sub_header():
    print('RESULTADO DA BUSCA')
    print('------------------\n')

def show_search_result(list):
    if list:
        __clear_screen()
        __show_header()
        __show_sub_header()
        for index, contact in enumerate(list):
            print(f'{index+1} - Nome: {contact['name']} \tTelefone: {contact['phone']}')
        print('\n')
