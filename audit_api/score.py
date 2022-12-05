def score(names,count_threshold) :

    import re

    def file(f) :
        file = []
        while True:
            line = f.readline()
            if not line: break
            line = re.sub(r'[^0-9]','',line)
            if line != '' :
                file.append(int(line))
        f.close()

        return file

    result = []

    day1 = 0
    day2 = 0
    def day(algorithm,interview) :
        if algorithm == interview :
            day = 1
        else :
            day = 0
        return day

    disposition1 = 0
    disposition2 = 0
    def disposition(algorithm,count_threshold) :
        if algorithm >= count_threshold :
            disposition = 1
        else :
            disposition = 0
        return disposition

    criteri = 0
    criteri1 = 0
    criteri2 = 0

    Suggestion1 = 0
    Suggestion2 = 0

    analysis = 0
    Help = 0
    Help_res = 0

    Cooperation = 0
    actuality = 0

    expert = 0
    expert_res = 0

    participation = 0
    participation_res = 0

    Development = 0
    Development_res = 0

    Usage = 0
    Usage_res = 0

    for name in range(0,len(names)) :

        f = open(f'./FILE_TXT/INTERVIEW_TXT/{names[name]}','rt', encoding='UTF8')
        interview = file(f)
        f = open(f'./FILE_TXT/MANGER_TXT/{names[name]}','rt', encoding='UTF8')
        manger = file(f)
        f = open(f'./FILE_TXT/ALGORITHM_TXT/{names[name]}','rt', encoding='UTF8')
        algorithm = file(f)
        f = open(f'./FILE_TXT/EXPERT_TXT/{names[name]}','rt', encoding='UTF8')
        exp = file(f)
        

        #1.
        day1 += day(algorithm[0],manger[0])
        day2 += day(algorithm[0],manger[1])

        criteri += algorithm[1]
        criteri1 += manger[4]
        criteri2 += manger[5]

        disposition1 += disposition(manger[2],90)
        disposition2 += disposition(manger[3],90)


        #2.
        Suggestion1 += interview[0]
        Suggestion2 += interview[1]

        analysis += interview[2] 
        Help += interview[3]
        Help_res += interview[4]
        

        #3.
        Cooperation += interview[5]
        actuality += interview[6]


        #4.
        expert += exp[0]
        expert_res += exp[4]

        participation += exp[1]
        participation_res += exp[5]

        Development += exp[2]
        Development_res += exp[6]

        Usage += exp[3]
        Usage_res += exp[7]






    #1.
    day1 = f'Deadline of the law : {day1}/{len(names)} ({int(day1/len(names)*100)}%)'
    day2 = f'The deadline : {day2}/{len(names)} ({int(day2/len(names)*100)}%)'

    disposition1 = f'Evidence-based : {disposition1}/{len(names)} ({int(disposition1/len(names)*100)}%)'
    disposition2 = f'Professional standards : {disposition2}/{len(names)} ({int(disposition2/len(names)*100)}%)'

    criteri1 = f'Official acceptance disposition : {criteri1}/{criteri} ({int(criteri1/criteri*100)}%)'
    criteri2 = f'Actual contribution disposition : {criteri2}/{criteri} ({int(criteri2/criteri*100)}%)'

    #2.
    Suggestion1 = f'Suggestions provided : {Suggestion1}/{len(names)} ({int(Suggestion1/len(names)*100)}%)'
    Suggestion2 = f'Reviewed suggestions : {Suggestion2}/{len(names)} ({int(Suggestion2/len(names)*100)}%)'

    analysis = f'Analysis contents : {analysis}/{len(names)} ({int(analysis/len(names)*100)}%)'
    Help = f'Senior officials : {Help}/{Help_res} ({int(Help/Help_res*100)}%)'

    #3.
    Cooperation = f'Relationship and contact : {Cooperation}/{len(names)} ({int(Cooperation/len(names)*100)}%)'
    actuality = f'application : {actuality}/{len(names)} ({int(actuality/len(names)*100)}%)'

    #4.
    expert = f'Specialized personnel : {expert}/{expert_res} ({int(expert/expert_res*100)}%)'

    participation = f'Actual participants : {participation}/{participation_res} ({int(participation/participation_res*100)}%)'

    Development = f'Development : {Development}/{Development_res} ({int(Development/Development_res*100)}%)'

    Usage = f'Analysis : {Usage}/{Usage_res} ({int(Usage/Usage_res*100)}%)'



    #1.
    result.append(day1) 
    result.append(day2)
    result.append(disposition1)
    result.append(disposition2)
    result.append(criteri1)
    result.append(criteri2)

    #2.
    result.append(Suggestion1)
    result.append(Suggestion2)
    result.append(analysis)
    result.append(Help)

    #3.
    result.append(Cooperation)
    result.append(actuality)

    #4.
    result.append(expert)
    result.append(participation)
    result.append(Development)
    result.append(Usage)

    return result