chrome.browserAction.onClicked.addListener(function(tab) {
  // Получите URL текущей вкладки и отправьте его в ваше API для парсинга
  const apiUrl = 'http://127.0.0.1:8000/api/parse_url/';
  fetch(apiUrl + '?url=' + encodeURIComponent(tab.url))
    .then(response => response.json())
    .then(data => {
      console.log('Data received:', data);
      // Действия с полученными данными
    })
    .catch(error => console.error('Error:', error));
});
