from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
]


