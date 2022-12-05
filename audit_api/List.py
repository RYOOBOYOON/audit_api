def EL() :

    import os

    names = os.listdir('./pdf_file/EC_result_report/pdf_url')

    ls = []

    for name in names :

        if name == '.keep' :

            continue

        else :
            name = name.replace('.txt','')

        ls.append(name)

    return ls


def NL() :

    import os

    names = os.listdir('./pdf_file/SO_result_report/pdf_url')

    ls = []

    for name in names :

        if name == '.keep' :

            continue

        else :
            name = name.replace('.txt','')

        ls.append(name)
        
    return ls
    

def last_list():

    import os
    files_1 = os.listdir('./FILE_TXT/INTERVIEW_TXT')
    files_2 = os.listdir('./FILE_TXT/MANGER_TXT')
    files_3 = os.listdir('./FILE_TXT/ALGORITHM_TXT')

    ls = []
    list = []

    for fi in files_1 :

        for fie in files_2 :

            if fi == '.keep' :
                continue

            elif fi == fie :

                ls.append(fi)

    for li in ls :

        for fi in files_3 :

            if li == fi :

                list.append(li)

    return list
