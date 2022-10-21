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
        ][0]

        prices = [f"Lowest Prices for {text}"]

        for price in regional_prices:
            prices.append("")
            prices.append(f"Type: {price['type']}")
            prices.append(f"**Price: {price['price']}**")
            prices.append(f"Name: {price['name']}")
            prices.append(f"Suburb: {price['suburb']}")
            prices.append(
                f"Location: https://maps.google.com/?q={price['lat']},{price['lng']}"
            )
            prices.append("")

        prices.append(
            f"Last Updated at: {datetime.fromtimestamp(json['updated']).isoformat(sep=' ')}"
        )

        return "\n".join(prices)
    else:
        return (
            "There was a problem with fetching the prices from api. Please try later!"
        )
