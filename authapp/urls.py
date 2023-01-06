from .apps import AuthappConfig
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, ProfileEditView


app_name = AuthappConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/<str:pk>/', ProfileEditView.as_view(), name='edit')
]