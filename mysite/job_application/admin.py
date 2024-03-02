from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from mysite.job_application.models import JobApplication
from scripts.utils import export_cover_letter, export_cv


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    actions = [export_cover_letter, export_cv]
    list_display = (
        'id', 'date_added', 'company_link', 'job_title', 'location', 'is_remote', 'required_experience', 'salary_range',
        'response_received', 'status', 'phone_interview_date',
        'onsite_interview_date', 'contact_person',
    )
    list_editable = ('response_received', 'phone_interview_date', 'onsite_interview_date', 'status')
    search_fields = ('company_name', 'job_title')
    readonly_fields = ('date_added',)

    # Обновите определение fieldsets для организации формы редактирования.
    fieldsets = (
        (None, {'fields': ('company_name', 'job_title', 'url', 'location', 'is_remote', 'language', 'german_level')}),
        ('Details', {
            'fields': (
                'key_skills', 'soft_skills', 'cover_letter', 'cv_intro', 'contact_person', 'salary_range', 'notes',
                'required_experience', 'vacation_days', 'other_benefits', 'minuses', 'info',
                'response_received', 'phone_interview_date', 'onsite_interview_date', 'status'
            )
        }),
    )

    def company_link(self, obj):
        link = reverse("admin:job_application_jobapplication_change", args=[obj.pk])
        return format_html('<a href="{}">{}</a>', link, obj.company_name)

    company_link.short_description = 'company_name'
