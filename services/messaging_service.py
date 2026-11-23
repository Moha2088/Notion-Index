from twilio.http.http_client import os
from config.twilio_client import twilio_client


FROM_NUMBER = os.getenv("FROM_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")



def send_message(body: str) -> None:
    twilio_client.messages.create(
        from_=FROM_NUMBER,
        to=TO_NUMBER,
        body=body
    )