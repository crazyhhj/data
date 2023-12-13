for i in range(len(script)):
    #init
    narrdict={}
    namedict={}
    narratage=[]
    narrdia=[]
    namedia=[]
    dia=[]

    t=script[i]
    #                     [ slug{content:[narratage],dia:[narrdia]},{content:[namedia],dia:[dia]}dia ]
    if script[i] in sluglines:
        j=i+1
        for j in range(j,len(script)):
            i = j
            t1 = script[j]


            if not script[j] in org_name and not script[j] in sluglines:
                narratage.append(script[j])

            if script[j] in sluglines:break

            if script[j] in org_name:

                narrdict['content'] = narratage;narrdict['dia'] = narrdia
                narratage=[]
                slugdia.append(narrdict)

                index = org_name.index(script[j])
                if len(per[index])>30:
                    break
                namedia = per[index]
                namedict['content'] = namedia
                k = j + 1

                dia=[]
                for k in range(k, len(script)):

                    if script[k]=="              I just don't wanna feel so bad\n":
                        a=1
                    i = k+1
                    j = k+1
                    t2 = script[k]
                    # print(t2)
                    if not script[k] == '\n':
                        dia.append(script[k])
                    else:

                        namedict['dia'] = dia
                        break

                slugdia.append(namedict)
