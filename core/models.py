from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("дата создания"), db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(_("дата обновления"), db_index=True, auto_now=True)

    class Meta:
        abstract = True