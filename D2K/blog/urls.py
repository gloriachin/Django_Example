from django.urls import path

from . import views

app_name = 'blog'



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.SubtitleView.as_view(), name='directory'),
    path('title/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('paragraph/<int:sub_id>/', views.ParagraphView.as_view(), name='paragraph'),

]