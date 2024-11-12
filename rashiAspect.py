from vedic_pts import _vedicpt
from downloads.user_data import pri            
zN= {'AR':1,'TA':2,'GE':3,'CN':4,'LE':5,'VI':6,        'LI':7,'SC':8,'SG':9,'CP':10,'AQ':11,'PI':12                                                  }

cadi = [1,4,7,10]
fixed = [2,5,8,11]
daul = [3,6,9,12]

sign_group = (
                (fixed,'fixed'),(daul,'daul'),
                (cadi,'cadi')
                )

def rAspect(nat, planet):
    plt = zN[nat[planet]['sign']]#11


    fixed_aspects_list = [plt + 2, plt + 5,
                        plt + 8
                        ]
    cadi_aspects_list = [plt + 4, plt + 7,
                        plt + 10
                        ]

    daul_aspects_list = [plt + 3, plt + 6,
                        plt + 12
                        ]

    for group,group_name in sign_group:
        if plt in group:
            name = f"""{group_name}_aspects_list"""
            #print(name)


    plt_aspects = []

    for num in eval(name):
        if num > 12:
            newN = num - 12
        else:
            newN = num
        plt_aspects.append(newN)

    return plt_aspects

def aspectToPlt(nat, plt):
    aPlt = []
    asptR = rAspect(nat, plt)
    for k, v in nat.items():
        if zN[v['sign']] in asptR and k != plt:
            aPlt.append(k)

    return aPlt

nat = _vedicpt(pri)
#print('nat: ', nat)
print(rAspect(nat, 'sa'))
print(aspectToPlt(nat, 'sa'))
