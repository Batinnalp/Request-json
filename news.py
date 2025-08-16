import requests

url = "https://newsapi.org/v2/top-headlines"
api_key = input("NewsAPI API key'inizi girin: ").strip()
konu = input("Hangi konuda haberler görmek istersiniz?").strip()
ulke = input("Ülke kodu veya boş geçmek için Enter:").strip().lower()

params = {
    "apiKey": api_key,
    "q": konu or None,
    "country": ulke or None,
    "pageSize": 10
}

params = {k: v for k, v in params.items() if v}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()

    if data.get("status") != "ok":
        print("API hatası:", data.get("message"))
    else:
        articles = data.get("articles", [])
        if not articles:
            print("Bu kriterlere uygun haber bulunamadı.")
        else:
            for i, art in enumerate(articles, start=1):
                başlık = art.get("title")
                kaynak = art.get("source", {}).get("name")
                print(f"{i}. {başlık} ({kaynak})")

except requests.exceptions.HTTPError as http_err:
    print("HTTP Hatası:", http_err)
except requests.exceptions.Timeout:
    print("Zaman aşımı oldu: Bağlantıyı kontrol edin.")
except requests.exceptions.RequestException as err:
    print("İstek sırasında genel bir hata oluştu:", err)