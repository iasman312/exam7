from django.views.generic import ListView, DetailView, CreateView, UpdateView
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


class PollUpdateView(UpdateView):
    form_class = PollForm
    model = Poll
    template_name = 'polls/update.html'
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll-view', kwargs={'pk': self.kwargs.get('pk')})
