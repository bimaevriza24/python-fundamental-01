#MENGGUNAKAN PACKAGE REQUEST (

import requests #import request berguna untuk mengambil url web

url = 'https://www.detik.com/' #url web dari detik.com
try: # (try) berguna untuk mencoba
    requests.get(url) # request.get (url) berguna untuk mendapatkan url yang diminta
    print('sukses')
except Exception as e: # (except = menerima) berguna untuk menerima
    print('ada error\n', e) # e untuk menampung error pada exception