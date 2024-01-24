from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from weasyprint import HTML


class IndexView(View):
    def get(self, request):
        user = get_user_model().objects.first()
        experiences = user.experience_set.all().order_by('order')
        educations = user.education_set.all().order_by('order')
        skills = user.skill_set.all()
        projects = user.project_set.filter(is_visible=True).order_by('order')
        open_source_projects = user.opensourceproject_set.all()
        print(projects.query)  # Вывод SQL-запроса
        print(projects)  # Вывод содержимого QuerySet
        return render(request, 'index.html', {'user': user,
                                              'experiences': experiences,
                                              'educations': educations,
                                              'skills': skills,
                                              'projects': projects,
                                              'open_source_projects': open_source_projects})


class PageNotFoundView(View):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, status=404)


class ExportPDFView(View):
    template_name = 'pdf/pdf_template.html'

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.first()
        experiences = user.experience_set.all().order_by('order')
        educations = user.education_set.all().order_by('order')
        skills = user.skill_set.all()
        projects = user.project_set.all().order_by('order')
        open_source_projects = user.opensourceproject_set.all()
        context = {
            'user': user,
            'experiences': experiences,
            'educations': educations,
            'skills': skills,
            'projects': projects,
            'open_source_projects': open_source_projects
        }

        # Render HTML content
        html_string = render_to_string(self.template_name, context)

        # Convert the HTML string to a PDF using WeasyPrint
        pdf = HTML(string=html_string).write_pdf()

        # Create a HttpResponse object with the PDF and correct MIME type
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="NikolaiGordienko_CV.pdf"'

        return response


class PDFview(LoginRequiredMixin, View):
    def get(self, request):
        user = get_user_model().objects.first()
        experiences = user.experience_set.all()
        educations = user.education_set.all()
        skills = user.skill_set.all()
        projects = user.project_set.all()
        open_source_projects = user.opensourceproject_set.all()
        context = {'user': user,
                   'experiences': experiences,
                   'educations': educations,
                   'skills': skills,
                   'projects': projects,
                   'open_source_projects': open_source_projects}
        return render(request, 'pdf/pdf_template.html', context)
