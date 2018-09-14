import datetime
import firebase_admin
from firebase_admin import messaging, credentials
from firebase_admin.messaging import ApiCallError
from django.conf import settings
from push.models import FirebasePushToken


def send_message_user(user, message):
    for token in user.firebasepushtoken_set.all().values_list('token', flat=True):
        message_id = send_message_token(token, message)
        if not message_id:
            FirebasePushToken.objects.filter(token=token).delete()


def send_message_token(registration_token, message):
    if not send_message_token.app:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        send_message_token.app = firebase_admin.initialize_app(credential=cred)
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

    message_id = None
    try:
        message_id = messaging.send(message)
    except ApiCallError:
        pass
    return message_id


send_message_token.app = None
