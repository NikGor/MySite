from modeltranslation.translator import register, TranslationOptions
from mysite.education.models import Education
from mysite.experience.models import Experience
from mysite.open_source.models import OpenSourceProject
from mysite.projects.models import Project
from mysite.skills.models import Skill
from mysite.user.models import User


@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('job_title', 'about_me')


@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('school', 'faculty', 'description')


@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('company', 'job_title', 'description')


@register(OpenSourceProject)
class OpenSourceProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'job_title', 'description')


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('skill_type', 'description')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
