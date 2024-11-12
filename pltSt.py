from downloads.user_data import pri,fe,bet,nk,nanndy,jef
from vedic_pts import _vedicpt, _zPt
from H import pltHRd,AR,TA,CN,LE,VI,LI,SC,SG,CP,AQ,PI

nat = _vedicpt(nanndy)
#print(nat)

E = {'su':'AR','mo':'TA','me':'VI',
've':'PI','ma':'CP','ju':'CN','sa':'LI','ra':'GE','ke':'SG'}

D = {'su':'LI','mo':'SC','me':'PI',
've':'VI','ma':'CN','ju':'CP','sa':'AR','ra':'SG','ke':'GE'}

pHo = {'su':'LE','mo':'CN','me':'GE',
've':'TA','ma':'SC','ju':'PI','sa':'CP','ra':'AQ','ke':'SC'}

pHoWk = {'su':'AQ','mo':'CP','me':'SG',
've':'SC','ma':'TA','ju':'VI','sa':'CN','ra':'LE','ke':'TA'}

oS = {'su':'LE','mo':'TA','me':'VI',
've':'LI','ma':'AɌ','ju':'SG','sa':'AQ','ra':'VI','ke':'PI'}

oW = {'su':'AQ','mo':'SC','me':'PI',
've':'AR','ma':'LI','ju':'GE','sa':'LE','ra':'PI','ke':'VI'}

hSt = {'su':'H10','mo':'H4','me':'H1',
've':'H4','ma':'H10','ju':'H1','sa':'H7',
'ra':'H7','ke':''}

hWk = {'su':'H4','mo':'H10','me':'H7',
've':'H10','ma':'H4','ju':'H7','sa':'H1',
'ra':'H1','ke':''}

comB = {'me':13,'ve':9,'ma':17,'ju':12,'sa':15}
crit = [0,1,28,29]


def eDebility(nat):
    ed = []
    for p, s in nat.items():
        if s['syb'] not in ('A'):
            for st, n in ((E,'E'),(D,'D'),(pHo,'Spho'),(pHoWk,'Wphwk'),(oS,'Sos'),(oW,'Wow')):
                if st[p] == s['sign']:
                    ed.append((p,n))
    return ed

def pltED(nat, pltN):
    plt = nat[pltN]['syb']
    sign = nat[pltN]['sign']
    ed = []
    if sign not in ('A'):
        for st, n in ((E,'E'),(D,'D'),(pHo,'Spho'),(pHoWk,'Wphwk'),(oS,'Sos'),(oW,'Wow')):
            if st[plt] == sign:
                ed.append(n)
    return ed

def hS(nat, asc,  plt):
    pltS = nat[plt]['sign']
    r = []
    house = eval(nat[asc]['sign'])
    for k, v in house.items():
        if pltS == v:
            h = k#H12
    for k1, v1 in hSt.items():
        if v1 == h:
            if k1 == plt:
                r.append((k1, 'dB'))
    for k2, v2 in hWk.items():
        if v2 == h:
            if k2 == plt:
                r.append((k2, 'zDB'))

    return r

def combC(nat):
    co, cr = [],[]
    suD = nat['su']['deg']
    suS = nat['su']['sign']
    for k, v in nat.items():
        pltS = v['sign']
        pltN = v['syb']#ve
        nPltD = v['deg']#2
        if pltN not in ['su','mo','ra','ke']:
            for kc, vc in comB.items():
                if pltS == suS:
                    if nPltD - suD == vc:
                        co.append(k)
        if nPltD in crit and k not in cr:
            cr.append(k)
    return co,cr

def pltWar(nat):
    w = []
    for plt in ['su','mo','me','ve','ma','ju','sa','ra','ke']:
        pltS = nat[plt]['sign']
        pltN = nat[plt]['syb']
        pltD = nat[plt]['deg']
        #pltM = [plt]['min']
        for k, v in nat.items():
            if v['deg'] == pltD and v['sign'] == pltS and v['syb'] != pltN:
                w.append(k)
            #if v['min'] > pltM:
            #    w.append(k)
            #else:
            #    w.append(pltN)
    return w

def mutual(nat):
    #rl = []
    m = []
    for plt in ['su','mo','me','ve','ma','ju','sa','ra','ke']:
        rl = []
        pltS = nat[plt]['sign']#sa, vi
        pltRS = pltHRd[plt]#aq,cp
        pltN = nat[plt]['syb']
        #sign ruled
        for p, r in pltHRd.items():
            for s in r:
                if pltS == s and p not in rl:#me
                    rl.append(p)
        #print('for ', pltN,'sign=',pltS,'rl = ',rl)
        for rp in rl:
            if nat[rp]['sign'] in pltRS and nat[rp]['syb'] not in m:
                m.append(nat[rp]['syb'])
                m.append(pltN)

    return m

def moS(nat):
    suD = _zPt(nat, 'su')
    moD = _zPt(nat, 'mo')
    s = moD - suD
   # print(s < 0, s == isinstance(s, int))
    #if s == isinstance(s, int):
        #print('Y')
    if s < 0:
        return abs(s), 'wan'
    return s, 'wax'


print(eDebility(nat))
print(pltED(nat, 'ju'))
print(hS(nat,'mo', 'su'))
print(combC(nat))
print('pltW = ',pltWar(nat))
print('mutual = ',mutual(nat))
print('moS = ',moS(nat))
