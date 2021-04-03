from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from mainapp.models import Poll, Answer, Choice
from mainapp.forms import PollForm


class PollChoicesAnswer(TemplateView):
    template_name = 'answers/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = get_object_or_404(Poll, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=kwargs.get('pk'))
        choice = Choice.objects.get(choice=request.POST.get('choice'))
        Answer.objects.create(poll=poll, choice=choice)
        return redirect('poll-list')


