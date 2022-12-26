from .apps import AuthappConfig
from django.urls import path
from .views import CostomLoginView, LogoutView, RegView, EditView


app_name = AuthappConfig.name

urlpatterns = [
    path('login/', CostomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegView.as_view(), name='register'),
    path('edit/', EditView.as_view(), name='edit')
]