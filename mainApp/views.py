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
from django.contrib.auth import authenticate
from .models import *
# Create your views here.

def test(request):
    return render(request, 'mainApp/LoginPage.html')

class mainView(APIView):
    def get(self, request):
        queryset = Detail_Category.objects.all()
        serializers = DetailCategorySerializer(queryset, many=True)
        return Response(serializers.data)


class TeachableUserView(APIView):
    def get(self, request):
        queryset = User.objects.filter(teachable__detail_name__in = ['한국어']) #json형식으로 받은 카테고리만 걸러서 리턴
        #for e in queryset:
        #    print(e)
        serializers = TeachableUserSerializer(queryset, many=True)
        return Response(serializers.data)

class TeacherView(RetrieveAPIView):
    #queryset = User.objects.filter(teachable__detail_name__in = ['언어']) #json형식으로 받은 카테고리만 걸러서 리턴
    queryset = User.objects.all()
    serializer_class = TeacherSerializer

    def get_context_data(self, **kwargs):
        print(self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context[self.kwargs['pk']] = User.objects.filter(teachable__deatil_name = self.kwargs['pk'])
        return context
    
class ProfileView(APIView):
    def get(self, request):
        querset = User.objects.all()
        serializers = ProfileSerializer(querset, many = True)
        return Response(serializers.data)

def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        email = data['email']
        password = data['password']
        user = authenticate(email='ata97@naver.com', password='1234')
        if user is not None:
            print(1)
            login(request, user) #session 에 login 정보 저장.
            serializers = BasicUserSerializer(user)
            return redirect('language/', serializers.data)
               # Redirect(serializers.data, status=200)
        else:
            return Http404("Question does not exist")
    if request.method == 'GET':
        user = User.objects.filter(email='junic@naver.com')
        serializers = BasicUserSerializer(user)
        redirect('언어/', serializers.data)
    user = User.objects.filter(email='junic@naver.com')
    serializers = BasicUserSerializer(user)
    return redirect('mainApp:language')



def logout(request):
    if request.user.is_authenticated: # 로그인이 완료 됬다면.
        return Response(status=200)
    else:
        return Response(status=400)
