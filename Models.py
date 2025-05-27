from sqlmodel import SQLModel, Field, create_engine
from typing import Optional


class Usuario(SQLModel, table=True):
       
    id: int = Field(primary_key=True, default=None)
    nome: str = Field(default=None)
    email: str = Field(index=True)
    senha: str = Field(default=None)



engine = create_engine("sqlite:///Projeto_Login.db")
# SQLModel.metadata.create_all(engine)
