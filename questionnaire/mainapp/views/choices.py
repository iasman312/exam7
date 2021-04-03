from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy


from mainapp.forms import ChoiceForm
from mainapp.models import Choice, Poll


class PollChoicesCreate(CreateView):
    template_name = 'choices/create.html'
    form_class = ChoiceForm
    model = Choice

    def get_success_url(self):
        return reverse(
            'poll-view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)


class PollChoicesUpdate(UpdateView):
    form_class = ChoiceForm
    model = Choice
    template_name = 'choices/update.html'
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll-view', kwargs={'pk': self.kwargs.get('pk')})


class PollChoicesDelete(DeleteView):
    model = Choice
    template_name = 'choices/delete.html'
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll-view', kwargs={'pk': self.object.poll.pk})
