import json
import os
import time
from dotenv import load_dotenv
from langdetect import detect
import requests
import newspaper
import openai
from bs4 import BeautifulSoup


def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL {url}: {e}")
        return None


def is_valid_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)'  # domain...
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def get_job_text(url):
    html = get_html_content(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text(separator=' ', strip=True)


def get_job_summary(url):
    if not is_valid_url(url):
        print("Invalid URL")
        return None
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error downloading or parsing the article: {e}")
        return None


def detect_job_language(url):
    text = get_job_summary(url)
    try:
        return detect(text)
    except Exception as e:
        print(f"Error detecting language: {e}")
        return None


def get_openai_response(prompt_text, model_id, api_key):
    """
    Функция для отправки запроса к ассистенту OpenAI и возвращения обработанного ответа.

    Аргументы:
    prompt_text (str): Текст запроса к модели.
    model_id (str): Идентификатор модели ассистента.
    api_key (str): API ключ для доступа к OpenAI.
    response_handler (function): Функция для обработки ответа от модели.

    Возвращает:
    dict: Обработанный текст ответа от ассистента.
    """

    # Инициализируйте клиента с вашим API ключом
    client = openai.OpenAI(api_key=api_key)

    # Создайте поток (разговор) с ассистентом
    thread = client.beta.threads.create()

    # Отправьте ваш запрос в созданный поток
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt_text
    )

    # Запустите ассистента для обработки вашего сообщения
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=model_id
    )

    # Ожидайте завершения обработки запроса
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id).status
        if run_status == 'completed':
            break
        time.sleep(1)  # Подождите некоторое время перед следующей проверкой статуса

    # Получите ответ ассистента
    message = client.beta.threads.messages.list(thread_id=thread.id, order="asc")
    response = next((message.content[0].text.value for message in message.data if message.role == "assistant"), None)

    if response:
        return response
    else:
        # Возвращаем ошибку, если ответ отсутствует или обработчик не определен
        return {"error": "No response from the assistant or handler is not defined"}


def process_json(response):
    """
    Удаляет блоки кода Markdown из ответа.

    Аргументы:
    response (str): Ответ от ассистента.

    Возвращает:
    dict: Ответ без блоков кода Markdown.
    """
    cleaned_response = response.replace("```json", "").replace("```", "").strip()

    try:
        result = json.loads(cleaned_response)
        return result
    except json.JSONDecodeError:
        # Возвращаем ошибку, если содержимое не удалось разобрать как JSON
        return {"error": "Invalid response from the API"}


def get_cv_intro(api_key, sample, language, skills, soft_skills):
    language_map = {
        'en': 'english',
        'de': 'deutsch'
    }

    client = openai.OpenAI(api_key=api_key)

    skills_formatted = '\n'.join(skills)
    soft_skills_formatted = '\n'.join(soft_skills)

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant for individually adapting my resume to a specific job vacancy."
                           f"I provide you with a sample, "
                           # f"the wordings in it are carefully chosen, do not change them. "
                           f"But your task is to neatly insert 75% of the keywords into the text so that they are "
                           f"mentioned in my introduction. Prepare in language of the vacancy: "
                           f"{language_map[language]}.\n\nSample: {sample} "
                           f"Don't change the sample too much just exchange some words to key-words."
                           f"Don't format the text in MD, just leave the format as it is."
            },
            {
                "role": "user",
                "content": f"Key words:\nskills: {skills_formatted}\nsoft_skills: {soft_skills_formatted}"
            }
        ],
        temperature=1,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


def get_cover_letter(api_key, job_title, company_name, sample, language, skills, soft_skills, contact_person):
    language_map = {
        'en': 'english',
        'de': 'deutsch'
    }

    client = openai.OpenAI(api_key=api_key)

    skills_formatted = '\n'.join(skills)
    soft_skills_formatted = '\n'.join(soft_skills)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant for individually adapting cover letter "
                           f"to a specific job vacancy of {job_title} in {company_name}."
                           f"I provide you with a sample, "
                           # f"the wordings in it are carefully chosen, do not change them. "
                           f"But your task is to neatly insert 75% of the keywords into the text so that they are "
                           f"mentioned in my introduction. Prepare in language of the vacancy: "
                           f"{language_map[language]}.\n\nSample: {sample} "
                           # f"Don't change the sample too much just exchange some words to key-words."
                           f"if the name of the contact person is provided, then begin the letter"
                           f"with the address Dear / Sehr geehrte Mr., Ms./ Herr, Frau (choose the appropriate one) "
                           f"and the surname of the contact person. Otherwise, from a neutral "
                           f"Dear hiring team or something else. Contact Person: {contact_person} "
                           f"Don't make the letter long, 9 sentences is enough. My level in english/german is B1, "
                           f"make the letter on this level"
            },
            {
                "role": "user",
                "content": f"Key words:\nskills: {skills_formatted}\nsoft_skills: {soft_skills_formatted}"
            }
        ],
        temperature=1,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    model_id = os.getenv("OPENAI_ASSISTANT_ID")

    language = 'de'
    field_name = f'about_me_{language}'
    sample = ("Hello! I'm Nikolai, a Python developer with a solid foundation in software engineering and "
              "a keen interest in innovative software development practices.")

    skills = ["Python", "Datenbanken", "APIs"]
    soft_skills = ["teamorientiert"]

    job_title = "Python Developer"
    company_name = "Intercon Solutions GmbH IT & Engineering Experts"
    contact_person = "Vladimir Merdzic"

    cv_intro = get_cover_letter(api_key, job_title, company_name, sample, language, skills, soft_skills, contact_person)
    print(cv_intro)
