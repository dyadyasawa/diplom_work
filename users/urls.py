
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LoginView, LogoutView
# from users.forms import LoginCustomForm
from users.apps import UsersConfig
# from users.views import UserCreateView, email_verification, RegisterMessageView
from users.views import UserCreateAPIView, UserListApiView, UserDetailApiView, UserUpdateApiView, UserDeleteApiView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login",),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh",),

    path("list/", UserListApiView.as_view(), name="list"),
    path("detail/<int:pk>/", UserDetailApiView.as_view(), name="detail"),
    path("update/<int:pk>/", UserUpdateApiView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDeleteApiView.as_view(), name="delete"),

    # path("login/", LoginView.as_view(template_name="users_app/login.html", form_class=LoginCustomForm), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    # path("register/", UserCreateView.as_view(), name="register"),
    # path("email_confirm/<str:token>/", email_verification, name="email_confirm"),
    # path('register/email_confirm/<str:token>/', email_verification, name='email_confirm'),
    # path("register_message/", RegisterMessageView.as_view(), name="register_message"),

    # path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
    # # path('password_recovery/create_new_password/<str:code>', create_new_password, name='create_new_password'),
    # path('password_recovery/message/', PasswordRecoveryMessageView.as_view(), name='recovery_message'),

    # path("users_list/", UserListView.as_view(), name="users_list"),
    # path("update_user/<int:pk>/", UserUpdateView.as_view(), name="update_user")
]

