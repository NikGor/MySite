from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name = 'projects'


urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('new/', ProjectCreateView.as_view(), name='project_new'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]
