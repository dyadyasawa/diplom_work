from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import (CourseCreateApiView, CourseDestroyApiView,
                             CourseDetailApiView, CourseListApiView,
                             CourseUpdateApiView, LessonCreateApiView,
                             LessonDestroyApiView, LessonDetailApiView,
                             LessonListApiView, LessonUpdateApiView,
                             SendContent)

app_name = MaterialsConfig.name

urlpatterns = [
    path("course/list/", CourseListApiView.as_view(), name="course_list"),
    path(
        "course/detail/<int:pk>/", CourseDetailApiView.as_view(), name="course_detail"
    ),
    path("course/create/", CourseCreateApiView.as_view(), name="course_create"),
    path(
        "course/update/<int:pk>/", CourseUpdateApiView.as_view(), name="course_update"
    ),
    path(
        "course/delete/<int:pk>/", CourseDestroyApiView.as_view(), name="course_delete"
    ),
    path("lesson/list/", LessonListApiView.as_view(), name="lesson_list"),
    path(
        "lesson/detail/<int:pk>/", LessonDetailApiView.as_view(), name="lesson_detail"
    ),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateApiView.as_view(), name="lesson_update"
    ),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
    path(
        "send/content/<int:lesson_pk>/<int:user_pk>/",
        SendContent.as_view(),
        name="send_content",
    ),
]
