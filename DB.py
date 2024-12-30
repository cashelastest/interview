import sqlalchemy as db
from sqlalchemy.orm import Session,as_declarative
from sqlalchemy import Integer, String

db_config ={
    "username":"root",
    "password":"",
    "host":"localhost",
    "port":"3306",
    "db_name":"interview"
}
engine = db.create_engine(f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config["port"]}/{db_config["db_name"]}")
session = Session(engine)


@as_declarative()
class BaseModel:
    id = db.Column("id",Integer,autoincrement=True, primary_key=True)
class User(BaseModel):
    __tablename__ = "users"
    username = db.Column("username", String,unique=True, primary_key=True)
    def __init__(self,username):
        self.username= username

def init_db():
    BaseModel.metadata.create_all(bind=engine)

def insert_data(username):
    user = User(username)
    try:
        session.add(user)
        session.commit()
        
    except:
        return "Такий юзернейм вже існує"

    return "Користувача додано!"
