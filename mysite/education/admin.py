from django.contrib import admin
from .models import Education
from scripts.utils import translate_model


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ('school', 'order', 'faculty', 'url', 'start_date', 'end_date')
    list_editable = ('order', 'start_date', 'end_date', 'url')
    search_fields = ('school', 'faculty')
    ordering = ('-start_date',)

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Education Information', {'fields': ('school', 'faculty', 'url', 'description', 'order')}),
        ('Date', {'fields': ('start_date', 'end_date')}),
        ('Translatable', {'fields': ('school_de', 'faculty_de', 'description_de')}),
    )
