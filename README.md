# Simplex

This assignment implements REST API for getting a quote for exchanging money from one
currency to another.

This project implemented in Python, uses FastAPI platform.

Running file: controller/quote_controller.

Swagger link: localhost:5000/docs

The API:
Full path: GET localhost:5000/docs/api/quote

This API gets 3 arguments as an input:
* from_currency_code
* amount
* to_currency_code


Dependencies:
* fastapi - version 0.79.0
* uvicorn - version 0.18.2
* pydantic - version 1.9.1
* requests - version 2.28.1

