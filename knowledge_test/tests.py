
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from knowledge_test.models import CourseTest, Question, Answer
from materials.models import Course
from users.models import User


class CourseTestTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com", is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Информатика", description="Про компьютеры и т.п.")
        self.course_test = CourseTest.objects.create(name="Тест по информатике", course=self.course)

    def test_course_test_retrieve(self):
        url = reverse("knowledge_test:course_test_detail", args=(self.course_test.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course_test.name)

    def test_course_test_create(self):
        url = reverse("knowledge_test:course_test_create")
        data = {
            "name": "Тест по литературе"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            CourseTest.objects.filter(name="Тест по литературе").count(), 1
        )

    def test_lesson_update(self):
        url = reverse("knowledge_test:course_test_update", args=(self.course_test.pk,))
        data = {
            "name": "Тест по биологии"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Тест по биологии"
        )

    def test_knowledge_test_delete(self):
        url = reverse("knowledge_test:course_test_delete", args=(self.course_test.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            CourseTest.objects.all().count(), 0
        )

    def test_knowledge_list(self):
        url = reverse("knowledge_test:course_test_list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = [
            {
                 "id": self.course_test.pk,
                 "name": self.course_test.name,
                 "course": self.course.pk

                }
            ]
        self.assertEqual(
            data, result
        )
