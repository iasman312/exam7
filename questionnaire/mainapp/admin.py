from django.contrib import admin

from mainapp.models import Poll, Choice, Answer

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)