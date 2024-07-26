from django.core.mail import send_mail
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from materials.models import Course, Lesson
from materials.paginations import CustomPagination
from materials.serializers import CourseSerializer, LessonSerializer
from users.models import User


class CourseListApiView(ListAPIView):
    """Просмотр списка курсов."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination
    permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )


class CourseCreateApiView(CreateAPIView):
    """Создание курса."""

    serializer_class = CourseSerializer
    permission_classes = (IsAdminUser,)


class CourseDetailApiView(RetrieveAPIView):
    """Просмотр выбранного курса."""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )


class CourseUpdateApiView(UpdateAPIView):
    """Редактирование выбранного курса."""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAdminUser,)


class CourseDestroyApiView(DestroyAPIView):
    """Удаление выбранного курса."""

    permission_classes = (IsAdminUser,)
    queryset = Course.objects.all()


class LessonListApiView(ListAPIView):
    """Просмотр списка уроков."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination
    permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )


class LessonCreateApiView(CreateAPIView):
    """Создание урока."""

    serializer_class = LessonSerializer
    permission_classes = (IsAdminUser,)


class LessonDetailApiView(RetrieveAPIView):
    """Просмотр выбранного урока."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )


class LessonUpdateApiView(UpdateAPIView):
    """Редактирование выбранного урока."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAdminUser,)


class LessonDestroyApiView(DestroyAPIView):
    """Удаление выбранного урока."""

    permission_classes = (IsAdminUser,)
    queryset = Lesson.objects.all()


class GetLessonsList(APIView):
    """ Получение списка уроков по id курса. """

    def get(self, request, *args, **kwargs):

        permission_classes = (IsAdminUser, IsAuthenticated,)

        course_pk = kwargs["course_pk"]
        lessons = Lesson.objects.filter(course=course_pk).values()

        return Response({"Темы доступных уроков": list(lessons)})




class SendContent(APIView):
    """Отправка пользователю ссылки на выбранный урок по id урока и id пользователя."""

    permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )

    def post(self, request, *args, **kwargs):
        lesson_pk = kwargs["lesson_pk"]
        url = Lesson.objects.get(pk=lesson_pk).url

        user_pk = kwargs["user_pk"]
        user_email = User.objects.get(pk=user_pk).email
        send_mail(
            subject="Ссылка на урок",
            message=f"Ваша ссылка на запрошенный контент: {url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user_email],
        )
        return Response(
            {"message": "На Ваш email отправлена ссылка на контент выбранного урока"}
        )
