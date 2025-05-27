from Models import Usuario, engine
from sqlmodel import SQLModel, Session, select
from Utils import Criptografia


class UsuarioDao():
    @classmethod
    def salvar_usuario(cls, usuario:Usuario):
        with Session(engine) as session:
           session.add(usuario)
           session.commit()

    @classmethod
    def verificar_email(cls, email):
        with Session(engine) as session:
            statement = select(Usuario).where(Usuario.email == email)
            results = session.exec(statement).all()

            if len(results) > 0:
                # print('Email OK')
                return True
            else:
                # print('Email existente')
                return False

    @classmethod
    def verificacao_de_senha(cls, email, senha):
        with Session(engine) as session:
            statement = select(Usuario).where(Usuario.email == email)
            usuario = session.exec(statement).first()

            if usuario:
                senha_hash = usuario.senha.encode('utf-8')

                return Criptografia.verificar_senha(senha, senha_hash)
            else:
                return False




            

