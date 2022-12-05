def EC() :

    import time
    import requests
    from bs4 import BeautifulSoup
    import datetime

    

    def url_passer(url) :    
        
        response = requests.get(url)
        html_source = response.text
        soup = BeautifulSoup(html_source, 'html.parser')

        return soup

    edu = 'https://www.moe.go.kr/'
    for page in range(1,86) :
        url = f"{edu}boardCnts/list.do?type=default&page={page}&m=041202&boardID=345"
        contents = url_passer(url)
        contents = contents.select('.contents tr a') #css선택자로 리스트 a태그 전부 추출
        contents_cd = [[contents['onclick']] for contents in contents] #추출된 a태그중 onclick만 다시 추출
        #PDF 제목
        contents_title = [[contents['title']] for contents in contents] #추출된 a태그중 onclick만 다시 추출
        for index in range(0,len(contents_cd)//2) :#같은 값이 중복되어 //2를하여 반복
            name = "".join(contents_title[index])
            
            if name.find("종합") != -1:
                if name.find("계획") != -1 or name.find("결과") != -1:
                    #페이지 추출하기
                    num = "".join(contents_cd[index]) #추출한 contents_cd가 리스트이므로 한개씩 추출하여 문자열로 변환
                    num = num.split(",") #문자열로 변환된 값을 ,단위로 리스트로 변환
                    characters = "'" # '를 변수로 지정
                    num =num[1].strip() #필요한 값만 추출
                    num = ''.join( x for x in num if x not in characters) #characternum에 포함된 값을 삭제
                    url = f'{edu}boardCnts/view.do?boardID=345&boardSeq={num}&lev=0&searchType=null&statusYN=W&page={page}&s=moe&m=041202&opType=N'
                    #추출된 num값을 이용하여 다운로드 링크가 있는 웹페이지로 이동
                    contents = url_passer(url).select('.contents tr a')
                    pdf_href = [[contents['href']] for contents in contents] #a태그중 href태그를 추출
                    pdf_num = pdf_href[0] #추출된 값중 제일 앞의 값만 추출
                    pdf_num = "".join(pdf_num) #문자열로 변환
                    pdf_num = pdf_num.split(",")
                    characters = "'"
                    pdf_num = ''.join( x for x in pdf_num if x not in characters)
                    url = f'{edu}{pdf_num}'
                    
                    path = ''

                    if name.find("계획") != -1 :
                        name = name.replace('계획','')
                        name = name.replace('실시','')
                        path ='EC_report_plan'
                        

                    if name.find("결과") != -1 :
                        name = name.replace('결과','')
                        name = name.replace('공개','')
                        path = 'EC_result_report'

                    name = name.replace(' ','')
                    name1 = name+'.pdf'
                    name2 = name+'.txt'
                    id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                    
                    with open(f'./pdf_file/{path}/pdf_url/{id}_{name2}', "w") as f:
                        f.write(url)

                    resp = requests.get(url)

                    with open(f'./pdf_file/{path}/{id}_{name1}', "wb") as f:
                        f.write(resp.content)


                    time.sleep(0.5) #딜레이를 줌

def NC() :

    import time
    import requests
    from bs4 import BeautifulSoup
    import datetime

    

    def url_passer(url) :   
        
        response = requests.get(url)
        html_source = response.text
        soup = BeautifulSoup(html_source, 'html.parser')
        
        return soup
    
    NC = 'https://kostat.go.kr/'
    for page in (range(1,4)) :
        
        url = f"{NC}portal/korea/kor_ip/4/1/2/1/index.board?bmode=list&bSeq=&aSeq=&pageNo={page}&rowNum=10&navCount=10&currPg=&searchInfo=&sTarget=title&sTxt="
        #통계청
        file_urls = url_passer(url).select('.file_icons a') #css선택자로 리스트 a태그 전부 추출
        file_urls = [[file_urls ['href']] for file_urls in file_urls] #파일 주소

        file_name = url_passer(url).select('.file_icons img')
        file_name = [[file_name ['alt']] for file_name in file_name ] #파일 이름

        for index in (range(0,len(file_urls))) :

            url = "".join(file_urls[index])
            url = f"{NC}{url}"
            resp = requests.get(url)

            name = "".join(file_name[index])
            
            name = name.replace('결과','')
            name = name.replace('첨부파일','')
            name = name.split(' ')

            tst = ['' for i in range(0,len(name))]

            for tet in range(0,len(name)) :

                if tet == 0 :

                    tst[-1] = name[0]

                elif tet != 0 :

                    tst[tet-1] = name[tet]
            
            name = ''.join(tst)

            name1 = ''

            if name.find('pdf') != -1 :
                name = name.replace('pdf','')
                name1 = f'{name}.pdf'
            elif name.find('hwp') != -1 :
                name = name.replace('hwp','')
                name1 = f'{name}.hwp'
            
            name2 = name + '.txt'
            id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            with open(f'./pdf_file/SO_result_report/pdf_url/{id}_{name2}', "w") as f:
                        f.write(url)
            with open(f'./pdf_file/SO_result_report/{id}_{name1}', "wb") as f:
                        f.write(resp.content)
        
        time.sleep(0.5)