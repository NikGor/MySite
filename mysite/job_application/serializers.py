from rest_framework import serializers
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    is_remote = serializers.BooleanField(default=False)

    class Meta:
        model = JobApplication
        fields = [
            'company_name', 'job_title', 'url', 'location', 'is_remote',
            'contact_person', 'key_skills', 'soft_skills', 'salary_range',
            'language', 'german_level'
        ]


class ParseTextSerializer(serializers.Serializer):
    text = serializers.CharField()
