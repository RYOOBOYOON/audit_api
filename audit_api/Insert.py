#-*- coding: utf-8 -*-

# 담당자 입력
def manger(id,day1,day2,criteri1,criteri2,disposition1,disposition2) :
    with open(f'./FILE_TXT/MANGER_TXT/{id}.txt', "w", encoding='UTF-8') as f:
        f.write(f'법규마감일 : {day1}\n계획마감일 : {day2}\n증거기반 : {criteri1}\n전문적기준 : {criteri2}\n공식수용처분 : {disposition1}\n실제기여처분 : {disposition2}')
        f.close()

# 인터뷰 입력
def interview(id,Suggestion1,Suggestion2,analysis,Help,Help_res,Cooperation,actuality) :
    with open(f'./FILE_TXT/INTERVIEW_TXT/{id}.txt', "w", encoding='UTF-8') as f:
        f.write(f'제공된감사정보및제언 : {Suggestion1}\n검토된감사정보및제언 : {Suggestion2}\n제공된감사의재정적분석내용 : {analysis}\n도움을인정하는피감기관고위관리층 수 : {Help}\n도움을인정하는피감기관고위관리층 비율 : {Help_res}\n협력적관계및접촉 : {Cooperation}\n실제감사에활용 : {actuality}')
        f.close()

# 전문가 입력
def expert(id,expert,participation,Development,Usage,expert_result,participation_result,Development_result,Usage_result):
    with open(f'./FILE_TXT/EXPERT_TXT/{id}.txt', "w", encoding='UTF-8') as f:
        f.write(f'\n보유전문감사인력수 : {expert},\n실제참여전문감사인력수 : {participation}\n개발하여보유중인감사기법수 : {Development}\n분석에사용된감사기법수 : {Usage}\n보유전문감사인력비율 : {expert_result}\n실제참여전문감사인력비율 : {participation_result}\n개발하여보유중인감사기법비율 : {Development_result}\n분석에사용된감사기법비율 : {Usage_result}')
        f.close()