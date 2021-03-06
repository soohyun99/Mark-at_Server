from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from server.serializers import *
from knox.models import AuthToken
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend
from server.filter import *
from server.models import *
from rest_framework import views
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views import View
from django.http import JsonResponse

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
#    if Login.objects.filter(id=id).exists():
#        account = Login.objects.get(id=id)
#        if account.pw == pw:
#            return JsonResponse({'message': 'Login SUCCESS'}, status=200)
#        return HttpResponse(status=401)


class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        Login(
            id     = data['id'],
            pw    = data['pw'],
            email = data['email'],
            nickname = data['nickname']
        )
        if Login.objects.filter(id = data['id']).exists() == True:
            return JsonResponse({"message" : "0"}, status = 401)
        else:
            Login.objects.create(id = data['id'], nickname = data['nickname'], pw = data['pw'], email = data['email'])
            return JsonResponse({"message" : "1"}, status = 200)

    def get(self, request):
        login = Login.objects.values()
        return JsonResponse({"data": list(login)}, status=200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        Login(
            id=data['id'],
            pw=data['pw']
        )
        if Login.objects.filter(id = data['id'], pw = data['pw']).exists() == True :
            return JsonResponse({"message": "1"}, status = 200)
        else:
            return JsonResponse({"message" : "0"}, status = 401)

    def get(self, request):
        login = Login.objects.values()
        return JsonResponse({"list" : list(login)}, status = 200)

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class BigmarketViewSet(viewsets.ModelViewSet):
    queryset = Bigmarket.objects.all()
    serializer_class = BigmarketSerializer

