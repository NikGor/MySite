document.getElementById('parse-btn').addEventListener('click', function() {
  var spinner = document.getElementById('loading-spinner');
  spinner.style.display = 'block';

  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "parse_url"}, function(response) {
      spinner.style.display = 'none';
    });
  });
});

document.getElementById('text-parse-btn').addEventListener('click', function() {
  var spinner = document.getElementById('loading-spinner');
  spinner.style.display = 'block';

  chrome.tabs.executeScript({
    code: 'window.getSelection().toString();'
  }, function(selection) {
    var selectedText = selection[0];
    if (selectedText) {
      fetch(`https://nikogordienko.up.railway.app/api/parse_text/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: selectedText})
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        spinner.style.display = 'none';
        // Обработайте ответ, например, показать результат в интерфейсе расширения
      })
      .catch(error => {
        console.error('Error Status:', response.status);
        console.error('Ошибка:', error);
        spinner.style.display = 'none';
        // Обработайте ошибку
      });
    } else {
      spinner.style.display = 'none';
      alert('Please select the text you want to parse.');
    }
  });
});
