from django.urls import path
from .views import EducationListView, EducationCreateView, EducationUpdateView, EducationDeleteView

app_name = 'education'

urlpatterns = [
    path('', EducationListView.as_view(), name='education_list'),
    path('new/', EducationCreateView.as_view(), name='education_new'),
    path('<int:pk>/edit/', EducationUpdateView.as_view(), name='education_edit'),
    path('<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
]