import sqlalchemy
from pydantic import BaseModel
from typing import List
from database import engine
from sqlalchemy import MetaData


metadata = MetaData()

audit_algorithm = sqlalchemy.Table(
    'audit_algorithm',
    metadata,
    sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key=True),# ID
    sqlalchemy.Column('Period', sqlalchemy.Integer),# algorithm1
    sqlalchemy.Column('The_number_of_dispositions', sqlalchemy.Integer),# algorithm2
    sqlalchemy.Column('Professional_standards', sqlalchemy.Integer),# algorithm3
    sqlalchemy.Column('Evidence_based', sqlalchemy.Integer),# algorithm4
)
metadata.create_all(engine)


audit_manger = sqlalchemy.Table(
    'audit_manger',
    metadata,
    sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key=True),# ID
    sqlalchemy.Column('day1', sqlalchemy.Integer),# manger1
    sqlalchemy.Column('day2', sqlalchemy.Integer),# manger2
    sqlalchemy.Column('criteri1', sqlalchemy.Integer),# manger3
    sqlalchemy.Column('criteri2', sqlalchemy.Integer),# manger4
    sqlalchemy.Column('disposition1', sqlalchemy.Integer),# manger5
    sqlalchemy.Column('disposition2', sqlalchemy.Integer),# manger6
)
metadata.create_all(engine)


audit_interview = sqlalchemy.Table(
    'audit_interview',
    metadata,
    sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key=True),# ID
    sqlalchemy.Column('Suggestion1', sqlalchemy.Integer),# interview1
    sqlalchemy.Column('Suggestion2', sqlalchemy.Integer),# interview2
    sqlalchemy.Column('analysis', sqlalchemy.String),# interview3
    sqlalchemy.Column('Help', sqlalchemy.Integer),# interview4
    sqlalchemy.Column('Help_res', sqlalchemy.Integer),# interview5
    sqlalchemy.Column('Cooperation', sqlalchemy.Integer),# interview6
    sqlalchemy.Column('actuality', sqlalchemy.Integer),# expert1
    sqlalchemy.Column('expert', sqlalchemy.Integer),# expert2
    sqlalchemy.Column('participation', sqlalchemy.Integer),# expert3
    sqlalchemy.Column('Development', sqlalchemy.Integer),# expert4
    sqlalchemy.Column('Usage', sqlalchemy.Integer),# expert5
    sqlalchemy.Column('expert_result', sqlalchemy.Integer),# expert6
    sqlalchemy.Column('participation_result', sqlalchemy.Integer),# expert7
    sqlalchemy.Column('Development_result', sqlalchemy.Integer),# expert8
    sqlalchemy.Column('Usage_result', sqlalchemy.Integer)# expert9
)
metadata.create_all(engine)

audit_expert = sqlalchemy.Table(
    'audit_expert',
    metadata,
    sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key=True),# ID
    sqlalchemy.Column('actuality', sqlalchemy.Integer),# expert1
    sqlalchemy.Column('expert', sqlalchemy.Integer),# expert2
    sqlalchemy.Column('participation', sqlalchemy.Integer),# expert3
    sqlalchemy.Column('Development', sqlalchemy.Integer),# expert4
    sqlalchemy.Column('Usage', sqlalchemy.Integer),# expert5
    sqlalchemy.Column('expert_result', sqlalchemy.Integer),# expert6
    sqlalchemy.Column('participation_result', sqlalchemy.Integer),# expert7
    sqlalchemy.Column('Development_result', sqlalchemy.Integer),# expert8
    sqlalchemy.Column('Usage_result', sqlalchemy.Integer)# expert9
)
metadata.create_all(engine)

class Item_manger(BaseModel) :
    id : int #0
    day1 : int#2
    day2: int#3
    criteri1: int#4
    criteri2: int#5
    disposition1: int#6
    disposition2 : int#7

class Item_interview(BaseModel) :
    id : int #0
    Suggestion1 : int#8
    Suggestion2 : int#9
    analysis : int#10
    Help : int#11
    Help_res : int#12
    Cooperation : int#13
    actuality : int#14

class Item_expert(BaseModel) :
    id : int #0
    expert : int#15
    participation : int#16
    Development : int#17
    Usage : int#18
    expert_result : int#19
    participation_result : int#20
    Development_result :int#21
    Usage_result : int#22
    

class Score(BaseModel) :
    names : List[str]
    count_threshold = 100

class parsers(BaseModel) :
    names : List[str]