program_name = 'main.py'

def __clear_screen():
    from core.common import read_config
    config_contents = read_config()
    lines_to_cls = int(config_contents.get('general', 'lines_to_cls'))
    print('\n' * lines_to_cls)

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

        len_cod = 8
        len_name = 30
        len_phone = 20
        first_line = 'CÓDIGO'.center(len_cod) + 'NOME'.center(len_name) + 'TELEFONE'.center(len_phone)
        print(first_line)
        print('-' * len(first_line))
        for index, contact in enumerate(list):
            contact_line = str(contact['index']).center(len_cod) + contact['name'].ljust(len_name) + contact['phone'].ljust(len_phone)
            if index % 2:
                print(f'\x1b[0;37;40m{contact_line}\x1b[0m')
            else:
                print(f'\x1b[0;30;47m{contact_line}\x1b[0m')
        print('-' * len(first_line))
        print(f'Total de contatos encontrados: {len(list)}')

def show_usage():
    print('\n')
    __show_header()
    print('Usage:\n')
    print(f'{program_name} <command> <options>|<contact infos>\n')
    print('Commands: add\tAdd a new contact to data base')
    print('\tmodify\tChange contact name and/or phone number')
    print('\tdel\tDelete one contact from data base')
    print('\tsearch\tSearch for a contact by name')
    print('\tlistall\tList all contacts')
    print('\thelp\tShow this help message')
    print('Examples:\n')
    print(f'- Adding a new contact: "{program_name} add contact_name contact_phone_number"')
    print(f'- Modifing a contact: "{program_name} modify contact_name"')
    print(f'- Deleting a contact: "{program_name} del contact_name"')
    print(f'- Searching a contact: "{program_name} search contact_name"')
    print(f'- List all contacts: "{program_name} listall"')
    print(f'- List all contacts: "{program_name} listall"')
    print(f'- Help: "{program_name} help"')
    print(f'\nTo list all contacts with certain letter, use search command and desired\nletter as option: Type "{program_name} search b" to search all contacts with "b" letter')
    print(f'\nYou can search by name part. Type "{program_name} search Crist" to search for "Cristopher"')

def final_message():
    print('\nPrograma finalizado.\n\n')

def show_message(msg, color=None):
    #Available colors: green and red
    if color == 'red':
        print(f'\n\x1b[1;37;41m' + msg + '\x1b[0m\n')  #bgcolor = red; color = white
    elif color == 'green':
        print(f'\n\x1b[6;30;42m' + msg + '\x1b[0m\n')  #bgcolor = green; font color = black
    else:
        print(msg)

def check_input(msg, options_list, input_type):
    user_input = input(msg)
    if input_type == int:
        try:
            user_input = int(user_input)
        except:
            show_message('Opção inválida! Tente novamente.', 'red')
            return False
        else:
            if not user_input in options_list:
                show_message('Índice inválido! Tente novamente.', 'red')
                return False
            else:
                return user_input
    else:
        if user_input not in options_list:
            show_message('Opção inválida! Tente novamente.', 'red')
            return False
        else:
            return user_input


def ask_message(msg, options_list, input_type, color=None):
    #Available colors: green and red
    if color == 'red':
        index_choice = check_input(f'\n\x1b[6;30;42m' + msg + '\x1b[0m ', options_list, input_type)  #bgcolor = green; font color = black
        return index_choice
    elif color == 'green':
        index_choice = check_input(f'\n\x1b[6;30;42m' + msg + '\x1b[0m ', options_list, input_type)  #bgcolor = green; font color = black
        return index_choice
    else:
        index_choice = check_input(f'{msg} ', options_list, input_type)
        return index_choice
    
def confirm_to_delete(index):
    return True if ask_message('Tem certeza que deseja excluir o contato (S/n)?', ['S', 'n'], str, 'red') == 'S' else show_message('\nExclusão abortada.')
        
def get_new_name(actual_name):
    print(f'\nNome atual do contato: {actual_name}')
    return input('Novo nome do contato (ENTER para não alterar): ')

def get_new_phone(actual_phone):
    print(f'\nTelefone atual do contato: {actual_phone}')
    return input('Novo telefone do contato (ENTER para não alterar): ')