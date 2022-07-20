from pydantic import BaseModel


class Settings(BaseModel):
    apis = [
        ("exchangerate", "https://api.exchangerate-api.com/v4/latest/"),
        ("frankfurter", "https://api.frankfurter.app/latest?from=")
        ]


settings = Settings()
