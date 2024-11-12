from __future__ import print_function, division

sign_tuple = ((range(0, 30),'AR'),(range(30, 60), 'TA'),(range(60, 90), 'GE'),
            (range(90, 120), 'CN'), (range(120, 150), 'LE'), (range(150, 180), 'VI'),
            (range(180, 210), 'LI'),(range(210, 240), 'SC'), (range(240, 270), 'SG'),
            (range(270, 300), 'CP'), (range(300, 330), 'AQ'),(range(330, 360), 'PI')
            )

zodiac = {'AR':0, 'TA':30, 'GE':60, 'CN':90, 'LE':120, 'VI':150, 'LI':180, 'SC':210, 'SG':240, 'CP':270,
          'AQ':300, 'PI':330}
zodiac_to_num = {'AR':1, 'TA':2, 'GE':3, 'CN':4, 'LE':5, 'VI':6, 'LI':7, 'SC':8, 'SG':9, 'CP':10,'AQ':11, 'PI':12}

#https://archive.org/details/lightonlife00hart/page/62/mode/1up?view=theater
planetStrenght = {'AR':{'sat':'weak','ven':'weak','jup':'strong','mas':'strong','sun':'exalted'},
                  'TA':{'mas':'weak','jup':'strong','rah':'weak','ket':'weak','ven':'strong(-)','mon':'exalted'},
                  'GE':{'mec':'strong','jup':'weak','sat':'strong','rah':'exalted'},
                  'CN':{'sat':'weak','mec':'strong','mas':'weak','mon':'strong','jup':'exalted'},
                  'LE':{'sat':'weak','mas':'strong','sun':'strong'},
                  'VI':{'jup':'weak','sat':'strong','ven':'weak', 'mec':'exalted(-)'},
                  'LI':{'mas':'weak','jup':'strong','sun':'weak','ven':'strong','sat':'exalted'},
                  'SC':{'ven':'weak','sun':'strong','mon':'weak','ket':'exalted','rah':'exalted','mas':'strong(-)'},
                  'SG':{'mec':'weak','ven':'strong','ket':'exalted','jup':'strong'},
                  'CP':{'mon':'weak','mec':'strong','jup':'weak','sat':'strong(-)','mas':'exalted'},
                  'AQ':{'sun':'weak','sat':'strong'},
                  'PI':{'mec':'weak','ven':'exalted','jup':'strong(-)'}
                  }

#https://archive.org/details/lightonlife00hart/page/60/mode/1up?view=theater
exalt_or_debilite = {'AR':{'sun':'exalted','sat':'debilited','ket':'debilited','rah':'debilited',},
                  'TA':{'mon':'exalted'},
                  'CN':{'jup':'exalted','mas':'debilited'},
                  'VI':{'mec':'exalted(-)','ven':'debilited'},
                  'LI':{'sat':'exalted','sun':'debilited'},
                  'SC':{'ket':'exalted','rah':'exalted','mon':'debilited'},
                  'CP':{'mas':'exalted','jup':'debilited'},
                  'PI':{'ven':'exalted','mec':'debilited'}
                  }

potentialStrenght = {'exalted':'87.5 - 100', 'trinal':'75 - 87.5', 'positive':'62.5 - 75','negative':'50 - 62.5',
                     'F':'37.5 - 50','N':'25 - 37.5','E':'12.5 - 25','weak':'0 - 12.5'}

planetRelationship = {'sun':{'mon':'Friend','jup':'Friend','mas':'Friend','mec':'Neutral','ven':'Enemy','sat':'Enemy'},
                  'mon':{'sun':'Friend','mec':'Friend','ven':'Neutral','mas':'Neutral','jup':'Neutral','sat':'Neutral'},
                  'mec':{'sun':'Friend','ven':'Friend','mas':'Neutral','jup':'Neutral','sat':'Neutral','mon':'Enemy'},
                  'ven':{'mec':'Friend','sat':'Friend','mas':'Neutral','jup':'Neutral','sun':'Enemy','mon':'Enemy'},
                  'mas':{'sun':'Friend','mon':'Friend','jup':'Friend','ven':'Neutral','mec':'Enemy','sat':'Neutral'},
                  'jup':{'sun':'Friend','mon':'Friend','mas':'Friend','sat':'Neutral','ven':'Enemy','mec':'Enemy'},
                  'sat':{'mec':'Friend','ven':'Friend','jup':'Neutral','sun':'Enemy','mon':'Enemy','mas':'Enemy'}
                  }
