from pydantic import BaseModel
from datetime import date
from typing import List

class Livro(BaseModel):
    titulo:str
    ano:int
    edicao:int