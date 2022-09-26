
# import vk

# TOKENS =['vk1.a.2vzOHjyqFRdE2a7UTRVYB8v0E1hcQr3Subwuj_gJPzCQ6gY3He79e9-TBfVDGW9q8nSyw6V31XtTfYy4Qv4Gf5xGNpxQzc26CxTBfVDGW9q8nSyw6V31XtTfYy4Qv4Gf5xGNMNfm2RfEHfK0yniS8pL6-mTIiXQDca_BGdhKvstKKar2-15TtNafiwjqq055','vk1.a.xGTSSpk95hLtWA-dcAw6ItCJUo9VAdJG4GrkxxL10Bujab-lNfJryD-qzQMKuXUI3rSYrIp3y-wXC2rxSHUQRiD0uVsIbu9Di7EG3LH3QhzwoP5VjK6a2t-LPWKtcPjpxQzc26CxTtPFuQMNfm2RfEHfKVXdT0sqv6WAuf93WxoYfcuh4kI_Ey_Vh_kOW4yM']
# TOKENS =['vk1.a.Rf01NFmgjJtkM68KRAAwpbEV2G73bqDKCCzwKyY9rmBJGu48FrkNMro4AWtCkc1fBEhfOwkHkfHuL-cF0emHHQKbkG5F_qZXQZLWrfpsHevNVPjafB2KrHn5j2h5OVV0eHkM6shG6IbtrmpE8LPWKtcPjpxQzc26CxTtPFuQMNfm2RfEHfKgMsIwczdCPNf5']

# vk_api = vk.API(access_token=TOKENS[0])

# vk_api.users.search(q='Грешко')

pass

import vk_api
from app.models import Orc, AreaToOrc, Areas

login = 'greshko@rambler.ru'
passwd = 'Qjuehn10'

vk_session = vk_api.VkApi(login, passwd)
vk_session.auth()
vk = vk_session.get_api()

country = vk.database.getCountries(code='RU')
country_id = country['items'][0]['id']

# region = vk.database.getRegions(q='Санкт-Петербург', country_id = country_id)
# region_id = region['items'][0]['id']

city = vk.database.getCities(q='ЗЕЛЕНОГРАД', country_id=country_id)
city_id = city ['items'][0]['id']

user = vk.users.search(q='Маликов Алексадр', country = country_id, city=city_id)

pass