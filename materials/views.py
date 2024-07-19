
# from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from materials.models import Course, Lesson


class StartPageView(TemplateView):
    template_name = "materials_app/start_page.html"


class CoursesListView(ListView):
    model = Course
    template_name = "materials_app/courses_list.html"


class CourseDetailView(ListView):
    model = Course
    template_name = "materials_app/course_detail.html"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        c = Course.objects.get(pk=self.kwargs.get('pk'))

        queryset = c.lesson_set.all()

        return queryset
