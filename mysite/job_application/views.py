import json
import os
import django
from django.http import JsonResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mysite.job_application.models import JobApplication
from mysite.job_application.parser import get_job_text, get_openai_response, process_json, get_cover_letter, \
    get_cv_intro
from mysite.job_application.serializers import JobApplicationSerializer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import get_user_model  # noqa: E402


class ParseURLView(APIView):
    """
    Обработчик запросов для парсинга URL.
    """

    @swagger_auto_schema(operation_description="Получить данные по заданному URL", query_serializer=JobApplicationSerializer)
    def get(self, request, *args, **kwargs):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        model_id = os.getenv("OPENAI_ASSISTANT_ID")

        url = request.GET.get('url', '')
        if not url:
            return Response({'error': 'No URL provided'}, status=status.HTTP_400_BAD_REQUEST)

        prompt_text = get_job_text(url)
        response = get_openai_response(prompt_text, model_id, api_key)
        result = process_json(response)

        if 'error' in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        company_name = result.get('company_name', '')
        job_title = result.get('job_title', '')
        contact_person = result.get('contact_person', '')
        key_skills = ', '.join(result.get('skills', []))
        soft_skills = ', '.join(result.get('soft_skills', []))
        language = result.get('language', '')

        user = get_user_model().objects.first()
        field_name = f'about_me_{language}'
        cv_intro_sample = getattr(user, field_name)
        cover_letter_sample = getattr(user, 'cover_letter_sample')

        cv_intro = get_cv_intro(api_key, cv_intro_sample, language, key_skills, soft_skills)
        cover_letter = get_cover_letter(api_key, job_title, company_name,
                                        cover_letter_sample, language, key_skills,
                                        soft_skills, contact_person)

        # Создание нового объекта JobApplication с полученными данными
        job_application = JobApplication(
            company_name=company_name,
            job_title=job_title,
            url=url,
            location=', '.join(result.get('location', [])),
            is_remote=result.get('is_remote', False),
            contact_person=contact_person,
            date_added=timezone.now(),
            key_skills=key_skills,
            soft_skills=soft_skills,
            required_experience=result.get('required_experience', ''),
            salary_range=result.get('salary_range', ''),
            vacation_days=result.get('vacation_days', ''),
            other_benefits='\n'.join(['- ' + benefit for benefit in result.get('other_benefits', [])]),
            minuses='\n'.join(['- ' + minus for minus in result.get('minuses', [])]),
            language=language,
            german_level=result.get('german', ''),
            cover_letter=cover_letter,
            cv_intro=cv_intro,
            info=result.get('info', ''),
            # Добавьте другие поля при необходимости
        )
        job_application.save()

        # Добавляем статус 'success' к result
        result['status'] = 'success'

        return Response(result, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class ParseTextView(View):
    """
    Обработчик запросов для парсинга текста.
    """

    def post(self, request, *args, **kwargs):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        model_id = os.getenv("OPENAI_ASSISTANT_ID")

        # Изменяем получение данных: вместо URL из параметров, берем текст из тела запроса
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        prompt_text = body.get('text', '')

        if not prompt_text:
            return JsonResponse({'error': 'No text provided'}, status=400)

        # Используем тот же метод parse_url
        response = get_openai_response(prompt_text, model_id, api_key)
        result = process_json(response)

        if 'error' in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        company_name = result.get('company_name', '')
        job_title = result.get('job_title', '')
        contact_person = result.get('contact_person', '')
        key_skills = ', '.join(result.get('skills', []))
        soft_skills = ', '.join(result.get('soft_skills', []))
        language = result.get('language', '')

        user = get_user_model().objects.first()
        field_name = f'about_me_{language}'
        cv_intro_sample = getattr(user, field_name)
        cover_letter_sample = getattr(user, 'cover_letter_sample')

        cv_intro = get_cv_intro(api_key, cv_intro_sample, language, key_skills, soft_skills)
        cover_letter = get_cover_letter(api_key, job_title, company_name,
                                        cover_letter_sample, language, key_skills,
                                        soft_skills, contact_person)

        # Создание нового объекта JobApplication с полученными данными
        job_application = JobApplication(
            company_name=company_name,
            job_title=job_title,
            location=', '.join(result.get('location', [])),
            is_remote=result.get('is_remote', False),
            contact_person=contact_person,
            date_added=timezone.now(),
            key_skills=key_skills,
            soft_skills=soft_skills,
            required_experience=result.get('required_experience', ''),
            salary_range=result.get('salary_range', ''),
            vacation_days=result.get('vacation_days', ''),
            other_benefits='\n'.join(['- ' + benefit for benefit in result.get('other_benefits', [])]),
            minuses='\n'.join(['- ' + minus for minus in result.get('minuses', [])]),
            language=language,
            german_level=result.get('german', ''),
            cover_letter=cover_letter,
            cv_intro=cv_intro,
            info=result.get('info', ''),
            # Добавьте другие поля при необходимости
        )
        job_application.save()

        result['status'] = 'success'
        return JsonResponse(result, status=201)
