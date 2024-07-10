from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT Fire', max_length=50)] 
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='SHS 12, Lote 1 - Asa Sul', max_length=60)]   
    proprietario: Annotated[str, Field(description='Proprietário do  Centro de Treinamento', example='Felipe', max_length=30)]   


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT Fire', max_length=50)] 


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Indentificador do centro de treinamento')]

    
