
# from config import settings
# from users.forms import UserRegisterForm
from rest_framework.generics import CreateAPIView

from users.models import User
# from django.views.generic import CreateView, TemplateView, ListView, UpdateView
# from django.core.mail import send_mail
# from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
# from django.shortcuts import get_object_or_404, redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy, reverse
# import secrets

from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
# class UserCreateView(CreateView):  # LoginRequiredMixin,
#     model = User
#     template_name = "users_app/user_form.html"
#     form_class = UserRegisterForm
#     success_url = reverse_lazy("users:register_message")
#
#     def form_valid(self, form):
#         user = form.save()
#         user.is_active = False
#         token = secrets.token_hex(8)
#         user.token = token
#         user.save()
#         host = self.request.get_host()
#         url = f"http://{host}/users/email_confirm/{token}/"
#
#         send_mail(
#             subject="Подтверждение почты",
#             message=f"Перейдите по ссылке для подтверждения почты {url}",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[user.email],
#         )
#         return super().form_valid(form)
#
#
# class RegisterMessageView(TemplateView):
#     template_name = "users_app/register_message.html"
#
#
# def email_verification(request, token):
#     user = get_object_or_404(User, token=token)
#     user.is_active = True
#     user.save()
#     return HttpResponseRedirect("/users/login/")
