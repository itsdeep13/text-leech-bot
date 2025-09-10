import os

API_ID    = os.environ.get("API_ID", "27473563")
API_HASH  = os.environ.get("API_HASH", "bc2ea0765ac96bb474891b0243f44390")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7102120132:AAH0S88KlVWNcJnWKLxcIUQmc6lDsleq7is") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
