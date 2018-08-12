import firebase_admin
from firebase_admin import messaging, credentials
from django.conf import settings


def send_message(registration_token, data):
    if not send_message.app:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        send_message.app = firebase_admin.initialize_app(credential=cred)
    message = messaging.Message(
        data=data,
        token=registration_token,
    )
    messaging.send(message)


send_message.app = None
