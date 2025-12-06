from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mark/', views.mark, name='mark'),
    path('mark/course/', views.course, name='course'),  # 👈 nested URL
    path('mark/course/dep/', views.dep, name='dep'),  # 👈 nested URL
    path('mark/course/dep/building/', views.building, name='building'),  # 👈 nested URL

]
