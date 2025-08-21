import requests

'''response = requests.get("https://randomuser.me/api/")
data = response.json()

print(data)'''

'''kisi_sayisi = int(input("Kaç kişi oluşturulsun ?"))

url = f"https://randomuser.me/api/?results={kisi_sayisi}"
response = requests.get(url)
data = response.json()
print(data)'''

kac_kisi = int(input("Kaç kişi oluşturulsun ?"))

url = f"https://randomuser.me/api/?results={kac_kisi}"
response = requests.get(url)
data = response.json()

for i, kisi in enumerate(data["results"], start=1):
    ad = kisi["name"]["first"]
    soyad = kisi["name"]["last"]
    email = kisi["email"]
    ulke = kisi["location"]["country"]
    foto = kisi["picture"]["large"]

    print(f"\n📍 Kullanıcı {i}")
    print(f"Ad Soyad : {ad} {soyad}")
    print(f"E-posta  : {email}")
    print(f"Ülke     : {ulke}")
    print(f"Fotoğraf : {foto}")