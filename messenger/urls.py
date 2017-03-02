from django.conf.urls import url
import messenger.views as mess_views

urlpatterns = [

    url(r'^messages/$', mess_views.messages, name='my_messages'),

]