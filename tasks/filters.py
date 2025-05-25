import django_filters

from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter(field_name="completed")
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    created_at = django_filters.DateFromToRangeFilter(field_name="created_at")
    updated_at = django_filters.DateFromToRangeFilter(field_name="updated_at")

    class Meta:
        model = Task
        fields = [
            "completed",
            "title",
            "created_at",
            "updated_at",
        ]
