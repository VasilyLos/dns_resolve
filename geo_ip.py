import requests

def get_geo_ip(ip_addr):
    list_get_geo_ip = []
    URL = 'https://api.ipgeolocation.io/ipgeo'
    KEY = 'api token

    params = {'apiKey': KEY, 'ip': ip_addr}

    try:
        r = requests.get(URL, params=params)
        res = r.json()
        list_get_geo_ip.append((res['country_name']))
        list_get_geo_ip.append((res['city']))
    except:
        print('domen error')
    return list_get_geo_ip
