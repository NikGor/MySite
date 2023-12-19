from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'order', 'company', 'url', 'city', 'country', 'start_date', 'end_date')
    list_filter = ('city', 'country',)
    list_editable = ('order', 'start_date', 'end_date', 'url')
    search_fields = ('job_title', 'company', 'city', 'country')
    ordering = ('-start_date',)

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Информация о работе', {'fields': ('job_title', 'company', 'url', 'description', 'order')}),
        ('Местоположение', {'fields': ('city', 'country')}),
        ('Даты', {'fields': ('start_date', 'end_date')}),
    )
