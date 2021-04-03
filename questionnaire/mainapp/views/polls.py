from django.views.generic import ListView
from mainapp.models import Poll


class IndexView(ListView):
    template_name = 'polls/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1