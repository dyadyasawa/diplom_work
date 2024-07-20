
from django.urls import path
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import

from materials.apps import MaterialsConfig
# from materials.views import StartPageView, CoursesListView, CourseDetailView
from materials.views import (
    CourseListApiView,
    CourseDetailApiView,
    CourseCreateApiView,
    CourseUpdateApiView,
    CourseDestroyApiView,
)

app_name = MaterialsConfig.name

urlpatterns = [
    # path("", StartPageView.as_view(), name="start_page"),

    # path("courses_list/", CoursesListView.as_view(), name="courses_list"),
    # path("course_detail/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),


    path("course_list/", CourseListApiView.as_view(), name="course_list"),
    path("course_detail/<int:pk>/", CourseDetailApiView.as_view(),  name="course_detail"),
    path("course_create/", CourseCreateApiView.as_view(), name="course_create"),
    path("course_update/<int:pk>/", CourseUpdateApiView.as_view(), name="course_update"),
    path("course_delete/<int:pk>/", CourseDestroyApiView.as_view(), name="course_delete"),

    path("lesson_list/", CourseListApiView.as_view(), name="lesson_list"),
    path("lesson_detail/<int:pk>/", CourseDetailApiView.as_view(), name="lesson_detail"),
    path("lesson_create/", CourseCreateApiView.as_view(), name="lesson_create"),
    path("lesson_update/<int:pk>/", CourseUpdateApiView.as_view(), name="lesson_update"),
    path("lesson_delete/<int:pk>/", CourseDestroyApiView.as_view(), name="lesson_delete"),
]

