import ssl
import requests
import certifi
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

class TLSAdapter(HTTPAdapter):
    """Sadece TLSv1.2 ve üstünü kullanacak bir HTTPS adapter."""
    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        ctx = ssl.create_default_context(cafile=certifi.where())
        # Eski TLS/SSL sürümlerini kapat
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_context=ctx,
        )

# 1️⃣ Session oluştur ve adapter’ı mount et
session = requests.Session()
session.mount("https://", TLSAdapter())

# 2️⃣ API endpoint ve header
url = "https://api.coinranking.com/v2/coins"
headers = {"x-access-token": "YOUR_API_KEY_HERE"}

# 3️⃣ Kaç coin çekeceğini sor
try:
    adet = int(input("Kaç coin gösterilsin? (örn: 5) "))
except ValueError:
    print("Geçersiz sayı; varsayılan 5 kullanılıyor.")
    adet = 5

params = {"limit": adet}

try:
    # 4️⃣ Güvenli istek: verify sertifikayı certifi’den alıyor
    resp = session.get(url, headers=headers, params=params, timeout=5, verify=certifi.where())
    resp.raise_for_status()

    coins = resp.json()["data"]["coins"]
    for c in coins:
        print(f"{c['rank']}. {c['name']} ({c['symbol']}): ${c['price']}")

except requests.exceptions.SSLError as e:
    print("🔒 SSL hatası:", e)
except requests.exceptions.HTTPError as e:
    print("🛑 HTTP hatası:", e)
except requests.exceptions.RequestException as e:
    print("❌ Genel istek hatası:", e)
