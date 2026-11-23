from dotenv import load_dotenv
from twilio.http.http_client import os
from twilio.rest import Client

AUTH_TOKEN = os.getenv("AUTH_TOKEN")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)