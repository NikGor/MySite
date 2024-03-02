chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.message === "parse_url") {
    const pageUrl = window.location.href;
    const apiUrl = `https://nikogordienko.up.railway.app/api/parse_url/?url=${encodeURIComponent(pageUrl)}`;

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        sendResponse({ data: data });
      })
      .catch(error => {
        console.error('Ошибка:', error);
        sendResponse({ error: error.message });
      });

    return true; // Для асинхронного ответа
  }
});
