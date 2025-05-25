from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Task(BaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(_("название"), max_length=200)
    description = models.TextField( _("описание"), blank=True, null=True)
    completed = models.BooleanField(_("выполнено"), default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("задача")
        verbose_name_plural = _("задачи")

    def __str__(self):
        return self.title