from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import MultilingualUser
from user.serializers import MultilingualUserSerializer


@api_view(['GET'])
def user_list_api(request):
    comments = MultilingualUser.objects.all()
    serializer = MultilingualUserSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login_api(request):
    user = authenticate(username=request.data['username'], password=request.data['password'])
    if user is not None:
        login(request, user)
        return Response("Вход выполнен.")
    else:
        return Response("Ваши логин или пароль не соответствуют.")


@api_view(['GET'])
def logout_api(request):
    logout(request)
    return Response("Выход выполнен.")
