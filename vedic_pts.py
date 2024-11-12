from __future__ import print_function, division
#from downloads.user_data import pri
from planet_details import zodiac

sign_tuple = ((range(0, 30),'AR'),(range(30, 60), 'TA'),(range(60, 90), 'GE'),
            (range(90, 120), 'CN'), (range(120, 150), 'LE'), (range(150, 180), 'VI'),
            (range(180, 210), 'LI'),(range(210, 240), 'SC'), (range(240, 270), 'SG'),
            (range(270, 300), 'CP'), (range(300, 330), 'AQ'),(range(330, 360), 'PI')
            )

def _vedicpt(nat):
    natP = {}
    """returns the planet vedic degree and sign"""
    for plt_pts in nat:

        if nat[plt_pts]['sign'] == 'AR':
            zodiacdeg = (360 +  nat[plt_pts]['deg']) - 23
            if zodiacdeg in range(360, 367):
                zodiacDeg = zodiacdeg - 360
            else:
                zodiacDeg = zodiacdeg

        else:
            zodiacDeg = (zodiac[nat[plt_pts]['sign']] +  nat[plt_pts]['deg']) - 23

        for range_, name_ in sign_tuple:
            if zodiacDeg in range_:

                vedic_sign = name_ #AQ

                vedicDeg = zodiacDeg - zodiac[vedic_sign]
                natP[plt_pts] = {'deg':vedicDeg,
                                'sign':vedic_sign,
                                'syb':nat[plt_pts]['syb']}


    return natP

def _zPt(nat, plt):
    """returns the planet vedic degree and sign"""
    #for plt_pts in nat:

    if nat[plt]['sign'] == 'AR':
        zodiacdeg = (360 +  nat[plt]['deg']) - 23
        if zodiacdeg in range(360, 367):
            zodiacDeg = zodiacdeg - 360
        else:
            zodiacDeg = zodiacdeg

    else:
        zodiacDeg = (zodiac[nat[plt]['sign']] +  nat[plt]['deg']) - 23
        """
        for range_, name_ in sign_tuple:
            if zodiacDeg in range_:

                vedic_sign = name_ #AQ

                vedicDeg = zodiacDeg - zodiac[vedic_sign]
                natP[plt_pts] = {'deg':vedicDeg,
                                'sign':vedic_sign,
                                'syb':nat[plt_pts]['syb']}

        """
    return zodiacDeg


#print(_vedicpt(pri))
#print(_zPt(pri, 'su'))
#print(_zPt(pri, 'mo')
