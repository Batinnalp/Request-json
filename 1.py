import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

veri = response.text
print("İlk 80 karakter:", veri[:80])

import requests

url = "https://jsonplaceholder.typicode.com/comments/1"

response = requests.get(url)

if response.status_code == 200:
    print("Başarılı istek!")
else:
    print("Hata oluştu, durum kodu:", response.status_code)

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
veriler = response.json()
ilk_kullanici = veriler[0]
print("İlk kullanıcının ismi:", ilk_kullanici["name"])

import json

json_veri = '{"isim": "Zeynep", "yas": 23}'
veri = json.loads(json_veri)
print("İsim:", veri["isim"])
print("Yaş:", veri["yas"])

import json

json_veri = '{"puanlar": [80, 90, 100]}'

veri = json.loads(json_veri)
puanlar = veri["puanlar"]
ortalama = sum(puanlar) / len(puanlar)
print("Ortalama puan:", ortalama)

import json

json_veri = '{"kullanici": "Ali", "aktif": true}'

veri = json.loads(json_veri)
aktif_mi = veri["aktif"]
print("Aktif mi?", aktif_mi)

import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
veri = response.json()
print("e-mail:", veri["email"])

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
gonderiler = response.json()
for i in range(3):
    print(f"{i+1}. Başlık:", gonderiler[i]["title"])

import requests

url = "https://jsonplaceholder.typicode.com/comments?postId=1"
response = requests.get(url)
yorumlar = response.json()
ilk_yorum = yorumlar[0]
print("Yorum adı:", ilk_yorum["name"])
print("Yorum İçeriği:", ilk_yorum["body"])

import requests

url = "https://jsonplaceholder.typicode.com/posts"
parametreler = {"userId": 2}
response = requests.get(url, params=parametreler)
gonderiler = response.json()
for gonderi in gonderiler:
    print("Başlık:", gonderi["title"])

import requests

url = "https://jsonplaceholder.typicode.com/comments"
parametreler = {"postId": 3}
response = requests.get(url, params=parametreler)
yorumlar = response.json()
for i in range(2):
    print(f"{i+1}. e-mail:", yorumlar[i]["email"])

import requests

url = "https://jsonplaceholder.typicode.com/posts"
parametreler = {"_limit": 4}
response = requests.get(url, params=parametreler)
gonderiler = response.json()
for gonderi in gonderiler:
    print("Gönderi ID:", gonderi["id"])

import requests

url = "https://httpbin.org/headers"
headers = {
    "User-Agent": "MyTestClient/1.0"
}

response = requests.get(url, headers=headers)
veri = response.json()
print("Sunucunun gördüğü header'lar:", veri["headers"])

import requests

url = "https://httpbin.org/bearer"

headers = {
    "Authorization": "Bearer 12345abcde"
}

response = requests.get(url, headers=headers)

print("Sunucunun cevabı:", response.json())

import requests

url = "https://httpbin.org/anything"
headers = {
    "x-api-key": "test_key_98765"
}

response = requests.get(url, headers=headers)
veri = response.json()
print("Sunucunun gördüğü header:", veri["headers"])

import requests

url = "https://httpbin.org/post"
veri = {
    "ad": "Batın",
    "Soyad": "Kayalıdere"
}

response = requests.post(url, data=veri)
cevap = response.json()
print("Sunucuya ulaşan form verisi:", cevap["form"])

import requests

url = "https://httpbin.org/post"
veri = {
    "kullanici": "Ali",
    "aktif": True
}

response = requests.post(url, json=veri)
cevap = response.json()
print("Sunucuya ulaşan JSON veri:", cevap["json"])

import requests
import json

url = "https://httpbin.org/post"
veri = {
    "kitap": "1984",
    "adet": 3
}

json_veri = json.dumps(veri)
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json_veri, headers=headers)
cevap = response.json()
print("Sunucuya ulaşan json:", cevap["json"])

veri = [
    {"id": 1, "isim": "Ali", "puan": 85},
    {"id": 2, "isim": "Ayşe", "puan": 92},
    {"id": 3, "isim": "Can", "puan": 75}
]

for ogrenci in veri:
    if ogrenci["puan"] > 80:
        print(f"{ogrenci['isim']} başarılı. Puan: {ogrenci["puan"]}")

veri = [
    {"id": 1, "isim": "Ali", "puan": 85},
    {"id": 2, "isim": "Ayşe", "puan": 92},
    {"id": 3, "isim": "Can", "puan": 75}
]

toplam = 0

for ogrenci in veri:
    toplam += ogrenci["puan"]
ortalama = toplam / len(veri)
print("Toplam puan:", toplam)
print("Ortalama puan:", ortalama)

import requests

try:
    url = "https://jsonplaceholder.typicode.com/yanlis-endpoint"
    response = requests.get(url)
    response.raise_for_status()
    print("Veri alındı:", response.json())
except requests.exceptions.HTTPError as e:
    print("Bir HTTP hatası oluştu:", e)

import requests

try:
    url = "https://httpbin.org/delay/3"
    response = requests.get(url, timeout=1)
    print("Durum kodu:", response.status_code)
except requests.exceptions.Timeout:
    print("Hata: İstek zaman aşımına uğradı.")