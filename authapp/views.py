from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'authapp/login.html'


class LogoutView(TemplateView):
    pass


class RegView(TemplateView):
    template_name = 'authapp/register.html'


class EditView(TemplateView):
    pass
