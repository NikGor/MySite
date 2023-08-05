from django.urls import path
from .views import SkillListView, SkillCreateView, SkillUpdateView, SkillDeleteView

app_name = 'skills'


urlpatterns = [
    path('', SkillListView.as_view(), name='skill_list'),
    path('new/', SkillCreateView.as_view(), name='skill_new'),
    path('<int:pk>/edit/', SkillUpdateView.as_view(), name='skill_edit'),
    path('<int:pk>/delete/', SkillDeleteView.as_view(), name='skill_delete'),
]