import os
from dotenv import load_dotenv
import requests


load_dotenv()


def get_transaction_amount_rub(transaction: dict) -> float:
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']
    if currency == 'RUB':
        return amount
    else:
        key = os.getenv("API_KEY")
        headers = {"apikey": key}
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        response = requests.request("GET", url, headers=headers)

        result = response.json()
        return float(result['result'])
