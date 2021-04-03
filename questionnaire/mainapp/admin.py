from django.contrib import admin

from mainapp.models import Poll, Choice

admin.site.register(Poll)
admin.site.register(Choice)