import requests

url = "http://cetteurlnexistepas.com"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("00ps: Something Else", err)
