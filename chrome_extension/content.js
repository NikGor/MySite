// content.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.message === "parse_url") {
    // Получаем URL текущей вкладки
    const pageUrl = window.location.href;

    // Здесь ваш API endpoint
    const apiUrl = `http://127.0.0.1:8000/api/parse_url/?url=${encodeURIComponent(pageUrl)}`;

    // Отправляем запрос к вашему API
    fetch(apiUrl)
      .then(response => {
        if (response.ok) {
          return response.json(); // или response.text() если ожидается не JSON
        }
        throw new Error('Ошибка запроса к API');
      })
      .then(data => {
        // Тут обработка полученных данных
        console.log(data);
        sendResponse({ data: data });
      })
      .catch(error => {
        console.error('Ошибка:', error);
        sendResponse({ error: error.message });
      });
  }

  // Важно: вернуть true, чтобы указать, что ответ будет асинхронным
  return true;
});
