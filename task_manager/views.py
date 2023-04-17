from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')