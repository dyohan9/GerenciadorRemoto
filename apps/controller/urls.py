from django.urls import path

from apps.controller.views import CallCelery

app_name = 'controller'

urlpatterns = [
    path('callcelery', CallCelery.as_view(), name='callcelery'),
]