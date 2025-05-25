from django.core.management import call_command
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.filters import TaskFilter
from tasks.models import Task, Participant
from tasks.serializers import TaskSerializer, ParticipantSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticated]
    search_fields = ["title"]

    def get_queryset(self):
        qs = Task.objects.filter(owner=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ParseParticipantsView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParticipantSerializer

    def get(self, request, *args, **kwargs):
        call_command("astanahub_parser")

        qs = Participant.objects.all()[:10]
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
