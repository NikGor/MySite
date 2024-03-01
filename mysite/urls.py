"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from mysite.views import IndexView, PageNotFoundView, ExportPDFView, PDFview
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.permissions import AllowAny
from django.utils.translation import override


def force_german(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        with override('de'):
            return view_func(request, *args, **kwargs)
    return _wrapped_view_func


schema_view = get_schema_view(
    openapi.Info(
        title="Job Application API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('404/', PageNotFoundView.as_view(), name='404'),
    path('export2pdf/', ExportPDFView.as_view(), name='export2pdf'),
    path('pdf/', PDFview.as_view(), name='pdf'),
    path("api/", include("mysite.job_application.urls")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('export2pdf/de/', force_german(ExportPDFView.as_view()), name='export2pdf'),
    path('pdf/de/', force_german(PDFview.as_view()), name='pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
