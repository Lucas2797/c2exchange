from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from accounts.serializers import ProfileSerializer
from typing import ClassVar
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import Investiment, Profile, Wallet
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout, login
from .decorators import already_authenticated_user, allowed_users



class LoginView(APIView):
    template_name = 'login.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("xabu")

def logout_view(request):
    logout(request)
    return redirect('home')


class RegisterView(APIView):
    template_name = 'register.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            user.login()
            return redirect('home')
        else:
            return HttpResponse("xabu")
        
class ProfileView(APIView):
    template_name = 'profile.html'

    def get(self,request, pk):
        p1 = Profile.objects.get(id=pk)
        if request.user.is_authenticated and request.user == p1.user:
            seri_obj = ProfileSerializer(p1)
            query = Investiment.objects.filter(wallet__one=p1)
            context = {
                'p1': p1,
                'query': query
            }
            return render(request, self.template_name, context)
        else:
            raise ValidationError("nao e o dono do perfil")




