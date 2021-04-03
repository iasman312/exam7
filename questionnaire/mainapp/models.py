from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=1000, null=False, blank=False,
                                verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True)


class Choice(models.Model):
    choice = models.TextField(max_length=1000, null=False, blank=False,
                              verbose_name='Вариант ответа')
    poll = models.ForeignKey('mainapp.Poll', on_delete=models.CASCADE,
                             related_name='choices', verbose_name='Опрос',
                             null=False, blank=False)


