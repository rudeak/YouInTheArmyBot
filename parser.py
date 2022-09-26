import io
from app.models import Orc
i = 1
with io.open('Priziv1volna.txt', encoding='utf-8') as file:
    for line in file:
        s = line.split('\t')
        if len(s) != 5:
            continue
        fio = s[0]
        print (str(i)+'. '+fio)
        i = i + 1

        date_of_b = s[1]
        adress = s[2]
        passport_no = s[3]
        passport_gov = s[4]

        fio_spl = fio.split(' ')
        try:
            name = fio_spl[1]
        except:
            name = fio
        try:
            fathername = fio_spl[2]
        except:
            fathername = fio
        try:
            surname = fio_spl[0]
        except:
            surname = fio

        if Orc.select().where(Orc.passport_no==passport_no.strip()).get_or_none() !=None:
            continue
        orc = Orc()
        orc.fio = fio
        orc.name = name
        orc.fathername = fathername
        orc.surname = surname
        orc.date_of_b = date_of_b
        orc.adress = adress
        orc.passport_no = passport_no
        orc.passport_gov = passport_gov
        orc.save()
