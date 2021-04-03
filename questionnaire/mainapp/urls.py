from django.urls import path

from mainapp.views import IndexView, PollView


urlpatterns = [
    path('', IndexView.as_view(), name='poll-list'),
    path('<int:pk>/', PollView.as_view(), name='poll-view')
]