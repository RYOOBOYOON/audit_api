from typing import List
from fastapi import FastAPI, UploadFile, File, Request
from sqlalchemy.sql import expression

import uvicorn

from model import *
from database import *

from audit_api.Crwilng import *
from audit_api.List import *
from audit_api.algorithm import *
from audit_api.Insert import *
from audit_api.score import *

import datetime

app = FastAPI()

#크롤링
@app.get("/v1/crawling/{org}")
async def crawling(org):
    try :
        if org == 'edu':
            EC()
        elif org == "nso":
            NC()

        return {"result":"OK"}
    except :
        return {'result':'false'}


#현재 감사성과파일 이름 출력
@app.get("/v1/have/{org}")
async def have(org):
        
    li = ''
    try :
        if org == 'edu' :
            li = EL()
        elif org == 'nso' :
            li = NL()

        return {"result": li}
    except :
        return {"result":"FAIL"}

#pdf 추출(감사기간,증거,법령,처분건수)
@app.post("/v1/pdf_parser/{org}")
async def pdf_parser(org,data : parsers):
    from tika import parser
    for name in data.names :
        sp = ''
        if org == 'edu' :
            f = open(f'./pdf_file/EC_result_report/pdf_url/{name}.txt','r')
            file = f.readline()
            f.close()
            files = parser.from_file(file)
            files = files['content'] 
            files = files.split("\n")
            
            sp = ES(files)

            with open(f'./FILE_TXT/ALGORITHM_TXT/{name[:14]}.txt', 'w', encoding='UTF-8') as f:
                f.write(f'\n감사기간 : {int(sp[0])}\n처분개수 : {int(sp[1])}\n전문적기준 : {int(sp[2])}\n증거기반 : {int(sp[3])}')
                f.close()
                
        elif org == 'nso' :
            f = open(f'./pdf_file/SO_result_report/pdf_url/{name}.txt','r')
            file = f.readline()
            f.close()
            files = parser.from_file(file)
            files = files['content'] 
            files = files.split("\n")

            sp = NS(files)

            with open(f'./FILE_TXT/ALGORITHM_TXT/{name[:14]}.txt', 'w', encoding='UTF-8') as f:
                f.write(f'\n감사기간 : {int(sp[0])}\n처분개수 : {int(sp[1])}\n전문적기준 : {int(sp[2])}\n증거기반 : {int(sp[3])}')
                f.close()

        return {"result":sp}


@app.post("/uploadfiles")
async def create_upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "./userfile"
    from tika import parser
    import re

    try :
        for file in files:
            id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            contents = await file.read()
            name = id+'_'+file.filename #파일이름
            fname = UPLOAD_DIRECTORY +'/' + name #파일저장경로
            with open(fname, "wb") as fp:
                fp.write(contents)

            files = parser.from_file(fname)
            files = files['content'] 
            files = files.split("\n")
            try : 
                sp = ES(files)
                with open(f'./FILE_TXT/ALGORITHM_TXT/{name[:14]}.txt', 'w', encoding='UTF-8') as f:
                    f.write(f'\n감사기간 : {int(sp[0])}\n처분개수 : {int(sp[1])}\n전문적기준 : {int(sp[2])}\n증거기반 : {int(sp[3])}')
                    f.close()
                return sp

            except :
                sp = NS(files)
                with open(f'./FILE_TXT/ALGORITHM_TXT/{name[:14]}.txt', 'w', encoding='UTF-8') as f:
                    f.write(f'\n감사기간 : {int(sp[0])}\n처분개수 : {int(sp[1])}\n전문적기준 : {int(sp[2])}\n증거기반 : {int(sp[3])}')
                    f.close()
                return sp

    except expression as k:
        return k

@app.post('/urlupload')
async def url_upload(request : Request, data : parsers):
    from tika import parser

    for name in data.names :
        
        files = parser.from_file(name)
        files = files['content'] 
        files = files.split("\n")
        print('1')

        try :
            sp = ES(files)
            print('2')
            num = 1
            a=f'test{num}'
            with open(f'./FILE_TXT/ALGORITHM_TXT/{a}.txt', 'w', encoding='UTF-8') as f:
                f.write(f'\n감사기간 : {int(sp[0])}\n처분개수 : {int(sp[1])}\n전문적기준 : {int(sp[2])}\n증거기반 : {int(sp[3])}')
                f.close()
            num+=1
            return sp

        except :
            sp = NS(files)
            num = 1
            a=f'test{num}'
            with open(f'./FILE_TXT/ALGORITHM_TXT/{a}.txt', 'w', encoding='UTF-8') as f:
                f.write(f'\n감사기간 : {int(sp[0])}\n처분개수 : {int(sp[1])}\n전문적기준 : {int(sp[2])}\n증거기반 : {int(sp[3])}')
                f.close()
            num+=1
            return sp




# 담당자 점수 입력
@app.post("/v1/manger")
async def manger_insert(data:Item_manger) :
    
    try :
        manger(data.id,#1
        data.day1,#2
        data.day2,#3
        data.criteri1,#4
        data.criteri2,#5
        data.disposition1,#6
        data.disposition2#7
        )
        
        with engine.begin() as conn:
            conn.execute(audit_manger.insert(), data.dict())

        return {"result":"OK"}
    except Exception as kk:
        return {"result":str(kk)}

# 인터뷰 점수 입력
@app.post("/v1/interview")
async def interview_insert(data:Item_interview) :
    
    try :
        interview(    
        data.id,#1
        data.Suggestion1,#8
        data.Suggestion2,#9
        data.analysis,#10
        data.Help,#11
        data.Help_res,#12
        data.Cooperation,#13
        data.actuality#14
        )

        with engine.begin() as conn:
            conn.execute(audit_interview.insert(), data.dict())

        return {"result":"OK"}
    except Exception as kk:
        return {"result":str(kk)}

# 전문가 점수 입력
@app.post("/v1/expert")
async def expert_insert(data:Item_expert) :
    
    try :
        expert(
        data.id,#1
        data.expert,#15
        data.participation,#16
        data.Development,#17
        data.Usage,#18
        data.expert_result,#19
        data.participation_result,#20
        data.Development_result,#21
        data.Usage_result#22
        )
        
        with engine.begin() as conn:
            conn.execute(audit_expert.insert(), data.dict())

        return {"result":"OK"}
    except Exception as kk:
        return {"result":str(kk)}


#3개 txt 파일이 있을경우 리스트 출력
@app.get("/v1/avail")
async def avail():
    li = ''
    li = last_list()
    return {"result": li}

#점수
@app.post("/v1/score")
async def total_score(data:Score):
    Score_res = score(data.names,data.count_threshold)
    return {"result":Score_res}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=20113)