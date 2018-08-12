from django.shortcuts import render

from push.send import send_message


def send_notification(request):
    sent = []
    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST['text']
        for token in request.user.firebasepushtoken_set.all():
            send_message(token.token, text)
            sent.append(token.token)

    return render(request, 'push/index.html', {'sent': sent})
