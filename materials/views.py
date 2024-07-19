
from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class StartPageView(TemplateView):
    template_name = "materials_app/start_page.html"
