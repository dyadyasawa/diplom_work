
from django.urls import path
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import

from materials.apps import MaterialsConfig
from materials.views import StartPageView, CoursesListView, CourseDetailView

app_name = MaterialsConfig.name

urlpatterns = [
    path("", StartPageView.as_view(), name="start_page"),

    path("courses_list/", CoursesListView.as_view(), name="courses_list"),
    path("course_detail/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
]
