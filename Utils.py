import bcrypt
import re


class Criptografia():
    @staticmethod
    def criptografar_senha(senha_descript: str) -> bytes:
        senha_cript = senha_descript.encode('utf-8')
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha_cript, salt)
        return senha_hash
    
    @staticmethod
    def verificar_senha(senha_descipt: str, senha_hash: bytes) -> bool:
        return bcrypt.checkpw(senha_descipt.encode('utf-8'), senha_hash)
    
    @staticmethod
    def senha_valida(senha: str) -> bool:
        return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', senha))
