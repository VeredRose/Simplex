
from pydantic import BaseModel


class OutputQuote(BaseModel):
    exchange_rate: float
    currency_code: str
    amount_output: float
    provider_name: str



