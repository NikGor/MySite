from django.urls import path
from .views import ExperienceListView, ExperienceCreateView, ExperienceUpdateView, ExperienceDeleteView

app_name = 'experience'

urlpatterns = [
    path('', ExperienceListView.as_view(), name='experience_list'),
    path('new/', ExperienceCreateView.as_view(), name='experience_new'),
    path('<int:pk>/edit/', ExperienceUpdateView.as_view(), name='experience_edit'),
    path('<int:pk>/delete/', ExperienceDeleteView.as_view(), name='experience_delete'),
]
