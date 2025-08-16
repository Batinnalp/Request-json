import requests

sehir = input("Hangi şehrin hava durumunu öğrenmek istiyorsunuz?")
api_key = "b386cbb1b3f75ada947614166fa76a4a"
url = "https://api.openweathermap.org/data/2.5/weather"
parametreler = {
    "q": sehir,
    "appid": api_key,
    "units": "metric",
    "lang": "tr"
}

try:
    response = requests.get(url, params=parametreler, timeout=5)
    response.raise_for_status()
    veri = response.json()

    print(f"{sehir} için hava durumu:")
    print("Sıcaklık:", veri["main"]["temp"], "°C")
    print("Hissedilen:", veri["main"]["feels_like"], "°C")
    print("Durum:", veri["weather"][0]["description"])
except requests.exceptions.HTTPError as e:
    print("API'den hata cevabı geldi:", e)
except requests.exceptions.Timeout:
    print("Hata: İstek zaman aşımına uğradı.")
except requests.exceptions.RequestException as e:
    print("Bir hata oluştu:", e)