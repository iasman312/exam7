from django.urls import path

from mainapp.views import IndexView, PollView, CreatePollView


urlpatterns = [
    path('', IndexView.as_view(), name='poll-list'),
    path('add/', CreatePollView.as_view(), name='poll-add'),
    path('<int:pk>/', PollView.as_view(), name='poll-view'),
]