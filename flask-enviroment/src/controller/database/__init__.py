from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from src.enviroment import getElement

engine = create_engine(getElement("SQLALCHEMY_DATABASE_URI"))
sessionObj = sessionmaker(bind=engine)