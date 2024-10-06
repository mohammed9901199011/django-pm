
from django.urls import path , include
from . import views
from .views import ProjectListView
urlpatterns = [
    path('',views.ProjectListView.as_view(), name = 'project_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='project_create')
]
