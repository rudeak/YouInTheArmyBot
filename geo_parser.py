from app.models import Orc, Geo, Areas, AreaToOrc

for area in Areas.select():
    if AreaToOrc.select().where(AreaToOrc.area==area).get_or_none() == None:
        query = area.delete()
        query.execute()

not_found_city = 0
not_found_city_array = []
not_found_region = 0
not_found_region_array = []
for orc in Orc.select():
    geo = Geo.select().where(Geo.orc == orc).get_or_none()
    if geo !=None:
        continue
    if orc.adress.find(' ,')>=0:
        orc.adress = orc.adress.replace(' ,',', ')
        orc.save()
    if orc.adress.find('  ')>=0:
        orc.adress = orc.adress.replace('  ',' ')
        orc.save()
    if orc.adress.find(',,')>=0:
        orc.adress = orc.adress.replace(',,',',')
        orc.save()
    if orc.adress.find('Г.Г.')>=0:
        orc.adress = orc.adress.replace('Г.Г.','Г.')
        orc.save()

    if orc.adress.find('Г САНКТ-ПЕТЕРБУРГ ')==0:
        orc.adress = orc.adress.replace('Г САНКТ-ПЕТЕРБУРГ ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('САНКТ-ПЕТЕРБУРГ, ')==0:
        orc.adress = orc.adress.replace('САНКТ-ПЕТЕРБУРГ, ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('Г САНКТ - ПЕТЕРБУРГ ')==0:
        orc.adress = orc.adress.replace('Г САНКТ - ПЕТЕРБУРГ ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('Г.САНКТ ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('Г.САНКТ ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('С.-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('С.-ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('Г.САНКТ-ПЕТЕРБУРГ МОСКОВСКИЙ')==0:
        orc.adress = orc.adress.replace('Г.САНКТ-ПЕТЕРБУРГ МОСКОВСКИЙ','Г. САНКТ-ПЕТЕРБУРГ, МОСКОВСКИЙ')
        orc.save()
    if orc.adress.find('Г С. ПЕТЕРБУРГ')==0:
        orc.adress = orc.adress.replace('Г С. ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ')
        orc.save()
    long_string = 'РОССИЯ 196084 САНКТ-ПЕТЕРБУРГ Г ЗАСТАВСКАЯ УЛ ДОМ 46 КОРПУС 1 ЛИТЕР А КВАРТИРА 87, РОССИЯ 196084 САНКТ-ПЕТЕРБУРГ Г ЗАСТАВСКАЯ УЛ ДОМ 46 КОРПУС 1 ЛИТЕР А КВАРТИРА 87'
    if orc.adress.find(long_string)>=0:
        orc.adress = orc.adress.replace(long_string,'Г. САНКТ-ПЕТЕРБУРГ, ЗАСТАВСКАЯ ДОМ 46 КОРПУС 1 ЛИТЕР А КВАРТИРА 87')
        orc.save()
    if orc.adress.find('САНКТ ПЕТЕРБУРГ')==0:
        orc.adress = orc.adress.replace('САНКТ ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('САНКТ-ПЕТЕРБУРГ ')==0:
        orc.adress = orc.adress.replace('САНКТ-ПЕТЕРБУРГ ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find(', Г, САНКТ-ПЕТЕРБУРГ')==0:
        orc.adress = orc.adress.replace(', Г, САНКТ-ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find(' , САНКТ-ПЕТЕРБУРГ, ')>=0:
        orc.adress = orc.adress.replace(' , САНКТ-ПЕТЕРБУРГ, ',', Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find(' , САНКТ-ПЕТЕРБУРГ Г,')>=0:
        orc.adress = orc.adress.replace(' , САНКТ-ПЕТЕРБУРГ Г,',' ,Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find(', САНКТ-ПЕТЕРБУРГ Г,')>=0:
        orc.adress = orc.adress.replace(', САНКТ-ПЕТЕРБУРГ Г,',',Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find(', Г, САНКТ-ПЕТЕРБУРГ, ')>=0:
        orc.adress = orc.adress.replace(', Г, САНКТ-ПЕТЕРБУРГ, ',',Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('ГОРОД САНКТ-ПЕТЕРБУРГ, ')>=0:
        orc.adress = orc.adress.replace('ГОРОД САНКТ-ПЕТЕРБУРГ, ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('САНКТ- ПЕТЕРБУРГ')==0:
        orc.adress = orc.adress.replace('САНКТ- ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find(', САНКТ-ПЕТЕРБУРГ, ')>=0:
        orc.adress = orc.adress.replace(', САНКТ-ПЕТЕРБУРГ, ',',Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('Г САНКТ-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('Г САНКТ-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('С-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('С-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('191119, САНКТ-ПЕТЕРБУРГ Г.,')==0:
        orc.adress = orc.adress.replace('191119, САНКТ-ПЕТЕРБУРГ Г.,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('САНКТ-ПЕТЕРБУРГ Г.,')>=0:
        orc.adress = orc.adress.replace('САНКТ-ПЕТЕРБУРГ Г.,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
# 
    if orc.adress.find('Г САНКТ ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('Г САНКТ ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('САНАТ-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНАТ-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find(', Г САНКТ-ПЕТЕРБУРГ,')>=0:
        orc.adress = orc.adress.replace(', Г САНКТ-ПЕТЕРБУРГ,',',Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('РОССИЯ, САНКТ-ПЕТЕРБУРГ ')==0:
        orc.adress = orc.adress.replace('РОССИЯ, САНКТ-ПЕТЕРБУРГ ','Г. САНКТ-ПЕТЕРБУРГ, ')
        orc.save()
    if orc.adress.find('САНКТ-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНКТ-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('САНК-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНК-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('САНКТ - ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНКТ - ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('ГОР САНКТ-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('ГОР САНКТ-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('САНКТПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНКТПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('Г САНКТ-ПЕТЕРБУРГ\\')==0:
        orc.adress = orc.adress.replace('Г САНКТ-ПЕТЕРБУРГ\\','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('Г САНКТ-ПЕТЕРБУРГ')==0:
        orc.adress = orc.adress.replace('Г САНКТ-ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('САНКТ-ПЕТЕРБУРГ. Г.')==0:
        orc.adress = orc.adress.replace('САНКТ-ПЕТЕРБУРГ. Г.','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('Г. САНКТ- ПЕТЕРБУРГ')>=0:
        orc.adress = orc.adress.replace('Г. САНКТ- ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ')
        orc.save()
    if orc.adress.find('Г. САНКТ ПЕТЕРБУРГ')>=0:
        orc.adress = orc.adress.replace('Г. САНКТ ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ')
        orc.save()
    if orc.adress.find('СПБ,')>=0:
        orc.adress = orc.adress.replace('СПБ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('127254, ')>=0:
        orc.adress = orc.adress.replace('127254, ','')
        orc.save()
    if orc.adress.find('109507, ')>=0:
        orc.adress = orc.adress.replace('109507, ','')
        orc.save()
    if orc.adress.find('195067, ')>=0:
        orc.adress = orc.adress.replace('195067, ','')
        orc.save()
    if orc.adress.find('Г.САНКТ-ПЕТЕРБУРГ УЛ.')>=0:
        orc.adress = orc.adress.replace('Г.САНКТ-ПЕТЕРБУРГ УЛ.','Г. САНКТ-ПЕТЕРБУРГ, УЛ.')
        orc.save()
    if orc.adress.find('САНКТ - ПЕТЕРБУРГ')>=0:
        orc.adress = orc.adress.replace('САНКТ - ПЕТЕРБУРГ','САНКТ-ПЕТЕРБУРГ')
        orc.save()


    if orc.adress.find('123103 МОСКВА,')>=0:
        orc.adress = orc.adress.replace('123103 МОСКВА,','Г. МОСКВА,')
        orc.save()

    if orc.adress.find('САНКТ-ПЕТЕРБУРГ')==0:
        orc.adress = orc.adress.replace('САНКТ-ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ')
        orc.save()
    if orc.adress.find('САНТК ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНТК ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ')
        orc.save()
    if orc.adress.find('САНКТПЕТЕРБУРГ')>=0:
        orc.adress = orc.adress.replace('САНКТПЕТЕРБУРГ','САНКТ-ПЕТЕРБУРГ')
        orc.save()
    if orc.adress.find('ГОР. САНКТ-ПЕТЕРБУРГ,')>=0:
        orc.adress = orc.adress.replace('ГОР. САНКТ-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('Г. С-ПЕТЕРБУРГ')>=0:
        orc.adress = orc.adress.replace('Г. С-ПЕТЕРБУРГ','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('ГОР.ШАМАЛДУ-САТ')>=0:
        orc.adress = orc.adress.replace('ГОР.ШАМАЛДУ-САТ','Г. ШАМАЛДУ-САТ')
        orc.save()
    if orc.adress.find('МОСКВА Г.')>=0:
        orc.adress = orc.adress.replace('МОСКВА Г.','Г. МОСКВА')
        orc.save()
    if orc.adress.find('ГОР МОСКВА Х')>=0:
        orc.adress = orc.adress.replace('ГОР МОСКВА Х','Г. МОСКВА, Х')
        orc.save()





    if orc.adress.find('Г. ЛОМОНОСОВ САНКТ ПЕТЕРБУРГ')>=0:
        orc.adress = orc.adress.replace('Г. ЛОМОНОСОВ САНКТ ПЕТЕРБУРГ','Г. ЛОМОНОСОВ, Г. САНКТ ПЕТЕРБУРГ')
        orc.save()
    if orc.adress.find('ИНДЕКС 198412 ')>=0:
        orc.adress = orc.adress.replace('ИНДЕКС 198412 ','')
        orc.save()
    if orc.adress.find('ГОР. БЕКАБАД ')>=0:
        orc.adress = orc.adress.replace('ГОР. БЕКАБАД ','Г. БЕКАБАД, ')
        orc.save()
# 
    if orc.adress.find('САНКТ -ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНКТ -ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('Г.САНКТ-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('Г.САНКТ-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('С МОКРА')==0:
        orc.adress = orc.adress.replace('С МОКРА','С. МОКРА')
        orc.save()
    if orc.adress.find('С.АК-ТАШ')==0:
        orc.adress = orc.adress.replace('С.АК-ТАШ','С. АК-ТАШ')
        orc.save()

    if orc.adress.find('САНК-ПЕТЕРБУРГ ')==0:
        orc.adress = orc.adress.replace('САНК-ПЕТЕРБУРГ ','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('Г ПУШКИН ')==0:
        orc.adress = orc.adress.replace('Г ПУШКИН ','Г. ПУШКИН, ')
        orc.save()
    if orc.adress.find('САНКТ_ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('САНКТ_ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('РОССИЯ, САНКТ-ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('РОССИЯ, САНКТ-ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()
    if orc.adress.find('СПНКТ ПЕТЕРБУРГ,')==0:
        orc.adress = orc.adress.replace('СПНКТ ПЕТЕРБУРГ,','Г. САНКТ-ПЕТЕРБУРГ,')
        orc.save()

    if orc.adress.find(', Г СЕРГИЕВ ПОСАД, ')>=0:
        orc.adress = orc.adress.replace(', Г СЕРГИЕВ ПОСАД, ',', Г. СЕРГИЕВ ПОСАД, ')
        orc.save()
    if orc.adress.find('РОССИЯ,ГМОСКВА,')==0:
        orc.adress = orc.adress.replace('РОССИЯ,ГМОСКВА,','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('ГОРОД МОСКВА П.')==0:
        orc.adress = orc.adress.replace('ГОРОД МОСКВА П.','Г. МОСКВА, П.')
        orc.save()

    if orc.adress.find('ГМОСКВА,')>=0:
        orc.adress = orc.adress.replace('ГМОСКВА,','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('Г МОСКВА ,')==0:
        orc.adress = orc.adress.replace('Г МОСКВА ,','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('Г МОСКВА, ')==0:
        orc.adress = orc.adress.replace('Г МОСКВА, ','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('МОСКВА, ')==0:
        orc.adress = orc.adress.replace('МОСКВА, ','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('ГОР. МОСКВА,')==0:
        orc.adress = orc.adress.replace('ГОР. МОСКВА,','Г. МОСКВА,')
        orc.save()
    if orc.adress.find('ГОР.МОСКВА')==0:
        orc.adress = orc.adress.replace('ГОР.МОСКВА','Г. МОСКВА,')
        orc.save()

    if orc.adress.find('МОСКВА,')==0:
        orc.adress = orc.adress.replace('МОСКВА,','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find(' МОСКВА ')==0:
        orc.adress = orc.adress.replace(' МОСКВА ','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('МОСКВА ')==0:
        orc.adress = orc.adress.replace('МОСКВА ','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('МОСКВА')==0:
        orc.adress = orc.adress.replace('МОСКВА','Г. МОСКВА')
        orc.save()
    if orc.adress.find('МОСКВА. П ')==0:
        orc.adress = orc.adress.replace('МОСКВА','Г. МОСКВА, П.')
        orc.save()
    if orc.adress.find('МОСКВА Г,')>=0:
        orc.adress = orc.adress.replace('МОСКВА Г,','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('ГОРОД МОСКВА,')>=0:
        orc.adress = orc.adress.replace('ГОРОД МОСКВА,','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('ГОР МОСКВА,')>=0:
        orc.adress = orc.adress.replace('ГОР МОСКВА,','Г. МОСКВА,')
        orc.save()
# 
    if orc.adress.find(', МОСКВА,')>=0:
        orc.adress = orc.adress.replace(', МОСКВА,',',Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('ГОРОД МОСКВА,')==0:
        orc.adress = orc.adress.replace(' ГОРОД МОСКВА,','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('РОССИЯ МОСКВА,')==0:
        orc.adress = orc.adress.replace('РОССИЯ МОСКВА,','Г. МОСКВА,')
        orc.save()
    if orc.adress.find(' ГОРОД МОСКВА ')>=0:
        orc.adress = orc.adress.replace(' ГОРОД МОСКВА ',' Г. МОСКВА, ')
        orc.save()
    if orc.adress.find(', МОСКВА,')>=0:
        orc.adress = orc.adress.replace(', МОСКВА,',', Г. МОСКВА,')
        orc.save()
    if orc.adress.find('Г МОСКВА')>=0:
        orc.adress = orc.adress.replace('Г МОСКВА','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('Г.МОСКВА')>=0:
        orc.adress = orc.adress.replace('Г.МОСКВА','Г. МОСКВА, ')
        orc.save()
    if orc.adress.find('УСТЬ-КАМЕНОГОРСК')==0:
        orc.adress = orc.adress.replace('УСТЬ-КАМЕНОГОРСК','Г. УСТЬ-КАМЕНОГОРСК')
        orc.save()
    if orc.adress.find('Г.УСТЬ-КАМЕНОГОРСК')==0:
        orc.adress = orc.adress.replace('Г.УСТЬ-КАМЕНОГОРСК','Г. УСТЬ-КАМЕНОГОРСК')
        orc.save()
    if orc.adress.find('КАНИБАДАН')==0:
        orc.adress = orc.adress.replace('КАНИБАДАН','Г. КАНИБАДАН')
        orc.save()
    if orc.adress.find('ГОР. АКТЮБИНСК')==0:
        orc.adress = orc.adress.replace('ГОР. АКТЮБИНСК','Г. АКТЮБИНСК')
        orc.save()

    if orc.adress.find('ЧУВАШИЯ ЧУВАШСКАЯ РЕСПУБЛИКА -,')==0:
        orc.adress = orc.adress.replace('ЧУВАШИЯ ЧУВАШСКАЯ РЕСПУБЛИКА -,','РЕСП. ЧУВАШИЯ,')
        orc.save()
    if orc.adress.find('РЕСПУБЛИКА АБХАЗИЯ')>=0:
        orc.adress = orc.adress.replace('РЕСПУБЛИКА АБХАЗИЯ','РЕСП. АБХАЗИЯ')
        orc.save()

    if orc.adress.find(' ,')>=0:
        orc.adress = orc.adress.replace(' ,',', ')
        orc.save()
    if orc.adress.find('  ')>=0:
        orc.adress = orc.adress.replace('  ',' ')
        orc.save()
    if orc.adress.find(',,')>=0:
        orc.adress = orc.adress.replace(',,',',')
        orc.save()
    if orc.adress.find('Г.Г.')>=0:
        orc.adress = orc.adress.replace('Г.Г.','Г.')
        orc.save()

    address_spl = orc.adress.split(',')
    city =''
    city_pos = 0
    region = ''
    region_pos = 0
    i = 0
    c_pref = ''
    r_pref = ''
    for a in address_spl:
        if a.find('Г. ')>=0:
            city_pos = i
            c_pref = 'Г. '
            city = a
        if a.find('Г.')>=0:
            city_pos = i
            c_pref = 'Г.'
            city = a
        if a.find('С. ')>=0:
            city_pos = i
            c_pref = 'С. '
            city = a
        if a.find('СТ-ЦА ')>=0:
            city_pos = i
            c_pref = 'СТ-ЦА '
            city = a
        if a.find('Х. ')>=0:
            city_pos = i
            c_pref = 'Х. '
            city = a
        if a.find(' Д. ')>=0:
            city_pos = i
            c_pref = ' Д. '
            city = a
        if a.find(' П. ')>=0:
            city_pos = i
            c_pref = ' П. '
            city = a
        if a.find(' РП. ')>=0:
            city_pos = i
            c_pref = ' РП. '
            city = a
        if a.find(' ПГТ. ')>=0:
            city_pos = i
            c_pref = ' ПГТ. '
            city = a
        if a.find(' СТ. ')>=0:
            city_pos = i
            c_pref = ' СТ. '
            city = a
        if a.find('ГОР.')>=0:
            city_pos = i
            c_pref = 'ГОР.'
            city = a
        if a.find(' АУЛ ')>=0:
            city_pos = i
            c_pref = ' АУЛ '
            city = a
        if a.find(' ДП ')>=0:
            city_pos = i
            c_pref = ' ДП '
            city = a
        if a.find(' СНТ ')>=0:
            city_pos = i
            c_pref = ' СНТ '
            city = a
        if a.find(' ГП. ')>=0:
            city_pos = i
            c_pref = ' ГП. '
            city = a
        if a.find(' С.П. ')>=0:
            city_pos = i
            c_pref = ' С.П. '
            city = a
        if a.find(' П-К ')>=0:
            city_pos = i
            c_pref = ' П-К '
            city = a
        if a.find(' П/О ')>=0:
            city_pos = i
            c_pref = ' П/О '
            city = a
        if a.find(' Г-К ')>=0:
            city_pos = i
            c_pref = ' Г-К '
            city = a
        if a.find(' СЛ. ')>=0:
            city_pos = i
            c_pref = ' СЛ. '
            city = a
        if a.find(' КП. ')>=0:
            city_pos = i
            c_pref = ' КП. '
            city = a
        if a.find(' У. ')>=0:
            city_pos = i
            c_pref = ' У. '
            city = a
        if a.find(' ТЕР. ГОРОДОК ')>=0:
            city_pos = i
            c_pref = ' ТЕР. ГОРОДОК '
            city = a
        if a.find(' ДЕР. ')>=0:
            city_pos = i
            c_pref = ' ДЕР. '
            city = a
        if a.find(' ДНП ')>=0:
            city_pos = i
            c_pref = ' ДНП '
            city = a
        if a.find(' МАССИВ ')>=0:
            city_pos = i
            c_pref = ' МАССИВ '
            city = a
        if a.find(' М-КО ')>=0:
            city_pos = i
            c_pref = ' М-КО '
            city = a
        if a.find(' НП ')>=0:
            city_pos = i
            c_pref = ' НП '
            city = a
        if a.find(' РЗД. ')>=0:
            city_pos = i
            c_pref = ' РЗД. '
            city = a
        if a.find(' СП. ')>=0:
            city_pos = i
            c_pref = ' СП. '
            city = a
        if a.find(' МКР. ')>=0:
            city_pos = i
            c_pref = ' МКР. '
            city = a
        if a.find(' В-КИ ')>=0:
            city_pos = i
            c_pref = ' В-КИ '
            city = a
        if a.find(' С/С ')>=0:
            city_pos = i
            c_pref = ' С/С '
            city = a
        if a.find(' ТЕР.')>=0:
            city_pos = i
            c_pref = ' ТЕР.'
            city = a
# ПОИСК РЕГИОНА
        if a.find('КРАЙ')>=0:
            region_pos = i
            r_pref = 'КРАЙ'
            region = a
        if a.find('ОБЛ. ')>=0:
            region_pos = i
            r_pref = 'ОБЛ. '
            region = a
        if a.find('РЕСП.')>=0:
            region_pos = i
            r_pref = 'РЕСП.'
            region = a
        if a.find('А.ОКР. ')>=0:
            region_pos = i
            r_pref = 'А.ОКР. '
            region = a
        if a.find('Г. МОСКВА')>=0:
            region_pos = i
            r_pref = 'Г. МОСКВА'
            region = a
        if a.find('Г. САНКТ-ПЕТЕРБУРГ')>=0:
            region_pos = i
            r_pref = 'Г. САНКТ-ПЕТЕРБУРГ'
            region = a
        if a.find('Г. СЕВАСТОПОЛЬ')>=0:
            region_pos = i
            r_pref = 'Г. СЕВАСТОПОЛЬ'
            region = a

        i = i + 1
    if city == '':
        c = 'Город не найден: '+ orc.adress+'['+str(orc.id)+']'
        not_found_city_array.append (c)
        not_found_city = not_found_city + 1
    if region == '':
        r = 'Регион не найден: '+ orc.adress+'['+str(orc.id)+']'
        not_found_region_array.append (r)
        # print (r)
        not_found_region = not_found_region + 1
    if city != '' and region != '':
        if c_pref !='' and r_pref !='':
            db_city = city.replace(c_pref, '').strip()
            db_region = region.replace(r_pref,'').strip()
            if r_pref == 'Г. САНКТ-ПЕТЕРБУРГ':
                    r_pref = 'Г.'
                    db_region = 'САНКТ-ПЕТЕРБУРГ'
            if r_pref == 'Г. МОСКВА':
                    r_pref = 'Г.'
                    db_region = 'МОСКВА'
            if r_pref == 'Г. СЕВАСТОПОЛЬ':
                    r_pref = 'Г.'
                    db_region = 'СЕВАСТОПОЛЬ'
            area = Areas.select().where (Areas.city==db_city, Areas.region==db_region).get_or_none()
            if area == None:
                print ('Добавляю: '+c_pref+db_city+' '+r_pref+' '+db_region)
                area = Areas()
                area.city_type = c_pref.strip()
                area.region_type = r_pref.strip()
                area.city = db_city
                area.region = db_region
                area.save()
            area_to_orc = AreaToOrc.select().where(AreaToOrc.orc==orc).get_or_none()
            if area_to_orc == None:
                area_to_orc = AreaToOrc()
                area_to_orc.orc = orc
                area_to_orc.area = area
                area_to_orc.full_address = orc.adress
                area_to_orc.save()
                print ('Поселили орка ['+str(orc.id)+']')

print ('*****************************************************')
print ('всего не найдено населенных пунктов: '+str(not_found_city))
print ('*****************************************************')

for r in not_found_region_array:
    print (r)

print ('*****************************************************')
print ('всего не найдено регионов: '+str(not_found_region))
print ('*****************************************************')


