from django.urls import path
from mysite.job_application.views import ParseURLView

urlpatterns = [
    path('parse_url/', ParseURLView.as_view(), name='parse_url'),
]
