def ES(files):
    import re
    try :
        sp = []

        #날짜 추출
        Period = [v for v in files if "감사기간" in v][0] #files 안에 files를 찾음
        Period = "".join(Period) #str변환
        Period = Period.split('.')
        Pid = []
        for Per in Period :
            if Per!=Period[-1] :
                Pid.append(Per)
        Period = ''.join(Pid)
        Period = re.sub(r'[^0-9]','',Period)

        sp.append(Period)

        #처분건수
        fns = ['경징계','중징계','통보','시정','경고','주의','개선','수사의뢰','고발']
        fn = []
        for idx in fns :
            for file in range(0,len(files)) :
                if files[file].find(idx) != -1 :
                    if files[file].find('ㅇ') != -1 or files[file].find('◦') != -1 :
                        fn.append(file)
        fn = set(fn)
        fn = list(fn)
                            
        sp.append(len(fn))

        #키워드 추출
        finds = ['연번 지 적 사 항','데도,','있음']
        keys = [[],[],[]]
        for find in range(0,len(finds)) :
            for content in range(0,len(files)) :
                if files[content].find(finds[find]) != -1  :
                    if find != 1 :
                        keys[find].append(content+1)
                    else :
                        keys[find].append(content)

        #묶기
        scopes = []

        for first in range(0,len(keys[0])) : #keys값 각 지적사항별 분리
            serialls = []
            serialls.append(keys[0][first])
            for second in range(0,len(keys[1])) :
                if first+1<len(keys[0]) and keys[0][first] < keys[1][second] < keys[0][first+1] : #keys[1]값이 keys[0] 현재값보다 크고 다음값보다 작을때 추가 
                    serialls.append(keys[1][second])
                elif first+1==len(keys[0]) and keys[0][first] < keys[1][second] : #keys[0]의 다음 값이 없으면 나머지를 묶어줘
                    serialls.append(keys[1][second])
            if len(serialls)>1 : #위에 정리된 리스트중 값이 1개인것을 제외
                serialls.sort()
                scopes.append(serialls)
        for first in range(0,len(scopes)) :
            for second in range(0,len(keys[2])) :
                if first+1 < len(scopes) :
                    if scopes[first][0] < keys[2][second] < scopes[first+1][0] :
                        scopes[first].append(keys[2][second])
                elif first+1 == len(scopes) :
                    if scopes[first][0] < keys[2][second]:
                        scopes[first].append(keys[2][second])

        sp.append(len(scopes))

        #전문적증거(법령)
        tr = []
        content = []
        for aa in range(0,len(scopes)) :#법령범위
            con = []
            ct = []
            st = scopes[aa][0]
            end = scopes[aa][-1]
            result = files[st:end]
            for res in result :
                if res.find("따르면") !=-1 : #전문적기준은 '따르면' 한개에 기준 한개
                    con.append(res)
                
                elif res.find("붙임") != -1 : #증거 기반을 '붙임'의 개수로 기준
                    ct.append(res)

            if len(con) >= len(scopes[aa])-2 : #전문적기준이 지적사항-2 개수보다 많거나 같으면 
                tr.append(1)
            else :
                tr.append(0)

            if len(ct) >= len(scopes[aa])-2 : #증거기반이 있음 개수보다 많거나 같으면 
                content.append(1)
            else :
                content.append(0)
            
        sp.append(tr.count(1)/len(tr)*100)
        sp.append(content.count(1)/len(content)*100)

        

        return sp

    except :
        result = '완료하지 못하였습니다'
        return result


def NS(files) :
    import re

    sp = []

    

    Period = [v for v in files if "○ 감사기간" in v] #files[0] 안에 files[file]를 찾음
    Period = "".join(Period) #str변환
    Period = Period.split('.')

    Pid = []
    for Per in Period :
        if Per!=Period[-1] :
            Pid.append(Per)
    Period = ''.join(Pid)
    Period = re.sub(r'[^0-9]','',Period)

    #처분개수
    fn = []
    for file in files :
        if file.find('일련번호') != -1 :
            fn.append(file)
    finds = ['2. 관계법령 등(판단기준)','3. 감사결과 확인된 문제','관계기관 의견']
    keys = [[],[],[]]
    for fi in range(0,len(finds)) :
        for file in range(0,len(files)) :
            if files[file].find(finds[fi]) != -1 :
                keys[fi].append(file)
    scopes=[]
    for first in range(0,len(keys[0])) : #keys값 각 지적사항별 분리
        serialls = []
        serialls.append(keys[0][first])
        for second in range(0,len(keys[1])) :
            if first+1<len(keys[0]) and keys[0][first] < keys[1][second] < keys[0][first+1] : #keys[1]값이 keys[0] 현재값보다 크고 다음값보다 작을때 추가 
                serialls.append(keys[1][second])
            elif first+1==len(keys[0]) and keys[0][first] < keys[1][second] : #keys[0]의 다음 값이 없으면 나머지를 묶어줘
                serialls.append(keys[1][second])
        if len(serialls)>1 : #위에 정리된 리스트중 값이 1개인것을 제외
            serialls.sort()
            scopes.append(serialls)
    for first in range(0,len(scopes)) :
        for second in range(0,len(keys[2])) :
            if first+1 < len(scopes) :
                if scopes[first][0] < keys[2][second] < scopes[first+1][0] :
                    scopes[first].append(keys[2][second])
            elif first+1 == len(scopes) :
                if scopes[first][0] < keys[2][second]:
                    scopes[first].append(keys[2][second])
    tr = []
    for index in range(0,len(scopes)) :#법령범위
        con = []
        st = scopes[index][0]
        end = scopes[index][1]
        result = files[st:end]
        for res in result :
            if res.find("있다.") !=-1 : #전문적기준은 '따르면' 한개에 기준 한개
                con.append(res)
        if len(con) >= len(scopes[index])-2 : #전문적기준이 지적사항-2 개수보다 많거나 같으면 
            tr.append(1)
        else :
            tr.append(0)
    content = []
    ta = []
    tk = []
    for index in range(0,len(scopes)) :#법령범위
        con = []
        tc = []
        st = scopes[index][1]
        end = scopes[index][-1]
        result = files[st:end]
        for res in result :
            tt = res.split(' ') 
            for ti in tt :
                
                if ti.find("였") !=-1 or ti.find("났") !=-1 or ti.find("었") !=-1 :
                
                    if ti.find('.') != -1 or ti.find(',') != -1 :
                        tc.append(ti)
                elif ti.find("참조") !=-1 : #전문적기준은 '따르면' 한개에 기준 한개
                    con.append(ti)
        ta.append(tc)
        tk.append(con)
        if len(con) >= len(tc)-1 : #전문적기준이 지적사항-2 개수보다 많거나 같으면 
            content.append(1)
        else :
            content.append(0)
        
    sp.append(Period)
    sp.append(len(fn))
    sp.append(tr.count(1))
    sp.append(content.count(1))

    return sp