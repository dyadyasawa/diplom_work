from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(
        upload_to="materials/courses", verbose_name="Превью", **NULLABLE
    )
    last_update_date = models.DateTimeField(
        auto_now=True, **NULLABLE, verbose_name="Дата последнего обновления"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    preview = models.ImageField(
        upload_to="lms/lessons", verbose_name="Превью", **NULLABLE
    )
    url = models.CharField(max_length=100, verbose_name="Ссылка на видео", **NULLABLE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", **NULLABLE
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
