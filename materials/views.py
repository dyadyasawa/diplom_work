
# from django.shortcuts import render

# from django.views.generic import (
#     TemplateView,
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView,
# )
#
# from materials.models import Course, Lesson
#
#
# class StartPageView(TemplateView):
#     template_name = "materials_app/start_page.html"
#
#
# class CoursesListView(ListView):
#     model = Course
#     template_name = "materials_app/courses_list.html"
#
#
# class CourseDetailView(ListView):
#     model = Course
#     template_name = "materials_app/course_detail.html"
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset(*args, **kwargs)
#         c = Course.objects.get(pk=self.kwargs.get('pk'))
#
#         queryset = c.lesson_set.all()
#
#         return queryset

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser  # , AllowAny

from materials.models import Course, Lesson
from materials.paginations import CustomPagination
from materials.serializers import CourseSerializer, LessonSerializer


class CourseListApiView(ListAPIView):  # Работает
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsAdminUser,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Course.objects.all()
    #     elif user.is_authenticated:
    #         return Course.objects.filter(owner=user)


class CourseCreateApiView(CreateAPIView):  # Работает
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUser,)

    # def perform_create(self, serializer):
    #     """Делаем текущего пользователя 'Создателем' привычки."""
    #     new_course = serializer.save()
    #     new_course.owner = self.request.user
    #     new_lesson.save()


class CourseDetailApiView(RetrieveAPIView):  # Работает
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Course.objects.filter(owner=user)


class CourseUpdateApiView(UpdateAPIView):  # Работает
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAdminUser,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Course.objects.filter(owner=user)


class CourseDestroyApiView(DestroyAPIView):  # Работает
    permission_classes = (IsAdminUser,)
    queryset = Course.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Course.objects.filter(owner=user)


class LessonListApiView(ListAPIView):  # Работает
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsAdminUser,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Lesson.objects.all()
    #     elif user.is_authenticated:
    #         return Lesson.objects.filter(owner=user)


class LessonCreateApiView(CreateAPIView):  # Работает
    serializer_class = LessonSerializer
    permission_classes = (IsAdminUser,)

    # def perform_create(self, serializer):
    #     """Делаем текущего пользователя 'Создателем' привычки."""
    #     new_lesson = serializer.save()
    #     new_lesson.owner = self.request.user
    #     new_lesson.save()


class LessonDetailApiView(RetrieveAPIView):  # Работает
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)

    # def get_queryset(self):
    #     # user = self.request.user
    #     # if user.is_authenticated or user.is_superuser:
    #     return Lesson.objects.filter(pk=)


class LessonUpdateApiView(UpdateAPIView):  # Работает
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAdminUser,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Lesson.objects.filter(owner=user)


class LessonDestroyApiView(DestroyAPIView):  # Работает
    permission_classes = (IsAdminUser,)
    queryset = Lesson.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Lesson.objects.filter(owner=user)
