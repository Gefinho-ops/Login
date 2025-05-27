from Models import *
from Dao import *
from Utils import Criptografia

class UsuarioController():
    def cadastrar_usuario(self, nome, email, senha):
        if nome and email and senha:
            if not UsuarioDao.verificar_email(email):
                if Criptografia.senha_valida(senha):
                    nova_senha = Criptografia.criptografar_senha(senha)
                    senha_verificada = nova_senha.decode('utf-8')
                    usuario = Usuario(nome=nome, email=email, senha=senha_verificada)                        #sqlmodel requer argumentos nomeados (nome=nome)
                    UsuarioDao.salvar_usuario(usuario)
                    print('Usuário cadastrado com sucesso!')
                else:
                    print('Senha fraca! sua senha deve conter letras, números e ao menos 8 caracteres.')
            else:
                print('E-mail já existente no banco de dados!')
        else:
            print('Preencha todos os dados!')

    def logar_sistema(self, email, senha):
        if UsuarioDao.verificar_email(email):
            if UsuarioDao.verificacao_de_senha(email, senha):
                print('Login realizado com sucesso')
            else:
                print('senha incorreta')
        else:
            print('E-mail incorreto')



