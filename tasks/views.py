from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tasks.filters import TaskFilter
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['title']

    def get_queryset(self):
        qs = Task.objects.filter(owner=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
