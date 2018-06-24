import firebase_admin
from firebase_admin import messaging, credentials

app = None

def send_message(registration_token, data):
    if not app:
        cred = credentials.Certificate('credentials.json')
        app = firebase_admin.initialize_app(credential=cred)
    message = messaging.Message(
        data=data,
        token=registration_token,
    )
    messaging.send(message)
