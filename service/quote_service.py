import requests
import json
from model.config import settings


def get_data_from_api(from_currency_code, to_currency_code):
    for provider_name, url in settings.apis:
        response = requests.get(f'{url}/{from_currency_code}')
        if response.ok:
            text = json.loads(response.text)
            exchange_rate = get_rate(text, to_currency_code)
            if exchange_rate is not None:
                return exchange_rate, provider_name


def get_rate(text, to_currency_code):
    rates = text.get("rates")
    value = rates.get(to_currency_code, None)
    return value

