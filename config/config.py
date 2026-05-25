import os

from dotenv import load_dotenv

load_dotenv()

def get_value_from_config(key):
    value = os.getenv(key.upper())
    # if key == "browsers":
    #     return [b.strip() for b in value.split(",")]

    if value is None:
        raise ValueError(f"{key} environment variable is not found in .env file")
    return value