let accordionBody = document.querySelector('.accordion-body');
accordionBody.classList.add('collapsing');
// Выполнение операций раскрытия/скрытия элемента аккордеона...
accordionBody.addEventListener('transitionend', () => {
  accordionBody.classList.remove('collapsing');
});
