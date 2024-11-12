#from downloads.user_data import pri
#from vedic_pts import _vedicpt

zN = {'AR':1, 'TA':2, 'GE':3, 'CN':4, 'LE':5, 'VI':6, 'LI':7, 'SC':8, 'SG':9, 'CP':10,'AQ':11, 'PI':12}

su = {'f':6,'s1':0,'s2':0,'s3':0}
mo = {'f':6,'s1':0,'s2':0,'s3':0}
me = {'f':6,'s1':0,'s2':0,'s3':0}
ve = {'f':6,'s1':0,'s2':0,'s3':0}
ma = {'f':6,'s1':3,'s2':7,'s3':0}
ju = {'f':6,'s1':4,'s2':8,'s3':0}
sa = {'f':6,'s1':2,'s2':9,'s3':0}
ra = {'f':6,'s1':1,'s2':4,'s3':8}
#ke = {'f':6,'s1':1,'s2':3,'s3':7}

aspect_tup = ('f','s1','s2','s3')


#nat  = _vedicpt(pri)

def aspects(planet, dicts):
    aspect_list = []

    #get the plt sign
    pltS = zN[dicts[planet]['sign']]#AQ,11
    for k, v in dicts.items():
        pltsS = v['syb']

        for asp in aspect_tup:
            if pltsS not in ['A','ke']:
                aspectt = zN[v['sign']] + eval(pltsS)[asp]

                if aspectt >= 13:
                    planet_aspect = aspectt - 12
                else:
                    planet_aspect = aspectt

                if pltS == planet_aspect and v['syb'] != planet and pltsS not in aspect_list:
                    aspect_list.append(pltsS)

    return aspect_list



#for p in ['su','mo','me','ve','ma','ju','sa','ra','ke']:
#    print(p,' = ',aspects(p, nat)
