
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from users.models import User

from users.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class UserCreateAPIView(CreateAPIView):
    """ Создание пользователя. """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListApiView(ListAPIView):
    """ Просмотр списка пользователей. """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserDetailApiView(RetrieveAPIView):
    """ Просмотр выбранного пользователя. """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserUpdateApiView(UpdateAPIView):
    """ Редактирование пользователя. """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserDeleteApiView(DestroyAPIView):
    """ Удаление пользователя. """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
