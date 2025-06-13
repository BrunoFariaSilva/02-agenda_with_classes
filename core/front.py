program_name = 'main.py'

def __clear_screen():
    ###Função para limpar a tela
    from core.common import read_config  #Importa a função de leitura das configurações
    lines_to_cls = int(read_config('general', 'lines_to_cls'))  #Recupera a qtd de linhas para limpar a tela
    print('\n' * lines_to_cls)

def __show_header():
    ###Função que mostra o cabeçalho na tela
    print('AGENDA DE TELEFONES DO SEU JOÃO')
    print('===============================\n')

def __show_sub_header():
    ###Função que mostra o subcabeçalho na tela
    print('RESULTADO DA BUSCA')
    print('------------------\n')

def show_search_result(list):
    ###Função que mostra o resultado da busca
    if list:                    #Se existir resultado na lista de busca
        __clear_screen()        #Limpa a tela
        __show_header()         #Mostra o cabeçalho
        __show_sub_header()     #Mostra o subcabeçalho

        len_cod = 8             #Tamanho da coluna para código do contato
        len_name = 30           #Tamanho da coluna para nome do contato
        len_phone = 20          #Tamanho da coluna para telefone do contato
        first_line = 'CÓDIGO'.center(len_cod) + 'NOME'.center(len_name) + 'TELEFONE'.center(len_phone)
                                #Primeira linha da tabela
        print(first_line)       #Mostra primeira linha
        print('-' * len(first_line))
        from core.common import read_config  #Importa a função de configurações
        lines_to_pause = int(read_config('general', 'lines_to_pause'))  #Recupera a informação de qtd de linhas para pausar a listagem
        for index, contact in enumerate(list):  #Varre toda a lista de resultado
            contact_line = str(contact['index']).center(len_cod) + contact['name'].center(len_name) + contact['phone'].center(len_phone)
                                #Concatena as informações em colunas, centralizada em cada uma
            if index % 2:       #Verifica a alternância de uma linha para outra
                print(f'\x1b[0;37;40m{contact_line}\x1b[0m')    #Mostra a linha em uma cor
            else:               
                print(f'\x1b[0;30;47m{contact_line}\x1b[0m')    #Mostra a linha de outra cor
            if (len(list) > 20) and ((index > 0) and (index % lines_to_pause == 0)):  #Se a listagem possui mais de 20 resultados,
                                #E chegou na contagem de linhas para pausar, excluindo o primeiro index
                show_message('Pressione ENTER para continuar...', 'green')  #Mostra msg
                input()         #Insere uma input vazia
        print('-' * len(first_line))
        print(f'Total de contatos encontrados: {len(list)}')
    else:                       #Se a lista de resultados é vazia
        show_message('Nenhum contato encontrado.', 'red')

def final_message():
    ###Função que mostra a mensagem de finalização do programa
    print('\nPrograma finalizado.\n\n')

def show_message(msg, color=None):
    ###Função que mostra mensagens ao usuário
    ##Recebe a mensagem e a cor
    #Available colors: green, red and None
    if color == 'red':
        print(f'\n\x1b[1;37;41m' + msg + '\x1b[0m\n')  #bgcolor = red; color = white
    elif color == 'green':
        print(f'\n\x1b[6;30;42m' + msg + '\x1b[0m\n')  #bgcolor = green; font color = black
    else:
        print(msg)

def check_input(msg, options_list, input_type):
    ###Função que trata a input do usuário conforme os parâmetros
    ##Recebe a mensagem, a lista de opções, o tipo da input
    user_input = input(msg)     #Recebe a input do usuário
    if input_type == int:       #Verifica se o tipo é inteiro
        try:                    #Tenta...
            user_input = int(user_input)  #Converter para inteiro
        except:                 #Se não conseguir,
            show_message('Opção inválida! Tente novamente.', 'red')  #Mostra msg de erro
            return False        #Retorna falso
        else:                   #Se conseguir converter
            if not user_input in options_list:  #Verifica se a input é inválida conforme a lista recebida
                show_message('Índice inválido! Tente novamente.', 'red')  #Mostra msg
                return False    #Retorna falso
            else:               #Se for válida
                return user_input  #Retorna a input
    else:                       #Para todos os outros tipos de input
        if user_input not in options_list:  #Verifica se a input é inválida conforme a lista recebida
            show_message('Opção inválida! Tente novamente.', 'red')  #Mostra msg
            return False        #Retorna falso
        else:                   #Se for válida
            return user_input   #Retorna a input


def ask_message(msg, options_list, input_type, color=None):
    ###Função que mostra mensagens ao usuário e aguarda a confirmação
    ##Recebe a mensagem, a lista de opções, o tipo da input e a cor
    #Available colors: green, red and None
    if color == 'red':
        index_choice = check_input(f'\n\x1b[6;30;42m' + msg + '\x1b[0m ', options_list, input_type)
                                #bgcolor = green; font color = black
        return index_choice
    elif color == 'green':
        index_choice = check_input(f'\n\x1b[6;30;42m' + msg + '\x1b[0m ', options_list, input_type)
                                #bgcolor = green; font color = black
        return index_choice
    else:
        index_choice = check_input(f'{msg} ', options_list, input_type)  #No color
        return index_choice
    
def confirm_to_delete(index):
    ###Função que retorna a confirmação de exclusão do contato
    return True if ask_message('Tem certeza que deseja excluir o contato (S/n)?',
                               ['S', 'n'], str, 'red') == 'S' else show_message('\nExclusão abortada.')
        
def get_new_name(actual_name):
    ###Função que solicita o novo nome do contato
    print(f'\nNome atual do contato: {actual_name}')
    return input('Novo nome do contato (ENTER para não alterar): ')

def get_new_phone(actual_phone):
    ###Função que solicita o novo telefone do contato
    print(f'\nTelefone atual do contato: {actual_phone}')
    return input('Novo telefone do contato (ENTER para não alterar): ')