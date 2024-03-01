from django.contrib import admin
from scripts.utils import translate_model
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ('user', 'skill_type', 'description')
    list_filter = ('user', 'skill_type')
    search_fields = ('user', 'skill_type')
    ordering = ('user', 'skill_type')
