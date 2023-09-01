from django.contrib import admin
from .models import JobApplication


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company_name', 'job_title', 'location', 'date_added', 'responded',
        'response_received', 'phone_interview_invited', 'phone_interview_date',
        'phone_interview_done', 'onsite_interview_invited', 'onsite_interview_date',
        'onsite_interview_done', 'contact_person', 'status', 'final_decision'
    )
    list_editable = (
        'responded', 'response_received', 'phone_interview_invited', 'phone_interview_date',
        'phone_interview_done', 'onsite_interview_invited', 'onsite_interview_date',
        'onsite_interview_done', 'status', 'final_decision'
    )
    search_fields = ('company_name',)
    list_filter = (
        'responded', 'response_received', 'phone_interview_invited',
        'phone_interview_done', 'onsite_interview_invited', 'onsite_interview_done',
        'status', 'final_decision'
    )


admin.site.register(JobApplication, JobApplicationAdmin)
