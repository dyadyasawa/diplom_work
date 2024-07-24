from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from knowledge_test.models import Answer, CourseTest, Question
from materials.models import Course
from users.models import User


class CourseTestTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com", is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="Информатика", description="Про компьютеры и т.п."
        )
        self.course_test = CourseTest.objects.create(
            name="Тест по информатике", course=self.course
        )

    def test_course_test_retrieve(self):
        url = reverse("knowledge_test:course_test_detail", args=(self.course_test.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course_test.name)

    def test_course_test_create(self):
        url = reverse("knowledge_test:course_test_create")
        data = {"name": "Тест по литературе"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            CourseTest.objects.filter(name="Тест по литературе").count(), 1
        )

    def test_course_test_update(self):
        url = reverse("knowledge_test:course_test_update", args=(self.course_test.pk,))
        data = {"name": "Тест по биологии"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Тест по биологии")

    def test_course_test_delete(self):
        url = reverse("knowledge_test:course_test_delete", args=(self.course_test.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CourseTest.objects.all().count(), 0)

    def test_course_test_list(self):
        url = reverse("knowledge_test:course_test_list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course_test.pk,
                    "name": self.course_test.name,
                    "course": self.course.pk,
                }
            ],
        }

        self.assertEqual(data, result)


class QuestionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com", is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="Информатика", description="Про компьютеры и т.п."
        )
        self.course_test = CourseTest.objects.create(
            name="Тест по информатике", course=self.course
        )
        self.question = Question.objects.create(
            question_text="Доколе?", course_test=self.course_test
        )

    def test_question_retrieve(self):
        url = reverse("knowledge_test:question_detail", args=(self.question.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("question_text"), self.question.question_text)

    def test_question_create(self):
        url = reverse("knowledge_test:question_create")
        data = {"question_text": "Который час?"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.filter(question_text="Доколе?").count(), 1)

    # def test_question_update(self):
    #     url = reverse("knowledge_test:question_update", args=(self.question.pk,))
    #     data = {
    #         "question_text": "Текст"
    #     }
    #     response = self.client.patch(url, data)
    #     data = response.json()
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         data.get("question_text"), "Текст"
    #     )

    # def test_question_delete(self):
    #     url = reverse("knowledge_test:question_delete", args=(self.question.pk,))
    #     response = self.client.delete(url)
    #     self.assertEqual(
    #         response.status_code, status.HTTP_204_NO_CONTENT
    #     )
    #     self.assertEqual(
    #         Question.objects.all().count(), 0
    #     )

    def test_question_list(self):
        url = reverse("knowledge_test:question_list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.question.pk,
                    "question_text": self.question.question_text,
                    "course_test": self.course_test.pk,
                }
            ],
        }
        self.assertEqual(data, result)


class AnswerTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com", is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="Информатика", description="Про компьютеры и т.п."
        )
        self.course_test = CourseTest.objects.create(
            name="Тест по информатике", course=self.course
        )
        self.question = Question.objects.create(
            question_text="Доколе?", course_test=self.course_test
        )
        self.answer = Answer.objects.create(
            question=self.question, answer_text="Потому что", is_correct=False
        )

    def test_answer_retrieve(self):
        url = reverse("knowledge_test:answer_detail", args=(self.answer.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("answer_text"), self.answer.answer_text)

    def test_answer_create(self):
        url = reverse("knowledge_test:answer_create")
        data = {"answer_text": "42", "is_correct": False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.filter(is_correct=False).count(), 2)

    def test_answer_update(self):
        url = reverse("knowledge_test:answer_update", args=(self.answer.pk,))
        data = {"answer_text": "Никогда"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("answer_text"), "Никогда")

    def test_answer_delete(self):
        url = reverse("knowledge_test:answer_delete", args=(self.answer.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Answer.objects.all().count(), 0)

    def test_answer_list(self):
        url = reverse("knowledge_test:answer_list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.answer.pk,
                    "answer_text": self.answer.answer_text,
                    "is_correct": False,
                    "question": self.question.pk,
                }
            ],
        }
        self.assertEqual(data, result)
