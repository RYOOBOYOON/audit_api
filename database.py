import sqlalchemy
import database

database = 'sqlite:///./audit.db'

engine = sqlalchemy.create_engine(
    database,
    connect_args={'check_same_thread' : False}
)