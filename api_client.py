import requests

from typing import List, Dict

BASE_URL = "https://www.metaweather.com/api/location"

def get_woeids(query_params: Dict) -> List[str]:
    url = f"{BASE_URL}/search/"
    resp = requests.get(url, params=query_params)
    woeids = list()
    if resp.json():
        for result in resp.json():
            woeids.append(result["woeid"])
    return woeids

def get_weather_forecast(woeids: List[str]) -> List[Dict]:
    results = list()
    for woeid in woeids:
        url = f"{BASE_URL}/{woeid}/"
        resp = requests.get(url)
        if resp.json():
            results.append({
                "location": resp.json()["title"],
                "forecast": resp.json()["consolidated_weather"]
            })
    return results