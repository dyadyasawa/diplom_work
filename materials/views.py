
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
from rest_framework.views import APIView
from django.core.mail import send_mail

from materials.models import Course, Lesson
from users.models import User
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


class SendContent(APIView):
    def post(self, request, *args, **kwargs):
        lesson_pk = kwargs["lesson_pk"]
        user_pk = kwargs["user_pk"]

        # model = User
        # template_name = "users_app/user_form.html"
        # form_class = UserRegisterForm
        # success_url = reverse_lazy("users:register_message")
        #
        # def form_valid(self, form):
        #     user = form.save()
        #     user.is_active = False
        #     code = secrets.token_hex(8)
        #     user.code = code
        #     user.save()
        #     host = self.request.get_host()
        #     url = f"http://{host}/users/email_confirm/{code}/"
        #
        #     send_mail(
        #         subject="Подтверждение почты",
        #         message=f"Перейдите по ссылке для подтверждения почты {url}",
        #         from_email=settings.EMAIL_HOST_USER,
        #         recipient_list=[user.email],
        #     )
        #     return super().form_valid(form)
