// Для каждого элемента аккордеона
$('.accordion .accordion-item').each(function() {
  // Получить аккордеон
  var $accordion = $(this);

  // Закрыть аккордеон при загрузке страницы
  var $accordionCollapse = $accordion.find('.collapse');
  $accordionCollapse.collapse('hide');

  // Добавить слушатель событий на элемент аккордеона
  $accordion.on('click', function() {
    // Развернуть или свернуть аккордеон
    $accordionCollapse.collapse('toggle');
  });
});

$(document).ready(function() {
  $(".show-more-link").on("click", function() {
      var shortText = $(this).prevAll(".text-short");
      var fullText = $(this).prevAll(".text-full");

      if(fullText.is(":hidden")){
          shortText.hide();
          fullText.show();
          $(this).text("less");
      } else {
          fullText.hide();
          shortText.show();
          $(this).text("...more");
      }
  });
});

function showEmail() {
  document.getElementById('email').style.display = 'block';
}
