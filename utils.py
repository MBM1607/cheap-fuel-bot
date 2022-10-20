from datetime import datetime

import requests

import config


def fetch_prices(text: str) -> str:
    if text not in config.REGIONS:
        return "There was a problem in the name you used, please enter different name"

    response = requests.get(config.API_URL)

    if response.ok:
        json = response.json()
        regional_prices = [
            item["prices"] for item in json["regions"] if item["region"] == text
        ]

        prices = str(regional_prices)

        prices += f"\n{datetime.fromtimestamp(json['updated']).isoformat(sep=' ')}"
        return prices
    else:
        return (
            "There was a problem with fetching the prices from api. Please try later!"
        )
