
from django.urls import path
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import

from materials.apps import MaterialsConfig
from materials.views import StartPageView

app_name = MaterialsConfig.name

urlpatterns = [
    path("", StartPageView.as_view(), name="start_page"),
]
