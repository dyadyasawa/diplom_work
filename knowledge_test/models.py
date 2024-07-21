
from django.db import models

from materials.models import Course

# NULLABLE = {"null": True, "blank": True}


class CourseTest(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название теста")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.name


class Question(models.Model):
    course_test = models.ForeignKey(CourseTest, on_delete=models.CASCADE, verbose_name="Тест")
    question_text = models.CharField(max_length=300, verbose_name="Текст вопроса")

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer_text = models.CharField(max_length=300, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильность ответа")

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"

    def __str__(self):
        return f"{self.answer_text}({self.is_correct})"
