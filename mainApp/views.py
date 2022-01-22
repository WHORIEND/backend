import json
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from rest_framework.generics import *
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate , login,logout
from .models import *
# Create your views here.

class mainView(APIView):
    def get(self, request):
        queryset = Detail_Category.objects.all()
        serializers = DetailCategorySerializer(queryset, many=True)
        return render(request, 'mainApp/MainPage.html', {'data' : serializers.data})


class TeachableUserView(APIView):
    def get(self, request):
        queryset = User.objects.filter(teachable__detail_name__in = ['한국어']) #json형식으로 받은 카테고리만 걸러서 리턴
        #for e in queryset:
        #    print(e)
        serializers = TeachableUserSerializer(queryset, many=True)
        return Response(serializers.data)

class TeacherView(RetrieveAPIView):
    queryset = User.objects.filter(teachable__detail_name__in = ['언어']) #json형식으로 받은 카테고리만 걸러서 리턴
    serializer_class = TeacherSerializer

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # post에 포함된 정보 가져오기
        password = request.POST.get('password')
        print(email,' ',password)
        user = authenticate(email=email, password=password)
        if user is not None:
            print(1)
            login(request,user) #session 에 login 정보 저장.
            return redirect('mainApp:mainpage')
        else:
            return render(request,'mainApp/LoginPage.html')
    if request.method == 'GET':
        return render(request,'mainApp/LoginPage.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'mainApp/SignUp.html')
    if request.method == 'POST':
        email = request.POST.get('email')  # post에 포함된 정보 가져오기
        nickname = request.POST.get('nickname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        if password1 == password2:
            user = User.objects.create_user(email, "1997-07-12",nickname, password1)
            if user is not None:
                return redirect('mainApp:login')


def logout(request):
    if request.user.is_authenticated: # 로그인이 완료 됬다면.
        return Response(status=200)
    else:
        return Response(status=400)