rulership = {'AR':'mas', 'TA':'ven', 'GE':'mec', 'CN':'mon', 'LE':'sun', 'VI':'mec', 'LI':'ven', 'SC':'mas',
             'SG':'jup', 'CP':'sat', 'AQ':'sat', 'PI':'jup'}

rulership2 = {'AR':'mas', 'TA':['ven','mon'], 'GE':'mec', 'CN':'mon', 'LE':'sun', 'VI':['mec','rah'], 'LI':'ven',
              'SC':['mas','ket'], 'SG':'jup', 'CP':'sat', 'AQ':['sat','rah'], 'PI':['jup','ket']}
                #['TA','VI','SC','AQ','PI']

head_rise = ['GE', 'LE', 'VI', 'LI', 'SC', 'AQ']#auspicious
back_rise = ['AR', 'TA', 'CN', 'SG', 'CP']#unauspicious
both = ['PI']#changable


class PlanetDetails:
    '''vars'''
    def __init__(self, natal, transit_):
        self.nat = natal
        self.transit = transit_

    def _vedicpt(self, planet):
        """returns the planet vedic degree and sign"""
        if self.nat[planet]['sign'] == 'AR':
            zodiacdeg = (360 +  self.nat[planet]['deg']) - 23
            if zodiacdeg in range(360, 367):
                zodiacDeg = zodiacdeg - 360
            else:
                zodiacDeg = zodiacdeg

        else:
            zodiacDeg = (zodiac[self.nat[planet]['sign']] +  self.nat[planet]['deg']) - 23 #sun (330 + 3) - 23 = 310

        #get the range of 310
        for range_, name_ in sign_tuple:
            if zodiacDeg in range_:
                vedic_sign = name_ #AQ

        #                 310 - 300 = 10
        vedicDeg = zodiacDeg - zodiac[vedic_sign]
        strenght = planetStrenght[vedic_sign].get(self.nat[planet]['syb'])
        #print('caalleed')
        #                10             aq                       310
        return {'deg':vedicDeg, 'sign':vedic_sign, 'zodiac_deg':zodiacDeg, 'strenght':strenght}

    def moonStrenth(self):
        #mon details = strong from 5 day after new to 10 day after full i used 72
        sunDts = self._vedicpt('sun')['zodiac_deg']
        moonDts = self._vedicpt('mon')['zodiac_deg']

        if sunDts >= moonDts:
            b4dist = sunDts - moonDts
        elif sunDts <= moonDts:
            b4dist = moonDts - sunDts

        if b4dist >= 180:
            dist = 360 - b4dist
        else:
           dist = b4dist

        if dist <= 72:
            return 'weak'
        return 'strong'


    def enemy_or_friend(self, planet):
        planet_sign = self._vedicpt(planet)['sign'] #CP
        ruler_planet_sign = rulership[planet_sign] #sat
        enemy_or_friend_ruler_sign = planetRelationship[ruler_planet_sign].get(planet) #E

        return enemy_or_friend_ruler_sign

    def planetState(self, planet):

        planet_signn = self._vedicpt(planet)['sign'] #CP
        odd_sign_range = (
                            (range(zodiac[planet_signn], zodiac[planet_signn] + 7),'child'),
                            (range(zodiac[planet_signn] + 7, zodiac[planet_signn] + 14),'youth'),
                            (range(zodiac[planet_signn] + 14, zodiac[planet_signn] + 21),'young'),
                            (range(zodiac[planet_signn] + 21, zodiac[planet_signn] + 28),'aged'),
                            (range(zodiac[planet_signn] + 28, zodiac[planet_signn] + 35),'dead')
                            )

        even_sign_range = (
                            (range(zodiac[planet_signn] + 28, zodiac[planet_signn] + 35),'dead'),
                            (range(zodiac[planet_signn] + 21, zodiac[planet_signn] + 28),'aged'),
                            (range(zodiac[planet_signn] + 14, zodiac[planet_signn] + 21),'young'),
                            (range(zodiac[planet_signn] + 7, zodiac[planet_signn] + 14),'youth'),
                            (range(zodiac[planet_signn], zodiac[planet_signn] + 7),'child')
                            )

        if planet_signn in ['AR','GE','LE','LI','SG','AQ']:
            for range_, state in odd_sign_range:
                if self._vedicpt(planet)['zodiac_deg'] in range_:
                    planet_statee = state
                    break

        if planet_signn in ['TA','CN','VI','SC','CP','PI']:
            for range_, state in even_sign_range:
                if self._vedicpt(planet)['zodiac_deg'] in range_:
                    planet_statee = state
                    break

        return planet_statee

    #AGE of planets = https://archive.org/details/lightonlife00hart/page/69/mode/1up?view=theater
    def directional_strenght(self, planet, house):#house position
        H1 = {'mec':'strong','jup':'strong','sat':'weak',}#east
        H4 = {'mon':'strong','ven':'strong','sun':'weak','mas':'weak'}#north
        H7 = {'sat':'strong','jup':'weak','mec':'weak'}#west
        H10 = {'sun':'strong','mas':'strong','mon':'weak','ven':'weak',}#south
        return house[planet]
    def planetMature(self):
         mature = {'sun':22,'mon':24,'mas':28,'mec':32,'jup':16,'ven':25,'sat':36,'rah':48,'ket':48}

    def planetCombust(self, planet):       #'mec':[14D,12R]
         combustDeg = {'mas':[17,8],'mec':[14,12],'jup':[11,8],'ven':[10,8],'sat':[15,8]}
         sunDeg = self._vedicpt('sun')['zodiac_deg']
         planetDeg = self._vedicpt(planet)['zodiac_deg']
         print(sunDeg,planetDeg)
         print(planetDeg - sunDeg)

    def planetR(self, planet):       #'mec':[14D,12R]
         #combustDeg = {'mas':[17,8],'mec':[14,12],'jup':[11,8],'ven':[10,8],'sat':[15,8]}
         sunDeg = self._vedicpt('sun')['zodiac_deg']
         planetDeg = self._vedicpt(planet)['zodiac_deg']
         print(sunDeg,planetDeg)
         print(sunDeg - planetDeg)

    def planet_details(self):
        star_list = []
        for star in ('asc','sun','mon','mec','ven','mas','jup','sat','rah','ket'):
            sign = self._vedicpt(star)['sign']
            starStrent = self._vedicpt(star)['strenght']
            starCamp = self.enemy_or_friend(star)
            starState = self.planetState(star)
            #star_list.append(f"The {star} is {starStrent} in strength, in {starCamp}'s camp and is {starState}.")
            star_list.append({'planet':star,'strenght':starStrent,'camp':starCamp,'state':starState,'sign':sign})
        return star_list

    def tithi(self):
        s_long  = self._vedicpt('sun')
        m_long  = self._vedicpt('mon')

        sun_long  = s_long['zodiac_deg']
        mon_long  = m_long['zodiac_deg']

        if mon_long < sun_long:
            tith = (((mon_long + 360) - sun_long) // 12) + 1
            if tith < 15:
                tithi_name = 'shulkla_paksha'
                tithi = tith
            else:
                tithi_name = 'krishna_paksha'
                tithi = tith - 15
        else:
            tith = ((mon_long  - sun_long) // 6) + 1
            if tith < 15:
                tithi_name = 'shulkla_paksha'
                tithi = tith
            else:
                tithi_name = 'krishna_paksha'
                tithi = tith - 15

        #tith = ((mon_long - sun_long) // 6) + 1
        return tithi,tithi_name


    def __str__(self):
        return """returns the planet vedic degree and sign"""

"""
from user_data import jef,nanndy,bet,fe,nk,pri,fe_w,confi,transit

chart = PlanetDetails(pri, transit)

star_details = chart.planet_details()
print(star_details)
#print(chart.tithi())
"""
