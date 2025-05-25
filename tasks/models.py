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


class Participant(BaseModel):
    company_name = models.CharField(_("наименование компании"), max_length=255)
    bin = models.CharField(_("БИН"), max_length=255)
    status = models.CharField(
        _("статус"),
        null=True,
        blank=True,
        max_length=50,
    )
    issue_date = models.DateField(
        verbose_name="дата выдачи",
        null=True,
        blank=True,
    )
    expiration_date = models.DateField(
        verbose_name="срок действия",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("участник")
        verbose_name_plural = _("участники")

    def __str__(self):
        return self.company_name
