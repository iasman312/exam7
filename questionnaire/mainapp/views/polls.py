from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from mainapp.models import Poll
from mainapp.forms import PollForm


class IndexView(ListView):
    template_name = 'polls/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    model = Poll
    template_name = 'polls/view.html'


class CreatePollView(CreateView):
    template_name = 'polls/create.html'
    form_class = PollForm
    model = Poll
    success_url = reverse_lazy('poll-list')