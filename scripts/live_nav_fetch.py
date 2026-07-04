import requests
import pandas as pd

amfi_code = 119551

url = f"https://api.mfapi.in/mf/{amfi_code}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    latest = data["data"][0]

    print("Scheme :", data["meta"]["scheme_name"])
    print("Date   :", latest["date"])
    print("NAV    :", latest["nav"])

else:
    print("Unable to fetch NAV.")