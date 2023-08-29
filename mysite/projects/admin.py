import os
from django.contrib import admin
from django.utils.html import format_html
from .models import Project
import requests


def create_screenshot(modeladmin, request, queryset):
    screenshot_folder = 'static/screenshots'

    # Создать папку screenshots, если она не существует
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)

    for project in queryset:
        url_to_capture = project.url if project.url else project.github_url

        if url_to_capture:
            api_url = "https://api.apiflash.com/v1/urltoimage"
            params = {
                "access_key": "d1753a1756d346b690a66246fee2d66c",
                "url": url_to_capture
            }
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                screenshot_filename = f"{project.id}_{project.name}.png"
                screenshot_path = os.path.join(screenshot_folder, screenshot_filename)
                with open(screenshot_path, "wb") as f:
                    f.write(response.content)
                project.screenshot_url = f'/screenshots/{screenshot_filename}'
                project.save()


create_screenshot.short_description = "Create screenshot using ApiFlash"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_visible', 'github_link', 'project_link', 'screenshot_link')
    list_filter = ('is_visible',)
    search_fields = ('name', 'description')
    ordering = ('order',)
    list_editable = ('order', 'is_visible')
    actions = [create_screenshot]

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
