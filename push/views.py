from django.shortcuts import render

from push.send import send_message


def send_notification(request):
    sent = []
    if request.method == 'post' and request.user.is_authenticated:
        text = request.data['text']

        for token in request.user.firebase_push_token_set.all():
            send_message(token.token, text)
            sent.append(token.token)

    return render(request, 'push/index.html', {'sent': sent})
