from django.shortcuts import render

from push.send import send_message_user


def send_notification(request):
    sent = []
    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST['text']
        send_message_user(request.user, text)

    return render(request, 'push/index.html', {'sent': sent})
