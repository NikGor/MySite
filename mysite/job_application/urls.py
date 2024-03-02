from django.urls import path
from mysite.job_application.views import ParseURLView, ParseTextView

urlpatterns = [
    path('parse_url/', ParseURLView.as_view(), name='parse_url'),
    path('parse_text/', ParseTextView.as_view(), name='parse_text'),
]
