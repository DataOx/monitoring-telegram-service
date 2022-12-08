from django.urls import path

from .views import MessagesInfoView

urlpatterns = [
    path('message-info/', MessagesInfoView.as_view())
]
