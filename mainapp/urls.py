from django.urls import path
from . import views
from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('news/', views.NewsPageView.as_view(), name='news'),
    path('news/<pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('courses/', views.CoursesPageView.as_view(), name='courses'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts'),
    path('doc_site/', views.DocSitePageView.as_view(), name='doc_site'),
    path('login/', views.LoginPageView.as_view(), name='login'),
]