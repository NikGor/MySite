import os
from dotenv import load_dotenv
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mysite.job_application.parser import parse_url
from mysite.job_application.serializers import JobApplicationSerializer


class ParseURLView(APIView):
    """
    Обработчик запросов для парсинга URL.
    """
    @swagger_auto_schema(
        operation_description="Получить данные по заданному URL",
        query_serializer=JobApplicationSerializer,
    )
    def get(self, request, *args, **kwargs):
        # Загрузка переменных окружения
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        model_id = os.getenv("OPENAI_ASSISTANT_ID")

        url = request.GET.get('url', '')
        if not url:
            return Response({'error': 'No URL provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Передача api_key и model_id в функцию parse_url
        result = parse_url(url, model_id, api_key)
        return Response(result, status=status.HTTP_200_OK)
