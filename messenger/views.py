from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from messenger.models import *


@login_required()
def messages(request):

    my_messages = Message.objects.get_inbox(request.user)

    data = {
        'messages': my_messages
    }
    print(my_messages)
    return render(request, 'messenger/messages.html', data)