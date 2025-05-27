from Models import *
from Dao import *
from Controller import *


if __name__=='__main__':
    while True:
        desejo = int(input('Digite 1 para cadastrar um usuário\n'
                           'Digite 2 para fazer login\n'
                           'Digite 3 para sair: '))

        if desejo == 1:
            cad = UsuarioController()
            nome = input('Digite o nome: ')
            email = input('Digite o E-mail: ')
            senha = input('Digite a senha: ')

            cad.cadastrar_usuario(nome, email, senha)
        elif desejo ==2:
            log = UsuarioController()
            email = input('Digite o E-mail: ')
            senha = input('Digite a senha: ')

            log.logar_sistema(email, senha)

        elif desejo == 3:
            break

        else:
            print('Opção Inválida!')




