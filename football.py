import requests

team_name = input("Takım adını girin:")

search_url = f"https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={team_name}"
response = requests.get(search_url)
print("Durum Kodu:", response.status_code)
print("Cevap Metni:", response.text)
data = response.json()

teams = data.get("teams")

if not teams:
    print("Takım bulunamadı")
else:
    team = teams[0]
    print("\n📋 Takım Bilgisi")
    print("Adı:", team["strTeam"])
    print("Ülke:", team["strCountry"])
    print("Kuruluş Yılı:", team["intFormedYear"])
    print("Stadyum:", team["strStadium"])
    print("Açıklama:", team["strDescriptionEN"][:300], "...")