from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(_('Sarlavha'), max_length=50)
    description = models.TextField(_('Batafsil'))

    def __str__(self):
        return self.title