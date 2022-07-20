from model.output_quote import OutputQuote
from service.quote_service import get_data_from_api
import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.route("/api/quote", methods=['GET'])
async def data(from_currency_code, amount, to_currency_code):
    exchange_rate, provider_name = get_data_from_api(from_currency_code, to_currency_code)
    output = OutputQuote(exchange_rate=exchange_rate,
                         currency_code=to_currency_code,
                         amount_output=float(amount) * exchange_rate,
                         provider_name=provider_name)

    return output


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)
