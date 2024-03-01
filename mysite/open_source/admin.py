from django.contrib import admin
from scripts.utils import translate_model
from .models import OpenSourceProject
from django.utils.html import format_html


@admin.register(OpenSourceProject)
class OpenSourceProjectAdmin(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ('user', 'job_title', 'name', 'start_date', 'end_date', 'url', 'github_url')
    list_editable = ('start_date', 'end_date', 'url', 'github_url')
    ordering = ('-start_date',)

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Project Information', {'fields': ('job_title', 'name', 'description', 'url', 'github_url', 'screenshot_url')}),
        ('Date', {'fields': ('start_date', 'end_date')}),
        ('Translatable', {'fields': ('job_title_de', 'name_de', 'description_de')}),
    )

    def github_link(self, obj):
        if obj.github_url:
            return format_html('<a href="{}" target="_blank">GitHub</a>', obj.github_url)
        return "N/A"

    github_link.short_description = 'GitHub URL'

    def project_link(self, obj):
        if obj.url:
            return format_html('<a href="{}" target="_blank">Project</a>', obj.url)
        return "N/A"

    def screenshot_link(self, obj):
        if obj.screenshot_url:
            return format_html('<a href="{}" target="_blank">Screenshot</a>', obj.screenshot_url)
        return "N/A"

    project_link.short_description = 'Project URL'
