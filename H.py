AR = {'H1':'AR','H2':'TA','H3':'GE',
        'H4':'CN','H5':'LE','H6':'VI',
        'H7':'LI','H8':'SC','H9':'SG',                 'H10':'CP','H11':'AQ','H12':'PI'}

TA = {'H1':'TA','H2':'GE','H3':'CN',
        'H4':'LE','H5':'VI','H6':'LI',
        'H7':'SC','H8':'SG','H9':'CP',
        'H10':'AQ','H11':'PI','H12':'AR'}

GE = {'H1':'GE','H2':'CN','H3':'LE',
        'H4':'VI','H5':'LI','H6':'SC',
        'H7':'SG','H8':'CP','H9':'AQ',
        'H10':'PI','H11':'AR','H12':'TA'}

CN = {'H1':'CN','H2':'LE','H3':'VI',
        'H4':'LI','H5':'SC','H6':'SG',
         'H7':'CP','H8':'AQ','H9':'PI',
        'H10':'AR','H11':'TA','H12':'GE'}

LE = {'H1':'LE','H2':'VI','H3':'LI',
        'H4':'SC','H5':'SG','H6':'CP',
        'H7':'AQ','H8':'PI','H9':'AR',
        'H10':'TA','H11':'GE','H12':'CN'}

VI = {'H1':'VI','H2':'LI','H3':'SC',
        'H4':'SG','H5':'CP','H6':'AQ',
        'H7':'PI','H8':'AR','H9':'TA',
        'H10':'GE','H11':'CN','H12':'LE'}

LI = {'H1':'LI','H2':'SC','H3':'SG',
        'H4':'CP','H5':'AQ','H6':'PI',
         'H7':'AR','H8':'TA','H9':'GE',
        'H10':'CN','H11':'LE','H12':'VI'}

SC = {'H1':'SC','H2':'SG','H3':'CP',
        'H4':'AQ','H5':'PI','H6':'AR',
        'H7':'TA','H8':'GE','H9':'CN',
        'H10':'LE','H11':'VI','H12':'LI'}

SG = {'H1':'SG','H2':'CP','H3':'AQ',
        'H4':'PI','H5':'AR','H6':'TA',
        'H7':'GE','H8':'CN','H9':'LE',
        'H10':'VI','H11':'LI','H12':'SC'}

CP = {'H1':'CP','H2':'AQ','H3':'PI',
        'H4':'AR','H5':'TA','H6':'GE',
        'H7':'CN','H8':'LE','H9':'VI',
        'H10':'LI','H11':'SC','H12':'SG'}

AQ = {'H1':'AQ','H2':'PI','H3':'AR',
        'H4':'TA','H5':'GE','H6':'CN',
        'H7':'LE','H8':'VI','H9':'LI',
        'H10':'SC','H11':'SG','H12':'CP'}
PI = {'H1':'PI','H2':'AR','H3':'TA',
        'H4':'GE','H5':'CN','H6':'LE',
        'H7':'VI','H8':'LI','H9':'SC',
        'H10':'SG','H11':'CP','H12':'AQ'}

pltHRd = {'su':['LE',''],
        'mo':['TA','CN'],
        'me':['GE','VI'],
        've':['TA','LI'],
        'ma':['AR','SC'],
        'ju':['SG','PI'],
        'sa':['CP','AQ'],
        'ra':['AQ','VI'],
        'ke':['SC','PI'],
        }

cvtH = {'H1':1,'H2':2,'H3':3,'H4':4,'H5':5,
            'H6':6,'H7':7,'H8':8,'H9':9,
            'H10':10,'H11':11,'H12':12
            }

su = ['soul','king','ruler','father','government','dhama','order','power','wealth','creativity','success']
mo = ['mother','nurturing','food','early education','home','emotion','longivity','family','society']
me = ['speech','money','business','communication','humour','intellect','journey','sister','study','friends','youth','nature']
ve = ['juice','love','beauty','sexuality','attraction','wife','procreation','luxury','wealth','arts','music']
ma = ['strength','war','army','fighting','anger','police','violence','security','conflict',
      'accident','discipling','courage','celibacy','brother']
ju = ['bliss','education','children','wisdom','philosophy','religion','teacher','abundance',
      'peace','god/divine','spirituality','husband']
sa = ['sorrow','time','limitation','structure','debts','loss','suffering','depression','sickness',
      'long life','struggle','old age','fear']
ra = ['illusion','desire','insatiable','shocks','criminals','deception','drugs','politices','borders',
      'animals','foreign lands']
ke = ['moksha','past life','detachment','extremism','freedom','isolation','mistakes',
      'renunciation','locality','dogs']



def pltMv(pltS, pltN):
    h = []
    #get the house planet rules
    for signn in pltHRd[pltN]:
        #[SG, PI]
        for k, v in eval(signn).items():
            if pltS == v:
                #h.append(convertH[k])
                #[H11,H8]movemnt
                h.append(k)
    return h

def pltPos(ascS, pltS):
    for k, v in eval(ascS).items():
        if pltS == v:
            h = k
    return h

def pltRH(ascS, pltN):
    hr = []
    for signn in pltHRd[pltN]:
        #[SG, PI]
        for k, v in eval(ascS).items():
            if signn == v:
                hr.append(k)
    return hr

def pltRS(ascS, pltN):
    return pltHRd[pltN]

def karaka(pltN):
    return eval(pltN)

#print(pltRH('LI', 'ju'))
#print(pltPos('SC', 'LI'))
print(pltRH('SC', 'ju'))
