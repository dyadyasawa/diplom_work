from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserDeleteApiView,
    UserDetailApiView,
    UserListApiView,
    UserUpdateApiView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("list/", UserListApiView.as_view(), name="list"),
    path("detail/<int:pk>/", UserDetailApiView.as_view(), name="detail"),
    path("update/<int:pk>/", UserUpdateApiView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDeleteApiView.as_view(), name="delete"),
]
