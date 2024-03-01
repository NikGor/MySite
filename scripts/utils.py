import os
import requests
from openai import OpenAI
from modeltranslation.translator import translator
from django.conf import settings
from django.db.models.fields import CharField, TextField


def translate_model(modeladmin, request, queryset):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    for obj in queryset:
        translation_opts = translator.get_options_for_model(obj.__class__)

        for field_name in translation_opts.fields.keys():
            field_object = obj._meta.get_field(field_name)

            if isinstance(field_object, (CharField, TextField)):
                source_value = getattr(obj, field_name, None)
                if source_value:
                    for lang_code, lang_name in settings.LANGUAGES:
                        if lang_code == settings.LANGUAGE_CODE:
                            continue

                        response = client.completions.create(model="gpt-3.5-turbo-instruct",
                                                             prompt=f"Please translate this to {lang_name}: {source_value}",
                                                             temperature=0.5,
                                                             max_tokens=1500,
                                                             top_p=1,
                                                             frequency_penalty=0,
                                                             presence_penalty=0)
                        translated_text = response.choices[0].text.strip()
                        translated_field_name = f'{field_name}_{lang_code}'
                        setattr(obj, translated_field_name, translated_text)

        obj.save()


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
                "url": url_to_capture,
                "accept-language": "en"
            }
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                screenshot_filename = f"{project.id}_{project.name}.png"
                screenshot_path = os.path.join(screenshot_folder, screenshot_filename)
                with open(screenshot_path, "wb") as f:
                    f.write(response.content)
                project.screenshot_url = f'/screenshots/{screenshot_filename}'
                project.save()
