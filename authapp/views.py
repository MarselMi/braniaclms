from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import TemplateView
from .models import User


class CostomLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Авторизация пользователя'
    }


class CustomLogoutView(LogoutView):
    pass


class RegView(TemplateView):
    template_name = 'authapp/register.html'
    extra_context = {
        'title': 'Регистрация пользователя'
    }
    def post(self, request, *args, **kwargs):
        try:
            if all(
                    (
                        request.POST.get('username'),
                        request.POST.get('password1'),
                        request.POST.get('password2'),
                        request.POST.get('firstname'),
                        request.POST.get('lastname'),
                        request.POST.get('password1') == request.POST.get('password2'),
                    )
            ):
                new_user = User.objects.create(
                    username=request.POST.get('username'),
                    first_name=request.POST.get('firstname'),
                    last_name=request.POST.get('lastname'),
                    email=request.POST.get('email'),
                    age=request.POST.get('age') if request.POST.get('age') else 0,
                    avatar=request.POST.get('avatar')
                )
                new_user.set_password(request.POST.get('password1'))
                new_user.save()
                messages.add_message(request, messages.INFO, 'Регистрация прошла успешно')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    'В регистрации возникла ошибка'
                )
                return HttpResponseRedirect(reverse('authapp:register'))
        except Exception:
            messages.add_message(
                request,
                messages.INFO,
                'В регистрации возникла ошибка'
            )
            return HttpResponseRedirect(reverse('authapp:register'))


class EditView(TemplateView):
    template_name = 'authapp/edit.html'
    extra_context = {
        'title': 'Страница редактирования профиля'
    }
    def post(self):

