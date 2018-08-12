import datetime
import firebase_admin
from firebase_admin import messaging, credentials
from django.conf import settings


def send_message(registration_token, message):
    if not send_message.app:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        send_message.app = firebase_admin.initialize_app(credential=cred)
    message = messaging.Message(
        notification=messaging.Notification(
            title='Live in Concert',
            body=message
        ),
        data={
            'click_action': 'FLUTTER_NOTIFICATION_CLICK',
        },
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(days=1),
        ),
        token=registration_token
    )
    print(messaging.send(message))


send_message.app = None
