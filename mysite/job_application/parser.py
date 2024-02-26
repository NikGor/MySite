import json
import time
from langdetect import detect
import requests
import newspaper
import openai
from bs4 import BeautifulSoup


def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
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


def parse_url(url, model_id, api_key):
    """
    Функция для отправки запроса к ассистенту OpenAI и возвращения ответа.

    Аргументы:
    prompt_text (str): Текст запроса к модели.
    model_id (str): Идентификатор модели ассистента.
    api_key (str): API ключ для доступа к OpenAI.

    Возвращает:
    dict: Список текстов ответов от ассистента.
    """

    prompt_text = get_job_text(url)

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

    # Получите ответы ассистента
    messages = client.beta.threads.messages.list(thread_id=thread.id, order="asc")
    responses = [message.content[0].text.value for message in messages.data if message.role == "assistant"]
    result = json.loads(responses[0])
    result['url'] = url
    return result


if __name__ == "__main__":
    url = "https://jobs.siegenia.com/job/Wilnsdorf-Software-Entwickler-%2528mwd%2529-57234/997024201/?src=LinkedIn"
    print(get_job_text(url))
