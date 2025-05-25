from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task
from rest_framework_simplejwt.tokens import RefreshToken


class TaskCRUDTest(APITestCase):
    def setUp(self):
        # Создаём пользователя и получаем JWTsdsdsd
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        # Начальные данные
        self.create_url = reverse("tasks-list")  # /tasks/

    def test_create_task(self):
        data = {"title": "New Task", "description": "Test desc", "completed": False}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.title, data["title"])
        self.assertEqual(task.owner, self.user)

    def test_get_task_list(self):
        Task.objects.create(owner=self.user, title="Task1")
        Task.objects.create(owner=self.user, title="Task2", completed=True)
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_get_task_detail(self):
        task = Task.objects.create(owner=self.user, title="Detail Task")
        url = reverse("tasks-detail", args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], task.title)

    def test_update_task(self):
        task = Task.objects.create(owner=self.user, title="Old Title")
        url = reverse("tasks-detail", args=[task.id])
        data = {"title": "Updated Title", "completed": True}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, data["title"])
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = Task.objects.create(owner=self.user, title="To Delete")
        url = reverse("tasks-detail", args=[task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
