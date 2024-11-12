from downloads.user_data import pri, fe
from planet_details import zodiac_to_num as z  from vedic_pts import _vedicpt
from H import pltRH, pltPos, pltMv,pltRS,karakafrom rashiAspect import rasi_aspect
from aspect import aspects                     
                                               nat = _vedicpt(fe)
                                               pltMoves = {'H1':'good','H2':'challenging',
        'H3':'challenging','H4':'good',
        'H5':'good',                                   'H6':'difficult', 'H7':'weakest',
        'H8':'difficult',                              'H9':'good','H10':'good',
        'H11':'challenging',
        'H12':'challenging'}

hN = {'H1':'First','H2':'Second','H3':'Third','H4':'Fourth','H5':'Fifth','H6':'Sixth', 'H7':'Seventh','H8':'Eigth','H9':'Ninth','H10':'Tenth','H11':'Eleventh','H12':'Twelveth'}

sN = {'AR':'Aries','TA':'Taurus',
        'GE':'Gemini','CN':'Cancer',
        'LE':'Leo',
        'VI':'Virgo', 'LI':'Libra',
        'SC':'Scopio',
        'SG':'Sagittarius','CP':'Capricorn',
        'AQ':'Aquarius',
        'PI':'Pisces'}

pN = {'su':'Sun','mo':'Moon','me':'Mercury',
've':'Venus','ma':'Mars','ju':'Jupiter',
'sa':'Saturn','ra':'Rahu','ke':'ketu'}

readH = {
'H1':['Self', 'personality',
'physical appearance', 'health',
'vitality', 'identity', 'fame',
'beginnings', 'personal power'],
'H2':['Wealth and money', 'family of origin', 'speech', 'values', 'material possessions', 'savings'],
'H3':['Communication', 'siblings', 'courage', 'short journeys', 'hobbies', 'skills', 'media', 'writing', 'neighbors', 'effort'],
'H4':['Home', 'mother', 'comfort', 'property', 'emotional security', 'vehicles', 'upbringing', 'domestic life', 'roots'],
'H5':['Creativity', 'children', 'education', 'intellect', 'romance'],
'H6':
['pets', 'conflicts','difficulty', 'service'],
'H7':['Marriage', 'spouse', 'partnerships', 'business', 'public interactions', 'open enemies', 'contracts', 'movement', 'compassion'],
'H8':['Transformation', 'death', 'rebirth', 'occult', 'secrets', 'inheritance', 'trauma', 'business skills', 'sudden changes', 'mysteries'],
'H9':
['Father', 'foreign land', 'higher education', 'religion'],
'H10':['Career', 'status', 'public image', 'deeds', 'achievements', 'responsibility', 'authority', 'father’s wealth', 'societal role'],
'H11':['Gains', 'profits', 'social networks', 'elder siblings', 'desires', 'ambitions', 'workplace conflicts', 'group involvement'],
'H12':['Loss', 'isolation', 'foreign lands', 'expenses', 'charity', 'sleep', 'bed pleasures', 'spiritual liberation', 'large institutions', 'moksha']
}

ascS = nat['mo']['sign']
pltS = nat['ju']['sign']
pltN = nat['ju']['syb']

plt_mv = pltMv(pltS, pltN)#h11,h8
plt_ruledH = pltRH(ascS, pltN)
plt_ruledS = pltRS(ascS, pltN)
pltApt = rasi_aspect(nat, pltN)


name = 'Princly'
pltH = pltPos(ascS, pltS)
pltSs = sN[pltS]
pltC = aspects(pltN, nat)
pltm1 = pltMoves[plt_mv[0]]
pltm2 = pltMoves[plt_mv[1]]
pltSRuled1 = sN[plt_ruledS[0]]
pltSRuled2 = sN[plt_ruledS[1]]
pltHRuled1 = plt_ruledH[0]
pltHRuled2 = plt_ruledH[1]
pltK =karaka(pltN)


readJu = f"""
let's see {pN[pltN]} in {name}'s chart
{pN[pltN]} is in the {hN[pltH]} House of
the chart and in the sign of {pltSs} with
{pltC} this is a {pltm1} and
{pltm2} placement, {pN[pltN]} in {pltSs} is
challenging in itself but the {hN[pltH]} House
makes it doubly so, so for all the
significators of {pN[pltN]} there's going to
be some challenge in this chart.

now {pN[pltN]} is karaka for {pltK[0]}
karaka for {pltK[1]} karaka for {pltK[2]}
and with all of these things {name} may have
difficulty as we're going to see but let's
start with the houses lorded by by {pN[pltN]}
because to understand {pN[pltN]} he will also
show end result of the houses ruled.

The two houses in your chart that {pN[pltN]}
rule is {pltSRuled1}, the {hN[pltHRuled1]}
house of {readH[pltHRuled1][0]}, {readH[pltHRuled1][1]},
{readH[pltHRuled1][2]}, {readH[pltHRuled1][3]},
{readH[pltHRuled1][4]}, and {readH[pltHRuled1][5]},

and {pltSRuled2},the {hN[pltHRuled2]} house,
the house of {readH[pltHRuled2][0]}, {readH[pltHRuled2][1]},
{readH[pltHRuled2][2]}, and {readH[pltHRuled2][3]}
Etc

let's start with the {hN[pltHRuled1]} house,
this could be a {pltm1} situation in
{readH[pltH][0]} of {readH[pltHRuled1][0]}
or {pltm1} {readH[pltH][1]} {readH[pltHRuled1][1]},
{readH[pltH][2]} {readH[pltHRuled1][2]},
{readH[pltH][3]} {readH[pltHRuled1][3]},
{readH[pltH][4]} {readH[pltHRuled1][4]}

Then with respect to {hN[pltHRuled2]} house,
{pN[pltN]}, moved {hN[plt_mv[1]]} houses
away this could be a {pltm2} situation in
{readH[plt_mv[1]][0]} of
{readH[pltHRuled2][0]} or {pltm2}
{readH[plt_mv[1]][1]} {readH[pltHRuled2][1]},
{readH[plt_mv[1]][2]} {readH[pltHRuled2][2]},
{readH[plt_mv[1]][3]} {readH[pltHRuled2][3]},
{readH[plt_mv[1]][4]} {readH[pltHRuled2][4]}

The thing is of course {pN[pltN]} is a
blessing {pN[pltN]} does come back to
support.

Though, {pltK[0]}, {pltK[1]}, {pltK[2]}
maybe challenging {pN[pltN]} will come back
to support.
"""


print(readJu)
