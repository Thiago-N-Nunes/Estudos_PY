import os
restaurantes = ['Sushi', 'Pizza']

def exibir_nome_do_programa():
    print("""🅂🄰🄱🄾🅁 🄴🅇🄿🅁🄴🅂🅂""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('APP FINALIZADO')
    voltar_menu()

def voltar_menu():
    input('Digite uma tecla pra voltar pro menu principal')
    main()

def opcao_invalida():
    print("Opção Invalida")
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print (texto)
    print()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('CADASTRO DE NOVO RESTAURANTE')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('LISTANDO RESTAURANTES')
    
    for restaurante in restaurantes:
        print(f'.{restaurante}')
        
    
    voltar_menu()

def ecolher_opcao():
    try:
        escolha_do_user = int(input('Escolha uma opção: '))

        match escolha_do_user: 
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()    
    except:
        opcao_invalida()    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    ecolher_opcao()
    
if __name__ == '__main__':
    main()