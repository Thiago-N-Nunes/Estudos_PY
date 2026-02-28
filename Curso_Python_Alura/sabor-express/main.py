import os

print("""🅂🄰🄱🄾🅁 🄴🅇🄿🅁🄴🅂🅂""")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')
escolha_do_user = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('cls')
    print('Finalizou app\n')



if escolha_do_user == 1:
    print('Cadastrar restaurante')
elif escolha_do_user == 2:
    print('Listar restaurante')
elif escolha_do_user == 3:
    print('Ativar restaurante')
else:
    finalizar_app()