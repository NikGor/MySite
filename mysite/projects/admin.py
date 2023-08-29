from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_visible', 'github_link', 'project_link', 'screenshot_url')
    list_filter = ('is_visible',)
    search_fields = ('name', 'description')
    ordering = ('order',)
    list_editable = ('order', 'is_visible', 'screenshot_url')

    def github_link(self, obj):
        if obj.github_url:
            return format_html('<a href="{}" target="_blank">GitHub</a>', obj.github_url)
        return "N/A"

    github_link.short_description = 'GitHub URL'

    def project_link(self, obj):
        if obj.url:
            return format_html('<a href="{}" target="_blank">Project</a>', obj.url)
        return "N/A"

    project_link.short_description = 'Project URL'
