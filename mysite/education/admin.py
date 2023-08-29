from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'faculty', 'start_date', 'end_date')
    list_filter = ('school', 'faculty', 'start_date')
    search_fields = ('school', 'faculty')
    ordering = ('-start_date',)

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Education Information', {'fields': ('school', 'faculty', 'description')}),
        ('Date', {'fields': ('start_date', 'end_date')}),
    )
