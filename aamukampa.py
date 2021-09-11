import ast, gspread, tweepy, datetime, sheetin_luku, twiittaus

api = twiittaus.alusta("twitter_keys.txt")
with open("sheet_id.txt") as f:
    sheet_id = f.readline().rstrip()

taulukko = sheetin_luku.anna_taulukko("service_worker.json", sheet_id)

tyoaamuja = sheetin_luku.lue(taulukko, "Sheet1", "A2")
aamuja_kaikkiaan = sheetin_luku.lue(taulukko, "Sheet1", "C2")

if int(tyoaamuja) < 0 or int(aamuja_kaikkiaan) < 0:
    pass
else:
    twiittaus.twiittaa(api, f"Työaamuja vielä jäljellä {tyoaamuja}\nAamuja kaikkiaan jäljellä {aamuja_kaikkiaan}")
