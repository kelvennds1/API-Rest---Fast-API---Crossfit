from fastapi import APIRouter
from workout_api.centro_treinamento.controller import router as centro_treinamento
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['Aletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['Categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['Centros Treinamento'])


