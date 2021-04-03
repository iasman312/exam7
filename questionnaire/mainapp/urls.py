from django.urls import path

from mainapp.views import IndexView, PollView, CreatePollView, \
    PollUpdateView, PollDeleteView, PollChoicesCreate


urlpatterns = [
    path('', IndexView.as_view(), name='poll-list'),
    path('add/', CreatePollView.as_view(), name='poll-add'),
    path('<int:pk>/', PollView.as_view(), name='poll-view'),
    path('<int:pk>/update/', PollUpdateView.as_view(), name='poll-update'),
    path('<int:pk>/delete/', PollDeleteView.as_view(), name='poll-delete'),
    path('<int:pk>/choices/add/', PollChoicesCreate.as_view(),
         name='poll-choices-add')
]