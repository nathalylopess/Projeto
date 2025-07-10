from typing import List,Annotated
from sqlmodel import SQLModel,Session,create_engine,select
from fastapi import FastAPI,Depends
from models import Aluno
from contextlib import asynccontextmanager

url = "sqlite:///banco.db"
# PostgreSQL - psycopg2-binary
urlpg = "postgresql://usuario:senha@localhost/banco"
#Mysql - pymysql
urlmysql = "mysql+pymysql://usuario:senha@localhost/banco"
args = {"check_same_thread": False}
engine = create_engine(url,connect_args=args)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def get_create_db():
    SQLModel.metadata.create_all(engine)
    
@asynccontextmanager
async def lifespan(app:FastAPI):
    get_create_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/alunos")
def alunos(session:SessionDep)-> List[Aluno]:
    alunos = session.exec(select(Aluno)).all()
    return alunos
