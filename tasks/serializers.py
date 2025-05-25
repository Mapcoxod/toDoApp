from rest_framework import serializers

from tasks.models import Task, Participant


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "completed", "created_at", "updated_at"]


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = [
            "id",
            "company_name",
            "bin",
            "status",
            "issue_date",
            "expiration_date",
            "created_at",
        ]
