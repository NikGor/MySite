from django.urls import path
from .views import UserView, UpdateUserView

app_name = 'users'

urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('<int:pk>/update/', UpdateUserView.as_view(), name='update_user'),
]
